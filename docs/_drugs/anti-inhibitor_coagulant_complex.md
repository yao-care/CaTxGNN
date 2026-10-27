---
layout: default
title: Anti-Inhibitor Coagulant Complex
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Anti-Inhibitor Coagulant Complex: predicted new indication Glanzmann thrombasthenia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "ANTI-INHIBITOR COAGULANT COMPLEX"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets"]
---

# Anti-Inhibitor Coagulant Complex
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Anti-Inhibitor Coagulant Complex: From an Unspecified Original Indication to Glanzmann Thrombasthenia
{: .text-alpha }

## One-Sentence Summary

Anti-inhibitor coagulant complex (marketed in Canada as FEIBA NF) is a plasma-derived coagulation product, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia**,
yet **no clinical trials and no publications** currently support this direction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Based on general coagulation biology, anti-inhibitor coagulant complex is an activated prothrombin complex concentrate. It contains vitamin K-dependent factors (II, VII, IX and X, including activated forms) that promote thrombin generation.

Glanzmann thrombasthenia is a platelet disorder in which platelets cannot aggregate because the GPIIb/IIIa receptor is defective or missing. A product that boosts thrombin generation may bypass this defect and help control bleeding. This is plausible mainly for patients who do not respond to platelet transfusion or who have developed anti-platelet antibodies.

This reasoning is a hypothesis. The high score (0.993) is a computational prediction only. Real-world use, such as case reports of bypassing-agent therapy, is not captured in the data compiled for this report. The thrombotic risk known for activated prothrombin complex products has also not been weighed against the potential benefit.

A second prediction, **primary release disorder of platelets** (score 99.22%), follows a similar bypass logic. It also has no supporting trials or publications.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02202581 | FEIBA NF | Not listed | Not listed |
| 02353903 | FEIBA NF | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions** (5 interactions found):
  - **Major:** Aminocaproic acid, Aprotinin, Emicizumab, Tranexamic acid
  - **Moderate:** Coagulation factor VIIa (recombinant human)

  The major interactions involve antifibrinolytic agents and emicizumab. Combining these with a pro-coagulant product may raise thrombotic risk, so such combinations need careful review.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a plausible mechanistic basis, but there are no clinical trials or publications, and the evidence level is L5 (model prediction only). Label-based safety information is missing, and several major drug interactions are flagged. The thrombotic risk in this patient population has not been assessed.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (needed before safety screening)
- Mechanism of action data from DrugBank
- A literature search for case reports or off-label use of bypassing agents in Glanzmann thrombasthenia and platelet release disorders
- A comparison with standard management (platelet transfusion, recombinant factor VIIa, antifibrinolytics, desmopressin)
- A thrombotic risk-benefit assessment, including the interaction risks listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

