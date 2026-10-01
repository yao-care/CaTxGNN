---
layout: default
title: Selpercatinib
parent: Model Prediction Only (L5)
nav_order: 835
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Selpercatinib: From RET-Driven Cancers to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib (brand name RETEVMO) is a selective RET kinase inhibitor. The supplied literature points to RET fusion-positive non-small-cell lung cancer as its established use.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **0 clinical trials** and **2 publications** that do not address this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records provided; the literature points to RET fusion-positive non-small-cell lung cancer |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Selpercatinib is known to be a selective RET kinase inhibitor, and its efficacy has been studied in RET fusion-positive lung cancer. A link to pulmonary hypertension could only be speculative, for example through kinase signalling in pulmonary vascular remodelling. The data provided do not support such a link.

The high TxGNN score (0.992) comes from the knowledge graph alone. Hypertension is a known adverse effect of RET inhibitors, which argues against a benefit in pulmonary hypertension rather than for one.

The model also ranked two migraine-related conditions highly: migraine disorder (99.17%) and migraine with brainstem aura (99.05%). Neither has any trials or literature. The second prediction is likely correlated with its parent condition and is not independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Pharmacovigilance study | Front Pharmacol | Real-world FAERS comparison of adverse events between pralsetinib and selpercatinib; a safety study, not evidence of benefit in pulmonary hypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective cohort | Ther Adv Med Oncol | SIREN: real-world use of selpercatinib in RET fusion-positive NSCLC through an access program; supports the original oncology use, not the predicted indication |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2516926 | RETEVMO |
| 2516918 | RETEVMO |

Dosage form and approved indication text are not recorded for these licenses.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Hypertension** is a known adverse effect of RET inhibitors. This is relevant when considering use in pulmonary hypertension.

Please refer to the package insert for further safety information, including warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, and neither publication addresses pulmonary hypertension. No supported mechanistic link exists, and the known hypertensive effect of RET inhibitors argues against benefit.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) to assess any plausible link to pulmonary vascular biology
- Health Canada package insert warnings and contraindications, which block safety screening
- Preclinical or observational evidence specific to pulmonary hypertension
- Approved indication, dosage form and route data for the two RETEVMO DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

