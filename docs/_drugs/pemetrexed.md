---
layout: default
title: Pemetrexed
parent: Model Prediction Only (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: Toward Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multi-targeted antifolate chemotherapy that is widely marketed in Canada (14 licences). The Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **malignant peritoneal mesothelioma**, with **10 clinical trials** and **20 publications** linked to this prediction.
The evidence is mostly Phase 2 trials, case reports and reviews, and it is largely extrapolated from pleural mesothelioma, where pemetrexed plus cisplatin is the established first-line regimen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada licence records provided |
| Predicted New Indication | Malignant peritoneal mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (as scored; one completed Phase 2 trial in a mixed pleural/peritoneal population, no Phase 3 data for the peritoneal setting) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From the repurposing analysis, pemetrexed inhibits thymidylate synthase (TS), DHFR and GARFT. This blocks purine and pyrimidine synthesis in rapidly dividing tumour cells, and TS expression is linked to pemetrexed sensitivity in mesothelioma.

Peritoneal mesothelioma shares histology and TS-dependent biology with pleural mesothelioma. Pemetrexed plus cisplatin is the established first-line regimen for unresectable pleural disease, so antifolate activity in the peritoneum is mechanistically plausible. In practice, a pemetrexed–platinum doublet is commonly used off-label for the peritoneal form. Newer approaches, such as intraperitoneal chemotherapy and pressurised intraperitoneal aerosol chemotherapy (PIPAC), are under study.

The main caveat is that most supporting data come from pleural disease or from mixed pleural/peritoneal studies. Peritoneal mesothelioma is rare, so randomised peritoneal-specific data are scarce.

---

## Clinical Trial Evidence

Ten trials are linked to this prediction, listed below with the more relevant ones first.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed plus gemcitabine as front-line therapy in pleural or peritoneal mesothelioma; includes the peritoneal population directly |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomised: carboplatin, pemetrexed and bevacizumab with or without atezolizumab in peritoneal mesothelioma |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm: sintilimab and bevacizumab with pemetrexed and cisplatin in unresectable peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | Randomised: PIPAC plus systemic cisplatin-pemetrexed versus systemic chemotherapy alone, first-line (MESOTIP) |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed and imatinib in unresectable or metastatic mesothelioma; safety data on the combination |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Talazoparib maintenance after first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 (methoxyamine) with cisplatin and pemetrexed in advanced solid tumours or mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 with pemetrexed and cisplatin; peritoneal mesothelioma included in the dose-escalation cohort only |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Intraperitoneal versus intravenous chemotherapy after cytoreductive surgery and HIPEC; the role of pemetrexed is unclear |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin; withdrawn, so it provides no data |

---

## Literature Evidence

No randomised controlled trials were identified for the peritoneal setting. The table lists the most relevant publications, with studies of pemetrexed-based therapy first, followed by reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Clinical study (type not stated) | Jpn J Clin Oncol | Efficacy and safety of first-line pemetrexed plus cisplatin in advanced peritoneal mesothelioma, where no standard systemic regimen exists |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Rev Anticancer Ther | Retrospective evaluation of first-line pemetrexed plus cisplatin in peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multicentre study | Ann Surg Oncol | Treatment strategies and outcomes in a rare, heterogeneous peritoneal mesothelioma population |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Rep | Good response to pemetrexed-cisplatin, with a response again on rechallenge after progression |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series (2 patients) | J Immunother | Chemoimmunotherapy in two patients with platinum-nonresponsive peritoneal mesothelioma |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Case report | Pleura Peritoneum | Bidirectional chemotherapy to make initially unresectable disease eligible for surgery and HIPEC |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | Diagnostic and therapeutic pathway; cytoreductive surgery with HIPEC gives the best survival (median OS 34–92 months) in selected patients |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment overview; cytoreduction plus HIPEC is the preferred initial treatment in selected patients |
| [29423664](https://pubmed.ncbi.nlm.nih.gov/29423664/) | 2018 | Review | Ann Surg Oncol | Current management and future opportunities in peritoneal mesothelioma |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management of peritoneal mesothelioma |

---

## Canada Market Information

Fourteen licences are recorded. The first five are listed below. Dosage form and approved-indication text are blank in the records provided.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2463083 | Pemetrexed for Injection, USP | Not stated | Not stated |
| 2463091 | Pemetrexed for Injection, USP | Not stated | Not stated |
| 2515423 | Pemetrexed for Injection | Not stated | Not stated |
| 2517647 | Pemetrexed Disodium for Injection | Not stated | Not stated |
| 2528754 | Pemetrexed Disodium for Injection | Not stated | Not stated |

---

## Cytotoxicity

The Evidence Pack contains no toxicity data. The entries below reflect general knowledge of the drug class and should be checked against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate / antimetabolite) |
| Myelosuppression Risk | Moderate to high; hematologic toxicity (anaemia, neutropenia, thrombocytopenia) is the main dose-limiting toxicity. Folic acid and vitamin B12 supplementation reduces it (per NCT03537833). |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, renal function, liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pemetrexed–platinum is established in pleural mesothelioma and is already used in peritoneal disease. The peritoneal-specific evidence is still Phase 2 trials, retrospective series and case reports, with no randomised efficacy data yet. Several randomised Phase 2 trials are recruiting or suspended.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Verification of the Canadian label status. The pleural mesothelioma indication may already be approved, so the peritoneal setting could be an extension of an existing indication rather than true repurposing.
- Results from the ongoing randomised peritoneal trials (NCT05001880, NCT03875144, NCT06057935)
- Relevance grading for the trials still marked "pending"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

