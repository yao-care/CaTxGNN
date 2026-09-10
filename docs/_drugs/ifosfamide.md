---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Soft Tissue Sarcoma/Testicular Carcinoma to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an oxazaphosphorine alkylating agent whose established clinical use covers soft tissue sarcoma and testicular carcinoma.
The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**,
with **8 clinical trials** and **20 publications** currently supporting this direction — largely reflecting decades of real-world combination-chemotherapy use rather than a novel hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma, testicular carcinoma (per literature review PMID 3286879; Health Canada label data unavailable — drug not marketed in Canada) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available (Data Gap). Based on known information, ifosfamide is a cyclophosphamide analog of the oxazaphosphorine alkylating class; it requires hepatic and intratumoral bioactivation by CYP3A4/CYP2C9/CYP2B6 to its active metabolite 4-hydroxy-ifosfamide, which then forms DNA cross-links and triggers cytotoxicity in rapidly dividing cells. This is a broad-spectrum cytotoxic mechanism rather than a tissue-specific one.

Breast tumor tissue itself expresses CYP3A4/CYP2C9/CYP2B6 (PMID 14970873) and demonstrable ifosfamide-induced DNA damage has been measured directly in both breast tumor tissue and peripheral lymphocytes of breast cancer patients (PMID 11138456), supporting local drug activation within the tumor microenvironment rather than reliance on systemic exposure alone.

Importantly, this is not an exploratory "old drug, new use" hypothesis in the strict sense: ifosfamide-containing regimens (with vinorelbine, epirubicin, paclitaxel, etoposide, mitoxantrone, etc.) have already been used clinically as second-line/salvage therapy in anthracycline-resistant and refractory metastatic breast cancer for over three decades, as reflected in the literature evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | High-dose chemotherapy + peripheral stem cell transplant vs. optimized conventional-dose chemotherapy in metastatic breast cancer |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin/cyclophosphamide/etoposide and ifosfamide/carboplatin/taxol with autologous stem cell support in advanced cancer |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line chemotherapy in metastatic breast cancer |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | Paclitaxel/carboplatin vs. ifosfamide/paclitaxel in carcinosarcoma of the uterus, fallopian tube, peritoneum or ovary — **note: this trial's population is gynecologic carcinosarcoma, not breast carcinoma; likely an evidence-mapping mismatch worth manual verification** |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Repeated high-dose chemotherapy + double autologous bone marrow transplant + Samarium-153 in stage IV breast cancer |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid high-throughput drug screening to select chemotherapy in refractory solid tumors |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Chemotherapy + peripheral stem cell transplant + activated T-cell therapy in stage IV breast cancer |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | Intensive-dose topotecan/ifosfamide-mesna/etoposide (TIME) followed by autologous stem cell rescue in metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | RCT/Phase 2 | Cancer | Paclitaxel (24-hr infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma |
| [8711499](https://pubmed.ncbi.nlm.nih.gov/8711499/) | 1996 | Randomized Phase 2 (n=357) | Seminars in Oncology | Epirubicin + ifosfamide maintenance vs. treatment interruption in metastatic breast cancer; 45% overall response |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Cohort | Cancer Chemotherapy and Pharmacology | Epirubicin + ifosfamide in refractory breast cancer and other metastatic solid tumors (n=58, 23 breast) |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Cohort | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Cohort | Journal of Clinical Oncology | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Cohort | Journal of Chemotherapy | Ifosfamide/mesna/epirubicin (IMEpi) as second-line therapy; overall response rate 50% |
| [10602907](https://pubmed.ncbi.nlm.nih.gov/10602907/) | 1999 | Cohort | Cancer Chemotherapy and Pharmacology | Ifosfamide, carboplatin, etoposide (ICE) in metastatic/refractory breast cancer after prior chemotherapy failure |
| [26030252](https://pubmed.ncbi.nlm.nih.gov/26030252/) | 2015 | Review | Archives of Pathology & Laboratory Medicine | Metaplastic carcinoma of the breast — rare, aggressive subtype with poor response to standard therapy |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Case series | Current Problems in Cancer | Metaplastic breast cancer treated with ifosfamide-based chemotherapy; literature on first-line use remains scarce |
| [3286879](https://pubmed.ncbi.nlm.nih.gov/3286879/) | 1988 | Review | Journal of the National Cancer Institute | Comprehensive review of ifosfamide activity across tumor types, including sarcoma and testicular carcinoma |

---

## Cytotoxicity

Ifosfamide is a well-established cytotoxic chemotherapy agent (oxazaphosphorine alkylating class, cyclophosphamide analog); the following reflects standard oncology knowledge for this drug class, supplemented where the evidence pack provides direct support (DrugBank toxicity data itself is a Data Gap, DG002).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (oxazaphosphorine alkylating agent) |
| Myelosuppression Risk | High — dose-limiting neutropenia/thrombocytopenia is consistently reported across the trial evidence above (e.g., regimens combining ifosfamide with carboplatin/etoposide required G-CSF/thrombopoietin support per NCT00003597, NCT00187109) |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential, renal function (nephrotoxicity risk), urinalysis (hemorrhagic cystitis — multiple trials in this pack pair ifosfamide with mesna uroprotection), neurological status (encephalopathy risk) |
| Handling Protection | Cytotoxic drug handling precautions required per standard hazardous drug protocols |

---

## Safety Considerations

Please refer to the package insert for safety information — TFDA/Health Canada label warnings, contraindications, and drug interaction data are not currently available in this evidence pack (Data Gap DG001, flagged Blocking severity; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
20 publications spanning 1988–2024, including an RCT/Phase 2 study and multiple cohort studies, document real clinical activity of ifosfamide-based combination regimens in metastatic and refractory breast cancer — this is corroborating evidence for established combination-chemotherapy practice rather than a speculative new hypothesis. However, formal safety documentation (label warnings/contraindications) is still missing, and the drug currently has no Canadian market authorization (0 DINs).

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph warnings and contraindications (DG001, Blocking — required before S1 safety screening can proceed)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Since ifosfamide is not marketed in Canada, clarification of the access pathway (e.g., Special Access Programme) needed for any repurposing pathway
- Manual verification of NCT00954174 — its stated population is uterine/fallopian tube/ovarian carcinosarcoma, not breast carcinoma, suggesting a possible evidence-mapping error that should be corrected before this trial is counted toward the breast cancer evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

