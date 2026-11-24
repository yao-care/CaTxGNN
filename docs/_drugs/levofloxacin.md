---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "LEVOFLOXACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In Canada: 17 DINs (17 marketed)"
---

# Levofloxacin
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

## Levofloxacin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial marketed in Canada in multiple single-ingredient products.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 clinical trials** and only **1 publication** (an outbreak report on a different, microsporidial cause of keratoconjunctivitis), so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 17 of 17) |
| Number of DINs | 17 (marketed: 17) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for levofloxacin: "Levofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] Levofloxacin is the L-isomer of the racemate, ofloxacin, a quinolone antimicrobial agent. The antibacterial activity of ofloxacin resides primarily in the L-isomer. The mechanism of action of levofloxacin and other fluoroquinolone antimicrobials involves inhibition of bacterial topoisomerase IV and DNA gyrase (both of which are type II topoisomerases), enzymes required for DNA replication, transcription, repair and recombination." ([DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5), label version 2026-11-05; accessed 2026-11-19.) Levofloxacin belongs to the fluoroquinolone class of antibacterials, which act by inhibiting bacterial DNA replication. The model likely scored this disease highly because of its similarity to other ocular infections and inflammatory eye conditions.

The link is weak. The only retrieved paper describes an outbreak of microsporidial keratoconjunctivitis from contaminated swimming-pool water. Fluoroquinolones have no established activity against microsporidia, so that report does not support a benefit from levofloxacin. The high score reflects computational proximity, not clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis linked to swimming-pool water contamination in Taiwan; no levofloxacin treatment data |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02284707 | APO-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02284715 | APO-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02298635 | SANDOZ LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02298643 | SANDOZ LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02298651 | SANDOZ LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02314932 | LEVOFLOXACIN IN 5% DEXTROSE INJECTION | LEVOFLOXACIN | Marketed |
| 02315424 | TEVA-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02315432 | TEVA-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02315440 | TEVA-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02325942 | APO-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02415879 | PRO-LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02442302 | QUINSAIR | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02508443 | JAMP LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02508451 | JAMP LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02508478 | JAMP LEVOFLOXACIN | LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |
| 02537079 | LEVOFLOXACIN IN 5% DEXTROSE INJECTION | LEVOFLOXACIN | Marketed |
| 02543745 | LEVODEXA | DEXAMETHASONE (DEXAMETHASONE SODIUM PHOSPHATE); LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD.

<!-- review:begin ca-lic-20261106-levofloxacin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 17 licences in the local records are valid single-ingredient products." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-levofloxacin-1 -->

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 entries. Major-level interactions include tramadol and hydrocortisone. Many moderate-level interactions were also found, including with antidiabetic agents (acarbose, alogliptin, metformin, pioglitazone, albiglutide), NSAIDs (ibuprofen, ketorolac), famotidine, abiraterone, adenosine, alfuzosin, amifampridine, ethinylestradiol, formoterol and salbutamol.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the single retrieved publication concerns a microsporidial outbreak that levofloxacin is not expected to treat. The high TxGNN score is not backed by direct clinical evidence, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or preclinical studies of levofloxacin in punctate epithelial keratoconjunctivitis, including the ocular route and formulation
- Mechanism of action data and an analysis of the likely causative organisms in this condition
- Package insert warnings and contraindications from Health Canada

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

