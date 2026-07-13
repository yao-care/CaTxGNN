---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Mogamulizumab
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is a defucosylated anti-CCR4 monoclonal antibody approved in the US (2018) for cutaneous T-cell lymphoma (mycosis fungoides and Sézary syndrome) and in Japan for adult T-cell leukemia/lymphoma, though it currently holds no Canadian market authorization. The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma** — the top-ranked of 10 predicted indications — driven by the drug's established ability to deplete CCR4+ regulatory T cells within tumor microenvironments. Currently, **no clinical trials and no publications** exist to support any of these 10 predicted indications, placing all predictions at the earliest evidence stage (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cutaneous T-cell lymphoma (mycosis fungoides / Sézary syndrome); not approved in Canada |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on publicly known pharmacology, Mogamulizumab is an afucosylated IgG1 monoclonal antibody that targets CC chemokine receptor 4 (CCR4) — a receptor preferentially expressed on malignant T-cells in cutaneous and peripheral T-cell lymphomas, as well as on immunosuppressive regulatory T cells (Tregs). Its primary anti-tumor mechanism is antibody-dependent cellular cytotoxicity (ADCC), which is substantially enhanced by the afucosylation modification that increases NK cell Fc receptor binding affinity. This dual action — eliminating both malignant CCR4+ lymphoma cells and immunosuppressive Tregs — distinguishes Mogamulizumab from conventional cytotoxic agents.

The mechanistic rationale for extending this drug to urothelial carcinoma stems from tumor microenvironment (TME) biology: CCR4+ FoxP3+ Tregs infiltrate a broad range of solid tumors, including urothelial cancers, where they suppress effector T-cell activity and correlate with worse prognosis. Depleting these Tregs via anti-CCR4 therapy theoretically "releases the brake" on anti-tumor immunity — a concept with growing preclinical support, particularly in combination with PD-1/PD-L1 checkpoint blockade. Mogamulizumab has already been studied alongside nivolumab in hematological malignancies, establishing a precedent for Treg-depletion/checkpoint inhibitor synergy.

However, prostatic urethra urothelial carcinoma is an exceptionally rare pathological subtype with no published data on CCR4 expression, Treg infiltration, or immune checkpoint responsiveness specific to this entity. The TxGNN high score most likely reflects topological proximity in the knowledge graph to established CCR4/Treg biology across urothelial cancers broadly, rather than direct experimental evidence for this specific subtype. This prediction is best treated as a hypothesis-generating signal, not a clinically actionable finding at this stage.

---

## All TxGNN Predicted Indications (Top 10)

| Rank | Disease | TxGNN Score | Recommendation | Key Rationale |
|------|---------|-------------|----------------|---------------|
| 1 | Prostatic urethra urothelial carcinoma | 99.44% | Hold | CCR4+ Treg depletion mechanistically plausible for TME; extremely rare subtype with zero CCR4-specific data |
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.42% | Hold | Upper urinary tract UCC shares Treg biology; sarcomatoid variant-specific CCR4 data entirely absent |
| 3 | Infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.40% | Hold | Bladder TME Treg infiltration linked to poor prognosis; no clinical data for sarcomatoid variant |
| 4 | Renal pelvis papillary urothelial carcinoma | 99.37% | Hold | Molecular features shared with bladder TCC; score likely driven by urothelial graph cluster effect |
| 5 | Human herpesvirus 8-related tumor | 99.24% | **Research Question** | CCR4 expressed on HHV-8-infected T-cells and some PEL cell lines; ADCC + Treg depletion conceptually plausible |
| 6 | Ectomesenchymoma | 99.15% | Hold | Extremely rare pediatric tumor; no known CCR4 association; likely knowledge graph false positive |
| 7 | Malignant cutaneous granular cell skin tumor | 99.15% | Hold | Cutaneous location superficially resembles CTCL setting; completely different neural cell origin, no CCR4 data |
| 8 | Middle ear neuroendocrine tumor | 98.99% | Hold | Treg infiltration reported in some NETs, but CCR4-specific data absent; prediction likely topological noise |
| 9 | Transitional cell carcinoma | 98.98% | **Research Question** | Broader disease category; in vitro evidence for Treg depletion + PD-1 synergy in urothelial cancer worth exploring |
| 10 | Richter syndrome | 98.56% | **Research Question** | CLL→DLBCL transformation with CCR4+ Treg-rich TME; partial CCR4 expression on transformed cells; highest mechanistic specificity and unmet need among all predictions |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mogamulizumab in any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for Mogamulizumab in any of the 10 predicted indications.

