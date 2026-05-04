---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Taxane Cytotoxic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (Taxotere) is a second-generation taxane cytotoxic agent belonging to the microtubule-stabilizing class of antineoplastic drugs, with well-established global use across multiple solid tumor types.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a score of **99.90%**, supported by **50 clinical trials** and **20 publications** — including several landmark Phase 3 randomized controlled trials — making this one of the most evidence-rich predictions in the repurposing dataset.
Although docetaxel currently has no registered Drug Identification Numbers (DINs) in Canada according to the regulatory data reviewed, the global clinical evidence for this indication is extensive and mature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Canadian DINs registered) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semi-synthetic taxane derived from the European yew tree (*Taxus baccata*). Its mechanism of action centers on binding to and stabilizing polymerized microtubules, preventing their depolymerization during cell division. This disrupts the dynamic equilibrium required for spindle formation, arrests tumor cells in the G2/M phase of the cell cycle, and ultimately triggers apoptosis. Because this mechanism targets the fundamental machinery of cell division rather than a specific molecular target, docetaxel is broadly active against rapidly proliferating cancer cells. The taxane class is distinct from other cytotoxic agents in that it *stabilizes* microtubules (rather than inhibiting polymerization like vinca alkaloids), which confers a unique activity profile that complements anthracycline-based regimens.

Breast cancer cells — particularly HER2-positive and triple-negative subtypes (TNBC) — are highly sensitive to taxane-class agents. This sensitivity arises in part because these subtypes have higher baseline mitotic rates and impaired checkpoint control, making them more vulnerable to G2/M blockade. Docetaxel has demonstrated consistent synergy when combined with trastuzumab (anti-HER2 monoclonal antibody), anthracyclines (doxorubicin, epirubicin), and capecitabine, enabling its use across neoadjuvant, adjuvant, and metastatic settings. In TNBC — a subtype with no hormonal or HER2-directed targets — taxane-based regimens represent a cornerstone of therapy, and the Gemcitabine + Docetaxel (GemDoc) combination has also been evaluated as a salvage option.

