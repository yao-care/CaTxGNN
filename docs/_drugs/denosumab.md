---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody that inhibits RANK Ligand (RANKL), widely used internationally for osteoporosis and prevention of skeletal-related events in cancer patients.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy** with a score of 99.63%; however, **no direct clinical trials or publications** currently support this specific indication.
Indirect mechanistic and real-world evidence exists through the broader diabetic retinopathy indication (**1 clinical trial**, **2 publications**), keeping the overall evidence at Level 5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis; bone loss prevention in patients on hormone-deprivation therapy |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (no DIN records found) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, Denosumab is a fully human IgG2 monoclonal antibody that binds and neutralises RANK Ligand (RANKL), the key cytokine driving osteoclast maturation and survival. By blocking the RANKL–RANK interaction, Denosumab reduces osteoclast activity and is approved internationally for postmenopausal osteoporosis, glucocorticoid-induced osteoporosis, and prevention of skeletal-related events in malignancy.

The biological rationale for extending Denosumab into diabetic retinopathy centres on the RANKL/OPG (Osteoprotegerin) axis. OPG, the endogenous decoy receptor for RANKL, is expressed in retinal vasculature, and imbalance between RANKL and OPG has been proposed to amplify vascular inflammation, endothelial dysfunction, and microvascular injury—all hallmarks of diabetic retinopathy. Furthermore, RANKL inhibition suppresses systemic pro-inflammatory mediators such as TNF-α and IL-6, which are known to contribute to diabetic microvascular damage. Supporting this indirectly, a 2024 real-world cohort analysis (PMID 38899553) found that Denosumab reduces the incidence of type 2 diabetes and its microvascular complications (including retinopathy) compared with bisphosphonates.

That said, the TxGNN score of 99.63% reflects knowledge-graph topological proximity — not validated efficacy. No preclinical model has directly tested Denosumab in retinal tissue under diabetic conditions, and no clinical trial has enrolled patients with severe nonproliferative diabetic retinopathy as a primary population. This prediction should be treated strictly as a hypothesis-generating signal requiring prospective investigation.

---

## Clinical Trial Evidence

No clinical trials directly evaluating Denosumab for **severe nonproliferative diabetic retinopathy** were identified.

The following trial was retrieved for the broader **diabetic retinopathy** search and is included for contextual reference:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Evaluated new or worsening lens opacifications (cataract) in men with non-metastatic prostate cancer receiving Denosumab for ADT-induced bone loss. The primary endpoint was ocular safety (crystalline lens changes), not diabetic retinopathy. Retinal outcomes, if collected, would be incidental safety observations only. Grade C relevance — does not support DR efficacy. |

---

## Literature Evidence

No publications directly addressing Denosumab in **severe nonproliferative diabetic retinopathy** were identified.

The following publications were retrieved for the broader **diabetic retinopathy / diabetes complications** search:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observational cohort + Meta-analysis | *Diabetes, Obesity & Metabolism* | Real-world cohort analysis with systematic review and meta-analysis. Denosumab reduced the incidence of type 2 diabetes and long-term microvascular complications (retinopathy, neuropathy, nephropathy) compared with bisphosphonates. Provides indirect population-level signal that RANKL inhibition may protect against diabetic microvascular disease, including retinopathy. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cross-sectional | *Cureus* | Evaluated fracture risk (FRAX tool) in adults with type 2 diabetes to identify patients eligible for anti-osteoporotic therapy. Contextually relevant to the bone–diabetes interface but provides no direct data on Denosumab's effect on retinopathy. |

---

## Canada Market Information

No DIN records for Denosumab were found in the current regulatory dataset.

> **Note:** This finding may reflect a data gap rather than true non-approval. Denosumab is marketed internationally under the brand names **Prolia** (osteoporosis) and **Xgeva** (oncology/bone metastases). Verification against Health Canada's Drug Product Database is recommended before drawing regulatory conclusions.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) were returned by the current data pipeline for Denosumab.

Please refer to the Prolia/Xgeva Canadian product monograph for complete safety information. Key areas to review include:
- **Hypocalcaemia** (must correct before initiating therapy)
- **Osteonecrosis of the jaw**
- **Atypical femoral fracture**
- **Serious infections** (skin, urinary tract, endocarditis)
- **Rebound vertebral fractures** upon discontinuation

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.63%), but this reflects knowledge-graph structural similarity, not clinical evidence. There are currently no preclinical or clinical studies directly investigating Denosumab for severe nonproliferative diabetic retinopathy, placing this candidate at Evidence Level 5. The indirect signal from PMID 38899553 is promising but insufficient to advance without further mechanistic and translational validation.

**To proceed, the following is needed:**

- **Mechanistic validation:** Preclinical studies (in vitro endothelial/pericyte models; streptozotocin or db/db mouse retinal models) to assess whether RANKL inhibition attenuates retinal microangiopathy
- **Biomarker data:** Characterise RANKL/OPG expression in diabetic retinal tissue (human biopsy or vitreous humour analysis)
- **Post-hoc data mining:** Query existing large Denosumab trial datasets (e.g., FREEDOM, DECIDE, NCT00925600) for any collected retinal or fundoscopic outcomes
- **Regulatory clarification:** Verify Denosumab DIN status in Health Canada's Drug Product Database and obtain the full Canadian product monograph for safety screening
- **MOA confirmation:** Retrieve complete DrugBank pharmacology entry (DB06643) to enable formal mechanism-of-action relevance scoring
- **Evidence uplift target:** Advance to L4 (at minimum one preclinical study) before proceeding to clinical feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

