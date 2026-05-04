---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib (Zykadia) is a second-generation ALK (Anaplastic Lymphoma Kinase) tyrosine kinase inhibitor approved in the United States and European Union for the treatment of ALK-positive non-small cell lung cancer (NSCLC), but currently not marketed in Canada.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis** with a prediction score of **99.86%**; however, **no clinical trials and no supporting literature** exist for this indication, making this a model-only (L5) prediction.
The high prediction score is likely attributable to non-specific knowledge graph node connections rather than any genuine mechanistic link between ceritinib and this disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive NSCLC (established from published literature; not approved in Canada) |
| Predicted New Indication | Gingival Fibromatosis (*fibromatosis, gingival*) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory dataset. Based on published literature, ceritinib is a potent, selective second-generation ALK inhibitor — approximately 20-fold more potent than the first-generation inhibitor crizotinib. In addition to ALK, it inhibits ROS1, IGF-1R (Insulin-like Growth Factor 1 Receptor), and FAK (Focal Adhesion Kinase). Its established clinical utility is in patients whose NSCLC harbours the EML4-ALK fusion oncogene, which drives uncontrolled proliferative signalling through the ALK receptor tyrosine kinase pathway.

Gingival fibromatosis is a benign, slow-growing fibrous proliferation of the gingival tissue. Its pathophysiology involves abnormalities in the CTNNB1 or APC genes, leading to dysregulation of the β-catenin (Wnt) signalling pathway. There is no established biological intersection between this pathway and the ALK/ROS1 signalling axis that ceritinib targets. The two disease entities are mechanistically unrelated.

The high TxGNN score (99.86%) is most plausibly explained by non-specific linkage within the knowledge graph — likely connecting "fibroblast proliferation" nodes to "kinase regulation" nodes via indirect multi-hop paths. This is a characteristic pattern of TxGNN model generalization bias rather than disease-specific predictive signal. **No clinical, preclinical, or mechanistic evidence supports ceritinib for gingival fibromatosis.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ceritinib holds no approved Drug Identification Numbers (DINs) in Canada as of the data cutoff (April 4, 2026) and is therefore not marketed in Canada. For reference, ceritinib is approved in the United States (FDA, 2014, under Breakthrough Therapy designation) and in the European Union (EMA, 2015) for ALK-positive metastatic NSCLC.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (oral small molecule) |
| Myelosuppression Risk | Low to moderate (lymphopenia reported; less myelosuppressive than conventional cytotoxic chemotherapy) |
| Emetogenicity Classification | Moderate to high (nausea, vomiting, and diarrhoea are among the most common and dose-limiting toxicities; food restriction at initiation recommended) |
| Monitoring Items | Liver function tests (hepatotoxicity, including fatal cases reported), fasting blood glucose (hyperglycaemia), ECG (QTc prolongation), CBC with differential (lymphopenia), serum lipase/amylase (pancreatitis), pulmonary function (interstitial lung disease / pneumonitis) |
| Handling Protection | Should be handled following institutional cytotoxic drug handling procedures for oral antineoplastic agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The evidence dataset contains no approved Canadian product monograph or package insert data for ceritinib (DG001: Blocking data gap). Key known class-related risks from published literature include: QT interval prolongation, severe hepatotoxicity, interstitial lung disease/pneumonitis, severe diarrhoea and nausea/vomiting (dose-limiting), hyperglycaemia, and bradycardia. These should be verified against the originator product monograph (Zykadia; Novartis) before any clinical use consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of ceritinib for gingival fibromatosis is assessed as a knowledge graph false positive. Gingival fibromatosis is a benign fibroblast proliferative disorder mechanistically driven by β-catenin/Wnt pathway abnormalities, with no known overlap with the ALK/ROS1/IGF-1R signalling that ceritinib inhibits. There is zero supporting clinical trial or literature evidence, and the repurposing rationale analysis explicitly identifies this as a model generalization artefact.

**To proceed, the following would be needed:**

- Demonstration of ALK, ROS1, or IGF-1R expression or aberrant activation in gingival fibromatosis tissue samples (currently undocumented in any published literature)
- Preclinical cell line or animal model data showing ceritinib activity against fibromatosis or β-catenin-driven fibroproliferative disease
- Clarification of ceritinib's full mechanism of action from DrugBank (DG002: High severity data gap) to identify any previously uncharacterised off-target activity relevant to fibromatosis pathways
- This indication is recommended to be **flagged as a TxGNN disease-classification false positive** and deprioritized in all downstream analysis pipelines

> ⚠️ **Research Note:** Among all 10 predicted indications in this Evidence Pack, the most evidence-supported candidate is **Lung Germ Cell Tumor** (Rank 7, Evidence Level L4, Decision Stage S1: "Research Question"), which carries indirect mechanistic plausibility through ALK expression in neural crest-derived tumours and confirmed CNS penetration (Phase 0 trial NCT02605746). Should a repurposing programme for ceritinib be considered, this indication warrants prioritisation over the rank-1 prediction.

---

*Report generated: 2026-04-04 | Data cutoff: 2026-04-04 | Candidate ID: TW-DB09063-multi v4*

*⚠️ This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

