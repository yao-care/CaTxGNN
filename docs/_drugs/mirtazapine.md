---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 3
---

# Mirtazapine
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a marketed antidepressant with 20 licences in Canada. The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**, but there are currently **0 clinical trials** and **0 publications** supporting this. The prediction rests on model output alone, so the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (general drug knowledge; approved indication text is not provided in the Canadian licence records) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. From the pharmacology in the evidence pack, mirtazapine is an antagonist at alpha-2 adrenergic, 5-HT2, 5-HT3 and H1 receptors, and this profile underlies its use as an antidepressant.

The prediction is difficult to justify biologically. Ohdo syndrome and its variants are rare neurodevelopmental disorders, typically linked to variants in KAT6B, a histone acetyltransferase gene. Their features are structural and developmental. Mirtazapine's receptor pharmacology does not address this chromatin-regulation defect, so no plausible pathway connects the two. The high TxGNN score most likely reflects sparse graph connectivity for a rare-disease node rather than a real biological rationale.

Two other predictions in the pack have the same limitations:
- **Blepharophimosis - intellectual disability syndrome, Ohdo type** (score 99.11%) is the same clinical entity as the top prediction. It is not independent evidence. Any symptomatic use, for example for mood or sleep, would be a separate question from treating the underlying disease.
- **Benign paroxysmal torticollis of infancy** (score 99.11%) has only a speculative, indirect link. The condition is considered a migraine equivalent, and some serotonergic or antihistaminic antidepressants are used in migraine prophylaxis. That is a hypothesis, not evidence for mirtazapine. The condition is self-limiting, and mirtazapine is not established for use in infants, so the safety bar is high and the benefit is unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorisations are shown. Dosage form and approved indication text are not available in the source records.

| DIN | Product Name |
|---------|------|
| 2411709 | AURO-MIRTAZAPINE |
| 2286629 | APO-MIRTAZAPINE |
| 2411695 | AURO-MIRTAZAPINE |
| 2256126 | MYLAN-MIRTAZAPINE |
| 2299828 | AURO-MIRTAZAPINE OD |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials or literature. No mechanistic link exists between mirtazapine's receptor pharmacology and the developmental pathology of Ohdo syndrome. The top two predictions describe the same disease, so they do not corroborate each other.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism-of-action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- Any preclinical or clinical evidence linking mirtazapine to KAT6B-related disorders
- A review of whether the two Ohdo-related predictions should be merged into one entity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

