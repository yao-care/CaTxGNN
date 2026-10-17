---
layout: default
title: Ceritinib
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceritinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: Non-small cell lung cancer (ALK-positive)"
monitor_inn: "CERITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "junctional epidermolysis bullosa"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ceritinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK/ROS1 kinase inhibitor, originally used to treat ALK-positive non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but this is a graph-based prediction only.
There are **0 clinical trials** and **0 publications** supporting this specific indication, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (ALK-positive) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ceritinib is a kinase inhibitor targeting ALK and ROS1, and its efficacy in ALK-rearranged non-small cell lung cancer has been established.

No mechanistic link has been identified between ALK/ROS1 inhibition and gingival fibromatosis, which is a benign overgrowth of gum tissue. The very high TxGNN score reflects a pattern in the knowledge graph rather than biological or clinical evidence. The prediction should be treated as a hypothesis only.

Other predicted indications in the top 10 fall into three groups:
- **Lung tumours** (lung hilum carcinoma, pulmonary sulcus neoplasm): these are likely subsets of the already approved NSCLC indication rather than true new uses.
- **Benign or rare lung and other tumours** (fibroma of lung, hamartoma of lung, lung benign neoplasm, lung germ cell tumour): no direct evidence supports benefit.
- **Unrelated genetic disorders** (e.g. junctional epidermolysis bullosa, VCP-related inclusion body myopathy): no known link to ALK inhibition.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

For context, the literature retrieved for other predicted indications mainly covers ceritinib in its approved NSCLC use. This includes the ASCEND-4 phase 3 randomised trial ([PMID 28126333](https://pubmed.ncbi.nlm.nih.gov/28126333/), Lancet, 2017), which compared first-line ceritinib with platinum-based chemotherapy in ALK-rearranged NSCLC. It does not support the predicted new indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02436779 | ZYKADIA | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; literature flags QT prolongation, hypersensitivity/interstitial lung disease, and renal effects of ALK inhibitors as areas for monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples shown):
- **Major**: triamcinolone, budesonide
- **Moderate**: acid-suppressing drugs (famotidine, ranitidine, omeprazole, rabeprazole), other corticosteroids (dexamethasone, hydrocortisone, betamethasone), diabetes drugs (metformin, pioglitazone, alogliptin, acarbose, canagliflozin, albiglutide), aprepitant, loperamide, bisacodyl

A published study has specifically assessed the interaction between ceritinib and proton pump inhibitors ([PMID 28424965](https://pubmed.ncbi.nlm.nih.gov/28424965/)).

Literature also flags QT prolongation with tyrosine kinase inhibitors including ceritinib, and a case of ceritinib hypersensitivity with diffuse infiltrative lung disease. Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score. There are no clinical trials or publications for gingival fibromatosis, and no plausible mechanistic link to ALK/ROS1 inhibition. Ceritinib also carries substantial safety and interaction burdens, which are hard to justify for a benign condition.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale connecting ALK/ROS1 signalling to gingival fibromatosis
- Preclinical or case-level evidence in the proposed indication
- Health Canada package insert warnings and contraindications
- A benefit-risk assessment, given the safety profile in a benign condition
- Evaluation of whether the lung-tumour predictions (hilum carcinoma, pulmonary sulcus neoplasm) are already covered by the approved NSCLC indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

