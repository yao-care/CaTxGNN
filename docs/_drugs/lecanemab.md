---
layout: default
title: Lecanemab
parent: Model Prediction Only (L5)
nav_order: 450
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

Lecanemab is a monoclonal antibody targeting amyloid-beta protofibrils, currently validated only for Alzheimer's disease.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests solely on knowledge-graph pattern similarity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's Disease (only validated indication; formal MOA/indication text not on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data for lecanemab is not on file in this evidence pack. Based on available information, lecanemab is a humanized IgG1 monoclonal antibody that selectively binds amyloid-beta (Aβ) protofibrils in the central nervous system; its only clinically validated use is slowing cognitive decline in early Alzheimer's disease.

Diabetic cataract, by contrast, arises from an entirely different pathology — polyol pathway activation, oxidative stress, and non-enzymatic glycation-driven aggregation of lens crystallin proteins. While some basic-science literature notes amyloid-like protein aggregates in aging/diabetic lenses, this is a distinct anatomical and molecular context from the CNS Aβ protofibrils lecanemab targets. There is no evidence that a systemically administered anti-Aβ antibody reaches or modifies lens protein aggregation.

Given this, the mechanistic link should be treated as speculative and graph-derived rather than biologically established. The same caveat applies to the other nine ranked candidates in this evidence pack (all cataract subtypes plus diabetic retinopathy, scores 98.19–98.48%), which share the same weak or absent mechanistic rationale according to their own repurposing_rationale notes.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Lecanemab currently has no marketing authorization (DIN) in Canada (0 licenses on file); market status is recorded as "Not Marketed."

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN graph-similarity score (L5, S0 stage) with zero clinical trials, zero publications, and no plausible direct mechanistic pathway connecting anti-Aβ immunotherapy to diabetic cataract formation. The drug is also unmarketed in Canada.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph warnings and contraindications (currently blocking — DG001)
- Verified mechanism-of-action documentation from DrugBank (DG002)
- Preclinical or mechanistic studies evaluating Aβ-antibody exposure/effect in lens tissue
- Any registered clinical trials or case reports in diabetic cataract or related ocular indications before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

