---
layout: default
title: Trolamine Salicylate
parent: Model Prediction Only (L5)
nav_order: 952
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Trolamine Salicylate: predicted new indication Exostosis (evidence level L5). Approved use: Not stated in the licence records. Product names suggest topical pain…"
monitor_inn: "TROLAMINE SALICYLATE"
predicted_indications: ["exostosis", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "fibromyalgia", "inclusion body myositis", "exostoses, multiple,", "rheumatoid arthritis", "headache disorder", "gout"]
---

# Trolamine Salicylate
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

## Trolamine Salicylate: From Topical Musculoskeletal Pain Relief to Exostosis
{: .text-alpha }

## One-Sentence Summary

Trolamine salicylate is a topical salicylate marketed in Canada in creams and rubs for muscle, joint and arthritis pain. The TxGNN model predicts it may be effective for **exostosis** (score 0.9975), but **no clinical trials and no publications** were found to support this prediction. It is a model-only signal (evidence level L5), and the most biologically coherent prediction in the list is tendinitis, not exostosis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records. Product names suggest topical pain relief (muscle, joint, arthritis) |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 11 of 11) |
| Number of DINs | 11 (marketed: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, trolamine salicylate is a topical salicylate with analgesic and anti-inflammatory activity. It is applied to the skin to relieve local musculoskeletal pain.

Such an action could ease pain, but it has no plausible effect on the bony outgrowth that defines exostosis. The high score therefore looks like a model-level association rather than a verified mechanistic link, and similarity to the original indication has not yet been assessed.

**Other predictions from the model** (all with no trials or literature, all evidence level L5, all Hold):

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Tendinitis | 0.9970 | Most coherent: symptomatic relief of local musculoskeletal inflammation and pain. This is general pharmacology, not evidence from the data |
| 3 | Myositis fibrosa | 0.9965 | At most symptomatic analgesia. Tied score with rank 4 may reflect similarities the model learned between related diseases, not biological evidence |
| 4 | Idiopathic granulomatous myositis | 0.9965 | Immune-mediated, so topical salicylate is unlikely to address the pathology |
| 5 | Fibromyalgia | 0.9959 | Central sensitization, so limited benefit from a topical peripheral analgesic |
| 6 | Inclusion body myositis | 0.9946 | Poorly responsive to anti-inflammatory therapy. No disease-modifying role |
| 7 | Exostoses, multiple | 0.9943 | Hereditary (EXT1/EXT2). No mechanistic link to salicylates |
| 8 | Rheumatoid arthritis | 0.9925 | At best adjunctive relief of localized joint pain. No disease-modifying effect |
| 9 | Headache disorder | 0.9923 | Minimal systemic absorption from the topical form, so extrapolation is weak |
| 10 | Gout | 0.9918 | Urate effects apply to systemic dosing, not topical use |

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
| 02074702 | EXTRA STRENGTH ASPERCREME CREME RUB 15% | TROLAMINE SALICYLATE | Marketed |
| 02152827 | MYOFLEX REGULAR STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02226022 | MYOFLEX EXTRA STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02244573 | MYOFLEX MAXIMUM STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02358131 | PAIN RELIEF CREAM REGULAR STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02410907 | PAIN RELIEF RUB TRIETHANOLAMINE SALICYLATE CREAM | TROLAMINE SALICYLATE | Marketed |
| 02413442 | PAIN RELIEF CREAM EXTRA STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02473135 | MUSCLE & JOINT NO ODOUR EXTRA STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02473143 | MUSCLE & JOINT NO ODOUR REGULAR STRENGTH | TROLAMINE SALICYLATE | Marketed |
| 02486725 | ARTHRITIS PAIN RELIEF | CAPSAICIN; MENTHOL; TROLAMINE SALICYLATE | Marketed |
| 02516713 | FLEXACRÈME PAIN RELIEF RUB | TROLAMINE SALICYLATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-trolamine_salicylate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The remaining six are Myoflex Maximum Strength, Pain Relief Cream Extra Strength, Flexacrème Pain Relief Rub, Myoflex Regular Strength, Pain Relief Rub Triethanolamine Salicylate Cream and Arthritis Pain Relief." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-trolamine_salicylate-1 -->

The table above lists each DIN with its current status in the DPD. No licences are cancelled.

<!-- review:begin ca-lic-20261106-trolamine_salicylate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "These are 5 of 11 valid single-ingredient licences." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-trolamine_salicylate-1 -->

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications support it, and the mechanism does not plausibly link a topical analgesic to bony outgrowth. Safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism of action data for trolamine salicylate
- A systematic literature and trial-registry search, prioritizing tendinitis as the most plausible candidate and, secondarily, localized joint pain in rheumatoid arthritis
- Approved indication text and dosage forms for the Canadian licences
- Assessment of route compatibility and similarity to the original indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-24 | Removed: "The remaining six are Myoflex Maximum Strength, Pain Relief Cream Extra Strength, Flexacrème Pain Relief Rub, Myoflex Regular Strength, Pain Relief Rub Triethanolamine Salicylate Cream and Arthritis Pain Relief." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

