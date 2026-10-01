---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 481
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog used to control blood glucose in diabetes.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting insulin analog, and its efficacy in glycemic control in diabetes is well established. The evidence provided does not show a mechanistic link to autoimmune oophoritis.

The high score (99.78%) most likely reflects proximity between autoimmune and endocrine nodes in the knowledge graph. It does not indicate a plausible effect of insulin on autoimmune attack of the ovary. Without trials or literature, this prediction should be treated as a hypothesis only.

The other eight predictions in the pack are also unsupported or weak, and none is a clear repurposing opportunity:
- **Pancreatic agenesis** is the strongest of them (Evidence Level L4). Insulin replacement is physiologically rational and already standard care. The two retrieved articles cover type 2 diabetes, not this condition, so they are only indirect evidence.
- **Thiamine-responsive dysfunction syndrome** and the **stiff-person spectrum** disorders (focal stiff limb syndrome and classic stiff person syndrome) are linked through comorbid diabetes. Insulin would only treat the diabetes, not the underlying disease.
- **Drug-induced localized lipodystrophy**, **centrifugal lipodystrophy** and **pressure-induced localized lipoatrophy** should be read as adverse-effect signals. Injected insulin is a known cause of injection-site lipodystrophy and lipoatrophy.
- **Opsismodysplasia** has only a speculative pathway link through SHIP2/PI3K signaling.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

12 authorizations are recorded. The main ones are listed below. Dosage form and approved indication text were not provided.

| DIN | Product Name |
|---------|------|
| 02403412 | HUMALOG (KWIKPEN) |
| 02469898 | ADMELOG |
| 02469901 | ADMELOG |
| 02439611 | HUMALOG 200 UNITS/ML KWIKPEN |
| 02469871 | ADMELOG SOLOSTAR |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (Evidence Level L5), and no plausible mechanism links insulin lispro to autoimmune oophoritis. The high TxGNN score most likely reflects graph proximity rather than biological effect.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), for example from DrugBank
- Health Canada package insert warnings and contraindications, which are needed for safety screening
- Any preclinical or clinical evidence linking insulin to autoimmune oophoritis
- Approved indication text and dosage forms for the Canadian licenses
- Route compatibility assessment, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

