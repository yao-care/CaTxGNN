---
layout: default
title: Desvenlafaxine
parent: Moderate Evidence (L3-L4)
nav_order: 267
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-28
description: "Desvenlafaxine: predicted new indication Obsessive-compulsive disorder (evidence level L4). Approved use: Unipolar depression, major depressive disorder, anxiety disorder"
monitor_inn: "DESVENLAFAXINE"
predicted_indications: ["obsessive-compulsive disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "schizoid personality disorder", "schizotypal personality disorder", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Desvenlafaxine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

## Desvenlafaxine: From Depression to Obsessive-Compulsive Disorder
{: .text-alpha }

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally used to treat depressive disorders (unipolar depression, major depressive disorder) and anxiety disorder.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**, but **no clinical trials** and only **3 publications** (none testing desvenlafaxine directly in OCD) are available, so the evidence is limited to the model prediction and general class-level literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, major depressive disorder, anxiety disorder (the Canadian licence records contain no indication text) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses: 20 of 20) |
| Number of DINs | 20 (valid: 20) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, desvenlafaxine is an SNRI. Its efficacy in major depressive disorder is established, and mechanistically it may be applicable to OCD.

Serotonergic reuptake inhibition is the established pharmacological basis for OCD treatment (SSRIs, clomipramine), so a plausible mechanistic link exists. A 2014 review of double-blind studies supports the central role of the serotonin system in OCD.

There are important caveats. Desvenlafaxine's serotonergic selectivity is weaker than that of SSRIs, and the retrieved literature contains no direct efficacy data for desvenlafaxine in OCD. The high score should therefore be read as a hypothesis, not as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for OCD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Updated review of double-blind studies of serotonergic antidepressants in OCD; supports the role of the 5-HT system (not desvenlafaxine-specific) |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression; mentions later OCD and anxiety as long-term consequences (indirect relevance) |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical study | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder (not OCD) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02321092 | PRISTIQ | Not listed | Not listed |
| 02321106 | PRISTIQ | Not listed | Not listed |
| 02458217 | TEVA-DESVENLAFAXINE | Not listed | Not listed |
| 02466988 | APO-DESVENLAFAXINE | Not listed | Not listed |
| 02495147 | JAMP DESVENLAFAXINE | Not listed | Not listed |

These are 5 of 20 valid single-ingredient licences. The others are generic products from Apotex, AG, Taro, Sandoz, Teva, JAMP and other labels.

---

## Safety Considerations

- **Disease-related cautions (TxGNN model signals, not label text)**: The TxGNN model (deep learning) links desvenlafaxine to caution or contraindication in the following conditions. These signals may reflect similarities the model learned between related diseases, not biological evidence:
  - Cardiovascular: hypertension, cardiovascular disease, heart disease, cerebrovascular disorder
  - Neurological and psychiatric: epilepsy, bipolar disorder / major affective disorder, serotonin syndrome, neuroleptic malignant syndrome
  - Organ function and bleeding: liver disease, impaired renal function, gallbladder disease, blood coagulation disease
  - Eye: angle-closure glaucoma, ocular hypertension
  - Metabolic, electrolyte and lung: hypertriglyceridemia, inappropriate ADH syndrome (including nephrogenic form), interstitial lung disease
- **Drug Interactions**: 100 interactions were identified; the first 20 retrieved are summarised here.
  - **Major**: bupropion, lorcaserin, dexfenfluramine, fenfluramine, diethylpropion, mazindol, dolasetron, granisetron. Many involve additive serotonergic or sympathomimetic effects.
  - **Moderate**: epinephrine (including ophthalmic and topical), ephedrine (including nasal), morphine, acetylsalicylic acid (bleeding risk), dronabinol, mannitol, picosulfuric acid, polyethylene glycol with electrolytes.
  - **Minor**: cimetidine.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The OCD prediction rests on a model score and a class-level serotonergic rationale. No trials or desvenlafaxine-specific studies exist, and an SNRI with weaker serotonergic selectivity than SSRIs is not a clear fit for OCD.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and serotonin transporter selectivity analysis
- Preclinical or pilot clinical data of desvenlafaxine in OCD, ideally compared with SSRIs
- Health Canada package insert warnings and contraindications, plus approved indication text for the licences
- A safety review for patients with hypertension, cardiovascular disease, bipolar disorder, and those taking serotonergic drugs

### Other Predicted Indications Worth Noting

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Agoraphobia | 0.9970 | L5 | Class-level rationale only; no desvenlafaxine data. |
| Personality disorder cluster (histrionic, paranoid, schizoid, schizotypal) | 0.9984 | L5 | Identical scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Ohdo syndrome; benign paroxysmal torticollis of infancy | 0.9974; 0.9974 | L5 | No plausible mechanism; likely model artifacts. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

