---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Denosumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Osteoporosis (including postmenopausal osteoporosis and drug-induced…"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a monoclonal antibody originally used to treat osteoporosis, including postmenopausal and drug-induced osteoporosis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
This is a computational prediction only, with **0 clinical trials** and **0 publications** directly supporting this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (including postmenopausal osteoporosis and drug-induced osteoporosis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

A second prediction, **diabetic retinopathy** (score 99.23%, also L5, Hold), is discussed in the sections below where relevant.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Denosumab is known to be a RANKL-neutralizing monoclonal antibody. Its efficacy in osteoporosis is established through this pathway.

A plausible but unvalidated link is that RANKL/RANK/OPG signaling is involved in vascular calcification, inflammation, and endothelial dysfunction. These processes may relate to microvascular disease in diabetes. No direct evidence has been shown for effects on the retina.

For the broader diabetic retinopathy prediction, two publications give only indirect context. A 2024 real-world cohort analysis with meta-analysis suggests denosumab is associated with a lower incidence of type 2 diabetes and lower risk of foot ulceration compared with bisphosphonates. It does not assess retinopathy outcomes as an established finding. The other is a fracture-risk study in people with type 2 diabetes. Neither shows that denosumab affects the onset or progression of retinopathy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly addresses severe nonproliferative diabetic retinopathy. For the related prediction of diabetic retinopathy, the following indirectly relevant publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observational / meta-analysis (inferred from title) | Diabetes, Obesity & Metabolism | Real-world cohort data with systematic review: denosumab vs bisphosphonates in relation to type 2 diabetes incidence, foot ulceration and all-cause mortality; microvascular outcomes including retinopathy were among the outcomes examined |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observational (inferred from title) | Cureus | Use of the FRAX fracture risk tool in adults with type 2 diabetes; concerns osteoporosis risk stratification, not retinopathy treatment |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02343541 | PROLIA | Not specified | Not specified |
| 02368153 | XGEVA | Not specified | Not specified |
| 02560895 | OSENVELT | Not specified | Not specified |
| 02545764 | WYOST | Not specified | Not specified |
| 02545411 | JUBBONTI | Not specified | Not specified |

A sixth authorization, STOBOCLO (DIN 02560917), is also valid. All 6 authorizations are single-ingredient products with valid status.

---

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 records. The ones listed are all rated Moderate. Main examples:
- Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone
- Immunosuppressants and immunomodulators: tacrolimus, mercaptopurine, levamisole, dupilumab
- Radiopharmaceuticals and related agents: ibritumomab tiuxetan, iobenguane (I-131), tositumomab
- Others: trimetrexate, corticotropin, tetracosactide

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN scores are very high (99.63% and 99.23%), but there are no clinical trials and no literature showing an effect of denosumab on retinopathy. The evidence is L5, a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data to anchor the proposed RANKL/RANK/OPG link to retinal or microvascular disease
- Preclinical or mechanistic studies testing denosumab effects in diabetic retinopathy models
- Review of retinopathy outcomes in existing denosumab diabetes cohorts
- Package insert warnings and contraindications from Health Canada, needed before safety screening
- Approved indication text and dosage forms for the Canadian products, to confirm route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

