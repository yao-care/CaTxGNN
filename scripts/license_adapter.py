"""CA（Health Canada Drug Product Database）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：DPD 全量萃取檔四包（免金鑰）：allfiles.zip（上市）、allfiles_ia.zip（停用）、allfiles_dr.zip（休眠）、allfiles_ap.zip（核准未上市）
https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/<名稱>.zip
drug*.txt：第 1 欄 DRUG_CODE、第 4 欄 DIN；status*.txt：第 1 欄 DRUG_CODE、第 2 欄 CURRENT_STATUS_FLAG（Y＝現行）、第 3 欄 STATUS。
證據包紀錄 license_id＝DIN、status＝DPD STATUS 原文（MARKETED／APPROVED／DORMANT／CANCELLED POST MARKET…）；
reviewer 依文字判定（cancel 算註銷，dormant、approved 算核准未上市）。同一 DIN 多筆時取 MARKETED > APPROVED／DORMANT > 其他。
新檔沒有的 DIN 保留原狀態。
2026-11-25（第五輪，用戶決定「adapter 存成分」）：RAW_FILE 每筆另存收集器比對要用的欄位：drug_code、class（Human／Veterinary…）、
brand（BRAND_NAME）、ingredients（ingred*.txt 的 INGREDIENT，依原順序去重）、forms（PHARMACEUTICAL_FORM）、routes（ROUTE_OF_ADMINISTRATION）、
company（comp*.txt 的 DIN owner）——讓 Release 帶著現行清單的成分，量測與補收不用另下載。萃取檔四包任一下載失敗（canada.ca 從雲端常連不上）時，
改用 Health Canada DPD API（https://health-products.canada.ca/api/drug/，drugproduct／status／activeingredient／form／route，同一個資料庫）
取同樣的欄位，狀態轉成萃取檔的大寫寫法（Marketed→MARKETED、Cancelled Post Market→CANCELLED POST MARKET），set 依狀態歸到四包之一；
劑型、給藥途徑也轉大寫（萃取檔寫法）。
"""
import csv
import io
import time
import zipfile

import requests

RAW_FILE = "raw/dpd_current_status.json"
BASE_URL = "https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/"
SETS = {"allfiles": "", "allfiles_ia": "_ia", "allfiles_dr": "_dr", "allfiles_ap": "_ap"}
RANK = lambda s: 3 if s == "MARKETED" else 2 if s in ("APPROVED", "DORMANT") else 1


def _zip(name):
    for attempt in range(4):
        try:
            r = requests.get(BASE_URL + name + ".zip", timeout=300)
            r.raise_for_status()
            return zipfile.ZipFile(io.BytesIO(r.content))
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def _rows(z, fname):
    with z.open(fname) as fh:
        raw = fh.read()
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        txt = raw.decode("latin-1")
    return list(csv.reader(io.StringIO(txt)))


def _multi(z, fname, col):
    """drug_code → [欄位值]（依檔案順序去重）；檔案不在包裡就回傳空"""
    out = {}
    if fname not in z.namelist():
        return out
    for r in _rows(z, fname):
        if len(r) > col and r[col].strip():
            v = out.setdefault(r[0], [])
            if r[col].strip() not in v:
                v.append(r[col].strip())
    return out


def _fetch_extract():
    out = []
    for name, sfx in SETS.items():
        z = _zip(name)
        drug = {r[0]: r for r in _rows(z, f"drug{sfx}.txt") if len(r) > 4}
        ing = _multi(z, f"ingred{sfx}.txt", 2)
        form = _multi(z, f"form{sfx}.txt", 2)
        route = _multi(z, f"route{sfx}.txt", 2)
        comp = {}
        if f"comp{sfx}.txt" in z.namelist():
            for r in _rows(z, f"comp{sfx}.txt"):
                if len(r) > 4 and (r[0] not in comp or r[4] == "DIN_OWNER"):
                    comp[r[0]] = r[3].strip()
        n = 0
        for r in _rows(z, f"status{sfx}.txt"):
            if len(r) > 2 and r[1] == "Y" and r[0] in drug and drug[r[0]][3].strip():
                d = drug[r[0]]
                out.append({"din": d[3].strip(), "status": r[2].strip(), "set": name, "drug_code": r[0], "class": d[2].strip(),
                            "brand": d[4].strip(), "ingredients": ing.get(r[0], []), "forms": form.get(r[0], []),
                            "routes": route.get(r[0], []), "company": comp.get(r[0], "")})
                n += 1
        if n == 0:
            raise RuntimeError(f"{name} 沒有現行狀態紀錄，疑似格式改變")
    return out


