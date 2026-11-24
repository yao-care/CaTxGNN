---
layout: default
title: Conjugated Estrogens
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Conjugated estrogens"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "heparin cofactor 2 deficiency", "Prinzmetal angina", "hemoglobinopathy", "thrombophilia"]
description: "Conjugated Estrogens: predicted new indication Migraine disorder (evidence level L5). In Canada: 6 DINs (6 marketed)"
---

# Conjugated Estrogens
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

## Conjugated Estrogens: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Conjugated estrogens are a hormone therapy marketed in Canada under several Premarin and Duavive products.
The TxGNN model predicts they may be relevant for **migraine disorder**, but **no clinical trials** and **no publication that tests conjugated estrogens in migraine** are available, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for conjugated estrogens: "Endogenous estrogens are largely responsible for the development and maintenance of the female reproductive system and secondary sexual characteristics. Although circulating estrogens exist in a dynamic equilibrium of metabolic interconversions, estradiol is the principal intracellular human estrogen and is substantially more potent than its metabolites, estrone and estriol, at the receptor level. […] Thus, estrone and the sulfate-conjugated form, estrone sulfate, are the most abundant circulating estrogens in postmenopausal women." ([DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5), label version 2025-05-30; accessed 2026-11-19.) Based on general knowledge, they are a mixture of estrogens that act on estrogen receptors.

Menstrual and perimenopausal migraine is linked to fluctuations in estrogen levels, so stabilising estrogen exposure could in theory change migraine frequency. The clinical literature, however, shows inconsistent effects. Oral conjugated estrogens and cyclic regimens have worsened migraine in some postmenopausal women, while transdermal, continuous regimens tend to be better tolerated. The effect therefore depends on formulation and regimen. Migraine with aura also carries a higher risk of ischaemic stroke, and estrogen adds to that concern.

The model score reflects an association, not proof of benefit. The retrieved publications discuss hormones and migraine in general and do not test conjugated estrogens as a migraine treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29521155](https://pubmed.ncbi.nlm.nih.gov/29521155/) | 2018 | Review | Climacteric | Hormonal fluctuations, especially around the menopausal transition, are an important migraine trigger; effects vary by migraine type |
| [11306204](https://pubmed.ncbi.nlm.nih.gov/11306204/) | 2001 | Cohort | Maturitas | Evaluated how hormone replacement therapy influences primary headaches in postmenopausal women |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral hormone replacement regimens and their effect on migraine course in postmenopausal women |
| [8309263](https://pubmed.ncbi.nlm.nih.gov/8309263/) | 1994 | Review | Mayo Clinic Proceedings | Compared transdermal and oral estrogen therapy across groups of women; not specific to migraine |
| [14195735](https://pubmed.ncbi.nlm.nih.gov/14195735/) | 1964 | Case series | Medizinische Klinik | Treatment of climacteric disorders with conjugated estrogens; not about migraine |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02043386 | PREMARIN INTRAVENOUS | CONJUGATED ESTROGENS | Marketed |
| 02043440 | PREMARIN VAGINAL CREAM | CONJUGATED ESTROGENS | Marketed |
| 02414678 | PREMARIN | CONJUGATED ESTROGENS | Marketed |
| 02414686 | PREMARIN | CONJUGATED ESTROGENS | Marketed |
| 02414694 | PREMARIN | CONJUGATED ESTROGENS | Marketed |
| 02432854 | DUAVIVE | BAZEDOXIFENE (BAZEDOXIFENE ACETATE); CONJUGATED ESTROGENS | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-conjugated_estrogens-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least one more licence (DUAVIVE, DIN 02432854) is also valid." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-conjugated_estrogens-1 -->

All 6 licences are currently valid.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. Examples rated Moderate include acarbose, hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, clarithromycin, aprepitant, clotrimazole and several antidiabetic drugs (e.g. alogliptin, canagliflozin, dapagliflozin, empagliflozin, dulaglutide, chlorpropamide). Cimetidine is rated Minor.
- **Thrombotic and stroke risk**: Estrogens raise thrombotic risk, and migraine with aura already carries a higher ischaemic stroke risk. This is a key concern for any migraine use.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model alone (evidence level L5). No study tests conjugated estrogens in migraine, the published hormone-and-migraine data are inconsistent in direction, and the stroke and thrombotic risks are a real safety concern.

**To proceed, the following is needed:**
- Controlled studies of conjugated estrogens, or specific regimens, in migraine, separating migraine with and without aura
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A stroke and thrombosis risk assessment for migraine populations

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for conjugated estrogens are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5) |
| 2026-11-24 | Removed: "At least one more licence (DUAVIVE, DIN 02432854) is also valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

