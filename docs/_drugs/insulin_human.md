---
layout: default
title: Insulin Human
parent: Model Prediction Only (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is a glucose-lowering hormone therapy, marketed in Canada under two licences (MYXREDLIN and HUMULIN 30/70).
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but the prediction rests on the knowledge graph alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (standard use of insulin; the licence records supplied contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Insulin human is a replacement hormone whose efficacy in diabetes is well established. Whether that translates to autoimmune oophoritis is not supported by the supplied data.

No mechanistic link between insulin and autoimmune oophoritis was identified. The score of 0.998 (model rank 3692) comes from the knowledge-graph prediction alone. Nothing else supports it: no trials, no publications, and no indication for similarity to the original use. A very high model score is therefore not enough to justify further investment on its own.

The other top-ranked predictions show the same weakness:
- **Pancreatic agenesis** (the only rank-1–10 candidate at stage S1, "Research Question"): insulin is already the standard replacement therapy for the absolute insulin deficiency this condition causes. This is standard care, not repurposing. None of the supplied citations is a trial of insulin in this condition.
- **Localized lipodystrophy and lipoatrophy** (ranks 6, 7, 8, 10): injected insulin is a recognised cause of these injection-site changes. These predictions most likely reflect a causal, adverse relationship, so they are safety signals rather than treatment opportunities.
- **Stiff person syndrome variants, thiamine-responsive dysfunction syndrome and opsismodysplasia**: the links are shared autoimmunity, diabetes co-occurrence, or shared insulin-signalling pathways. None shows that insulin treats the condition.

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
| 2529602 | MYXREDLIN |
| 795879 | HUMULIN 30/70 (INSULIN HUMAN BIOSYNTH INJ) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5, stage S0). There are no trials or publications, and no mechanistic link between insulin and autoimmune oophoritis is supported by the data. Safety screening also cannot proceed because Health Canada package insert information has not been collected.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap; download and parse the product monograph PDFs)
- Mechanism of action data from DrugBank (DB00030), to allow a proper mechanistic-link analysis
- Approved indication text, dosage form and manufacturer for both licences, to confirm the original indication and route compatibility
- Literature and trial searches specific to autoimmune oophoritis and insulin, to test whether any real signal exists
- Consideration of prioritising other candidates for review, since insulin's expected role in pancreatic agenesis is standard care and the lipodystrophy predictions are adverse-effect signals

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

