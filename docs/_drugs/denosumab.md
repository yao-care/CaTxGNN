---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

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
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 10 of 10) |
| Number of DINs | 10 (marketed: 10) |
| Recommended Decision | Hold |

A second prediction, **diabetic retinopathy** (score 0.9923, also L5, Hold), is discussed in the sections below where relevant.

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for denosumab: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), label version 2026-11-04; accessed 2026-11-19.) Denosumab is known to be a RANKL-neutralizing monoclonal antibody. Its efficacy in osteoporosis is established through this pathway.

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

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02343541 | PROLIA | DENOSUMAB | Marketed |
| 02368153 | XGEVA | DENOSUMAB | Marketed |
| 02545411 | JUBBONTI | DENOSUMAB | Marketed |
| 02545764 | WYOST | DENOSUMAB | Marketed |
| 02560895 | OSENVELT | DENOSUMAB | Marketed |
| 02560917 | STOBOCLO | DENOSUMAB | Marketed |
| 02565951 | BILDYOS | DENOSUMAB | Marketed |
| 02566001 | TUZEMTY | DENOSUMAB | Marketed |
| 02566265 | DENOZA | DENOSUMAB | Marketed |
| 02566273 | IDENOS | DENOSUMAB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-denosumab-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A sixth authorization, STOBOCLO (DIN 02560917), is also valid." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-denosumab-1 -->

All 10 authorizations are single-ingredient products with valid status.

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
The TxGNN scores are very high (0.9963 and 0.9923), but there are no clinical trials and no literature showing an effect of denosumab on retinopathy. The evidence is L5, a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data to anchor the proposed RANKL/RANK/OPG link to retinal or microvascular disease
- Preclinical or mechanistic studies testing denosumab effects in diabetic retinopathy models
- Review of retinopathy outcomes in existing denosumab diabetes cohorts
- Package insert warnings and contraindications from Health Canada, needed before safety screening
- Approved indication text and dosage forms for the Canadian products, to confirm route compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |
| 2026-11-24 | Removed: "A sixth authorization, STOBOCLO (DIN 02560917), is also valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

