---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Crizotinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma / lung cancer"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Crizotinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis
{: .text-alpha }

## One-Sentence Summary

Crizotinib is a targeted kinase inhibitor, originally used to treat non-small cell lung carcinoma (ALK-positive and ROS1-positive disease).
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 99.8%), but **no clinical trials and no publications** currently support this prediction.
It is a computational signal only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma / lung cancer (the Canadian licence records list no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, crizotinib is an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases ALK, ROS1 and c-MET. It is approved for ALK-rearranged and ROS1-rearranged non-small cell lung cancer.

Gingival fibromatosis is a benign overgrowth of gum connective tissue. It is not an ALK-, ROS1- or MET-driven malignancy, and the data show no plausible link between these targets and this condition. The high TxGNN score reflects a pattern in the knowledge graph and has no clinical or literature support. The prediction should be regarded as speculative.

Other lower-ranked predictions have some indirect evidence. Examples are lung germ cell tumor, where two broad ALK-altered tumor trials exist, and lung hilum carcinoma, where case reports in ROS1/ALK-positive lung adenocarcinoma overlap with the existing lung cancer indication. These do not change the assessment for the top-ranked indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02384264 | XALKORI | Not listed | Not listed |
| 02384256 | XALKORI | Not listed | Not listed |

Both licences are valid single-ingredient products. None are cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests, ECG and heart rate (case reports describe QT prolongation, bradycardia and fatal liver failure), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 interacting drugs. Among those listed, the following are classified as **Major**: clarithromycin, cisapride, dolasetron, eliglustat and granisetron. Moderate interactions include famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone and budesonide.
- **Reported toxicities in the literature (case reports)**: fatal fulminant liver failure, combined cardiac toxicities (bradycardia, QT prolongation, ventricular rhythm, pericarditis), sick sinus syndrome, erythema multiforme and erosive esophagitis.

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has the highest score but no clinical trials, no literature and no plausible mechanistic link between ALK/ROS1/MET inhibition and gingival fibromatosis. Known serious toxicities (hepatic, cardiac) are difficult to justify for a benign condition without supporting evidence.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess whether any pathway overlaps with gingival fibromatosis
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Preclinical evidence (for example fibroblast or gingival tissue models) showing a biological effect of crizotinib
- A risk-benefit assessment for a benign indication, including route and formulation considerations
- Consideration of other predictions with some indirect evidence, such as lung germ cell tumor, as alternative candidates for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

