---
layout: default
title: Olaparib
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 1
---

# Olaparib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Olaparib: From an Unlisted Registered Indication to Female Breast Carcinoma

## One-Sentence Summary

Olaparib (Lynparza) is an oral PARP inhibitor marketed in Canada, but the supplied data does not list its original approved indication.
The TxGNN model predicts it may be effective for **female breast carcinoma**, and **50 clinical trials** and **20 publications** are linked to this direction.
The strongest support comes from Phase 3 RCTs (OlympiA and OlympiAD) in germline BRCA1/2-mutated, HER2-negative breast cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (the Canadian licence records contain no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 (based on the published Phase 3 RCTs OlympiA and OlympiAD) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. The explanation below comes from the published literature.

Olaparib inhibits PARP, an enzyme involved in repairing DNA single-strand breaks. Tumours with germline BRCA1/2 mutations cannot repair double-strand breaks by homologous recombination. Blocking PARP in these cells causes synthetic lethality, and the cancer cells die while normal cells are largely spared.

Breast cancers carrying BRCA1/2 mutations have exactly this repair defect. That is why the TxGNN prediction fits the clinical data. The pivotal trials enrolled patients with germline BRCA-mutated, HER2-negative disease, and the TxGNN score (0.99) agrees with those results.

The benefit is established only in this biomarker-defined group. Evidence in wider homologous-recombination-deficient (HRD) populations comes from Phase 2 data (TBCRC 048) and is still suggestive. Because the original indication is missing from the data, the Health Canada label should be checked to confirm whether breast cancer is already an approved use or a true new indication.

---

## Clinical Trial Evidence

The list below shows the 10 most relevant breast-cancer trials out of 50 retrieved. Most of them are early-phase combination studies, so the registered trials mainly support safety and early activity.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib alone or with durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Elacestrant added to olaparib versus olaparib alone in HR-positive, HER2-negative, gBRCA1/2-mutated advanced breast cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | AZD2281 (olaparib) in BRCA-mutated or triple-negative breast cancer and in ovarian cancer, measuring response rate and response markers |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | Active, not recruiting | 155 | Cediranib plus olaparib versus olaparib alone in recurrent triple-negative breast cancer and ovarian cancers |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib plus navitoclax in BRCA1/2- or PALB2-mutated triple-negative breast cancer and high-grade serous ovarian cancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiation therapy in triple-negative breast cancer |
| [NCT02208375](https://clinicaltrials.gov/study/NCT02208375) | Phase 1 | Active, not recruiting | 159 | Olaparib with vistusertib or capivasertib in recurrent endometrial, triple-negative breast and ovarian cancers |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC personalised pre-surgical treatment of high-risk breast cancer (olaparib likely one of several biomarker-guided options) |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib plus carboplatin in BRCA1/2 carriers and sporadic triple-negative breast and ovarian cancer; dose-finding and early activity |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Olaparib in Indian patients with platinum-sensitive relapsed ovarian cancer and metastatic breast cancer with germline BRCA1/2 mutation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib in BRCA1/2-mutated early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall-survival analysis; the first interim analysis had shown a significant improvement in invasive disease-free survival with 1 year of olaparib versus placebo |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib in metastatic breast cancer with a germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final overall survival versus physician's-choice chemotherapy, plus tolerability; median OS 19.3 vs 17.1 months (P = 0.513) |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up for survival and safety |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT (Phase 2–3) | Nature | PARTNER: neoadjuvant carboplatin-paclitaxel with or without olaparib in 559 patients with germline BRCA wild-type triple-negative breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 | J Clin Oncol | TBCRC 048: olaparib in metastatic breast cancer with somatic BRCA1/2 or other homologous-recombination gene mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 | Cancer Cell | I-SPY2: durvalumab plus olaparib plus paclitaxel raised pathologic complete response rates in HER2-negative stage II/III breast cancer |
| [34518313](https://pubmed.ncbi.nlm.nih.gov/34518313/) | 2021 | Phase 1b | Clin Cancer Res | Olaparib plus capivasertib in recurrent endometrial, triple-negative breast and ovarian cancer; dose expansion and response markers |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Target Oncol | Overview of PARP inhibitors (olaparib and talazoparib) for breast cancer |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2475200 | LYNPARZA |
| 2475219 | LYNPARZA |

---

## Cytotoxicity

Olaparib is an antineoplastic drug.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |

For myelosuppression risk, emetogenicity, monitoring items and handling protection, please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug in the queried source.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 RCTs (OlympiA and OlympiAD) support olaparib in germline BRCA-mutated, HER2-negative breast cancer, and the TxGNN prediction agrees with the established synthetic-lethality mechanism. The benefit is limited to this biomarker-defined group, so use must be restricted to confirmed BRCA-mutated patients.

**To proceed, the following is needed:**
- Obtain the Health Canada product monograph (warnings and contraindications), a blocking gap for safety screening.
- Confirm the approved indications on the Canadian label, to decide whether breast cancer is already approved or a true repurposing.
- Require BRCA testing before use; evidence in wider HRD populations is still Phase 2 only.
- Obtain DrugBank mechanism-of-action data to complete the mechanistic analysis.
- Review the 30 trials still pending relevance grading, especially the breast-specific Phase 2 trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

