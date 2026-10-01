---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 876
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tazarotene: From Marketed Topical Retinoid to Seborrheic Dermatitis

## One-Sentence Summary

Tazarotene is a retinoid marketed in Canada in two products (ARAZLO and DUOBRII). The package does not list an approved indication for it.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**, but only **1 registered clinical trial** was retrieved, and it was judged not relevant. **No publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. The following comes from the mechanistic analysis in the evidence pack. Tazarotene is a prodrug whose active metabolite, tazarotenic acid, selectively activates retinoic acid receptors RAR-beta and RAR-gamma. This changes how skin cells (keratinocytes) mature and multiply, and it has anti-inflammatory effects.

Seborrheic dermatitis is driven mainly by *Malassezia* yeast and skin inflammation. Retinoid effects on keratinocyte turnover and inflammation make a link plausible, but no retinoid-specific data were provided to confirm it. The very high TxGNN score (99.79%, rank 4704) is a computational prediction, not clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | N/A | Unknown | 40 | Platelet-rich plasma plus topical retinoids versus topical retinoids alone in **acne vulgaris**. |

This trial does not study seborrheic dermatitis. It was graded C (low relevance) and appears to have been matched only on the keyword "topical retinoid". It cannot support this indication.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2517868 | ARAZLO |
| 2499967 | DUOBRII |

Dosage form and approved indication text were not provided for either product.

---

## Safety Considerations

Please refer to the package insert for safety information.

Drug interaction queries returned no records. Tazarotene is a known local irritant, which matters for sensitive skin areas.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible mechanistically, but evidence is at the lowest level (L5). The one retrieved trial is unrelated (acne), and there are no supporting publications. The pack gives no basis for moving beyond the screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indications and dosage forms for ARAZLO and DUOBRII
- Mechanism-of-action data from DrugBank
- Retinoid-specific clinical or preclinical studies in seborrheic dermatitis
- Assessment of route compatibility (currently pending)

**Other predictions for this drug:**
- **Seborrheic keratosis** (score 99.51%) has somewhat stronger support, at L4 with a "Research Question" recommendation. It has a 2023 systematic review of topical treatments and a 2004 comparative study that included topical tazarotene. Clinical effect is still unconfirmed.
- **Vulvar inverted follicular keratosis** (score 99.38%) has no trials or publications (L5, Hold). The vulvar site is sensitive, and tazarotene's local irritation is a concern there.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

