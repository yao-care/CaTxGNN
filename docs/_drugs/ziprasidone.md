---
layout: default
title: Ziprasidone
parent: Model Prediction Only (L5)
nav_order: 994
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "ZIPRASIDONE"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
description: "Ziprasidone: predicted new indication Trichotillomania (evidence level L5). Approved use: Not recorded in the local data"
---

# Ziprasidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ziprasidone: Trichotillomania
{: .text-alpha }

## One-Sentence Summary

Ziprasidone is an atypical antipsychotic marketed in Canada. The TxGNN model predicts it may be effective for **trichotillomania**, but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 8) |
| Number of DINs | 8 (marketed: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, ziprasidone blocks dopamine D2 and serotonin 5-HT2A receptors. Both pathways are involved in repetitive and compulsive behaviours, which are central features of trichotillomania.

This link is plausible but unproven. No trial or publication in the compiled data studies ziprasidone in trichotillomania, so the mechanistic argument is a hypothesis, not a finding. The high model score should be read as a prompt for further investigation, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02298597 | ZELDOX |
| 02298619 | ZELDOX |
| 02449544 | AURO-ZIPRASIDONE |
| 02449552 | AURO-ZIPRASIDONE |
| 02449579 | AURO-ZIPRASIDONE |

Eight single-ingredient licences are currently valid, and none are cancelled. The table lists five of them.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Major-level interactions in the listed sample include hydrocortisone, amphotericin B (including the lipid complex form), bupropion and morphine. Several moderate interactions involve antidiabetic drugs (acarbose, metformin, pioglitazone, alogliptin, albiglutide) and anticholinergic agents (atropine, hyoscyamine, glycopyrronium).
- **Conditions flagged as cautions for ziprasidone** include long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, orthostatic hypotension, epilepsy, neutropenia, agranulocytosis, diabetes and diabetic ketoacidosis, liver failure and kidney disease. These come from a drug–disease relationship dataset, not from label text.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trichotillomania is supported only by a high model score. No trials or literature address this disease, so the evidence level is L5. The D2/5-HT2A mechanism is plausible but untested.

**To proceed, the following is needed:**
- Mechanism-of-action data for ziprasidone
- Package insert warnings and contraindications from Health Canada, including QTc-related cautions
- A literature search and, if warranted, preclinical or small exploratory clinical data in trichotillomania
- A comparison against existing treatment options for the condition before any clinical development decision

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

