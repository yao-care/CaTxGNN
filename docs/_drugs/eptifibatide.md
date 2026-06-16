---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is a cyclic peptide GPIIb/IIIa (αIIbβ3 integrin) antagonist, clinically established for reducing thrombotic events in acute coronary syndromes (ACS).
The TxGNN model assigns its highest repurposing score to **Rheumatoid Arthritis**, but this connection is currently supported by **no clinical trials** and **no published literature**.
Notably, among all predictions in this evidence pack, **Hemoglobinopathy (Sickle Cell Disease)** carries the most substantive evidence base — **1 Phase I/II randomized trial** and **4 publications** — and warrants prioritized clinical review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Coronary Syndrome / UA/NSTEMI (not registered in Canada) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack (flagged as a high-severity data gap). Based on established pharmacology, eptifibatide is a synthetic cyclic heptapeptide (KGD motif) that selectively antagonizes the GPIIb/IIIa (αIIbβ3 integrin) receptor on platelets — the final common pathway of platelet aggregation. It is delivered intravenously and is standard-of-care for ACS patients (UA/NSTEMI) undergoing percutaneous coronary intervention.

The mechanistic case for rheumatoid arthritis is highly theoretical. Platelets are increasingly recognized as participants in synovial inflammation: activated platelets can shed microparticles bearing αIIbβ3, P-selectin, and pro-inflammatory phospholipids that interact with immune effector cells in the joint. Blocking αIIbβ3 could theoretically dampen this platelet-driven inflammatory amplification. However, no direct preclinical or clinical studies have evaluated this hypothesis in RA specifically.

The TxGNN model's near-perfect score most likely reflects non-specific connectivity between immunovascular nodes in the underlying knowledge graph rather than a direct drug-target-disease relationship. This prediction should be treated as hypothesis-generating only — a starting point for basic science inquiry, not a clinical development priority.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Eptifibatide in Rheumatoid Arthritis.

---

## Literature Evidence

Currently no related literature available for Eptifibatide in Rheumatoid Arthritis.

---

## Canada Market Information

Eptifibatide is not currently registered in Canada. There are no DINs on file and no Health Canada-licensed products. Any clinical use in Canada would require a Special Access Programme (SAP) authorization.

---

## Safety Considerations

Safety profile data (key warnings, contraindications, drug interactions) was not available in this evidence pack. Please refer to the original product monograph (e.g., Integrilin®) and Health Canada's drug product database for comprehensive prescribing safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction rests entirely on model inference (L5), with no supporting preclinical or clinical evidence; the theoretical platelet-synovitis mechanism has not been tested in any published study, and eptifibatide's IV-only route is poorly suited to a chronic inflammatory condition like RA.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept**: In vitro or animal model studies examining eptifibatide's effect on platelet-synoviocyte interactions in RA models
- **MOA data gap closure**: Retrieve full mechanism of action and pharmacodynamic profile from DrugBank API (DG002)
- **Safety data gap closure**: Download and parse TFDA/Health Canada product monograph for warnings and contraindications (DG001)

---

> **⚠️ Higher-Priority Signal Identified**
>
> Within this same evidence pack, **Hemoglobinopathy / Sickle Cell Disease** (rank 7 by TxGNN, evidence level **L3**) has a substantially stronger evidentiary foundation and should be reviewed separately:
>
> | Trial | Phase | Status | Enrollment |
> |-------|-------|--------|------------|
> | [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase I/II RCT | Terminated | 13 |
>
> | PMID | Year | Type | Key Finding |
> |------|------|------|-------------|
> | [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase I Study | Safety/PD data confirmed in 4 SCA patients; αIIbβ3 inhibition rationale established |
> | [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot Study | Safety and efficacy assessed during acute pain episodes in SCD |
> | [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Pilot Study | Inflammatory marker reduction observed during acute SCD pain episodes |
> | [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In Vitro | Microfluidic model recapitulated SCD microvascular occlusion |
>
> The αIIbβ3-mediated platelet–sickle erythrocyte–endothelium interaction is mechanistically well-supported, and the existing clinical signals — though from small, early-phase studies — justify a formal **Research Question** evaluation with a dedicated evidence pack.

---

*This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

