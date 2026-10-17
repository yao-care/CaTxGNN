---
layout: default
title: Doxorubicin
parent: High Evidence (L1-L2)
nav_order: 304
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Doxorubicin: predicted new indication Ewing sarcoma (evidence level L1). Approved use: Acute lymphoblastic leukemia, Hodgkin lymphoma, non-Hodgkin lymphoma…"
monitor_inn: "Doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
---

# Doxorubicin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Doxorubicin: From Lymphoma and Leukemia to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is an anthracycline chemotherapy drug originally used for acute lymphoblastic leukemia, Hodgkin and non-Hodgkin lymphoma, mantle cell lymphoma and related blood cancers.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **28 clinical trials** and **20 publications** currently supporting this direction.
Doxorubicin is already part of standard multi-agent Ewing sarcoma regimens, so this prediction is closer to confirming an existing practice than to discovering a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia, Hodgkin lymphoma, non-Hodgkin lymphoma, mantle cell lymphoma (approved-indication text for Canadian licences is not available; the original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Doxorubicin is a topoisomerase II poison and DNA intercalator. It damages DNA in rapidly dividing cells, which makes it active against fast-growing small round cell sarcomas such as Ewing sarcoma. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on well-established pharmacology.

Its original indications (leukemias and lymphomas) are also fast-proliferating cancers that respond to DNA-damaging chemotherapy. In Ewing sarcoma, doxorubicin is a backbone of standard regimens such as VDC/IE (vincristine, doxorubicin, cyclophosphamide alternating with ifosfamide and etoposide) and VAC. Several Phase 3 randomized trials of these regimens include doxorubicin, including interval-compressed chemotherapy studies, EURO-EWING 99 and a ganitumab combination trial.

The main limitation is that most of these trials test the whole regimen or an added drug, not doxorubicin alone, so its individual contribution is hard to isolate.

---

## Clinical Trial Evidence

The table lists the 10 most relevant of the trials compiled for Ewing sarcoma.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy compared with standard regimens in Ewing sarcoma and related tumors |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to a standard 5-drug regimen (including doxorubicin) in non-metastatic disease |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Standard vs. intensified treatment in non-metastatic Ewing sarcoma |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: chemotherapy with or without radiotherapy, surgery or stem cell transplantation |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy in metastatic Ewing sarcoma |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not reported | EICESS 92: comparison of combination chemotherapy regimens plus surgery and radiotherapy |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | Terminated | 46 | Randomized VAC with dexrazoxane, with or without ImmTher, in high-risk disease; terminated early |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Completed | Not reported | Randomized VAC with dexrazoxane, with or without ImmTher, in newly diagnosed high-risk disease |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not reported | Multi-agent regimen including doxorubicin followed by resection and radiotherapy |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | Active, not recruiting | 83 | Irinotecan and temozolomide added to alkylator-based chemotherapy; doxorubicin is part of the background regimen |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma and PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012: open-label Phase 3 comparison of two chemotherapy strategies |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma (Children's Oncology Group) |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy for localized Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | EURO EWING 2012 protocol comparing induction and consolidation regimens |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | Consensus recommendations on Ewing sarcoma management from the National Ewing Sarcoma Tumor Board |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and future approaches to Ewing sarcoma |
| [25993235](https://pubmed.ncbi.nlm.nih.gov/25993235/) | 2015 | Review | ASCO Educ Book | Systemic therapy for osteosarcoma and Ewing sarcoma |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Dose-intensity analysis | J Natl Cancer Inst | Doxorubicin dose intensity in relation to response and outcome in osteogenic and Ewing sarcoma |
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Review | ASCO Educ Book | Predicting and preventing anthracycline-related cardiotoxicity |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02194465 | Doxorubicin Hydrochloride for Injection USP | Not listed | Not listed |
| 02194473 | Doxorubicin Hydrochloride for Injection USP | Not listed | Not listed |
| 02410397 | Doxorubicin | Not listed | Not listed |
| 02238389 | Caelyx (liposomal doxorubicin) | Not listed | Not listed |
| 02493020 | Taro-Doxorubicin Liposomal | Not listed | Not listed |

Seven single-ingredient licences are valid in Canada; the five above are shown, and none has been cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor and DNA intercalator) |
| Myelosuppression Risk | High (neutropenia, leukopenia, thrombocytopenia and anemia are listed among the knowledge-graph contraindications) |
| Emetogenicity Classification | Moderate to high at typical combination doses; please refer to the package insert |
| Monitoring Items | CBC with differential, liver function (including bilirubin), renal function, and cardiac function (baseline and serial echocardiography or LVEF; cumulative dose tracking) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text)**: The graph links doxorubicin to liver failure and liver disease, hyperbilirubinemia, thrombocytopenia, neutropenia, leukopenia, agranulocytosis, anemia, heart disease, cardiovascular disease, cardiomyopathy, congestive heart failure and heart failure, heart conduction disease, sudden cardiac arrest, and infectious disease including fungal infection. These should be checked against the Health Canada label.
- **Cardiotoxicity guardrails**: Cumulative dose limits and cardiac monitoring are needed, with consideration of dexrazoxane cardioprotection. The literature compiled for this report also highlights anthracycline-related cardiotoxicity.
- **Drug Interactions**: 100 interactions were found. The ones shown include:
  - **Major**: dolasetron, cisapride, papaverine
  - **Moderate**: aprepitant, ondansetron, granisetron, palonosetron, rolapitant, dexamethasone, clarithromycin, levofloxacin, famotidine, loperamide, eliglustat, metreleptin, troglitazone, picosulfuric acid, polyethylene glycol with electrolytes

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 randomized trials of regimens containing doxorubicin support its use in Ewing sarcoma, and the regimens (VDC/IE, VAC) are established standard care. The drug is marketed in Canada, but cumulative cardiotoxicity and myelosuppression require strict safety controls.

**To proceed, the following is needed:**
- Health Canada label warnings, contraindications and approved-indication text, which were not available in the data compiled for this report
- Mechanism of action data from DrugBank
- Evidence isolating doxorubicin's own contribution within multi-drug regimens
- A cardiac monitoring plan (baseline and serial echocardiography, cumulative dose limits, dexrazoxane consideration)
- A review of the major drug interactions against the intended supportive-care medicines (for example antiemetics)

**Other predicted indications (for reference):**
- **Pulmonary blastoma and rhabdomyosarcoma**: Doxorubicin has plausible activity, with a Phase 3 trial under way for pleuropulmonary blastoma and large Phase 3 soft-tissue sarcoma trials relevant to rhabdomyosarcoma. These are research questions or need guardrails, and doxorubicin is not the standard backbone for pediatric rhabdomyosarcoma.
- **Chronic myelogenous leukemia, monocytic leukemia, primary pulmonary lymphoma, other rhabdomyosarcoma subtypes, ganglioneuroblastoma, and a rare lung tumor (well-differentiated fetal adenocarcinoma)**: Evidence is limited to case reports, preclinical work or indirect trials, so these should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

