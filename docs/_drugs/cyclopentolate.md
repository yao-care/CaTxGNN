---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 231
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Cyclopentolate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Cycloplegia"
monitor_inn: "Cyclopentolate"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
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

# Cyclopentolate: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a topical anticholinergic eye medication, originally used to produce cycloplegia (temporary paralysis of the eye's focusing muscle).
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score and class-level reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

Two other predictions were also generated: obsolete neurogenic bladder (99.40%) and irritable bowel syndrome (99.27%). Both are also L5 and Hold.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyclopentolate is a topical muscarinic antagonist (anticholinergic) used for cycloplegia and mydriasis. Its efficacy in the eye is established, and mechanistically the same receptor blockade may be applicable to conditions where muscarinic signalling drives symptoms.

The proposed link to cauda equina syndrome is through neurogenic bladder dysfunction, a major feature of the condition. Antimuscarinic agents reduce detrusor overactivity and are used for neurogenic bladder. However, the primary treatment for cauda equina syndrome is urgent surgical decompression, so any drug role would be limited to symptom management. Cyclopentolate is formulated as an ophthalmic solution with no established systemic use for this purpose, and the mechanism is inferred rather than demonstrated.

The related predictions follow the same class-level logic:
- **Neurogenic bladder:** Antimuscarinics such as oxybutynin and tolterodine are standard therapy, so the mechanism is plausible. However, better-characterized, bladder-selective alternatives exist. The disease term is also flagged as obsolete in the ontology, which weakens interpretability.
- **Irritable bowel syndrome:** Antispasmodics such as dicyclomine and hyoscyamine are used for cramping. Cyclopentolate has no GI-targeted pharmacokinetic data, and systemic anticholinergic effects (dry mouth, constipation, CNS effects) limit feasibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00626627 | ODAN-CYCLOPENTOLATE | Not specified | Not specified |
| 02148382 | MINIMS CYCLOPENTOLATE HYDROCHLORIDE | Not specified | Not specified |
| 00252506 | CYCLOGYL | Not specified | Not specified |

All three authorizations are valid single-ingredient products. None are cancelled.

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text):** The knowledge graph links cyclopentolate to contraindication with the following conditions:
  - **Cardiovascular:** hypertension, heart disease, cardiovascular disease, coronary artery disease, sudden cardiac arrest, heart conduction disease, arteriosclerosis, atherosclerosis
  - **Metabolic/endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - **Eye:** angle-closure glaucoma, closed-angle glaucoma
  - **Urological:** benign prostatic hyperplasia
  - **Neurological:** brain injury, brain disease, Down syndrome
- **Systemic anticholinergic risk:** Rationale notes on the predictions mention CNS-penetrant toxicity (e.g., psychosis, ataxia, seizures) and effects such as dry mouth and constipation. These would matter if systemic use were considered.
- **Drug interactions:** No interaction records were found in the data compiled for this report.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predictions are supported only by the model score and class-level mechanistic reasoning, with no clinical trials or publications. Cyclopentolate is an ophthalmic agent with no established systemic use, and better-characterized antimuscarinic alternatives already exist for neurogenic bladder and IBS. The knowledge graph also flags several relevant contraindications, including benign prostatic hyperplasia and cardiovascular disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (e.g., from DrugBank)
- Preclinical or pharmacokinetic evidence on systemic exposure and feasibility of a non-ophthalmic route
- Comparative rationale against established antimuscarinics for the predicted indications
- Route compatibility assessment, since no available or required routes have been defined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

