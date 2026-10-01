---
layout: default
title: Landiolol
parent: Model Prediction Only (L5)
nav_order: 517
evidence_level: L5
indication_count: 6
---

# Landiolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Landiolol: From Rapid Heart Rhythm Control to Lingual-Facial-Buccal Dyskinesia

## One-Sentence Summary

Landiolol is an ultra-short-acting, beta-1-selective adrenergic blocker given intravenously. It is generally used for heart rhythm control, although the Canadian licence record supplied here lists no approved indication text.
The TxGNN model predicts it may be effective for **lingual-facial-buccal dyskinesia**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence record (general knowledge: rapid heart rhythm control with an IV beta-1 blocker) |
| Predicted New Indication | Lingual-facial-buccal dyskinesia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, landiolol is an intravenous, ultra-short-acting beta-1-selective blocker. It has little central nervous system activity, and its efficacy in its original setting is established. Mechanistically, however, its applicability to orofacial dyskinesia is speculative.

Beta-blockade has no established role in orofacial or tardive dyskinesia. Non-selective beta-blockers such as propranolol act on some tremor and akathisia conditions. Beta-1-selective landiolol has no supporting data for movement disorders. Its IV-only route and very short half-life also make it hard to use in chronic neurological conditions.

The model's other top predictions are all movement-related conditions, and none has supporting evidence in the pack:

| Rank | Predicted Disease | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Chronic tic disorder | 99.08% | Standard therapy targets dopaminergic and alpha-2 pathways, not beta-1 blockade |
| 3 | Psychogenic movement disorders | 99.05% | No plausible mechanism; management is mainly non-pharmacological |
| 4 | Extrapyramidal and movement disease | 99.04% | Broad, non-specific category |
| 5 | Benign shuddering attacks | 99.04% | Benign, self-limiting pediatric condition; IV therapy unjustified |
| 6 | Primary orthostatic tremor | 99.00% | Weak theoretical link; generally refractory to beta-blockers |

The consistent pattern of movement-disorder predictions may reflect graph-level similarity rather than a real pharmacological link. It should be treated with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2543338 | SIBBORAN |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for landiolol in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (evidence level L5), with no trials or literature. The mechanistic link between beta-1 blockade and orofacial dyskinesia is speculative. The IV-only, short-acting profile is also impractical for a chronic condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening (currently blocking)
- Detailed mechanism of action data (for example, from DrugBank)
- Approved indication text and dosage form for the Canadian licence
- Any preclinical or clinical evidence linking beta-1 blockade to dyskinesia
- A route-compatibility assessment for IV-only administration against the chronic-use requirements of the predicted indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

