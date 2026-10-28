---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 975
evidence_level: L5
indication_count: 7
monitor_inn: "Vilazodone"
predicted_indications: ["neurotic disorder", "obsessive-compulsive disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "Keppen-Lubinsky syndrome", "Ohdo syndrome and variants", "schizotypal personality disorder"]
last_modified_at: 2026-10-28
description: "Vilazodone: predicted new indication Neurotic disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Vilazodone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Vilazodone: Neurotic disorder
{: .text-alpha }

## One-Sentence Summary

Vilazodone is an antidepressant, and it is marketed in Canada.
The TxGNN model predicts it may be effective for **neurotic disorder**, but there are currently **0 clinical trials** and **0 publications** that directly study this condition, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Neurotic disorder |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Number of approvals | 6 licences (all single-ingredient, all valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, vilazodone combines serotonin reuptake inhibition with 5-HT1A partial agonism. This profile is plausibly relevant to the anxiety and depressive symptoms seen in neurotic disorders.

Neurotic disorder is a broad category that overlaps heavily with anxiety disorder, so the prediction is mechanistically understandable. For the same reason, it adds little as a new repurposing target. The high score (0.9975) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No supporting trials or literature are cited.

Other predictions in the list are weaker or less relevant:
- **Obsessive-compulsive disorder** (score 0.9972): serotonergic drugs are an established treatment class, but the three publications found are class-level reviews, and none was confirmed to report vilazodone data. This is a research question, not evidence of efficacy.
- **Agoraphobia** (0.9968): a serotonergic rationale exists, but there is no study evidence.
- **Schizotypal personality disorder** (0.9951): some affective overlap, but SSRI monotherapy is not an established treatment.
- **Benign paroxysmal torticollis of infancy, Keppen-Lubinsky syndrome, Ohdo syndrome and variants**: no plausible mechanistic link is evident. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for neurotic disorder.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02551810 | APO-VILAZODONE | Not listed | Not listed |
| 02443732 | VIIBRYD | Not listed | Not listed |
| 02443740 | VIIBRYD | Not listed | Not listed |
| 02551837 | APO-VILAZODONE | Not listed | Not listed |
| 02551829 | APO-VILAZODONE | Not listed | Not listed |

One more valid licence (DIN 02443724, VIIBRYD) is also on record, for six in total.

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (these are graph relations, not label text): epilepsy, bipolar disorder, major affective disorder, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, serotonin syndrome.
- **Drug Interactions**: 100 interactions were found in total. Examples of **Major** interactions include bupropion, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron and phentermine. Examples of **Moderate** interactions include acetylsalicylic acid, morphine, dexamethasone, aprepitant, pioglitazone, glimepiride, chlorpropamide and several insulins. Several of these are consistent with serotonergic, QT or bleeding concerns.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. No trial or publication directly studies vilazodone in neurotic disorder, so the evidence level is L5. The category also overlaps with anxiety disorder, which is already recorded for this drug.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently missing, and blocking for safety screening)
- Mechanism of action data from DrugBank
- A clearer definition of neurotic disorder and of how it differs from the recorded anxiety disorder indication
- A targeted literature and trial search for vilazodone in anxiety-spectrum conditions, especially obsessive-compulsive disorder, which is the most mechanistically plausible secondary candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

