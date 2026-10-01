---
layout: default
title: Lecanemab
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
---

# Lecanemab
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

# Lecanemab: From Alzheimer's Disease to Diabetic Cataract

## One-Sentence Summary

Lecanemab is an anti-amyloid-beta antibody marketed in Canada as LEQEMBI. It is generally known as an Alzheimer's disease therapy, although the Canadian licence data supplied do not state an indication.
The TxGNN model predicts it may be effective for **diabetic cataract** with a very high score, but **0 clinical trials** and **0 publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (general knowledge; the supplied licence record has no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Lecanemab is an anti-amyloid-beta protofibril monoclonal antibody. Its efficacy in its original indication is not documented in the supplied data, and only a speculative mechanistic link to cataract exists.

The link is weak. Amyloid-beta has been proposed to deposit in the lens, but there is no evidence that antibody-mediated clearance affects cataract formation. Diabetic cataract is driven mainly by hyperglycemia, polyol pathway activation and oxidative stress, none of which lecanemab targets. A systemically or intravenously given biologic is also unlikely to reach the lens meaningfully.

The high score (0.985) is a model prediction only. It may reflect sparse knowledge-graph edges for this biologic, or score propagation shared across related cataract terms. Nine of the ten top predictions are cataract subtypes (diabetic, type 2 diabetes-associated, craniostenosis, tetanic, immature, mature, nuclear senile, cortical and senile), and all share the same speculative rationale with no supporting evidence. The tenth prediction, **diabetic retinopathy** (score 98.19%), is the most biologically plausible, because retinal amyloid-beta accumulation and neurodegeneration have been discussed in both diabetic retinopathy and Alzheimer's disease. It is still only a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2562383 | LEQEMBI | Not listed | Not listed |

## Safety Considerations

Safety data in the Evidence Pack are limited, and no drug interactions were found in the query. Please refer to the package insert for warnings, contraindications and interactions.

One point from the analysis: lecanemab's known risk of amyloid-related imaging abnormalities (ARIA) offers no basis for exposing patients to it for an ophthalmic indication without supporting evidence. This would matter especially in a vascular retinal disease such as diabetic retinopathy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials, literature or plausible mechanistic support. Established treatments already exist for related conditions, such as anti-VEGF therapy and laser for diabetic retinopathy and surgery for cataract.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Preclinical evidence that amyloid-beta plays a role in lens opacity, or for the more plausible diabetic retinopathy, retinal disease
- An assessment of whether a systemic biologic can reach the eye at relevant concentrations
- An ARIA and vascular safety risk assessment for any ophthalmic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

