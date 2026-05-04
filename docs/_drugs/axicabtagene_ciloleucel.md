---
layout: default
title: Axicabtagene Ciloleucel
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Axicabtagene Ciloleucel
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

# Axicabtagene Ciloleucel: From Large B-cell Lymphoma to Crohn's Colitis

## One-Sentence Summary

Axicabtagene ciloleucel (Axi-cel; brand name Yescarta) is a CD19-directed chimeric antigen receptor T-cell (CAR-T) therapy originally developed for relapsed or refractory large B-cell lymphoma and follicular lymphoma.
The TxGNN model predicts it may be effective for **Crohn's Colitis**, with a prediction score of 91.39%; however, **no clinical trials and no publications** currently support this specific repurposing direction, and the mechanistic rationale is notably weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Large B-cell Lymphoma / Follicular Lymphoma (per global regulatory approvals; no Canadian authorization on record) |
| Predicted New Indication | Crohn's Colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, axicabtagene ciloleucel is an autologous CAR-T cell therapy in which the patient's own T cells are genetically engineered to express a chimeric antigen receptor targeting **CD19** — a surface protein expressed on normal and malignant B cells. By redirecting cytotoxic T cells to eliminate CD19-positive cells, Axi-cel achieves deep B-cell depletion in lymphoma patients. Its approved indications are B-cell malignancies, where the target antigen is constitutively expressed on tumor cells.

The proposed extension to Crohn's colitis rests on a theoretical premise that B-cell elimination might modulate chronic intestinal inflammation. However, the mechanistic link is weak. Crohn's colitis is predominantly driven by aberrant CD4+ T-cell responses (Th1/Th17 axis) and dysregulated innate immunity at the mucosal barrier — not by B-cell overactivity. Unlike rheumatoid arthritis, where anti-CD20 rituximab has validated B-cell depletion as a meaningful therapeutic strategy, no comparable evidence supports this approach in Crohn's disease.

An additional safety concern further undermines this prediction: the cytokine release syndrome (CRS) associated with CAR-T infusion could plausibly worsen intestinal inflammation rather than ameliorate it. The high TxGNN score (91.39%) most likely reflects network-level graph topology similarities within the knowledge graph rather than direct biological plausibility. The mechanistic relevance is assessed as **weak**, and this repurposing direction is not currently supported by available evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Axicabtagene ciloleucel (Yescarta) is **not currently approved or marketed in Canada**. No Drug Identification Numbers (DINs) are on record with Health Canada.

> For reference: Axi-cel has received marketing authorization in the United States (FDA, October 2017), the European Union (EMA, August 2018), and several other jurisdictions for large B-cell lymphoma and follicular lymphoma. A Canadian Health Canada submission and review would be required before any authorized use in Canada.

---

## Cytotoxicity

Axicabtagene ciloleucel is an antineoplastic cellular immunotherapy. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — CAR-T cell therapy (gene-modified autologous T-cell product); not a conventional cytotoxic agent |
| Myelosuppression Risk | High — lymphodepletion conditioning (fludarabine + cyclophosphamide) is required prior to infusion; severe and prolonged cytopenias (neutropenia, thrombocytopenia, anemia) are common post-infusion |
| Emetogenicity Classification | Low from Axi-cel infusion itself; Moderate from the conditioning chemotherapy regimen |
| Monitoring Items | CBC with differential (daily during hospitalization period), comprehensive metabolic panel, serum ferritin, IL-6 (CRS monitoring), continuous neurological assessment (ICANS grading), vital signs, oxygen saturation |
| Handling Protection | Requires specialized handling per cellular and gene therapy protocols; must be prepared and administered only at certified treatment centers equipped with tocilizumab, corticosteroids, and intensive care support on standby |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 91.39%, the mechanistic basis for Axi-cel in Crohn's colitis is weak — Crohn's disease is a T-cell-predominant disorder where CD19-directed B-cell depletion lacks a clear therapeutic rationale, and the CRS risk profile may actively contraindicate use in an inflamed bowel setting. With zero supporting clinical trials and zero publications (Level L5 — model prediction only), there is insufficient basis to advance this candidate.

**To proceed with any further evaluation, the following is needed:**

- **MOA data**: Retrieve full mechanism of action and target profile from DrugBank (DB13915) to confirm CD19 specificity and off-target risks
- **Health Canada product monograph**: Obtain the Canadian package insert equivalent for complete safety, contraindication, and DDI profiling
- **Disease biology review**: Commission a literature review on B-cell involvement in specific Crohn's colitis endotypes (e.g., antibody-positive subgroups) to reassess mechanistic plausibility
- **CRS risk assessment in IBD**: Evaluate whether intestinal inflammation constitutes a contraindication to CAR-T infusion in this patient population
- **Re-prioritize candidates**: Consider advancing the three indications flagged as **"Research Question"** — **rheumatoid vasculitis** (moderate mechanistic link via B-cell axis, supported by indirect Schett et al. 2023–2024 autoimmune CAR-T data), **idiopathic aplastic anemia** (emerging class-effect signal), and **ankylosing spondylitis** (emerging autoimmune CAR-T field) — before investing further in Crohn's colitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

