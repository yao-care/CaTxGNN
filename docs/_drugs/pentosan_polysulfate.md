---
layout: default
title: Pentosan Polysulfate
parent: Model Prediction Only (L5)
nav_order: 720
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
description: "Pentosan Polysulfate: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Pentosan Polysulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Pentosan Polysulfate: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Pentosan polysulfate is a semi-synthetic sulfated polysaccharide with heparin-like properties, originally used to treat interstitial cystitis.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction, and its anticoagulant activity could plausibly worsen bleeding in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

Two other predictions were also generated, both with equally weak support: Glanzmann thrombasthenia (0.9965) and pseudo-von Willebrand disease (0.9962). Each has an L5 evidence level and a Hold recommendation.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pentosan polysulfate is a semi-synthetic sulfated polysaccharide with heparin-like anticoagulant and weak antithrombotic activity. Its efficacy in interstitial cystitis is the basis for its original use.

Mechanistically, a heparin-like compound could plausibly affect platelet and coagulation pathways, which may explain why the model links it to platelet disorders. However, a platelet release (secretion) disorder is a platelet function defect, and an agent with anticoagulant properties would be expected to worsen bleeding rather than treat it. The mechanistic rationale for benefit is therefore unclear and possibly contradictory.

The same caution applies to the other two predictions:
- **Glanzmann thrombasthenia**: an inherited bleeding disorder caused by deficiency or dysfunction of integrin αIIbβ3 (GPIIb/IIIa), which impairs platelet aggregation. No plausible therapeutic mechanism has been established, and the association may be a network-proximity artifact of the model.
- **Pseudo-von Willebrand disease**: caused by a gain-of-function defect in platelet GPIbα that increases binding to von Willebrand factor. A sulfated polyanion could theoretically interact with these pathways, but there is no direct evidence, and anticoagulant activity raises bleeding risk in a bleeding disorder.

The prediction should be regarded as speculative and based on the model score alone.

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
| 02029448 | ELMIRON | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (these come from the TxGNN knowledge graph, not from product label text): liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease, hemophilia, and heparin-induced thrombocytopenia. Several of these overlap directly with the bleeding disorders being predicted, which is a significant concern.
- **Drug Interactions**: 58 interactions were recorded. The 20 listed in the compiled data are all of Moderate severity and mostly involve agents that affect bleeding or clotting, which raises the risk of additive bleeding. Examples include:
  - Anticoagulants: warfarin, apixaban, edoxaban, betrixaban, dalteparin, bivalirudin, antithrombin III human
  - Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, dipyridamole, cangrelor, abciximab
  - Thrombolytics and related agents: alteplase, anistreplase, defibrotide, caplacizumab
  - Radiolabelled antibodies: ibritumomab tiuxetan, tositumomab (including I-131)

Package insert warnings and contraindications from Health Canada were not available for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score, with no clinical trials or publications. The drug's anticoagulant properties and the knowledge-graph contraindications (coagulation disease, hemophilia, thrombocytopenia) point toward potential harm rather than benefit in platelet and bleeding disorders.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether any plausible therapeutic link exists
- Health Canada package insert warnings and contraindications, which are required for any safety screening
- Preclinical or mechanistic studies showing a possible benefit in platelet function disorders
- A bleeding-risk assessment specific to patients with platelet and von Willebrand-related disorders
- Approved indication text and dosage form details for the Canadian product (ELMIRON, DIN 02029448)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

