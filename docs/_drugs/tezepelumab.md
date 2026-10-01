---
layout: default
title: Tezepelumab
parent: Model Prediction Only (L5)
nav_order: 899
evidence_level: L5
indication_count: 10
---

# Tezepelumab
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

# Tezepelumab: From Severe Asthma to Diabetic Cataract

## One-Sentence Summary

Tezepelumab is an anti-TSLP monoclonal antibody marketed in Canada as TEZSPIRE, with severe asthma as its original use. The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe asthma (taken from the prediction rationale; the Canadian license records contain no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, tezepelumab is a monoclonal antibody that blocks thymic stromal lymphopoietin (TSLP), an upstream cytokine in type 2 inflammation. Its efficacy in severe asthma is the basis for its marketing.

The link to diabetic cataract is weak. Diabetic cataract is driven mainly by hyperglycaemia-related processes such as the polyol pathway and oxidative stress. TSLP blockade does not address these, and no established connection between TSLP signalling and lens opacification was identified.

The high score (98.40%) most likely reflects proximity among cataract-related nodes in the knowledge graph rather than pharmacology. Nine of the top ten predictions are cataract subtypes with nearly identical scores (98.2%–98.4%), which points to a correlated artifact rather than independent signals. These include:

- Tetanic cataract
- Craniostenosis cataract
- Immature cataract
- Mature cataract
- Type 2 diabetes-associated cataract
- Nuclear senile cataract
- Cortical cataract
- Senile cataract

The tenth prediction, **diabetic retinopathy** (98.12%), is the only one with a plausible biological angle, since chronic low-grade inflammation and cytokine signalling contribute to the disease. It is flagged as a research question only. A role for TSLP in retinal pathology is hypothetical, and ocular penetration of a systemic IgG2 antibody would also need to be considered.

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
| 2529548 | TEZSPIRE |
| 2529556 | TEZSPIRE |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no trials, no publications and no plausible mechanism linking TSLP blockade to lens opacification. The clustering of near-identical scores across cataract subtypes suggests a graph artifact rather than a real signal.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and the approved indication text from the Health Canada product monograph
- Package insert warnings and contraindications, which are required before any safety screening
- Preclinical or mechanistic evidence for TSLP involvement in lens or retinal pathology
- If follow-up is pursued, prioritise diabetic retinopathy as a research question, starting with a preclinical or retrospective-cohort study that also addresses ocular penetration of a systemic antibody

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

