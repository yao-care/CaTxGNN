---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 868
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension, congestive heart failure…"
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
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

# Spironolactone: From Hypertension and Heart Failure to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a long-established medicine used for hypertension, congestive heart failure and primary aldosteronism (conditions of excess aldosterone).
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but the data compiled for this report show **0 clinical trials** and **0 publications** supporting this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure, hyperaldosteronism / primary aldosteronism (from the knowledge graph; Canadian label indication text is not available) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

A second prediction, congenital hypotrichosis milia (score 99.04%), is also at L5 with no supporting studies and a Hold recommendation.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Spironolactone is generally known as a mineralocorticoid receptor antagonist with anti-androgen activity. Its efficacy in hypertension, heart failure and aldosterone-excess states is established.

That anti-androgen action gives a plausible but indirect link to hair loss. Spironolactone is used off-label for androgenetic alopecia and female pattern hair loss, where it reduces androgen signalling at the hair follicle. This is probably why the model links the drug to hair-related conditions.

The link is weak for this specific disease. Hypotrichosis simplex of the scalp is a rare hereditary disorder, mainly caused by variants in *CDSN*, *APCDD1* or *RPL21*. These are structural and Wnt-pathway defects, not androgen-driven follicle miniaturisation, so anti-androgen action is not expected to address the underlying cause. The high score of 0.993 is a computational prediction only.

For the second prediction, congenital hypotrichosis milia, there is no direct mechanistic rationale. The score likely reflects network proximity to other hypotrichosis phenotypes rather than a biological mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ten single-ingredient authorisations are valid, none cancelled. Dosage form and approved indication text are not available in the compiled data. The table lists five of them.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02518821 | JAMP SPIRONOLACTONE | Not available | Not available |
| 00613223 | TEVA-SPIRONOLACTONE | Not available | Not available |
| 02488159 | MINT-SPIRONOLACTONE | Not available | Not available |
| 00285455 | ALDACTONE 100 MG | Not available | Not available |
| 00028606 | ALDACTONE 25 MG | Not available | Not available |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, hypercalcemia, hyperparathyroidism, nephrocalcinosis, phosphorus metabolism disease, gout, hyperuricemia, hepatic coma and hepatic encephalopathy, pancreatitis, systemic lupus erythematosus (including paediatric), pyoureter, osteitis fibrosa, and neonatal jaundice.
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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

