---
layout: default
title: Benzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Benzyl Alcohol: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
monitor_inn: "BENZYL ALCOHOL"
predicted_indications: ["bronchitis"]
---

# Benzyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Benzyl Alcohol: From Dermatitis to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Benzyl alcohol was originally associated with dermatitis treatment and is currently marketed in Canada in topical pain-relief products.
The TxGNN model predicts it may be effective for **bronchitis**, but there are **no registered clinical trials** and only **2 publications**, neither of which supports a therapeutic benefit.
The one clinical report available actually describes bronchitis as an adverse effect of inhaled benzyl alcohol.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benzyl alcohol is known as an antimicrobial and bacteriostatic preservative and a mild local anaesthetic, and it has been used in topical products. Mechanistically, antimicrobial properties could plausibly be relevant to respiratory infection, but this is speculative.

The link between dermatitis and bronchitis is weak. Both involve inflammation, but they affect different organ systems, and no evidence supports a shared mechanism for this drug. The prediction rests almost entirely on the model's high score.

The available literature points in the opposite direction. A report on nebulized bacteriostatic saline, which is preserved with benzyl alcohol, found it to be a possible irritant to the airway lining and a cause of bronchitis. Inhaled exposure is therefore a potential safety signal rather than a therapeutic one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Case report/series | The Journal of Family Practice | Examined whether nebulized bacteriostatic saline (preserved with benzyl alcohol) irritates the airway lining in healthy adults; reported bronchitis as an adverse event. |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | In vitro / plant extract study | Heliyon | Evaluated Senna tora leaf extracts for antioxidant, anti-inflammatory and antibacterial activity. Does not assess benzyl alcohol as a treatment. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02511428 | SALONPAS PAIN RELIEVING SOLUTION | Not specified | Not specified |
| 02511339 | SALONPAS PAIN RELIEVING CREAM | Not specified | Not specified |

---

## Safety Considerations

- **Disease-related cautions (from knowledge graph contraindication links, not label text):** the data compiled for this report link benzyl alcohol to possible contraindication in the following conditions:
  - Cardiovascular: hypertension, coronary artery disease, coronary atherosclerosis, arteriosclerosis, atherosclerosis
  - Respiratory: chronic obstructive pulmonary disease (including severe early-onset COPD)
  - Gastrointestinal: peptic ulcer disease
  - Skin: contact dermatitis, occupational dermatitis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Genitourinary: benign prostatic hyperplasia, bladder neck obstruction
  - Eye: angle-closure glaucoma
- **Respiratory exposure:** published reports describe bronchitis after inhalation of benzyl alcohol-preserved nebulized saline.

No drug interaction data were found. Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no registered trials, and the only relevant publication suggests that inhaled benzyl alcohol may cause bronchitis rather than treat it. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Mechanism of action data for benzyl alcohol
- Package insert warnings and contraindications from Health Canada
- Evidence of therapeutic benefit in bronchitis (preclinical or clinical), and a resolution of the inhalation safety signal
- Assessment of route compatibility, since current Canadian products are topical and bronchitis would likely require a different route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

