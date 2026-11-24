---
layout: default
title: Turoctocog Alfa
parent: Model Prediction Only (L5)
nav_order: 955
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Turoctocog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Hemophilia (including the symptomatic form of hemophilia in female ca…"
monitor_inn: "TUROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "thrombotic thrombocytopenic purpura", "hereditary thrombocytosis with transverse limb defect"]
---

# Turoctocog Alfa
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

## Turoctocog Alfa: From Hemophilia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Turoctocog alfa is a recombinant factor VIII (FVIII) replacement product, originally used to treat hemophilia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but **no clinical trials and no publications** currently support this direction, and the biological rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia (including the symptomatic form of hemophilia in female carriers) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 14; dormant: 6) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of turoctocog alfa as: Coagulation factor VIII exogenous protein ([ChEMBL CHEMBL2108286 (turoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2108286), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, turoctocog alfa is a recombinant, B-domain-truncated FVIII. It replaces the missing clotting factor in hemophilia A, and its efficacy in that setting is established.

Primary release disorder of platelets is a platelet function defect caused by impaired granule secretion. It is not caused by FVIII deficiency. Because FVIII replacement does not address the underlying defect, there is no plausible direct mechanism. The high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. Most involve platelet or von Willebrand factor (VWF) defects (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, constitutional thrombocytopenia), where FVIII replacement is not expected to help. The most biologically plausible candidate is **acquired coagulation factor deficiency** (rank 5, for example acquired hemophilia A). Even there, autoantibody inhibitors neutralize FVIII, bypassing agents are the standard of care, and turoctocog alfa is not established for this use. It is best treated as a research question rather than a candidate for development.

One prediction, **thrombotic thrombocytopenic purpura**, raises a theoretical safety concern, since a procoagulant agent could worsen a prothrombotic state.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- review:begin ca-lic-20261124b-turoctocog_alfa-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The remaining licences are under the same or related brand names." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-turoctocog_alfa-1 -->

Turoctocog alfa is authorized in Canada under 20 valid single-ingredient licences. The data compiled for this report do not include dosage form or approved indication text for these entries.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02261219 | HUMATE-P | ANTIHEMOPHILIC FACTOR (HUMAN); VON WILLEBRAND FACTOR (HUMAN) | Marketed |
| 02261227 | HUMATE-P | ANTIHEMOPHILIC FACTOR (HUMAN); VON WILLEBRAND FACTOR (HUMAN) | Marketed |
| 02261235 | HUMATE-P | ANTIHEMOPHILIC FACTOR (HUMAN); VON WILLEBRAND FACTOR (HUMAN) | Marketed |
| 02430312 | ELOCTATE | ANTIHEMOPHILIC FACTOR (RECOMBINANT BDD), FC FUSION PROTEIN | Marketed |
| 02430320 | ELOCTATE | ANTIHEMOPHILIC FACTOR (RECOMBINANT BDD), FC FUSION PROTEIN | Marketed |
| 02430339 | ELOCTATE | ANTIHEMOPHILIC FACTOR (RECOMBINANT BDD), FC FUSION PROTEIN | Marketed |
| 02447401 | OBIZUR | ANTIHEMOPHILIC FACTOR (RECOMBINANT) PORCINE SEQUENCE | Marketed |
| 02451441 | KOVALTRY | ANTIHEMOPHILIC FACTOR (RECOMBINANT) | Marketed |
| 02451468 | KOVALTRY | ANTIHEMOPHILIC FACTOR (RECOMBINANT) | Marketed |
| 02451476 | KOVALTRY | ANTIHEMOPHILIC FACTOR (RECOMBINANT) | Marketed |
| 02451484 | KOVALTRY | ANTIHEMOPHILIC FACTOR (RECOMBINANT) | Marketed |
| 02451492 | KOVALTRY | ANTIHEMOPHILIC FACTOR (RECOMBINANT) | Marketed |
| 02498537 | ADYNOVATE | ANTIHEMOPHILIC FACTOR (RECOMBINANT), PEGYLATED | Marketed |
| 02498545 | ADYNOVATE | ANTIHEMOPHILIC FACTOR (RECOMBINANT), PEGYLATED | Marketed |
| 02435187 | ZONOVATE | TUROCTOCOG ALFA | Dormant |
| 02435195 | ZONOVATE | TUROCTOCOG ALFA | Dormant |
| 02435209 | ZONOVATE | TUROCTOCOG ALFA | Dormant |
| 02435217 | ZONOVATE | TUROCTOCOG ALFA | Dormant |
| 02435225 | ZONOVATE | TUROCTOCOG ALFA | Dormant |
| 02435233 | ZONOVATE | TUROCTOCOG ALFA | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

Note: the licence list also includes products carrying other brand names (OBIZUR, HUMATE-P, ELOCTATE, ADYNOVATE). These should be verified against Health Canada records to confirm which licences correspond to turoctocog alfa itself.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

One theoretical concern applies to the predicted indications: FVIII replacement in thrombotic thrombocytopenic purpura could worsen the prothrombotic state.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (evidence level L5). Platelet release disorders arise from platelet function defects, not FVIII deficiency, so the high TxGNN score appears to be a network-propagation artifact. Acquired coagulation factor deficiency is the only candidate with any plausibility, and it is better framed as a research question than a repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data for turoctocog alfa
- Package insert warnings and contraindications from Health Canada
- A mechanistic and clinical literature review for acquired FVIII deficiency, if it is pursued as a research question
- Verification of the ambiguous "flood factor deficiency" term against the source ontology
- Confirmation of which Canadian licences correspond to turoctocog alfa, with dosage form and indication text

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL2108286 (turoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2108286) |
| 2026-11-24 | Removed: "The remaining licences are under the same or related brand names." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

