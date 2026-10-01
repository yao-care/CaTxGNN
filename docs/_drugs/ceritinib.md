---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Ceritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK inhibitor. The published literature describes it for ALK-rearranged non-small cell lung cancer (NSCLC), although the Canadian license record supplied here does not state an indication.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **0 clinical trials** and **0 publications** were found for this prediction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-rearranged NSCLC (from published literature; not stated in the supplied license record) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ceritinib inhibits the receptor tyrosine kinases ALK, ROS1 and IGF-1R. Its established use is in cancers driven by ALK rearrangement, and the ASCEND-4 Phase 3 trial (PMID 28126333) compared it with platinum chemotherapy in ALK-rearranged NSCLC.

For gingival fibromatosis, a benign overgrowth of gum tissue, no mechanistic link to ALK, ROS1 or IGF-1R signalling is documented. The high score (99.86%, model rank 3,435) is a knowledge-graph prediction, not a finding supported by laboratory or clinical data. It should be treated as a hypothesis to test, not a reason to use the drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2436779 | ZYKADIA |

The supplied record does not include the dosage form or the approved indication text.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/IGF-1R kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert. Literature on ceritinib also flags QT prolongation and cardiac toxicity, so ECG and cardiac monitoring should be considered |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available in the supplied data, so please refer to the package insert for safety information.

The literature retrieved for other predicted indications reports the following ceritinib safety signals. They are not specific to gingival fibromatosis but would matter in any future assessment:
- QT prolongation (PMID 29413968)
- Hypersensitivity with interstitial lung disease, pericarditis and pleural effusion (PMID 31280988)
- Cardiac toxicities in pharmacovigilance analyses (PMID 34418561)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no documented mechanism, so it stays at evidence level L5. Ceritinib also carries meaningful oncology-grade toxicity, which is hard to justify for a benign condition without efficacy data.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- A plausible mechanistic hypothesis linking ALK, ROS1 or IGF-1R signalling to gingival fibromatosis, backed by preclinical or tissue-level evidence
- A benefit-risk assessment against existing treatments for gingival fibromatosis
- A check of the other nine predictions for stronger candidates. Several (for example lung hilum carcinoma and pulmonary sulcus neoplasm) are plausible only if the tumour is ALK-driven, and none has direct trial evidence in the supplied data.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

