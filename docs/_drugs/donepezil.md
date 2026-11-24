---
layout: default
title: Donepezil
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 8
monitor_inn: "Donepezil"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "extrapyramidal and movement disease", "benign shuddering attacks", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "lingual-facial-buccal dyskinesia"]
last_modified_at: 2026-11-24
description: "Donepezil: predicted new indication Psychogenic movement disorders (evidence level L5). In Canada: at least 20 DINs"
---

# Donepezil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Donepezil: Acetylcholinesterase inhibitor → psychogenic movement disorders
{: .text-alpha }

## One-Sentence Summary

Donepezil is a cholinesterase inhibitor marketed in Canada under many licences. The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **no clinical trials and no publications** currently support this specific prediction, so it remains a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 19; dormant: 1) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for donepezil: "Current theories on the pathogenesis of the cognitive signs and symptoms of Alzheimer’s disease attribute some of them to a deficiency of cholinergic neurotransmission. Donepezil hydrochloride is postulated to exert its therapeutic effect by enhancing cholinergic function." ([DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975), label version 2021-12-30; accessed 2026-11-19.) Donepezil is generally known as an acetylcholinesterase inhibitor that raises cholinergic tone, and cholinergic signalling in the basal ganglia is involved in the control of movement.

That link is plausible but speculative for this condition. Psychogenic movement disorders are functional in origin, and no established pharmacological target for donepezil has been identified for them. The high model score is therefore not backed by any trial, case report or mechanistic study in the compiled data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

The data compiled for this report show 20 valid single-ingredient licences, with no cancelled licences. The list may be partial. Dosage form and approved-indication text are not recorded in the local data.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02232043 | ARICEPT | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02232044 | ARICEPT | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02322331 | PMS-DONEPEZIL | DONEPEZIL HYDROCHLORIDE (DONEPEZIL HYDROCHLORIDE MONOHYDRATE) | Marketed |
| 02322358 | PMS-DONEPEZIL | DONEPEZIL HYDROCHLORIDE (DONEPEZIL HYDROCHLORIDE MONOHYDRATE) | Marketed |
| 02328682 | SANDOZ DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02340607 | TEVA-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02340615 | TEVA-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02362260 | APO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE (DONEPEZIL HYDROCHLORIDE MONOHYDRATE) | Marketed |
| 02381508 | TARO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02381516 | TARO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02400588 | AURO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02416417 | PRO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE (DONEPEZIL HYDROCHLORIDE MONOHYDRATE) | Marketed |
| 02426846 | DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02426854 | DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02432684 | AG-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02432692 | AG-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02467453 | M-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02475278 | DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02535386 | NRA-DONEPEZIL | DONEPEZIL HYDROCHLORIDE | Marketed |
| 02362279 | APO-DONEPEZIL | DONEPEZIL HYDROCHLORIDE (DONEPEZIL HYDROCHLORIDE MONOHYDRATE) | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. The entries listed include:
  - **Major**: Bupropion
  - **Moderate**: Famotidine, Ranitidine, Cimetidine, Hyoscyamine, Atropine, Glycopyrronium, Clidinium, Dicyclomine, Dexamethasone, Metronidazole, Loperamide, Dolasetron, Picosulfuric acid
  - **Minor**: Aprepitant, Acetylsalicylic acid, Lorcaserin, Clarithromycin

  Many of the moderate entries are anticholinergic agents, which may oppose donepezil's pharmacological action.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9923), but no clinical trials or publications address psychogenic movement disorders. The mechanistic rationale is speculative, so the evidence level is L5.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence in psychogenic (functional) movement disorders
- Detailed mechanism-of-action data for donepezil
- Package insert warnings and contraindications from Health Canada
- A safety review, since the interaction screening flagged a major interaction (bupropion) and several anticholinergic combinations, and the literature on cholinesterase inhibitors reports movement-disorder adverse effects in some patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for donepezil is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

