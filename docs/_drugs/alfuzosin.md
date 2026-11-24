---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Alfuzosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Alfuzosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Alfuzosin
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

## Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic blocker originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for alfuzosin: "Alfuzosin is a selective antagonist of post-synaptic alpha 1 -adrenoreceptors, which are located in the prostate, bladder base, bladder neck, prostatic capsule, and prostatic urethra." ([DailyMed: Uroxatral (alfuzosin hcl) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9fc7f119-f36b-44cf-945d-940160f3afe3), label version 2024-12-05; accessed 2026-11-19.) Based on known information, alfuzosin is a uroselective alpha-1 adrenergic antagonist. Its efficacy in BPH is established, but no mechanistic route to the predicted new indication is known.

Ambras syndrome is a rare genetic disorder caused by chromosomal rearrangements that affect regulation of the TRPS1 gene. No plausible pathway links alpha-1 blockade to this condition. The very high TxGNN score (1.0000) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as a cluster of hypertrichosis and hair-disorder diseases, not biological evidence.

The other top predictions (hypertrichosis, dental/periodontal malformation syndromes, Dandy-Walker–type syndromes, hair shaft abnormalities, trichomegaly, allergic urticaria, persistent fetal circulation syndrome, hypotrichosis simplex of the scalp, and congenital hypotrichosis milia) also have no supporting trials or literature. Persistent fetal circulation syndrome has only a loose vasodilation rationale, and it carries a serious hypotension risk in neonates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02245565 | XATRAL | ALFUZOSIN HYDROCHLORIDE | Marketed |
| 02304678 | SANDOZ ALFUZOSIN | ALFUZOSIN HYDROCHLORIDE | Marketed |
| 02315866 | APO-ALFUZOSIN | ALFUZOSIN HYDROCHLORIDE | Marketed |
| 02443201 | AURO-ALFUZOSIN | ALFUZOSIN HYDROCHLORIDE | Marketed |
| 02447576 | ALFUZOSIN | ALFUZOSIN HYDROCHLORIDE | Marketed |
| 02519844 | ALFUZOSIN | ALFUZOSIN HYDROCHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-alfuzosin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A sixth valid authorization (DIN 02315866, APO-ALFUZOSIN) is also marketed." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-alfuzosin-1 -->

All six are single-ingredient products.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, gallbladder disease, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. Examples:
  - **Major**: cisapride, clarithromycin, dolasetron
  - **Moderate**: famotidine, aprepitant, bupropion, levofloxacin, granisetron, dronabinol, the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), and several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose)
  - **Minor**: cimetidine

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links alpha-1 blockade to Ambras-type hypertrichosis, which is a genetic disorder. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic analysis
- Package insert warnings and contraindications from Health Canada, to complete safety screening
- Any preclinical or clinical evidence linking alpha-1 blockade to hair growth or TRPS1-related biology
- A review of the other ranked predictions for any with a more credible pharmacological rationale

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Uroxatral (alfuzosin hcl) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9fc7f119-f36b-44cf-945d-940160f3afe3) |
| 2026-11-24 | Removed: "A sixth valid authorization (DIN 02315866, APO-ALFUZOSIN) is also marketed." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

