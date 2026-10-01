---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 829
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Scopolamine: From Its Approved Use to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is a non-selective muscarinic antagonist marketed in Canada as an injection, but the source record does not list its approved indication.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, with a very high score.
However, there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on general pharmacology, scopolamine blocks muscarinic acetylcholine receptors. It also crosses the blood-brain barrier, so it can cause central effects such as sedation and confusion.

This prediction has **no direct mechanistic link**. Cauda equina syndrome is compression of the lumbosacral nerve roots, and blocking muscarinic receptors does not relieve compression. At most, an antimuscarinic could ease downstream bladder symptoms, and that is a separate indication. The high TxGNN score is a model output only. No trial or publication backs it.

The other top predictions fall into two groups:

- **Neurogenic bladder (rank 2, score 99.98%):** this is the only one with class-level plausibility, because antimuscarinics reduce detrusor overactivity by blocking M3 receptors. Scopolamine has no supporting clinical data here, and its central side effects make it a poor fit compared with bladder-selective agents. The disease term is also marked obsolete in the ontology, so the mapping should be reviewed and possibly redirected to a current neurogenic detrusor overactivity term.
- **Conjunctivitis types (ranks 3–6: papillary, atopic, rosacea-related and vernal):** there is no clear mechanistic link. These conditions are driven by mechanical irritation, allergic or Th2 pathways, or ocular surface inflammation. Anticholinergic effects such as mydriasis and dry eye could make symptoms worse.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2242811 | SCOPOLAMINE HYDROBROMIDE INJECTION |
| 2242810 | SCOPOLAMINE HYDROBROMIDE INJECTION |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it (L5) and no plausible mechanistic link to cauda equina syndrome. Scopolamine's central nervous system effects add a further concern. The more plausible neurogenic bladder prediction uses an obsolete disease term and has no supporting data either.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm the approved indication, warnings and contraindications
- Mechanism of action data from DrugBank
- A review of the obsolete neurogenic bladder term, and a re-run of the prediction against the current neurogenic detrusor overactivity term
- A targeted literature and trial search for scopolamine in neurogenic bladder or neurogenic detrusor overactivity
- A route-of-administration compatibility assessment for the injection formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

