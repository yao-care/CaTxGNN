---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Pirfenidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an antifibrotic agent whose established use — per public drug identity data (DrugBank DB04951) — is idiopathic pulmonary fibrosis (IPF); this is not documented in the current evidence pack because the drug is not marketed in this jurisdiction. The TxGNN model's top-ranked prediction is **Extracutaneous Mastocytoma**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review explicitly finds no biological link between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (public drug identity knowledge; not present in local regulatory data — drug not marketed in this jurisdiction) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap, DG002). Based on known information, pirfenidone is an oral antifibrotic small molecule generally understood to inhibit TGF-β1 and platelet-derived growth factor signalling, reducing fibroblast proliferation and collagen synthesis in fibrotic tissue — this is its accepted mechanism in IPF.

Extracutaneous mastocytoma, however, is a mast-cell proliferative lesion driven by **KIT mutation**-related mast cell hyperplasia, a pathway unrelated to TGF-β/collagen biology. The evidence pack's own mechanistic review for this candidate states there is "no known association with pirfenidone's TGF-β/collagen-synthesis inhibition mechanism, and no clinical or mechanistic evidence supports this link." No clinical trials, ICTRP registrations, or PubMed literature were retrieved for this drug–disease pair (query IDs 2–4 in the query log, all zero results).

Taken together, this top-ranked TxGNN score appears to reflect a graph-embedding similarity signal rather than a biologically grounded repurposing hypothesis. By contrast, a lower-ranked candidate in this same evidence pack — fibroblastic neoplasm (rank 9) — has actual in-vitro mechanistic literature and a small pilot clinical trial, and may be a more productive research direction (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Pirfenidone currently holds no Canadian market authorizations in this dataset (0 DINs, market status: Not Marketed). No licence records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (extracutaneous mastocytoma) has no supporting clinical trials, literature, or mechanistic rationale — its own evidence review flags it as a likely embedding-similarity artifact rather than a genuine signal. Combined with a blocking data gap on drug label warnings/contraindications (DG001) and missing MOA data (DG002), there is currently no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- Regulatory label warnings and contraindications (DG001, blocking — required before any S1 safety screening)
- Confirmed mechanism of action data via DrugBank API (DG002)
- If pursuing repurposing research further, consider redirecting attention to **fibroblastic neoplasm** (rank 9), which has direct in-vitro mechanistic studies and a small prospective pilot trial (PMID 12907346) in a related fibrotic tumour (FAP-associated desmoid tumour) — though note this also carries a conflicting safety signal (case reports of pirfenidone-associated fibroblastic malignancy) that would need to be resolved before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

