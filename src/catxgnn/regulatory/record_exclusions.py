"""證據包收錯品項的排除規則（2026-11-25 第五輪，用戶決定；規則與依據在 config/bundle_record_exclusions.json，比照 CHTxGNN）。

drug_mapping.csv 依 DrugBank ID 對照 DIN，另一個有效成分被對到本藥 DrugBank ID 時（SODIUM LACTATE→DB09395 Sodium acetate、
ANTIHEMOPHILIC FACTOR→DB09109 Turoctocog alfa）會被收進本藥證據包。規則：證據包名在規則的 bundles 裡，紀錄成分欄
（DPD active ingredient，「;」分隔）有一段符合 family、卻沒有一段符合 keep → 排除（比對不分大小寫）。
scripts/exclude_mismatched_records.py 與 collectors/cafda.py 共用。
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

CONF = Path(__file__).resolve().parents[3] / "config" / "bundle_record_exclusions.json"


def _norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().upper()
    return re.sub(r"\s+", " ", s).strip()


def bundle_key(name) -> str:
    return re.sub(r"[^a-z0-9]+", "_", _norm(name).lower()).strip("_")


@lru_cache(maxsize=None)
def rules() -> dict:
    """證據包名 → [規則]（設定檔不存在時沒有規則）"""
    out = {}
    if not CONF.exists():
        return out
    for r in json.loads(CONF.read_text(encoding="utf-8")).get("rules") or []:
        for b in r["bundles"]:
            out.setdefault(bundle_key(b), []).append(r)
    return out


def components(ingredients) -> list:
    return [_norm(c) for c in re.split(r";", str(ingredients or "")) if c.strip()]


def match(bundle, ingredients):
    """成分欄字串（或含 ingredients 的紀錄 dict）依規則該排除就回傳規則，否則 None"""
    if isinstance(ingredients, dict):
        ingredients = ingredients.get("ingredients")
    comps = components(ingredients)
    if not comps:
        return None
    for r in rules().get(bundle_key(bundle), ()):
        fam, keep = re.compile(r["family"], re.I), re.compile(r["keep"], re.I)
        if any(fam.search(c) for c in comps) and not any(keep.search(c) for c in comps):
            return r
    return None
