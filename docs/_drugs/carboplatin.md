---
layout: default
title: Carboplatin
parent: High Evidence (L1-L2)
nav_order: 157
evidence_level: L2
indication_count: 10
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy. The supplied Canadian licence records do not state its approved indication, so "ovarian cancer" in the title comes from general knowledge, not from the Evidence Pack. The TxGNN model predicts it may be effective for **female breast carcinoma**, mainly triple-negative disease. **50 clinical trials** and **20 publications** were retrieved, including several randomized Phase 2 and Phase 2/3 studies and one completed Phase 3 trial (GeparOcto) that includes a carboplatin arm. Whether carboplatin itself adds benefit in most of these trials still has to be confirmed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Health Canada records (generally used for ovarian cancer) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Carboplatin is a platinum agent. It forms DNA adducts and interstrand crosslinks that block DNA replication and trigger cell death. This is the known class mechanism and is not taken from the supplied MOA field.

Tumours with impaired homologous-recombination DNA repair are especially vulnerable to this damage. That includes BRCA1/2-associated breast cancers and many triple-negative breast cancers (TNBC). This explains why breast cancer is a plausible new use for a drug established in gynaecological cancers.

The clinical data support this most clearly in TNBC. Randomized Phase 2 neoadjuvant studies (for example GeparSixto, PMID 24794243, and NeoSTOP, PMID 33208340) tested adding carboplatin to standard chemotherapy. A 2014 meta-analysis (PMID 25247558) reports that carboplatin improves the pathological complete response rate in neoadjuvant TNBC treatment. The benefit is less clear in HER2-positive and hormone-receptor-positive disease. No Phase 3 trial in the supplied data confirms the benefit of adding carboplatin.

## Clinical Trial Evidence

Fifty trials were retrieved. The 10 most relevant are listed below. Many others are combination or basket studies in which carboplatin's contribution cannot be isolated.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Randomized: neoadjuvant weekly paclitaxel vs paclitaxel plus carboplatin in large operable or locally advanced TNBC; no results in the supplied data |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense neoadjuvant regimens in high-risk early breast cancer, one including carboplatin |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | Randomized: carboplatin added to neoadjuvant therapy in TNBC and HER2-positive early breast cancer |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3222 | Adjuvant AC-T vs AC-TH vs docetaxel/carboplatin/trastuzumab (TCH) in HER2-positive breast cancer; carboplatin sits inside a combination |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | First-line metastatic TNBC: nab-paclitaxel with gemcitabine or carboplatin vs gemcitabine/carboplatin |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomized: carboplatin vs docetaxel in metastatic breast cancer with BRCA mutation |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomized: neoadjuvant carboplatin plus docetaxel or paclitaxel, then AC, in stage I–III TNBC |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | Active, not recruiting | 120 | Neoadjuvant pembrolizumab plus carboplatin and docetaxel in TNBC |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Neoadjuvant bevacizumab, docetaxel and carboplatin in TNBC |
| [NCT00589238](https://clinicaltrials.gov/study/NCT00589238) | Phase 2 | Terminated | 16 | Randomized: weekly paclitaxel with or without carboplatin in basal-like breast cancer; stopped early, so limited weight |

NCT00585689 was left out. Its title describes bladder cancer, but its relevance note describes breast cancer, so the record is inconsistent.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2) | Lancet Oncol | GeparSixto: tested adding carboplatin to neoadjuvant therapy in TNBC and HER2-positive early breast cancer |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clin Cancer Res | NeoSTOP: anthracycline-free vs anthracycline-containing neoadjuvant carboplatin regimens in stage I–III TNBC |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3) | Eur J Cancer | BROCADE3: final overall survival for veliparib added to carboplatin/paclitaxel in BRCA-mutated advanced breast cancer |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Carboplatin and bevacizumab each improve the pathological complete response rate in neoadjuvant TNBC treatment |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | RCT (Phase 2) | Breast Cancer Res Treat | Single-agent carboplatin vs carboplatin plus everolimus in advanced TNBC |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: camrelizumab vs placebo plus neoadjuvant chemotherapy (platinum-containing) in early or locally advanced TNBC |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nat Commun | ARX788 plus pyrotinib vs the standard docetaxel/carboplatin/trastuzumab/pertuzumab regimen in HER2-positive disease |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 single-arm | Breast Cancer Res | Carboplatin plus bevacizumab in breast cancer brain metastases |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Evidence for synergy, efficacy and safety of paclitaxel-carboplatin in advanced breast cancer |
| [35837812](https://pubmed.ncbi.nlm.nih.gov/35837812/) | 2023 | Retrospective | Cancer Med | Grade 3/4 anaemia and pathological complete response by carboplatin dose in neoadjuvant TCHP (294 patients) |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2126680 | CARBOPLATIN INJECTION BP |
| 2125439 | CARBOPLATIN INJECTION |
| 2320371 | CARBOPLATIN INJECTION BP |

The supplied records do not list dosage form, manufacturer or approved indication text for these products.

## Cytotoxicity

The details below come from general knowledge of platinum chemotherapy, not from the supplied data. Please refer to the package insert warnings and precautions for authoritative information.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | High (thrombocytopenia is typically dose-limiting; neutropenia and anaemia are common) |
| Emetogenicity Classification | Moderate (higher at higher AUC doses) |
| Monitoring Items | CBC with differential, renal function, liver function, electrolytes; watch for neuropathy and hearing changes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

Health Canada warnings, contraindications and drug interactions were not available in the supplied data. One literature signal is relevant here: grade 3/4 anaemia is frequent with carboplatin-containing neoadjuvant regimens, and carboplatin dose reduction is discussed in that context (PMID 35837812).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized Phase 2 and Phase 2/3 studies, plus a supportive meta-analysis, point to a benefit from adding carboplatin in neoadjuvant TNBC, and carboplatin is already marketed in Canada. However, no Phase 3 result isolating carboplatin's effect is in the supplied data, and the benefit outside TNBC is less certain. Because carboplatin is myelosuppressive, use should stay within specialist oncology settings.

**To proceed, the following is needed:**
- Results from the ongoing Phase 3 trial NCT03168880 (paclitaxel with or without carboplatin in TNBC), and a check that the NCT00585689 record is correctly mapped
- Health Canada package insert warnings and contraindications, which are still missing
- Mechanism-of-action data from DrugBank
- Definition of the target population (TNBC, BRCA-mutated) and a monitoring plan for myelosuppression and anaemia
- Confirmation of the original approved indication from the Canadian product monographs

Other predicted indications for this drug are weaker. Adult germ cell tumour and endometrial mixed adenocarcinoma have some Phase 2 support. The remaining candidates have little or no direct evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

