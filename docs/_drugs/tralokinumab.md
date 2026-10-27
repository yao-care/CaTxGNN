---
layout: default
title: Tralokinumab
parent: Model Prediction Only (L5)
nav_order: 926
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tralokinumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Tralokinumab"
predicted_indications: ["diabetic cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "mature cataract", "craniostenosis cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic retinopathy"]
---

# Tralokinumab
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

## Tralokinumab: From an Approved Anti-IL-13 Biologic to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Tralokinumab is an anti-IL-13 monoclonal antibody that is marketed in Canada under the brand name ADTRALZA. The data compiled for this report did not include the approved indication text.
The TxGNN model predicts it may be effective for **diabetic cataract**, but this prediction is based on the model alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the licence records contain no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.69% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Tralokinumab is known to be an anti-IL-13 monoclonal antibody, meaning it blocks a type 2 inflammatory cytokine. Its approved Canadian indication could not be confirmed from the data compiled for this report.

The link to diabetic cataract rests only on a TxGNN knowledge-graph prediction. IL-13 is not an established driver of lens opacity in diabetes. Diabetic cataract is driven mainly by polyol pathway activation, oxidative stress and glycation, so a mechanistic connection to IL-13 blockade is not supported.

The same score of about 98.6% appears across many cataract subtypes (immature, mature, cortical, nuclear, senile, tetanic, craniostenosis-associated and type 2 diabetes-associated). This suggests the prediction may be an artifact of graph propagation across related disease nodes rather than a drug-specific signal.

Among the other top-ranked predictions, **diabetic retinopathy** (score 98.40%) is the most biologically plausible. It has an inflammatory component, and type 2 cytokines are of speculative interest. It remains hypothesis-level, with no supporting trials or literature.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02540193 | ADTRALZA | Not specified | Not specified |
| 02521288 | ADTRALZA | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). No clinical trials or publications were found, and there is no plausible IL-13-mediated mechanism in lens opacification. Safety information from the Canadian package insert has also not been reviewed, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert to obtain the approved indication, warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Conduct a targeted literature review of IL-13 in lens biology and in retinal inflammation and vascular permeability
- Consider prioritising diabetic retinopathy over the cataract subtypes for any follow-up, as it is the most biologically plausible of the predicted indications
- Confirm route-of-administration compatibility. Ophthalmic use would require evidence beyond the currently marketed formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

