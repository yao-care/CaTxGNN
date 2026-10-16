---
layout: default
title: Abiraterone
parent: Model Prediction Only (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Abiraterone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Canadian license records compiled for this report (…"
monitor_inn: "Abiraterone"
predicted_indications: ["migraine disorder", "migraine with or without aura, susceptibility to", "migraine with brainstem aura", "leprosy", "pulmonary hypertension", "nephrogenic syndrome of inappropriate antidiuresis", "rheumatoid arthritis", "kyphoscoliotic heart disease", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Abiraterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone is an androgen-synthesis (CYP17A1) inhibitor marketed in Canada, and the Canadian license records compiled for this report do not list an approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only prediction (L5), and the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records compiled for this report (abiraterone is generally used in prostate cancer) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge, abiraterone inhibits CYP17A1, an enzyme needed for androgen and cortisol-precursor synthesis, which is the basis of its use in hormone-driven prostate cancer.

The link to migraine is weak. Sex-hormone fluctuation is implicated in migraine, so a connection through hormone modulation is conceivable, but this is speculative. No established mechanistic link has been identified. The high TxGNN score (0.988) is a computational output and is not backed by clinical trials or literature.

The other top predictions are also not clinically supported. Two are closely related migraine variants (migraine with or without aura susceptibility, and migraine with brainstem aura), likely knowledge-graph neighbors of the first prediction. The rest, such as leprosy, pulmonary hypertension, rheumatoid arthritis, and rare skin or genetic disorders, have no plausible mechanism or supporting evidence either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for migraine disorder.

---

## Canada Market Information

Nineteen valid single-ingredient licenses exist. The records compiled for this report do not include dosage form or approved-indication text. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02371065 | ZYTIGA | Not available | Not available |
| 02503999 | MAR-ABIRATERONE | Not available | Not available |
| 02501503 | PMS-ABIRATERONE | Not available | Not available |
| 02540452 | PRZ-ABIRATERONE | Not available | Not available |
| 02502305 | JAMP ABIRATERONE | Not available | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (CYP17A1 inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Examples among the first 20 listed:
  - **Major**: cisapride, dolasetron, eliglustat, loperamide
  - **Moderate**: bisacodyl, castor oil, clarithromycin, dexfenfluramine, eluxadoline, famotidine, fenfluramine, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide, metoclopramide
  - **Minor**: metronidazole
- **Other concerns**: In the pulmonary hypertension assessment, abiraterone's mineralocorticoid-excess effects (hypertension, fluid retention) were flagged as a safety concern rather than a benefit.

For warnings and contraindications, please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests only on a TxGNN computational score. There are no clinical trials or publications, and no established mechanistic link. Safety label data is also missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism-of-action data, for example from DrugBank
- Original approved-indication text from the Canadian licenses
- Preclinical or mechanistic evidence connecting CYP17A1 inhibition or sex-hormone modulation to migraine
- A literature and trial search specific to abiraterone and migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

