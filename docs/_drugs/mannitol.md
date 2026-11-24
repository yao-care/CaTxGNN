---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). In Canada: 10 DINs (9 marketed)"
---

# Mannitol
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

## Mannitol: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain edema, intracranial hypertension, ocular hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are currently **no registered clinical trials** and only **1 general review article** behind this prediction, so the prediction is essentially model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 9 of 10; cancelled: 1) |
| Number of DINs | 10 (marketed: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mannitol: "Mannitol, when administered intravenously, exerts its osmotic diuretic effect as a solute of relatively small molecular size being largely confined to the extracellular space. Mannitol hinders tubular reabsorption of water and enhances excretion of sodium and chloride by elevating the osmolarity of the glomerular filtrate." ([DailyMed: Osmitrol (mannitol) prescribing information, Baxter Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d914965-7001-45cb-ba51-d7c5964b05bc), label version 2025-08-26; accessed 2026-11-19.) Based on known pharmacology, mannitol is an osmotic diuretic. It is filtered by the kidney but poorly reabsorbed, so it draws water into the urine and pulls fluid out of tissues such as the brain.

Nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations lead to water retention and low blood sodium (hyponatremia). In theory, osmotic diuresis could increase free-water excretion. However, this is not a recognized treatment; fluid restriction and urea are the usual approaches. The one retrieved paper is a general review of pitfalls in evaluating hyponatremia and contains no mannitol-specific evidence. The very high prediction score is therefore not supported by clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in diagnosing and treating hyponatremia. It is general background and does not evaluate mannitol. |

## Canada Market Information

Dosage form and approved indication text are not available for these products.

<!-- review:begin ca-lic-20261105-mannitol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Mannitol holds 10 valid single-ingredient authorizations in Canada. Dosage form and approved indication text are not available for these products." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). The Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-mannitol-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00038016 | MANNITOL INJECTION USP | MANNITOL | Marketed |
| 00038024 | MANNITOL INJECTION USP | MANNITOL | Marketed |
| 00060410 | OSMITROL INJECTION 10% | MANNITOL | Marketed |
| 00060437 | OSMITROL INJECTION 20% | MANNITOL | Marketed |
| 00498807 | SORBITOL MANNITOL IRRIGATION | MANNITOL; SORBITOL | Marketed |
| 00799963 | CYSTOSOL W 3% HEXITOLS | MANNITOL; SORBITOL | Marketed |
| 02243176 | MANNITOL INJECTION, USP | MANNITOL | Marketed |
| 02444097 | ADDITIVE SOLUTION SODIUM ADENINE GLUCOSE MANNITOL (SAGM) | ADENINE; DEXTROSE; MANNITOL; SODIUM CHLORIDE | Marketed |
| 02489562 | ARIDOL | MANNITOL | Marketed |
| 02386925 | SAG-M | ADENINE; DEXTROSE; MANNITOL; SODIUM CHLORIDE | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The licences also include another Mannitol Injection USP (00038024), Sorbitol Mannitol Irrigation, Cystosol W 3% Hexitols, SAG-M, and an additive solution of sodium, adenine, glucose and mannitol (SAGM).

<!-- review:begin ca-lic-20261124b-mannitol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The remaining five include another Mannitol Injection USP (00038024)," Reworded without the reference to the earlier licence table, which showed only some of the DINs (and without its counts); the products named are unchanged. The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-mannitol-1 -->

## Safety Considerations

- **Contraindication signals (from the knowledge graph, not label text):** liver failure and liver disease, hepatic coma and encephalopathy, anuria, impaired renal function, pulmonary edema, intracranial hemorrhage, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anemia, sleep apnea syndromes, substance abuse or dependence, and several anxiety and mood-related disorders. These should be checked against the official package insert.
- **Drug Interactions:** 100 interactions are recorded. Among those listed, the one rated **Major** is **amikacin**. Many are **Moderate**, including lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, desvenlafaxine, canagliflozin, dapagliflozin, cisatracurium, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid, diatrizoate and amifostine. Doxycycline is **Minor**.
- Mannitol's volume-expanding effect may worsen pulmonary edema or heart failure, and in nephrogenic diabetes insipidus its diuretic effect may worsen free-water loss and hypernatremia.

Please also refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. There are no clinical trials, and the single retrieved review is general and not specific to mannitol. Mannitol is also not a recognized treatment for this condition. Other top-ranked predictions (such as malignant hyperthermia and periodic paralysis) show only supportive or incidental use of mannitol, not disease-modifying benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Mechanistic or preclinical evidence that osmotic diuresis improves water handling in AVPR2 gain-of-function disease
- Approved indication text and dosage forms for the Canadian licences
- Expert review of the safety risks, particularly fluid and electrolyte effects

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Mannitol holds 10 valid single-ingredient authorizations in Canada" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Osmitrol (mannitol) prescribing information, Baxter Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d914965-7001-45cb-ba51-d7c5964b05bc) |
| 2026-11-24 | Reworded: "The remaining five include another Mannitol Injection USP (00038024)," | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

