---
layout: default
title: Imipenem
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "eosinophilia-myalgia syndrome"]
description: "Imipenem: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Imipenem
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

## Imipenem: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Imipenem is a carbapenem antibacterial that inhibits bacterial cell wall synthesis and is marketed in Canada as an injectable product.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, with a score of 0.9999.
**No clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacology, imipenem is a carbapenem that kills bacteria by blocking cell wall synthesis.

Diffuse scleroderma is an autoimmune, fibrotic disease. It is not driven by a bacterial infection, and no mechanistic link between an antibacterial's mode of action and the disease process is supported. The very high TxGNN score is a computational prediction only. Without trials or literature, it should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02351706 | TARO-IMIPENEM-CILASTATIN | Not recorded | Not recorded |
| 02358344 | IMIPENEM AND CILASTATIN FOR INJECTION USP | Not recorded | Not recorded |

Both licences are currently valid.

<!-- review:begin ca-lic-20261106-imipenem-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both licences are single-ingredient products and both are currently valid." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). The DPD lists 2 DINs for this drug, 2 marketed; the Quick Overview and the table under Canada Market Information show the current figures. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-imipenem-1 -->

## Safety Considerations

- **Drug Interactions:** 15 interactions were identified.
  - **Major:** bupropion, iohexol, iopamidol.
  - **Moderate:** polyethylene glycol (3350 with electrolytes), dicoumarol, warfarin, lindane, aminophylline, dyphylline, oxtriphylline, theophylline, cyclosporine, ethinylestradiol, mycophenolic acid, pemetrexed.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score for diffuse scleroderma is high, but there are no clinical trials or publications, and no plausible mechanism links a bacterial cell wall inhibitor to an autoimmune fibrotic disease. The evidence level is L5.

**To proceed, the following is needed:**
- Preclinical or mechanistic data showing a biological rationale for imipenem in diffuse scleroderma
- Review of the Health Canada package insert for warnings and contraindications
- Any clinical or observational studies directly addressing diffuse scleroderma, which could justify re-evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "are single-ingredient products and both" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

