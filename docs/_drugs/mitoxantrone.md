---
layout: default
title: Mitoxantrone
parent: Model Prediction Only (L5)
nav_order: 625
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
monitor_inn: "MITOXANTRONE"
predicted_indications: ["upper aerodigestive tract neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "head and neck cancer", "bladder exstrophy-epispadias-cloacal exstrophy complex"]
description: "Mitoxantrone: predicted new indication Upper aerodigestive tract neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Mitoxantrone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Mitoxantrone: Upper aerodigestive tract neoplasm
{: .text-alpha }

## One-Sentence Summary

Mitoxantrone is an anthracenedione chemotherapy agent, originally used to treat acute myeloid leukemia (AML) and related myeloid malignancies.
The TxGNN model predicts it may be effective for **head and neck cancer**, the most developed of its eight predicted new indications. Support comes from **6 clinical trials** (1 completed Phase Ib, 1 Phase III not yet recruiting, 3 Phase II, 1 Phase IV imaging study) and **20 publications**, most of them older Phase II studies with modest activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 (head and neck cancer); L4 for the broader upper aerodigestive tract category |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (head and neck cancer); Hold for the other predictions |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on the supporting literature, mitoxantrone is a topoisomerase II inhibitor and DNA intercalator with a mechanism similar to the anthracyclines. This makes it cytotoxic to rapidly dividing cells. Its efficacy in AML is established.

Head and neck cancers, including squamous cell carcinoma, nasopharyngeal carcinoma and adenoid cystic carcinoma, are rapidly proliferating tumours that can respond to DNA-damaging chemotherapy. Historic Phase II trials of mitoxantrone in head and neck cancer showed modest activity, and response rates were low. Interest has recently revived with liposomal mitoxantrone, which has a completed Phase Ib study in recurrent/metastatic disease and several ongoing Phase II/III nasopharyngeal carcinoma trials.

The link is plausible, but it rests on a general cytotoxic class effect rather than a disease-specific mechanism. A randomized Phase III trial has not yet reported.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04902027](https://clinicaltrials.gov/study/NCT04902027) | Phase 1 | Completed | 45 | Single-arm Phase Ib of liposomal mitoxantrone in recurrent/metastatic head and neck cancer, evaluating safety and preliminary efficacy |
| [NCT05717764](https://clinicaltrials.gov/study/NCT05717764) | Phase 3 | Not yet recruiting | 500 | Randomized study of liposomal mitoxantrone plus capecitabine vs capecitabine alone in platinum-refractory recurrent/metastatic nasopharyngeal carcinoma |
| [NCT06472713](https://clinicaltrials.gov/study/NCT06472713) | Phase 2 | Recruiting | 32 | Single-arm study of liposomal mitoxantrone plus PD-1 blockade in previously treated recurrent/metastatic nasopharyngeal carcinoma |
| [NCT06892431](https://clinicaltrials.gov/study/NCT06892431) | Phase 2 | Not yet recruiting | 150 | JMT101 plus liposomal mitoxantrone in nasopharyngeal cancer after at least two prior lines of therapy; the contribution of mitoxantrone is hard to isolate |
| [NCT07070479](https://clinicaltrials.gov/study/NCT07070479) | Phase 2 | Recruiting | 208 | Bayesian adaptive trial of four regimens in PD-1-resistant nasopharyngeal carcinoma; one arm is liposomal mitoxantrone plus anti-PD-1, and mitoxantrone is not the primary agent |
| [NCT07354698](https://clinicaltrials.gov/study/NCT07354698) | Phase 4 | Not yet recruiting | 114 | Mitoxantrone as a lymph node tracer in transoral robotic thyroid cancer surgery (a diagnostic/surgical use, not antitumour) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Phase 1b study | Oral Oncology | Liposomal mitoxantrone in recurrent/metastatic head and neck squamous cell carcinoma, evaluating safety and efficacy |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II | Anti-Cancer Drugs | Ifosfamide plus mitoxantrone in recurrent/metastatic squamous cell carcinoma of the head and neck (22 patients) |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II | Anti-Cancer Drugs | Mitoxantrone plus cisplatin in recurrent/metastatic salivary gland malignancies (14 patients) |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II | Annals of Oncology | EORTC study of mitoxantrone in adenoid cystic carcinoma of the head and neck |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Phase II | Am J Clin Oncol | Mitoxantrone 14 mg/m² in 19 patients with incurable head and neck carcinoma |
| [6511239](https://pubmed.ncbi.nlm.nih.gov/6511239/) | 1984 | Phase II | Investigational New Drugs | Mitoxantrone every 3 weeks in advanced head and neck cancer |
| [4066226](https://pubmed.ncbi.nlm.nih.gov/4066226/) | 1985 | Phase II | Investigational New Drugs | Southeastern Cancer Study Group trial; 53 evaluable patients with advanced squamous cell carcinoma |
| [6511243](https://pubmed.ncbi.nlm.nih.gov/6511243/) | 1984 | Phase II | Investigational New Drugs | Southwest Oncology Group trial; 1 partial response among 22 evaluable patients, with no significant antitumour activity and leukopenia and thrombocytopenia as the main toxicities |
| [34659878](https://pubmed.ncbi.nlm.nih.gov/34659878/) | 2021 | Review | Am J Cancer Res | Systemic therapies for salivary gland adenoid cystic carcinoma |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Systematic review | Bulletin du Cancer | Systemic treatments for recurrent/metastatic adenoid cystic carcinoma of the head and neck |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02286300 | MITOXANTRONE INJECTION | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracenedione, topoisomerase II inhibitor) |
| Myelosuppression Risk | High (leukopenia and thrombocytopenia are the main toxicities reported in head and neck Phase II trials) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function, and cardiac function (cardiotoxicity is a documented concern) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from graph relationships, not label text): liver failure, liver disease, gallbladder disease, heart failure, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia, macrocytic anaemia, epilepsy, infectious disease, fungal infectious disease, dermatophytosis.
- **Drug Interactions** (100 interactions recorded):
  - Major: dolasetron.
  - Moderate: clarithromycin, eliglustat, rolapitant.
  - Minor: levofloxacin.
  - Many others are of unknown severity, including metformin, amphotericin B, hydrocortisone, and several proton pump inhibitors.

Package insert warnings and contraindications were not available. Please refer to the Health Canada package insert for authoritative safety information.

---

## Other Predicted Indications

| Predicted Indication | Score | Evidence Level | Summary |
|------|------|------|------|
| Upper aerodigestive tract neoplasm | 0.9978 | L5 | No linked trials. Literature is indirect, consisting of reviews, pharmacokinetics, and small studies in nasopharyngeal and salivary gland cancers. |
| Small cell lung carcinoma | 0.9943 | L4 | No linked trials. Literature is preclinical or pharmacokinetic, and ABC transporter-mediated resistance is a concern. |
| Primary pulmonary lymphoma | 0.9941 | L4 | No dedicated trials. Only a small series of fludarabine plus mitoxantrone regimens in lung marginal zone lymphoma. |
| Well-differentiated fetal adenocarcinoma of the lung | 0.9937 | L5 | Model prediction only; no trials or literature. |
| Pulmonary blastoma | 0.9935 | L5 | Model prediction only; no trials or literature. |
| Bladder exstrophy-epispadias-cloacal exstrophy complex | 0.9900 | L5 | A congenital malformation with no plausible antineoplastic mechanism, so this is likely a prediction artifact. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (head and neck cancer); Hold for the remaining predictions**

**Rationale:**
Head and neck cancer, particularly nasopharyngeal carcinoma, has the strongest repurposing signal. It has a completed Phase Ib study, a 2025 publication, and ongoing Phase II and Phase III trials of liposomal mitoxantrone. However, older Phase II trials showed low response rates, and the Phase III trial has not yet reported. The other predictions lack direct clinical evidence or are implausible.

**To proceed, the following is needed:**
- Results from the liposomal mitoxantrone Phase Ib study and the Phase III nasopharyngeal carcinoma trial
- Clarification of whether the liposomal formulation is available in Canada, since the only Canadian product (DIN 02286300) is a standard injection with no indication or dosage form recorded
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A cardiac and haematological monitoring plan, given the knowledge graph contraindications for heart failure and cytopenias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

