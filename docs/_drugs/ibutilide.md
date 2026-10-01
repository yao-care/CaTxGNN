---
layout: default
title: Ibutilide
parent: Model Prediction Only (L5)
nav_order: 459
evidence_level: L5
indication_count: 2
---

# Ibutilide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ibutilide: From Atrial Fibrillation/Flutter to Rheumatoid Arthritis

## One-Sentence Summary

Ibutilide is a class III antiarrhythmic used to convert acute atrial fibrillation or flutter to normal rhythm.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it so far.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute conversion of atrial fibrillation/flutter (the Health Canada licence record contains no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Ibutilide is generally described as a class III antiarrhythmic. It blocks the IKr (hERG) potassium channel and enhances a slow inward sodium current, which prolongs cardiac repolarisation. Its efficacy in acute atrial fibrillation/flutter is established, but no mechanistic link to rheumatoid arthritis has been shown.

Rheumatoid arthritis is a chronic systemic autoimmune disease, and ibutilide's known actions are on cardiac ion channels. Any route between the two, such as ion-channel effects on immune cells or shared neighbours in the knowledge graph, is speculative and not supported by the data provided. The high TxGNN score reflects a knowledge-graph association and is not evidence of efficacy.

Practical fit is also poor. Ibutilide is used as an inpatient intravenous drug with a known QT-prolongation and torsades de pointes risk, which makes chronic use in a long-term autoimmune condition implausible without strong supporting evidence.

A second prediction, nephrogenic syndrome of inappropriate antidiuresis (TxGNN score 99.30%), is in the same position. It is an ultra-rare V2-receptor disorder with no known link to ibutilide's mechanism. Hyponatraemia would also increase torsades risk.

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
| 2242470 | CORVERT | — | — |

The supplied record has no dosage form or indication text for this licence.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Proarrhythmic risk (from the repurposing assessment)**: Ibutilide carries QT-prolongation and torsades de pointes risk. Electrolyte disturbances such as hyponatraemia increase this risk.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the knowledge-graph score alone (Evidence Level L5, stage S0), with no trials, no literature and no established mechanism. Ibutilide's proarrhythmic risk and inpatient IV-only use further weaken the case for chronic use in rheumatoid arthritis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Detailed mechanism of action data (e.g. from DrugBank), to test for a biological link to rheumatoid arthritis
- Preclinical or observational evidence supporting a plausible immune or inflammatory effect
- Assessment of route and dosing compatibility, since the current IV inpatient use does not suit a chronic condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

