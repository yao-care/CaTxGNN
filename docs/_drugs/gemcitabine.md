---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Pancreatic Cancer & Solid Tumors to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a deoxycytidine nucleoside analogue antineoplastic agent, established globally as standard-of-care chemotherapy for pancreatic cancer, non-small cell lung cancer, bladder cancer, and other solid tumors.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a prediction score of 99.98%,
supported by **multiple Phase III clinical trials** and **20 publications** — and notably, the FDA approved gemcitabine + paclitaxel for HER2-negative metastatic breast cancer as early as 2004, making this one of the most evidence-rich repurposing candidates in the dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pancreatic cancer, NSCLC, bladder cancer, ovarian cancer (established global approvals; no Health Canada DINs captured in current dataset) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Gemcitabine (2′,2′-difluorodeoxycytidine) is a nucleoside analogue that exerts cytotoxicity via two complementary mechanisms after intracellular phosphorylation to its active triphosphate form (dFdCTP): (1) inhibition of ribonucleotide reductase, depleting the deoxyribonucleotide pool needed for DNA replication; and (2) incorporation into elongating DNA strands, causing "masked" chain termination that evades proofreading by DNA polymerase. This self-potentiating dual action makes gemcitabine especially potent against rapidly proliferating tumor cells. While formal MOA data is not available in the current dataset, the mechanistic rationale is well-established in published literature and referenced within the evidence pack's repurposing rationale.

Breast cancer — particularly triple-negative (TNBC) and HER2-positive subtypes — is characterized by high proliferative indices and heavy reliance on continuous DNA synthesis, making tumor cells directly vulnerable to gemcitabine's DNA replication blockade. The mechanistic synergy with taxanes is especially well-characterized: paclitaxel arrests cells at the G2/M boundary by stabilizing microtubules, while gemcitabine blocks S-phase DNA synthesis, creating a two-pronged attack on the cell cycle at distinct checkpoints. This complementary mechanism led to FDA approval of gemcitabine + paclitaxel for HER2-negative metastatic breast cancer in 2004, based on Phase III data demonstrating superior progression-free survival over paclitaxel monotherapy.

