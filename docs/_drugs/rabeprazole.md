---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 788
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "Rabeprazole"
predicted_indications: ["Smouldering systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia"]
---

# Rabeprazole
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

# Rabeprazole: From Peptic Ulcer Disease and Gastroesophageal Reflux Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease and related acid-related conditions.
The TxGNN model predicts it may be effective for **Smouldering systemic mastocytosis**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, duodenal ulcer, Zollinger-Ellison syndrome (the Canadian licence records contain no indication text, so this list comes from the knowledge graph) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rabeprazole is a proton pump inhibitor that suppresses gastric acid secretion. Its efficacy in acid-related disease is established, and it may plausibly help with symptoms in mastocytosis.

In systemic mastocytosis, mast cells release mediators such as histamine, which can drive gastric acid hypersecretion, peptic disease and reflux. Acid suppression could therefore relieve these upper gastrointestinal symptoms. This would be symptomatic management only. Nothing in the data compiled for this report suggests any effect on the underlying clonal mast cell disease (for example KIT D816V-driven proliferation) in the smouldering subtype.

The knowledge graph already lists systemic mastocytosis and mastocytosis among rabeprazole's original indications. The high score may therefore reflect an existing association rather than a new repurposing signal, which limits the independent value of this prediction.

A second prediction, lymphoadenopathic mastocytosis with eosinophilia (score 99.35%), has the same limitations: no trials, no literature, and likely reflects the related mastocytosis indications already listed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02385449 | RABEPRAZOLE | Not specified | Not specified |
| 02356538 | RABEPRAZOLE EC | Not specified | Not specified |
| 02385457 | RABEPRAZOLE | Not specified | Not specified |
| 02314177 | SANDOZ RABEPRAZOLE | Not specified | Not specified |
| 02356511 | RABEPRAZOLE EC | Not specified | Not specified |

Eight valid single-ingredient licences are listed in total (including PARIET 10 mg and 20 mg enteric-coated tablets, and a second SANDOZ RABEPRAZOLE); only the first five are shown.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture.
- **Drug Interactions**: 100 interactions were identified in the database queried. Among those reviewed, the main ones are:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: for example aminoglycosides (amikacin), amphotericin B formulations, amphetamine, apalutamide, aprepitant, armodafinil, bosutinib, thiazide diuretics (bendroflumethiazide, benzthiazide), anisindione
  - **Minor**: acetylsalicylic acid, axitinib

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or literature (Evidence Level L5). Any plausible benefit is symptomatic control of acid-related symptoms, not treatment of the underlying disease. The prediction may also simply reflect mastocytosis indications already associated with the drug.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data for rabeprazole
- Literature and trial searches on proton pump inhibitors for symptom control in systemic mastocytosis, including the smouldering subtype
- Clarification of whether mastocytosis is already an established indication, to separate genuine repurposing from existing use
- Review of the long-term safety signals (bone fracture, osteoporosis, liver disease) in the intended mastocytosis population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

