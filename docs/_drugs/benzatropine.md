---
layout: default
title: Benzatropine
parent: Model Prediction Only (L5)
nav_order: 102
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Benzatropine: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease and related movement disorders (parkinsonian syndro…"
monitor_inn: "benzatropine"
predicted_indications: ["PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder"]
---

# Benzatropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Benzatropine: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Benzatropine is an anticholinergic medicine originally used to treat Parkinson disease and related movement disorders.
The TxGNN model predicts it may be useful for **PLA2G6-associated neurodegeneration**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related movement disorders (parkinsonian syndromes, basal ganglia disease, focal hand dystonia, blepharospasm) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9917 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for benzatropine: "Benztropine mesylate possesses both anticholinergic and antihistaminic effects, although only the former have been established as therapeutically significant in the management of parkinsonism. In the isolated guinea pig ileum, the anticholinergic activity of this drug is about equal to that of atropine; however, when administered orally to unanesthetized cats, it is only about half as active as atropine." ([DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6), label version 2026-11-11; accessed 2026-11-19.) Based on known information, benzatropine is an anticholinergic (muscarinic antagonist) used for parkinsonism and dystonia, and its efficacy in these movement disorders is established.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. These conditions involve basal ganglia dysfunction with dystonia and parkinsonism. This overlaps with the motor features benzatropine is already used to treat, so it could plausibly offer **symptomatic relief**.

This link is unverified. Nothing in the data suggests benzatropine acts on the underlying PLA2G6 / phospholipid metabolism defect, so any benefit would likely be symptomatic only. Anticholinergic side effects (cognitive impairment, sedation, constipation, urinary retention) are also a concern in a progressive neurodegenerative population that often includes children.

A second prediction, **attention deficit-hyperactivity disorder** (score 0.9903), has no supporting trials or literature and a weak mechanistic rationale. Anticholinergic burden typically impairs attention and memory, which runs counter to the therapeutic goal. It should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00706531 | PDP-BENZTROPINE | BENZTROPINE MESYLATE | Marketed |
| 02238903 | BENZTROPINE OMEGA | BENZTROPINE MESYLATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (derived from drug-disease relationships, not package insert text): hypertensive disorder, chronic obstructive pulmonary disease, gastric ulcer, kidney disease, liver disease, gallbladder disease, open-angle and angle-closure glaucoma, benign prostatic hyperplasia, hypotensive disorder, coronary artery disease, *Clostridium difficile* colitis, necrotizing enterocolitis, sudden cardiac arrest, heart conduction disease, myasthenia gravis and other neuromuscular junction disease, ulcerative colitis and inflammatory bowel disease, achalasia and megaesophagus, hiatus hernia, and paralytic ileus.
- **Drug Interactions**: 78 interactions were recorded in total; 20 are listed here.
  - **Major**: potassium chloride, potassium citrate.
  - **Moderate**: other anticholinergics (hyoscyamine, atropine, clidinium, dicyclomine, glycopyrronium, mepenzolate, methscopolamine, propantheline); opioids and opioid-like agents (morphine, liposomal morphine, opium, loperamide, eluxadoline); cannabinoids (dronabinol, nabilone); metoclopramide; pramlintide.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5). There are no clinical trials or publications, and the mechanism is unverified and likely symptomatic only. The anticholinergic safety profile is a concern in a progressive neurodegenerative population that often includes children.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which is a blocking gap for safety screening
- Mechanism of action data for benzatropine
- A literature and trial search on anticholinergic treatment of dystonia-parkinsonism in PLA2G6-associated neurodegeneration
- Approved indication text and dosage forms for the Canadian products
- A benefit-risk assessment of anticholinergic burden, especially in paediatric patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

