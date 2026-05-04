---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug originally approved for colorectal cancer and breast cancer, selectively converted to active 5-fluorouracil (5-FU) within tumor tissue by thymidine phosphorylase (TP).
The TxGNN model predicts efficacy across **10 gastric cancer subtypes** (scores 99.89–99.94%); among these, **Gastric Tubular Adenocarcinoma** (TxGNN Rank #3) carries the strongest clinical foundation, supported by **20 publications** including multiple completed Phase 3 RCTs that directly establish CAPOX (capecitabine + oxaliplatin) as adjuvant standard-of-care in gastric cancer—though the drug is currently not registered in Canada.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer; breast cancer |
| Predicted New Indication | Gastric Tubular Adenocarcinoma (strongest evidence; TxGNN overall Rank #3) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Multi-Indication Overview

This evidence pack covers 10 gastric cancer subtypes predicted by TxGNN. Evidence strength and recommendations vary substantially across subtypes:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) | 99.94% | L5 | Hold |
| 2 | Microinvasive Gastric Cancer | 99.94% | L5 | Hold |
| **3** | **Gastric Tubular Adenocarcinoma** ⭐ | **99.94%** | **L1** | **Proceed with Guardrails** |
| 4 | Signet Ring Cell Gastric Adenocarcinoma | 99.94% | L2 | Research Question |
| **5** | **Gastric Cardia Adenocarcinoma** | **99.91%** | **L1** | **Proceed with Guardrails** |
| 6 | Carcinoma of Stomach, Salivary Gland Type | 99.91% | L3 | Research Question |
| 7 | Gastric Pylorus Carcinoma | 99.91% | L4 | Research Question |
| **8** | **Gastric Body Carcinoma** | **99.90%** | **L1** | **Proceed with Guardrails** |
| 9 | Epstein-Barr Virus-Associated Gastric Carcinoma | 99.90% | L4 | Research Question |
| 10 | Malignant Gastric Granular Cell Tumor | 99.89% | L5 | Hold |

The remainder of this report focuses on **Gastric Tubular Adenocarcinoma** (⭐), the subtype with the strongest clinical evidence base. Gastric Cardia Adenocarcinoma and Gastric Body Carcinoma also reach L1 and are reflected in the clinical trials and literature sections below.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on established pharmacology, capecitabine is an orally administered prodrug that undergoes a three-step enzymatic conversion to 5-fluorouracil (5-FU), with the final activation step catalyzed by thymidine phosphorylase (TP) — an enzyme substantially overexpressed in tumor tissue relative to normal gastrointestinal mucosa. Gastric tubular adenocarcinoma is the predominant histological subtype of Lauren intestinal-type gastric cancer, and intestinal-type tumors are known to exhibit particularly high TP activity, making them an ideal substrate for capecitabine's selective tumor-site activation mechanism.

Colorectal cancer and gastric tubular adenocarcinoma share overlapping molecular characteristics: both arise from gastrointestinal epithelium, both show chromosomal instability (CIN) as a dominant genomic pathway, and both demonstrate robust sensitivity to fluoropyrimidine-based chemotherapy. This mechanistic and biological continuity explains why the clinical evidence for capecitabine in gastric cancer is exceptionally strong — the drug's development trajectory followed the same TP-mediated activation logic from colorectal to gastric settings. The TxGNN model appears to be capturing this genuine pharmacological signal rather than generating a spurious high-score prediction.

The evolution of capecitabine from a single adjuvant agent (established by CLASSIC Phase 3 RCT) to a perioperative backbone (confirmed by RESOLVE) and then to the chemotherapy partner of choice for immunotherapy combinations (confirmed by KEYNOTE-859, CheckMate-649, RATIONALE-305, ORIENT-16, and GLOW) demonstrates its versatile and deeply validated position across all treatment settings of gastric adenocarcinoma. The uniformly high TxGNN scores (99.89–99.94%) across all 10 gastric subtypes therefore reflect genuine cross-subtype biological signal, though evidence quality diverges sharply between common histological subtypes (tubular, cardia, body) and rare variants (GAPPS, granular cell tumor, salivary gland type).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00374036](https://clinicaltrials.gov/study/NCT00374036) | Phase 3 | Completed | 416 | **REAL2 trial**: 2×2 factorial design comparing capecitabine vs. 5-FU and oxaliplatin vs. cisplatin in advanced gastric/GEJ adenocarcinoma. Capecitabine arm confirmed non-inferior to 5-FU — highest-level direct evidence establishing capecitabine as an oral first-line backbone. |
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | CAPOX (capecitabine + oxaliplatin) in metastatic esophageal, gastroesophageal junction, and gastric cardia adenocarcinoma. Direct subtype-specific evaluation in the cardia; demonstrates activity and tolerability of the CAPOX combination. |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Randomized Phase 2 of extended neoadjuvant therapy for locally advanced adenocarcinoma of the esophagus, GEJ, and gastric cardia; capecitabine-containing arm included, supporting preoperative use. |
| [NCT06238752](https://clinicaltrials.gov/study/NCT06238752) | Phase 2 | Completed | 33 | Apatinib + tislelizumab + XELOX (capecitabine + oxaliplatin) as first-line treatment for HER2-negative advanced G/GEJ cancer, including signet ring cell carcinoma; provides Phase 2 safety data for CAPECITABINE in combination with anti-angiogenic and immunotherapy. |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | Phase N/A (dose-finding) | Completed | 27 | TEX (docetaxel + oxaliplatin + capecitabine) + trastuzumab in HER2-positive advanced gastroesophageal cancer including cardia; confirms capecitabine tolerability within a triplet cytotoxic combination. |
| [NCT00414271](https://clinicaltrials.gov/study/NCT00414271) | Phase 2 | Completed | 18 | Neoadjuvant chemotherapy in locally advanced gastric cancer; investigates thymidylate synthase (TS) expression by IHC as a predictive biomarker for 5-FU/capecitabine response — directly mechanistically relevant. |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | Not Yet Recruiting | 66 | AK112 (PD-1/VEGF bispecific antibody) + chemotherapy as neoadjuvant treatment specifically designed for signet ring cell–containing gastric/GEJ adenocarcinoma; prospective subtype-specific evidence generation planned. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT Phase 3 | Lancet | **CLASSIC trial**: CAPOX adjuvant chemotherapy vs. observation after D2 gastrectomy in Stage II–IIIB gastric cancer (n=1,035). Landmark trial directly establishing capecitabine + oxaliplatin as post-surgical standard-of-care; disease-free survival benefit confirmed. |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT Phase 3 | Lancet Oncology | **RESOLVE trial**: Perioperative SOX vs. postoperative CAPOX after D2 gastrectomy for locally advanced gastric/GEJ cancer; confirms CAPOX as standard adjuvant regimen with comparable efficacy to SOX in the perioperative setting. |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT Phase 3 | Lancet Oncology | **RESOLVE final report**: Updated overall survival analysis from the RESOLVE trial; long-term confirmation of CAPOX benefit in locally advanced gastric cancer after D2 gastrectomy. |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT Phase 3 | Nature Medicine | **GLOW trial**: Zolbetuximab + CAPOX (capecitabine + oxaliplatin) in CLDN18.2-positive HER2-negative advanced gastric/GEJ adenocarcinoma; capecitabine-containing regimen achieves statistically significant survival benefit in molecularly selected patients. |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT Phase 3 | Lancet | **CheckMate 649**: Nivolumab + chemotherapy (capecitabine/oxaliplatin-based) vs. chemotherapy alone for advanced HER2-negative gastric/GEJ/esophageal adenocarcinoma; large Phase 3 trial confirming capecitabine as the chemotherapy backbone in the immunotherapy era. |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | RCT Phase 3 | BMJ | **RATIONALE-305**: Tislelizumab + chemotherapy (including capecitabine) vs. placebo + chemotherapy as first-line treatment for advanced gastric/GEJ adenocarcinoma; positive Phase 3 result in a broad population. |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT Phase 3 | Lancet Oncology | **KEYNOTE-859**: Pembrolizumab + chemotherapy (capecitabine-containing) vs. placebo + chemotherapy for HER2-negative advanced gastric/GEJ adenocarcinoma; overall survival benefit confirmed. |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | RCT Phase 3 | JAMA | **ORIENT-16**: Sintilimab (anti-PD-1) + chemotherapy (capecitabine-containing) vs. chemotherapy alone for unresectable gastric/GEJ cancer; independent Phase 3 replication of capecitabine-immunotherapy combination benefit. |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT Phase 3 | Lancet | **FLOT4 trial**: FLOT vs. ECF/ECX perioperative chemotherapy for locally advanced resectable gastric/GEJ adenocarcinoma; ECX (epirubicin + cisplatin + capecitabine) arm represents the established capecitabine-containing perioperative regimen as active comparator. |
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Phase 2 Trial | Annals of Oncology | CAPOX in metastatic adenocarcinoma of the esophagus, GEJ, and gastric cardia (NCCTG Phase 2, n=48). Direct early evidence of capecitabine + oxaliplatin activity specifically in the cardia subtype; confirmed tolerability and preliminary efficacy. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine class; orally administered prodrug of 5-fluorouracil) |
| Myelosuppression Risk | Moderate (neutropenia and thrombocytopenia reported; generally less myelosuppressive than continuous-infusion IV 5-FU) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (baseline and each cycle), renal function (creatinine clearance essential for dose adjustment), liver function tests |
| Handling Protection | Must follow cytotoxic drug handling regulations; oral tablet dispensing requires appropriate institutional controls |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**
*(applicable to L1-evidence subtypes: Gastric Tubular Adenocarcinoma, Gastric Cardia Adenocarcinoma, Gastric Body Carcinoma)*

**Rationale:**
The CLASSIC (PMID 22226517) and RESOLVE (PMID 34252374) Phase 3 RCTs directly establish CAPOX as adjuvant standard-of-care after D2 gastrectomy; REAL2 (NCT00374036, n=416) confirms capecitabine non-inferiority to 5-FU across advanced gastric cancer; and at least five additional major Phase 3 trials (KEYNOTE-859, CheckMate-649, RATIONALE-305, ORIENT-16, GLOW) have successfully incorporated capecitabine as the chemotherapy backbone in immunotherapy combinations. This constitutes an overwhelming base of Level 1 evidence for the three L1-designated subtypes. TxGNN's uniformly high prediction scores (99.89–99.94%) reflect genuine mechanistic and clinical signal rather than model artifacts.

**To proceed, the following is needed:**
- Verify Health Canada registration status: capecitabine may already hold DINs for colorectal or breast cancer indications — a search of the Health Canada Drug Product Database is required to confirm current approval scope and whether gastric cancer is included or accessible via off-label use
- Obtain the Canadian product monograph to establish the full safety profile for prescribing
- Complete MOA data retrieval from DrugBank (DrugBank ID: DB01101) to support formal pharmacological justification documents
- Establish a safety monitoring protocol including CBC monitoring, creatinine clearance assessment for dose adjustment, and hand-foot syndrome surveillance
- For **Ranks 1–2** (GAPPS, microinvasive gastric cancer) and **Rank 10** (malignant gastric granular cell tumor): maintain **Hold** — these require dedicated evidence generation before any clinical application can be considered
- For **Rank 4** (signet ring cell), **Rank 6** (salivary gland type), **Rank 7** (pylorus), and **Rank 9** (EBV-associated): treat as **Research Questions** — subtype-specific biomarker-stratified prospective studies are needed before routine clinical implementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

