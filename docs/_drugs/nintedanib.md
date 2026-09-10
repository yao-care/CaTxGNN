---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis/NSCLC to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib is a triple angiokinase inhibitor (VEGFR/FGFR/PDGFR) originally marketed for idiopathic pulmonary fibrosis and, in combination therapy, for non-small cell lung cancer — though this evidence pack itself does not record the original indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, with **0 clinical trials** and **1 publication** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (original_indications empty, original_moa flagged as data gap) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa: [Data Gap]). Based on the repurposing rationale provided, Nintedanib is a small-molecule triple angiokinase inhibitor that blocks VEGFR1-3, FGFR1-3, and PDGFRα/β — this characterization comes from the mechanistic rationale field, not from a verified DrugBank MOA record, and should be treated as supplementary background rather than confirmed evidence.

DFSP is characterized by a hallmark COL1A1-PDGFB fusion gene that drives constitutive PDGFR activation, and PDGFR inhibitors (notably imatinib) are already an established treatment option for this cancer. This provides a plausible mechanistic rationale for nintedanib's PDGFR-inhibitory activity to be relevant in DFSP. However, this connection is currently theoretical: no clinical trials, no ICTRP registrations, and only a single general review article touch on this drug-disease pair, and that review does not specifically discuss DFSP.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological research | General review of small-molecule PDGFR inhibitors in neoplastic disease; discusses PDGF/PDGFR biology and inhibitor classes but does not specifically address nintedanib in DFSP |

## Canada Market Information

Nintedanib is not currently marketed in Canada — no DIN records are available in this evidence pack (total_licenses: 0).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase/angiokinase inhibitor targeting VEGFR1-3/FGFR1-3/PDGFRα,β), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single non-specific review article (L4, mechanism-level only) with no clinical trials or registry entries for nintedanib in DFSP, and the drug is not currently marketed in this jurisdiction (0 DIN). A Blocking-severity data gap on regulatory safety warnings/contraindications (DG001) also prevents any S1 initial safety assessment.

**To proceed, the following is needed:**
- Regulatory label warnings and contraindications (DG001, Blocking — requires sourcing from official label/PDF)
- Confirmed mechanism of action via DrugBank API (DG002)
- Preclinical or case-level evidence specific to DFSP (current literature is a general PDGFR-inhibitor review, not DFSP-specific)
- Assessment of regulatory pathway, given the drug is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

