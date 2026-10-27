---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 883
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Tazarotene: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Psoriasis, parapsoriasis, acne"
monitor_inn: "TAZAROTENE"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
---

# Tazarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Tazarotene: From Psoriasis to Seborrheic Dermatitis
{: .text-alpha }

## One-Sentence Summary

Tazarotene is a topical retinoid originally used to treat psoriasis, parapsoriasis, and acne.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it remains a computational hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne (from the TxGNN knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, tazarotene is a topical retinoid prodrug converted to tazarotenic acid, which selectively binds retinoic acid receptors RAR-beta and RAR-gamma. This helps normalise keratinocyte differentiation and reduces skin-cell overgrowth and inflammation.

Psoriasis and seborrheic dermatitis are both scaling, inflammatory skin conditions with some shared features, such as excess growth of the outer skin layer. This is the main reason the prediction is plausible.

There are important limits, however. Seborrheic dermatitis is also driven by *Malassezia* yeast colonisation and the local immune response, which retinoids do not directly target. Retinoid-related irritation could also make the condition worse, since it often affects sensitive facial areas. The very high TxGNN score is a computational output only and is not backed by clinical evidence here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for seborrheic dermatitis.

*For reference:* for the second-ranked prediction, **seborrheic keratosis** (TxGNN score 99.51%, evidence level L4), two publications were found. Whether tazarotene was actually studied in them could not be confirmed from the information available.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | Systematic review | J Dermatolog Treat | Reviewed the efficacy and safety of topical treatments for seborrheic keratoses (26 reports included); tazarotene-specific results not confirmed |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative study | Int J Dermatol | Compared standard cryosurgery with topical calcipotriene, tazarotene, and imiquimod for seborrheic keratoses; results not available in the data provided |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02517868 | ARAZLO | Not specified | Not specified |
| 02499967 | DUOBRII | Not specified | Not specified |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): photoparoxysmal response, photosensitivity disease, sunburn.
- **Drug Interactions**: 25 potential interactions were identified, all with an unclassified severity level. Examples include:
  - Doxycycline and minocycline
  - Adapalene and tretinoin (other retinoids)
  - Clobetasol and tacrolimus (other topical agents)
  - Omeprazole, citalopram, duloxetine, diclofenac, and others

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for seborrheic dermatitis relies solely on a model score, with no clinical trials or publications (evidence level L5). The mechanism is only partly plausible, and skin irritation is a concern in the affected areas.

**To proceed, the following is needed:**
- Obtain and review the Health Canada package inserts for warnings and contraindications
- Add detailed mechanism of action data
- Search for clinical or preclinical studies of tazarotene in seborrheic dermatitis
- Review the full text of the two seborrheic keratosis publications to see whether tazarotene data exist, as this is a possible alternative direction
- Assess tolerability in sensitive facial skin and the photosensitivity-related signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

