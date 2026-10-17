---
layout: default
title: Chlorambucil
parent: Moderate Evidence (L3-L4)
nav_order: 180
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-13
description: "Chlorambucil: predicted new indication Pregerminal center chronic lymphocytic leukemia/small lymphocytic lym… (evidence level L4). Approved use: Hodgkin lymphoma (including classic subtypes), follicu…"
monitor_inn: "CHLORAMBUCIL"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
---

# Chlorambucil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Chlorambucil: From Hodgkin Lymphoma and Chronic B-Cell Malignancies to Pregerminal Center CLL/SLL

## One-Sentence Summary

Chlorambucil is an alkylating chemotherapy drug originally used for Hodgkin lymphoma, follicular lymphoma, acute lymphoblastic leukaemia and related B-cell malignancies.
The TxGNN model predicts it may be effective for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)**,
but there are **no registered clinical trials** and only **1 publication (a 2003 review)** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma (including classic subtypes), follicular lymphoma, mature B-cell neoplasms, acute lymphoblastic leukaemia, Richter syndrome (the Health Canada licence record contains no indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, chlorambucil is a DNA-alkylating agent, its efficacy in B-cell lymphoid malignancies is long established, and mechanistically it may be applicable to this CLL/SLL subtype.

The predicted disease sits within the CLL/SLL spectrum, a mature B-cell neoplasm closely related to the original indications. The prediction is therefore largely a subtype refinement of an existing use, not a true repurposing to a different disease area. The high score likely reflects how close this disease is to the original indications in the knowledge graph.

There are important caveats. The only supporting reference is a 2003 review on risk-adapted CLL management, which is not subtype-specific data. Modern practice also favours targeted agents (BTK inhibitors, venetoclax, anti-CD20 antibodies) over chlorambucil, especially in high-risk disease. A more recent publication (RESONATE-2) reports that ibrutinib was superior to chlorambucil in older patients with previously untreated CLL/SLL.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Nederlands tijdschrift voor geneeskunde | CLL is the most common leukaemia in the Western world and is not always indolent. Two biological subtypes exist, including a pre-germinal centre type with unmutated immunoglobulin variable-region genes, which supports a risk-adapted treatment approach. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00004626 (licence number) | LEUKERAN | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. Neutropenia, thrombocytopenia, leukopenia and anaemia appear among the knowledge-graph contraindication entries, which points to bone marrow toxicity. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, and liver and renal function. Please also refer to the package insert. |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications (knowledge-graph entries, not label text)**: the knowledge graph lists the following conditions: epilepsy; thrombocytopenia, neutropenia, agranulocytosis, leukopenia and lymphopenia; anaemia (including macrocytic anaemia); nephrotic syndrome (including familial nephrotic syndrome and lipoid nephrosis); interstitial lung disease and pulmonary fibrosis; drug-induced liver injury; and acute leukaemias (including mixed phenotype and biphenotypic types).
- **Drug Interactions**: 100 interactions were found. The main ones by severity are:
  - **Major**: deferiprone; samarium (153Sm) lexidronam.
  - **Moderate**: amphotericin B (including the lipid complex, cholesteryl sulfate and liposomal forms); mercaptopurine; roflumilast; chloramphenicol; palifermin; strontium chloride Sr-89.
  - **Minor**: levofloxacin.
  - Some interactions, such as warfarin, prednisone and omeprazole, have no severity grade assigned.
- Please also refer to the package insert for the full warnings, because label-based warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, because it is a subtype of CLL/SLL, a disease area where chlorambucil already has a long history. However, there are no registered trials and only one non-specific review, and targeted agents have largely replaced chlorambucil in this setting. The evidence is model-driven and indirect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Subtype-specific efficacy data (for example, outcomes by IGHV mutation status) and comparison with current standard-of-care targeted therapies
- Approved indication text and dosage form for the Canadian licence, to confirm how the predicted use relates to the labelled indications

### Other Predicted Indications (Brief Notes)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| CLL/SLL with IGHV somatic hypermutation | 99.72% | L5 | Prediction only, no trials or literature. Related to the approved CLL/SLL use. |
| ALK-positive large B-cell lymphoma | 99.61% | L5 | Prediction only. This aggressive lymphoma usually needs intensive combination chemotherapy. |
| Primary pulmonary lymphoma | 99.42% | L3 | Mostly MALT-type marginal zone lymphoma. Case reports, cohort data and a guideline provide indirect support, with no registered trials. This is the most promising of the additional candidates (flagged as a research question). |
| Well-differentiated fetal adenocarcinoma of the lung | 99.39% | L5 | No mechanistic rationale beyond generic alkylator activity. |
| Pulmonary blastoma | 99.37% | L5 | No specific rationale. Treated mainly with surgery and platinum-based regimens. |
| Acute lymphoblastic leukaemia | 99.25% | L4 | Already among the original indications, so not a new use. The retrieved literature does not show efficacy. |
| Small cell lung carcinoma | 99.24% | L3 | Older trials showed no durable advantage over modern standards. A 2026 preclinical conjugate study is not evidence for chlorambucil itself. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

