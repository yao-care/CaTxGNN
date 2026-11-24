---
layout: default
title: Oxtriphylline
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Oxtriphylline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not specified in the available licence data"
monitor_inn: "OXTRIPHYLLINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Oxtriphylline
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

## Oxtriphylline: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Oxtriphylline is a choline salt of theophylline, a methylxanthine drug. It is marketed in Canada as an expectorant product, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of oxtriphylline as: Phosphodiesterase 4 inhibitor; Phosphodiesterase 3 inhibitor; Adenosine receptor antagonist ([ChEMBL CHEMBL1200434 (oxtriphylline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200434), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacology, oxtriphylline is a choline salt of theophylline. Theophylline is a methylxanthine that works as a non-selective phosphodiesterase inhibitor and an adenosine receptor antagonist.

A possible link to migraine runs through these two actions. Adenosine is implicated in activation of the trigeminovascular system and in cerebral vasodilation. Changes in cAMP/cGMP signalling can also affect vascular tone. Caffeine, another methylxanthine, is already used as an analgesic adjuvant in migraine therapy, which gives some indirect biological plausibility.

There are important caveats. Theophylline-class drugs can themselves provoke headache. The score of 0.9964 is a computational prediction only, and no trials or publications were found for this drug–indication pair. The original indication could not be established from the licence data, so the relationship between the old and new indications cannot be assessed.

**Other predicted indications (all L5, Hold):**

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Migraine with brainstem aura | 0.9955 | A migraine subtype. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00476374 | CHOLEDYL EXPECTORANT | GUAIFENESIN; OXTRIPHYLLINE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

**Drug Interactions:** The interaction screen was completed and found 100 interacting drugs in total. The 20 entries reviewed for this report are mostly Moderate, with a few Major and Minor ones.

- **Major:** bupropion, deferasirox, iopamidol, iohexol
- **Moderate (examples):** famotidine, ranitidine, cimetidine, nizatidine, clarithromycin, doxycycline, tetracycline, minocycline, activated charcoal, obeticholic acid, metreleptin, and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)
- **Minor:** lansoprazole, ephedrine

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on the TxGNN model score. No clinical trials or publications support oxtriphylline for migraine, and the evidence level is L5. The mechanistic rationale is indirect, and theophylline-class drugs can cause headache. Warnings and contraindications from the Canadian package insert are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The Health Canada package insert, to obtain warnings, contraindications and the approved indication
- Mechanism of action data from DrugBank
- A systematic literature search on methylxanthines (theophylline, caffeine) in migraine, including the risk of drug-induced headache
- A review of the major drug interactions (bupropion, deferasirox, iodinated contrast agents) for a migraine patient population
- Preclinical or early clinical evidence for the drug–migraine pair before moving past the model-prediction stage

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1200434 (oxtriphylline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200434) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

