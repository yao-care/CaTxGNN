---
layout: default
title: Givosiran
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Early-Onset Familial Noncirrhotic Portal Hypertension

## One-Sentence Summary

Givosiran is a liver-targeted siRNA drug used for acute hepatic porphyria. The Evidence Pack does not list an approved indication, so this is taken from the literature.
The TxGNN model predicts it may be effective for **early-onset familial noncirrhotic portal hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hepatic porphyria (from the literature; no approved indication text in the licence record) |
| Predicted New Indication | Early-onset familial noncirrhotic portal hypertension |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Givosiran is a GalNAc-conjugated small interfering RNA (siRNA) that is taken up by liver cells and silences hepatic ALAS1. This lowers the heme-synthesis precursors ALA and PBG, which are thought to drive the neurovisceral attacks of acute hepatic porphyria. Formal mechanism-of-action data were not provided in the record, so this description comes from the mechanistic notes and published literature.

The evidence does not support a link between this mechanism and the predicted disease. Portal hypertension without cirrhosis is a disorder of the portal vasculature, and ALAS1 silencing does not address it. The high TxGNN score most likely reflects the drug and disease sitting close together in the knowledge graph, not a biological rationale.

The same is true of the other top-ranked predictions, which include portal vein thrombosis, hepatoportal sclerosis, hepatopulmonary syndrome and chronic viral hepatitis. None has a clinical trial or publication, and the assessments found no plausible mechanism for any of them. The one exception is rank 9, ALAD porphyria. It is a subtype of the acute hepatic porphyria family, so it is not a true repurposing case, and its only ALAD-specific report describes a lack of response to givosiran.

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
| 2506343 | GIVLAARI | — | — |

Dosage form and approved indication text are not recorded for this licence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score (L5), with no trials, no literature and no plausible mechanistic link between ALAS1 silencing and non-cirrhotic portal hypertension. Nothing currently justifies moving it forward.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence connecting hepatic ALAS1 or heme-precursor biology to portal vascular pathology
- The Canadian package insert (warnings and contraindications), and the approved indication and dosage form for DIN 2506343
- Formal mechanism-of-action data from DrugBank
- If the goal is to prioritise within givosiran's predictions, a separate review of the ALAD porphyria signal (rank 9), given the contradictory case report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

