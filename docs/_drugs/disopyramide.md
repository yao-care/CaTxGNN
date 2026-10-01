---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a class Ia antiarrhythmic drug, originally used to treat cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone and is likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arrhythmia (the approved indication text is not recorded in the Canadian license data) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Disopyramide is known to be a class Ia sodium channel blocker with anticholinergic activity, and its efficacy in arrhythmia is established.

We could not identify a credible mechanistic link to Tourette syndrome. Tourette syndrome is a neurodevelopmental tic disorder, usually treated by modulating dopamine and related neurotransmitter pathways. That is not what disopyramide does.

The high score (0.9986) is most likely explained by shared neuro-receptor or ion-channel neighbors in the knowledge graph. No independent evidence supports it.

**Other model predictions.** The other top-ranked predictions show the same pattern, mostly with scores above 99%:
- Most have no trials or literature: ADHD and its inattentive subtype, trichotillomania, faciodigitogenital syndrome, specific developmental disorder, chondromyxoid fibroma and trigeminal nerve neoplasm. The two ADHD entries are likely one correlated signal, not independent evidence.
- **Idiopathic neonatal atrial flutter** is biologically coherent for a class Ia antiarrhythmic, but has no evidence, and disopyramide's anticholinergic and negative inotropic effects are a safety concern in neonates.
- **Multifocal atrial tachycardia** is coherent as well. Its only publication (PMID 7418495, 1980) concerns lorcainide, a different drug, in ventricular arrhythmias, so it is indirect evidence at best. It could be worth a literature review as a research question, but gives no basis for a recommendation.

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
| 2224801 | RYTHMODAN |

Dosage form, manufacturer and approved indication text are not recorded for this license.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note from the candidate review: the anticholinergic and cardiac effects of disopyramide would be a particular concern in a pediatric or neurodevelopmental population such as Tourette syndrome.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-derived only (L5), with no trials or publications and no plausible mechanistic link between a sodium channel blocker and tic disorders. The candidate does not currently justify further investment.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings and contraindications), required before any safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- A targeted literature search for disopyramide or class Ia antiarrhythmics in tic disorders
- The approved indication text for the Canadian license, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

