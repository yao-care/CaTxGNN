---
layout: default
title: Tezepelumab
parent: Model Prediction Only (L5)
nav_order: 906
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tezepelumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Severe asthma"
monitor_inn: "Tezepelumab"
predicted_indications: ["diabetic cataract", "tetanic cataract", "craniostenosis cataract", "immature cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic retinopathy"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tezepelumab: From Severe Asthma to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Tezepelumab is an anti-TSLP monoclonal antibody marketed in Canada as TEZSPIRE. The Health Canada data compiled for this report do not list an approved indication text, but the drug is known for severe asthma.
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe asthma (general drug knowledge; the Canadian license records compiled for this report contain no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tezepelumab is known to be a monoclonal antibody that blocks thymic stromal lymphopoietin (TSLP), an epithelial alarmin that drives type 2 and other inflammatory signaling. Its efficacy in severe asthma is the basis of its marketing authorization.

A link to diabetic cataract is speculative. One hypothesis is that TSLP-related inflammatory signaling could play a role in the lens epithelium or in diabetic ocular inflammation. No data compiled for this report support this. The high TxGNN score (0.984) is a graph-based prediction. It likely reflects clustering of related cataract terms in the knowledge graph rather than a drug-specific signal.

Other cataract subtypes also scored highly (about 0.98), including tetanic, craniostenosis, immature, mature, type 2 diabetes-associated, nuclear senile, cortical and senile cataract. Several have no plausible link to TSLP blockade. For example, tetanic cataract arises from calcium disturbance, craniostenosis cataract is a developmental genetic disorder, and age-related cataract is driven by oxidative damage and crystallin aggregation. This pattern supports reading the predictions as a cluster effect.

Diabetic retinopathy (score 0.981) is the biologically most plausible of the ten predictions, because inflammation and cytokine signaling contribute to the disease. It remains hypothetical and could only be framed as a preclinical research question, such as TSLP expression in the diabetic retina.

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
| 02529548 | TEZSPIRE | Not specified | Not specified |
| 02529556 | TEZSPIRE | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for this drug in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature and no supported mechanistic link between TSLP blockade and lens opacity. The same score pattern across unrelated cataract subtypes suggests a knowledge-graph clustering effect rather than a real drug-specific signal.

**To proceed, the following is needed:**
- Mechanism of action data for tezepelumab, to allow a proper mechanistic-link analysis
- Health Canada package insert warnings, contraindications and approved indication text
- Preclinical evidence of TSLP involvement in lens or diabetic ocular pathology, for example in the diabetic retina
- A literature search for TSLP in cataract and diabetic eye disease
- A route-of-administration assessment, since the available routes (systemic biologic) have not been compared with ocular treatment needs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