The breadth of clinical investigation in breast cancer is remarkable: multiple large Phase III trials (including trials with n=4,894 and n=1,206) have evaluated gemcitabine across neoadjuvant, adjuvant, and metastatic settings. Combinations with trastuzumab, pertuzumab, carboplatin, and bevacizumab have all been explored in Phase II studies, collectively indicating that gemcitabine's activity in breast cancer is not setting-specific but spans multiple clinical contexts. The TxGNN score of 99.98% accurately reflects this depth of biological and clinical corroboration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase III | Completed | 4,894 | Adjuvant trial in node-positive breast cancer comparing three regimens, one of which (dose-dense AC→paclitaxel+gemcitabine) directly evaluates gemcitabine in the adjuvant breast cancer setting; the largest gemcitabine breast cancer trial on record |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase III | Unknown | 1,206 | Large randomized neoadjuvant trial examining whether adding gemcitabine (or capecitabine) to docetaxel before AC chemotherapy (±bevacizumab) improves pathologic complete response (pCR) in palpable, operable breast cancer; includes biomarker analyses to predict pCR |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase III | Unknown | ~800 | tAnGo trial: randomized comparison of paclitaxel + epirubicin + cyclophosphamide ±gemcitabine as adjuvant therapy in ER/PgR-poor early breast cancer after surgery |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase III | Unknown | 800 | Randomized neoadjuvant trial of sequential epirubicin/cyclophosphamide → paclitaxel ±gemcitabine in poor-risk early breast cancer; directly targets the neoadjuvant setting |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase III | Terminated | 90 | Randomized comparison of gemcitabine+trastuzumab vs. capecitabine+trastuzumab in pretreated HER2-positive metastatic breast cancer; terminated early (underpowered, n=90) before reaching the primary endpoint |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase II/III | Completed | 191 | Randomized study of nab-paclitaxel+gemcitabine or nab-paclitaxel+carboplatin vs. gemcitabine+carboplatin as first-line treatment in triple-negative metastatic breast cancer; directly addresses the TNBC subtype |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase II | Unknown | 99 | Multi-center neoadjuvant trial evaluating docetaxel+gemcitabine in locally advanced breast cancer; assesses tumor response rate in the pre-surgical setting |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase II | Completed | 45 | Gemcitabine + trastuzumab + pertuzumab in previously treated HER2-positive metastatic breast cancer that progressed on prior anti-HER2 therapy (T-DM1, trastuzumab, or lapatinib); evaluates gemcitabine as a re-induction backbone |
| [NCT00462865](https://clinicaltrials.gov/study/NCT00462865) | Phase II | Terminated | 18 | Adjuvant gemcitabine/capecitabine + bevacizumab in high-risk early breast cancer with residual disease after neoadjuvant chemotherapy; terminated early due to slow accrual |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase II | Completed | 30 | Single-agent gemcitabine in women with metastatic breast cancer previously treated with doxorubicin and paclitaxel; one of the earliest studies establishing gemcitabine's single-agent activity in this setting |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Systematic Review (with RCT data) | Oncology | Comprehensive synthesis of gemcitabine+paclitaxel in metastatic breast cancer; 52% objective response rate (114/221 patients) across Phase II/III trials; provided the evidentiary basis supporting FDA approval of this combination |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I/II Clinical Study | Breast Cancer Res Treat | Phase I trial of mifepristone+carboplatin+gemcitabine in advanced breast cancer; rationale based on glucocorticoid receptor (GR) antagonism enhancing gemcitabine-induced apoptosis in GR-positive breast cancer cells |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase I Trial | Gynecol Oncol | Mirvetuximab soravtansine+gemcitabine in FRα-positive triple-negative breast cancer; determined MTD and recommended Phase 2 dose; confirms gemcitabine's continued role in novel combination strategies for TNBC |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Prospective Cohort / Phase II | Cancer Chemother Pharmacol | Biweekly docetaxel+gemcitabine+bevacizumab in pretreated HER2-negative metastatic breast cancer; demonstrated activity and acceptable tolerability as salvage chemotherapy |
| [15685824](https://pubmed.ncbi.nlm.nih.gov/15685824/) | 2004 | Translational/Clinical | Oncology | Characterized synergistic interactions between gemcitabine, trastuzumab, and platinum salts in HER2-overexpressing breast cancer cell lines; supported use of gemcitabine as a cardiotoxicity-sparing alternative to anthracyclines in HER2+ disease |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Narrative Review | Oncology | Review of gemcitabine combinations with anthracyclines and taxanes in advanced breast cancer; overall response rates up to 94% reported with triplet regimens, though toxicity management is critical |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Clinical Review | Oncology | Review of gemcitabine+platinum combinations in metastatic breast cancer after anthracycline/taxane failure; established gemcitabine+cisplatin or carboplatin as an active second-line doublet with meaningful response rates |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Semin Oncol | Early summary of ~20 Phase II trials confirming gemcitabine's single-agent activity (16–37% response rate) in metastatic breast cancer; combination regimens with platinums, taxanes, vinorelbine, and anthracyclines showed further enhanced activity |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology | Synthesis of gemcitabine+docetaxel combinations in metastatic breast cancer; standard dosing of gemcitabine 900–1,000 mg/m² on days 1+8 with docetaxel 75–100 mg/m² Q3W established as an active regimen |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase II / Dose-Finding | Tumori | Multi-center Phase II of weekly docetaxel+gemcitabine as first-line treatment for metastatic breast cancer; evaluated weekly scheduling to preserve quality of life while maintaining efficacy in anthracycline-pretreated patients |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Deoxycytidine nucleoside analogue (antimetabolite class) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are the primary dose-limiting toxicities; risk is amplified in combination regimens (e.g., with platinum, taxanes) |
| Emetogenicity Classification | Low to Moderate (gemcitabine monotherapy carries minimal emetic risk; combination regimens containing platinum or anthracyclines elevate emetogenicity to moderate–high) |
| Monitoring Items | CBC with differential before each cycle; liver function tests (AST, ALT, bilirubin); renal function (creatinine, eGFR); pulmonary status (dyspnea, radiographic changes if symptoms arise) |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) recommended for preparation and administration; appropriate PPE (gloves, gown, eye protection) required |

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug interactions) is not available in the current dataset. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large Phase III randomized trials (including n=4,894 and n=1,206) directly evaluate gemcitabine-containing regimens across breast cancer settings, and the FDA approved gemcitabine+paclitaxel for HER2-negative metastatic breast cancer in 2004 — establishing L1-level evidence that the TxGNN prediction correctly identifies a clinically validated repurposing opportunity. The primary guardrail is the absence of Health Canada regulatory records and incomplete safety documentation in the current dataset.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm Health Canada approval status — gemcitabine (brand: Gemzar; generics widely available) is likely approved in Canada but is absent from the current regulatory dataset; DIN search on the Health Canada Drug Product Database is required
- **Safety data gap closure**: Obtain product monograph from Health Canada or TFDA to complete the S1 safety screening (currently blocked by DG001 — key warnings/contraindications not captured)
- **MOA documentation** (DG002): Retrieve full MOA data from DrugBank API to formalize mechanism-of-action section and support indication-linkage analysis
- **Subtype stratification**: Define the target patient population more precisely (TNBC, HER2+, or HR+/HER2−), as optimal combination partners and dosing schedules differ materially across subtypes
- **Combination partner DDI review**: Assess drug-drug interaction profile for planned combination agents (paclitaxel, carboplatin, trastuzumab, bevacizumab) before clinical application
- **Dose-adjustment protocols**: Document renal and hepatic dose-reduction thresholds for Canadian clinical implementation guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

