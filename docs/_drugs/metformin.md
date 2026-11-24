---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). In Canada: at least 20 DINs"
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

## Metformin: Focal stiff limb syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is a widely used oral glucose-lowering drug, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but **no clinical trials and no publications** currently support this direction, so it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 18; dormant: 1; cancelled: 1) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metformin: "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), label version 2026-09-21; accessed 2026-11-19.) Based on known information, metformin is an established biguanide antidiabetic whose efficacy in type 2 diabetes is well proven. Its activation of AMPK and possible immunometabolic effects may, in theory, be applicable to focal stiff limb syndrome, but this link is speculative.

Focal stiff limb syndrome belongs to the stiff-person spectrum, which is autoimmune and involves impaired GABAergic signalling. The data compiled for this report provide no evidence connecting metformin to this pathway.

Several cautions apply:
- The classic stiff person syndrome has an identical score (0.9945), which suggests the model treats the two diseases as closely related rather than providing independent evidence.
- Anti-GAD65 autoimmunity is associated with diabetes. This shared annotation may confound the TxGNN model (deep learning) prediction, which may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions are also unsupported by evidence: classic stiff person syndrome (0.9945), opsismodysplasia (0.9940), thiamine-responsive dysfunction syndrome (0.9940), and drug-induced localized lipodystrophy (0.9906). All are L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and indication text were not available in the data compiled for this report.

<!-- review:begin ca-lic-20261105-metformin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Health Canada lists 20 valid single-ingredient licences, with no cancelled ones. Dosage form and indication text were not available in the data compiled for this report." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-metformin-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02099233 | GLUCOPHAGE | METFORMIN HYDROCHLORIDE | Marketed |
| 02239081 | RIVA-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02242783 | RIVA-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02246821 | SANDOZ METFORMIN FC | METFORMIN HYDROCHLORIDE | Marketed |
| 02257734 | TEVA-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02268493 | GLUMETZA | METFORMIN HYDROCHLORIDE | Marketed |
| 02305062 | APO-METFORMIN ER | METFORMIN HYDROCHLORIDE | Marketed |
| 02385341 | METFORMIN FC | METFORMIN HYDROCHLORIDE | Marketed |
| 02385368 | METFORMIN FC | METFORMIN HYDROCHLORIDE | Marketed |
| 02494418 | AG-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02514486 | METFORMIN TABLETS | METFORMIN HYDROCHLORIDE | Marketed |
| 02534673 | PRZ-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02536439 | NRA-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02547775 | M-METFORMIN | METFORMIN HYDROCHLORIDE | Marketed |
| 02550504 | MAR-METFORMIN XR | METFORMIN HYDROCHLORIDE | Marketed |
| 02550512 | MAR-METFORMIN XR | METFORMIN HYDROCHLORIDE | Marketed |
| 02552027 | TARO-METFORMIN XR | METFORMIN HYDROCHLORIDE | Marketed |
| 02558793 | METFORMIN ER | METFORMIN HYDROCHLORIDE | Marketed |
| 02520311 | PMSC-METFORMIN | METFORMIN HYDROCHLORIDE | Dormant |
| 02162849 | GLUCOPHAGE | METFORMIN HYDROCHLORIDE | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Health Canada lists 20 valid single-ingredient licences, with no cancelled ones" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

