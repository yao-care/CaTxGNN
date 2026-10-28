---
layout: default
title: Verteporfin
parent: Model Prediction Only (L5)
nav_order: 973
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Verteporfin: predicted new indication mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies (evidence level L5). Approved use: Macular degeneration"
monitor_inn: "VERTEPORFIN"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
---

# Verteporfin
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

## Verteporfin: From Macular Degeneration to Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies
{: .text-alpha }

## One-Sentence Summary

Verteporfin is a light-activated drug (photosensitizer) originally used to treat macular degeneration.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but **no clinical trials and no publications** currently support this direction, so the prediction is a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, verteporfin is a photosensitizer activated by non-thermal red light. Once activated, it generates reactive oxygen species and causes local blockage of blood vessels, which is how it treats abnormal vessel growth in macular degeneration.

The link to the predicted indication comes only from the TxGNN model (deep learning), with a score of 0.9949. The score may reflect similarities the model learned between related diseases, not biological evidence. Nothing in the compiled data connects verteporfin's action to disorders of mitochondrial energy production caused by nuclear DNA defects. Preclinical work outside the compiled data suggests verteporfin may inhibit YAP-TEAD signaling, but no evidence here ties this to the predicted disease.

There is also a reason for caution. Verteporfin's light-triggered production of reactive oxygen species could plausibly be harmful in mitochondrial disease, where oxidative stress is already a concern. The high score should be treated as a hypothesis, not as support for repurposing.

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
| 02242367 | VISUDYNE | Not specified | Not specified |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: inherited porphyria, porphyrin metabolism disease, porphyria, liver disease, gallbladder disease.
- **Drug Interactions**: 100 interactions were identified in the interaction screening. The sample reviewed includes mostly Moderate-level and one Minor-level interactions. Main examples:
  - Tetracycline-class antibiotics: doxycycline, tetracycline, minocycline (including topical forms)
  - Sulfonylurea antidiabetic drugs: chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, acetohexamide
  - Others: acetylsalicylic acid, levofloxacin, mannitol, sulfasalazine, beta carotene, papaverine
  - Minor: polymyxin B

  Many of these agents are likely relevant because of additive photosensitivity, but the compiled data does not state the mechanism.

Please refer to the Health Canada package insert for official warnings and contraindications, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature, and no mechanism data linking verteporfin to this disease. Its ROS-generating, light-activated action also raises a plausible safety concern in mitochondrial disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic-link analysis
- Preclinical evidence on whether verteporfin has any beneficial or harmful effect in models of nuclear-DNA-driven oxidative phosphorylation disorders
- A route and administration compatibility assessment, since verteporfin requires intravenous infusion followed by light activation in the eye
- A safety review of oxidative stress risk in mitochondrial disease, and of the porphyria and liver or gallbladder disease contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

