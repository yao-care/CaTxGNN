---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Acarbose: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "ACARBOSE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose was originally used to treat **type 2 diabetes mellitus**.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Canadian licence records contain no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acarbose is an alpha-glucosidase inhibitor that acts locally in the gut, and its efficacy in type 2 diabetes mellitus is established. It slows carbohydrate digestion and so reduces the rise in blood sugar after meals.

The link to focal stiff limb syndrome is weak. This is a rare neurological condition closely related to stiff person syndrome, which is typically autoimmune (often anti-GAD) and frequently occurs alongside diabetes. The model's high score most likely reflects network proximity to diabetes-associated autoimmune neurological conditions, not a pharmacological relationship. Acarbose has no known effect on GABAergic signalling or on the autoimmune process, so the prediction should be treated as a hypothesis only.

The same pattern applies to the other top predictions (classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and several localized lipodystrophies). All are model predictions with no supporting trials or literature, and none has a plausible mechanistic link to acarbose.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

The only publications retrieved were for a lower-ranked prediction, pancreatic agenesis (rank 9). They cover type 2 diabetes, beta-cell preservation, insulin autoimmune syndrome and animal models, and none addresses pancreatic agenesis directly. They therefore do not support the lead prediction.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02494086 | MAR-ACARBOSE | Not listed | Not listed |
| 02494078 | MAR-ACARBOSE | Not listed | Not listed |

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycemia, injury.

**Drug Interactions:** 100 interactions were identified in the DDInter database. The first 20 returned include:
- **Moderate:** acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, asparaginase (Erwinia chrysanthemi and E. coli), atazanavir, bedaquiline, bendroflumethiazide, benzphetamine, benzthiazide, betamethasone
- **Minor:** albiglutide, alclometasone (topical), lipoic acid, amcinonide, anisindione

Many of the moderate interactions involve drugs that can raise blood glucose (such as corticosteroids, thiazides and some antipsychotics), which may reduce the glucose-lowering effect of acarbose. The full list of 100 interactions was not available for review.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or literature, so the evidence level is L5. No plausible pharmacological link exists between a gut alpha-glucosidase inhibitor and focal stiff limb syndrome.

**To proceed, the following is needed:**
- Mechanism of action data for acarbose, to allow a proper mechanistic analysis
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Any clinical or preclinical evidence linking acarbose to focal stiff limb syndrome or stiff person spectrum disorders
- Indication and dosage form details for the two Canadian DINs
- Reassessment of whether other predicted indications have better support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

