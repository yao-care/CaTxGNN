---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 2
---

# Ponatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ponatinib: Signals for Fibromatosis, Gingival and Liposarcoma

## One-Sentence Summary

Ponatinib is a multi-kinase inhibitor (BCR-ABL, FGFR1-3, PDGFRα, VEGFR2, SRC); its original approved indication is not recorded in this evidence pack, and the drug is currently **not marketed in Canada**.
The TxGNN model's top prediction is **Fibromatosis, Gingival** (score 99.04%), but this has **no clinical trial or literature support**. A secondary prediction, **Liposarcoma** (score 99.00%), is backed by **1 preclinical publication** suggesting kinase-targetable vulnerabilities in this tumour type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Canada license on file; original indication not recorded in evidence pack) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is not available as a structured field in this evidence pack. However, the evidence pack's own analysis identifies ponatinib as a **multi-kinase inhibitor** targeting BCR-ABL, FGFR1-3, PDGFRα, VEGFR2, and SRC — consistent with its known use as a tyrosine kinase inhibitor (TKI).

For the top-ranked prediction, **Fibromatosis, Gingival** — a benign fibroproliferative gum condition — there is no established mechanistic link to ponatinib's kinase inhibition profile. The 99.04% TxGNN score reflects a purely computational knowledge-graph association with no supporting clinical or preclinical evidence, which is why this candidate is scored L5 (model prediction only) and staged as **Hold**.

For the secondary prediction, **Liposarcoma**, the mechanistic rationale is stronger: known FGFR/PDGFR pathway dysregulation in liposarcoma subtypes aligns with ponatinib's kinase inhibition spectrum. One in vitro drug-screening study (PMID 29132397) found kinase inhibitors, including candidates in ponatinib's target class, to have activity against liposarcoma cell lines — supporting a plausible but still preclinical (L4) hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for either Fibromatosis, Gingival or Liposarcoma).

---

## Literature Evidence

**For Fibromatosis, Gingival (top-ranked prediction):** Currently no related literature available.

**For Liposarcoma (secondary prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinical/Drug Screening (in vitro) | Journal of Hematology & Oncology | RNAi and drug screening in liposarcoma identified druggable kinase targets, supporting kinase inhibitor activity in this understudied tumour type |

---

## Canada Market Information

Ponatinib is currently not marketed in Canada — no active licenses (DINs) are on file.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor / TKI, per known BCR-ABL/FGFR/PDGFR/VEGFR/SRC profile) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Fibromatosis, Gingival) has no clinical or literature support and is a pure model artifact (L5). A **Blocking** data gap also exists — Canada/TFDA regulatory warnings and contraindications are not on file, preventing a valid S1 safety evaluation for either candidate.

**To proceed, the following is needed:**
- Retrieve official prescribing information (warnings, contraindications, DDI) to resolve the blocking safety data gap
- Confirm ponatinib's mechanism of action and original approved indication via DrugBank/regulatory sources
- If pursuing the Liposarcoma signal, expand the literature search beyond the single preclinical study and monitor for emerging trial registrations
- Given the weak mechanistic basis, do not advance the Fibromatosis, Gingival candidate without additional independent evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

