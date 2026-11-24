---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Ethosuximide: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Absence epilepsy"
monitor_inn: "ETHOSUXIMIDE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ethosuximide: From Absence Epilepsy to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ethosuximide is an anti-seizure medicine originally used to treat absence epilepsy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ethosuximide: "Ethosuximide suppresses the paroxysmal three cycle per second spike and wave activity associated with lapses of consciousness which is common in absence (petit mal) seizures. The frequency of epileptiform attacks is reduced, apparently by depression of the motor cortex and elevation of the threshold of the central nervous system to convulsive stimuli." ([DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6), label version 2026-05-25; accessed 2026-11-19.) Ethosuximide is generally known to block T-type calcium channels in thalamic neurons, which underlies its effect against absence seizures.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). The receptor is constitutively active, so the body retains water even when vasopressin levels are low. No link between T-type calcium channel blockade and V2 receptor signalling is established, so the two conditions do not share an obvious mechanism.

The very high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by clinical or literature evidence. The idea would need independent mechanistic testing first, for example whether ethosuximide affects cAMP signaling or aquaporin-2 trafficking in collecting-duct cells.

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
| 00022799 | ZARONTIN | ETHOSUXIMIDE | Marketed |
| 00023485 | ZARONTIN SYRUP | ETHOSUXIMIDE | Marketed |
| 02545772 | MAR-ETHOSUXIMIDE | ETHOSUXIMIDE | Marketed |
| 02547171 | ODAN-ETHOSUXIMIDE | ETHOSUXIMIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications / cautions from the knowledge graph (not label text)**: The model's knowledge graph links ethosuximide to the following conditions as contraindications: anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, haematologic disease, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis and acute intermittent porphyria. The kidney disease link deserves particular attention given the proposed renal-related indication.
- **Drug Interactions**: 92 interacting drugs were identified. The 20 listed in the compiled data are all rated Moderate: aprepitant, morphine (including liposomal), dronabinol, nabilone, metoclopramide, opium, sibutramine, ethanol, cobicistat, folic acid, deferasirox, promethazine, levoleucovorin, leucovorin, fostamatinib, chloroquine, mefloquine, hydroxychloroquine and chlorpheniramine. Many of these are central nervous system depressants or affect folate handling.

Please refer to the Health Canada package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it (evidence level L5). There are no trials or publications, and no plausible mechanistic link between T-type calcium channel blockade and the AVPR2 gain-of-function that drives NSIAD. The knowledge graph also lists kidney disease as a contraindication.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical mechanistic testing, such as effects on cAMP signalling or aquaporin-2 trafficking in collecting-duct cells
- A literature and trial search specific to NSIAD, to confirm that no supporting studies exist
- Dosage form and approved indication details for the four Canadian DINs

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

