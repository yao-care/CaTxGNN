---
layout: default
title: Triheptanoin
parent: Model Prediction Only (L5)
nav_order: 939
evidence_level: L5
indication_count: 10
---

# Triheptanoin
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

# Triheptanoin: From Anaplerotic Energy-Substrate Therapy to Craniostenosis Cataract

## One-Sentence Summary

Triheptanoin is an odd-chain (C7) triglyceride that supplies alternative energy substrates to cells. It is marketed in Canada as DOJOLVI, but the approved indication text is not included in the data provided.
The TxGNN model predicts it may be effective for **craniostenosis cataract** (a rare syndromic condition), but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (the Canadian licence record has no indication text) |
| Predicted New Indication | Craniostenosis cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. From general pharmacology, triheptanoin is broken down into heptanoate, which yields C4/C5 ketones and propionyl-CoA. Propionyl-CoA feeds succinyl-CoA into the TCA cycle (anaplerosis), which supports cellular energy production. The approved indication should be confirmed against the Canadian product monograph.

The link to the predicted indication is weak. Craniostenosis with cataract is a rare, likely genetic syndromic condition with no known energy-metabolism defect that this mechanism would correct. The score comes from graph-embedding similarity alone, with no supporting clinical or preclinical data.

The other nine top predictions show the same pattern:

- Seven are cataract subtypes. Their scores are identical or nearly identical (0.99971–0.99975), which suggests clustering of cataract terms in the knowledge graph rather than disease-specific signal.
- Two have only a speculative, hypothesis-level link: diabetes mellitus type 2 associated cataract and diabetic cataract. In theory, anaplerotic substrates could support lens energy metabolism under hyperglycaemic stress, but no lens data exist.
- Antithrombin deficiency type 2 has no plausible mechanistic link and is most likely an embedding artifact.

| Rank | Predicted Disease | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Craniostenosis cataract | 99.98% | L5 | Hold |
| 2 | Diabetes mellitus type 2 associated cataract | 99.98% | L5 | Research Question |
| 3 | Mature cataract | 99.98% | L5 | Hold |
| 4 | Immature cataract | 99.98% | L5 | Hold |
| 5 | Tetanic cataract | 99.98% | L5 | Hold |
| 6 | Diabetic cataract | 99.97% | L5 | Research Question |
| 7 | Cortical cataract | 99.97% | L5 | Hold |
| 8 | Nuclear senile cataract | 99.97% | L5 | Hold |
| 9 | Senile cataract | 99.97% | L5 | Hold |
| 10 | Antithrombin deficiency type 2 | 99.97% | L5 | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2512556 | DOJOLVI | Not provided | Not provided |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records for this drug. This does not confirm absence of interactions.

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-embedding score, with no trials or publications. The mechanistic link to craniostenosis cataract is not supported, and the tied scores across cataract terms point to a model artifact. Safety data for the Canadian label is also missing.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism-of-action data from DrugBank
- Any preclinical lens or cataract-model data for anaplerotic or ketogenic substrates
- A literature and trial search outside the current pack, focused on the diabetic cataract hypotheses (ranks 2 and 6), which are the most testable
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

