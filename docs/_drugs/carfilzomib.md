---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib: From Multiple Myeloma to CMM7 (Cutaneous Malignant Melanoma 7)

## One-Sentence Summary

Carfilzomib is a second-generation irreversible proteasome inhibitor, originally approved for the treatment of relapsed or refractory multiple myeloma. The TxGNN model predicts it may be effective for **CMM7 (Cutaneous Malignant Melanoma 7)**, a genetic subtype of cutaneous malignant melanoma, with **0 clinical trials** and **0 publications** directly supporting this specific indication. Broader preclinical evidence for the general melanoma indication (TxGNN rank 5) comprises 5 publications, all at the in vitro or computational level, with no clinical data yet available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed or Refractory Multiple Myeloma |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma 7) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Carfilzomib is a second-generation, selective, irreversible inhibitor of the 20S proteasome's chymotrypsin-like (β5), trypsin-like (β2), and caspase-like (β1) catalytic subunits. By blocking protein degradation, it causes accumulation of ubiquitinated proteins, triggers endoplasmic reticulum (ER) stress, and drives caspase-mediated apoptosis. This mechanism has been clinically validated in multiple myeloma, where malignant plasma cells are highly dependent on proteasome activity for survival.

CMM7 is a genetic classification of cutaneous malignant melanoma. Melanoma cells, like myeloma cells, frequently exhibit upregulated proteasome activity and dependence on NF-κB pro-survival signaling — both of which are disrupted by proteasome inhibition. Preclinical in vitro evidence (PMID 33671902) demonstrates that carfilzomib, both alone and in combination with bortezomib, induces apoptosis in B16-F1 melanoma cells through activation of caspases 3, 8, 9, and 12. This mechanistic overlap provides the theoretical basis for the TxGNN model's prediction cluster across multiple melanoma subtypes (ranks 1–5).

However, solid tumors — including melanoma — generally show substantially lower sensitivity to proteasome inhibitors than hematologic malignancies. The CMM7 genetic subtype lacks any direct clinical or preclinical evidence in the current literature, and the prediction remains entirely model-driven for this specific subtype.

---

## Clinical Trial Evidence

Currently no clinical trials for Carfilzomib in CMM7 (Cutaneous Malignant Melanoma 7) are registered.

---

## Literature Evidence

No literature directly addressing Carfilzomib in CMM7 is currently available.

**Supplementary Context — Broader Melanoma Evidence (TxGNN Rank 5, Score 99.03%, Evidence Level L4)**

The following preclinical publications are identified under the **melanoma** indication and provide indirect mechanistic context for the CMM7 prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro | Biology | Carfilzomib + bortezomib induces apoptosis in B16-F1 melanoma cells via caspase 3/8/9/12 activation; provides direct evidence for proteasome inhibition in melanoma |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational | J Biomol Struct Dyn | Molecular docking and MD simulation screening of clinical drugs against 18 cancer kinase targets including melanoma; carfilzomib identified as active |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic | Mol Cancer Res | ZANF2a (AIRAP) gene regulates cell survival in human melanoma via E3-ligase cIAP2 and the proteasome pathway; mechanistic link to proteasome dependency |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical | Leukemia | PROTAC-mediated BRD4 degradation via proteasomal pathway is active in myeloma models; broader implication that proteasome pathway is druggable across cancer types |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic | Matrix Biol | Carfilzomib activates NF-κB to upregulate heparanase in tumor cells; potential unintended pro-tumorigenic effect on tumor microenvironment warrants monitoring |

> ⚠️ All five publications are Tier 3 (in vitro, computational, or preclinical mechanistic). None constitute clinical evidence. The last publication (PMID 27016342) raises a cautionary signal: carfilzomib-induced NF-κB activation may paradoxically upregulate heparanase, potentially promoting angiogenesis and metastasis in solid tumors.

---

## Canada Market Information

Carfilzomib currently holds **no Drug Identification Numbers (DINs)** in Canada and is classified as not marketed. No regulatory license data is available in the current dataset.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent classified as a targeted therapy. Its original indication (multiple myeloma) confirms antineoplastic status.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation irreversible proteasome inhibitor (Epoxyketone class) |
| Myelosuppression Risk | High — Thrombocytopenia and anemia are common dose-limiting toxicities; neutropenia also reported |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (weekly during cycle 1), serum creatinine (renal function), cardiac function (LVEF by ECHO, blood pressure monitoring), pulmonary function (dyspnea assessment) |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV administration requires trained oncology nursing staff |

> ⚠️ **Cardiac toxicity is a distinguishing safety concern for Carfilzomib** relative to other proteasome inhibitors. Cardiac failure, hypertension, and reduced LVEF have been reported. This is especially relevant if exploring use in solid tumor populations with different baseline cardiac risk profiles than myeloma patients.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Full prescribing information (warnings, contraindications) was not available in the current Evidence Pack. Retrieval of TFDA/Health Canada product monograph is identified as a blocking data gap (DG001) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a high prediction score (99.37%) for CMM7, but no clinical trials or CMM7-specific publications have been identified, placing this at Evidence Level L5 (model prediction only). The mechanistic rationale is theoretically plausible — melanoma shares some proteasome dependence with myeloma — but solid tumors historically show poor clinical response to proteasome inhibitors, and the CMM7 genetic subtype adds an additional layer of specificity with no supporting data.

**To proceed, the following is needed:**
- Retrieve Health Canada / TFDA product monograph to resolve the blocking safety data gap (DG001) before any repurposing assessment can advance to S1 stage
- Obtain complete Carfilzomib MOA and toxicity profile from DrugBank API (DG002)
- Determine the molecular characteristics of CMM7 (specific mutations, pathway dependencies) to assess whether proteasome inhibition is mechanistically relevant to this subtype
- Review in vitro sensitivity data for CMM7 cell lines (if available) to CMM7-specific proteasome inhibitor treatment
- Evaluate the cautionary signal from PMID 27016342 (NF-κB/heparanase induction) before advancing any solid tumor study design
- If proceeding to research stage, prioritize CMM7-specific in vitro experiments and consider combination strategies (e.g., with MEK or BRAF inhibitors where applicable) to overcome solid tumor resistance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

