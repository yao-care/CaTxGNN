---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib (brand name Xalkori) is a first-in-class ATP-competitive inhibitor of the ALK, ROS1, and MET receptor tyrosine kinases, originally developed and approved internationally for the treatment of ALK-positive and ROS1-rearranged non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival** with a model confidence score of **99.81%**; however, **no clinical trials** and **no disease-specific literature** have been identified to support this particular indication.
This is a purely model-driven hypothesis and requires preclinical mechanistic validation before any clinical consideration can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK/ROS1-positive Non-Small Cell Lung Cancer — inferred from published evidence (no Taiwan/Canada regulatory approval on record in current dataset) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 — Model prediction only; no clinical trials or published literature identified for this specific indication |
| Canada Market Status | Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack (data gap). Based on extensively published evidence in the retrieved literature, crizotinib is a small-molecule tyrosine kinase inhibitor that competitively binds the ATP site of three oncogenic receptor kinases — ALK (anaplastic lymphoma kinase), ROS1, and MET (c-Met). By blocking constitutive kinase activity arising from chromosomal rearrangements or amplification events, crizotinib suppresses downstream proliferative and survival signalling (including the MAPK/ERK and PI3K/AKT pathways) in susceptible tumour cells. This mechanism forms the basis of its approval in ALK-rearranged and ROS1-rearranged NSCLC, where it has demonstrated robust objective response rates.

Fibromatosis, Gingival is a rare, benign condition characterised by progressive, non-inflammatory overgrowth of gingival connective tissue driven largely by fibroblast dysregulation and extracellular matrix accumulation. The MET/HGF signalling axis is recognised as a promoter of fibroblast proliferation, migration, and tissue remodelling across multiple fibrotic contexts — this represents the most plausible mechanistic bridge the TxGNN knowledge graph may have identified between crizotinib and gingival fibromatosis. A 2023 study (PMID 36534968) further demonstrated that crizotinib can be repurposed to inhibit RIPK1-dependent cell death and inflammation, suggesting that its target profile extends beyond classical oncology contexts.

However, it must be emphasised that no direct evidence links ALK, ROS1, or MET activation to the established pathophysiology of gingival fibromatosis (which is predominantly associated with SOS1, VEGFR, and extracellular matrix gene variants). The TxGNN prediction likely reflects topological proximity in the biomedical knowledge graph rather than a validated biological mechanism. Mechanistic studies in gingival fibroblast models are the essential prerequisite before this hypothesis can be meaningfully assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Crizotinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Crizotinib in Fibromatosis, Gingival.

---

## Canada Market Information

No regulatory approvals for Crizotinib are currently recorded in the dataset for Canada. No Drug Identification Numbers (DINs) are on file. For current market authorisation status, refer directly to Health Canada's Drug Product Database.

---

## Cytotoxicity

Crizotinib is an antineoplastic agent approved for the treatment of ALK-positive and ROS1-positive NSCLC and therefore qualifies for cytotoxicity assessment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ATP-competitive inhibitor of ALK, ROS1, and MET receptor tyrosine kinases; not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low to moderate (neutropenia and anaemia reported in clinical trials; substantially lower myelosuppressive burden compared to conventional chemotherapy) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (neutropenia surveillance); liver function tests — ALT, AST, total bilirubin (hepatotoxicity risk, including fatal cases of fulminant liver failure reported); ECG with QTc interval (risk of QT prolongation, bradycardia, and ventricular arrhythmia); pulmonary function and imaging (interstitial lung disease / organising pneumonia surveillance) |
| Handling Protection | Please refer to the package insert warnings and precautions for cytotoxic drug handling requirements |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug-drug interaction data are not available in the current evidence pack. Based on published literature retrieved in this pack, clinically important safety signals include: **hepatotoxicity** (including fatal fulminant liver failure, PMID 26898609), **cardiotoxicity** (QT prolongation, bradycardia, ventricular arrhythmia, pericarditis, PMID 29717400), **interstitial lung disease / pneumonitis** (PMID 37062732), and **drug-induced skin reactions** such as erythema multiforme (PMID 25994067). These signals should be reviewed against the full prescribing information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN model confidence score (99.81%), there is currently zero supporting evidence for crizotinib in gingival fibromatosis — no clinical trials, no case reports, and no preclinical studies. The biological plausibility rests on an unvalidated hypothesis involving MET/HGF signalling in fibroblast biology, and advancing this candidate without foundational mechanistic data would not meet the minimum standard required for a drug-repurposing programme.

**To proceed, the following is needed:**

- **Mechanistic validation:** Determine whether ALK, ROS1, or MET are expressed or activated in gingival fibroblasts from fibromatosis patients; assess whether crizotinib suppresses fibroblast proliferation and matrix production in vitro
- **Knowledge graph path review:** Examine the specific TxGNN network path driving this prediction to identify which intermediate nodes (targets, pathways, or biological processes) connect crizotinib to gingival fibromatosis — this will clarify whether the link is mechanistically credible
- **MOA documentation:** Retrieve full DrugBank entry for DB08865 to close the current data gap and support or refute the mechanistic rationale
- **Safety dossier completion:** Download and parse the Xalkori prescribing information to populate key warnings, contraindications, and drug-interaction data before any safety evaluation can proceed
- **Canada/Taiwan regulatory clarification:** Confirm whether Crizotinib holds any approved indication in Canada (Health Canada DPD) or Taiwan (TFDA) to correctly characterise regulatory starting point
- **Orphan disease context:** Evaluate whether gingival fibromatosis qualifies for orphan drug designation pathways, which may alter the evidentiary threshold required for repurposing viability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

