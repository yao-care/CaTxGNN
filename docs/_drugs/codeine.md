---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "CODEINE"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
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

## Codeine: From Allergic Rhinitis and Related Upper Airway Conditions to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid originally associated with symptom relief in upper airway and headache conditions, such as allergic rhinitis, pharyngitis, the common cold and headache disorder.
The TxGNN model predicts it may be useful for **nasal cavity disease**, but there are **0 clinical trials** and only **1 publication** (a case report describing an adverse event rather than a benefit), so the prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (the Canadian licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Codeine is generally known as an opioid analgesic and cough suppressant, but the data compiled for this report do not include a mechanism entry, so no mechanism-based link can be drawn here.

The high score (0.9993) comes from the TxGNN model (deep learning). It may reflect similarities the model learned between "nasal cavity disease" and codeine's existing rhinitis, nasopharyngitis and common cold indications, not biological evidence that codeine treats nasal disease. The only publication is a case report of a rhinolith (nasal stone) formed around a hardened codeine and opium mixture, an incidental or harmful event rather than a therapeutic effect.

Other predictions in the same analysis show a similar pattern:

- **Trigeminal autonomic cephalalgia** (score 0.9943): opioids are not recommended for cluster headache and carry risks of medication-overuse headache and dependence. The two papers retrieved do not show any benefit.
- **Allergic urticaria** (score 0.9937): the literature points the opposite way. Codeine directly triggers mast cell histamine release, is used as a positive control in skin tests, and can itself cause urticarial rash. Repurposing for this condition is not supported and may be harmful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a rhinolith formed around an impacted foreign body, which turned out to be a hardened codeine and opium mixture. This describes an adverse or incidental event, not a treatment effect. |

---

## Canada Market Information

Twenty valid single-ingredient licences are on record. The records do not include dosage form or approved indication text. The five listed below are examples.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00593451 | TEVA-CODEINE | Not specified | Not specified |
| 02009757 | CODEINE 30 | Not specified | Not specified |
| 00050024 | CODEINE PHOSPHATE SYRUP | Not specified | Not specified |
| 02163748 | CODEINE CONTIN 100MG CONTROLLED RELEASE TAB | Controlled-release tablet | Not specified |
| 02154234 | ACETAMINOPHEN, CAFFEINE AND CODEINE PHOSPHATE TABLETS | Tablet | Not specified |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationships in the knowledge graph, not from label text): hypertension, liver failure and liver disease, kidney disease, epilepsy, insomnia, chronic obstructive pulmonary disease, anxiety and other mental disorders (including psychotic disorders), porphyria, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, gastritis and dermatitis herpetiformis.
- **Drug Interactions**: 100 interactions were found in total. Two are rated Major: **alvimopan** and **bupropion**. Many others are rated Moderate, including atropine, cimetidine, dexamethasone, dicyclomine, loperamide, glycopyrronium, hyoscyamine, granisetron, dolasetron, dronabinol, eliglustat, eluxadoline and fenfluramine.
- Opioids can cause allergic urticarial rash and contact dermatitis, and codeine directly triggers mast cell histamine release (see the allergic urticaria literature above).

Warnings and contraindications from the Canadian package insert were not available. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there are no clinical trials, and the only publication is a case report of an adverse event. The prediction most likely reflects proximity to codeine's existing symptomatic indications, not a new therapeutic signal. The other top predictions are either simple extensions of current use, unsupported (trigeminal autonomic cephalalgia), or point to possible harm (allergic urticaria).

**To proceed, the following is needed:**
- Mechanism of action data, to allow any mechanistic-link analysis
- The Health Canada package insert, with its warnings and contraindications, so that safety screening can begin
- Evidence that codeine provides a therapeutic benefit in nasal cavity disease, such as controlled studies or mechanistic or preclinical data
- A clearer definition of what "nasal cavity disease" means here, since it is a broad category, and a check of whether any benefit goes beyond symptomatic cough or cold relief
- Review of opioid-specific risks (dependence, respiratory depression, and the genetic variability in codeine metabolism) against any proposed new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

