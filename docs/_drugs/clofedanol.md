---
layout: default
title: Clofedanol
parent: Model Prediction Only (L5)
nav_order: 210
evidence_level: L5
indication_count: 7
---

# Clofedanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Clofedanol: From Cough to Nasal Cavity Disease

## One-Sentence Summary

Clofedanol is a centrally acting antitussive (cough suppressant).
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this, so the prediction is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough (antitussive use; the license record does not state an approved indication) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Clofedanol is a centrally acting cough suppressant. It is described as having weak antihistaminic and anticholinergic properties. Its efficacy in cough is the basis of its use, and mechanistically these secondary properties may be applicable to nasal symptoms.

"Nasal cavity disease" is a broad, non-specific term, so the prediction is hard to interpret and cannot be verified from the supplied material. The link rests on the weak antihistamine and anticholinergic activity alone, which is speculative.

The other predictions are weaker or more plausible in different ways:
- **Acute laryngopharyngitis** (score 99.99%) is the most biologically plausible candidate. Cough suppression would relieve symptoms of upper airway irritation, but it would not modify the disease. It is best treated as a research question.
- **Allergic urticaria, cold urticaria and papillary conjunctivitis** (scores 99.98% to 99.72%) depend on H1 antagonism, which is weak for clofedanol and unlikely to compete with established antihistamines.
- **Faucial diphtheria and cervical disc degenerative disorder** (scores about 99.3%) have no plausible mechanistic link and are likely graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1966294 | ULONE | — | — |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no verifiable mechanism data (Evidence Level L5). The disease term is also too broad to act on. Among the seven predictions, acute laryngopharyngitis is the only one worth exploring as a symptom-relief research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, to allow safety screening
- Mechanism of action data (for example, from DrugBank)
- The approved indication and dosage form for the ULONE license
- A literature and trial search for clofedanol in upper airway conditions, especially acute laryngopharyngitis
- A route-compatibility assessment for any candidate new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

