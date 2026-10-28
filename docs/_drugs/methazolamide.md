---
layout: default
title: Methazolamide
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "METHAZOLAMIDE"
predicted_indications: ["congestive heart failure", "acute pulmonary heart disease"]
description: "Methazolamide: predicted new indication Congestive heart failure (evidence level L5). Approved use: Not recorded in the local data"
---

# Methazolamide
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

## Methazolamide: Congestive heart failure
{: .text-alpha }

## One-Sentence Summary

Methazolamide is a carbonic anhydrase inhibitor originally used to treat open-angle and angle-closure glaucoma.
The TxGNN model predicts it may be effective for **congestive heart failure**,
but currently there are **0 clinical trials** and **0 publications** specific to this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congestive heart failure |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, methazolamide is a carbonic anhydrase inhibitor. It lowers intraocular pressure (IOP) by reducing aqueous humour secretion, and its efficacy in open-angle and angle-closure glaucoma is established.

Primary hereditary glaucoma (for example, forms related to MYOC or CYP1B1) shares the same final pathway of elevated IOP. Mechanistically, lowering aqueous humour production could therefore be applicable.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not new biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245882 | METHAZOLAMIDE | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver failure, liver disease, kidney disease, renal tubular acidosis, hematologic disease, gallbladder disease, gout, respiratory failure, diabetes (type 1 and type 2), diabetic ketoacidosis, and adrenal insufficiency conditions (including Addison disease and congenital adrenal hyperplasia).
- **Drug Interactions**: 100 interactions were identified. Main examples:
  - **Major**: metformin, acetylsalicylic acid
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone), amphotericin B, antidiabetic agents (acarbose, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), and laxatives or bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol)
  - **Minor**: doxycycline

Package insert warnings were not available. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but the prediction is essentially an extension of the existing glaucoma indication. There are no trials or publications for the hereditary subtype, and the Canadian licence data lack indication text and package insert safety information.

**To proceed, the following is needed:**
- Mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Clinical or literature evidence specific to primary hereditary glaucoma
- Confirmation of whether the existing glaucoma indication already covers hereditary forms, since this may not be a new indication
- A review of the metabolic and renal contraindications and the large drug interaction burden for the intended patient population

---

### Other Predictions Noted

- **Congestive heart failure** (TxGNN score 0.9943, evidence level L4, research question only): there are no clinical trials. The supporting literature is historical diuretic reviews and preclinical studies, including a mouse model of diabetic cardiomyopathy and cardiomyocyte hypertrophy studies. Modern heart failure practice uses other diuretic classes, and the risks include metabolic acidosis and the large interaction burden.
- **Acute pulmonary heart disease** (TxGNN score 0.9928, evidence level L5, Hold): this is a model-only prediction with no trials or literature, and nothing in the available data supports a rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

