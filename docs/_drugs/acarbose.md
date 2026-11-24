---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
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

## Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Acarbose was originally used to treat **type 2 diabetes mellitus**.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Canadian licence records contain no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for acarbose: "In contrast to sulfonylureas, Acarbose Tablets do not enhance insulin secretion. The antihyperglycemic action of acarbose results from a competitive, reversible inhibition of pancreatic alpha-amylase and membrane-bound intestinal alpha-glucoside hydrolase enzymes." ([DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a), label version 2026-08-11; accessed 2026-11-19.) Based on known information, acarbose is an alpha-glucosidase inhibitor that acts locally in the gut, and its efficacy in type 2 diabetes mellitus is established. It slows carbohydrate digestion and so reduces the rise in blood sugar after meals.

The link to focal stiff limb syndrome is weak. This is a rare neurological condition closely related to stiff person syndrome, which is typically autoimmune (often anti-GAD) and frequently occurs alongside diabetes. The model's high score most likely reflects network proximity to diabetes-associated autoimmune neurological conditions, not a pharmacological relationship. Acarbose has no known effect on GABAergic signalling or on the autoimmune process, so the prediction should be treated as a hypothesis only.

The same pattern applies to the other top predictions (classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and several localized lipodystrophies). All are model predictions with no supporting trials or literature, and none has a plausible mechanistic link to acarbose.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

The only publications retrieved were for a lower-ranked prediction, pancreatic agenesis (rank 9). They cover type 2 diabetes, beta-cell preservation, insulin autoimmune syndrome and animal models, and none addresses pancreatic agenesis directly. They therefore do not support the lead prediction.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02494078 | MAR-ACARBOSE | ACARBOSE | Marketed |
| 02494086 | MAR-ACARBOSE | ACARBOSE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

