---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
---

# Amantadine
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

# Amantadine: From Established Marketed Use to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is a long-marketed drug with three Canadian product licences, but the Evidence Pack does not record its approved indications.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but there are **0 clinical trials** and **0 publications** for this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for amantadine is not available in the Evidence Pack. The only mechanistic information comes from the candidate's rationale: amantadine is a weak NMDA receptor antagonist.

Rasmussen encephalitis involves immune-mediated brain injury and glutamate excitotoxicity. Because glutamate signalling is part of the disease process, blocking NMDA receptors is conceivable in theory. This link is speculative. No trial or publication supports it, and the high TxGNN score (0.995) is a model output, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage forms below are inferred from the product names, because the licence records list no dosage form or approved indication text.

| DIN | Product Name | Dosage Form |
|---------|------|------|
| 2538601 | ODAN-AMANTADINE SYRUP | Syrup |
| 2022826 | PDP-AMANTADINE HYDROCHLORIDE SYRUP | Syrup |
| 1990403 | PDP-AMANTADINE HYDROCHLORIDE CAPSULES | Capsule |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no literature behind it, and the mechanistic link is speculative. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings and contraindications), which is currently blocking safety screening
- Mechanism of action data from DrugBank
- Any clinical or preclinical evidence of amantadine, or NMDA antagonists, in Rasmussen encephalitis
- A judgement on whether the third-ranked candidate, myelitis, is the better lead. It has a small placebo-controlled amantadine trial in post-polio fatigue (PMID 7611638), but that concerns a late sequela of poliomyelitis rather than inflammatory myelitis itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

