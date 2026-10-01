---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is a kinase inhibitor (ALK, ROS1 and MET) used to treat ALK-positive and ROS1-positive non-small cell lung cancer. The TxGNN model predicts it may be effective for **gingival fibromatosis**, with a very high score of 99.81%. However, **no clinical trials and no publications** currently support this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (taken from published literature; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% (model rank 4337) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Crizotinib is an ATP-competitive inhibitor of the receptor tyrosine kinases ALK, ROS1 and c-MET. It is established in non-small cell lung cancer driven by ALK or ROS1 rearrangements. Detailed mechanism-of-action data are not available in the DrugBank record supplied for this report. The kinase targets above come from the literature retrieved for other predicted indications.

The link to gingival fibromatosis, a benign overgrowth of gum tissue, is weak. No connection between ALK, ROS1 or MET signalling and this condition is documented in the data provided. The high score most likely reflects proximity in the knowledge graph rather than a demonstrated biological rationale. It should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2384264 | XALKORI |
| 2384256 | XALKORI |

Dosage form and approved-indication text are not included in the licence records provided.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Literature reports point to liver function, cardiac rhythm (heart rate, QT interval) and respiratory symptoms (interstitial lung disease); confirm against the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

The Health Canada package insert warnings, contraindications and drug interaction data were not available for this report. The retrieved literature describes the following crizotinib safety signals:

- **Hepatotoxicity**: a case report of fatal fulminant liver failure after 24 days of therapy (PMID 26898609).
- **Cardiac toxicity**: case reports of bradycardia, QT prolongation and sick sinus syndrome (PMIDs 29717400, 25922742).
- **Lung injury**: drug-induced organizing pneumonia (PMID 37062732).

These signals matter for any new use, especially in a benign condition where the risk-benefit balance is far less favourable than in advanced cancer. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no literature and no documented mechanistic link to gingival fibromatosis. Crizotinib carries serious toxicities (liver, heart, lung), which are hard to justify in a benign gum condition without any supporting evidence.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking ALK, ROS1 or MET signalling to gingival fibromatosis
- The Health Canada package insert warnings and contraindications
- Mechanism-of-action data from DrugBank
- A review of whether a benign, non-life-threatening condition can justify the toxicity profile

Among the other predictions for this drug, only lung hilum carcinoma (rank 4) has anecdotal case-report support in ALK-positive and ROS1-positive lung cancer. It was flagged as a research question, and it may be a more practical starting point than gingival fibromatosis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

