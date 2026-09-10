---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine (DrugBank DB00047) is a long-acting basal insulin analog whose established use is glycemic control in Type 1 and Type 2 diabetes mellitus. The TxGNN model's top-ranked prediction is **autoimmune oophoritis** (score 99.88%), but this evidence pack contains **zero clinical trials and zero publications** supporting that link — the prediction currently rests on the knowledge-graph score alone.

*Note: The evidence pack itself does not contain a sourced "original indication" text (regulatory license data is empty for this candidate); "Diabetes Mellitus" is stated here as well-established background pharmacology for insulin glargine, not as data extracted from this pack.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1 and Type 2) — background knowledge, not present in pack |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record (flagged as a High-severity data gap). Based on known pharmacology, insulin glargine binds the insulin receptor to promote peripheral glucose uptake and suppress hepatic glucose output; its efficacy in diabetes mellitus is well established.

For autoimmune oophoritis specifically, the pack's own rationale is explicit that no direct mechanistic pathway exists between insulin/glucose metabolism and ovarian autoimmunity. The only plausible connection is indirect: autoimmune oophoritis can occur as part of autoimmune polyendocrine syndrome (APS), which frequently co-occurs with Type 1 diabetes. That is a shared-comorbidity relationship, not evidence that insulin glargine treats oophoritis — and no trial or literature evidence in this pack supports a treatment effect. This should be read as a low-confidence graph association rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are recorded for this candidate in the evidence pack — market status is "Not Marketed" with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Note: regulatory warnings/contraindications are a Blocking-severity data gap in this pack — this must be resolved before any safety assessment.)*

---

## Other Predicted Indications — Signal Quality Notes

This candidate set contains 10 predictions, and reviewing them together surfaces patterns worth flagging before committing research resources to the top-ranked one:

| Rank | Disease | Evidence | Key Concern |
|------|---------|----------|--------------|
| 6 | Pancreatic agenesis | L3, 6 PubMed refs | Not a novel repurposing signal — insulin replacement for pancreatic-agenesis-induced diabetes is already standard clinical practice. High score likely reflects a known causal fact already in the graph, not a discovery. |
| 7–10 | Localized/drug-induced lipodystrophy, centrifugal lipodystrophy, pressure-induced lipoatrophy, idiopathic localized lipodystrophy | L5, no evidence | **Likely reversed edge direction.** Insulin injection is a well-documented *cause* of injection-site lipodystrophy/lipoatrophy, not a treatment for it. These four should be treated as a possible TxGNN knowledge-graph artifact and flagged for edge-direction audit, not as research candidates. |
| 3–4 | Focal stiff limb syndrome, classic stiff person syndrome | L4, no evidence | Comorbidity confound — both conditions co-occur with anti-GAD65-antibody-positive Type 1 diabetes. Insulin here would manage the comorbid diabetes, not the neurological syndrome itself. |
| 2 | Thiamine-responsive dysfunction syndrome | L4, no evidence | Likely TRMA (Rogers syndrome), which includes a diabetes phenotype; insulin is already a known supportive treatment for that phenotype rather than a new use. |
| 5 | Opsismodysplasia | L5, no evidence | No known physiological link to insulin/glucose pathways; graph artifact, no supporting evidence. |

None of the 10 candidates currently constitute a genuine, evidence-backed new indication for insulin glargine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (autoimmune oophoritis) has no clinical trial or literature support and only an indirect, comorbidity-based mechanistic rationale. Reviewing the full candidate set raises an additional concern that at least four lower-ranked predictions (the lipodystrophy cluster) may reflect a reversed cause/effect edge in the knowledge graph rather than a treatment signal.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: regulatory warnings/contraindications (TFDA/Health Canada label data)
- Resolve the High-severity data gap: confirmed mechanism of action data from DrugBank
- Independent literature search specifically on insulin/APS/autoimmune oophoritis beyond the current DrugBank + PubMed input scope
- Manual audit of the TxGNN knowledge-graph edges underlying the lipodystrophy-cluster predictions (ranks 7–10) to rule out reversed causal direction before any further scoring
- Regulatory/licensing confirmation of insulin glargine's current Canadian market status, since 0 DINs is inconsistent with insulin glargine's known broad availability and should be verified against the Health Canada Drug Product Database
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

