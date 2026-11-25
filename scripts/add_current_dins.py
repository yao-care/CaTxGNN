#!/usr/bin/env python3
"""依原收集規則補收 DPD 現行清單有、證據包沒收的本藥 DIN（2026-11-25 第六輪，用戶決定；全程不用 AI）。

問題：證據包的 DIN 是 collectors/cafda.py（LocalFDACollector）收的：藥名 → data/processed/drug_mapping.csv 的
「標準化成分 → DrugBank ID」→ 同一個 ID 的 DIN → data/raw/drug.txt 等（2026-03 DPD 萃取檔 allfiles，人用）那一列；
最多存 20 筆（單方在前），total_matches 是全部筆數；對照完全對不到時退回比對成分欄文字（_text_match）。
2026-03 之後才上市的 DIN 不在 drug_mapping、也不在 2026-03 萃取檔，每週排程只更新既有 DIN 的狀態，永遠收不進來。

收集規則：證據包收集的時間不同、用到的 drug_mapping 也不同——2026-10-12 rescue_mapping 補救之前收的照
drug_mapping.csv.bak_20261012（那一版 DIN 前導 0 被吃掉，loader 2026-10-12 修好；這裡補回 8 位數比對），之後收的照現行
drug_mapping.csv。每個證據包第一次跑時，照兩份對照分別在 2026-03 萃取檔重算一次原收集器的結果（同 cafda.matches，扣掉排除表），
張數正好等於 total_matches、而且證據包現有紀錄都在裡面的那份就是它的收集規則（兩份都對用現行），記在 tfda.collection_rule；
當時算進 total_matches 卻因 20 筆上限沒存的 DIN 回填到 tfda.records_not_stored（避免重複計數）。重算不出來的證據包整個不補（停損）。

補收（只加不刪、可重複執行）：DPD 現行清單（license_adapter.fetch() 存的 data/raw/dpd_current_status.json；照原收集範圍只取
allfiles＝上市中的人用藥）裡不在 2026-03 萃取檔的 DIN：
- 成分照 loader 的寫法（INGREDIENT 去重排序、以「; 」連接）；同一個原始成分字串在該份 drug_mapping 出現過就沿用它的 DrugBank ID
  （當時對不到的照舊不收）；沒見過的字串照 map_fda_drugs_to_drugbank 同一套逐成分（get_all_synonyms）對：成分名在該份
  drug_mapping 的標準化成分出現過就沿用（含現行版 rescue 補救的對照），否則用 mapping/drugbank_mapper 對 drugbank_vocab；
- 對到的 DrugBank ID 跟本藥（收集器用 inn 查到的 ID）相交就收；文字比對模式的證據包照 cafda._text_match 比成分欄；
- 排除表（config/bundle_record_exclusions.json）判定為另一個有效成分的不收；records、records_not_stored、excluded_records、excluded_ids 有的不重收。
records 未滿 20 筆存進 records（單方在前），滿了只記號碼在 records_not_stored；都算進 total_matches。每筆記 source、added；狀態照現行清單。

用法（repo 根目錄）：python3 scripts/add_current_dins.py [--download] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑（下載失敗不擋排程）。
"""
import copy
import csv
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as A  # noqa: E402

BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data" / A.RAW_FILE
MAPS = {"drug_mapping.csv": ROOT / "data/processed/drug_mapping.csv",
        "drug_mapping.csv.bak_20261012": ROOT / "data/processed/drug_mapping.csv.bak_20261012"}
CUR = "drug_mapping.csv"
CAP = 20
MIN_CURRENT = 30000
csv.field_size_limit(10**9)


def ing_str(r):
    """同 data/loader.load_fda_drugs：INGREDIENT 去重排序、以「; 」連接"""
    return "; ".join(sorted({str(i).strip() for i in r.get("ingredients") or [] if str(i).strip()}))


def ncomp(s):
    return len(re.split(r"[,;+/&]|&&| and | y | e | und | et ", s or "x"))


