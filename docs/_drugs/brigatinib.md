---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib (ALUNBRIG®) is a next-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor, approved in the United States since 2017 for ALK-positive metastatic non-small cell lung cancer (NSCLC) — both in the first-line setting and for patients who progressed on crizotinib.
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival** with a high prediction score of **99.89%**;
however, **no clinical trials or supporting literature** have been identified for this specific indication, placing the overall evidence at **Level L5** with a recommendation to **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive metastatic NSCLC (approved in the US/EU/Japan; not marketed in Canada) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 — Model prediction only; no supporting studies identified |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brigatinib is a second-generation ALK tyrosine kinase inhibitor designed to overcome crizotinib resistance. Its primary mechanism is inhibition of ALK fusion proteins — most commonly EML4-ALK — which are the oncogenic driver in approximately 3–5% of advanced NSCLC cases. Beyond ALK, brigatinib also inhibits ROS1, ErbB2 (HER2), FLT3, and EGFR at clinically relevant concentrations, giving it a broader kinase inhibition profile than first-generation agents. This multi-kinase activity is the basis for evaluating it in non-NSCLC indications such as NF2-related schwannomatosis (where ErbB2 suppression is the proposed mechanism).

Gingival fibromatosis is characterized by diffuse overgrowth of gingival connective tissue. Hereditary forms are driven primarily by mutations in the **RAS-MAPK pathway** (e.g., SOS1, PTPN11), while drug-induced forms (calcium channel blockers, phenytoin, cyclosporine) involve altered fibroblast proliferation through calcium- and mTOR-mediated mechanisms. There is no known intersection between the RAS-MAPK dysregulation underlying gingival fibromatosis and the ALK/ROS1/ErbB2 pathways that brigatinib targets.

The high TxGNN score most likely reflects a knowledge graph artifact: the "fibroproliferative process" or "connective tissue neoplasm" ontology nodes may be broadly linked to kinase inhibitors without discriminating between the specific molecular drivers of each fibroproliferative disease. In the absence of any biological rationale or supporting evidence, this prediction cannot be considered clinically actionable at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brigatinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Brigatinib in Fibromatosis, Gingival.

---

## Canada Market Information

Brigatinib is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) have been issued by Health Canada as of the data cutoff (April 5, 2026).

> For reference: Brigatinib (ALUNBRIG®) has received regulatory approval in the United States (FDA accelerated approval April 2017; full approval May 2020), the European Union (EMA 2018), and Japan (PMDA). Canadian regulatory status should be confirmed via the Health Canada Drug Product Database.

---

## Cytotoxicity

Brigatinib is an antineoplastic agent (small-molecule TKI targeting ALK-positive malignancies); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK / ROS1 / ErbB2 tyrosine kinase inhibitor (oral small molecule) |
| Myelosuppression Risk | Low to Moderate — cytopenias (anemia, neutropenia) are reported but substantially less frequent than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low (oral targeted agent; nausea reported in ~33% at 180 mg QD but rarely severe) |
| Monitoring Items | CBC with differential; liver function tests (AST/ALT/bilirubin); creatine phosphokinase (CPK — myalgia and CPK elevation are common); pulmonary function and CT imaging (risk of early-onset interstitial lung disease/pneumonitis, especially in first 7 days); blood pressure; heart rate (bradycardia) |
| Handling Protection | Standard oral antineoplastic handling precautions required; follow institutional cytotoxic drug-handling policies |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RAS-MAPK–driven pathogenesis of gingival fibromatosis has no established intersection with the ALK/ROS1/ErbB2 signaling axis that brigatinib targets, and no clinical or preclinical data support this predicted indication. The high TxGNN score is likely a knowledge graph artifact from broad ontological node linkage rather than a genuine mechanistic connection.

**To proceed, the following is needed:**
- Molecular profiling studies of gingival fibromatosis tissue to determine whether ALK, ROS1, or ErbB2 pathway activation is present in any subtype
- Preclinical studies (cell line or animal model) demonstrating brigatinib activity in fibroblastic gingival overgrowth
- Retrieval and review of the official package insert (Health Canada / FDA monograph) to fill safety gaps (contraindications, key warnings)
- Complete MOA data from DrugBank (DB12267) to enable a full mechanistic cross-indication analysis
- Reassessment of whether the TxGNN knowledge graph correctly distinguishes between ALK-driven fibroproliferative malignancies and non-ALK connective tissue disorders before elevating this candidate's priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

