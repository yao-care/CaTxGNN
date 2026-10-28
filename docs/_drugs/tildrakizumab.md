---
layout: default
title: Tildrakizumab
parent: Model Prediction Only (L5)
nav_order: 914
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
description: "Tildrakizumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not recorded in the local data"
---

# Tildrakizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tildrakizumab: Severe nonproliferative diabetic retinopathy
{: .text-alpha }

## One-Sentence Summary

Tildrakizumab is a monoclonal antibody that targets the p19 subunit of IL-23, and it is marketed in Canada under the brand name ILUMYA. The data compiled for this report do not list its approved indication.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **no clinical trials and no publications** supporting this direction, so the prediction rests on a computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known information, tildrakizumab is an antibody that blocks the p19 subunit of IL-23, a cytokine that drives the IL-23/IL-17 inflammatory axis.

Chronic inflammation and cytokine signalling have been proposed to contribute to retinal microvascular damage in diabetic retinopathy. This offers a possible link to IL-23 blockade. The link is speculative, because nothing in the data connects IL-23 inhibition to retinopathy outcomes. The high TxGNN score is a computational prediction without clinical corroboration.

A large antibody also raises a delivery question: whether systemic dosing would reach the eye, or whether intravitreal administration would be needed. This would need to be assessed before any translational work.

Other predictions from the model include diabetic retinopathy (0.9953), diabetic cataract (0.9921) and drug-induced osteoporosis (0.9920). The rationale for diabetic cataract is weak, since that condition is driven mainly by polyol pathway activation and oxidative stress. The osteoporosis link is plausible but indirect, through IL-23/IL-17 effects on bone loss, and established therapies already exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02558904 | ILUMYA | Not specified | Not specified |
| 02516098 | ILUMYA | Not specified | Not specified |

## Safety Considerations

**Drug Interactions**: The interaction screening found 78 interacting drugs. The compiled data list the following, including several rated Major:

- **Major**: adalimumab, baricitinib, certolizumab pegol, cladribine
- **Moderate**: roflumilast, tacrolimus, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, cyclosporine, denosumab, and certain vaccines (tetanus toxoid, anthrax, live cholera)
- **Minor**: zinc salts (sulfate, acetate, gluconate, chloride)

Most of the Major and Moderate items are other immunosuppressive or immunomodulatory agents, so combined immunosuppression is the main concern. Live vaccines also warrant caution. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no validated mechanism. Warnings, contraindications and the approved indication are also missing from the compiled data, so safety screening cannot yet proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications and approved indication), which is a blocking gap
- Mechanism of action data from DrugBank
- Preclinical or literature evidence linking IL-23/IL-17 signalling to diabetic retinopathy
- An assessment of route of delivery and ocular penetration (systemic versus intravitreal)
- A comparison against current standard treatments for diabetic retinopathy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

