---
layout: default
title: Bimekizumab
parent: Model Prediction Only (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: From an IL-17A/F Inhibitor to Diabetic Cataract

## One-Sentence Summary

Bimekizumab is a monoclonal antibody that neutralizes the inflammatory cytokines IL-17A, IL-17F and IL-17AF. The source record does not list an original indication.
The TxGNN model predicts it may be effective for **diabetic cataract** with a score of 98.2%, but **0 clinical trials** and **0 publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record, and no original indications are listed. Bimekizumab is known to neutralize IL-17A, IL-17F and IL-17AF. These are cytokines involved in inflammatory signaling.

The proposed link to diabetic cataract is weak. Chronic low-grade inflammation, including IL-17-related signaling, has been proposed as a contributor to diabetic complications. However, a causal role in lens opacification is speculative. The established drivers of diabetic cataract are hyperglycemia-related mechanisms, such as the polyol pathway and oxidative stress. Nothing in the available data shows that blocking IL-17 would prevent or reverse lens opacity.

The other top-ranked predictions are also mostly cataract subtypes (immature, mature, nuclear senile, cortical, senile, tetanic, craniostenosis and type 2 diabetes-associated cataract), with similar scores of about 98%. Each lacks a plausible mechanism and has no supporting evidence. The model output likely reflects shared cataract-related neighbors in the knowledge graph rather than biology specific to bimekizumab. The tenth prediction, antithrombin deficiency type 2, is a hereditary coagulation disorder unrelated to IL-17 and looks like a graph artifact.

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
| 2553627 | BIMZELX |
| 2525275 | BIMZELX |
| 2525267 | BIMZELX |
| 2553619 | BIMZELX |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no trials or publications, and no credible mechanistic link between IL-17A/F blockade and cataract formation. The high score across many cataract subtypes suggests a graph-based artifact rather than a true repurposing signal.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and original indication information for bimekizumab
- Preclinical or observational evidence linking IL-17 signaling to lens opacification in diabetes
- Confirmation of route compatibility for any ocular use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

