---
layout: default
title: Dasatinib
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral multi-kinase inhibitor (BCR-ABL, SRC family, KIT, PDGFR) used for chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL).
The TxGNN model predicts it may be useful in **Ewing sarcoma**.
Support is thin: **2 dasatinib trials** (a mixed-sarcoma Phase 2 study and a terminated pediatric study with 7 patients) and **about 6 relevant publications**, mostly preclinical. One review reports that dasatinib **failed as a single agent** in Ewing sarcoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CML and Ph+ ALL (from the retrieved literature; the Health Canada indication text was not provided) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (preclinical and mechanistic evidence; the only clinical data are a non-randomized, mixed-sarcoma Phase 2 study, which does not meet the L2 definition of a randomized trial. The source pack labelled this L2.) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. From the retrieved literature, dasatinib is a small-molecule inhibitor of BCR-ABL, SRC-family kinases, c-KIT and PDGFR. Its efficacy in CML and Ph+ ALL is well established.

The link to Ewing sarcoma runs through SRC. Laboratory studies show that SRC activation and the FAK-SRC complex drive invasion, migration and invadopodia formation in Ewing sarcoma models. Dasatinib blocks SRC directly. In cell lines it reduced proliferation and migration and induced apoptosis in bone sarcoma cells that depend on SRC for survival.

Laboratory promise has not translated into clinical benefit so far. A 2022 review notes that in a Phase 2 study of advanced sarcomas, dasatinib **failed as a single agent** in Ewing sarcoma and rhabdomyosarcoma. The remaining question is whether dasatinib could work in combination or in a selected biomarker group. That question is untested.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib in advanced sarcomas, with response rate and 6-month progression-free survival as endpoints. Ewing sarcoma is one of several cohorts, so evidence is indirect. Cohort-level results are not in the input. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib plus ifosfamide, carboplatin and etoposide in pediatric patients. Terminated early with 7 patients, so it says nothing about efficacy. |

A third retrieved trial, NCT06500819 (B7-H3 CAR-T in pediatric solid tumors), does not involve dasatinib and is excluded.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Reviews targeting the FAK-SRC complex in DSRCT, Ewing sarcoma and rhabdomyosarcoma. Single-agent dasatinib failed in the Phase 2 sarcoma study. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncol Lett | Reviews the role of Src signaling in sarcoma and its potential as a drug target. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical | Cancer Res | Dasatinib inhibited migration and invasion in diverse sarcoma cell lines and induced apoptosis in bone sarcoma cells dependent on SRC. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical | Oncol Rep | Dasatinib showed antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to promote invadopodia formation in Ewing sarcoma. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma. |

---

## Canada Market Information

The input lists 20 authorizations. Dosage form, manufacturer and approved indication text were empty in the data, so only the identifiers are shown (5 of 20).

| DIN | Product Name |
|---------|------|
| 02293137 | SPRYCEL |
| 02470713 | APO-DASATINIB |
| 02470721 | APO-DASATINIB |
| 02499304 | TARO-DASATINIB |
| 02499282 | TARO-DASATINIB |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link (SRC signaling) is plausible, but the only clinical evidence is a mixed-sarcoma Phase 2 study, which a published review says showed no single-agent activity in Ewing sarcoma. The only pediatric combination trial was terminated with 7 patients. This is currently a research question, not a development candidate.

**To proceed, the following is needed:**
- Ewing sarcoma cohort-level results from NCT00464620 (response rate, progression-free survival)
- A rationale for combination use or a biomarker-defined subgroup, with preclinical support
- Health Canada product monograph warnings, contraindications and interactions
- Mechanism of action data confirmed from DrugBank
- Pediatric and young-adult safety data, since Ewing sarcoma mainly affects this group

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

