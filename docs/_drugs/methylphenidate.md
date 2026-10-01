---
layout: default
title: Methylphenidate
parent: Model Prediction Only (L5)
nav_order: 600
evidence_level: L5
indication_count: 4
---

# Methylphenidate
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

# Methylphenidate: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Methylphenidate is a central nervous system stimulant that is widely used as a first-line treatment for ADHD (the Health Canada license text supplied contains no indication wording). The TxGNN model predicts it may be effective for **faciodigitogenital syndrome**, a rare developmental disorder. This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (from the literature; license text not provided) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Methylphenidate is known to block the dopamine and norepinephrine transporters, which increases catecholamine signaling in prefrontal and striatal circuits. Its efficacy in ADHD is well established.

No biological link connects this mechanism to faciodigitogenital syndrome. The disorder is a rare developmental condition, and the supplied data contain no rationale tying catecholamine reuptake inhibition to its pathophysiology. The very high score (rank 109 in the model output) is a graph-based prediction only. It should not be read as supporting evidence.

Among the other predictions for this drug, only "specific developmental disorder" has any trial evidence. It is described in the Conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Five of the 20 authorizations are shown. Dosage form and approved indication text were not provided.

| DIN | Product Name |
|---------|------|
| 02247733 | CONCERTA |
| 02277131 | BIPHENTIN |
| 02553066 | JORNAY PM |
| 02537001 | PMS-METHYLPHENIDATE CR |
| 02441950 | ACT METHYLPHENIDATE ER |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link. Evidence is at L5 (model prediction only), and the high score is likely a graph artifact.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and any biological rationale connecting it to this disorder
- Health Canada package insert warnings and contraindications, currently missing and blocking safety screening
- Any clinical or preclinical study in this specific condition
- Consideration of other candidates. "Specific developmental disorder" (rank 3) has one completed, small Phase 2 placebo-controlled crossover trial of methylphenidate in childhood apraxia of speech ([NCT05185583](https://clinicaltrials.gov/study/NCT05185583), n=18, no results supplied). That signal is the more promising research question, but it would need a defined subtype and results before any advancement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