API_URL = "https://health-products.canada.ca/api/drug/"
API_SET = {"MARKETED": "allfiles", "APPROVED": "allfiles_ap", "DORMANT": "allfiles_dr"}


def _api(endpoint):
    for attempt in range(4):
        try:
            r = requests.get(f"{API_URL}{endpoint}/?lang=en&type=json", timeout=600)
            r.raise_for_status()
            return r.json()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def _fetch_api():
    prod = {str(r["drug_code"]): r for r in _api("drugproduct")}
    def multi(rows, key):
        o = {}
        for r in rows:
            v = str(r.get(key) or "").strip()
            if v:
                L = o.setdefault(str(r["drug_code"]), [])
                if v not in L:
                    L.append(v)
        return o
    ing = multi(_api("activeingredient"), "ingredient_name")
    form = {k: [x.upper() for x in v] for k, v in multi(_api("form"), "pharmaceutical_form_name").items()}
    route = {k: [x.upper() for x in v] for k, v in multi(_api("route"), "route_of_administration_name").items()}
    out = []
    for r in _api("status"):
        c = str(r["drug_code"])
        p = prod.get(c)
        din = str((p or {}).get("drug_identification_number") or "").strip()
        if not din:
            continue
        st = str(r.get("status") or "").strip().upper()
        out.append({"din": din, "status": st, "set": API_SET.get(st, "allfiles_ia"), "drug_code": c, "class": p.get("class_name", ""),
                    "brand": str(p.get("brand_name") or "").strip(), "ingredients": ing.get(c, []), "forms": form.get(c, []),
                    "routes": route.get(c, []), "company": str(p.get("company_name") or "").strip()})
    return out


def fetch():
    try:
        return _fetch_extract()
    except Exception as e:  # 萃取檔下載不到（雲端 session 常見）→ 同一資料庫的 API
        print(f"DPD 萃取檔下載失敗（{str(e)[:120]}），改用 DPD API", flush=True)
        return _fetch_api()


def validate(new, old):
    p = []
    if len(new) < 30000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if not any(r["status"] == "MARKETED" for r in new):
        p.append("沒有任何 MARKETED，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:
        cur = idx.get(r["din"])
        if cur is None or RANK(r["status"]) > RANK(cur):
            idx[r["din"]] = r["status"]
    return idx


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True


# 2026-11-24（用戶決定「程式產生許可證表」）：每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）在概覽表同步之後，
# 依證據包把市場段落的程式許可證表重排（scripts/sync_license_tables.py --bundles；所有頁比對、只寫有變的）。
# PAGE_NOTE：排程 3b 自我檢查允許的非表格列（程式區塊標記、來源句、部分紀錄說明句、沒有 DIN 的說明句；2026-11-24 第三輪起含補的市場段落標題）。
def _slt(site_dir):
    import importlib.util
    from pathlib import Path
    s = importlib.util.spec_from_file_location("sync_license_tables", Path(site_dir) / "scripts" / "sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def sync_tables(site_dir, bundles):
    """回傳 [(頁, 欄位, 前值, 後值)]；所有有證據包的頁都比對（只寫內容有變的），不只 bundles 列出的藥"""
    import difflib
    from pathlib import Path
    m = _slt(site_dir)
    drugs = Path(site_dir) / "docs" / "_drugs"
    before = {p.name: p.read_text(encoding="utf-8") for p in drugs.glob("*.md")}
    out = []
    for name in m.run(from_bundles=True):
        new = (drugs / name).read_text(encoding="utf-8")
        for l in difflib.unified_diff(before[name].split("\n"), new.split("\n"), lineterm="", n=0):
            if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].startswith("|"):
                out.append((name[:-3], "Licence table (programmatic)", l[1:] if l[0] == "-" else "", l[1:] if l[0] == "+" else ""))
    return out


try:
    import importlib.util as _ilu
    from pathlib import Path as _P
    _s = _ilu.spec_from_file_location("_slt_note", _P(__file__).resolve().parent / "sync_license_tables.py")
    _m = _ilu.module_from_spec(_s)
    _s.loader.exec_module(_m)
    PAGE_NOTE = _m.PAGE_NOTE
except Exception:  # 站上的 license_adapter 被母目錄當模組載入時，路徑一定在 scripts/ 下；這裡只防萬一
    PAGE_NOTE = r"^<!-- licenses:(begin|end) -->$"
