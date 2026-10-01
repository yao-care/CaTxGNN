---
layout: default
title: Articaine
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 4
---

# Articaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Articaine: From Dental Local Anesthesia to Gout

## One-Sentence Summary

Articaine is an amide local anesthetic sold in Canada in dental products. The original indication is inferred from the product names, because the approved-indication text is not available in the data. The TxGNN model predicts it may be effective for **gout**, but **0 clinical trials** and **0 publications** support this, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dental local anesthesia (inferred from product names; approved-indication text not available) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Articaine belongs to the amide local anesthetic class, which works by blocking voltage-gated sodium channels. It is used to numb tissue during dental procedures.

No credible mechanistic link to gout has been identified. Gout is driven by uric acid crystal deposition and the inflammation that follows. A sodium channel-blocking anesthetic has no known effect on urate metabolism or on gouty inflammation. The high TxGNN score (rank 8,213) is a computational output only, and it should be read as a hypothesis-generating signal rather than supporting evidence.

The other top predictions show the same pattern: exostosis, allergic asthma and intrinsic asthma. All have L5 evidence and a Hold recommendation. For allergic asthma, three publications were retrieved, but they concern hypersensitivity reactions to local anesthetics, not treatment. They match on the keyword "allergy" and do not support efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for gout.

---

## Canada Market Information

Dosage form and approved-indication text are not listed for these licenses. Five of the 12 licenses are shown.

| DIN | Product Name |
|---------|------|
| 02248489 | 4% ASTRACAINE DENTAL WITH EPINEPHRINE 1:200,000 (0.005MG/ML) |
| 02123371 | SEPTANEST N |
| 02339544 | ARTICAINE HYDROCHLORIDE AND EPINEPHRINE BITARTRATE INJECTION |
| 02248488 | 4% ASTRACAINE DENTAL WITH EPINEPHRINE FORTE 1:100,000 (0.01MG/ML) |
| 02381338 | POSICAINE SP |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction has no clinical trials, no literature and no plausible mechanistic link. The TxGNN score is the only support, so the candidate stays at evidence level L5 (model prediction only).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A credible mechanistic hypothesis connecting sodium channel blockade to urate metabolism or gouty inflammation
- Route compatibility assessment: articaine is a dental injectable, and gout would require a different route and dosing context
- Preclinical or literature evidence in gout before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

