---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Leukemia (CML) to Ewing Sarcoma

---

## One-Sentence Summary

Dasatinib is a second-generation multi-targeted tyrosine kinase inhibitor (TKI), originally established for the treatment of chronic myeloid leukemia (CML) and Philadelphia chromosome-positive (Ph+) leukemia through potent inhibition of the BCR-ABL1 oncoprotein.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukemia (CML) / Ph+ leukemia (no Canadian DIN record available) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Canadian regulatory record. Based on known published information, dasatinib is a small-molecule TKI that inhibits BCR-ABL1, Src family kinases (SFKs), c-KIT, and PDGFR-β at nanomolar concentrations — approximately 325-fold more potent than imatinib against BCR-ABL1 in vitro. Its established role in CML and Ph+ ALL is driven primarily by BCR-ABL1 inhibition; however, the concurrent inhibition of Src family kinases provides a mechanistic bridge to solid tumour indications where SFK signalling is pathologically activated.

Ewing sarcoma is a highly aggressive bone and soft-tissue malignancy most commonly diagnosed in adolescents and young adults. A defining feature of Ewing sarcoma biology is its dependence on **Src kinase activation** under microenvironmental stress (hypoxia, nutrient deprivation), which drives invadopodia formation, cellular invasion, and metastatic spread. Multiple preclinical studies spanning 2007–2022 directly demonstrate that dasatinib inhibits the Src/FAK signalling complex in Ewing sarcoma cell lines, reducing migration and invasion while inducing apoptosis in cells dependent on SRC for survival. The FAK-Src inhibitory axis has been validated across multiple sarcoma subtypes sharing mesenchymal origin with Ewing sarcoma.

Although dasatinib showed limited activity as a single agent in the completed Phase 2 SARC019 trial (NCT00464620; broad advanced sarcoma population), the mechanistic rationale for combination approaches — particularly with DNA-damaging chemotherapy (ifosfamide, carboplatin, etoposide) — remains scientifically compelling. The early termination of the paediatric Phase I/II combination trial (NCT00788125) was attributable to low enrolment rather than safety signals, leaving the combination hypothesis open for further exploration in relapsed or refractory paediatric Ewing sarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Large-scale multi-sarcoma trial evaluating dasatinib monotherapy for 6-month progression-free survival and response rate; includes Ewing sarcoma patients; results indicate limited single-agent activity in sarcomas overall |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Paediatric sarcoma trial (including Ewing sarcoma) combining dasatinib with ifosfamide, carboplatin, and etoposide; terminated early due to enrolment challenges (7 patients enrolled), not safety concerns; provides preliminary dose and safety reference data |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy in relapsed/refractory paediatric solid tumours including Ewing sarcoma; **not dasatinib-based** — reflects active therapeutic exploration in this indication but provides no direct evidence for dasatinib |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (in vitro) | Cancer Research | Seminal study demonstrating dasatinib inhibits migration and invasion in diverse human sarcoma cell lines and induces apoptosis specifically in bone sarcoma cells dependent on SRC kinase for survival |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (in vitro) | Oncology Reports | Direct demonstration of dasatinib antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines; implicates c-KIT and PDGFR inhibition as contributing mechanisms |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Translational Review | Sarcoma | Evaluation of FAK-Src complex targeting in Ewing sarcoma, DSRCT, and rhabdomyosarcoma; single-agent dasatinib failed in Phase 2, but combination strategies with FAK inhibitors show synergistic preclinical activity |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical (in vitro/in vivo) | Neoplasia | Microenvironmental stress (hypoxia, nutrient deprivation) activates Src in Ewing sarcoma cells, driving invadopodia formation and migration — a pathway directly targetable by dasatinib |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate under microenvironmental stress to promote invadopodia formation in Ewing sarcoma; supports Src inhibition as a mechanistically grounded anti-metastatic strategy |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src kinase overexpression and activation across sarcoma subtypes; validates Src as a viable therapeutic target and provides mechanistic context for dasatinib repurposing |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Curr Treatment Options Oncol | Systemic therapy review for chondrosarcoma; discusses TKI approaches across mesenchymal tumours and notes the role of antiangiogenic therapy, providing peripheral mechanistic context |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical | Cell Commun Signal | CXCR4 antagonist plerixafor activates receptor tyrosine kinase signalling in Ewing sarcoma; illustrates complex signalling network cross-talk relevant to understanding combination targeting strategies |

---

## Canada Market Information

Dasatinib currently has **no Drug Identification Numbers (DINs) on record** and is **not approved or marketed in Canada**. No regulatory licence data is available for this drug in the Canadian market at this time. Reference to international regulatory filings (FDA, EMA) would be required for safety and indication documentation.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-targeted tyrosine kinase inhibitor (BCR-ABL1 / Src family kinases / c-KIT / PDGFR-β inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate to High — neutropenia, thrombocytopenia, and anaemia are commonly reported adverse effects; haematological monitoring is essential |
| Emetogenicity Classification | Low (oral TKI; minimal direct emetogenic potential relative to conventional cytotoxics) |
| Monitoring Items | CBC with differential (baseline and periodic), liver function tests (ALT/AST/bilirubin), renal function, fluid retention assessment, pleural effusion monitoring (chest X-ray or CT), ECG/QTc interval at baseline, pulmonary function if respiratory symptoms arise |
| Handling Protection | Follow institutional oral chemotherapy handling protocols; cytotoxic precautions apply for preparation and disposal per applicable guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from published literature:** Clinically significant adverse events reported with dasatinib in leukemia populations include **pleural effusion** (most common fluid-related toxicity), **pulmonary hypertension**, **pericardial effusion**, **chylothorax** (rare), and **interstitial pneumonitis**. These risks — while characterised primarily in adult CML patients — should be proactively considered when evaluating dasatinib in paediatric Ewing sarcoma populations given the different physiological context. Formal safety data from the Canadian regulatory package insert is not currently available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One large-scale completed Phase 2 trial (NCT00464620; n=366) evaluated dasatinib in advanced sarcomas inclusive of Ewing sarcoma, and a convergent body of preclinical evidence (2007–2022) directly validates the Src/FAK pathway as a mechanistically sound target in Ewing sarcoma biology. While single-agent activity appears insufficient, the scientific rationale for combination approaches is compelling and remains incompletely tested clinically.

**To proceed, the following is needed:**
- Subgroup analysis data for Ewing sarcoma patients from NCT00464620 to quantify dasatinib's single-agent activity in this specific population
- Formal MOA documentation from DrugBank or a primary regulatory dossier (currently a data gap)
- Canadian regulatory pathway assessment — Health Canada marketing authorisation or Special Access Programme (SAP) eligibility review, given no current DIN
- Design of a prospective combination trial (e.g., dasatinib + ifosfamide/carboplatin/etoposide) with a paediatric-appropriate enrolment strategy and defined safety monitoring plan
- Pharmacokinetic data in paediatric patients to support dosing optimisation in the Ewing sarcoma setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

