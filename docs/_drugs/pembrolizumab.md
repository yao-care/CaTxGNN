---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: From Oncology Immunotherapy to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor used across multiple advanced malignancies (the evidence pack's own literature references its established role in non-small-cell lung cancer, melanoma, MSI-H/dMMR colorectal cancer, hepatocellular carcinoma, and head-and-neck cancer), though this specific evidence pack does not record a formal original-indication or MOA entry.
The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but this signal is supported by **0 clinical trials** and **0 publications** — it is a model-score-only prediction with an explicitly stated lack of mechanistic plausibility.
Given the complete absence of direct evidence and the biological mismatch between an immune-checkpoint mechanism and a benign fibrous overgrowth condition, this candidate does not currently warrant further investment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Canada license on file; literature in this pack references established oncology use in NSCLC, melanoma, MSI-H/dMMR CRC, HCC, HNSCC) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal drug record (flagged as a High-severity data gap, DG002). Based on evidence contained elsewhere in this pack, pembrolizumab is a humanized monoclonal antibody that blocks the PD-1 receptor, disinhibiting T-cell-mediated antitumor immunity — a mechanism well documented across the literature retrieved for other candidate indications in this same evidence pack (e.g., PMID 27398650, PMID 26558876).

Gingival fibromatosis, however, is a benign, non-neoplastic gum overgrowth condition driven by fibroblast/connective-tissue proliferation, not by tumor-mediated immune evasion. The evidence pack's own rationale for this candidate states explicitly that there is **no known mechanistic link** between PD-1/PD-L1 checkpoint blockade and gingival fibromatosis pathology — this is a high TxGNN score with no supporting mechanistic or clinical rationale.

No clinical trials or publications were retrieved for this drug-disease pair (query IDs 2–4 in the query log all returned zero results), reinforcing that this is a pure model-prediction signal rather than an evidence-supported hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

No Health Canada licenses are on file for this drug in this evidence pack (market status: Not Marketed; total licenses: 0).

---

## Cytotoxicity

Pembrolizumab is an antineoplastic agent (PD-1 immune checkpoint inhibitor), based on its extensively documented oncology use in the literature retrieved elsewhere in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions — no direct toxicity data on file; literature in this pack instead documents immune-related adverse events (irAEs) as the primary toxicity concern (e.g., PMID 26874776 "Management of toxicities of immune checkpoint inhibitors"; PMID 32126176, neurologic irAEs) |
| Emetogenicity Classification | Low (not a conventional cytotoxic chemotherapeutic) |
| Monitoring Items | Thyroid function, liver and renal function, and clinical monitoring for immune-related adverse events (colitis, hepatitis, pneumonitis, endocrinopathies) |
| Handling Protection | Please refer to the package insert warnings and precautions — no cytotoxic-handling data on file for this record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (L5), with zero clinical trials or publications retrieved, and the pack's own mechanistic assessment finds no plausible link between PD-1 blockade and a benign gingival overgrowth condition. Two blocking/high-severity data gaps (missing TFDA/product labeling and missing MOA documentation) also prevent even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A credible mechanistic or preclinical rationale connecting PD-1 checkpoint blockade to gingival fibromatosis before any further evidence collection is warranted
- Manual review of TxGNN disease-mapping quality — the query log shows several other candidates in this same output (e.g., "lung hilum carcinoma," "lung germ cell tumor," rated L3–L4) carry substantially more clinical/literature support and may be better prioritized for further evaluation than this top-ranked score-only signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

