---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Gastrointestinal Cancer to Osteoclastic Giant Cell Tumor of Pancreas

## One-Sentence Summary

Mitomycin (Mitomycin C) is a classic antineoplastic antibiotic historically used in combination chemotherapy regimens such as FAM (5-Fluorouracil + Adriamycin + Mitomycin) for gastrointestinal cancers including gastric and pancreatic cancer, and intravesically for bladder cancer.
The TxGNN model predicts it may be effective for **Osteoclastic Giant Cell Tumor of Pancreas**, an extremely rare non-epithelial pancreatic malignancy of osteoclastic origin.
However, there are currently **0 clinical trials** and **0 publications** directly supporting this specific indication — this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (Mitomycin is not currently approved in Canada) |
| Predicted New Indication | Osteoclastic Giant Cell Tumor of Pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on contextual information in the repurposing rationale, Mitomycin C is a broad-spectrum DNA cross-linking alkylating agent (antitumor antibiotic) produced by *Streptomyces caespitosus*. It exerts cytotoxicity by forming covalent interstrand and intrastrand crosslinks in DNA, inhibiting replication in actively dividing cells. This mechanism is theoretically applicable to any rapidly proliferating malignancy.

Osteoclastic giant cell tumor of the pancreas is an extremely rare non-epithelial neoplasm characterized by osteoclast-like multinucleated giant cells of mesenchymal/osteoclastic differentiation — biologically distinct from the more common pancreatic ductal adenocarcinoma. Its proliferation kinetics and molecular drivers differ substantially from epithelial pancreatic cancers, making the mechanistic match with Mitomycin C uncertain. While MMC has a historical role in the FAM regimen (5-FU + Adriamycin + Mitomycin) used in 1980–90s pancreatic cancer treatment, this experience pertains to adenocarcinoma histology, not osteoclastic subtypes.

Notably, all 10 TxGNN top predictions for Mitomycin cluster within pancreatic cancer subtypes. This likely reflects the drug's historical use in pancreatic cancer chemotherapy regimens being encoded in the knowledge graph. The high prediction score (99.86%) represents the model's structural confidence based on graph topology — not clinical efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mitomycin in osteoclastic giant cell tumor of pancreas.

---

## Literature Evidence

Currently no related literature available for Mitomycin in osteoclastic giant cell tumor of pancreas.

---

## Canada Market Information

Mitomycin is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on record with Health Canada. This means there is no approved indication, no available dosage form, and no Canadian label information to draw upon for safety or dosing guidance.

---

## Cytotoxicity

Mitomycin C qualifies as an antineoplastic agent based on its mechanism of action (DNA cross-linking alkylation), its historical use in cancer combination chemotherapy, and its class membership as an antitumor antibiotic. The cytotoxicity section is therefore required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antitumor antibiotic / Alkylating agent (bifunctional) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No safety data is available in this Evidence Pack for Mitomycin. Health Canada package insert data, TFDA label warnings, contraindications, and drug interaction records were not retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Osteoclastic giant cell tumor of the pancreas is an extremely rare, non-epithelial malignancy with no clinical trial or literature evidence supporting Mitomycin C use. This is a pure model prediction (L5), and the biological mismatch between MMC's DNA cross-linking mechanism and the osteoclastic cell lineage further reduces the plausibility of direct applicability. Additionally, Mitomycin C is not currently marketed in Canada, and all safety information in this Evidence Pack is unavailable.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank (DG002: High severity gap)
- Health Canada / TFDA package insert for safety warnings and contraindications (DG001: Blocking gap)
- Preclinical data (in vitro or animal models) demonstrating MMC activity against osteoclastic giant cell tumor specifically
- Histopathological and molecular profiling data for this tumor subtype to assess DNA replication dependency (Ki-67 index, proliferation markers)
- Review of the broader pancreatic prediction cluster — notably, **Malignant Exocrine Pancreas Neoplasm** (Rank 8, L4 evidence, Stage S1: Research Question) has historical literature support for MMC in the FAM regimen and is the most clinically actionable of the 10 predictions; a focused evaluation of this indication should be prioritized alongside bladder cancer HIPEC contexts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

