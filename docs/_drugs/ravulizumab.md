---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From PNH/aHUS to Autosomal Recessive Severe Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

> Ravulizumab is a complement C5 inhibitor whose approved use, per the evidence pack's own mechanistic notes, covers PNH (paroxysmal nocturnal hemoglobinuria) and aHUS (atypical hemolytic uremic syndrome) — complement-driven, thrombotic microangiopathy-related conditions.
> The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, with a prediction score of **99.96%**,
> but **zero clinical trials and zero publications** currently support this direction, and the model's own rationale explicitly flags no direct mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this pack (licenses list is empty); mechanistic notes reference PNH and aHUS as approved, complement/TMA-related indications |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ravulizumab is flagged as a data gap in this pack (DG002). Based on the information available in the evidence pack's own repurposing rationale, ravulizumab is an anti-complement C5 monoclonal antibody that blocks formation of the C5b-9 membrane attack complex (MAC), consistent with its known approved use in PNH and aHUS — both complement/thrombotic microangiopathy (TMA)-related diseases.

G6PC3-deficient severe congenital neutropenia, however, is a metabolic-developmental disorder driven by endoplasmic reticulum stress, increased neutrophil apoptosis, and abnormal glucose metabolism. The evidence pack's own rationale states there is **no direct mechanistic relationship** between this pathway and C5-mediated terminal complement inhibition. The high TxGNN score is attributed to embedding similarity among neutropenia/rare hematologic disease nodes in the knowledge graph, rather than to any causal or pharmacological connection.

In short, this is a graph-similarity-driven signal rather than a mechanistically grounded hypothesis. All nine other candidates in this pack carry the same caveat — none show a direct pathway overlap with C5 inhibition, and none are supported by trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ravulizumab has **0 licensed products** on record in this dataset and is marked **Not Marketed** in Canada. No DIN-level product or indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/label-level warnings and contraindications are flagged in this pack as a **Blocking** data gap — see "To proceed" below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on a TxGNN similarity score with no clinical trials, no literature, and no marketed presence in Canada. The evidence pack's own mechanistic rationale explicitly states there is no direct pathway link between complement C5 inhibition and G6PC3-related neutropenia, so the prediction should be treated as a graph-embedding signal rather than a testable hypothesis at this stage.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (DG001, blocking — required before any safety pre-screen)
- Verified mechanism of action data from DrugBank or primary labeling (DG002)
- Preclinical or mechanistic studies establishing any plausible link between complement inhibition and G6PC3-deficient neutropenia
- At minimum, case-level or observational evidence before moving this candidate beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

