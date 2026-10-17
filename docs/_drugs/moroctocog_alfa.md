---
layout: default
title: Moroctocog Alfa
parent: Model Prediction Only (L5)
nav_order: 631
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Moroctocog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Hemophilia"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Moroctocog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Moroctocog Alfa: From Hemophilia to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant (B-domain deleted) factor VIII product, originally used to treat hemophilia, including the symptomatic form in female carriers.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia; symptomatic form of hemophilia in female carriers |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, moroctocog alfa is a recombinant factor VIII that replaces the missing clotting factor in hemophilia A, and its efficacy there is the basis for its marketed use.

The predicted new indication is a primary platelet function defect, in which platelets fail to release their granule contents properly. Factor VIII activity in these patients is normally intact, so factor VIII replacement does not address the underlying defect. The very high TxGNN score (99.97%) most likely reflects shared bleeding-disorder associations in the knowledge graph rather than a true mechanistic rationale.

**Other predictions considered (all L5, all Hold):**

| Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|------|------|------|
| Pseudo-von Willebrand disease | 99.97% | Weak. Platelet GPIbα gain-of-function defect. Factor VIII is carried by VWF, so there is an indirect link only. |
| Glanzmann thrombasthenia | 99.96% | Weak. Integrin αIIbβ3 defect. Standard therapy is platelet transfusion or recombinant factor VIIa. |
| Acquired coagulation factor deficiency | 99.88% | Most plausible. Factor VIII could in principle treat an acquired deficiency, but inhibitory autoantibodies (acquired hemophilia A) often neutralize it, and the category also includes deficiencies of other factors. |
| Scott syndrome | 99.86% | Weak. Defective platelet phosphatidylserine exposure with normal factor VIII levels. |
| Bleeding diathesis due to a collagen receptor defect | 99.73% | Weak. Platelet-intrinsic defect. |
| Hemorrhagic disorder due to a constitutional thrombocytopenia | 99.72% | Weak. Bleeding stems from low platelet count, not factor VIII deficiency. |
| "Flood factor deficiency" | 99.11% | Cannot be assessed. The term is not a recognized standard name and the entity needs clarification. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02374072 | XYNTHA SOLOFUSE | Not specified | Not specified |
| 02309491 | XYNTHA | Not specified | Not specified |
| 02309483 | XYNTHA | Not specified | Not specified |
| 02374099 | XYNTHA SOLOFUSE | Not specified | Not specified |
| 02374080 | XYNTHA SOLOFUSE | Not specified | Not specified |

A sixth license (DIN 02374064, XYNTHA SOLOFUSE) is also valid. All six licenses are single-ingredient products with valid status and none are cancelled.

## Safety Considerations

No drug interactions were found in the data compiled for this report, and no disease-specific contraindications were recorded from the knowledge graph.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score, with no clinical trials or publications. Primary platelet release disorder is a platelet-intrinsic defect with normal factor VIII activity, so there is no clear mechanistic reason for factor VIII replacement to help. Among the other predicted indications, acquired coagulation factor deficiency is the most plausible but still lacks any supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to support a mechanistic-link analysis
- Dosage form and approved indication text for the Canadian licenses
- Clarification of the ambiguous "flood factor deficiency" entry
- Any clinical or preclinical evidence for factor VIII in the predicted conditions, with priority on acquired coagulation factor deficiency
- Route-of-administration compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

