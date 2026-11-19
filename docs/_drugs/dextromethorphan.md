---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 274
evidence_level: L5
indication_count: 5
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
last_modified_at: 2026-11-20
description: "Dextromethorphan: predicted new indication nasal cavity disease (evidence level L5). In Canada: at least 20 DINs"
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dextromethorphan: NMDA receptor antagonist and sigma-1 agonist (centrally acting antitussive) → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Dextromethorphan is a centrally acting cough suppressant that is marketed in Canada in many single-ingredient products.
The TxGNN model predicts it may be relevant for **nasal cavity disease**, but **no clinical trials and no publications** were found to support this direction, so the evidence rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dextromethorphan acts in the central nervous system as an NMDA receptor antagonist and sigma-1 receptor agonist. According to the Mechanism of Action section of the US FDA-approved prescribing information for dextromethorphan hydrobromide, bupropion hydrochloride (a combination product containing dextromethorphan): "Dextromethorphan is an uncompetitive antagonist of the NMDA receptor (an ionotropic glutamate receptor) and a sigma-1 receptor agonist. The mechanism of dextromethorphan in the treatment of MDD and agitation associated with dementia due to Alzheimer’s disease is unclear." ([DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79), label version 2026-08-17; accessed 2026-11-19.) This description reflects general pharmacological knowledge rather than the supplied data.

The high score for nasal cavity disease most likely reflects how close this condition sits to upper respiratory conditions already linked to the drug, such as rhinitis and the common cold. It looks like a broad parent-category prediction that overlaps with those existing uses rather than a new repurposing signal. Nothing in the supplied data gives an independent mechanistic reason why a centrally acting antitussive would treat a disease of the nasal cavity itself. At most, it may relieve symptoms such as cough that accompany these conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

At least 20 valid single-ingredient licences were found, and the list may be partial. Approved indication text is not recorded in the local data. Five representative products:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01944738 | BENYLIN EXTRA STRENGTH DRY COUGH | Not recorded | Not recorded |
| 02511320 | BUCKLEY'S DRY COUGH EXTRA STRENGTH | Not recorded | Not recorded |
| 02534754 | DRY COUGH RELIEF EXTRA STRENGTH | Not recorded | Not recorded |
| 01928775 | BALMINIL DM (3MG/ML SUCROSE FREE) | Not recorded | Not recorded |
| 02549360 | DAYQUIL KIDS HONEY | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions include:
  - Serotonergic agents: dexfenfluramine, fenfluramine, lorcaserin, sibutramine
  - 5-HT3 antagonist antiemetics: dolasetron, granisetron, ondansetron, palonosetron
- Moderate-level examples: bupropion, cimetidine, morphine, metoclopramide, opium, phentermine, dronabinol, nabilone, eliglustat, mazindol, glycerol phenylbutyrate.
- **Other considerations**: Dextromethorphan depends on CYP2D6 metabolism, so CYP2D6 inhibitors (such as bupropion) deserve particular attention.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there is no clinical or published evidence for nasal cavity disease, and the prediction likely overlaps with conditions the drug is already associated with. No independent mechanistic rationale is supported.

**To proceed, the following is needed:**
- Direct clinical or preclinical studies in nasal cavity disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A clear definition of how the predicted condition differs from the existing upper respiratory uses
- A review of the interaction profile (serotonergic agents, CYP2D6 inhibitors) for any new use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

