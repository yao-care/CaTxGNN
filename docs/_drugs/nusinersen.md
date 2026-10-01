---
layout: default
title: Nusinersen
parent: Model Prediction Only (L5)
nav_order: 664
evidence_level: L5
indication_count: 10
---

# Nusinersen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Nusinersen: From Spinal Muscular Atrophy to Neoplasm of Immature B and T Cells

## One-Sentence Summary

Nusinersen is an antisense oligonucleotide marketed in Canada as SPINRAZA, originally used for spinal muscular atrophy (SMA).
The TxGNN model predicts it may be effective for **neoplasm of immature B and T cells**, but the score is only 50% (non-discriminative), and **0 clinical trials** and **0 publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (the licence record has no indication text, so this comes from the drug's known use) |
| Predicted New Indication | Neoplasm of immature B and T cells |
| TxGNN Prediction Score | 50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Nusinersen is known to modulate splicing of SMN2 exon 7 to increase production of functional SMN protein, which is the basis of its use in SMA.

No plausible mechanistic link to immature B/T-cell neoplasms has been identified. SMA is a motor neuron disease and the predicted indication is a haematological malignancy, and nothing in the data connects SMN2 splice modulation to the biology of these cancers. A score of 0.5 is not informative, and the prediction is best treated as a knowledge-graph artifact until independent evidence appears.

The other nine predicted indications (for example myeloid/lymphoid neoplasms with eosinophilia, cytomegalovirus infection, exanthem, mature T/NK-cell neoplasms) are in the same position. All are at L5 and Hold with the same 0.5 score. Two of them have retrieved literature (JAK2-driven neoplasms and NK-cell biology). That literature is disease background only and does not mention nusinersen.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2465663 | SPINRAZA | — | — |

The record in the Evidence Pack does not include a dosage form, manufacturer, or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link. The drug's known mechanism (SMN2 splice modulation) is unrelated to immature B/T-cell neoplasms, so the evidence stays at L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Any independent preclinical or clinical evidence linking nusinersen or SMN2 splicing to this neoplasm
- Confirmation of the approved indication text, dosage form, and route of administration for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

