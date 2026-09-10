---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Rivastigmine: From Alzheimer's Disease to Glaucoma

## One-Sentence Summary

> Rivastigmine is a dual acetylcholinesterase (AChE)/butyrylcholinesterase (BuChE) inhibitor traditionally used for Alzheimer's disease and dementia-related cognitive decline.
> The TxGNN model predicts it may be effective for **Glaucoma**,
> with **no registered clinical trials** and **3 supporting publications** currently available — evidence remains at the mechanistic/preclinical stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease / dementia (general pharmacological knowledge; not documented in the Canadian regulatory data provided — drug is not marketed) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap in this evidence pack). Based on the repurposing rationale provided, rivastigmine belongs to the cholinergic drug class as a dual AChE/BuChE inhibitor. Historically, related cholinergic agents (e.g., physostigmine, echothiophate, demecarium) have been used as miotic agents to lower intraocular pressure (IOP) — the proposed mechanism involves stimulating ciliary muscle contraction and increasing aqueous humor outflow through the trabecular meshwork.

A 2000 animal study directly demonstrated that topically applied rivastigmine lowers IOP in rabbits, and a 2024 systems-genetics/molecular review further supports a role for the cholinergic pathway in IOP regulation. However, this is largely a **class-effect inference** drawn from related cholinesterase inhibitors rather than direct clinical validation of rivastigmine itself in glaucoma patients. The mechanistic plausibility is moderate-to-high, but translational evidence in humans is still lacking.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Animal Study | J Ocul Pharmacol Ther | Topical rivastigmine lowered intraocular pressure in normotensive rabbits, providing direct (preclinical) evidence for an IOP-lowering effect |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review | Frontiers in Molecular Biosciences | Systems genetics and molecular modeling support a role for cholinergic/muscarinic signaling in IOP regulation via the trabecular meshwork |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opinion on Therapeutic Patents | Notes that mild AChE inhibition has recognized therapeutic relevance in Alzheimer's disease, myasthenia gravis, and glaucoma |

---

## Canada Market Information

Rivastigmine currently has **no Canadian market authorizations** recorded in this evidence pack (0 licenses, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: This evidence pack flags the absence of Health Canada label warnings/contraindications as a **Blocking** data gap (DG001), meaning a formal safety (S1) assessment cannot yet be completed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to preclinical/mechanistic data (Evidence Level L4, decision stage S0 — "Research Question") with no clinical trials in glaucoma, and the drug is not currently marketed in Canada. A Blocking data gap on Health Canada label warnings/contraindications also prevents a safety pre-assessment at this stage.

**To proceed, the following is needed:**
- Health Canada/TFDA label warnings and contraindications (resolve Blocking gap DG001)
- Confirmed mechanism of action data from DrugBank (resolve High-severity gap DG002)
- Route compatibility assessment — systemic rivastigmine (oral/transdermal) is not currently formulated for ocular/topical use; feasibility of a topical formulation needs evaluation
- Human clinical evidence (even early-phase) directly testing rivastigmine or class-related AChE inhibitors for IOP reduction in glaucoma patients
- Drug interaction data (current DDI query returned no results — status: not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

