---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Glimepiride: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea used to lower blood glucose in type 2 diabetes. The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from the drug class; the Canadian licence records contain no indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Glimepiride blocks the K-ATP channel (SUR1) on pancreatic beta cells, which stimulates insulin secretion. The Evidence Pack has no formal MOA entry for this drug, so this description comes from the mechanistic analysis in the pack.

On mechanism, the prediction is weak. Stiff person syndrome is an autoimmune disorder of GABAergic signalling, usually with anti-GAD65 antibodies. No plausible pathway links K-ATP channel blockade to the central motor-inhibition problem in this disease. The only connection is epidemiological: stiff person syndrome often co-occurs with type 1 diabetes and other autoimmune conditions. That would make glimepiride a treatment for a comorbidity, not for the disease itself. The high score (rank 5,493 in the model) most likely reflects graph proximity rather than biology.

The same pattern holds for the other top predictions:
- **Focal stiff limb syndrome** has the same score and no plausible mechanism.
- **Opsismodysplasia** has only a loose link through SHIP2 and insulin signalling.
- **Thiamine-responsive dysfunction syndrome** has a diabetes component that a sulfonylurea could treat symptomatically. Thiamine remains first-line therapy.
- **Four localized lipodystrophy conditions** have no plausible pharmacological rationale.
- **Pancreatic agenesis** is unlikely to respond, because beta cells are absent and insulin replacement is standard.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2269619 | SANDOZ GLIMEPIRIDE |
| 2269597 | SANDOZ GLIMEPIRIDE |
| 2269589 | SANDOZ GLIMEPIRIDE |

## Safety Considerations

- **Hypoglycemia risk**: This is the main safety concern if a sulfonylurea were given to patients who are not diabetic or who have limited glycemic reserve. The mechanistic analysis flags it for the stiff person syndrome population.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high (99.75%), but there are no supporting trials or publications and no plausible mechanism. The evidence is model prediction only (L5). The prediction looks like a graph artifact driven by diabetes and autoimmunity links.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Formal mechanism-of-action data from DrugBank
- Any preclinical or clinical signal for glimepiride in stiff person syndrome, such as case reports or a targeted literature search
- Confirmation of the approved indication text and dosage forms for the three DINs
- A hypoglycemia risk assessment for the target population, if any further evaluation goes ahead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

