---
layout: default
title: Esketamine
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Esketamine: predicted new indication Agoraphobia (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
---

# Esketamine
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

# Esketamine: From Anxiety Disorder to Agoraphobia

## One-Sentence Summary

Esketamine was originally associated with anxiety disorder, neurotic disorder and dysthymic disorder, and it is marketed in Canada as SPRAVATO.
The TxGNN model predicts it may be effective for **agoraphobia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (from the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Esketamine is generally known as an NMDA receptor antagonist, but this could not be verified from the supplied data.

Agoraphobia is classified as an anxiety disorder, and esketamine's original indications in the knowledge graph include anxiety disorder and neurotic disorder. The high score may therefore reflect the closeness of these conditions in the knowledge graph. This is an indirect, hypothesis-level link and not clinical evidence.

Esketamine is also marketed for treatment-resistant depression, which often co-occurs with anxiety. That context is not part of the supplied data and does not support an agoraphobia claim.

The second-ranked prediction, benign paroxysmal torticollis of infancy (score 99.49%), has no supporting evidence and no plausible mechanistic bridge from the original indications. It is a rare, self-limiting paediatric movement disorder, and esketamine's safety and use in infants have not been established. It should be treated as low-plausibility, likely a graph artefact.

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
| 02499290 | SPRAVATO | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: vascular disease; arteriovenous hemangioma/malformation.
- **Drug Interactions**: 70 interactions were identified. Major-level interactions in the listed results include:
  - Diethylpropion
  - Phentermine
  - Fenfluramine
  - Mazindol
  - Caffeine

  Moderate-level interactions include opioids and related agents (morphine, liposomal morphine, opium, loperamide, difenoxin, diphenoxylate), cannabinoids (dronabinol, nabilone), metoclopramide, scopolamine, and several nasal corticosteroids and decongestants (beclomethasone, budesonide, triamcinolone, dexamethasone, ephedrine).
- Esketamine has a psychotomimetic and dissociative profile, and its safety in infants has not been established.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but it is a model prediction only. No clinical trials or publications support agoraphobia, and the mechanism of action could not be verified. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) to assess the mechanistic link to agoraphobia
- Health Canada package insert warnings and contraindications, which are required before safety screening can proceed
- Literature and clinical trial searches specific to esketamine in agoraphobia and related anxiety disorders
- Approved indication and dosage form details for DIN 02499290
- Route-of-administration compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

