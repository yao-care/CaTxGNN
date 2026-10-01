---
layout: default
title: Gemcitabine
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Solid-Tumour Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a nucleoside-analog cytotoxic chemotherapy drug. The Canadian label indication text was not captured in the source data.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **50 linked clinical trials** (many only indirectly relevant, and 5 breast-specific Phase 3 trials among them) and **20 publications** currently associated with this direction.
Breast cancer may already be a recognised use of gemcitabine, so how novel this "repurposing" is must be checked against the approved label.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (the pack's pre-score is L1; see the note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

**Note on the evidence level:** L1 requires at least 2 completed Phase 3 RCTs in this indication. Only one breast-cancer Phase 3 trial is confirmed as completed (NCT00093795). The other breast Phase 3 trials are terminated or of unknown status. One Phase 2/3 trial is also completed (NCT01881230). This report therefore assigns L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Gemcitabine is a cytotoxic nucleoside analog. Its active metabolites (dFdCDP and dFdCTP) inhibit ribonucleotide reductase and are incorporated into DNA, where they cause chain termination in rapidly dividing tumour cells. This general pharmacology is not tied to one tumour type, which makes activity in breast cancer mechanistically plausible.

Preclinical work supports the link. Gemcitabine combined with trastuzumab showed additive or synergistic effects in HER2-overexpressing breast cancer cell lines (PMIDs 12057039 and 15685824). The clinical literature describes single-agent response rates of 16–37% in metastatic breast cancer, and higher response rates in combinations with taxanes, platinums and anthracyclines.

Because the original indications are not recorded here, the relationship between the original and new indication cannot be assessed directly. Novelty should be confirmed against the Health Canada label.

---

## Clinical Trial Evidence

The 10 most relevant breast-cancer trials are listed. The pack gives trial designs, not results, so the findings column describes each design.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | Completed | 4894 | Adjuvant, node-positive breast cancer: TAC vs dose-dense AC→paclitaxel vs the same regimen plus gemcitabine. Results not summarised in the pack. |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Gemcitabine + Herceptin vs capecitabine + Herceptin in pretreated HER2-positive metastatic breast cancer. Terminated early, so power is limited. |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant: capecitabine or gemcitabine added to docetaxel before AC, with or without bevacizumab. Endpoint is pathologic complete response. |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | Unknown | 800 | Neoadjuvant epirubicin/cyclophosphamide followed by paclitaxel with or without gemcitabine in poor-risk early breast cancer. |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Unknown | Not reported | tAnGo: paclitaxel/epirubicin/cyclophosphamide with or without gemcitabine, adjuvant, ER/PgR-poor early breast cancer. |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | First-line triple-negative metastatic breast cancer: nab-paclitaxel + gemcitabine or carboplatin vs gemcitabine/carboplatin. |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | Unknown | 99 | Neoadjuvant docetaxel + gemcitabine in locally advanced breast cancer. |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine + trastuzumab + pertuzumab in metastatic HER2-positive breast cancer after prior HER2 therapy. |
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Phase 2 | Completed | 41 | Weekly gemcitabine + Herceptin in HER2-overexpressing metastatic breast cancer. |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | Completed | 30 | Single-agent gemcitabine in metastatic breast cancer previously treated with doxorubicin and paclitaxel. |

**Data-quality caveat:** NCT00585689 is retrieved for this indication, and the pack's relevance note calls it a breast trial. Its title and summary describe locally advanced **bladder** cancer, so it is excluded from the table above. Many of the other linked trials are basket, bladder or ovarian studies with only indirect relevance.

---

## Literature Evidence

No RCT publications were retrieved. The list below is drawn from Phase 2 studies, early-phase trials and reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Phase 2 trial | Cancer Chemother Pharmacol | Biweekly docetaxel + gemcitabine + bevacizumab as salvage therapy in pretreated HER2-negative metastatic breast cancer; activity and safety evaluated. |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 (multicenter) | Oncology | Weekly docetaxel + gemcitabine as first-line metastatic breast cancer treatment; efficacy, toxicity and dose intensity assessed. |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 trial | Breast Cancer Res Treat | Carboplatin + gemcitabine + mifepristone in advanced breast and ovarian cancer, based on a glucocorticoid-receptor rationale. |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 trial | Gynecol Oncol | Mirvetuximab soravtansine + gemcitabine in FRα-positive tumours including triple-negative breast cancer; primary endpoint was MTD/RP2D. |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Unclassified (Phase 2 report) | Semin Oncol | Preliminary phase II results of gemcitabine + trastuzumab in heavily pretreated metastatic breast cancer; preclinical additive or synergistic effects. |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Unclassified (overview) | Semin Oncol | About 20 phase II trials confirm single-agent activity in metastatic breast cancer, with response rates of 16–37%. |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine + paclitaxel in metastatic breast cancer; 114 of 221 phase II patients (52%) responded. |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Adding gemcitabine to platinum compounds gives significant clinical benefit and response rates in metastatic breast cancer. |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Reviews gemcitabine, anthracycline and taxane combinations in advanced breast cancer. |
| [21980041](https://pubmed.ncbi.nlm.nih.gov/21980041/) | 2011 | Unclassified (pharmacogenetics) | Cancer Genomics Proteomics | Gemcitabine/carboplatin is efficacious in Asian breast cancer patients but causes significant haematologic toxicity; genetic variants were analysed to predict toxicity. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2412292 | GEMCITABINE INJECTION |
| 2402831 | GEMCITABINE INJECTION |

Dosage form, manufacturer and approved indication text were not captured for these licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Significant haematologic toxicity is reported with gemcitabine/carboplatin in breast cancer (PMID 21980041); a Phase 1 trial combined gemcitabine with filgrastim support (NCT00014456). Please refer to the package insert for the full profile. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. The Health Canada warnings and contraindications were not obtained, and no drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gemcitabine has a plausible antimetabolite mechanism and a large body of breast-cancer clinical research. This includes one completed adjuvant Phase 3 trial (n=4894), a completed Phase 2/3 triple-negative trial and many Phase 2 combination studies. However, the rating is limited by three things. The Phase 3 trials are largely of unknown or terminated status. Outcome data are not in the pack. Breast cancer may already be an approved use rather than a true repurposing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications), to confirm whether breast cancer is already labelled
- Published outcomes for the Phase 3 trials NCT00093795, NCT00408408, NCT00070278 and NCT00039546
- Mechanism-of-action data from DrugBank
- Removal of mis-mapped trials, such as the bladder-cancer trial NCT00585689, from the breast-cancer evidence set
- A safety monitoring plan covering haematologic toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

