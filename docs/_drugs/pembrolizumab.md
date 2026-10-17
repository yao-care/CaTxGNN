---
layout: default
title: Pembrolizumab
parent: Model Prediction Only (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pembrolizumab: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer, lung cancer, metastatic melanoma"
monitor_inn: "Pembrolizumab"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung hilum carcinoma", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
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

# Pembrolizumab: From Non-Small Cell Lung Cancer and Metastatic Melanoma to Fibromatosis, Gingival

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor, originally used to treat non-small cell lung cancer, lung cancer and metastatic melanoma.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** were found for this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, lung cancer, metastatic melanoma (the Canadian licence record contains no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pembrolizumab is known to be a monoclonal antibody that targets programmed cell death protein 1 (PD-1, PDCD1). Blocking PD-1 releases the brake on T cells so that they can attack tumour cells. Its efficacy in melanoma and lung cancer is well established.

Gingival fibromatosis, however, is a benign, usually hereditary, overgrowth of gum tissue. It is not a cancer and has no known dependence on PD-1/PD-L1 biology. Immune activation is not an expected treatment strategy for it. The high score therefore looks like a statistical artefact of the model rather than a biologically grounded link, and no mechanistic rationale could be identified.

The other top-ranked predictions show the same pattern. Most are benign or rare genetic conditions (for example inclusion body myopathy, ovarioleukodystrophy, lung hamartoma and lung fibroma) with no plausible PD-1 rationale. A few are lung cancer subtypes (lung hilum carcinoma, pulmonary sulcus neoplasm) that are largely covered by the existing NSCLC indication, so they are not distinct repurposing opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02456869 | KEYTRUDA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low. Direct myelosuppression is not a characteristic effect, but immune-related haematological adverse events can occur |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions. Immune-related adverse events are generally monitored through blood counts, liver, renal and thyroid function |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions** (13 records found; none is specific to the predicted indication):
- **Major:** lenalidomide, pomalidomide, thalidomide
- **Moderate:** corticosteroids, including hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort
- **Target pharmacology:** the antibody acts on PD-1 (PDCD1)

Package insert warnings and contraindications for Canada were not available in the data compiled for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials, literature or mechanistic rationale (Evidence Level L5). Gingival fibromatosis is a benign condition for which immune checkpoint blockade is not expected to help. It also carries a risk of serious immune-related adverse events, so the risk-benefit balance is unfavourable on current information.

**To proceed, the following is needed:**
- A biological rationale linking PD-1 signalling to gingival fibromatosis (for example preclinical or tissue-level data)
- Mechanism of action data
- Health Canada package insert warnings and contraindications
- Indication text for the Canadian licence (DIN 02456869)
- If any repurposing direction is pursued, consider the lung cancer subtypes (lung hilum carcinoma, pulmonary sulcus neoplasm) only after checking whether the existing NSCLC approval already covers them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

