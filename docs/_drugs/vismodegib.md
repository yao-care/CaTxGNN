---
layout: default
title: Vismodegib
parent: Model Prediction Only (L5)
nav_order: 828
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

> Vismodegib is a Hedgehog-pathway (Smoothened) inhibitor with established efficacy in advanced basal cell carcinoma (documented in this evidence pack's own literature, though not captured in the drug's regulatory record).
> The TxGNN model's top new prediction is **Medulloblastoma with Extensive Nodularity (MBEN)**, a pediatric SHH-subtype brain tumour,
> but this specific prediction currently has **zero clinical trials and zero publications** in the evidence pack — it is a pure model prediction (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic Basal Cell Carcinoma *(inferred from literature evidence in this pack for a related predicted entry; not present in the drug record — data gap)* |
| Predicted New Indication | Medulloblastoma with Extensive Nodularity (MBEN) |
| TxGNN Prediction Score | 99.93% (rank 1,808) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the drug record (data gap DG002). Based on the literature captured elsewhere in this same evidence pack (for the "skin cancer" entry, see below), vismodegib is a small-molecule antagonist of the Hedgehog (Hh) signaling pathway that binds Smoothened (SMO), blocking aberrant Hh activation. It was the first Hedgehog-pathway inhibitor approved for basal cell carcinoma, a tumour type driven by mutations in PTCH1, SMO, and SUFU.

Medulloblastoma with Extensive Nodularity (MBEN) is a subtype of medulloblastoma driven by the same SHH pathway (PTCH1/SMO/SUFU abnormalities), giving it a high degree of mechanistic overlap with vismodegib's known target. This is a biologically coherent extension of the drug's established mode of action from one Hh-driven tumour (BCC) to another (MBEN).

However, the evidence pack contains **no clinical trials or publications specific to vismodegib in MBEN or medulloblastoma**. The rationale is mechanism-only, and the pediatric population raises additional safety concerns not addressed here (e.g., growth-plate closure, long-term skeletal effects of Hh-pathway inhibition in children). This must be treated as a research hypothesis, not a treatment recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

Two lower-ranked predictions in this evidence pack carry substantially more mature evidence and may warrant separate, dedicated evaluation:

| Rank | Disease | TxGNN Score | Evidence Summary |
|------|---------|-------------|-------------------|
| 9 | Skin cancer (basal cell carcinoma) | 99.82% | 22 clinical trials incl. the pivotal Phase 2/3 ERIVANCE trial (Sekulic et al., NEJM 2012, PMID 22670903) and 20 publications. This is vismodegib's **already-approved** indication — the model is recovering known truth rather than proposing something new. |
| 2 | Xeroderma pigmentosum | 99.91% | 5 case reports/reviews, including documented off-label use of vismodegib for multiple BCCs in XP patients (e.g., PMID 30178564, 28297142). No registered clinical trials; evidence level L3–L4 at best. |

These findings suggest the model correctly re-identifies vismodegib's real-world use in Hh-driven skin tumours, which lends indirect credibility to its mechanistic reasoning for MBEN — but does not substitute for direct evidence in that indication.

---

## Canada Market Information

Vismodegib is **not currently marketed in Canada** — 0 DINs are on file, and no license records are available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / Smoothened inhibitor) — based on literature within this evidence pack |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (data gap — DG001) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (data gap — DG001) |
| Monitoring Items | Please refer to the package insert warnings and precautions (data gap — DG001) |
| Handling Protection | Please refer to the package insert warnings and precautions (data gap — DG001) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (MBEN) is supported by mechanism alone (L5, zero trials, zero publications), and the drug's own safety file is blocked at the most basic level — no TFDA/Health Canada label warnings or contraindications are available (DG001, Blocking severity), so a Stage 1 safety screen cannot even be initiated.

**To proceed, the following is needed:**
- Retrieve Health Canada product monograph / TFDA label for warnings, contraindications, and DDI (resolves DG001, Blocking)
- Confirm formal mechanism-of-action documentation via DrugBank API (resolves DG002, High)
- Targeted literature search for vismodegib in medulloblastoma/SHH-driven pediatric brain tumours (e.g., SJMB, PBTC trial series), which are not captured in this dataset
- Pediatric-specific safety assessment (growth-plate closure, bone development) given vismodegib's known adverse effect profile in children
- If pursued, evaluate the xeroderma pigmentosum and skin cancer (BCC) predictions in parallel — they carry materially stronger evidence and may represent nearer-term, lower-risk opportunities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

