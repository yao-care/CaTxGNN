---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 828
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: predicted new indication Perioral myoclonia with absences (evidence level L5). In Canada: 5 DINs (5 marketed)"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## One-Sentence Summary

Rufinamide is an antiseizure medication originally used to treat Lennox-Gastaut syndrome.
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Perioral myoclonia with absences |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

Note: the Canadian licence records compiled for this report contain no approved-indication text.

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for rufinamide: "The precise mechanism(s) by which rufinamide exerts its antiepileptic effect is unknown. The results of in vitro studies suggest that the principal mechanism of action of rufinamide is modulation of the activity of sodium channels and, in particular, prolongation of the inactive state of the channel." ([DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d), label version 2022-12-15; accessed 2026-11-19.) Based on general knowledge, rufinamide is an antiseizure medication that is widely understood to prolong the inactive state of voltage-gated sodium channels. It is approved for Lennox-Gastaut syndrome, a severe childhood epileptic encephalopathy.

FIRES is also a severe, treatment-resistant epileptic encephalopathy. However, neuroinflammation is thought to play a major role in it, so a sodium-channel mechanism alone gives only a plausible but unproven link. It is not clinical evidence.

Other predicted indications also have no supporting studies. They are listed below for reference:

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Perioral myoclonia with absences | 0.9951 | L5 |

For atypical childhood epilepsy with centrotemporal spikes, sodium-channel blockers can aggravate some of these syndromes. This would need careful consideration in any future evaluation.

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
| 02545985 | AURO-RUFINAMIDE | Not specified | Not specified |
| 02369613 | BANZEL | Not specified | Not specified |
| 02369648 | BANZEL | Not specified | Not specified |
| 02369621 | BANZEL | Not specified | Not specified |
| 02545993 | AURO-RUFINAMIDE | Not specified | Not specified |

All five licences are valid single-ingredient products.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from network associations, not from package insert text): liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder, dysthymic disorder.
- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed here were all rated Moderate. They include:
  - Corticosteroids: hydrocortisone, prednisone, betamethasone, triamcinolone
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol
  - Opioids and related agents: morphine, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Antiemetics and prokinetics: ondansetron, metoclopramide, rolapitant
  - Others: pioglitazone, bupropion, eliglustat, naloxegol, nitisinone

Please refer to the package insert for warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no registered trials or publications. The mechanistic link to FIRES is plausible but unproven.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Detailed mechanism of action data, for example from DrugBank
- A literature and trial search for rufinamide in FIRES and other refractory epileptic encephalopathies
- A review of the relevance of the knowledge-graph contraindications (liver disease, leukopenia) to the target population
- Dosage form and approved-indication details for the Canadian licences, to assess route compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

