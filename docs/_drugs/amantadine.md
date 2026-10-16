---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Amantadine: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease"
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Amantadine: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine was originally used to treat Parkinson disease and related movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **no clinical trials** and **no publications** directly supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (the Canadian license records compiled for this report contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amantadine has an established role in Parkinson disease and other movement disorders (such as dystonia and parkinsonian syndromes), and it is generally described as an NMDA receptor antagonist with dopaminergic effects.

Rasmussen encephalitis is a rare, immune-mediated brain disease that causes severe, treatment-resistant epilepsy. One plausible link is that blocking NMDA receptors could reduce glutamate-driven excitotoxicity, which is thought to contribute to neuronal injury in this condition. This is a hypothesis only. No clinical or literature data compiled for this report confirm it.

For context, other predictions for amantadine were also reviewed. Of these, post-polio myelitis (fatigue studies) and PLA2G6-associated neurodegeneration (indirect evidence from a related disease, PKAN) have some supporting literature. Rasmussen encephalitis, the top-ranked prediction, has none.

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
| 02538601 | ODAN-AMANTADINE SYRUP | Syrup (by product name) | Not available |
| 02022826 | PDP-AMANTADINE HYDROCHLORIDE SYRUP | Syrup (by product name) | Not available |
| 01990403 | PDP-AMANTADINE HYDROCHLORIDE CAPSULES | Capsule (by product name) | Not available |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, kidney disease, pyoureter, congestive heart failure, psychotic disorder, schizophreniform disorder, mental disorder, schizoaffective disorder, melanoma, angle-closure glaucoma, closed-angle glaucoma, substance-related disorder, substance abuse/dependence, atopic eczema and dermatitis. The listed **epilepsy** signal is especially relevant, because Rasmussen encephalitis presents with severe seizures.
- **Drug Interactions:** 93 interactions were identified in total. Examples:
  - **Major:** bupropion.
  - **Moderate:** anticholinergic agents (atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, propantheline, trospium, mepenzolate, methscopolamine), metoclopramide, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate.
  - **Unknown severity:** calcitriol, pantoprazole, glimepiride, doxycycline and metformin.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.48%), but there are no clinical trials or publications for Rasmussen encephalitis, and the mechanism of action data are missing. The knowledge graph also flags epilepsy as a contraindication signal, which needs careful review given the seizure-dominant nature of the target disease. At present this is a model hypothesis only.

**To proceed, the following is needed:**
- Mechanism of action data for amantadine (for example from DrugBank)
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- A targeted literature search for amantadine or NMDA antagonists in Rasmussen encephalitis and related immune-mediated epilepsies
- Review of the epilepsy contraindication signal and the major interaction with bupropion
- Preclinical or case-level evidence before considering any clinical study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

