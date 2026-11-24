---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: predicted new indication Acne (disease) (evidence level L5). In Canada: at least 20 DINs"
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Clotrimazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is an azole antifungal that has been marketed in Canada for many years.
The TxGNN model predicts it may be useful for **acne**, but the supporting evidence is thin: **1 clinical trial** (a suspended combination-product study) and **no publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for clotrimazole: "Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations." ([DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f), label version 2025-03-27; accessed 2026-11-19.) In general, clotrimazole inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and has reported antimicrobial and anti-inflammatory activity on the skin.

A plausible link to acne is through reduced colonisation by yeasts such as Malassezia or Candida and lower follicular inflammation. This link is indirect. Acne is mainly a disorder of sebum production, follicular blockage, *Cutibacterium acnes* and inflammation, and an antifungal does not directly target these. The high score (0.9986) is a computational prediction only and is not evidence of clinical benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Fixed-dose combination of beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1% cream in subjects with contaminated dermatosis showing bilateral symmetrical lesions. No results reported. |

This trial tested a combination product, so any effect cannot be attributed to clotrimazole alone. The corticosteroid and antibiotic components confound the result. The trial is suspended, and the registry text does not clearly confirm that acne was the studied condition. For these reasons it is not counted as direct evidence for clotrimazole in acne.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Clotrimazole is marketed in Canada, and all 20 single-ingredient licences in the local data are valid. The records are partial. Dosage form and approved-indication text are not recorded in the local data.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00812366 | CLOTRIMADERM VAGINAL 6 | CLOTRIMAZOLE | Marketed |
| 00812374 | CLOTRIMADERM VAGINAL 3 | CLOTRIMAZOLE | Marketed |
| 00812382 | CLOTRIMADERM TOPICAL | CLOTRIMAZOLE | Marketed |
| 02150840 | CANESTEN COMFORTAB 3 | CLOTRIMAZOLE | Marketed |
| 02150859 | CANESTEN COMFORTAB 1 | CLOTRIMAZOLE | Marketed |
| 02150867 | CANESTEN 1% TOPICAL CREAM | CLOTRIMAZOLE | Marketed |
| 02150883 | CANESTEN 1 DAY INTERNAL CREAM | CLOTRIMAZOLE | Marketed |
| 02150891 | CANESTEN 6 DAY INTERNAL CREAM | CLOTRIMAZOLE | Marketed |
| 02229378 | CLOTRIMAZOLE VAGINAL 6 | CLOTRIMAZOLE | Marketed |
| 02229379 | CLOTRIMAZOLE VAGINAL 3 | CLOTRIMAZOLE | Marketed |
| 02229380 | CLOTRIMAZOLE TOPICAL | CLOTRIMAZOLE | Marketed |
| 02230509 | CANESTEN COMBI 1 DAY INTERNAL + EXTERNAL CREAMS | CLOTRIMAZOLE | Marketed |
| 02239432 | CANESTEN EXTERNAL ANTIFUNGAL CREAM | CLOTRIMAZOLE | Marketed |
| 02264102 | CANESTEN COMBI 1 DAY | CLOTRIMAZOLE | Marketed |
| 02311720 | CANESTEN EXTERNAL CREAM | CLOTRIMAZOLE | Marketed |
| 02462397 | CLOTRIMAZOLE EXTERNAL ANTIFUNGAL CREAM | CLOTRIMAZOLE | Marketed |
| 02490927 | CANESTEN EXTRA STRENGTH EXTERNAL ANTIFUNGAL CREAM | CLOTRIMAZOLE | Marketed |
| 02503360 | CLOTRIMAZOLE EXTRA STRENGTH EXTERNAL ANTIFUNGAL CREAM | CLOTRIMAZOLE | Marketed |
| 02547252 | CANESTEN SOFT CAPSULE 1 | CLOTRIMAZOLE | Marketed |
| 02547260 | CANESTEN COMBI 1 DAY SOFT CAPSULE + EXTRA STRENGTH EXTERNAL CREAM | CLOTRIMAZOLE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions include fentanyl, alfentanil, hydrocodone and amiodarone. Moderate-level examples include paclitaxel, abemaciclib, acalabrutinib, nifedipine, amlodipine, apixaban, alprazolam, estradiol, levonorgestrel and norethisterone.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only related trial is a suspended study of a three-drug combination with no results, and no publications address clotrimazole in acne. The mechanistic link is indirect, so the prediction rests on the model score alone.

**To proceed, the following is needed:**
- Mechanism-of-action data for clotrimazole
- Package insert warnings and contraindications from Health Canada
- Preclinical or clinical studies of clotrimazole as a single agent in acne
- Clarification of the condition studied in NCT01244256 and whether the trial will resume
- Assessment of whether a topical formulation suits acne-prone skin

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for clotrimazole is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

