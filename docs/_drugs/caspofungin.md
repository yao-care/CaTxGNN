---
layout: default
title: Caspofungin
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Fungal Infections to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin antifungal used for fungal infections. The TxGNN model predicts it may be effective for **gastrin secretion abnormality**, but **no clinical trials and no publications** currently support this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (antifungal class; the Canadian license records provide no indication text) |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for caspofungin is not available in the source record. Based on known pharmacology, caspofungin inhibits fungal beta-(1,3)-D-glucan synthase, an enzyme needed to build the fungal cell wall. Mammalian cells do not have this target.

Gastrin secretion abnormality is an endocrine/gastrointestinal regulatory problem, not an infection. There is no known pathway linking glucan synthase inhibition to gastrin regulation. The high TxGNN score (0.994) reflects graph-based proximity only, and nothing in the trial or literature searches supports it.

On the evidence available, this should be treated as a model artifact rather than a credible repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2460947 | Caspofungin for Injection |
| 2460955 | Caspofungin for Injection |
| 2244265 | Cancidas |
| 2486997 | Caspofungin for Injection |
| 2244266 | Cancidas |

The records list 6 licenses in total, of which 5 are shown above. Dosage form and approved indication text are not available in the records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism, so it is Level L5 evidence. Other predicted indications for caspofungin (neonatal candidiasis, Pneumocystis pneumonia in HIV) have more evidence, but they mostly fall within existing antifungal use rather than true repurposing.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking fungal glucan synthase inhibition to gastrin regulation, or evidence from preclinical work
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Prioritization review of the better-supported predictions (neonatal candidiasis, fungal opportunistic infections in HIV)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

