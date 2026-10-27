---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Obstructive airway disease"
monitor_inn: "INDACATEROL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: From Obstructive Airway Disease (COPD/Asthma) to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an inhaled, once-daily, ultra-long-acting beta2-agonist (ultra-LABA), used as a bronchodilator for obstructive airway disease.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)** with a very high score,
but **no clinical trials and no publications** support this prediction, so it remains a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obstructive airway disease (COPD and asthma, based on the published literature; the Health Canada licence records compiled for this report contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Indacaterol is a beta2-adrenergic agonist. It relaxes bronchial smooth muscle by activating beta2-receptors and raising intracellular cAMP. Detailed mechanism-of-action data were not available in the drug database records compiled for this report, so this description relies on the drug class and the published literature.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2), which also signals through cAMP. This shared second messenger is the only visible link the model may be picking up on. It is not a therapeutic rationale: boosting cAMP signalling would, in theory, increase rather than reduce water-retention signalling. The very high score is therefore not supported by any mechanistic or clinical evidence, and it likely reflects class-level or network associations in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|------|
| 02498685 | ATECTURA BREEZHALER | Valid |
| 02498707 | ATECTURA BREEZHALER | Valid |
| 02498693 | ATECTURA BREEZHALER | Valid |
| 02418282 | ULTIBRO BREEZHALER | Valid |
| 02501244 | ENERZAIR BREEZHALER | Valid |

All five authorisations are currently valid, and none are cancelled. Dosage form, manufacturer and approved indication text were not available in the records compiled for this report.

## Safety Considerations

- **Disease associations from the knowledge graph** (these come from model-derived drug-disease contraindication links, not from label text): hypertension and hypertensive disorder, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, coronary artery disease, epilepsy, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, and thyrotoxicosis, hyperthyroidism and Graves disease.
- **Drug interactions:** 100 interactions were identified. The ones reviewed include:
  - *Moderate:* epinephrine, isometheptene, clarithromycin, famotidine, and several antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, albiglutide, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide).
  - *Minor:* corticosteroids (hydrocortisone, dexamethasone, triamcinolone, beclomethasone, betamethasone, budesonide) and aprepitant.

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications. The mechanistic link is unfavourable, because beta2-agonism acting through cAMP could in theory worsen the cAMP-driven water retention in NSIAD. The same applies to the other nine top-ranked predictions: none has clinical evidence. One of them, bronchial disease (rank 7), has substantial Phase 3 support, but it largely restates the drug's existing marketed use rather than representing new repurposing.

**To proceed, the following is needed:**
- A plausible pharmacological rationale, for example preclinical work in AVPR2 gain-of-function models.
- Any clinical or case-level evidence in NSIAD.
- The Health Canada package insert, to complete the label-based warnings and contraindications.
- A safety assessment for the cardiovascular, metabolic and electrolyte risks noted above, especially in the population affected by NSIAD.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

