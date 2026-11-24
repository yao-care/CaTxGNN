---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
monitor_inn: "ADAPALENE"
predicted_indications: ["zinc, elevated plasma"]
last_modified_at: 2026-11-24
description: "Adapalene: predicted new indication zinc, elevated plasma (evidence level L5). In Canada: 10 DINs (10 marketed)"
---

# Adapalene
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

## Adapalene: topical retinoid (RAR-β/γ agonist) → zinc, elevated plasma
{: .text-alpha }

## One-Sentence Summary

Adapalene is a topical retinoid used on the skin. The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but **no clinical trials and no publications** currently support this direction, so it rests on a model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | zinc, elevated plasma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 10 of 10) |
| Number of DINs | 10 (marketed: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for adapalene: "Adapalene binds to specific retinoic acid nuclear receptors but does not bind to cytosolic receptor protein. Biochemical and pharmacological profile studies have demonstrated that adapalene is a modulator of cellular differentiation, keratinization, and inflammatory processes." ([DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec), label version 2023-12-27; accessed 2026-11-19.) From general pharmacology, adapalene is a topical retinoid that selectively binds retinoic acid receptors (RAR-β and RAR-γ) and modulates keratinocyte differentiation and inflammation.

Elevated plasma zinc (hyperzincemia) is a biochemical state, typically caused by excess zinc intake, certain genetic variants, or altered zinc-binding protein levels. No known pathway links RAR signalling to systemic zinc homeostasis in a way that would support therapeutic use. The high score of 0.9951 most likely reflects network proximity in the model (for example shared zinc- or retinoid-related gene and protein associations) rather than biological or clinical validity. Adapalene is also applied topically with low systemic absorption, so an effect on plasma zinc is improbable. The prediction should be treated as a weak, unvalidated hypothesis.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02148749 | DIFFERIN | ADAPALENE | Marketed |
| 02231592 | DIFFERIN | ADAPALENE | Marketed |
| 02274000 | DIFFERIN XP | ADAPALENE | Marketed |
| 02365871 | TACTUPUMP | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02446235 | TACTUPUMP FORTE | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02456923 | TARO-ADAPALENE/BENZOYL PEROXIDE | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02489007 | SANDOZ ADAPALENE / BENZOYL PEROXIDE | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02505053 | TARO-ADAPALENE/BENZOYL PEROXIDE FORTE | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02517205 | SANDOZ ADAPALENE / BENZOYL PEROXIDE FORTE | ADAPALENE; BENZOYL PEROXIDE | Marketed |
| 02550423 | CABTREO | ADAPALENE; BENZOYL PEROXIDE; CLINDAMYCIN PHOSPHATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Ten valid licences are on record.

## Safety Considerations

- **Drug Interactions**: 58 potential interactions were identified in the interaction database, all with an unspecified severity level. Examples include doxycycline, minocycline, tetracycline, metronidazole, prednisone, triamcinolone, budesonide, ibuprofen and fluconazole.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or literature, no plausible mechanistic link between retinoid receptor signalling and plasma zinc, and minimal systemic exposure from topical use.

**To proceed, the following is needed:**
- Any study directly addressing adapalene and plasma zinc levels
- Mechanism-of-action data and a plausible biological pathway
- Package insert warnings and contraindications from Health Canada
- Evidence on systemic absorption and route compatibility for a systemic condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for adapalene are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

