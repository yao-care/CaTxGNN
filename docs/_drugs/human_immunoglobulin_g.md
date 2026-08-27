---
layout: default
title: Human Immunoglobulin G
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Human Immunoglobulin G
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

# Human Immunoglobulin G: Toward Severe Nonproliferative Diabetic Retinopathy

*Note: This evidence pack does not include an on-file "original indication" for Human Immunoglobulin G (drug.original_indications is empty; taiwan_regulatory.licenses is empty). The title format below therefore reflects only the predicted new indication; the original-use context could not be populated from the data provided.*

## One-Sentence Summary

Human Immunoglobulin G (DB00028) has no original indication or mechanism-of-action data on file in this evidence pack, and it is currently **not marketed** in the Canadian dataset reviewed (0 licenses/DINs).
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, with a prediction score of **99.75%**, but this is supported by **0 clinical trials** and only **1 publication**, which is itself a biomarker/observational study rather than treatment evidence.
Given the evidence level (**L5**) and a blocking data gap on regulatory safety information, the recommended decision at this stage is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved indication or license record on file) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Human Immunoglobulin G in this evidence pack (flagged as a High-severity data gap, DG002). Without MOA data and without a documented original indication, it is not possible to construct a pharmacological rationale linking this drug's established use to diabetic retinopathy.

The only supporting literature identified (PMID 40204274) investigates serum IgG Fc N-glycosylation patterns as a potential *diagnostic biomarker* for distinguishing nonproliferative from proliferative diabetic retinopathy. This is a disease-staging correlation study, not a therapeutic intervention study — it shows that IgG glycosylation *changes* with disease state, not that administering IgG *treats* the disease. As the evidence pack's own mechanistic assessment notes, this is an observational/correlative finding and cannot be used to support therapeutic use of IgG in this indication.

In short, the high TxGNN score (99.75%) appears to be driven by network-level embedding similarity rather than by any confirmed causal or mechanistic relationship. The prediction should be treated as a hypothesis-generating signal only, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40204274](https://pubmed.ncbi.nlm.nih.gov/40204274/) | 2025 | Cross-sectional biomarker study | Molecular & Cellular Proteomics | Analyzed serum disease-specific IgG Fc N-glycosylation in 160 patients (47 non-diabetic retinopathy, 51 nonproliferative DR, 62 proliferative DR) to evaluate its potential as a diagnostic biomarker for distinguishing DR stages; does not evaluate IgG as a treatment. |

---

## Canada Market Information

Human Immunoglobulin G is currently **not marketed** in the dataset reviewed — total_licenses is 0 and no license records are available, so no product/DIN table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) — there are no clinical trials and only a single, non-interventional biomarker study supporting a link between IgG and severe nonproliferative diabetic retinopathy. Combined with the absence of mechanism-of-action data and the lack of any market/regulatory safety file, there is currently insufficient basis to advance this candidate beyond an early hypothesis.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (Blocking data gap, DG001) — required before any Stage 1 safety screening can occur
- Mechanism of action (MOA) data via DrugBank API (High-severity data gap, DG002) — needed to assess mechanistic plausibility
- Interventional (not merely observational/biomarker) studies testing IgG administration in diabetic retinopathy
- Confirmation of Canadian market/regulatory status and any available product information, since no licenses are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

