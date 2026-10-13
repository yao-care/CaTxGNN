---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pegfilgrastim: From Neutropenia Support (Original Indication Not Listed) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a long-acting, PEGylated form of granulocyte colony-stimulating factor (G-CSF), and eight products are currently licensed in Canada. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy** (and the broader category of diabetic retinopathy). However, **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian license records contain no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, pegfilgrastim is a PEGylated G-CSF that stimulates the production of neutrophils, and it belongs to the class of hematopoietic growth factors. Its use in reducing neutropenia is established, but the data compiled for this report do not list an original indication.

A speculative link to diabetic retinopathy is that G-CSF may mobilize bone marrow-derived endothelial progenitor cells, which could in theory contribute to repair of damaged retinal blood vessels. The effect could also go the other way: increased neutrophil and progenitor-cell activity might promote inflammation and abnormal new vessel growth, which are harmful in the diabetic retina. The direction of effect is therefore uncertain, and nothing in the available data resolves it.

The two predicted indications are not independent. Diabetic retinopathy (score 99.73%) is the broader parent category of severe nonproliferative diabetic retinopathy (score 99.89%), and both come from the same model-derived association. The safety of systemic G-CSF for the retina in people with diabetes has not been established in the data reviewed here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02529343 | LAPELGA | Not specified | Not specified |
| 02249790 | NEULASTA | Not specified | Not specified |
| 02484153 | FULPHILA | Not specified | Not specified |
| 02497395 | ZIEXTENZO | Not specified | Not specified |
| 02474565 | LAPELGA | Not specified | Not specified |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

