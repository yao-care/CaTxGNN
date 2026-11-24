---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pegfilgrastim: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastim: From Neutropenia Support (Original Indication Not Listed) to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegfilgrastim is a long-acting, PEGylated form of granulocyte colony-stimulating factor (G-CSF), and eight products are currently licensed in Canada. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy** (and the broader category of diabetic retinopathy). However, **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian license records contain no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (marketed DINs: 8 of 8) |
| Number of DINs | 8 (marketed: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pegfilgrastim: "Pegfilgrastim products are colony-stimulating factor that acts on hematopoietic cells by binding to specific cell surface receptors, thereby stimulating proliferation, differentiation, commitment, and end cell functional activation." ([DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83), label version 2026-10-29; accessed 2026-11-19.) Based on general knowledge, pegfilgrastim is a PEGylated G-CSF that stimulates the production of neutrophils, and it belongs to the class of hematopoietic growth factors. Its use in reducing neutropenia is established, but the data compiled for this report do not list an original indication.

A speculative link to diabetic retinopathy is that G-CSF may mobilize bone marrow-derived endothelial progenitor cells, which could in theory contribute to repair of damaged retinal blood vessels. The effect could also go the other way: increased neutrophil and progenitor-cell activity might promote inflammation and abnormal new vessel growth, which are harmful in the diabetic retina. The direction of effect is therefore uncertain, and nothing in the available data resolves it.

The two predicted indications are not independent. Diabetic retinopathy (score 0.9973) is the broader parent category of severe nonproliferative diabetic retinopathy (score 0.9989), and both come from the same model-derived association. The safety of systemic G-CSF for the retina in people with diabetes has not been established in the data reviewed here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02249790 | NEULASTA | PEGFILGRASTIM | Marketed |
| 02474565 | LAPELGA | PEGFILGRASTIM | Marketed |
| 02484153 | FULPHILA | PEGFILGRASTIM | Marketed |
| 02497395 | ZIEXTENZO | PEGFILGRASTIM | Marketed |
| 02506238 | NYVEPRIA | PEGFILGRASTIM | Marketed |
| 02529343 | LAPELGA | PEGFILGRASTIM | Marketed |
| 02546973 | NIOPEG | PEGFILGRASTIM | Marketed |
| 02553945 | PEXEGRA | PEGFILGRASTIM | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Three more valid single-ingredient licenses are on record: NYVEPRIA (02506238), NIOPEG (02546973) and PEXEGRA (02553945). There are no cancelled licenses.

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. All of the entries reviewed are rated Moderate (source: DDInter). Examples include:
  - Chemotherapy and antineoplastic agents: paclitaxel, mercaptopurine, trimetrexate, azacitidine, arsenic trioxide, altretamine, abemaciclib
  - Biologics and immunotherapies: aldesleukin, alemtuzumab, belantamab mafodotin, asparaginase
  - Radiopharmaceuticals and radioimmunotherapy: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab
  - Others: levamisole, acalabrutinib, avapritinib, pegvaliase

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (L5). There are no clinical trials or publications, and the mechanism is speculative and could plausibly worsen retinal disease through inflammation or abnormal vessel growth. The package insert safety data and the mechanism of action are also missing, so the safety screening step cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text for the Canadian licenses
- A literature and trial search on G-CSF, endothelial progenitor cells and diabetic retinopathy, including retinal safety in diabetic patients
- Preclinical or mechanistic studies to establish whether the effect on the diabetic retina would be protective or harmful
- Assessment of route compatibility (the current formulations are systemic, whereas retinal disease may call for other delivery routes)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

