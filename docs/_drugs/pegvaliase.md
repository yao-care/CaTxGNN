---
layout: default
title: Pegvaliase
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Pegvaliase: predicted new indication Diabetic retinopathy (evidence level L5). Approved use: Not listed in the Canadian license data (generally phenylketonuria)"
monitor_inn: "Pegvaliase"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract"]
---

# Pegvaliase
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

## Pegvaliase: From Phenylketonuria to Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia lyase enzyme that breaks down phenylalanine. It is marketed in Canada as PALYNZIQ, and its original indication is not listed in the data compiled for this report (it is generally used for phenylketonuria).
The TxGNN model predicts it may be effective for **diabetic retinopathy**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data (generally phenylketonuria) |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 0.9917 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for pegvaliase: "Pegvaliase-pqpz is a PEGylated phenylalanine ammonia lyase (PAL) enzyme that converts phenylalanine to ammonia and trans -cinnamic acid. It substitutes for the deficient phenylalanine hydroxylase (PAH) enzyme activity in patients with PKU and reduces blood phenylalanine concentrations." ([DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c), label version 2026-03-02; accessed 2026-11-19.) Based on known information, pegvaliase is a PEGylated phenylalanine ammonia lyase that degrades phenylalanine, and it is marketed for phenylketonuria.

No established mechanistic link has been identified between phenylalanine depletion and diabetic retinal microvascular disease. The high TxGNN score is a TxGNN model (deep learning) prediction only, and the data compiled for this report do not support a biological pathway connecting the two.

The other top predictions are severe nonproliferative diabetic retinopathy (0.9916) and diabetic cataract (0.9911). These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related eye diseases, not biological evidence specific to this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02526247 | PALYNZIQ | PEGVALIASE | Marketed |
| 02526255 | PALYNZIQ | PEGVALIASE | Marketed |
| 02526263 | PALYNZIQ | PEGVALIASE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: 16 interactions were identified, all rated Moderate. They mainly involve other PEGylated or pegylated-class products and a few other drugs:
- PEGylated products: certolizumab pegol, pegaptanib (ophthalmic), pegloticase, pegademase, pegaspargase, pegfilgrastim, peginesatide, peginterferon alfa-2a, peginterferon alfa-2b, peginterferon beta-1a, pegvisomant, liposomal doxorubicin
- Coagulation factors: recombinant antihemophilic factor, human coagulation factor IX
- Others: medroxyprogesterone acetate, naloxegol

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, no supported mechanistic link to diabetic retinopathy, and the safety data from the label are incomplete.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale connecting phenylalanine depletion to retinal or lens disease
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Original approved indication, dosage form and manufacturer details for the three DINs
- Preclinical or literature evidence in diabetic retinopathy models
- Assessment of route compatibility (injectable enzyme therapy versus the routes typically used for eye disease)
- Review of the moderate interactions, particularly with other PEGylated products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

