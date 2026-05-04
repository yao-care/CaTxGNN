---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Severe Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab (Fasenra) is a humanized anti-IL-5Rα monoclonal antibody approved internationally for severe eosinophilic asthma and eosinophilic granulomatosis with polyangiitis (EGPA), though not currently marketed in Canada.
The TxGNN model ranks **Thrombocytopenia Due to Immune Destruction** as its top repurposing candidate,
yet **no clinical trials** and **no published literature** currently support this direction — placing the evidence at the lowest confidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (globally approved; not registered in Canada) |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab binds directly to the IL-5 receptor α-subunit (IL-5Rα) expressed on eosinophils and basophils. Through antibody-dependent cell-mediated cytotoxicity (ADCC), it triggers rapid, near-complete depletion of circulating eosinophils. This mechanism underpins its proven efficacy in severe eosinophilic asthma and EGPA — diseases where eosinophil-driven type 2 inflammation is the central pathological driver.

Thrombocytopenia due to immune destruction (immune thrombocytopenia, ITP) operates through an entirely different immune axis: autoreactive IgG antibodies targeting platelet surface glycoproteins (GPIIb/IIIa), combined with cytotoxic CD8+ T cell activity and splenic macrophage-mediated phagocytosis of antibody-coated platelets. Eosinophils do not play an established causal role in platelet destruction, and there is no known mechanistic link between IL-5 signalling and the pathophysiology of ITP.

The high TxGNN score most likely reflects **topological proximity within the knowledge graph** — benralizumab's connections to autoimmune inflammatory diseases (EGPA, eosinophilic disorders) place it near other autoimmune nodes such as ITP — rather than a true biological relationship. Based on current immunological evidence, the mechanistic rationale for this specific repurposing is weak, and the prediction should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Benralizumab has no Drug Identification Numbers (DINs) registered with Health Canada and is currently not marketed in Canada. No approved product information is available from the Canadian regulatory database.

> **Note:** Benralizumab is commercially available internationally as **Fasenra** (AstraZeneca) with approvals in the United States (FDA, 2017), European Union (EMA, 2018), and Japan (PMDA), among others. Any future Canadian submission would require a separate Health Canada review.

---

## Safety Considerations

Please refer to the prescribing information and package insert for safety information. Canadian-specific warnings, contraindications, and drug interaction data are not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high score (99.34%), this appears to reflect knowledge graph network topology — the proximity of autoimmune disease nodes — rather than a genuine mechanistic link between benralizumab's IL-5Rα blockade and immune-mediated platelet destruction. With zero supporting clinical trials, zero publications, no Canadian market authorization, and no established mechanistic rationale, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Preclinical or translational evidence establishing a role for IL-5 or eosinophils in ITP pathophysiology
- Biomarker data from ITP patient cohorts documenting elevated IL-5 levels or eosinophil infiltration in bone marrow/spleen
- A mechanistic hypothesis beyond knowledge graph topology (e.g., eosinophil-platelet crosstalk, IL-5-mediated immune regulation)
- Full MOA documentation retrieved from DrugBank API (currently a data gap)
- Health Canada prescribing information or equivalent package insert for complete safety and contraindication assessment
- Consideration of the broader predicted indication list: **Dermatitis** (Rank 2) and **Childhood CTD-ILD** (Rank 7) carry stronger mechanistic rationale and are flagged as "Research Question" — these may be more productive starting points for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

