---
layout: default
title: Dimethicone
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Dimethicone
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

# Dimethicone: From Topical Skin Protection to Insomnia

## One-Sentence Summary

Dimethicone is an inert silicone polymer (polydimethylsiloxane) widely used as a topical skin protectant, emollient, and antifoaming excipient in pharmaceutical and cosmetic formulations.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **94.35%**; however, there is **1 tangentially related clinical trial** (Grade C relevance) and **0 supporting publications** for this specific indication, and critical mechanistic concerns are present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered therapeutic indication in Canada |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 — Model prediction only; no supporting clinical studies |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on what is broadly known, Dimethicone (polydimethylsiloxane, PDMS) is a chemically inert siloxane polymer. It does not cross biological membranes in a pharmacologically meaningful way, and there is **no established central nervous system (CNS) activity** for this compound — no known interaction with GABA receptors, melatonin pathways, orexin receptors, or any other sleep-regulating mechanism.

**This prediction is not mechanistically supported.** The high TxGNN score (94.35%) most likely reflects indirect node associations within the knowledge graph — for example, shared cosmetic product contexts, co-occurrence in clinical records, or excipient-level co-formulation data — rather than a genuine biological rationale for treating insomnia. Dimethicone has no known blood-brain barrier penetration and is generally considered pharmacologically inactive as a standalone compound.

It is also important to flag a systemic concern across the lower-ranked predictions (Ranks 2–9), which are predominantly cataract subtypes. Silicone oil (a high-viscosity form of PDMS/Dimethicone) is used in vitreoretinal surgery as a tamponade agent — and a well-documented **complication** of this use is cataract formation. The TxGNN model appears to have detected the Dimethicone–cataract association in the knowledge graph and interpreted it as a potential treatment opportunity, when in fact the direction of the relationship is the **opposite**: Dimethicone is a known contributor to cataract development in surgical contexts, not a treatment for it. This pattern suggests that TxGNN may be generating false positives for this compound across multiple indications.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | Not Applicable | Completed | 74 | A skin health study evaluating oral supplementation ("Inner Calm") and topical "Super Calm" formulations for skin redness and sensitivity. Sleep quality may have appeared as a secondary endpoint within a general wellness assessment. **This study does not evaluate Dimethicone as a treatment for insomnia.** (Relevance Grade: C — Not applicable) |

> **Note:** No clinical trials directly investigating Dimethicone for insomnia treatment were identified.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dimethicone (DB11074) has no active Drug Identification Numbers (DINs) registered in Canada. It is not licensed as a standalone therapeutic agent by Health Canada. It may appear as an inactive excipient or topical skin protectant ingredient in multi-ingredient products, but no standalone DIN records were found in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dimethicone is a chemically inert siloxane polymer with no known pharmacological mechanism relevant to insomnia or any CNS condition. The single retrieved clinical trial (NCT04872946) is not relevant to insomnia treatment. With an Evidence Level of L5 (model prediction only) and a complete absence of mechanistic plausibility, this candidate does not meet the threshold for further repurposing evaluation at this time. Additionally, the cluster of cataract-related predictions (Ranks 2–9) raises a knowledge graph directionality concern that may affect the reliability of TxGNN outputs for this compound more broadly.

**To revisit or escalate this candidate, the following would be needed:**

- **Mechanistic clarification:** A formal MOA review from DrugBank or primary literature to confirm (or rule out) any CNS-relevant activity
- **KG audit:** Review the knowledge graph edges connecting Dimethicone to sleep-related nodes to determine if the association is excipient co-formulation, indirect co-occurrence, or a genuine biological link
- **Directionality correction for cataract nodes:** Flag Dimethicone–cataract edges in the KG as adverse/causative rather than therapeutic, to prevent future false-positive predictions
- **Canada regulatory review:** Confirm whether Dimethicone appears in any multi-ingredient DIN products that carry a therapeutic claim, which could provide additional safety context

> *This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

