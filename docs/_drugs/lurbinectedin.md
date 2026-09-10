---
layout: default
title: Lurbinectedin
parent: 僅模型預測 (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: From Small Cell Lung Cancer to Multiple Endocrine Neoplasia

*(Original indication is not present in this evidence pack — DrugBank query returned no indication text. "Small cell lung cancer" reflects Lurbinectedin's known public labeling (Zepzelca®) and is not confirmed by the data below; see Data Gap DG002.)*

## One-Sentence Summary

Lurbinectedin (DrugBank DB12674) is a marketed antineoplastic agent, but its original indication and mechanism of action are both missing from this evidence pack. TxGNN predicts a possible link to **multiple endocrine neoplasia** with a score of **99.44%**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (DrugBank query incomplete — see DG002) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lurbinectedin in this evidence pack (Data Gap DG002, High severity), and no original indication is recorded either. Without either piece of information, no mechanistic bridge between the drug and multiple endocrine neoplasia can be constructed from the available data.

The pack's own rationale for this candidate states: the ranking rests solely on the TxGNN knowledge-graph score (0.9944); there is no clinical trial or literature evidence, and because the drug's original indication and mechanism are both data gaps, no biological link to this endocrine tumour syndrome can currently be established.

The other nine candidates in this batch (HIV, rheumatoid arthritis, ALS, CMV infection, and several veterinary conditions such as feline immunodeficiency syndrome, malignant catarrh, and infectious bovine rhinotracheitis) show the same pattern — high raw TxGNN scores with zero supporting trials or literature, and in several cases the predicted "disease" is not even a human condition. This suggests the current prediction set for this drug should be treated as exploratory model output rather than a vetted repurposing shortlist.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Lurbinectedin is not currently marketed in Canada (0 DINs on file); no license records are available to summarize.

## Cytotoxicity

Lurbinectedin is a known antineoplastic (chemotherapy) agent, so this section is included. Detailed toxicity data was not returned in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-binding agent), based on general drug classification — not confirmed within this evidence pack |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (multiple endocrine neoplasia) has Evidence Level L5 — a knowledge-graph score with zero clinical trials or literature — and the drug's own safety and mechanism data are flagged as a Blocking data gap (DG001), which by itself prevents entry into initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA/Health Canada-equivalent label warnings and contraindications (DG001, Blocking)
- Mechanism of action data from DrugBank API (DG002, High)
- Confirmed original indication for this drug
- At least preclinical or mechanistic evidence linking Lurbinectedin to multiple endocrine neoplasia before advancing past L5
- Re-screening of the remaining 9 candidates to filter out non-human-disease predictions before further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

