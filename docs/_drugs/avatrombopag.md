---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Avatrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Avatrombopag: From Thrombocytopenia (TPO-RA) to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is a thrombopoietin receptor agonist (TPO-RA) known for treating thrombocytopenia (including immune thrombocytopenia and thrombocytopenia in chronic liver disease), although no formal approved indication data is on record in the current evidence pack.
The TxGNN model predicts it may have potential for **Macrothrombocytopenia with Mitral Valve Insufficiency** (rank 1 of 10 predicted indications), with a mechanistic rationale grounded in class-effect evidence from the related agent eltrombopag.
Currently, **0 clinical trials** and **0 publications** directly support this specific indication for avatrombopag, making this an L4 (preclinical/mechanism-level) signal only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not on record in evidence pack (known TPO-RA class: ITP, CLD-associated thrombocytopenia) |
| Predicted New Indication | Macrothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L4 (mechanism/class-effect reasoning only) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on the repurposing rationale embedded in the evidence pack, avatrombopag is a TPO receptor agonist (TPO-RA) that stimulates the thrombopoietin (TPO) signalling pathway to increase platelet production. Its efficacy in thrombocytopenic conditions has been demonstrated in approved settings, and mechanistically it may be applicable to other conditions where platelet counts are reduced.

Macrothrombocytopenia with mitral valve insufficiency is most commonly caused by hereditary skeletal-protein defects such as MYH9-related diseases (e.g., May-Hegglin anomaly, Fechtner syndrome). In these conditions, platelet numbers are reduced, which is where a TPO-RA could theoretically help — by stimulating the bone marrow to produce more platelets. However, the root structural defect in platelet morphology (enlarged, dysfunctional platelets) is not addressable by TPO-RA agents. The co-occurrence of mitral valve insufficiency further suggests a specific genetic syndrome where TPO signalling pathway integrity needs to be independently assessed before any therapeutic intervention.

The indirect support for this prediction comes from a class-effect observation: eltrombopag (another TPO-RA) has been reported in a small number of MYH9-related disease cases. Avatrombopag and eltrombopag share the same mechanistic class, making the class-effect extrapolation plausible but unconfirmed. The TxGNN model's high score (>0.9999) likely reflects this known TPO-RA class-disease node connection in the knowledge graph rather than drug-specific clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for avatrombopag in macrothrombocytopenia with mitral valve insufficiency.

---

## Literature Evidence

Currently no related literature available for avatrombopag in macrothrombocytopenia with mitral valve insufficiency.

---

## Canada Market Information

Avatrombopag has no approved licenses or DINs in Canada as of the data cutoff (2026-04-05). No market authorisation data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields — key warnings, contraindications, and drug–drug interactions — were returned as data gaps in the current evidence pack. Package insert review is required before any clinical consideration.)*

---

## Full Prediction Landscape

For transparency, all 10 TxGNN-predicted indications are summarised below, grouped by mechanistic plausibility:

### Group A — Thrombocytopenic Indications (Mechanistically Plausible, Research-Stage)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Note |
|------|---------|------------|----------------|----------------|-----------------|
| 1 | Macrothrombocytopenia with mitral valve insufficiency | 99.995% | L4 | Research Question | TPO-RA may raise platelet count; cannot correct structural defect. Class-effect from eltrombopag in MYH9-related disease. |
| 2 | Hereditary thrombocytopenia with normal platelets | 99.995% | L4 | Research Question | Normal platelet size excludes MYH9; transcription factor mutation subtypes (RUNX1, ANKRD26, ETV6) may respond to TPO-RA. Eltrombopag positive in ANKRD26-related cases. |
| 3 | Transient neonatal thrombocytopenia | 99.995% | L4 | Research Question | Mechanistically plausible (TPO-RA as rescue therapy in NAIT). Major safety concern: no pharmacokinetic/safety data in neonates for avatrombopag. |

### Group B — Platelet Function Disorder (Mechanism Mismatch — Hold)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Note |
|------|---------|------------|----------------|----------------|-----------------|
| 4 | Dense granule disease | 99.995% | L5 | Hold | Storage pool defect (ADP/serotonin deficiency); platelet count usually normal. TPO-RA addresses quantity, not granule function. Likely false positive. |

### Group C — Neurological Diseases (No Mechanistic Basis — Hold)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Note |
|------|---------|------------|----------------|----------------|-----------------|
| 5 | Amyotrophic lateral sclerosis | 99.993% | L5 | Hold | Motor neuron degeneration (TDP-43/FUS/SOD1); no connection to TPO/c-Mpl pathway. Cluster pattern suggests systematic KG bias. |
| 6 | Bilateral parasagittal parieto-occipital polymicrogyria | 99.992% | L5 | Hold | Rare cortical malformation (TUBB2B, LAMC3 mutations); platelet counts typically normal. KG noise output. |
| 7 | Lower motor neuron syndrome with late-adult onset | 99.992% | L5 | Hold | ALS-spectrum anterior horn cell degeneration; no relation to platelet synthesis pathway. |
| 8 | Amyotrophic lateral sclerosis, susceptibility to | 99.991% | L5 | Hold | Redundant with rank 5 ALS entry; same mechanistic mismatch. |
| 9 | Mills syndrome | 99.991% | L5 | Hold | ALS variant (corticospinal tract); part of the same neurodegeneration cluster. |
| 10 | Monomelic amyotrophy | 99.990% | L5 | Hold | Hirayama disease (cervical anterior horn); benign, self-limiting. No TPO pathway relevance. |

> ⚠️ **Model Bias Alert**: Ranks 5–10 (6 neurological diseases) all score >0.9999 with **zero** supporting clinical or literature evidence. This cluster pattern strongly suggests a systematic false-positive bias in TxGNN's neurodegeneration knowledge subgraph. A dedicated audit and recalibration of this subgraph is recommended.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the top three predictions (ranks 1–3) carry a plausible TPO-RA mechanistic rationale and are classified as L4 research-stage signals, there is currently **zero direct clinical or literature evidence** for avatrombopag in any of the predicted indications. The drug is not marketed in Canada, and safety data (warnings, contraindications, interactions) is entirely absent from the current evidence pack. The neurological disease cluster (ranks 5–10) appears to represent systematic model noise rather than genuine repurposing opportunity.

**To move from Hold to Research Question, the following is needed:**

- **Safety data (Blocking):** Retrieve the full prescribing information (package insert / SmPC) for avatrombopag (Doptelet®) — key warnings, contraindications, and drug–drug interaction profile must be assessed before any S1 safety screen can proceed.
- **MOA data (High Priority):** Confirm the complete mechanism of action via DrugBank API or primary literature to strengthen mechanistic-link analysis for the thrombocytopenic indications.
- **Class-effect literature review:** Systematically search PubMed for eltrombopag and romiplostim in MYH9-related disease, ANKRD26-related thrombocytopenia, and neonatal thrombocytopenia to establish indirect class-level evidence for ranks 1–3.
- **Neonatal safety assessment (Rank 3):** Before rank 3 (transient neonatal thrombocytopenia) can advance, a dedicated neonatal pharmacokinetic/safety assessment is required — avatrombopag has only been studied in adults.
- **TxGNN model audit:** Commission a targeted review of the neurodegeneration subgraph within the TxGNN knowledge graph to identify and correct the source of false-positive clustering across ranks 5–10.

---

> *This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

