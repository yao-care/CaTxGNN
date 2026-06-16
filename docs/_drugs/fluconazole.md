---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 1
---

# Fluconazole
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

# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a triazole antifungal agent that works by blocking ergosterol biosynthesis in fungal cells, primarily used to treat systemic and superficial fungal infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
however there are currently **no clinical trials** and **no publications** supporting this specific direction — the prediction rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal infections (no Canadian DIN on file; based on known pharmacology) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis (PEK) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (no DIN registered) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluconazole is a triazole antifungal that inhibits fungal CYP51 (14α-lanosterol demethylase), blocking the biosynthesis of ergosterol — an essential component of the fungal cell membrane. By depleting ergosterol, fluconazole compromises membrane integrity and halts fungal replication. It is active against a broad range of *Candida* and *Cryptococcus* species, and is widely used systemically for candidiasis, cryptococcal meningitis, and dermatophyte infections.

The theoretical link to PEK is narrow but not entirely implausible: PEK can occasionally arise from fungal etiologies, such as early-stage *Candida* keratitis, where scattered punctate epithelial lesions may precede deeper stromal infiltration. In this narrow subset of cases, systemic or topical antifungal therapy targeting the causative organism could theoretically resolve the epithelial disruption.

However, this rationale has significant limitations. The overwhelming majority of PEK cases are non-fungal in origin — caused by adenoviral infection, dry eye disease, drug toxicity, or ultraviolet exposure. Furthermore, fluconazole is not the preferred agent for ocular surface fungal infections; voriconazole and natamycin have far better ocular penetration and established evidence in fungal keratitis. The TxGNN score of 99.24% reflects topological proximity in the knowledge graph, but with zero supporting clinical trials or literature, this prediction lacks the real-world corroboration needed to proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Canadian drug licenses (DINs) are currently registered for fluconazole in this dataset.

> **Note:** This may reflect a data pipeline gap. Fluconazole (e.g., Diflucan®) is generally available in many markets; please verify against the Health Canada Drug Product Database directly before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence linking fluconazole to punctate epithelial keratoconjunctivitis, and the mechanistic connection is limited to a narrow fungal-etiology subset of a condition that is predominantly non-fungal in practice. A high TxGNN score alone, at Evidence Level L5, is insufficient to justify advancement.

**To proceed, the following is needed:**

- Verification of Canadian regulatory status via the Health Canada Drug Product Database (DIN lookup for fluconazole / Diflucan®)
- Formal MOA documentation from DrugBank (DB00196) to complete the mechanism-of-action analysis
- A targeted literature search for fluconazole use in fungal keratitis or keratoconjunctivitis, which represents the only plausible mechanistic bridge
- Safety data retrieval (key warnings, contraindications, DDI profile) from the product monograph before any clinical feasibility discussion
- If any supporting case reports or small studies are identified in a supplementary search, upgrade evidence level and reassess
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

