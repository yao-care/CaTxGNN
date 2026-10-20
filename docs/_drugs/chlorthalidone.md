---
layout: default
title: Chlorthalidone
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chlorthalidone: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension, congestive heart failure"
monitor_inn: "CHLORTHALIDONE"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **no clinical trials and no relevant publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure (the Canadian licence records contain no indication text; this is based on the drug's known indications) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorthalidone is a thiazide-like diuretic. Its efficacy in hypertension and congestive heart failure is established, but its mechanistic applicability to primary hereditary glaucoma is unclear.

The high TxGNN score (99.92%) reflects a model-based association only. Systemic thiazide-like diuretics are not a recognized glaucoma treatment, and any effect on aqueous humour dynamics or intraocular pressure is speculative.

Other predictions for this drug are more plausible. Malignant hypertensive renal disease and malignant renovascular hypertension are closely related to the approved hypertension indication. Chronic pulmonary heart disease is related to the approved heart failure indication, and it is the only prediction with directly relevant literature. This report focuses on the top-ranked prediction, as requested.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02523809 | JAMP CHLORTHALIDONE | Not specified | Not specified |
| 00360279 | APO-CHLORTHALIDONE | Not specified | Not specified |
| 02523817 | JAMP CHLORTHALIDONE | Not specified | Not specified |
| 02523795 | JAMP CHLORTHALIDONE | Not specified | Not specified |
| 02248763 | AA-ATENIDONE | Not specified | Not specified |

Eight single-ingredient licences are currently valid, and none are cancelled. The other three valid licences are AA-ATENIDONE (02248764) and EDARBYCLOR (02397749 and 02397765).

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, kidney disease, anuria, gout, type 2 diabetes mellitus, asthma, systemic lupus erythematosus, pancreatitis, peptic ulcer disease, myocardial infarction, hypercalcaemia, potassium deficiency, epilepsy, anxiety disorder, psoriasis and others. These come from a knowledge-graph association and must be verified against the official Canadian product monograph.
- **Drug Interactions**: 100 interactions were identified; the 20 reviewed include:
  - **Major**: cisapride and dolasetron.
  - **Moderate**: antidiabetic agents (metformin, acarbose, alogliptin, albiglutide), corticosteroids (hydrocortisone, dexamethasone, triamcinolone, beclomethasone), amphotericin B, bupropion, morphine, omeprazole, rabeprazole and cholecalciferol.
  - **Minor**: doxycycline, atropine and hyoscyamine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or literature, no established mechanistic link between a systemic thiazide-like diuretic and hereditary glaucoma, and the safety review is incomplete because the product monograph warnings and contraindications have not been obtained.

**To proceed, the following is needed:**
- Mechanism of action data, for example from DrugBank.
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening).
- Preclinical or observational evidence on chlorthalidone and intraocular pressure or aqueous humour dynamics.
- Consideration of reprioritising to better-supported candidates, such as malignant hypertensive renal disease, malignant renovascular hypertension or chronic pulmonary heart disease. The latter has only a 1967 case-level report and a 2017 background review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

