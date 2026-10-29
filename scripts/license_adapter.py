"""CA（Health Canada Drug Product Database）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：DPD 全量萃取檔四包（免金鑰）：allfiles.zip（上市）、allfiles_ia.zip（停用）、allfiles_dr.zip（休眠）、allfiles_ap.zip（核准未上市）
https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/<名稱>.zip
drug*.txt：第 1 欄 DRUG_CODE、第 4 欄 DIN；status*.txt：第 1 欄 DRUG_CODE、第 2 欄 CURRENT_STATUS_FLAG（Y＝現行）、第 3 欄 STATUS。
證據包紀錄 license_id＝DIN、status＝DPD STATUS 原文（MARKETED／APPROVED／DORMANT／CANCELLED POST MARKET…）；
reviewer 依文字判定（cancel 算註銷，dormant、approved 算核准未上市）。同一 DIN 多筆時取 MARKETED > APPROVED／DORMANT > 其他。
新檔沒有的 DIN 保留原狀態。
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
        return list(csv.reader(io.TextIOWrapper(fh, encoding="latin-1")))


def fetch():
    out = []
    for name, sfx in SETS.items():
        z = _zip(name)
        din = {r[0]: r[3].strip() for r in _rows(z, f"drug{sfx}.txt") if len(r) > 3}
        n = 0
        for r in _rows(z, f"status{sfx}.txt"):
            if len(r) > 2 and r[1] == "Y" and r[0] in din and din[r[0]]:
                out.append({"din": din[r[0]], "status": r[2].strip(), "set": name}); n += 1
        if n == 0:
            raise RuntimeError(f"{name} 沒有現行狀態紀錄，疑似格式改變")
    return out


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
