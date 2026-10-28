---
layout: default
title: Hemin
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hemin: predicted new indication Thrombocytopenic purpura (evidence level L5). Approved use: Acute intermittent porphyria"
monitor_inn: "Hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
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

## Hemin: From Acute Intermittent Porphyria to Thrombocytopenic Purpura
{: .text-alpha }

## One-Sentence Summary

Hemin is a heme preparation originally used to treat acute intermittent porphyria.
The TxGNN model predicts it may be effective for **thrombocytopenic purpura**, but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal and should be treated as a hypothesis, not as evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute intermittent porphyria |
| Predicted New Indication | Thrombocytopenic purpura |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hemin supplies heme and is known to induce heme oxygenase-1. Its efficacy in acute intermittent porphyria is established, because replenishing heme suppresses the overactive heme-synthesis pathway in that disease.

No established link between hemin and platelet disorders such as immune thrombocytopenia (ITP) or thrombotic thrombocytopenic purpura (TTP) is documented in the data compiled for this report. The very high TxGNN model (deep learning) score (0.9979) is not corroborated by any trial or publication. It comes from the model and may reflect similarities the model learned between related diseases, not biological evidence.

The other nine top-ranked predictions are all bleeding, clotting, or complement-related conditions: hemophilia, C1 inhibitor deficiency, acquired coagulation factor deficiency, serpinopathy, hereditary angioedema, inherited thrombophilia, hemophilia in female carriers, von Willebrand disease, and congenital factor XI deficiency. None has supporting clinical evidence either. Several raise safety concerns, because hemin has been reported to have mild anticoagulant effects and a risk of thrombophlebitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for thrombocytopenic purpura.

For the second-ranked prediction (hemophilia), three publications were retrieved. They concern acute hepatic porphyria (givosiran trials and a patient-reported outcomes study), not hemophilia, and were matched only by keyword. They do not support hemin in hemophilia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02478765 | PANHEMATIN | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: 74 potential interactions were identified. Those listed in the compiled data include:
  - **Major**: ethinylestradiol, estradiol, conjugated estrogens, and the barbiturates butalbital, amobarbital and phenobarbital.
  - **Moderate**: antiplatelet and anticoagulant agents (acetylsalicylic acid, abciximab, apixaban, betrixaban, dipyridamole, anagrelide, antithrombin products), alteplase, acalabrutinib, avapritinib, ibritumomab tiuxetan, I-131 tositumomab, and trastuzumab emtansine.
- **Other considerations**: Hemin has been associated with mild anticoagulant effects and thrombophlebitis. This matters if it were considered for platelet or bleeding disorders, where the combination with antiplatelet or anticoagulant agents is also a concern.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no relevant literature, and no established mechanism. Hemin's known coagulation-related adverse effects argue for caution in platelet and bleeding disorders.

**To proceed, the following is needed:**
- Mechanism of action data for hemin, and a plausible biological link to platelet disorders
- A targeted literature search for hemin or heme oxygenase-1 in ITP or TTP
- The Health Canada product monograph (warnings, contraindications, approved indication, dosage form) for PANHEMATIN
- A safety review of thrombosis and bleeding risk, and of the interactions with antiplatelet and anticoagulant drugs
- Preclinical or early exploratory evidence before any clinical trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

