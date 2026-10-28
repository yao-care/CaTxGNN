---
layout: default
title: Dacarbazine
parent: Model Prediction Only (L5)
nav_order: 241
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Dacarbazine: predicted new indication Upper aerodigestive tract neoplasm (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "DACARBAZINE"
predicted_indications: ["upper aerodigestive tract neoplasm"]
---

# Dacarbazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Dacarbazine: From Hodgkin Lymphoma and Metastatic Melanoma to Upper Aerodigestive Tract Neoplasm
{: .text-alpha }

## One-Sentence Summary

Dacarbazine is an alkylating chemotherapy drug originally used for metastatic melanoma and Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm**,
but **no clinical trials** are registered for this indication, and the **20 publications** compiled are mostly indirect: reviews, case reports, and studies of related tumours.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma; Hodgkin lymphoma (including classic Hodgkin lymphoma) |
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 (no direct clinical studies; the data's preliminary grading was L4, but only indirect and mechanistic-adjacent literature exists) |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on general knowledge, dacarbazine is an alkylating agent. It is converted to an active metabolite (MTIC) that methylates DNA, and its efficacy in metastatic melanoma and Hodgkin lymphoma is established.

Melanoma and Hodgkin lymphoma can both involve the head and neck or upper aerodigestive mucosa. Examples include mucosal melanoma metastases and extranodal or nodal head and neck Hodgkin lymphoma. The high TxGNN score likely reflects these shared disease neighbourhoods rather than proven activity against primary upper aerodigestive tract carcinomas such as squamous cell carcinoma.

Indirect signals also come from dacarbazine-containing regimens in other neuroendocrine or neural-crest tumours, such as medullary thyroid carcinoma and malignant paraganglioma. No direct mechanistic evidence supports efficacy in primary upper aerodigestive tract neoplasms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below were retrieved for this prediction. None is a trial of dacarbazine in primary upper aerodigestive tract cancer. Their relevance has not yet been reviewed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | RCT (Phase 3) | JAMA Oncol | Toripalimab vs dacarbazine as first-line therapy in advanced acral melanoma. Dacarbazine is the on-label comparator, so this is not the target indication. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Clinical study | Ann Oncol | Small study of dacarbazine plus 5-FU in advanced medullary thyroid cancer, a neuroendocrine tumour. |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Retrospective cohort | Cancer | Characteristics and outcomes of Hodgkin lymphoma involving head and neck sites. |
| [31621203](https://pubmed.ncbi.nlm.nih.gov/31621203/) | 2019 | Prospective observational | Cancer Med | Carbon-ion radiotherapy plus dacarbazine, nimustine and vincristine (DAV) in 21 patients with head and neck mucosal melanoma. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohort | Ear Nose Throat J | Six patients with head and neck malignant paragangliomas; clinical, genetic and treatment features. |
| [11815960](https://pubmed.ncbi.nlm.nih.gov/11815960/) | 2002 | Preclinical | Cancer | In mouse xenografts of medullary thyroid carcinoma, dacarbazine was effective alone and combined with radioimmunotherapy. |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clin Oncol | Review of medullary thyroid carcinoma. |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Review | Transfus Apher Sci | Review of HIV-associated Hodgkin lymphoma. |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | Review of current melanoma management. |
| [12845209](https://pubmed.ncbi.nlm.nih.gov/12845209/) | 2003 | Case report | Onkologie | Stage IV melanoma with mucosal metastases to the oesophagus, stomach, bladder and tonsil. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02241445 | DACARBAZINE FOR INJECTION BP | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High. Knowledge-graph contraindications include thrombocytopenia, leukopenia and anaemia, which indicate haematological toxicity. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function, renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text)**: Kidney disease, liver disease, gallbladder disease, hepatic vein thrombosis, Budd-Chiari syndrome, pyoureter, thrombocytopenia, anaemia, macrocytic anaemia and leukopenia.
- **Drug Interactions**: 100 interactions were identified. Only the two with a graded level are listed here: naltrexone (Moderate) and levofloxacin (Minor). Other listed drugs, such as pantoprazole, morphine, metformin, omeprazole, prednisone, simvastatin, ondansetron, aprepitant and palonosetron, have an unknown severity level.

For warnings and contraindications from the label, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and no direct evidence in primary upper aerodigestive tract cancers. The literature is indirect, drawn from melanoma, Hodgkin lymphoma and neuroendocrine tumours, and the label-based safety review cannot proceed without the Health Canada package insert.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Clarification of which upper aerodigestive tract tumour types are meant (for example, mucosal melanoma versus squamous cell carcinoma)
- Relevance review of the retrieved literature and a search for direct clinical data in the target population
- Approved indication text and dosage form for DIN 02241445
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

