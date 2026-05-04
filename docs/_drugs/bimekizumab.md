---
layout: default
title: Bimekizumab
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: From Inflammatory Conditions to Diabetic Cataract

## One-Sentence Summary

Bimekizumab is a dual IL-17A/F inhibitor biologic established in neutrophil-driven inflammatory diseases such as plaque psoriasis and spondyloarthritis. The TxGNN model predicts it may be effective for **Diabetic Cataract**, achieving a prediction score of 98.23% — yet **zero clinical trials and zero publications** currently support this direction. The mechanistic rationale is considered extremely weak, with the high score most likely attributable to knowledge-graph topology artefacts rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from market data (publicly known: plaque psoriasis, psoriatic arthritis, axial spondyloarthritis) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on publicly known information, Bimekizumab is a humanized monoclonal IgG1 antibody that selectively and simultaneously inhibits both IL-17A and IL-17F cytokines, blocking their binding to the shared IL-17RA/RC receptor complex. This dual blockade produces markedly stronger suppression of downstream neutrophil-driven inflammation than inhibiting either cytokine alone — which is the basis for its established efficacy in plaque psoriasis, psoriatic arthritis, and axial spondyloarthritis.

Diabetic cataract, the top-ranked TxGNN prediction, has a fundamentally different pathological basis. The primary disease mechanism involves aldose reductase–driven accumulation of sorbitol within the lens, combined with advanced glycation end-product (AGE) deposition and oxidative protein cross-linking, leading to irreversible lens opacity. While IL-17 has been documented to contribute to diabetic retinopathy through promotion of neovascularization and neuroinflammation, this is a distinct ocular compartment and disease process from the sorbitol-driven lens pathology of diabetic cataract.

The Evidence Pack's internal mechanistic analysis explicitly identifies the connection as extremely weak, noting that the high TxGNN score most likely reflects graph topology adjacency — specifically, Bimekizumab's drug node shares graph neighbours with the broader "diabetes" disease cluster in the knowledge graph, not a direct IL-17A/F → lens biology axis. This is a well-recognised artefact in graph-based repurposing models and significantly undermines the clinical relevance of this prediction. Notably, all 10 top-ranked predictions are cataract subtypes or an unrelated coagulation disorder (antithrombin deficiency type 2), further suggesting systematic graph topology bias rather than meaningful biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Health Canada drug authorizations on record for Bimekizumab at the time of this report (data cutoff: 2026-04-05). The drug is classified as **not marketed** in Canada, with zero Drug Identification Numbers (DINs) issued.

> **Note:** Health Canada regulatory status should be independently verified against the Health Canada Drug Product Database, as market authorization data may have changed since the data cutoff date.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No safety data was available in this Evidence Pack. Key warnings, contraindications, and drug interaction data are all identified as data gaps requiring remediation via the Health Canada product monograph or DrugBank API query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the raw TxGNN score is high (98.23%), the prediction almost certainly reflects knowledge-graph topology artefacts — the "diabetes" cluster shares graph neighbours with Bimekizumab's IL-17 pathway nodes — rather than a genuine mechanistic relationship. IL-17A/F inhibition has no established connection to the sorbitol pathway, AGE accumulation, or lens protein aggregation that drives diabetic cataract. With zero supporting clinical trials, zero publications, and an explicitly weak mechanistic link identified in the internal Evidence Pack analysis, this indication does not meet the threshold for further development investment at this stage.

**To proceed, the following is needed:**
- Graph topology ablation analysis to confirm whether the cataract cluster signal disappears when diabetes-related nodes are removed from the knowledge graph
- Preclinical evidence (in vitro or animal model) demonstrating any IL-17A or IL-17F involvement in lens epithelial cell dysfunction or sorbitol pathway modulation
- Formal MOA data retrieval from DrugBank (DG002) to complete the mechanistic assessment
- Health Canada product monograph retrieval (DG001) to establish baseline safety profile before any indication expansion planning
- If any preclinical IL-17/lens signal is subsequently identified: hypothesis-testing studies in streptozotocin-induced diabetic cataract animal models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

