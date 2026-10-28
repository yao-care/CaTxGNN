---
layout: default
title: Vorinostat
parent: Model Prediction Only (L5)
nav_order: 982
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Vorinostat: predicted new indication Primary cutaneous B-cell lymphoma (evidence level L5). Approved use: Primary cutaneous T-cell lymphoma"
monitor_inn: "VORINOSTAT"
predicted_indications: ["primary cutaneous B-cell lymphoma", "Sezary syndrome"]
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vorinostat: From Primary Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Vorinostat is an HDAC inhibitor originally used to treat primary cutaneous T-cell lymphoma.
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma**,
but evidence for this specific indication is limited: **4 early-phase clinical trials** with indirect relevance and **1 preclinical publication** (in mantle cell lymphoma). A second prediction, Sezary syndrome, is closely related to the original indication and is covered at the end of this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary cutaneous T-cell lymphoma (the Canadian licence record contains no indication text) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 (supportive evidence is indirect; no completed Phase 2/3 trial in this indication) |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on known class information, vorinostat is a class I/II histone deacetylase (HDAC) inhibitor. It increases acetylation of histones and other proteins, which can trigger apoptosis and cell-cycle arrest in lymphoid cancer cells.

Its efficacy in cutaneous T-cell lymphoma is established. A preclinical study (PMID 21652541) showed vorinostat induces apoptosis in mantle cell lymphoma, a B-cell neoplasm, by acetylating proapoptotic BH3-only gene promoters. This makes the mechanism biologically plausible in B-cell lymphomas generally.

However, no data are specific to primary cutaneous B-cell lymphoma. The very high TxGNN score is a computational prediction only and should not be read as clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib plus vorinostat in relapsed Hodgkin, B-cell non-Hodgkin and peripheral T-cell lymphomas; combination safety and dosing, no cutaneous-specific efficacy |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat in solid tumours and lymphomas with hepatic dysfunction; safety and pharmacokinetics |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat with tacrolimus and methotrexate to prevent graft-versus-host disease after transplant; not a lymphoma treatment study |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | Not reported | Oral vorinostat (SAHA) in advanced solid tumours and haematological malignancies; general dose and safety data |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical/in vitro | Clin Cancer Res | Vorinostat induces apoptosis in mantle cell lymphoma through acetylation of proapoptotic BH3-only gene promoters |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02327619 | ZOLINZA | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/epigenetic therapy (HDAC inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (the knowledge graph lists thrombocytopenia and anaemia as contraindication-related conditions) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood counts (including platelets), electrolytes (potassium, calcium), blood glucose, liver function, and ECG/QT interval, based on the associated conditions below |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Official label warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

- **Conditions flagged in the knowledge graph (not label text):** long QT syndrome (including familial), liver disease, gallbladder disease, thrombocytopenia, anaemia (including macrocytic), hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, pulmonary embolism, and diarrhoeal disease.
- **Drug interactions:** 61 interactions were identified; the 20 listed in the data compiled for this report are all rated Moderate. They are mainly glucose-lowering agents, including metformin, pioglitazone, glimepiride, glipizide, glyburide, insulin (human and aspart), acarbose, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), DPP-4 inhibitors (alogliptin, linagliptin) and GLP-1 agonists (albiglutide, dulaglutide, exenatide, semaglutide). Blood glucose should be monitored when combined.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for primary cutaneous B-cell lymphoma is a high computational score, one preclinical study in a different B-cell lymphoma, and early-phase trials that are not specific to this disease. There is no efficacy signal in the target indication.

**To proceed, the following is needed:**
- Disease-specific preclinical or case-series data in primary cutaneous B-cell lymphoma
- The Health Canada package insert, to confirm warnings and contraindications
- Detailed mechanism of action data
- Comparison with the current standard of care for cutaneous B-cell lymphoma

---

## Additional Note: Second Predicted Indication, Sezary Syndrome

The second prediction, **Sezary syndrome** (score 0.9907), is a leukaemic variant of cutaneous T-cell lymphoma, vorinostat's original indication. It is therefore essentially an on-label or closely related use rather than true repurposing.

- **Evidence level:** L1, with a recommendation of **Proceed with Guardrails**.
- **Key trials:**
  - [NCT01728805](https://clinicaltrials.gov/study/NCT01728805) (MAVORIC, Phase 3, completed, n=372): mogamulizumab versus vorinostat in previously treated CTCL. Vorinostat was the comparator and had lower progression-free survival.
  - [NCT00091559](https://clinicaltrials.gov/study/NCT00091559) (Phase 2b, completed, n=74): oral vorinostat in advanced CTCL, the pivotal single-arm study.
- **Key literature:**
  - [PMID 30100375](https://pubmed.ncbi.nlm.nih.gov/30100375/): MAVORIC randomised Phase 3 trial, *Lancet Oncology*, 2018.
  - [PMID 17594194](https://pubmed.ncbi.nlm.nih.gov/17594194/): review of vorinostat's approval for CTCL.
- **Caveat:** vorinostat is now mainly a comparator and later-line option, since mogamulizumab outperformed it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

