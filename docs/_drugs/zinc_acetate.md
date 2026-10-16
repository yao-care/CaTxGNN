---
layout: default
title: Zinc Acetate
parent: Model Prediction Only (L5)
nav_order: 991
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zinc Acetate: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Dermatitis, rash, Wilson disease and other conditions"
---

# Zinc Acetate
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

# Zinc Acetate: From Dermatitis and Wilson Disease to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Zinc acetate is a zinc salt used for skin conditions (such as dermatitis and rash) and for metal-metabolism disorders such as Wilson disease.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but **no clinical trials and no publications** currently support this prediction. It rests on the model's score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis, rash, Wilson disease and other conditions (the Canadian licence records contain no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zinc acetate is a zinc salt used in skin conditions and in disorders of copper and iron metabolism, and its mechanism may be applicable to the predicted indication.

One speculative link is that zinc is a cofactor for antioxidant enzymes such as copper/zinc superoxide dismutase (Cu/Zn-SOD). Oxidative stress contributes to retinal injury in diabetes, so this could be relevant. No trial or publication in the data compiled for this report supports this link, and it should be treated as a hypothesis only.

The predicted indications ranked 2 to 10 are also supported only by model scores or by indirect literature. They include bronchitis, diabetic retinopathy (closely related to the lead prediction rather than independent evidence), several skin and autoimmune conditions, and urinary tract infection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

Indirect literature exists only for lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32679246](https://pubmed.ncbi.nlm.nih.gov/32679246/) | 2020 | In vitro / materials study | Microbial Pathogenesis | Compares zinc oxide nanoparticles made by two methods against *Staphylococcus aureus*. This is a different compound and not a clinical study in bronchitis (linked to bronchitis, rank 2). |
| [10398312](https://pubmed.ncbi.nlm.nih.gov/10398312/) | 1999 | Clinical study (design unconfirmed) | American Journal of Hematology | Zinc supplementation in sickle cell disease, examining infection incidence and hospital admissions. Indirect evidence only, not specific to UTI (linked to urinary tract infection, rank 10). |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02246156 | POLYSPORIN ITCH RELIEF | Not specified | Not specified |
| 02280868 | BENADRYL BUG BITE RELIEF | Not specified | Not specified |
| 02484838 | BENADRYL ITCH STOPPING CREAM | Not specified | Not specified |
| 02478072 | CHILDREN'S BENADRYL BUG BITE RELIEF | Not specified | Not specified |

All four licences are valid single-ingredient authorizations. The product names suggest topical itch and bug-bite products.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: inherited porphyria, porphyrin metabolism disease and porphyria.
- **Drug Interactions**: 100 interactions were found in the DDI query. The ones listed in the data are mostly Minor and include immunosuppressants and biologics (abatacept, adalimumab, azathioprine) and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone). Moderate interactions include:
  - Bisphosphonates: alendronic acid, risedronic acid, ibandronate
  - Tetracycline
  - Baloxavir marboxil

  These moderate interactions are consistent with zinc binding other drugs and reducing their absorption, but the data do not state a mechanism.

Package insert warnings and contraindications from Health Canada have not been obtained. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for severe nonproliferative diabetic retinopathy has a high model score (99.97%) but no supporting clinical trials or literature (Evidence Level L5). The Canadian licences cover only topical itch and bug-bite products, which are not an obvious fit for a retinal disease. Label-based safety data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications for safety screening
- Detailed mechanism of action data, for example from DrugBank
- A literature search on zinc and diabetic retinopathy, including preclinical oxidative-stress studies
- Assessment of route and formulation compatibility, since the marketed products are topical and a retinal indication would likely need a different route
- Review of the porphyria contraindication signal and the moderate drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