---

## Canada Market Information

Mogamulizumab currently holds no Health Canada approvals and is not marketed in Canada (0 DINs). For reference, the drug is commercialized as Poteligeo® (Kyowa Kirin) with FDA approval in the US for mycosis fungoides and Sézary syndrome, and with approval in Japan for adult T-cell leukemia/lymphoma. Canadian regulatory submission would require a full dossier review prior to any domestic use.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — defucosylated anti-CCR4 monoclonal antibody; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate (mechanism-based lymphopenia expected; does not cause typical myelosuppression seen with cytotoxic chemotherapy) |
| Emetogenicity Classification | Low (consistent with monoclonal antibody class) |
| Monitoring Items | CBC with differential (particularly lymphocyte count), liver function tests, skin assessment (infusion reactions; serious dermatologic adverse events reported in class) |
| Handling Protection | Standard biologic/monoclonal antibody handling protocols apply; formal closed-system cytotoxic drug handling precautions not required for this agent class |

> This Evidence Pack contains no toxicity data (TFDA package insert not retrieved; Data Gap DG001). Please refer to the Poteligeo® US Prescribing Information for complete warnings, including risk of serious cutaneous reactions (DRESS, Stevens-Johnson Syndrome, Toxic Epidermal Necrolysis) and severe graft-versus-host disease if allogeneic HSCT is administered following treatment.

---

## Safety Considerations

Please refer to the package insert for safety information. This Evidence Pack contains no drug-specific safety data — the TFDA/Health Canada package insert has not yet been retrieved (Data Gap DG001, severity: Blocking), and no drug interaction data were identified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications currently have zero supporting clinical trials or published literature (L5 evidence across the board), and Mogamulizumab is not approved in Canada. While the anti-CCR4/Treg-depletion mechanism has genuine theoretical applicability to immunosuppressed tumor microenvironments — including urothelial and certain hematological cancers — no direct experimental evidence exists to bridge this mechanism to any of the specific predicted disease entities. The top 4 predictions are all rare or ultra-rare urothelial subtypes where even the existence of CCR4 expression has not been demonstrated.

**Among the 10 predictions, three warrant prioritized follow-up before committing to a full Hold:**

- **Richter syndrome (Rank 10)** — Highest mechanistic specificity: CCR4+ Tregs documented in the CLL-to-DLBCL TME, partial CCR4 expression on transformed cells reported, and the disease carries extreme unmet medical need with no established salvage standard of care. Priority candidate for a targeted literature search.
- **Transitional cell carcinoma (Rank 9)** — The broader urothelial category (rather than the rare subtypes at Ranks 1–4) has stronger biological rationale; in vitro preclinical data on Treg + checkpoint inhibitor synergy in bladder cancer exists and should be formally reviewed.
- **HHV-8-related tumors (Rank 5)** — Virus-associated CCR4 expression in infected T-cells provides a distinct and independent rationale from the urothelial cluster; a targeted PubMed search on CCR4/PEL/Kaposi sarcoma is low-effort with potentially high yield.

**To advance any of these to Research Question stage, the following is needed:**

- Retrieve complete MOA and category data from DrugBank API for Mogamulizumab (resolve Data Gap DG002)
- Retrieve and review the TFDA/Health Canada–equivalent package insert for full warnings and contraindications (resolve blocking Data Gap DG001)
- Conduct a targeted PubMed search for: (1) CCR4 expression in transitional cell carcinoma TME, (2) Treg infiltration in Richter syndrome, and (3) Mogamulizumab or anti-CCR4 therapy in HHV-8-associated malignancies
- Query TCGA and GEO datasets for CCR4 expression profiling in urothelial cancer subtypes to determine whether the predicted indications have a measurable biomarker basis
- For the three Research Question candidates: define a structured scoping review protocol before any clinical translation proposal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

