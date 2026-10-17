---
layout: default
title: Risdiplam
parent: Model Prediction Only (L5)
nav_order: 814
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Risdiplam: predicted new indication Acne (disease) (evidence level L5). Approved use: Spinal muscular atrophy"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)", "drug-induced osteoporosis", "zinc, elevated plasma", "common wart", "metastatic melanoma", "dermatitis", "non-cutaneous melanoma", "acrodermatitis chronica atrophicans", "epithelioid cell melanoma", "eyelid melanoma"]
---

# Risdiplam
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

# Risdiplam: From Spinal Muscular Atrophy to Acne

## One-Sentence Summary

Risdiplam is an SMN2 splicing modifier that is marketed in Canada under the brand name EVRYSDI. The TxGNN model predicts it may be effective for **acne**, but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (based on drug class knowledge; the Canadian licence records compiled for this report contain no indication text) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, risdiplam is an SMN2 splicing modifier used in spinal muscular atrophy, where it increases production of functional SMN protein.

No mechanistic pathway linking SMN2 splicing modulation to acne is supported by the available data. The score of 0.995 is a computational prediction only and has no clinical or literature backing. Acne is a skin condition, and the other top-ranked predictions for this drug also cluster around skin conditions (dermatitis, warts, several melanoma subtypes). This pattern may reflect a bias in the knowledge graph rather than true biological relevance. Any hypothesis would need independent preclinical validation first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02560747 | EVRYSDI | Not specified | Not specified |
| 02514931 | EVRYSDI | Not specified | Not specified |

## Other Predicted Indications (for Reference)

All of the following predictions are at evidence level L5, with no trials or publications, and a recommendation of Hold.

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Drug-induced osteoporosis | 97.72% |
| 3 | Zinc, elevated plasma | 97.32% |
| 4 | Common wart | 97.21% |
| 5 | Metastatic melanoma | 96.84% |
| 6 | Dermatitis | 96.62% |
| 7 | Non-cutaneous melanoma | 96.18% |
| 8 | Acrodermatitis chronica atrophicans | 96.11% |
| 9 | Epithelioid cell melanoma | 95.93% |
| 10 | Eyelid melanoma | 95.88% |

The melanoma predictions (ranks 5, 7, 9 and 10) are likely correlated rather than independent signals.

## Safety Considerations

**Drug Interactions** (2 moderate-level interactions found):
- Metformin (Moderate)
- Methylnaltrexone (Moderate)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a model score. There are no clinical trials, no publications, and no supported mechanistic link between risdiplam and acne. The package insert warnings and contraindications are also unavailable, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data for risdiplam
- Approved indication text and dosage form for the two Canadian licences
- Preclinical evidence of a biological link between SMN2 splicing modulation and acne
- Route compatibility assessment, since acne would likely require a different route of administration than the current product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

