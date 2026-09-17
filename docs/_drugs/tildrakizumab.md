---
layout: default
title: Tildrakizumab
parent: Model Prediction Only (L5)
nav_order: 775
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
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

Using the evidence-pack data as provided — this is a report-writing task with a fully specified template, no ambiguity requiring a skill workflow.

# Tildrakizumab: From an Undocumented Original Indication to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Tildrakizumab (DrugBank ID DB14004) is an anti-IL-23p19 monoclonal antibody; its originally approved indication and mechanism of action are **not documented** in the current evidence pack (blocking data gap) and the drug is **not marketed in Canada**.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-derived signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Canadian licenses on file, and `original_indications` is empty in the evidence pack |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the information present in the evidence pack's own rationale text, Tildrakizumab is an **anti-IL-23p19 monoclonal antibody** — a class of biologic typically used to suppress IL-23/Th17-driven chronic inflammatory disease.

The proposed link to severe nonproliferative diabetic retinopathy (NPDR) rests on the hypothesis that the IL-23/Th17 axis contributes to the chronic inflammatory component of diabetic microvascular disease. However, the evidence pack explicitly characterizes this link as **theoretical and unproven** — there is no direct molecular or clinical evidence that IL-23 inhibition improves retinal microvascular pathology. The high TxGNN score (0.9963) most likely reflects knowledge-graph co-occurrence or node similarity rather than a validated biological mechanism, and cannot on its own be distinguished from graph noise arising from shared comorbidity nodes (e.g., diabetes-related disease clusters).

Because the drug's original approved indication cannot be confirmed from available data, it is also not possible to assess pharmacological plausibility by comparing old vs. new indication — this comparison is currently "pending" per the evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Tildrakizumab currently holds **no Health Canada Drug Identification Number (DIN)** and has no on-file product license (0 total licenses). It is not marketed in Canada as of this data cutoff (2026-09-16).

---

## Other TxGNN-Predicted Indications (Same Drug)

For context, three additional candidate indications were generated for this drug in the same run — all rated L5 / Hold, with no supporting trials or literature, and mechanistic links assessed by the evidence pack as weak-to-speculative:

| Rank | Disease | TxGNN Score | Mechanistic Plausibility (per evidence pack) |
|------|---------|-------------|-----------------------------------------------|
| 2 | Diabetic Retinopathy | 99.53% | Same speculative IL-23/inflammation hypothesis as rank 1 |
| 3 | Diabetic Cataract | 99.21% | Weak — cataract pathology (protein oxidation/glycation) is not a known IL-23-driven process |
| 4 | Drug-Induced Osteoporosis | 99.20% | Weakest of the four — IL-17A (not IL-23p19) is the pathway more commonly implicated in osteoclast biology |

None of these should be treated as independent signals of confidence; they likely share the same underlying graph-similarity artifact.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: regulatory warnings/contraindications (label data) are recorded as a **Blocking** data gap (DG001) — this must be resolved before any safety screening (S1) can begin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications for this drug are Stage S0 / Evidence Level L5 — TxGNN model output only, with zero corroborating clinical trials or literature. The evidence pack's own mechanistic assessments describe the drug–disease link as theoretical at best and, for two of the four candidates, explicitly weak. Combined with a Blocking data gap on regulatory safety labeling, there is currently no basis to advance this candidate past model prediction.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain regulatory label warnings/contraindications before any S1 safety evaluation
- Resolve DG002 (High): confirm mechanism of action and the drug's actual originally approved indication(s)
- Independent literature or preclinical evidence connecting IL-23p19 inhibition to diabetic retinal microvascular disease
- Confirm regulatory/market status before further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