class Rule:
    """一份 drug_mapping 對照下的原收集器（cafda.LocalFDACollector 換掉對照表）"""

    def __init__(self, base, path, pad):
        from catxgnn.collectors.cafda import _key, _norm
        self.c = c = copy.copy(base)
        c.ing_to_db, c.db_to_lic = {}, {}
        self.orig = {}  # 原始主成分字串 → DrugBank ID（failed 的列記成空集合）
        self.std = {}   # 標準化成分（_norm）→ DrugBank ID
        self.dins = set()
        with open(path, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                lic = str(row.get("許可證字號") or "").strip()
                if pad and lic.isdigit():
                    lic = lic.zfill(8)
                self.dins.add(lic)
                o = str(row.get("原始主成分") or "").strip().upper()
                self.orig.setdefault(o, set())
                db = str(row.get("drugbank_id") or "").strip().upper()
                if not db or str(row.get("映射成功")).strip().lower() not in ("true", "1", "yes"):
                    continue
                self.orig[o].add(db)
                s = row.get("標準化成分") or ""
                self.std.setdefault(_norm(s), set()).add(db)
                for k in {_norm(s), _key(s)}:
                    if k:
                        c.ing_to_db.setdefault(k, set()).add(db)
                if lic:
                    c.db_to_lic.setdefault(db, set()).add(lic)


class Phase1:
    """本站 Phase 1 的成分 → DrugBank 對照（map_fda_drugs_to_drugbank 同一套），只在對照沒見過的字串用"""

    def __init__(self):
        from catxgnn.mapping import drugbank_mapper as M
        from catxgnn.mapping.normalizer import get_all_synonyms
        self.M, self.syn = M, get_all_synonyms
        self.idx = M.build_name_index(M.load_drugbank_vocab())
        self.cache = {}

    def ids(self, s, rule):
        from catxgnn.collectors.cafda import _norm
        k = (s, id(rule))
        if k not in self.cache:
            out = set()
            for main, syns in self.syn(s):
                got = rule.std.get(_norm(main))
                if not got:
                    db = self.M.map_ingredient_to_drugbank(main, self.idx)
                    for sy in ([] if db else syns):
                        db = self.M.map_ingredient_to_drugbank(sy, self.idx)
                        if db:
                            break
                    got = {db} if db else set()
                out |= got
            self.cache[k] = out
        return self.cache[k]


def text_hit(drug, s):
    """同 cafda.LocalFDACollector._text_match，對一筆成分字串"""
    from catxgnn.collectors.cafda import _norm
    core, ing = _norm(drug), " " + _norm(s) + " "
    if len(core) < 4:
        return False
    if " " not in core and len(core) >= 6:
        return bool(re.search(rf" {re.escape(core)}[a-z]{{0,3}} ", ing))
    return f" {core} " in ing


def new_ids(s, rule, p1):
    o = s.strip().upper()
    if o in rule.orig:  # 同一個原始成分字串對照裡見過：沿用（當時對不到的照舊不收）
        return rule.orig[o]
    return p1.ids(s, rule)


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    today = datetime.date.today().isoformat()
    if "--download" in argv:
        cur = A.fetch()
        p = A.validate(cur, None)
        if p:
            raise SystemExit("現行清單有問題，不補收：" + "；".join(p))
        RAW.write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    else:
        try:
            cur = json.loads(RAW.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到現行清單 {RAW}：{e}")
    if len(cur) < MIN_CURRENT:
        raise SystemExit(f"現行清單只有 {len(cur)} 筆，疑似下載或格式有問題，不補收")
    if not any(r.get("ingredients") for r in cur):
        raise SystemExit("現行清單沒有成分欄（舊格式），不補收")
    ldate = datetime.date.fromtimestamp(RAW.stat().st_mtime).isoformat()
    try:
        from catxgnn.collectors.cafda import LocalFDACollector, _norm
        from catxgnn.regulatory import record_exclusions as RX
        base = LocalFDACollector()
        base._prepare()
        rules = {k: Rule(base, p, pad=(k != CUR)) for k, p in MAPS.items() if p.exists()}
    except Exception as e:
        raise SystemExit(f"讀不到收集器資料（data/raw 萃取檔、drug_mapping、drugbank_vocab）：{e}")
    if CUR not in rules:
        raise SystemExit("沒有 data/processed/drug_mapping.csv，不補收")
    lf = base.fm["license_id"]
    base_dins = {str(r.get(lf)) for r in base.records}
    stat = A.status_index(cur)
    newd = {}
    for r in cur:
        if r.get("set") == "allfiles" and r.get("class") == "Human" and r["din"] not in base_dins and r["din"] not in newd:
            newd[r["din"]] = r
    p1 = Phase1()
    rows, nb, nrec, nfill, gaps, nrule, nmap = [], 0, 0, 0, [], 0, {}
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        t = b.get("tfda") or {}
        if not t:
            continue
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        recs = list(t.get("records") or [])
        not_stored = [str(x) for x in t.get("records_not_stored") or []]
        exc = {str(r.get("license_id")) for r in t.get("excluded_records") or []} | {str(x) for x in t.get("excluded_ids") or []}
        have = {str(r.get("license_id") or "") for r in recs} | set(not_stored) | exc
        total = int(t.get("total_matches") or len(recs)) if t.get("found") else 0
        rule = t.get("collection_rule")
        changed = False
        if not rule:  # 第一次：找出收集規則、回填當時沒存的 DIN
            for rn in (CUR, "drug_mapping.csv.bak_20261012"):
                if rn not in rules:
                    continue
                m, _ = rules[rn].c.matches(inn)
                dins = [str(x.get(lf)) for x in m]
                if len([d for d in dins if d not in exc]) == total and {str(r.get("license_id")) for r in recs} <= set(dins) | exc:
                    rule = rn
                    hid = sorted(set(dins) - have)
                    if hid:
                        not_stored += hid
                        have |= set(hid)
                        nfill += 1
                        rows.append(f"{page}\t-\t({len(hid)} hidden DINs)\tbackfill_not_stored\t{rn}\t")
                    break
            if not rule:
                gaps.append(page)
                rows.append(f"{page}\t-\t(兩份對照都重算不出 total_matches {total})\tskipped_rule\t\t")
                continue
            nrule += 1
            changed = True
        if rule not in rules:
            gaps.append(page)
            rows.append(f"{page}\t-\t(沒有 {rule})\tskipped_rule\t\t")
            continue
        if total - len([r for r in recs if str(r.get("license_id")) not in exc]) - len(set(not_stored) - exc) > 0:
            gaps.append(page)
            rows.append(f"{page}\t-\t(total_matches 比已知 DIN 多)\tskipped_gap\t\t")
            continue
        R = rules[rule]
        ids = R.c._drugbank_ids(inn)
        mapped = any(R.c.db_to_lic.get(db) for db in ids)
        want = []
        for din, r in newd.items():
            if din in have:
                continue
            s = ing_str(r)
            if not s:
                continue
            if mapped:
                hit = bool(new_ids(s, R, p1) & ids)
            else:  # 原收集器退回文字比對的證據包（cafda._text_match）
                hit = text_hit(inn, s)
            if hit and not RX.match(page, s):
                want.append(din)
        src = (f"Health Canada DPD extract allfiles ({ldate}); matched by the original collector rule ({rule}"
               f"{'' if rule == CUR else ', pre-2026-10-12 mapping used when this bundle was collected'})")
        added = []
        for din in sorted(want, key=lambda x: (ncomp(ing_str(newd[x])) > 1, x)):
            r = newd[din]
            s = ing_str(r)
            rec = {"license_id": din, "brand_name_zh": r.get("brand", ""), "brand_name_en": r.get("brand", ""), "ingredients": s,
                   "indication": "", "dosage_form": "", "manufacturer": "", "license_holder": "", "approval_date": "", "expiry_date": "",
                   "status": stat.get(din) or r.get("status") or "", "source": src, "added": today}
            total += 1
            if len(recs) < CAP:
                recs.append(rec)
                where = "records"
            else:
                not_stored.append(din)
                where = "not_stored"
            added.append(din)
            nmap[din] = nmap.get(din, 0) + 1
            rows.append(f"{page}\t{din}\t{r.get('brand', '')}\t{where}\t{s}\t{rec['status']}")
        if not added and not changed:
            continue
        nb += bool(added)
        nrec += len(added)
        t2 = dict(t, records=recs, total_matches=total, found=bool(recs) or t.get("found", False), collection_rule=rule)
        if not_stored:
            t2["records_not_stored"] = not_stored
        if not dry:
            b["tfda"] = t2
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tdin\tproduct\twhere\tingredients\tstatus\n" + "\n".join(rows) + "\n", encoding="utf-8")
    if nrule:
        print(f"記下收集規則：{nrule} 個證據包（回填 records_not_stored {nfill} 個）")
    if gaps:
        print(f"⚠ 判斷不了收集規則或已算進總數卻不知道 DIN、這次不補的證據包 {len(gaps)} 個：{', '.join(gaps[:20])}")
    print(f"{'（試跑）' if dry else ''}依原收集規則補收：{nb} 個證據包、{nrec} 筆（不重複 DIN {len(nmap)} 個；"
          f"現行清單 {len(cur)} 筆、新上市人用 DIN {len(newd)} 個，{ldate}）")


if __name__ == "__main__":
    main(sys.argv[1:])
