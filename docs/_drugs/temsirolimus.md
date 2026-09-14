---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Temsirolimus (Torisel) is an intravenous mTOR inhibitor originally developed and approved for advanced renal cell carcinoma. TxGNN predicts potential efficacy in **liposarcoma**, supported by **5 clinical trials** (2 using temsirolimus directly, 3 using mechanistically related mTOR/pathway inhibitors) and **1 review article**, but no head-to-head randomized controlled data exist for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in Evidence Pack (drug not marketed in Canada). Based on general pharmacological knowledge, temsirolimus was originally approved for advanced renal cell carcinoma. |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the Evidence Pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, temsirolimus is an ester analog of rapamycin (a rapalog) that selectively inhibits mTOR complex 1 (mTORC1), blocking downstream signaling (S6K1, 4E-BP1) that drives cell-cycle progression and angiogenesis. It is administered intravenously and was originally approved for advanced renal cell carcinoma, a cancer with frequent PI3K/AKT/mTOR pathway activation.

Liposarcoma — particularly the dedifferentiated and myxoid subtypes — is also characterized by frequent PI3K/AKT/mTOR pathway activation and, in some subtypes, CDK4/MDM2 co-amplification. This shared pathway dependency provides a plausible mechanistic bridge between the original indication (renal cell carcinoma) and the predicted new indication (liposarcoma): both tumor types can depend on mTOR-driven proliferative signaling, which temsirolimus directly targets.

Supporting this rationale, two trials in the evidence set used temsirolimus itself in sarcoma populations (NCT00949325, NCT01614795), and three additional trials used mechanistically related mTOR-pathway inhibitors (sirolimus, ridaforolimus, everolimus) in liposarcoma/sarcoma populations. However, all available trials are single-arm, non-randomized, Phase 1/2 studies — none directly confirm a survival or progression-free-survival benefit for temsirolimus specifically in liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin in recurrent advanced soft tissue/bone sarcoma, including liposarcoma; dose-finding and efficacy study. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Temsirolimus + cixutumumab (anti-IGF-1R mAb) in pediatric recurrent/refractory solid tumors including sarcoma. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus (mTOR inhibitor, same class) + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor AP23573) in advanced sarcoma; large single-arm study. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (mTOR inhibitor) in dedifferentiated liposarcoma and leiomyosarcoma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Review of targeted treatments for rare connective tissue tumors and sarcomas, classifying molecular subgroups and associated targeted therapy strategies. |

---

## Cytotoxicity

Temsirolimus is an antineoplastic agent (mTOR-inhibitor class, used in oncology for renal cell carcinoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low to Moderate (class-associated anemia and thrombocytopenia reported; less pronounced than conventional cytotoxics) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, renal function, fasting glucose and lipid panel (mTOR inhibitors associated with hyperglycemia/hyperlipidemia), pulmonary symptoms (interstitial lung disease risk with rapalogs) |
| Handling Protection | Not classified as a cytotoxic hazardous drug requiring special cytotoxic handling procedures; standard oncology parenteral drug handling precautions apply |

Please refer to the package insert warnings and precautions for definitive toxicity and monitoring guidance, as formal TFDA/Canadian label data has not yet been obtained for this Evidence Pack (see blocking data gap below).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal label warnings, contraindications, and drug-drug interaction data could not be retrieved for this Evidence Pack (data gap DG001, severity: Blocking). This gap must be resolved before any S1 safety-stage evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Mechanistic rationale and early-phase clinical signal (including two trials using temsirolimus directly in sarcoma populations) are encouraging, but all supporting evidence is non-randomized, single-arm, Phase 1/2 data (Evidence Level L2). Combined with a Blocking-severity data gap on TFDA/label safety information (DG001), the candidate cannot yet advance past the research-question stage.

**To proceed, the following is needed:**
- Obtain TFDA/Health Canada label warnings and contraindications (resolves DG001)
- Obtain confirmed mechanism-of-action documentation from DrugBank (resolves DG002)
- Identify or commission a randomized/controlled study of temsirolimus specifically in liposarcoma to confirm efficacy signal beyond single-arm data
- Assess route/formulation compatibility (temsirolimus is IV-only; confirm feasibility for target population)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

