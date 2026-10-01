---
layout: default
title: Tamoxifen
parent: Moderate Evidence (L3-L4)
nav_order: 873
evidence_level: L4
indication_count: 10
---

# Tamoxifen
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tamoxifen: From Breast Cancer to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is an estrogen-receptor-targeting hormone therapy, best known for breast cancer. The Canadian license data supplied here do not state an indication.
The TxGNN model predicts it may be effective for **mammary Paget disease**, but only **1 clinical trial** (which studies tamoxifen's side effects, not Paget disease efficacy) and **12 publications** (mostly case reports and retrospective data) are linked to this prediction. Direct evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (general knowledge of tamoxifen; not stated in the Canadian license data) |
| Predicted New Indication | Mammary Paget disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Tamoxifen is generally known as an estrogen receptor antagonist in breast tissue. Its efficacy in hormone receptor-positive breast cancer is well established, and mechanistically it may be applicable to mammary Paget disease.

Mammary Paget disease is usually associated with an underlying ductal carcinoma in situ (DCIS) or invasive ductal carcinoma, and many of these tumours are hormone receptor-positive. A tamoxifen benefit is therefore plausible through treatment of the associated breast cancer. It has not been shown for Paget disease itself.

The clinical hints are limited. One case report describes a response to tamoxifen in hormone receptor-positive *extramammary* Paget disease, which is a different condition. A case of extensive nipple Paget disease also reported a response to tamoxifen alongside radiotherapy. Other data are retrospective local-recurrence studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Medroxyprogesterone vs observation to prevent endometrial problems in postmenopausal women taking tamoxifen. Eligible patients included those with Paget's disease of the nipple. It addresses tamoxifen toxicity, not efficacy, so it is not direct evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-analysis | Breast Care | Compiled data on local recurrence after mastectomy vs breast-conserving surgery for Paget's disease. Total recurrence rate is 20-40%. |
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case report | Investigational New Drugs | Successful tamoxifen treatment of hormone receptor-positive metastatic extramammary Paget disease (a different condition). |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case report | Breast | Unusually extensive nipple Paget disease. A response was achieved with tamoxifen, plus radiotherapy for disease control. |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Case series | Br J Surg | 48 women with nipple Paget disease. Most had underlying DCIS or invasive carcinoma. Only one case was treated with tamoxifen. |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Cohort | Clin Breast Cancer | Paget disease of the nipple as local recurrence after breast-conservation treatment (2,181 women). |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case report | Il Giornale di Chirurgia | Male breast Paget disease. It can hide an invasive ductal cancer, and there are no standard guidelines. |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case report/review | Am Surg | A male case plus review of 32 published cases. |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case report | Arch Gynecol Obstet | Vulvar and breast Paget disease with synchronous underlying cancer. |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case report | Surgery Today | Synchronous bilateral breast cancer with Paget disease and invasive ductal carcinoma. |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case series | Niger J Clin Pract | 8 of 240 breast cancer patients in Benin City, Nigeria had Paget disease of the nipple-areola complex. |

No randomized trials are among these. Most papers describe the disease or its surgical management, and only the two case reports above link tamoxifen to a response.

---

## Canada Market Information

| License Number | Product Name |
|---------|------|
| 851973 | TEVA-TAMOXIFEN |
| 851965 | TEVA-TAMOXIFEN |
| 812404 | APO-TAMOX TAB 10MG |
| 812390 | APO-TAMOX TAB 20MG |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Endocrine therapy (selective estrogen receptor modulator), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but the supporting evidence is only case-level and retrospective, with no efficacy trial in mammary Paget disease. The one linked Phase 3 trial concerns tamoxifen toxicity and must not raise the evidence level.

Separately, the same prediction set includes breast carcinoma in situ and estrogen-receptor positive breast cancer, both L1 and Proceed with Guardrails. These are established uses of tamoxifen, so they confirm the model rather than offer new repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Hormone receptor status data in mammary Paget disease cohorts
- Studies that report tamoxifen-specific outcomes in Paget disease, including with underlying DCIS or invasive carcinoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

