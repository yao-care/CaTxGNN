---
layout: default
title: Docetaxel
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Non-Small Cell Lung, Prostate, Gastric, Head and Neck, and Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane chemotherapy drug, originally used for non-small cell lung cancer, prostate cancer, head and neck cancer, gastric cancer and breast cancer.
The TxGNN model ranks **female breast carcinoma** as its top prediction. Breast carcinoma is already one of the drug's original indications, so this is a confirmation of an existing use rather than true repurposing.
The data compiled for this report include **46 registered clinical trials** and **20 publications** for this indication; the trial table below lists the most relevant entries and the literature table lists the most informative publications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, prostate cancer, head and neck cancer, gastric cancer, breast cancer (the Canadian licence records contain no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Several completed Phase 3 trials appear in the data (for example NCT00003519, NCT00021255, NCT00003782, NCT00333775, NCT00887536 and NCT00002707). Their relevance has not yet been graded, and docetaxel is only one component of the regimens tested in them. The L2 grade follows the formal scoring in the data. The true level of evidence is probably higher, because breast cancer is a long-established use.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the published literature, docetaxel is a taxane that stabilises microtubules. This blocks the cell from dividing and arrests it in mitosis, which is why it acts on rapidly dividing tumour cells.

Breast carcinoma is already one of docetaxel's original indications. The prediction therefore reflects a well-established use more than a new direction. Reviews in the data describe docetaxel as an evidence-based component of therapy for advanced breast cancer. It is used alone and in combination with anthracyclines, cyclophosphamide, capecitabine, gemcitabine and HER2-targeted agents.

---

## Clinical Trial Evidence

The data list 46 registered trials. The table below shows the 10 most relevant. Phase 3 trials are included because they are the strongest design, even though their relevance grade is still pending.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomised comparison of carboplatin versus docetaxel in metastatic breast cancer with a genetic (BRCA) background |
| [NCT00003352](https://clinicaltrials.gov/study/NCT00003352) | Phase 2 | Completed | 89 | Doxorubicin, docetaxel and cyclophosphamide (ATC) in metastatic or locally advanced breast cancer |
| [NCT00003953](https://clinicaltrials.gov/study/NCT00003953) | Phase 2 | Completed | 39 | Preoperative dose-dense sequential doxorubicin then docetaxel in stage II–IIIB breast cancer |
| [NCT00379015](https://clinicaltrials.gov/study/NCT00379015) | Phase 2 | Completed | 38 | Neoadjuvant epirubicin/cyclophosphamide followed by docetaxel plus trastuzumab in HER2-positive disease |
| [NCT02502864](https://clinicaltrials.gov/study/NCT02502864) | Phase 4 | Completed | 9 | Pharmacokinetic-guided docetaxel dosing with cyclophosphamide in older adults; very small |
| [NCT00025493](https://clinicaltrials.gov/study/NCT00025493) | Phase 2 | Terminated | 27 | Single-agent docetaxel in metastatic breast cancer in patients aged 70 and older; stopped early |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Completed | 2,778 | Adjuvant doxorubicin/docetaxel versus doxorubicin/cyclophosphamide in node-positive or high-risk breast cancer |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3,222 | Adjuvant AC followed by docetaxel (AC-T), with or without trastuzumab, versus docetaxel/carboplatin/trastuzumab in HER2-positive disease |
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | Completed | 5,351 | Three adjuvant regimens containing docetaxel (AC-T, AT, ATC) in node-positive breast cancer |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | Bevacizumab plus docetaxel versus docetaxel plus placebo, first-line, HER2-negative metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC trials: docetaxel/cyclophosphamide (TC) compared with taxane-plus-anthracycline regimens in early breast cancer |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Paclitaxel and docetaxel are accepted evidence-based components of therapy for advanced breast, lung and ovarian cancers |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | Docetaxel–anthracycline combinations in metastatic breast cancer; rationale includes non-overlapping toxicity |
| [12868802](https://pubmed.ncbi.nlm.nih.gov/12868802/) | 2003 | Review | Breast Cancer Res Treat | Neoadjuvant docetaxel in locally advanced breast cancer |
| [9775340](https://pubmed.ncbi.nlm.nih.gov/9775340/) | 1998 | Review | Am J Health Syst Pharm | Pharmacology, clinical trials, adverse effects and dosing of docetaxel in metastatic breast cancer |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Review | Oncology (Williston Park) | Docetaxel plus vinorelbine in metastatic breast cancer and non-small cell lung cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 study | Oncology | Weekly docetaxel plus gemcitabine as first-line therapy for metastatic breast cancer |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 study | Cancer | Capecitabine with docetaxel and epirubicin in untreated advanced breast cancer |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective study | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Review | Expert Opin Drug Metab Toxicol | Lessons learned from the development of docetaxel |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02458020 | DOCETAXEL INJECTION | Not listed | Not listed |
| 02361957 | DOCETAXEL INJECTION USP | Not listed | Not listed |
| 02439336 | DOCETAXEL INJECTION | Not listed | Not listed |

All three licences are single-ingredient products and are currently valid. None has been cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabiliser) |
| Myelosuppression Risk | High. Neutropenia is a leading concern; the knowledge graph also flags thrombocytopenia, anaemia and agranulocytosis |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function (including bilirubin), signs of fluid retention, peripheral neuropathy and hypersensitivity |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications flagged in the drug–disease knowledge graph** (these are not label text): liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anaemia, hyperbilirubinaemia (including Gilbert syndrome), diarrhoeal disease, pulmonary oedema, stomatitis, neuritis (including motor nerve neuritis) and cardiac tamponade.
- **Drug interactions:** 100 interactions were identified; the first 20 retrieved are summarised here. The one rated Major is **clarithromycin**. Moderate interactions include aprepitant, rolapitant, metronidazole, tinidazole, cimetidine, miconazole, eliglustat, rosuvastatin, simvastatin and troglitazone. Minor interactions include dexamethasone, prednisone, prednisolone and levofloxacin. Several others are rated unknown.
- **Clinical points raised in the literature:** neutropenia, hypersensitivity reactions, fluid retention (including a possible association with lymphedema) and interstitial pneumonitis.

Official label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast carcinoma is an established docetaxel indication, with many Phase 2 and 3 trials and extensive literature. The "new indication" is therefore a confirmation rather than a repurposing opportunity. The guardrails are needed because the toxicity profile is substantial, the drug interaction burden is high, and the grading of the Phase 3 evidence is incomplete.

**To proceed, the following is needed:**
- Review of the Health Canada package inserts for warnings, contraindications and approved indications. The licence records currently show none.
- Relevance grading of the Phase 3 trials, so that the evidence level reflects the actual data.
- Detailed mechanism of action data from DrugBank.
- A monitoring plan for myelosuppression, hepatic function and neuropathy, and a review of co-medications, especially strong CYP3A4 inhibitors such as clarithromycin.

---

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | Evidence Level | Recommendation | Comment |
|---|---|---|---|---|
| 2 | Ewing sarcoma | L2 | Research Question | Phase 2 data for gemcitabine followed by docetaxel in recurrent disease; mostly mixed sarcoma cohorts |
| 8 | Rhabdomyosarcoma | L2 | Research Question | Pediatric solid-tumour and sarcoma data, with limited disease-specific signal |
| 3, 7 | Fetal lung adenocarcinoma, pulmonary blastoma | L4 | Hold | Case reports only |
| 4 | Small cell lung carcinoma | L4 | Hold | The evidence supplied concerns non-small cell lung cancer, an original indication |
| 5, 6, 9, 10 | Primary pulmonary lymphoma and rare rhabdomyosarcoma subtypes | L5 | Hold | Model prediction only, with no supporting clinical evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

