---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Pegfilgrastim: From Chemotherapy-Induced Neutropenia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a pegylated G-CSF (granulocyte colony-stimulating factor) analogue, established in clinical use to reduce the risk of infection from chemotherapy-induced neutropenia in cancer patients. The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the signal comes entirely from knowledge-graph embedding similarity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack; publicly known use is reduction of febrile-neutropenia/infection risk in non-myeloid malignancy patients receiving myelosuppressive chemotherapy |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this pack. Based on established pharmacology, pegfilgrastim stimulates proliferation and differentiation of bone-marrow granulocyte precursors and mobilizes neutrophils and endothelial progenitor cells (EPCs) into peripheral blood.

The proposed link to diabetic retinopathy rests on the hypothesis that EPC mobilization could influence the balance between retinal vascular repair and pathological neovascularization. This is a mechanistic hypothesis only — it is not supported by any preclinical, observational, or clinical evidence in this pack. Notably, the directionality is uncertain: G-CSF-driven EPC/neutrophil mobilization could theoretically *worsen* pathological neovascularization in proliferative diabetic eye disease rather than help it, so the therapeutic direction cannot be considered established even in theory.

A closely related second candidate, **diabetic retinopathy** (general, score 99.73%), was also predicted, which is consistent with this being a broad knowledge-graph similarity signal around diabetic vascular/retinal disease rather than a specific, mechanistically validated pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting this indication, the mechanistic link is speculative with uncertain directionality (possible risk of worsening retinal neovascularization), and the drug is not currently marketed in Canada with no available DDI or label safety data — the evidence base is insufficient to advance past model prediction (S0/L5).

**To proceed, the following is needed:**
- Confirmed original indication and MOA documentation (currently data gaps DG001/DG002)
- TFDA/Health Canada product label — key warnings and contraindications
- Preclinical or mechanistic studies specifically examining G-CSF/EPC mobilization effects on diabetic retinal neovascularization (both efficacy and harm signals)
- Any observational or case-level data on G-CSF exposure in diabetic retinopathy patients
- Drug interaction data before any safety (S1) evaluation can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

