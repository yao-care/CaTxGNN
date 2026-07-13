---
layout: default
title: Ganirelix
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Ganirelix
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

# Ganirelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Ganirelix is a synthetic GnRH (gonadotropin-releasing hormone) antagonist, originally used to prevent premature LH surges during controlled ovarian hyperstimulation in assisted reproductive technology (ART/IVF).
The TxGNN model predicts it may be effective for **Hypertrichosis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
All 10 predicted indications score at evidence level **L5** (model prediction only), with no empirical clinical support captured in this dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of premature LH surges during controlled ovarian hyperstimulation (ART/IVF) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, ganirelix is a competitive GnRH receptor antagonist — it binds to pituitary GnRH receptors and blocks the action of endogenous GnRH, thereby rapidly suppressing LH and FSH secretion without an initial hormonal "flare." By lowering circulating LH, ganirelix indirectly reduces gonadal androgen (testosterone) production. Its clinical efficacy in preventing premature ovulation during controlled ovarian stimulation is well established.

There is a narrow theoretical rationale for androgen-dependent **hirsutism** (male-pattern excess terminal hair in androgen-sensitive areas in women): suppressing LH → reducing testosterone → dampening androgen-driven hair follicle stimulation. However, the TxGNN top prediction is **hypertrichosis**, not hirsutism — and this distinction is clinically decisive.

Hypertrichosis is, by definition, **non-androgen-dependent** abnormal hair growth. It arises from genetic mutations, drug exposure (e.g., cyclosporine, minoxidil), or metabolic disturbances — none of which involve the HPG (hypothalamic-pituitary-gonadal) axis that ganirelix targets. The mechanistic link between GnRH antagonism and hypertrichosis is therefore extremely weak.

Reviewing the full top-10 prediction set reveals a consistent pattern: hair and skin disorders (ranks 1, 2, 5, 10), rare structural genetic syndromes (ranks 3, 4, 7), and HPG-axis disorders (ranks 6, 8, 9). The cluster of hair-related conditions at the top of the list most likely reflects **knowledge graph proximity** between adjacent disease nodes (hypertrichosis ↔ hirsutism ↔ hair shaft disorders) rather than genuine pharmacological plausibility. The two most biologically grounded predictions — aromatase excess syndrome (rank 8) and central precocious puberty (rank 9) — are the only indications classified as Research Questions (S1) with a coherent mechanistic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ganirelix and hypertrichosis.

---

## Literature Evidence

Currently no related literature available for ganirelix and hypertrichosis.

> **Note on rank 3 (malformation syndrome with odontal/periodontal component):** The PubMed query returned 20 results, but review confirmed all are general periodontology papers (treatment guidelines, diabetes–periodontal relationships, microbiology studies) with no connection to ganirelix. This constitutes a false-positive signal from keyword co-occurrence; no evidence for this repurposing direction exists.

---

## Canada Market Information

Ganirelix is not currently marketed in Canada. No DINs are registered in the Health Canada database.

| DIN | Product Name | Dosage Form | Approved Indication |
|-----|-------------|-------------|---------------------|
| — | Not marketed in Canada | — | — |

For reference, ganirelix is available internationally under the brand name **Orgalutran** (Organon) in the EU, Australia, and other markets, indicated for the prevention of premature LH surges in women undergoing controlled ovarian hyperstimulation for ART. The US formulation (Antagon, Merck) has been discontinued.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for ganirelix in hypertrichosis lacks mechanistic support — hypertrichosis is non-androgen-dependent, placing it entirely outside the scope of GnRH receptor antagonism. The high model score (99.98%) reflects knowledge graph clustering of hair-related disease nodes, not pharmacological plausibility. With zero supporting clinical trials and zero relevant publications, there is no basis to advance this specific repurposing hypothesis.

**Two higher-priority targets identified within this prediction set:**

| Rank | Indication | Stage | Mechanistic Pathway |
|------|-----------|-------|---------------------|
| 8 | Aromatase excess syndrome (AEXS) | S1 – Research Question | GnRH antagonist → ↓LH → ↓gonadal androgen substrate → ↓CYP19A1 conversion → ↓estrogen (indirect; standard therapy remains aromatase inhibitors) |
| 9 | Central precocious puberty (CPP) | S1 – Research Question | Direct GnRH receptor blockade → rapid LH/FSH suppression; class effect already demonstrated for degarelix and relugolix; advantage over GnRH agonists: no initial flare |

**To advance the Research Question candidates, the following is needed:**

- Retrieve complete MOA data from DrugBank API (Data Gap DG002) to confirm receptor binding kinetics for CPP/AEXS modelling
- Download and parse the international product monograph (e.g., Orgalutran EU SmPC) to populate safety fields (Data Gap DG001)
- Conduct a targeted literature search for: *ganirelix* OR *GnRH antagonist* AND *central precocious puberty* to capture class-level evidence from degarelix/relugolix trials
- Evaluate whether Health Canada has received any prior submissions for ganirelix; clarify the regulatory pathway if pursuing a new indication in an unregistered drug
- Design a prospective research protocol or systematic review to assess GnRH antagonists as adjunct therapy in aromatase excess syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

