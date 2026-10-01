---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine is a potassium channel blocker marketed in Canada (as FIRDAPSE and RUZURGI) for Lambert-Eaton myasthenic syndrome (LEMS).
The TxGNN model predicts it may be effective for **glaucoma** with a very high score, but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome (LEMS); the licence records provided contain no indication text |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amifampridine blocks voltage-gated potassium channels. This prolongs depolarization of the presynaptic nerve terminal and increases acetylcholine release at the neuromuscular junction, which is how it relieves weakness in LEMS.

For glaucoma, no credible mechanistic link could be identified. Glaucoma involves raised intraocular pressure and optic neuropathy, and enhanced neuromuscular transmission has no established relevance to either. The high TxGNN score is a graph-based prediction only and should not be read as biological or clinical support.

Among the other top-ranked predictions, the only one with any supporting literature is **paraneoplastic cerebellar degeneration**. It is biologically adjacent to LEMS, since both are associated with small cell lung cancer and anti-P/Q-type calcium channel antibodies. The two retrieved papers concern LEMS itself, not this condition, so they offer only indirect support.

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
| 2502984 | FIRDAPSE |
| 2503034 | RUZURGI |

---

## Safety Considerations

- **Seizure risk**: Amifampridine carries a dose-dependent seizure risk. This matters for any candidate population that is seizure-prone.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction is supported only by the model score, with no trials, no literature and no plausible mechanism. Evidence level is L5, and the candidate has not passed the initial screening stage.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking potassium channel blockade to intraocular pressure or optic nerve protection
- Preclinical or clinical studies of amifampridine or related aminopyridines in glaucoma
- Health Canada package insert warnings and contraindications, needed for safety screening
- Confirmation of the approved indication text and dosage forms for both DINs
- Consideration of paraneoplastic cerebellar degeneration as a better-grounded research question, supported by PCD-specific data such as case series
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

