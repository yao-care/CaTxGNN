---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 669
evidence_level: L5
indication_count: 6
---

# Rasagiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Rasagiline: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

> Rasagiline is a monoamine oxidase-B (MAO-B) inhibitor whose established clinical role is dopaminergic pathway modulation, as reflected in its own repurposing rationale text.
> The TxGNN model predicts a possible link to **PLA2G6-Associated Neurodegeneration**, a rare genetic disorder with a parkinsonism subtype (PARK14),
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug is pharmacologically characterized as an MAO-B inhibitor per rationale text; formal indication/MOA record is a flagged data gap — DG002) |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.71% (rank 6131) |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale attached to this candidate, rasagiline acts as an MAO-B inhibitor that modulates dopaminergic pathways — this is the pharmacological basis the TxGNN model appears to be drawing on.

PLA2G6-Associated Neurodegeneration is a rare inherited disorder in which some subtypes (including the PARK14 form) present with parkinsonism-like motor symptoms. On the surface, this creates a plausible link to a dopamine-pathway-active drug like rasagiline. However, the underlying disease biology — phospholipid metabolism dysfunction and iron accumulation in neural tissue — is mechanistically distinct from simple dopaminergic deficiency, and does not directly correspond to rasagiline's MAO-B inhibition mechanism. The connection should be read as an indirect, symptom-level inference rather than a validated disease-modifying rationale.

No clinical trials or literature currently exist to test this hypothesis in humans, and the disease itself is ultra-rare, which will constrain future study feasibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Rasagiline is currently **not marketed** in Canada — the evidence pack records 0 active licenses/DINs, so no product-level table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/label warnings and contraindications for this drug are currently an unresolved, Blocking-severity data gap (DG001) — this must be resolved before any formal safety assessment (S1 stage) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with zero supporting trials or literature, the target disease is ultra-rare with only an indirect mechanistic link, and a Blocking-severity safety data gap (missing label warnings/contraindications) prevents any safety evaluation from starting.

**To proceed, the following is needed:**
- TFDA/regulatory label data — warnings, contraindications (DG001, Blocking)
- Confirmed mechanism of action and original approved indication(s) for rasagiline (DG002, High)
- Preclinical or mechanistic studies directly linking MAO-B inhibition to the parkinsonism subtype of PLA2G6-Associated Neurodegeneration
- Assessment of feasibility for clinical study given the rarity of the target disease population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

