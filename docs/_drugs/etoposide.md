---
layout: default
title: Etoposide
parent: Model Prediction Only (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Etoposide: predicted new indication Ewing sarcoma (evidence level L5). Approved use: Small cell lung carcinoma, testicular cancer / germ cell tumour"
monitor_inn: "ETOPOSIDE"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
---

# Etoposide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Etoposide: From Small Cell Lung Carcinoma to Ewing Sarcoma

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor chemotherapy originally used for small cell lung carcinoma and testicular germ cell tumours.
The TxGNN model predicts it may be effective for **Ewing sarcoma** (the top-ranked prediction with the strongest evidence; the first-ranked prediction, well-differentiated fetal adenocarcinoma of the lung, has no trial support), with **31 clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung carcinoma, testicular cancer / germ cell tumour (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Ewing sarcoma (best-supported candidate; the model's rank-1 prediction, well-differentiated fetal adenocarcinoma of the lung, scored 99.94%) |
| TxGNN Prediction Score | 99.85% (Ewing sarcoma) |
| Evidence Level | L1 (Ewing sarcoma) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

**Overview of all predicted indications**

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Well-differentiated fetal adenocarcinoma of the lung | 99.94% | L4 | Hold |
| 2 | Primary pulmonary lymphoma | 99.94% | L4 | Hold |
| 3 | Pulmonary blastoma | 99.94% | L3 | Research question |
| 4 | **Ewing sarcoma** | 99.85% | L1 | Proceed with Guardrails |
| 5 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.80% | L4 | Hold |
| 6 | **Rhabdomyosarcoma** | 99.79% | L1 | Proceed with Guardrails |
| 7 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | L5 | Hold |
| 8 | Parameningeal embryonal rhabdomyosarcoma | 99.76% | L3 | Research question |
| 9 | Extrahepatic bile duct rhabdomyosarcoma | 99.75% | L5 | Hold |
| 10 | Prostate embryonal rhabdomyosarcoma | 99.74% | L4 | Hold |

The rest of this report focuses on Ewing sarcoma, with supporting notes on rhabdomyosarcoma.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, etoposide is a topoisomerase II poison: it stabilises DNA breaks and causes double-strand DNA damage in rapidly dividing cells. Its efficacy in small cell lung carcinoma and germ cell tumours is established, and mechanistically it may be applicable to other chemosensitive, fast-growing tumours.

Ewing sarcoma is a highly chemosensitive paediatric and young-adult bone and soft tissue cancer. Etoposide is already part of its standard backbone, alternating with ifosfamide (IE) and vincristine/doxorubicin/cyclophosphamide (VDC). A randomised trial showed that adding ifosfamide and etoposide to standard chemotherapy improved outcomes in newly diagnosed non-metastatic disease (Grier 2003). A mechanistic study also notes that Ewing sarcoma is highly sensitive to genotoxic agents such as etoposide.

A similar logic applies to rhabdomyosarcoma, where ifosfamide/etoposide regimens are used mainly in intermediate- and high-risk disease. The lower-ranked predictions (rare lung tumours, rhabdomyosarcoma sub-sites) rest largely on case reports or on the model score alone.

---

## Clinical Trial Evidence

Ewing sarcoma has 31 registered trials in the compiled data. The table lists the 10 most relevant (graded A/B first, then larger completed trials).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | N/A | EICESS 92: randomised comparison of etoposide-containing chemotherapy regimens plus surgery/radiotherapy in Ewing sarcoma |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: chemotherapy with or without radiotherapy/surgery and stem cell support |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy intensification in Ewing sarcoma and related tumours |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to standard 5-drug chemotherapy (including etoposide) in non-metastatic disease |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification versus standard treatment in non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multiagent chemotherapy (including etoposide) in metastatic disease |
| [NCT00002898](https://clinicaltrials.gov/study/NCT00002898) | Phase 3 | Completed | 400 | MMT 95: randomised chemotherapy regimens in soft tissue sarcomas including Ewing-type tumours (indirect evidence) |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and consolidation in metastatic Ewing sarcoma; etoposide as part of a multi-drug regimen |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | N/A | Cyclophosphamide, doxorubicin, vincristine, etoposide and ifosfamide followed by resection and radiotherapy |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Intensive chemotherapy with growth factor support in metastatic Ewing's tumour at diagnosis |

For rhabdomyosarcoma, the randomised Phase 3 trial [NCT00003052](https://clinicaltrials.gov/study/NCT00003052) (etoposide + ifosfamide + doxorubicin with or without hyperthermia in high-risk soft tissue sarcoma, 340 patients, completed) provides supporting evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012: comparison of two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (alternating VDC and IE) for localised Ewing sarcoma |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board consensus recommendations |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and collaborative approaches in Ewing sarcoma |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospective analysis | Sarcoma | Oral etoposide in 33 adolescent and adult patients with relapsed/refractory Ewing sarcoma |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Mechanism study | Nature | EWS-FLI1 causes R-loops and blocks BRCA1 repair, explaining sensitivity to genotoxic agents such as etoposide |
| [11846301](https://pubmed.ncbi.nlm.nih.gov/11846301/) | 2001 | Cohort/randomised comparison | J Pediatr Hematol Oncol | Ifosfamide + etoposide superior to vincristine + melphalan in metastatic rhabdomyosarcoma |
| [26503200](https://pubmed.ncbi.nlm.nih.gov/26503200/) | 2016 | Clinical trial | J Clin Oncol | Dose-compressed ifosfamide/etoposide and VDC cycles in high-risk rhabdomyosarcoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00616192 | VEPESID | Not specified | Not specified |
| 02080036 | ETOPOSIDE INJECTION | Not specified | Not specified |
| 02552671 | ETOPOSIDE INJECTION | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor, epipodophyllotoxin class) |
| Myelosuppression Risk | High (the knowledge graph lists neutropenia, leukopenia, thrombocytopenia and anaemia among contraindicated conditions) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for details.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** thrombocytopenia, neutropenia, agranulocytosis, anaemia, leukopenia, interstitial lung disease, pulmonary fibrosis, impaired renal function, acidosis/metabolic acidosis, and drug-induced liver injury. These point mainly to marrow, lung, kidney and liver risks and should be checked against the product monograph.
- **Drug interactions (100 recorded):** examples at moderate level include aprepitant, rolapitant, metronomidazole, tinidazole, eliglustat, rosuvastatin and simvastatin. Levofloxacin is minor. Others (e.g. cimetidine, pantoprazole, morphine, doxycycline) have an unknown severity level.
- **Regimen-related risks noted in the evidence:** myelosuppression and secondary leukaemia risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Ewing sarcoma and rhabdomyosarcoma). **Hold** for the lower-evidence rare tumours (rank 1, 2, 5, 7, 9, 10). Pulmonary blastoma and parameningeal embryonal rhabdomyosarcoma remain research questions.

**Rationale:**
- Ewing sarcoma is supported by several Phase 3 trials and randomised publications, and etoposide with ifosfamide is already part of standard care, so this is largely an established use rather than a new discovery. Rhabdomyosarcoma has similar but more risk-group-dependent support.
- The model's top-scoring predictions (fetal adenocarcinoma of the lung, primary pulmonary lymphoma) have no registered trials and only indirect or off-target literature.

**To proceed, the following is needed:**
- Canadian product monograph warnings and contraindications (not available in the compiled data), plus approved indication text for the three DINs
- Detailed mechanism of action data
- Confirmation of the exact regimen, risk stratification and age-appropriate dosing
- A plan for monitoring myelosuppression and secondary malignancy, with supportive care and a drug interaction review
- Dosage form and route information for the Canadian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

