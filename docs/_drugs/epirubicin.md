---
layout: default
title: Epirubicin
parent: Moderate Evidence (L3-L4)
nav_order: 337
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Epirubicin: predicted new indication Primary pulmonary lymphoma (evidence level L4). Approved use: Breast carcinoma / breast neoplasm"
---

# Epirubicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Epirubicin: From Breast Cancer to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy drug, originally used to treat breast cancer.
The TxGNN model predicts it may be effective for **primary pulmonary lymphoma**,
but there are **no registered clinical trials** and only **6 publications** (mostly reviews, case reports and retrospective series) behind this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast carcinoma / breast neoplasm (the Canadian licence record has no indication text) |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, epirubicin is an anthracycline (a topoisomerase II inhibitor and DNA intercalator) and a close relative of doxorubicin. Its efficacy in breast cancer is established.

Anthracyclines are a backbone of many lymphoma regimens, and epirubicin has appeared in regimens such as CEOP and VEBEP (the latter used in Hodgkin's disease). This gives a plausible mechanistic link to lymphoid malignancies, including primary pulmonary lymphoma.

However, the modern standard for diffuse large B-cell lymphoma is doxorubicin-based (R-CHOP, Pola-R-CHP). Epirubicin has not been specifically evaluated in primary pulmonary lymphoma, so the prediction is plausible but unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary pulmonary lymphoma.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Review of epirubicin pharmacology and use across cancers; efficacy similar to doxorubicin regimens in several malignancies |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | Cancer J Sci Am | VEBEP plus involved-field radiotherapy in advanced Hodgkin's disease: long-term efficacy and toxicity |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Cohort | Ann Hematol | Retrospective study of Pola-R-CHP in 117 DLBCL patients, including trial-ineligible and low-IPI patients |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Clinical features and prognostic factors of primary extranodal DLBCL in the rituximab era |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Transl Cancer Res | Misdiagnosed primary pleural MALT lymphoma, with literature review |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Review | Rev Invest Clin | Case of primary non-Hodgkin lymphoma of the lung |

Most of these papers address related lymphomas or general epirubicin use, and none directly tests epirubicin in primary pulmonary lymphoma.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02324091 | EPIRUBICIN FOR INJECTION | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor / DNA intercalator) |
| Myelosuppression Risk | High (the knowledge graph links the drug to neutropenia, thrombocytopenia and agranulocytosis as contraindication-related conditions; myelosuppression is dose-limiting for this class) |
| Emetogenicity Classification | Moderate to high (typical for anthracyclines) |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (e.g., LVEF) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (these come from a knowledge graph, not from label text):
  - Liver: liver failure, liver disease, gallbladder disease
  - Kidney: kidney disease, pyoureter
  - Blood: thrombocytopenia, neutropenia, agranulocytosis, hemoglobinopathy
  - Heart: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, myocardial disorder
  - Other: stomatitis
- **Drug Interactions**: 100 interactions were found in total. Examples of the major-level ones in the data reviewed:
  - Cimetidine (Major)
  - Dolasetron (Major)
  - Moderate-level examples include clarithromycin, levofloxacin, famotidine, bupropion and palonosetron.
- **Other notes**: The literature on epirubicin also documents a risk of secondary leukemia (AML/MDS) after adjuvant use.

The Health Canada package insert warnings were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.71%), but there are no registered trials and no direct evidence in primary pulmonary lymphoma. Doxorubicin-based regimens are the established standard, and epirubicin has no defined role in this disease. The safety profile (cardiac, haematological) is demanding.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications, and the approved indication text
- Disease-specific evidence, such as retrospective series or trials of epirubicin-containing regimens in pulmonary or extranodal lymphoma
- Comparative evidence against doxorubicin-based standard regimens (e.g., R-CHOP)
- A cardiac and haematological safety monitoring plan

**Other predictions to consider:** In the same analysis, **small cell lung carcinoma** (score 99.69%) has stronger support, including a Phase 3 RCT of cisplatin/etoposide with or without epirubicin and cyclophosphamide (NCT00003606). However, it is not shown to beat the current standard of platinum-etoposide plus immune checkpoint inhibitor. **Upper aerodigestive tract neoplasm** (mainly gastroesophageal cancer; score 99.06%) is supported by randomized evidence in which epirubicin is part of the ECF/EOX backbone, such as the MAGIC-type trial (PMID 16822992). These two are better candidates for a further research question than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

