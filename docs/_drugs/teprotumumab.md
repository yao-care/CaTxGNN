---
layout: default
title: Teprotumumab
parent: Model Prediction Only (L5)
nav_order: 895
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Endocrine Exophthalmos to Monosomy X

## One-Sentence Summary

Teprotumumab is an antibody originally used to treat endocrine exophthalmos (thyroid eye disease).
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endocrine exophthalmos (thyroid eye disease) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, teprotumumab is an antibody that inhibits the insulin-like growth factor 1 receptor (IGF-1R), and it is established for thyroid eye disease.

Monosomy X (Turner syndrome) is associated with short stature and altered growth-axis signalling, so a loose connection to the IGF-1 pathway is conceivable. However, IGF-1R blockade would be expected to worsen rather than improve growth deficits. Standard care for Turner syndrome is growth hormone and estrogen replacement, which works in the opposite direction.

The very high TxGNN score (0.998) most likely reflects graph proximity and ontology clustering of related disorders, not independent biological evidence. The prediction should be treated as a hypothesis only.

### Other Predicted Indications

All other predictions also have no clinical trials or literature (all L5, Hold):

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Esophageal varices without bleeding | 99.64% | No clear mechanistic link to IGF-1R inhibition |
| 3 | Esophageal varices with bleeding | 99.64% | Identical score to rank 2, suggesting a shared ontology-driven prediction |
| 4 | Mixed gonadal dysgenesis | 99.50% | Likely reflects proximity to other sex chromosome disorders |
| 5 | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 99.44% | No evidence that antibody blockade corrects a primary genetic defect |
| 6 | Turner syndrome due to structural X chromosome anomalies | 99.37% | Same rationale as monosomy X |
| 7 | Mosaic monosomy X | 99.37% | Turner syndrome variant |
| 8 | Sex chromosome disorder of sex development | 99.34% | Broad parent category |
| 9 | Varicose disease | 99.33% | Speculative link via vascular remodelling |
| 10 | X chromosome number anomaly | 99.32% | Broad category, graph association only |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02557061 | TEPEZZA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 45 interactions were identified in total, all of the 20 listed being rated Moderate. They are concentrated among glucose-lowering drugs, including:
  - Metformin, pioglitazone, acarbose
  - GLP-1 receptor agonists (semaglutide, dulaglutide, exenatide, albiglutide)
  - DPP-4 inhibitors (alogliptin, linagliptin, saxagliptin)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide)
  - Human insulin

  Blood glucose monitoring would be needed in patients on these agents.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no clinical trials or publications. The mechanism also points the wrong way, since IGF-1R inhibition would be expected to impair growth rather than help in Turner syndrome. Nothing in the data compiled for this report supports moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies showing a plausible benefit of IGF-1R blockade in monosomy X
- Specific approved indication text for the Canadian product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

