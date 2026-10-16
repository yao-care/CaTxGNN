---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 796
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Ranolazine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the Canadian license records compiled for this report (…"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ranolazine is a drug marketed in Canada, and it is known to be used for chronic angina. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records compiled for this report (chronic angina is the commonly known use) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, ranolazine inhibits the late sodium current (INaL) and, to a lesser degree, the rapid delayed rectifier potassium current (IKr). Its efficacy in chronic angina is established.

NSIAD is a rare genetic disorder caused by gain-of-function mutations in the vasopressin V2 receptor gene (AVPR2). The receptor is constitutively active, which leads to unregulated water reabsorption in the kidney collecting duct. A direct link between ranolazine's sodium-channel activity and V2 receptor signalling has not been established. Any connection would be speculative, for example through indirect effects on renal ion transport or cAMP-mediated aquaporin-2 signalling.

The very high score (0.996) should be read with caution. It may reflect the structure of the knowledge graph rather than true biological relevance. Because NSIAD is rare, the chance of finding trial data is also low.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02510227 | CORZYNA | Not specified | Not specified |
| 02510219 | CORZYNA | Not specified | Not specified |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationship data, not from package insert text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, cirrhosis of liver.
- **Drug Interactions**: 100 interactions were identified. Examples are listed below.
  - **Major**: aprepitant, dexamethasone, clarithromycin, dolasetron, eliglustat
  - **Moderate**: famotidine, metformin, loperamide, bisacodyl, budesonide, canagliflozin, dapagliflozin, empagliflozin, and others
  - **Minor**: bupropion, lorcaserin, cimetidine

The kidney disease flag deserves particular attention, because the predicted indication is a renal water-handling disorder. The QT-related flags are consistent with ranolazine's known effect on cardiac repolarisation. Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no clinical trials or publications, the mechanistic link to V2 receptor-driven antidiuresis is speculative, and the knowledge graph flags kidney disease as a contraindication. The safety review also cannot proceed without the package insert data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank, to allow a proper mechanistic analysis
- Approved indication text and dosage forms for the two CORZYNA licenses
- Preclinical or mechanistic evidence linking late sodium current inhibition to AVPR2 or aquaporin-2 signalling
- A literature search for any case reports or small studies in NSIAD
- A review of renal safety and QT risk in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

