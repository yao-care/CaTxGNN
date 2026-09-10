---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Iodixanol: From Diagnostic Contrast Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is a non-ionic iodinated contrast medium used for diagnostic imaging (CT/angiography), not a therapeutic drug for any approved indication in Canada. The TxGNN model predicts a top association with **Osteoarthritis Susceptibility**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None (diagnostic contrast agent; not marketed for any therapeutic indication in Canada) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Iodixanol as a therapeutic candidate. Based on known information, Iodixanol is a non-ionic, iso-osmolar iodinated contrast medium used purely for diagnostic imaging — it has no established pharmacodynamic mechanism aimed at disease treatment, and no marketing authorization of any kind exists for it in Canada.

The predicted link to osteoarthritis susceptibility has no supporting mechanistic rationale: iodixanol does not act on cartilage biology, inflammatory pathways, or joint tissue metabolism in any therapeutic sense. Reviewing the closely related prediction "osteoarthritis" (rank 2, same evidence pack) confirms this pattern — the 7 associated publications all use iodixanol purely as an imaging/diffusion-tracer tool to study cartilage structure (e.g., photon-counting CT, finite-element solute transport modeling), not as a treatment. This strongly suggests the TxGNN association arises from knowledge-graph co-occurrence between "contrast agent" and "joint/cartilage" nodes rather than a genuine drug-repurposing signal.

Across all 10 top-ranked predictions in this evidence pack (osteoarthritis, rheumatoid arthritis, hemoglobinopathy, and several rare skeletal dysplasias), the same issue recurs: either zero evidence exists, or the available literature describes iodixanol's use/behavior as a diagnostic or physiological-effect study subject, not as a candidate therapy. None of the 10 predictions reach a mechanistic plausibility threshold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Iodixanol currently holds no Drug Identification Numbers (DINs) in Canada (market status: Not Marketed). No authorization records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Manufacturer safety labeling (warnings, contraindications) has not yet been retrieved for this candidate — this is flagged as a **Blocking** data gap (DG001) and must be resolved before any safety-stage (S1) evaluation can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (osteoarthritis susceptibility) has no clinical trial or literature support — it is a model-score-only (L5) prediction. Iodixanol is a diagnostic contrast agent with no therapeutic MOA, no Canadian market presence, and no plausible mechanistic pathway to osteoarthritis or any of the other 9 predicted indications in this evidence pack, all of which were similarly assessed as Hold.

**To proceed, the following is needed:**
- Product monograph / regulatory safety data (warnings, contraindications) — currently a Blocking gap
- Verified mechanism of action data from DrugBank or primary literature
- Independent pharmacological or preclinical rationale connecting iodixanol to osteoarthritis pathophysiology, beyond its use as an imaging/diffusion-tracer agent
- Re-evaluation if future clinical trial or literature evidence emerges specifically testing iodixanol as a therapeutic (not diagnostic) intervention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

