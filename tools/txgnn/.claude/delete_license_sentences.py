"""刪除藥物頁正文裡跟許可證事實矛盾的句子（2026-11-05，用戶決定 7 站比照 Za 修；全程不用 AI、不改寫）。

判定與 check_drug_page.py 共用（m3_verdict＝M3／M3a–M3d，TW_LEFTOVER＝M5），所以刪完 checker 的 M3／M5 會歸零；
另讀本站 scripts/license_sentence_fixes.json 的人工清單（頁 → [{sentence, reason}]，checker 抓不到但已用新資料核對過的句子）。
規則：
- 正文（front matter、標題、概覽表狀態／張數列以外）跟事實矛盾的句子整句刪除；整行空掉就拿掉該行，連續空行併成一行。
- 表格列：只刪 M5（台灣模板殘留的狀態列、taiwan_regulatory dump 列）；表格只剩表頭時整張拿掉。
- 緊接在被刪句後面、以指代詞開頭的句子（DEPENDENT，各語言）一併刪除，避免留下失去指涉的半句。
- 刪掉的句子逐句寫進 --log（頁、規則、原句、依據）。
用法（工作目錄，先跑 dump_license_facts）：python3 .claude/delete_license_sentences.py <站> [--dry-run] [--log out.tsv] [--pages a,b]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
_s = importlib.util.spec_from_file_location("ck", BASE / ".claude/check_drug_page.py")
ck = importlib.util.module_from_spec(_s); _s.loader.exec_module(ck)

ABBR = [("e.g.", "e‧g‧"), ("i.e.", "i‧e‧"), ("vs.", "vs‧"), ("No.", "No‧"), ("et al.", "et al‧"), ("approx.", "approx‧"), ("Vet.", "Vet‧"),
        ("p. ej.", "p‧ ej‧"), ("aprox.", "aprox‧"), ("fx.", "fx‧"), ("bl.a.", "bl‧a‧"), ("mht.", "mht‧"), ("Inc.", "Inc‧"), ("Ltd.", "Ltd‧"),
        ("S.A.", "S‧A‧"), ("U.S.", "U‧S‧"), ("Dr.", "Dr‧"), ("St.", "St‧"), ("Co.", "Co‧"), ("spp.", "spp‧"), ("Sdn.", "Sdn‧"), ("Bhd.", "Bhd‧")]
DEPENDENT = {
    "en": re.compile(r"^\W*(It|Its|This|These|They|Their|Those|As noted above|See the note above|Without these|Under these)\b"),
    "es": re.compile(r"^\W*(Esto|Este|Esta|Estos|Estas|Ello|Por ello|Por lo tanto|Dicho|Dicha)\b"),
    "ko": re.compile(r"^\W*(이는|이것은|이러한|따라서 이|그러므로 이|이 때문에)"),
    "ms": re.compile(r"^\W*(Ini|Hal ini|Oleh itu|Perkara ini)\b"),
    "da": re.compile(r"^\W*(Det|Dette|Disse|De|Derfor)\b"),
}


# 2026-11-05 用戶決定：同一句混有藥物身分、療效或機轉內容時，只刪跟事實矛盾的子句（原句文字照舊，只做刪除）
_C = r"(?:Canada|the US|the U\.S\.|the United States|Denmark|Malaysia|Korea|España|Colombia|Dinamarca)"
_TAIL = r"(?: (?:as|under the brand names?|under the names?|como|con el nombre(?: de)?|bajo el nombre(?: de)?) [^,;.()]*?)?(?: \([^)]*\))?(?= para | to | for | que | in the | en el |[,;.]|$)"
CUTS = [re.compile(p, re.I) for p in (
    r",? (?:that|which) (?:is|are) (?:currently |already |widely |also )?marketed in " + _C + _TAIL,
    r",? and (?:the drug|it|the product) is (?:already |currently |also )?marketed in " + _C + _TAIL,
    r"(?<=\w)(?<! is)(?<! are)(?<! be) marketed in " + _C + _TAIL,
    r" with \d+ valid [^,;.()]*?(?:authori[sz]ations?|licen[cs]es?|DINs?)(?: \([^)]*\))?(?=[,;.]|$)",
    r",? y (?:ya )?(?:está|se encuentra) comercializad[oa] en (?:España|Colombia)" + _TAIL,
    r",? y (?:el fármaco|el medicamento|el producto) (?:ya )?(?:está|se encuentra) comercializad[oa] en (?:España|Colombia)" + _TAIL,
    r",? (?:que )?(?:ya )?(?:está|se encuentra) comercializad[oa] en (?:España|Colombia)" + _TAIL,
    r",? que se comercializa en (?:España|Colombia)" + _TAIL,
    r",? (?:autorizad[oa]s? y )?comercializad[oa]s? en (?:España|Colombia)" + _TAIL,
)]


def clause_cut(site, lang, core, fc, rule):
    """只刪矛盾子句（固定句型：關係子句、分詞片語、對等子句、「with N valid…」）；刪後仍矛盾或剩太短回 None"""
    if rule not in ("M3", "M3a", "M3b", "M3c", "M3d"):
        return None
    for rx in CUTS:
        m = rx.search(core)
        if not m or m.start() < 8:
            continue
        cand = (core[:m.start()] + core[m.end():]).strip()
        cand = re.sub(r"\s+([,.;:])", r"\1", cand)
        if len(re.findall(r"\w+", cand)) >= 4 and not ck.m3_verdict(site, lang, cand, fc) and not ck.TW_LEFTOVER.search(cand):
            return cand
    return None


def split_sentences(line):
    t = line
    for a, b in ABBR:
        t = t.replace(a, b)
    parts = re.split(r"(?<=[.!?。！？])(\s+)", t)
    out = []
    for i in range(0, len(parts), 2):
        s = parts[i]
        for a, b in ABBR:
            s = s.replace(b, a)
        out.append((s, parts[i + 1] if i + 1 < len(parts) else ""))
    return out


def process(site, lang, page, fc, manual):
    raw = page.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw[:500]
    t = raw.replace("\r\n", "\n")
    if "layout: id_redirect" in t[:3000] or 'http-equiv="refresh"' in t[:3000]:
        return None, []
    fm_end = t.index("\n---", 4) + 4 if t.startswith("---") else 0
    lines = t.split("\n")
    start = t[:fm_end].count("\n") + 1
    log = []
    man = manual.get(page.stem, [])
    dep = DEPENDENT.get("en" if lang == "en-us" else lang)
    in_managed = False
    tdel = set()
    for i in range(start, len(lines)):
        l = lines[i]
        if re.search(r"<!-- (review:begin \S+|brand-names:start) -->", l):
            in_managed = True
        if re.search(r"<!-- (review:end \S+|brand-names:end) -->", l):
            in_managed = False
            continue
        if in_managed or not l.strip() or l.startswith(("#", "{:", "<", "---")):
            continue
        if l.startswith("|"):
            mrow = next((m for m in man if not m.get("keep") and m["sentence"] in l), None)
            if mrow:
                log.append((page.stem, "MANUAL", l.strip(), mrow["reason"]))
                lines[i] = None
                tdel.add(i)
                continue
            if site != "TwTxGNN" and ck.TW_LEFTOVER.search(l) and not re.fullmatch(r"[\s|:\-]+", l):
                log.append((page.stem, "M5", l.strip(), "TwTxGNN 模板殘留的台灣上市狀態列／taiwan_regulatory 欄位，與本站無關"))
                lines[i] = None
                tdel.add(i)
            continue
        sents = split_sentences(l)
        keep, changed, prev_del = [], False, False
        for s, sp in sents:
            core = re.sub(r"^\s*([-*>]\s*|\d+\.\s+)+", "", s.strip())
            why = None
            cutm = next((m for m in man if m.get("cut") and m["sentence"] in s), None)
            if cutm:
                log.append((page.stem, "MANUAL（子句）", s.strip(), cutm["reason"] + f"；刪除片段：{cutm['cut']}"))
                keep.append((s.replace(cutm["cut"], "", 1), sp)); changed = True; prev_del = False
                continue
            if any(m.get("keep") and m["sentence"] in s for m in man):
                keep.append((s, sp)); prev_del = False
                continue
            for m in man:
                if not m.get("keep") and m["sentence"] in s:
                    why = ("MANUAL", m["reason"])
            if not why and fc and re.search(r"\w{3}", core):
                h = ck.m3_verdict(site, lang, core, fc)
                if h:
                    why = (h[0], h[1].split("，正文")[0].split("：")[0])
            if not why and site != "TwTxGNN" and ck.TW_LEFTOVER.search(core):
                why = ("M5", "TwTxGNN 模板殘留的台灣許可說法，與本站無關")
            if not why and prev_del and dep and dep.search(core) and re.search(ck._LIC + r"|market|comerciali|시판|허가|dipasarkan|markedsfør|regist", core, re.I):
                why = ("DEPENDENT", "緊接在被刪句後、以指代詞開頭；前句刪除後失去指涉對象（不改寫，一併刪除）")
            if why:
                lead = s[:len(s) - len(s.lstrip())] + re.match(r"^\s*(([-*>]\s*|\d+\.\s+)*)", s.strip()).group(1)
                cut = clause_cut(site, lang, core, fc, why[0]) if fc else None
                if cut:
                    log.append((page.stem, why[0] + "（子句）", s.strip(), why[1] + f"；只刪子句，保留：{cut}"))
                    keep.append((lead + cut, sp)); changed = True; prev_del = False
                    continue
                log.append((page.stem, why[0], s.strip(), why[1]))
                changed = prev_del = True
                continue
            prev_del = False
            keep.append((s, sp))
        if changed:
            new = "".join(s + sp for s, sp in keep).rstrip()
            bullet = re.match(r"^(\s*[-*]\s+|\s*\d+\.\s+|>\s*)", l)
            if not re.sub(r"^\s*([-*]|\d+\.|>)\s*", "", new).strip(" *_>"):
                new = None
            elif bullet and not new.startswith(bullet.group(1)):
                new = bullet.group(1) + new.lstrip(" -*>")
            lines[i] = new
    # 刪過列的表格若只剩表頭（＋分隔列）就整張拿掉
    k = start
    while k < len(lines):
        if lines[k] is not None and lines[k].startswith("|"):
            j = k
            while j < len(lines) and (lines[j] is None or lines[j].startswith("|")):
                j += 1
            rest = [x for x in lines[k:j] if x is not None]
            if tdel & set(range(k, j)) and len(rest) <= 2 and (len(rest) < 2 or re.fullmatch(r"[\s|:\-]+", rest[-1])):
                for x in range(k, j):
                    lines[x] = None
            k = j
        else:
            k += 1
    out = [x for x in lines if x is not None]
    if not log:
        return None, log
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    if t2 == t:
        return None, log
    return (t2.replace("\n", "\r\n") if crlf else t2), log


def main(argv):
    site = next(a for a in argv if a.endswith("TxGNN"))
    lang = ck.LANG.get(site, "en")
    dry = "--dry-run" in argv
    logf = argv[argv.index("--log") + 1] if "--log" in argv else None
    only = set(argv[argv.index("--pages") + 1].split(",")) if "--pages" in argv else None
    facts = json.loads((BASE / ".claude/cache/license_facts" / f"{site}.json").read_text(encoding="utf-8"))
    mf = BASE / site / "scripts/license_sentence_fixes.json"
    manual = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
    all_log, n = [], 0
    for page in sorted((BASE / site / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        fc = facts.get(page.stem) or facts.get(page.stem.replace("-", "_")) or facts.get(page.stem.replace("_", "-"))
        new, log = process(site, lang, page, fc, manual)
        all_log += log
        if new is not None:
            n += 1
            if not dry:
                page.write_bytes(new.encode("utf-8"))
    if logf:
        Path(logf).write_text("頁\t規則\t原句\t依據\n" + "\n".join("\t".join(x) for x in all_log) + "\n", encoding="utf-8")
    print(f"{site}：改頁 {n}；刪句 {len(all_log)}")


if __name__ == "__main__":
    main(sys.argv[1:])
