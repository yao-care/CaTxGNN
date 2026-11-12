---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
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

## Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tamsulosin is an alpha-1 adrenoceptor antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no biological rationale, and it should be treated as a computational artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 10 of 10) |
| Number of DINs | 10 (marketed: 10) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tamsulosin is an alpha-1A/1D adrenoceptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which is why it works in BPH.

The new indication does not follow from this mechanism. Ambras syndrome is a rare genetic disorder caused by a chromosomal rearrangement affecting regulation of the *TRPS1* gene. Alpha-1 blockade has no known role in promoting hair growth. Hypertrichosis is also not a recognised effect of alpha-blockers.

The very high score (1.0000) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other top-ranked predictions show the same pattern. They are dominated by hair and congenital conditions: hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia areata and alopecia. None has clinical or literature support for tamsulosin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For the broader hair-loss area (alopecia, rank 9), two papers were retrieved. Neither shows tamsulosin efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohort / pharmacovigilance | JAMA Dermatology | Suicidality and psychological adverse events with finasteride, a different drug used for alopecia and BPH |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cross-sectional | Cornea | Meibomian gland changes in men with BPH, an ocular observation unrelated to hair loss |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02413612 | TAMSULOSIN CR | Not specified | Not specified |
| 02427117 | TAMSULOSIN CR | Not specified | Not specified |
| 02545179 | AURO-TAMSULOSIN CR | Not specified | Not specified |
| 02368242 | TEVA-TAMSULOSIN CR | Not specified | Not specified |
| 02319217 | SANDOZ TAMSULOSIN | Not specified | Not specified |

Five of the 10 valid authorisations are listed here.

<!-- review:begin ca-lic-20261106-tamsulosin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Five of the 10 valid single-ingredient authorisations are listed here." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-tamsulosin-1 -->

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
- Multiple system atrophy
- Postural orthostatic tachycardia syndrome
- Orthostatic hypotension
- Liver disease
- Gallbladder disease
- Priapism
- Intraoperative floppy iris syndrome

**Drug Interactions:** 100 interactions were identified. The most clinically important is:
- **Major:** Clarithromycin

Moderate-level interactions include bupropion, aprepitant, morphine, cimetidine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, miconazole, clotrimazole, fenfluramine and opium.

Label-based warnings and contraindications were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, and no plausible mechanism links alpha-1 adrenoceptor blockade to hypertrichosis or the other predicted conditions. The other nine top predictions are in the same position.

**To proceed, the following is needed:**
- Mechanism of action data to assess any mechanistic link
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Any preclinical or clinical signal for tamsulosin in hair or congenital disorders. Without it, the prediction should be deprioritised.
- A review of any hair-related signals as possible adverse or off-target effects rather than therapeutic opportunities
- If repurposing is still pursued, a more plausible candidate indication among the lower-ranked predictions, assessed on its own evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "single-ingredient" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

