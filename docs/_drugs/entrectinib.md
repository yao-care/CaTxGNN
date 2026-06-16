---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: From NTRK/ROS1-Positive Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib is a pan-TRK, ROS1, and ALK kinase inhibitor, developed internationally for the treatment of NTRK fusion-positive solid tumors and ROS1-rearranged malignancies.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, with a model confidence score of 98.58%.
However, only **2 clinical trials** were identified for this pairing — and critically, neither trial directly addresses MEN — meaning the biological rationale remains unvalidated at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Canada (no DINs on file) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on clinical trial descriptions within the pack, Entrectinib is a small-molecule inhibitor that selectively targets three receptor tyrosine kinases: TRK (encoded by NTRK1, NTRK2, NTRK3), ROS1, and ALK. Its established utility lies in tumors driven by gene fusions involving these kinases — including NTRK fusion-positive solid tumors across multiple histologies and ROS1-rearranged non-small cell lung cancer, as evidenced by the STARTRK-2 basket trial (NCT02568267, n=534).

Multiple Endocrine Neoplasia is a syndrome driven by germline alterations in **RET** (MEN2A/2B), **MEN1** (MEN1 syndrome), and **CDKN1B** (MEN4) — none of which are primary targets of Entrectinib's TRK/ROS1/ALK inhibitory profile. A minority of MEN-associated tumor subtypes, such as papillary thyroid carcinoma occurring in MEN2 patients, may occasionally harbor NTRK fusions, but NTRK rearrangement is not a defining molecular feature of MEN as a syndrome.

The high TxGNN prediction score most likely reflects indirect topological proximity in the knowledge graph: Entrectinib's connections to broad oncology pathways place it near multiple cancer-associated disease nodes, including MEN. This is a known limitation of graph-based predictions when the drug has wide coverage across cancer biology. The current evidence does not support a direct mechanistic hypothesis for Entrectinib in MEN.

---

## Clinical Trial Evidence

The following trials were retrieved for the Entrectinib × Multiple Endocrine Neoplasia query. **Neither trial directly targets MEN** — both represent semantic co-retrieval artifacts:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, Not Recruiting | 65 | Neoadjuvant Entrectinib targeting ROS1 combined with endocrine therapy in ROS1+ invasive lobular breast carcinoma. The word "endocrine" in the trial title caused a semantic cross-match with MEN; this trial has no MEN-specific design or cohort. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME basket trial exploring precision drug combinations in refractory solid tumors. Terminated early with only 2 participants enrolled; no MEN-specific design. No usable evidence. |

---

## Cytotoxicity

Entrectinib is an antineoplastic kinase inhibitor used for solid tumor treatment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Pan-TRK / ROS1 / ALK kinase inhibitor) — not conventional cytotoxic |
| Myelosuppression Risk | Low to Moderate — anemia and thrombocytopenia (Grade 3–4 ~5–8%) reported in basket trials; less severe than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (AST/ALT), serum creatinine, neurological assessment (cognitive function, dizziness — due to CNS penetration), QTc interval, body weight |
| Handling Protection | Standard oncology targeted therapy precautions; does not require cytotoxic drug handling protocols applied to conventional chemotherapy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
MEN is defined by RET/MEN1/CDKN1B germline mutations, none of which are targets of Entrectinib's TRK/ROS1/ALK inhibitory mechanism. The two retrieved clinical trials are semantically mismatched and provide no direct evidence for this indication. The TxGNN score reflects knowledge graph topology rather than a validated biological link.

**To proceed, the following is needed:**

- Systematic review of NTRK fusion prevalence in MEN-associated tumor subtypes (especially papillary thyroid carcinoma in MEN2 patients) to determine whether a molecularly-selected subpopulation exists
- Retrieval of complete mechanism of action data from DrugBank (DB11986) to support or refute the mechanistic hypothesis
- Review of FDA/EMA pharmacovigilance and registry data from approved Entrectinib indications for any MEN-related clinical signals
- If NTRK fusion frequency in a MEN-associated tumor subtype is confirmed to be clinically meaningful (> ~1%), escalate to a feasibility assessment for a molecularly-selected basket trial cohort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

