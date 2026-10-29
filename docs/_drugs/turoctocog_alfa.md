---
layout: default
title: Turoctocog Alfa
parent: Model Prediction Only (L5)
nav_order: 955
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Turoctocog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Hemophilia (including the symptomatic form of hemophilia in female ca…"
monitor_inn: "TUROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "thrombotic thrombocytopenic purpura", "hereditary thrombocytosis with transverse limb defect"]
---

# Turoctocog Alfa
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

## Turoctocog Alfa: From Hemophilia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Turoctocog alfa is a recombinant factor VIII (FVIII) replacement product, originally used to treat hemophilia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but **no clinical trials and no publications** currently support this direction, and the biological rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia (including the symptomatic form of hemophilia in female carriers) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 14) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, turoctocog alfa is a recombinant, B-domain-truncated FVIII. It replaces the missing clotting factor in hemophilia A, and its efficacy in that setting is established.

Primary release disorder of platelets is a platelet function defect caused by impaired granule secretion. It is not caused by FVIII deficiency. Because FVIII replacement does not address the underlying defect, there is no plausible direct mechanism. The high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. Most involve platelet or von Willebrand factor (VWF) defects (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, constitutional thrombocytopenia), where FVIII replacement is not expected to help. The most biologically plausible candidate is **acquired coagulation factor deficiency** (rank 5, for example acquired hemophilia A). Even there, autoantibody inhibitors neutralize FVIII, bypassing agents are the standard of care, and turoctocog alfa is not established for this use. It is best treated as a research question rather than a candidate for development.

One prediction, **thrombotic thrombocytopenic purpura**, raises a theoretical safety concern, since a procoagulant agent could worsen a prothrombotic state.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Turoctocog alfa is authorized in Canada under 20 valid single-ingredient licences. The data compiled for this report do not include dosage form or approved indication text for these entries. The five listed below are examples; the remaining licences are under the same or related brand names.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02435217 | ZONOVATE | Not available | Not available |
| 02435187 | ZONOVATE | Not available | Not available |
| 02435209 | ZONOVATE | Not available | Not available |
| 02451484 | KOVALTRY | Not available | Not available |
| 02451476 | KOVALTRY | Not available | Not available |

Note: the licence list also includes products carrying other brand names (OBIZUR, HUMATE-P, ELOCTATE, ADYNOVATE). These should be verified against Health Canada records to confirm which licences correspond to turoctocog alfa itself.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

One theoretical concern applies to the predicted indications: FVIII replacement in thrombotic thrombocytopenic purpura could worsen the prothrombotic state.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (evidence level L5). Platelet release disorders arise from platelet function defects, not FVIII deficiency, so the high TxGNN score appears to be a network-propagation artifact. Acquired coagulation factor deficiency is the only candidate with any plausibility, and it is better framed as a research question than a repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data for turoctocog alfa
- Package insert warnings and contraindications from Health Canada
- A mechanistic and clinical literature review for acquired FVIII deficiency, if it is pursued as a research question
- Verification of the ambiguous "flood factor deficiency" term against the source ontology
- Confirmation of which Canadian licences correspond to turoctocog alfa, with dosage form and indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

