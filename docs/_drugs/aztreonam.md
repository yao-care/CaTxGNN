---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-24
description: "Aztreonam: predicted new indication polyclonal hyperviscosity syndrome (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Aztreonam
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

## Aztreonam: Monobactam antibiotic → polyclonal hyperviscosity syndrome (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic that acts against aerobic Gram-negative bacteria and is marketed in Canada.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome (polyclonal hyperviscosity syndrome)**,
but **no clinical trials and no publications** support this prediction, and no plausible mechanistic link was identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | polyclonal hyperviscosity syndrome (polyclonal hyperviscosity syndrome) |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aztreonam: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), label version 2024-06-03; accessed 2026-11-19.) Aztreonam is generally known as a monobactam that inhibits penicillin-binding protein 3 in aerobic Gram-negative bacteria, which is an antibacterial action.

Polyclonal hyperviscosity syndrome is a protein/immunoglobulin disorder rather than an infection. No plausible mechanistic link to aztreonam's antibacterial activity was identified. The high TxGNN score appears to be a model artifact rather than a signal supported by clinical or literature evidence, so the prediction should be treated with strong caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02329840 | CAYSTON | AZTREONAM | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 27 potential interactions were identified in the interaction databases. Those with a Moderate level include picosulfuric acid, dicoumarol and warfarin (anticoagulant effect should be monitored when combined). Others, such as vancomycin, amikacin, amphotericin B, tacrolimus, heparin and acetylsalicylic acid, have no rated severity.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and aztreonam's antibacterial mechanism has no recognized relationship to polyclonal hyperviscosity syndrome. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Any clinical or preclinical evidence that directly studies this disease with aztreonam
- A plausible mechanistic rationale
- Health Canada package insert warnings and contraindications for safety screening
- Detailed mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

