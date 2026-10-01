---
layout: default
title: Brigatinib
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib (marketed in Canada as ALUNBRIG) is a kinase inhibitor used to treat ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC); the Health Canada indication text was not supplied, so this comes from the retrieved literature |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Brigatinib is described in the data as an ALK/ROS1/EGFR kinase inhibitor. Its efficacy in ALK-positive NSCLC is well established, including in several Phase 3 trials (ALTA-1L, ALTA-3).

The provided data does not show a mechanistic link between kinase inhibition and gingival fibromatosis. The high TxGNN score (0.9989, model rank 2770) is a graph-based prediction only. No trial or publication addresses this condition, and the relationship to the original indication has not been assessed.

This is the top-ranked prediction, but it is not the best-supported one among brigatinib's candidates.

- **NF2-related schwannomatosis and NF2-deficient tumors:** a clinical case series (NEJM 2024) and preclinical work show brigatinib-associated tumor shrinkage.
- **ALK-altered non-NSCLC tumors:** case reports and preclinical work in pheochromocytoma, lung large cell neuroendocrine carcinoma, and neuroblastoma.

These signals came up under other predicted diseases (ranks 8 and 10). They are indirect and do not support gingival fibromatosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2479214 | ALUNBRIG |
| 2479206 | ALUNBRIG |
| 2479222 | ALUNBRIG |
| 2479230 | ALUNBRIG |

Dosage form and approved indication text were not supplied for these authorizations.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

One published case report describes **fatal tumour lysis syndrome** after brigatinib in a patient with ALK-rearranged lung adenocarcinoma who had received sequential ALK inhibitors (PMID 34987411). It is a single case in an oncology setting, but it shows that serious metabolic complications can occur.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no relevant literature, and no demonstrated mechanistic link between brigatinib's kinase targets and gingival fibromatosis. Brigatinib is a marketed oncology drug with a known serious-toxicity profile, so a repurposing case needs direct evidence first.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data, and an assessment of whether the relevant kinases play a role in gingival fibromatosis
- Preclinical or case-level evidence specific to gingival fibromatosis
- Evaluation of route and dosage-form compatibility (only oral use is implied by current data; this has not been confirmed)
- Consideration of the better-supported NF2-related schwannomatosis signal as a separate repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

