---
layout: default
title: Dextroamphetamine
parent: Model Prediction Only (L5)
nav_order: 273
evidence_level: L5
indication_count: 7
monitor_inn: "Dextroamphetamine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "multiple system atrophy", "variably protease-sensitive prionopathy", "postural orthostatic tachycardia syndrome", "trichotillomania"]
last_modified_at: 2026-11-25
description: "Dextroamphetamine: predicted new indication faciodigitogenital syndrome (evidence level L5). In Canada: 7 DINs (7 marketed)"
---

# Dextroamphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Dextroamphetamine: catecholamine-releasing CNS stimulant → faciodigitogenital syndrome
{: .text-alpha }

## One-Sentence Summary

Dextroamphetamine is a central nervous system stimulant that releases catecholamines and blocks their reuptake, and it is marketed in Canada.
The TxGNN model predicts it may be useful for **faciodigitogenital syndrome**, but **no clinical trials and no publications** directly support this prediction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | faciodigitogenital syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 7 of 7) |
| Number of DINs | 7 (marketed: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dextroamphetamine releases catecholamines and inhibits their reuptake (through TAAR1, VMAT2 and the dopamine transporter). According to the Clinical Pharmacology section of the US FDA-approved prescribing information for dextroamphetamine: "Amphetamines are noncatecholamine, sympathomimetic amines with CNS stimulant activity. Peripheral actions include elevations of systolic and diastolic blood pressures and weak bronchodilator and respiratory stimulant action." ([DailyMed: Dextroamphetamine Sulfate Extended-Release (dextroamphetamine sulfate) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69c40af8-3710-46bf-bd3d-137fe5eea23e), label version 2025-12-08; accessed 2026-11-20.)

Faciodigitogenital syndrome (Aarskog-Scott syndrome, FGD1-related) can include ADHD-like behavioural features. A stimulant could in principle ease those symptoms. This is an inference only: it would be symptom management, not disease modification, and no study in the data compiled for this report tests it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 01924516 | DEXEDRINE | DEXTROAMPHETAMINE SULFATE | Marketed |
| 01924559 | DEXEDRINE SPANSULE | DEXTROAMPHETAMINE SULFATE | Marketed |
| 01924567 | DEXEDRINE SPANSULE | DEXTROAMPHETAMINE SULFATE | Marketed |
| 02443236 | DEXTROAMPHETAMINE | DEXTROAMPHETAMINE SULFATE | Marketed |
| 02448319 | TEVA-DEXTROAMPHETAMINE SR | DEXTROAMPHETAMINE SULFATE | Marketed |
| 02448327 | TEVA-DEXTROAMPHETAMINE SR | DEXTROAMPHETAMINE SULFATE | Marketed |
| 02566605 | PMS-DEXTROAMPHETAMINE | DEXTROAMPHETAMINE SULFATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All of the single-ingredient licences are valid; the current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information.

<!-- review:begin ca-lic-20261125b-dextroamphetamine-1 -->

> **Review correction (2026-11-25)**: Originally stated: "All six single-ingredient licences are valid." Corrected: DINs marketed after the March 2026 DPD extract were added to the evidence for this page (same matching rule as the original collector), so the earlier count no longer applies. The current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261125b-dextroamphetamine-1 -->

## Safety Considerations

- **Drug Interactions**: 62 interactions were recorded. Examples of major-level interactions are bupropion, dexfenfluramine, fenfluramine and sibutramine. Moderate-level examples include epinephrine, ephedrine, isometheptene, and several antacids and alkalinising agents (aluminum hydroxide, calcium carbonate, magnesium hydroxide, magnesium oxide, potassium citrate).
- **Conditions of concern**: The data compiled for this report flag caution in hypertension, cardiovascular and cerebrovascular disease, epilepsy, bipolar and psychotic disorders, glaucoma, hyperthyroidism, anorexia nervosa and substance-related disorders. These are not taken from label text. Please confirm against the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9999) but no trials or literature on faciodigitogenital syndrome, so the evidence level is L5. Any plausible benefit is limited to treating ADHD-like symptoms, not the underlying disease.

**To proceed, the following is needed:**
- Case series or trials of stimulant use in FGD1-related (Aarskog-Scott) syndrome, particularly for behavioural symptoms
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data
- A cardiovascular and psychiatric safety assessment for this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data are not otherwise available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dextroamphetamine Sulfate Extended-Release (dextroamphetamine sulfate) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69c40af8-3710-46bf-bd3d-137fe5eea23e) |
| 2026-11-25 | Corrected: "All six single-ingredient licences are valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

