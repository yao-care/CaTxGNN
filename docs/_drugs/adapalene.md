---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# Adapalene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model alone and has no biological or clinical support in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (from the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, adapalene is a topical retinoid that selectively binds retinoic acid receptors (RAR-beta and RAR-gamma). It modulates keratinocyte differentiation and inflammation, which explains its use in acne.

**The prediction is not well supported mechanistically.** Elevated plasma zinc (hyperzincemia) is a biochemical state. It is typically caused by excess zinc intake, certain genetic variants, or altered zinc-binding protein levels. No known pathway connects RAR signalling to systemic zinc homeostasis in a way that would support therapeutic use.

The very high TxGNN score (99.51%) is a knowledge-graph prediction. It likely reflects network proximity, such as shared zinc-related or retinoid-related gene or protein associations, rather than biological or clinical validity. Adapalene is also applied topically with low systemic absorption, so effects on plasma zinc are improbable. Elevated plasma zinc is also a laboratory finding rather than a typical treatment target, which further weakens the rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02148749 | DIFFERIN | Not specified | Not specified |
| 02274000 | DIFFERIN XP | Not specified | Not specified |
| 02231592 | DIFFERIN | Not specified | Not specified |
| 02517205 | SANDOZ ADAPALENE / BENZOYL PEROXIDE FORTE | Not specified | Not specified |
| 02456923 | TARO-ADAPALENE/BENZOYL PEROXIDE | Not specified | Not specified |

A total of 10 valid single-ingredient licences are listed; the table shows the first 5.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the TxGNN knowledge graph, not from product label text): photoparoxysmal response, photosensitivity disease, exfoliative dermatitis, and dermatitis.
- **Drug Interactions**: The interaction screen returned 58 records, all with an unclassified severity level. Examples include doxycycline, minocycline, tetracycline, metronidazole, prednisone, triamcinolone, budesonide, clopidogrel, bupropion, ibuprofen, fluconazole, and several proton pump inhibitors (omeprazole, pantoprazole, rabeprazole). Clinical significance has not been graded, so these should be reviewed before any use.

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and no plausible mechanistic link exists between retinoid receptor signalling and plasma zinc levels. Low systemic absorption after topical use makes a systemic effect on zinc even less likely. The high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A credible biological hypothesis linking RAR signalling to zinc homeostasis, plus any supporting preclinical or observational data
- Clarification of whether elevated plasma zinc is a meaningful treatment target, given that it is a laboratory finding
- Assessment of route compatibility between topical adapalene and a systemic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

