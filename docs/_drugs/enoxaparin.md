---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 1
---

# Enoxaparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Enoxaparin: From Anticoagulation to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin, an established anticoagulant. The available data do not list its original approved indications.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**, but **no clinical trials or publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data (drug class: anticoagulant) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the record. Based on general pharmacology, enoxaparin potentiates antithrombin and mainly inhibits factor Xa, which reduces thrombin generation. This is the reasoning below, not a finding from the supplied data.

Protein C deficiency is a hypercoagulable state caused by loss of the protein C anticoagulant pathway, which normally inactivates factors Va and VIIIa. A plausible link is that enoxaparin compensates for the missing endogenous anticoagulation through an independent, antithrombin-dependent route.

The TxGNN score is high (0.996), but it is a computational prediction only. Enoxaparin is already an established anticoagulant, so the score may reflect a known-use or class-level association rather than a novel repurposing signal. The supplied data cannot confirm which.

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
| 2509156 | REDESCA HP |
| 2506505 | NOROMBY HP |
| 2539985 | AXBERI |
| 2540045 | AXBERI |
| 2509083 | REDESCA |

Dosage form and approved indication text are not provided for these authorizations. There are 20 licenses in total.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model-level support (L5), with no registered trials or literature. The record also lacks original indications, mechanism of action, and package insert safety data, and the high score may simply reflect enoxaparin's known anticoagulant class.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action and original approved indications, for example via the DrugBank API
- Clinical trial and literature searches specific to enoxaparin in protein C deficiency
- Confirmation of whether the prediction is a known-use, class-level association or a genuinely new signal
- Approved indication text and dosage forms for the Canadian authorizations, to check route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

