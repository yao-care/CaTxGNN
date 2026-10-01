---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 4
---

# Memantine
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

# Memantine: From Alzheimer's Disease to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist marketed in Canada, and the licence records supplied here do not state its approved indication. It is generally used for Alzheimer's-type dementia.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (general knowledge; the supplied licence records list no indication text) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Memantine is generally known as an NMDA receptor antagonist. Its efficacy in its original indication is established, but the supplied data do not show why it would work in pulmonary hypertension.

Pulmonary hypertension is a disease of the pulmonary blood vessels and the right heart. It is quite different from the neurological disorder memantine is used for. Any link through NMDA receptors in the pulmonary vasculature is speculative and is not supported by the supplied data.

The high score (0.995) therefore reflects a pattern in the knowledge graph, not confirmed biology. No trials or literature were retrieved to test it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2324067 | ACT MEMANTINE |
| 2446049 | MEMANTINE |
| 2375532 | SANDOZ MEMANTINE FCT |
| 2443082 | MEMANTINE |
| 2366487 | APO-MEMANTINE |

Dosage form and approved-indication text were not provided for these licences. Five of the 10 licences are shown.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link in the supplied data, so it cannot move past model-level screening. Blocking data gaps also remain: the Health Canada package insert safety information is missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence for memantine in pulmonary hypertension
- Approved indication text and dosage forms for the Canadian licences

**Note on other predictions for this drug:** Rank 2, **migraine disorder** (score 99.52%), has much stronger support: one completed Phase 3 RCT (NCT04698525, memantine vs sodium valproate, n=33), a meta-analysis of RCTs, systematic reviews and a network meta-analysis. Its evidence level is L1 with a "Research Question" recommendation. Because the sample sizes are small and a 2021 commentary calls the evidence limited, it would be worth evaluating as a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

