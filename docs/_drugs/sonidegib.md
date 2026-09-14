---
layout: default
title: Sonidegib
parent: 僅模型預測 (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: From Advanced Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

> Sonidegib is an oral Smoothened (SMO) receptor antagonist originally developed for **locally advanced basal cell carcinoma**, a cancer driven by aberrant Hedgehog pathway activation.
> TxGNN's top-ranked prediction suggests possible efficacy in **Medulloblastoma with Extensive Nodularity**, a Hedgehog-driven pediatric brain tumour subtype,
> but this specific pairing currently has **zero clinical trials and zero publications** — it is a pure model/mechanistic inference (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced basal cell carcinoma (laBCC) — inferred from supporting literature in this evidence pack; no structured license record exists for this market |
| Predicted New Indication | Medulloblastoma with Extensive Nodularity |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on supporting literature elsewhere in this evidence pack, sonidegib is an orally bioavailable, small-molecule Smoothened (SMO) receptor antagonist that blocks Hedgehog pathway signaling — its efficacy in advanced basal cell carcinoma, a cancer with near-universal Hedgehog pathway mutations, has been clinically established (see BOLT study evidence under the "skin cancer" candidate).

The SHH (Sonic Hedgehog) molecular subtype of medulloblastoma is likewise characterized by constitutive Hedgehog/SMO pathway activation, which gives the mechanistic rationale a degree of biological plausibility. However, this link is **theoretical only** — no clinical trial or published case has tested sonidegib specifically in medulloblastoma with extensive nodularity. Notably, the class-related SMO inhibitor vismodegib has shown concerning **growth-plate (bone) toxicity** when studied in pediatric medulloblastoma populations, a safety signal that would need direct evaluation before any sonidegib pediatric development could proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

This drug currently has **no approved product licenses in Canada** (0 DINs; market status: not marketed). No dosage form or indication record is available in this evidence pack.

---

## Cytotoxicity

*Sonidegib's original indication (advanced basal cell carcinoma) is antineoplastic, so this section is included.*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Smoothened/SMO receptor antagonist — Hedgehog pathway inhibitor, not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug–drug interaction data are all currently flagged as data gaps — TFDA/equivalent label retrieval is a Blocking-severity item that must be resolved before any S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction — medulloblastoma with extensive nodularity — has no clinical trial or literature support whatsoever; it rests entirely on TxGNN knowledge-graph embedding similarity (L5, decision stage S0). This is markedly weaker than the drug's already-established use in basal cell carcinoma (which appears further down this same prediction list, rank 6, backed by multiple completed Phase 2/3 RCTs including the pivotal BOLT trial) — a useful benchmark for how much evidence a "Go" recommendation would typically require. Given the known bone-toxicity signal for this drug class in pediatric brain tumour populations, proceeding without preclinical validation would be premature.

**To proceed, the following is needed:**
- Drug label / TFDA-equivalent warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank (currently High-severity data gap, DG002)
- Preclinical evidence of sonidegib activity specifically in SHH-subtype medulloblastoma models
- Pediatric safety data, particularly growth-plate/bone toxicity, given the precedent seen with vismodegib in this drug class
- Clarification of Canada regulatory pathway, since the drug is not currently marketed here (0 DINs)

*Note: Rank 2 (xeroderma pigmentosum) has one emerging 2026 case report and may warrant separate monitoring as evidence accumulates, despite currently being unclassified (pending).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

