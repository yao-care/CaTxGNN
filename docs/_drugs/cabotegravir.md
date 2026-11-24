---
layout: default
title: Cabotegravir
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Cabotegravir: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the Canadian licence data compiled for this report (cab…"
monitor_inn: "CABOTEGRAVIR"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
---

# Cabotegravir
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

## Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor marketed in Canada under several brand names (APRETUDE, VOCABRIA, CABENUVA).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **no clinical trials and no publications** supporting this prediction. It rests on a model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data compiled for this report (cabotegravir is known as an HIV-1 integrase inhibitor) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for cabotegravir: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), label version 2025-04-11; accessed 2026-11-19.) Cabotegravir is generally known as an HIV-1 integrase strand transfer inhibitor, and its activity is specific to the viral integrase enzyme.

No established mechanism links cabotegravir to rheumatoid arthritis or to immune and inflammatory pathways. The high TxGNN score reflects a TxGNN model (deep learning) prediction only, so any biological connection is speculative and unsupported by trials or literature.

Other top-ranked predictions are similarly weakly supported: sclerosing cholangitis (0.9922), bronchitis (0.9919), colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9916) and severe nonproliferative diabetic retinopathy (0.9903). All are L5 with no trials or literature. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02497204 | VOCABRIA | CABOTEGRAVIR (CABOTEGRAVIR SODIUM) | Marketed |
| 02497220 | CABENUVA | CABOTEGRAVIR; RILPIVIRINE | Marketed |
| 02497247 | CABENUVA | CABOTEGRAVIR; RILPIVIRINE | Marketed |
| 02547465 | APRETUDE | CABOTEGRAVIR (CABOTEGRAVIR SODIUM) | Marketed |
| 02547473 | APRETUDE | CABOTEGRAVIR | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD.

<!-- review:begin ca-lic-20261106-cabotegravir-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All five licences are valid single-ingredient authorizations; none are cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-cabotegravir-1 -->

---

## Safety Considerations

**Drug Interactions** (7 moderate-level interactions identified, all with polyvalent-cation antacids or buffering agents):
- Calcium carbonate
- Aluminum hydroxide
- Magnesium carbonate
- Magnesium hydroxide
- Magnesium oxide
- Sodium bicarbonate
- Sodium citrate

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no literature, and no plausible mechanistic link between an HIV integrase inhibitor and rheumatoid arthritis. Safety information from the package insert is also not yet available.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a credible hypothesis linking integrase inhibition to rheumatoid arthritis pathways
- Health Canada package insert warnings and contraindications
- Approved indication text and dosage form details for the Canadian licences
- Preclinical or early clinical evidence in rheumatoid arthritis
- Route and formulation compatibility assessment (cabotegravir is available in oral and long-acting injectable products, which would need to fit the new indication)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

