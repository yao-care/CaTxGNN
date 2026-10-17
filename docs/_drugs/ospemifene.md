---
layout: default
title: Ospemifene
parent: Model Prediction Only (L5)
nav_order: 690
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ospemifene: predicted new indication Leprosy (evidence level L5). Approved use: Psychologic dyspareunia"
monitor_inn: "Ospemifene"
predicted_indications: ["leprosy", "pulmonary hypertension", "kyphoscoliotic heart disease", "migraine with or without aura, susceptibility to", "migraine disorder", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis", "rheumatoid arthritis", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Ospemifene
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

# Ospemifene: From Psychologic Dyspareunia to Leprosy

## One-Sentence Summary

Ospemifene is a selective estrogen receptor modulator (SERM), and its original indication in the knowledge graph is psychologic dyspareunia.
The TxGNN model predicts it may be effective for **leprosy**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychologic dyspareunia (from the knowledge graph; no approved indication text is available for the Canadian license) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, ospemifene is a SERM with tissue-specific estrogenic and anti-estrogenic activity. Its efficacy in its original indication is the basis for its marketing in Canada.

A possible link to leprosy, a mycobacterial infection with immune-mediated neuropathy, would be through immunomodulation. This link is speculative. No trials or publications support it, and the high score is a graph-based prediction only.

Other top predictions show the same pattern. These include pulmonary hypertension (98.95%), kyphoscoliotic heart disease (98.78%), several migraine entities (98.2–98.7%) and rheumatoid arthritis (97.43%). None has clinical or literature evidence, and all are also rated L5 and Hold. Some have only a conceivable estrogen-related rationale, such as pulmonary hypertension, migraine and rheumatoid arthritis. Others, such as nephrogenic syndrome of inappropriate antidiuresis and kyphoscoliotic heart disease, show no plausible mechanistic link.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02518112 | OSPHENA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 37 interactions were identified in total. The data compiled for this report list 20, of which 2 are rated Major and the rest Moderate.
  - **Major**: tranexamic acid, fluconazole.
  - **Moderate (examples)**: metformin, clarithromycin, erythromycin, ketoconazole, miconazole, cobicistat, ethinylestradiol, dapagliflozin, empagliflozin, eltrombopag, apalutamide.
- **Population-specific concern**: Ospemifene carries venous thromboembolism and stroke warnings. These matter particularly for cardiopulmonary populations (for example pulmonary hypertension) and for aura-associated migraine.

Please refer to the package insert for the full warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction is based only on a graph-based score, with no registered clinical trials, no publications and no established mechanistic link. Safety data from the Canadian label are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for any safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A literature and preclinical review of SERMs or estrogen signaling in leprosy and mycobacterial immune response
- A review of other top predictions, such as rheumatoid arthritis and pulmonary hypertension, in case any has stronger evidence
- A review of the 2 Major interactions (tranexamic acid, fluconazole) and the thromboembolic and stroke risk for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

