---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 868
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). In Canada: 10 DINs (8 marketed)"
---

# Spironolactone
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

## Spironolactone: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone is a long-established medicine used for hypertension, congestive heart failure and primary aldosteronism (conditions of excess aldosterone).
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but the data compiled for this report show **0 clinical trials** and **0 publications** supporting this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 10; cancelled: 2) |
| Number of DINs | 10 (marketed: 8) |
| Recommended Decision | Hold |

A second prediction, congenital hypotrichosis milia (score 0.9904), is also at L5 with no supporting studies and a Hold recommendation.

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for spironolactone: "Spironolactone and its active metabolites are specific pharmacologic antagonists of aldosterone, acting primarily through competitive binding of receptors at the aldosterone-dependent sodium-potassium exchange site in the distal convoluted renal tubule. Spironolactone causes increased amounts of sodium and water to be excreted, while potassium is retained." ([DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc), label version 2025-11-28; accessed 2026-11-19.) Spironolactone is generally known as a mineralocorticoid receptor antagonist with anti-androgen activity. Its efficacy in hypertension, heart failure and aldosterone-excess states is established.

That anti-androgen action gives a plausible but indirect link to hair loss. Spironolactone is used off-label for androgenetic alopecia and female pattern hair loss, where it reduces androgen signalling at the hair follicle. This is probably why the model links the drug to hair-related conditions.

The link is weak for this specific disease. Hypotrichosis simplex of the scalp is a rare hereditary disorder, mainly caused by variants in *CDSN*, *APCDD1* or *RPL21*. These are structural and Wnt-pathway defects, not androgen-driven follicle miniaturisation, so anti-androgen action is not expected to address the underlying cause. The high score of 0.9926 is a computational prediction only.

For the second prediction, congenital hypotrichosis milia, there is no direct mechanistic rationale. The score likely reflects network proximity to other hypotrichosis phenotypes rather than a biological mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved indication text are not available in the compiled data.

<!-- review:begin ca-lic-20261105-spironolactone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Ten single-ingredient authorisations are valid, none cancelled. Dosage form and approved indication text are not available in the compiled data." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). The DPD lists 10 DINs for this drug, 8 marketed; the Quick Overview and the table under Canada Market Information show the current figures. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-spironolactone-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00613215 | TEVA-SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 00613223 | TEVA-SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 00613231 | TEVA-SPIRONOLACTONE/HCTZ | HYDROCHLOROTHIAZIDE; SPIRONOLACTONE | Marketed |
| 00657182 | TEVA-SPIRONOLACTONE/HCTZ | HYDROCHLOROTHIAZIDE; SPIRONOLACTONE | Marketed |
| 02488140 | MINT-SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 02488159 | MINT-SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 02518821 | JAMP SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 02518848 | JAMP SPIRONOLACTONE | SPIRONOLACTONE | Marketed |
| 00028606 | ALDACTONE 25 MG | SPIRONOLACTONE | Cancelled post market |
| 00285455 | ALDACTONE 100 MG | SPIRONOLACTONE | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence):** kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, hypercalcemia, hyperparathyroidism, nephrocalcinosis, phosphorus metabolism disease, gout, hyperuricemia, hepatic coma and hepatic encephalopathy, pancreatitis, systemic lupus erythematosus (including pediatric), pyoureter, osteitis fibrosa, and neonatal jaundice.
- **Drug Interactions:** The interaction screen returned 100 entries. The first 20 reviewed include:
  - **Major:** loperamide.
  - **Moderate:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, metformin, bupropion, morphine, bisacodyl, castor oil, dronabinol, exenatide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin.
  - **Minor:** doxycycline, acetylsalicylic acid, fidaxomicin.

Please refer to the package insert for the official warnings and contraindications, because label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature. The disease is genetically driven (structural and Wnt-pathway defects), so anti-androgen action is unlikely to address its cause. Label-based safety data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that mineralocorticoid or androgen receptor antagonism affects the *CDSN*, *APCDD1* or *RPL21* pathways
- Any case reports or early-phase studies in hereditary hypotrichosis
- Route compatibility assessment (oral spironolactone versus a possible topical approach for scalp conditions)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Ten single-ingredient authorisations are valid, none cancelled" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

