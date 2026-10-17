---
layout: default
title: Enzalutamide
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Enzalutamide: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "benign neoplasm of prostate", "prostate phyllodes tumor"]
---

# Enzalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor inhibitor, originally used to treat prostate cancer.
The TxGNN model predicts it may be effective for **prostate cancer/brain cancer susceptibility**, a genetic susceptibility category that overlaps with the approved indication.
No clinical trials or publications directly support this top-ranked prediction, so it rests on **model prediction only**. The strongest evidence in the data compiled for this report (**38 trials** and **20 publications** under "prostate neoplasm") concerns the already-approved prostate cancer indication, not a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (the Canadian licence record has no indication text, so this comes from the knowledge graph: prostate cancer, familial prostate carcinoma, prostate carcinoma) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only for the top-ranked indication) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, enzalutamide is an androgen receptor (AR) inhibitor. It blocks ligand binding, nuclear translocation and DNA binding of the receptor, and this is the basis of its efficacy in prostate cancer.

The predicted indication, "prostate cancer/brain cancer susceptibility," is a genetic susceptibility category that overlaps with the approved prostate cancer indication. This overlap probably explains the very high score (99.71%). No mechanistic evidence links androgen receptor inhibition to brain cancer, so the prediction should not be read as a new brain cancer use.

The other top-ranked predictions are similar. Prostate leiomyoma, fibroma of prostate, benign prostate phyllodes tumor and prostate phyllodes tumor are rare prostatic tumors with no trials or publications. Brenner tumor is an ovarian tumor with no clear link to AR inhibition, and its score is likely a graph-propagation artifact. Benign neoplasm of prostate has a plausible AR-dependence rationale, but only prostate cancer literature supports it, and the anti-androgen toxicity profile makes benefit-risk unfavourable for benign disease without dedicated studies.

---

## Clinical Trial Evidence

The top-ranked prediction has no registered trials. The table below shows the most relevant trials from the closely related categories "male reproductive organ cancer" and "prostate neoplasm". All of them study **prostate cancer, the approved indication**, so they are not evidence for a new use.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Phase 3 | Active, not recruiting | 1125 | ENZAMET: enzalutamide vs conventional non-steroidal anti-androgen with first-line ADT in metastatic prostate cancer |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | Active, not recruiting | 600 | MEVPRO-1: mevrometostat + enzalutamide vs enzalutamide or docetaxel in mCRPC after abiraterone |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) | Phase 3 | Recruiting | 500 | Standard of care (including enzalutamide) ± 177Lu-PSMA-617 in poorly responding de novo mHSPC |
| [NCT02987543](https://clinicaltrials.gov/study/NCT02987543) | Phase 3 | Completed | 387 | PROfound: olaparib vs enzalutamide or abiraterone in mCRPC with HRR gene mutations |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Phase 3 | Terminated | 1244 | KEYNOTE-641: pembrolizumab + enzalutamide vs placebo + enzalutamide in mCRPC |
| [NCT06136624](https://clinicaltrials.gov/study/NCT06136624) | Phase 3 | Recruiting | 1310 | OMAHA-003: opevesostat vs abiraterone or enzalutamide in mCRPC |
| [NCT03641560](https://clinicaltrials.gov/study/NCT03641560) | Phase 4 | Completed | 52 | Safety and efficacy of enzalutamide in Indian patients with docetaxel-pretreated mCRPC |
| [NCT06059118](https://clinicaltrials.gov/study/NCT06059118) | Phase 2 | Recruiting | 50 | APEX: DFMO and high-dose testosterone alternating with enzalutamide in mCRPC |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | Not yet recruiting | 26 | Dose optimization of enzalutamide in elderly patients with advanced prostate cancer |
| [NCT06228053](https://clinicaltrials.gov/study/NCT06228053) | Phase 2 | Recruiting | 53 | SX-682 (CXCR1/2 inhibitor) + enzalutamide in ARPI-resistant mCRPC |

---

## Literature Evidence

The top-ranked prediction has no publications. The table below lists key publications from the related "prostate neoplasm" category, all about the approved prostate cancer indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31329516](https://pubmed.ncbi.nlm.nih.gov/31329516/) | 2019 | RCT | J Clin Oncol | ARCHES: enzalutamide + ADT in metastatic hormone-sensitive prostate cancer |
| [29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/) | 2018 | RCT | N Engl J Med | PROSPER: enzalutamide in non-metastatic castration-resistant prostate cancer with rapidly rising PSA |
| [22894553](https://pubmed.ncbi.nlm.nih.gov/22894553/) | 2012 | RCT | N Engl J Med | AFFIRM: increased survival with enzalutamide after chemotherapy |
| [41124201](https://pubmed.ncbi.nlm.nih.gov/41124201/) | 2026 | RCT | N Engl J Med | EMBARK: improved survival with enzalutamide in biochemically recurrent prostate cancer |
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | RCT | N Engl J Med | Talazoparib + enzalutamide + ADT in metastatic prostate cancer |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Comparative | The Prostate | Real-world comparison of abiraterone, enzalutamide and apalutamide in mHSPC |
| [40439959](https://pubmed.ncbi.nlm.nih.gov/40439959/) | 2025 | Comparative | Adv Ther | Overall survival with apalutamide vs enzalutamide in mCSPC |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends Cancer | Treatment advances in advanced prostate cancer |
| [39275993](https://pubmed.ncbi.nlm.nih.gov/39275993/) | 2024 | Review | Expert Rev Anticancer Ther | Current uses and resistance mechanisms of enzalutamide |
| [38859590](https://pubmed.ncbi.nlm.nih.gov/38859590/) | 2024 | Preclinical | Adv Sci | Enzalutamide sensitizes CRPC cells to copper-mediated cell death |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02407329 | XTANDI | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (hormonal; androgen receptor inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Major-level interactions in the listed entries include bupropion, dolasetron and eliglustat. Many moderate-level interactions are also listed, for example famotidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, clarithromycin, aprepitant, loperamide, saxagliptin, linagliptin and empagliflozin.
- **Other considerations noted in the analysis**: seizure risk, fatigue and cardiovascular risk, plus CYP3A4/CYP2C8-related interactions. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (prostate cancer/brain cancer susceptibility) is supported by model score only, with no trials or publications, and no mechanism links androgen receptor inhibition to brain cancer. The strong Phase 3 evidence in the data concerns prostate cancer, the existing approved indication. It validates the model but is not a new repurposing opportunity.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clarification of what "prostate cancer/brain cancer susceptibility" means clinically, and whether any real new-use hypothesis exists
- Dedicated preclinical or clinical evidence for any candidate beyond prostate cancer, such as benign prostate neoplasms
- Indication text for the Canadian licence (DIN 02407329) to confirm the approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

