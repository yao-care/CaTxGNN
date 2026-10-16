---
layout: default
title: Teplizumab
parent: Model Prediction Only (L5)
nav_order: 894
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Teplizumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Delay of onset of stage 3 type 1 diabetes"
---

# Teplizumab
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

# Teplizumab: From Delaying Stage 3 Type 1 Diabetes to Diabetic Cataract

## One-Sentence Summary

Teplizumab is an anti-CD3 monoclonal antibody, approved in 2022 to delay the onset of stage 3 type 1 diabetes. The TxGNN model predicts it may be effective for **diabetic cataract**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Delay of onset of stage 3 type 1 diabetes (per the pharmacology data compiled for this report; the Canadian licence record contains no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, teplizumab is a humanized anti-CD3 antibody (a derivative of OKT3) that binds CD3e on T cells. It modulates T-cell activity to slow the autoimmune destruction of pancreatic beta cells.

The link to diabetic cataract is indirect at best. If teplizumab preserves beta-cell function and improves glycaemic control, it could in theory reduce hyperglycaemia-driven lens damage, such as polyol pathway activity. No direct effect on the lens has been established.

The high TxGNN score reflects proximity in a knowledge graph, not biological or clinical proof. Several other top-ranked predictions (for example immature, tetanic, craniostenosis-associated and senile cataract, and type 2 antithrombin deficiency) have no plausible mechanistic link. This suggests the score is partly a graph-propagation artifact from shared cataract-related nodes.

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
| 02557347 | TZIELD | Not listed | Not listed in the licence record |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry. It is a target-binding record (CD3e, the antibody's target), not a drug–drug interaction with a severity level.
- **Other relevant observations**: Development for moderate to severe psoriasis was terminated because of injection site reactions.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score, with no clinical trials, no literature and no established lens-specific mechanism. Package insert safety data are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- A literature and trial search specific to diabetic cataract
- Preclinical or mechanistic evidence for an effect on the lens, or an effect via preserved beta-cell function
- Assessment of route and formulation compatibility (the product is a systemic biologic)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

