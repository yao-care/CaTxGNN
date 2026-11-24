---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 374
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Herpes zoster"
monitor_inn: "Famciclovir"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
---

# Famciclovir
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

## Famciclovir: From Herpes Zoster to Post-infectious Neuralgia
{: .text-alpha }

## One-Sentence Summary

Famciclovir is an oral antiviral originally used to treat herpes zoster (shingles).
The TxGNN model predicts it may be useful for **post-infectious neuralgia**, which in this context is nerve pain after a viral infection such as postherpetic neuralgia.
Support is thin: **1 clinical trial** is linked, and it tests a different drug (oxycodone), with **no publications** found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for famciclovir: "Famciclovir is an orally administered prodrug of the anti-alpha herpes viral agent penciclovir." ([DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761), label version 2026-11-13; accessed 2026-11-19.) Based on known pharmacology, famciclovir is a prodrug of penciclovir. Penciclovir's active triphosphate form inhibits the DNA polymerase of varicella-zoster virus (VZV), which limits viral replication.

The link between the two conditions is that postherpetic neuralgia is the most common complication of herpes zoster. Treating the acute zoster episode early with an antiviral may reduce nerve damage and, in turn, the risk or duration of later neuralgia. The reasoning is plausible but indirect. The only linked trial studies oxycodone, not famciclovir, so there is no direct evidence that famciclovir prevents or treats post-infectious neuralgia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the studied drug, so this offers contextual support only. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Six valid single-ingredient authorizations are on the Canadian market. Dosage forms, manufacturers and approved-indication text are not available in the data compiled for this report.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02177102 | FAMVIR | FAMCICLOVIR | Marketed |
| 02229110 | FAMVIR | FAMCICLOVIR | Marketed |
| 02229129 | FAMVIR | FAMCICLOVIR | Marketed |
| 02292025 | APO-FAMCICLOVIR | FAMCICLOVIR | Marketed |
| 02292041 | APO-FAMCICLOVIR | FAMCICLOVIR | Marketed |
| 02292068 | APO-FAMCICLOVIR | FAMCICLOVIR | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-famciclovir-1 -->

> **Review correction (2026-11-24)**: Originally stated: "*(5 of 6 authorizations shown; the sixth is another APO-FAMCICLOVIR product, DIN 02292025.)*" Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-famciclovir-1 -->

---

## Safety Considerations

- **Disease-level contraindications (from a knowledge graph, not label text):** kidney disease and pyoureter. This is relevant because famciclovir is cleared by the kidneys. Confirm against the Canadian product monograph before any use.
- **Drug Interactions:** 84 potential interactions were identified, none with a severity level assigned. Examples include calcitriol, doxycycline, metformin, glimepiride, morphine, omeprazole, pantoprazole, prednisone, simvastatin and vancomycin. Clinical significance needs verification.

Please refer to the package insert for label warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, and the mechanism is plausible because famciclovir treats the infection that precedes postherpetic neuralgia. However, no trial or publication tests famciclovir for this outcome, so the evidence is at the L4 level. The prediction should stay a research question for now.

**To proceed, the following is needed:**
- A trial or systematic review of famciclovir or other antivirals for preventing or treating postherpetic neuralgia
- Mechanism-of-action data from a curated source
- Label warnings and contraindications from the Canadian product monograph
- Dose guidance for patients with renal impairment
- Approved-indication text for the Canadian authorizations

**Related finding:** Among the other predictions for famciclovir, **chickenpox** has the strongest support (L1). It has two completed Phase 3 studies, one on pediatric pharmacokinetics and safety (NCT00098046) and one on zoster efficacy (NCT01327144). Neither is a chickenpox efficacy trial, so this is worth a separate evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761) |
| 2026-11-24 | Removed: "*(5 of 6 authorizations shown; the sixth is another APO-FAMCICLOVIR product, DIN 02292025.)*" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

