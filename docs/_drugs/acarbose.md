---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Acarbose: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor that lowers blood glucose after meals, and it is generally used in diabetes. The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **0 clinical trials** and **0 publications** support this prediction. It is a model-only signal with no mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (general drug knowledge; the Health Canada licence records in the pack contain no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Acarbose is known to be an intestinal alpha-glucosidase inhibitor that slows carbohydrate digestion and reduces postprandial glucose. It acts locally in the gut.

Focal stiff limb syndrome belongs to the stiff-limb / stiff person spectrum. These are immune-mediated central nervous system disorders, often linked to anti-GAD65 antibodies and impaired GABAergic signalling. Acarbose does not act on these pathways, so **no plausible mechanistic link was identified**.

The high score (99.65%) is probably a graph-based artefact. Stiff person spectrum disorders are frequently comorbid with diabetes, and the knowledge graph may be linking the two through that shared neighbour. At most, acarbose could help glycaemic control in a patient who has both conditions. It would not treat the neurological disease itself.

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
| 2494086 | MAR-ACARBOSE |
| 2494078 | MAR-ACARBOSE |

Dosage form, manufacturer and approved indication text are not recorded for these two licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There is no trial or publication support and no plausible mechanism. Ranks 2–8 (classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia and four lipodystrophy variants) are also L5 and Hold. Rank 9, pancreatic agenesis, is L4 and Hold. Its 10 retrieved publications cover general diabetes, insulin autoimmune syndrome and postprandial hyperglycaemia, and none studies the predicted disease. Any benefit would be symptomatic glucose control in patients who also have diabetes, not repurposing for the underlying condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are missing and block safety screening
- Detailed mechanism of action data, from DrugBank
- Approved indication text, dosage form and manufacturer for the two DINs
- Any preclinical or clinical evidence linking acarbose to stiff-limb syndromes. Without it, the candidate should not advance beyond S0.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

