---
layout: default
title: Bismuth Subsalicylate
parent: Model Prediction Only (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
monitor_inn: "BISMUTH SUBSALICYLATE"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "salmonellosis", "typhoid fever", "conjunctivitis", "relapsing fever", "acute contagious conjunctivitis", "gingivitis", "punctate epithelial keratoconjunctivitis", "otitis externa"]
last_modified_at: 2026-10-28
description: "Bismuth Subsalicylate: predicted new indication Paratyphoid fever (evidence level L5). Approved use: Not recorded in the local data"
---

# Bismuth Subsalicylate
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

## Bismuth Subsalicylate: Antimicrobial and anti-secretory gastrointestinal agent → Paratyphoid fever
{: .text-alpha }

## One-Sentence Summary

Bismuth subsalicylate is a widely marketed gastrointestinal medicine with antimicrobial and anti-secretory activity.
The TxGNN model predicts it may be effective for **paratyphoid fever**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 14 of 14) |
| Number of DINs | 14 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on general knowledge, bismuth subsalicylate has antimicrobial and anti-secretory activity against enteric pathogens, including Salmonella. This makes the prediction biologically plausible, since paratyphoid fever is caused by Salmonella Paratyphi.

However, there are no trials or publications specific to paratyphoid fever. The high score most likely reflects the model's closeness to other Salmonella-related and diarrhoeal conditions rather than direct evidence. Paratyphoid fever is a systemic infection that normally requires antibiotics, and a luminal, minimally absorbed agent is unlikely to treat systemic disease on its own.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02313162 | Bismuth Subsalicylate Suspension | Not recorded | Not recorded |
| 02468646 | Regular Strength Bismuth | Not recorded | Not recorded |
| 02097079 | Pepto-Bismol | Not recorded | Not recorded |
| 02534436 | Gastrovol Liquid Gels | Not recorded | Not recorded |
| 02177994 | Pepto Bismol Caplet - 262 mg/Caplet | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 64 interactions were identified. Those listed are all moderate and include:
  - Tetracycline-class antibiotics (doxycycline, tetracycline, minocycline)
  - Morphine
  - Antidiabetic agents (insulins, glimepiride, glipizide, glyburide, chlorpropamide, repaglinide, nateglinide, tolazamide)
  - Fenfluramine

Please refer to the package insert for other safety information, including warnings and contraindications. The salicylate content of this product also warrants caution in some populations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for paratyphoid fever has a very high model score but no supporting trials or literature. The antibacterial mechanism is plausible, but a poorly absorbed gut-acting agent is unlikely to address a systemic infection that needs antibiotic therapy.

**To proceed, the following is needed:**
- Preclinical data on activity against Salmonella Paratyphi
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A clear rationale for how a minimally absorbed agent could affect systemic disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

