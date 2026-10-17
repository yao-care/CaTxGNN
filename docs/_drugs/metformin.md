---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely used oral glucose-lowering drug, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but **no clinical trials and no publications** currently support this direction, so it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Health Canada licence records contain no indication text, so this comes from the model's knowledge graph) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is an established biguanide antidiabetic whose efficacy in type 2 diabetes is well proven. Its activation of AMPK and possible immunometabolic effects may, in theory, be applicable to focal stiff limb syndrome, but this link is speculative.

Focal stiff limb syndrome belongs to the stiff-person spectrum, which is autoimmune and involves impaired GABAergic signalling. The data compiled for this report provide no evidence connecting metformin to this pathway.

Several cautions apply:
- The classic stiff person syndrome has an identical score (99.45%), which suggests the model treats the two diseases as closely related rather than providing independent evidence.
- Anti-GAD65 autoimmunity is associated with diabetes. This shared annotation may confound the graph-based prediction.

Other top predictions are also unsupported by evidence: classic stiff person syndrome (99.45%), opsismodysplasia (99.40%), thiamine-responsive dysfunction syndrome (99.40%), and drug-induced localized lipodystrophy (99.06%). All are L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada lists 20 valid single-ingredient licences, with no cancelled ones. Dosage form and indication text were not available in the data compiled for this report. Five main authorizations are shown below.

| DIN | Product Name |
|---------|------|
| 02099233 | GLUCOPHAGE |
| 02162849 | GLUCOPHAGE |
| 02268493 | GLUMETZA |
| 02257734 | TEVA-METFORMIN |
| 02305062 | APO-METFORMIN ER |

Other marketed products include several metformin generics and extended-release versions, such as MAR-METFORMIN XR, TARO-METFORMIN XR and RIVA-METFORMIN.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The model's knowledge graph links metformin with liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, congestive heart failure, adrenocortical insufficiency, thymus gland disease, pyoureter, and a large group of pituitary and hypogonadotropic disorders (such as hypopituitarism, growth hormone deficiencies, Kallmann syndrome, and Sheehan syndrome). These must be confirmed against the official package insert.
- **Drug Interactions:** 100 interactions are recorded. Examples:
  - **Major:** acetazolamide, ethanol
  - **Moderate:** dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acetohexamide
  - **Minor:** acarbose, topical hydrocortisone, topical alclometasone

Please refer to the package insert for label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is the only support. There are no clinical trials or publications, the mechanism is speculative, and the possible confounding through diabetes and anti-GAD autoimmunity weakens the prediction. The evidence level is L5.

**To proceed, the following is needed:**
- A systematic literature and trial search for metformin in stiff-person spectrum disorders
- Mechanism of action data and a mechanistic rationale for the stiff-person spectrum
- Package insert warnings and contraindications from Health Canada, to allow safety screening
- A check of whether the prediction is only a diabetes-annotation artefact
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

