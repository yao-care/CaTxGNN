---
layout: default
title: Cromoglicic Acid
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
monitor_inn: "Cromoglicic acid"
predicted_indications: ["ulcerative proctosigmoiditis", "nocardiosis", "rosacea conjunctivitis", "cap polyposis", "cutaneous photosensitivity-lethal colitis syndrome", "undetermined colitis", "pneumocystosis", "osteoarthritis", "allergic urticaria", "neonatal inflammatory skin and bowel disease"]
last_modified_at: 2026-11-24
description: "Cromoglicic Acid: predicted new indication ulcerative proctosigmoiditis (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Cromoglicic Acid
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

## Cromoglicic acid: mast cell stabilizer → ulcerative proctosigmoiditis
{: .text-alpha }

## One-Sentence Summary

Cromoglicic acid is a mast cell stabilizer that is currently marketed in Canada as an eye drop and an oral capsule (NALCROM).
The TxGNN model predicts it may be effective for **ulcerative proctosigmoiditis**, with a score of 0.9999.
No clinical trials or publications were found for this disease, so the prediction rests on the model alone.

<!-- review:begin ca-lic-20261124b-cromoglicic_acid-1 -->

> **Review correction (2026-11-24)**: Originally stated: "currently marketed in Canada as an eye drop and a nasal product" Corrected: the dosage forms described here did not match the Health Canada DPD product records (dosage form and route of administration) for the DINs on this page; the sentence now names the forms in those records. The table under Canada Market Information lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-cromoglicic_acid-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | ulcerative proctosigmoiditis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cromoglicic acid is generally known as a mast cell stabilizer. Mast cell activation may contribute to mucosal inflammation in the distal colon in ulcerative colitis, which gives a plausible but unvalidated link to ulcerative proctosigmoiditis.

Oral absorption of the drug is poor (under 1%), so it could in principle act locally in the gut. This is a hypothesis only. No trial or publication was supplied to support it, and the high TxGNN score is a computational prediction rather than evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00500895 | NALCROM | CROMOLYN SODIUM | Marketed |
| 02009277 | CROMOLYN EYE DROPS | CROMOLYN SODIUM | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Both licences are single-ingredient products and both are currently valid.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Only one is rated Moderate: inhaled rapid-acting human insulin. The others shown are of unknown severity, including theophylline, tramadol, lorazepam, valproic acid, erythromycin, fluconazole, metoprolol and valsartan. The clinical significance of these has not been established.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or publications for ulcerative proctosigmoiditis, so it stays at evidence level L5. The mast cell rationale is plausible but untested, and the poor oral absorption makes the route and formulation question important.

**To proceed, the following is needed:**
- A systematic literature search on mast cell stabilizers in ulcerative colitis and proctitis
- Mechanism of action data
- Health Canada package insert warnings and contraindications
- An assessment of whether a rectal or locally acting formulation is feasible
- Preclinical or early clinical data in distal ulcerative colitis

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Reworded: "currently marketed in Canada as an eye drop and a nasal product" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

