---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 1
monitor_inn: "AMMONIUM CHLORIDE"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-24
description: "Ammonium Chloride: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
---

# Ammonium Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ammonium Chloride: From Pharyngitis, Common Cold and Nasopharyngitis to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Ammonium chloride is an ingredient in cough and cold syrups.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (relations recorded in the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is used in cough and cold syrups. Mechanistically, it may be applicable to nasal cavity disease through thinning of mucus and clearance of secretions.

This link is plausible but unverified. No clinical or mechanistic data were compiled to support it for nasal cavity disease specifically. The predicted indication is also broad. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00535230 | CALMYLIN | AMMONIUM CHLORIDE; CODEINE PHOSPHATE; DIPHENHYDRAMINE HYDROCHLORIDE | Marketed |
| 00690074 | COUGH SYRUP | AMMONIUM CHLORIDE; CODEINE PHOSPHATE; DIPHENHYDRAMINE HYDROCHLORIDE | Marketed |
| 02245592 | DAMYLIN WITH CODEINE SYRUP | AMMONIUM CHLORIDE; CODEINE PHOSPHATE; DIPHENHYDRAMINE HYDROCHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD. The licence records compiled for this report contain no indication text.

<!-- review:begin ca-lic-20261106-ammonium_chloride-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All three are valid single-ingredient licences." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-ammonium_chloride-1 -->

## Safety Considerations

- **Contraindications (relations recorded in the knowledge graph, not label text)**: The knowledge graph links ammonium chloride to many conditions, including:
  - Cardiovascular: hypertension, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease, pulmonary edema
  - Liver and kidney: liver failure, impaired renal function, anuria, nephrocalcinosis
  - Metabolic and endocrine: hypercalcemia, phosphorus metabolism disease, adrenocortical insufficiency, Addison disease, hyperthyroidism, Graves disease, thyrotoxicosis
  - Eye: angle-closure glaucoma, ocular hypertension
  - Neuropsychiatric: epilepsy, insomnia, anxiety disorder, agoraphobia, obsessive-compulsive disorder
  - Other: peptic ulcer disease, benign prostatic hyperplasia, bladder neck obstruction, necrotizing enterocolitis
- **Drug Interactions**: 21 interactions were found.
  - Moderate: amphetamine, benzphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine
  - Minor (examples): ephedrine, pseudoephedrine, methadone, mexiletine, flecainide, and tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin, imipramine, nortriptyline, protriptyline, trimipramine)

Label warnings and contraindications from the Canadian package inserts were not available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trials or publications address nasal cavity disease, so the evidence level is L5. The predicted indication is broad, and label safety data are missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (to be downloaded and reviewed)
- Mechanism of action data (for example, from DrugBank)
- Indication text for the three Canadian licences
- A literature and trial search specific to nasal cavity disease
- Clarification of which specific nasal conditions are being targeted, and route and formulation compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

