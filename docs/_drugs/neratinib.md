---
layout: default
title: Neratinib
parent: High Evidence (L1-L2)
nav_order: 649
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Neratinib: predicted new indication Progesterone-receptor positive breast cancer (evidence level L2). Approved use: HER2 positive breast carcinoma"
monitor_inn: "Neratinib"
predicted_indications: ["synovium cancer", "tenosynovial giant cell tumor", "malignant giant cell tumor", "tenosynovial giant cell tumor, localized type", "fibroblastic neoplasm", "kidney fibrosarcoma"]
---

# Neratinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Neratinib: From HER2-Positive Breast Carcinoma to Progesterone-Receptor Positive Breast Cancer
{: .text-alpha }

## One-Sentence Summary

Neratinib is an irreversible tyrosine kinase inhibitor originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**,
with **2 registered clinical trials** (1 recruiting, 1 withdrawn) and **12 publications** currently supporting this direction.
This is largely a subpopulation of the existing indication rather than a wholly new disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2 positive breast carcinoma |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, neratinib is an irreversible pan-HER tyrosine kinase inhibitor (targeting EGFR/HER1, HER2 and HER4), and its efficacy in HER2-positive breast cancer has been established.

Many HER2-positive breast cancers are also hormone receptor positive (HR+/HER2+), including progesterone-receptor positive tumours, so the approved indication already overlaps with this population. Preclinical and early clinical data also suggest that HER2 blockade can reverse endocrine resistance through ER/HER2 crosstalk, which supports combining neratinib with endocrine therapy.

The high TxGNN score is consistent with this biology. The extended adjuvant evidence (ExteNET, PMID 26874901) comes from a HER2-positive population with a pre-specified HR+ subgroup benefit. The related entry "progesterone-receptor negative breast cancer" (score 99.67%) is likewise mostly a subpopulation of the approved indication, and "breast tumor luminal A or B" is supported mainly in mutation-selected settings (e.g., HER2-mutant disease).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib plus an aromatase inhibitor and trastuzumab for 24 weeks in ER-positive, HER2-positive cancers; no results yet |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Withdrawn | 0 | Neratinib plus fulvestrant in previously treated HR-positive, HER2-negative metastatic breast cancer; withdrawn before enrolment, so no evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT (Phase 3, ExteNET) | Lancet Oncol | 12 months of neratinib after trastuzumab-based adjuvant therapy in early-stage HER2-positive breast cancer |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT (I-SPY 2) | N Engl J Med | Adaptive phase 2 neoadjuvant trial of neratinib added to standard chemotherapy in high-risk early breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Guideline | J Natl Compr Canc Netw | NCCN breast cancer updates, including CDK4/6 inhibitors and extended adjuvant therapy |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohort | Breast Cancer Res Treat | Use and tolerance of adjuvant neratinib in HR+/HER2+ early breast cancer; GI side effects often lead to discontinuation |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | Current treatment trends in HR+/HER2+ breast cancer, including hormone plus anti-HER2 approaches |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Review | Clin Breast Cancer | Expert roundtable on clinical developments in HER2-positive breast cancer |
| [41499317](https://pubmed.ncbi.nlm.nih.gov/41499317/) | 2026 | Observational | Oncology | Prescribing trends of adjuvant neratinib in HR+/HER2+ breast cancer in current practice |
| [41886605](https://pubmed.ncbi.nlm.nih.gov/41886605/) | 2026 | Preclinical | Cancer Res | BRD8/EP400 chromatin module mediating anti-HER2 response in HR+/HER2+ breast cancer |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohort (in silico) | Breast Cancer Res | Targetable ERBB2 mutations as an adverse prognostic marker in ER+ lobular breast carcinoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02490536 | NERLYNX | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (irreversible pan-HER tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the literature highlights gastrointestinal tolerability as a key concern |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records; the first 20 reviewed include many Major-level interactions, notably with:
  - Acid-reducing agents: famotidine, ranitidine, cimetidine, and proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole)
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Clotrimazole
- Moderate interactions include loperamide, antacids (magnesium oxide, aluminum hydroxide, calcium carbonate), empagliflozin and naldemedine.
- Literature notes that significant gastrointestinal side effects often lead to treatment discontinuation (PMID 39153126).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Neratinib is already marketed in Canada for HER2-positive breast cancer, and a Phase 3 RCT (ExteNET) shows benefit in HER2-positive disease, including an HR+ subgroup. Direct evidence for progesterone-receptor positive disease specifically is limited to one small, recruiting Phase 2 trial without results, so this is best viewed as a subpopulation of the existing indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Results from NCT04886531 and PR-stratified analyses of ExteNET
- A plan for managing diarrhoea and acid-suppressant interactions, which are the main practical concerns
- Cytotoxicity and handling details from the package insert

**Other predictions:** The lower-ranked predictions (e.g., normal breast-like subtype, synovium cancer, tenosynovial giant cell tumour, malignant giant cell tumour, fibroblastic neoplasm, kidney fibrosarcoma) have no trials or literature and no plausible HER-pathway link; the recommendation for these is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

