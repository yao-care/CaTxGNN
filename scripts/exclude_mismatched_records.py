#!/usr/bin/env python3
"""證據包收錯品項移出（2026-11-25 第五輪，用戶決定；比照 CHTxGNN 第三輪）：依 config/bundle_record_exclusions.json，
把 data/bundles/*/drug_bundle.json 裡「drug_mapping 把另一個有效成分對到本藥 DrugBank ID」的紀錄從 tfda.records 移到
tfda.excluded_records（附 excluded＝第一次排除日、excluded_reason、excluded_basis），total_matches 扣掉收集器全部比對結果
（含因 20 筆上限沒存的 DIN）裡被規則排除的 DIN；扣過的 DIN 記在 tfda.excluded_ids，可重複執行（不重複扣）。
沒有 data/raw（DPD 萃取檔）或 drug_mapping.csv 時只能扣存下的筆數，照實印出。
每週 license-refresh.yml 在 license_refresh 前先跑；改完要重算證據包 local_regulatory、事實層與快照（排程本身會做）。
用法（repo 根目錄，先還原 data/）：python3 scripts/exclude_mismatched_records.py [--dry-run]
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from catxgnn.regulatory import record_exclusions as RX  # noqa: E402


def _collector():
    try:
        from catxgnn.collectors.cafda import LocalFDACollector
        c = LocalFDACollector()
        c._prepare()
        return c
    except Exception as e:  # noqa: BLE001
        print(f"  （收集器資料讀不到：{str(e)[:120]}；total_matches 只扣存下的筆數）")
        return None


def _status_index():
    """DPD 現行狀態（每週排程 license_adapter 存的 data/raw/dpd_current_status.json）；補回的紀錄照它寫狀態，沒有就留空、排程下次補"""
    f = ROOT / "data" / "raw" / "dpd_current_status.json"
    if not f.exists():
        return {}
    import importlib.util
    s = importlib.util.spec_from_file_location("license_adapter", ROOT / "scripts" / "license_adapter.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m.status_index(json.loads(f.read_text(encoding="utf-8")))


def run(dry=False):
    today = time.strftime("%Y-%m-%d")
    moved, deducted, refilled, touched = 0, 0, 0, []
    col = None
    stat = None
    for f in sorted((ROOT / "data" / "bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        if RX.bundle_key(name) not in RX.rules():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        keep, out = [], []
        for r in t.get("records") or []:
            rule = RX.match(name, r)
            if rule:
                out.append(dict(r, excluded=today, excluded_reason=rule["reason"], excluded_basis=rule["basis"]))
            else:
                keep.append(r)
        done = set(t.get("excluded_ids") or [])
        ex_ids = {str(r.get("license_id")) for r in out}
        if col is None:
            col = _collector() or False
        refill = []
        if col and stat is None:
            stat = _status_index()
        if col:
            recs, ids = col.matches(name.replace("_", " "))
            lf = col.fm.get("license_id")
            ex_ids |= {str(r.get(lf)) for r in recs if col.excluded(name, r)}
            # 移出後存下的不到 20 筆、收集器還有沒存的本藥 DIN：照收集器同一排序補回（只加不刪，記 source／added）
            have = {str(r.get("license_id")) for r in keep}
            if out and len(keep) < 20:
                ok = [r for r in recs if not col.excluded(name, r)]
                for r in col._format(ok, ids).get("records") or []:
                    if len(keep) + len(refill) >= 20:
                        break
                    if r["license_id"] not in have and r["license_id"] not in ex_ids:
                        r = dict(r, status=stat.get(r["license_id"]) or r.get("status") or "")
                        refill.append(dict(r, source="Health Canada DPD (collectors/cafda.py, same rule) — refilled after excluding mismatched records", added=today))
                        have.add(r["license_id"])
        new_ids = sorted(ex_ids - done)
        if not out and not new_ids:
            continue
        for r in refill:
            print(f"  {name}: 補回 {r.get('license_id')} {str(r.get('brand_name_en'))[:45]}（{str(r.get('ingredients'))[:70]}）")
        keep += refill
        for r in out:
            print(f"  {name}: 移出 {r.get('license_id')} {str(r.get('brand_name_en'))[:45]}（{str(r.get('ingredients'))[:70]}）")
        print(f"  {name}: total_matches 扣 {len(new_ids)}（{int(t.get('total_matches') or 0)} → {max(len(keep), int(t.get('total_matches') or 0) - len(new_ids))}）")
        moved += len(out)
        deducted += len(new_ids)
        refilled += len(refill)
        touched.append(name)
        if dry:
            continue
        t["records"] = keep
        if out:
            t["excluded_records"] = (t.get("excluded_records") or []) + out
        t["total_matches"] = max(len(keep), int(t.get("total_matches") or 0) - len(new_ids))
        t["excluded_ids"] = sorted(done | set(new_ids))
        if not keep:
            t["found"] = False
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"證據包收錯品項：移出 {moved} 筆、total_matches 扣 {deducted} 個 DIN、補回 {refilled} 筆（{len(touched)} 個證據包）{'（試跑，沒寫檔）' if dry else ''}")
    return touched


if __name__ == "__main__":
    run(dry="--dry-run" in sys.argv[1:])
