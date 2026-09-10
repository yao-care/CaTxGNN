---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: From Gastrointestinal Stromal Tumor to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib is a switch-control KIT/PDGFRA tyrosine kinase inhibitor approved for advanced gastrointestinal stromal tumor (GIST). The TxGNN model predicts a possible link to **Multiple Endocrine Neoplasia (MEN)**, but this direction is currently supported by **0 clinical trials** and **0 relevant publications** — the prediction stands on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced gastrointestinal stromal tumor (GIST) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ripretinib is a switch-control kinase inhibitor targeting KIT and PDGFRA, approved for fourth-line treatment of advanced GIST. Detailed, sourced mechanism-of-action data (e.g., binding kinetics, downstream pathway detail) is not available in this evidence pack — a flagged high-severity data gap.

MEN syndromes (MEN1/MEN2) are driven primarily by mutations in the *MEN1* gene or the *RET* proto-oncogene, neither of which overlaps with the KIT/PDGFRA pathway ripretinib targets. There is no known pharmacological or mechanistic bridge between KIT/PDGFRA inhibition and MEN pathogenesis, and no clinical or literature evidence has been found to support such a link.

Given this, the prediction should be treated as a knowledge-graph association rather than a mechanistically grounded hypothesis. It does not currently meet the bar for further pharmacological reasoning without additional target-pathway data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ripretinib is not currently marketed in Canada — no Drug Identification Numbers (DINs) are on record, and no product licenses were found.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (KIT/PDGFRA switch-control tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. Note: local product labeling (warnings/contraindications) could not be retrieved for this evidence pack, which is a blocking gap for any safety pre-screen.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No mechanistic, clinical, or literature evidence supports a KIT/PDGFRA–MEN connection; the prediction rests solely on the TxGNN score (L5, S0). Other top-ranked candidates in this same prediction batch (e.g., infectious bovine rhinotracheitis, malignant catarrh) are veterinary/non-human diseases, indicating this batch likely contains substantial knowledge-graph ontology noise — reinforcing caution before advancing rank 1.

**To proceed, the following is needed:**
- Verified mechanism-of-action data for ripretinib (DrugBank API query, DG002)
- Local product monograph / warnings and contraindications (DG001, blocking — required before any S1 safety screen)
- Targeted literature and clinical trial search specifically on ripretinib and MEN or related endocrine tumor pathways
- Independent mechanistic assessment of any indirect KIT/PDGFRA–endocrine tumor pathway link before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