The TxGNN prediction of female breast carcinoma at rank #1 (score 99.90%) is strongly corroborated by the available evidence: multiple completed Phase 3 randomized trials with thousands of participants (including NSABP B-27 with N=2,411 and FNCLCC/PACS01 with N=3,010) have established docetaxel's efficacy and safety in this indication. Globally, docetaxel is already approved for breast cancer by the FDA, EMA, and other major regulatory bodies. The absence of Canadian DINs in the current dataset warrants investigation but does not diminish the scientific rationale or global evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Landmark randomized trial comparing preoperative AC vs AC + docetaxel (neoadjuvant and/or adjuvant) in operable Stage II/III breast cancer; evaluated pathologic complete response and survival outcomes |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | Completed | 3,010 | Docetaxel 75 mg/m² + epirubicin 75 mg/m² vs FEC 100 in node-positive breast cancer; sequential trastuzumab arm added for HER2+++ patients; large multicenter randomized study |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1,384 | EC×4 → docetaxel×4 vs ET×4 → capecitabine×4 as adjuvant chemotherapy for HER2-negative, node-positive breast cancer; evaluating efficacy and safety profiles of two taxane-containing regimens |
| [NCT00615602](https://clinicaltrials.gov/study/NCT00615602) | Phase 3 | Completed | 489 | Randomized comparison of 6 vs 12 months of trastuzumab combined with dose-dense docetaxel following FE75C as adjuvant treatment in HER2-overexpressing, lymph-node-positive breast cancer |
| [NCT00015938](https://clinicaltrials.gov/study/NCT00015938) | Phase 2 | Completed | 95 | Docetaxel + vinorelbine + filgrastim in HER2-negative Stage IV breast cancer; directly evaluated the combination regimen's effectiveness and immune recovery support |
| [NCT00712881](https://clinicaltrials.gov/study/NCT00712881) | Phase 2 | Completed | 126 | Randomized study of MYOCET (liposomal doxorubicin) + cyclophosphamide + trastuzumab followed by docetaxel + trastuzumab in neoadjuvant setting for Stage II/III HER2-positive breast cancer |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Bevacizumab + docetaxel + carboplatin as neoadjuvant therapy for triple-negative breast cancer (NEAT trial); assessed pathologic complete response rates |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | Unknown | 99 | Multicenter Phase 2 trial of neoadjuvant docetaxel + gemcitabine in locally advanced breast cancer; assessed tumor response, efficacy, and safety |
| [NCT02365805](https://clinicaltrials.gov/study/NCT02365805) | Phase 2 | Completed | 30 | Randomized neoadjuvant trial customizing chemotherapy regimen (incorporating docetaxel) based on BRCA1 mRNA expression levels in HER2-negative breast cancer |
| [NCT02897050](https://clinicaltrials.gov/study/NCT02897050) | Phase 2 | Suspended | 170 | Docetaxel ± metronomic cyclophosphamide/capecitabine followed by FEC as neoadjuvant therapy for triple-negative breast cancer; evaluated anti-tumor immune effects |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT (ABC Trials) | J Clin Oncol | Three-trial series (USOR 06-090, NSABP B-46-I/USOR 07132, NSABP B-49) comparing TC×6 vs standard TaxAC regimens as adjuvant therapy in early breast cancer; demonstrated non-inferiority of anthracycline-containing taxane combinations in node-positive or high-risk disease |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review / Early Clinical Data | J Clin Oncol | Foundational review of docetaxel's preclinical antitumor profile and early clinical results; established the basis for its development as a front-line cytotoxic in breast and other cancers |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Clinical Study | Breast Cancer (Tokyo) | Evaluated docetaxel + cyclophosphamide + trastuzumab (HER-TC) as neoadjuvant chemotherapy in HER2-positive breast cancer; reported pathologic complete response rates stratified by hormone receptor status |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Oral capecitabine combined with docetaxel and epirubicin (TEX) as first-line therapy in locally advanced/metastatic breast carcinoma; demonstrated promising activity with manageable toxicity |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 | Oncology | Docetaxel + vinorelbine combination in metastatic breast cancer and NSCLC; reported projected median survival and response rates with the 100 mg/m² docetaxel schedule |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 Dose-Finding | Tumori | Dose-finding study of docetaxel + gemcitabine in metastatic breast cancer patients previously treated with anthracyclines; explored weekly administration schedules to preserve quality of life |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort Study | Anti-Cancer Drugs | Retrospective investigation of the relationship between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema; identified incidence rates and risk factors in Stage II/III patients |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Translational / Biomarker | Br J Cancer | Microarray analysis of gene expression profiles to identify predictive markers of pathological complete response to trastuzumab + docetaxel-based treatment in HER2-positive breast carcinoma |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Clinical Review | Drug Ther Bull | Comparative review of paclitaxel and docetaxel in breast and ovarian cancer following expanded licensing; assessed early clinical evidence and benefit profile for taxanes in breast cancer |
| [15074734](https://pubmed.ncbi.nlm.nih.gov/15074734/) | 2004 | Clinical Study | Clin Oncol | Real-world experience with trastuzumab + docetaxel combination in women with HER2-overexpressing (IHC 3+) metastatic breast cancer; reported toxicity profile and effectiveness data from a cancer center in India |

---

## Canada Market Information

Docetaxel currently has **no registered Drug Identification Numbers (DINs)** in Canada according to the regulatory data reviewed for this report. No approved product listings, dosage forms, or indication texts are available from the Canadian database.

> Note: This finding is unexpected given docetaxel's widespread global regulatory approval (FDA, EMA, and numerous other agencies) for breast cancer, NSCLC, prostate cancer, gastric cancer, and head and neck cancer. Verification against Health Canada's Drug Product Database (DPD) is strongly recommended, as the absence of DINs may reflect data gaps in the current dataset rather than a true absence from the Canadian market.

---

## Cytotoxicity

Docetaxel is an antineoplastic agent of the taxane class (semi-synthetic taxoid). This section is required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia incidence is significant and prophylactic G-CSF (filgrastim/pegfilgrastim) support is routinely required in many regimens |
| Emetogenicity Classification | Low to moderate (lower than platinum-based agents; premedication with dexamethasone required primarily for hypersensitivity and fluid retention prevention) |
| Monitoring Items | CBC with differential (nadir typically Day 7–11); liver function tests (ALT, AST, bilirubin, alkaline phosphatase); renal function; cumulative fluid retention assessment; peripheral neuropathy grading; nail changes and skin toxicity assessment |
| Handling Protection | **Yes** — Must be prepared and administered following cytotoxic drug handling regulations: closed-system drug transfer devices (CSTDs) required for preparation; PPE (gloves, gown, eye protection) mandatory; spill kits must be available; disposal as cytotoxic waste |

---

## Safety Considerations

Detailed safety information (warnings, contraindications, and drug interaction data) was not available from the regulatory data reviewed for this report.

> Please refer to the docetaxel package insert (product monograph) for complete warnings and precautions, including information on: hypersensitivity reactions (premedication with dexamethasone is required), severe fluid retention, myelosuppression, hepatic impairment dosing adjustments, neurotoxicity, and use in special populations (pregnancy, lactation, pediatric patients).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel's activity in female breast carcinoma is supported by some of the strongest clinical evidence available in oncology — including multiple completed Phase 3 RCTs with thousands of participants and global regulatory approvals across major jurisdictions — placing this at Evidence Level L1. The TxGNN prediction score of 99.90% aligns with the overwhelming mechanistic and clinical basis for this indication.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm actual Health Canada DPN/DIN status via the Drug Product Database (DPD); the current data showing zero DINs may reflect a data retrieval gap rather than true non-availability in Canada
- **Safety data package:** Obtain and review the Canadian product monograph (or equivalent) for current approved warnings, contraindications, and special population guidance — this was flagged as a Blocking data gap (DG001) in the evidence pack
- **Mechanism of action documentation:** Formally retrieve and document the complete MOA from DrugBank (DB01248) to support mechanistic analysis, as this was identified as a High-severity gap (DG002)
- **Subtype-specific evidence mapping:** Stratify the clinical evidence by breast cancer subtype (HR+/HER2−, HER2+, TNBC) to support precision medicine application and guide treatment sequencing recommendations
- **Canadian clinical context review:** Assess current Canadian oncology practice guidelines (e.g., Cancer Care Ontario, BC Cancer) to determine how docetaxel-based regimens fit within the existing standard of care landscape
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

