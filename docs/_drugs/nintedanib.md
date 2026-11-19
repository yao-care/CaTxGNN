---
layout: default
title: Nintedanib
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
monitor_inn: "Nintedanib"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
description: "Nintedanib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). In Canada: 6 DINs (6 marketed)"
---

# Nintedanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nintedanib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Nintedanib was originally used to treat idiopathic pulmonary fibrosis and non-small cell lung cancer.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but at present there are **0 clinical trials** and only **1 publication** (an indirect review) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9915 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nintedanib: "Nintedanib is a small molecule that inhibits multiple receptor tyrosine kinases (RTKs) and non-receptor tyrosine kinases (nRTKs). Nintedanib inhibits the following RTKs: platelet-derived growth factor receptor (PDGFR) α and β, fibroblast growth factor receptor (FGFR) 1-3, vascular endothelial growth factor receptor (VEGFR) 1-3, colony stimulating factor 1 receptor (CSF1R), and Fms-like tyrosine kinase-3 (FLT-3)." ([DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa), label version 2026-04-21; accessed 2026-11-19.) Based on known pharmacology, nintedanib is a triple angiokinase inhibitor that blocks VEGFR1-3, FGFR1-3 and PDGFR-alpha/beta. Its efficacy in pulmonary fibrosis and lung cancer is established, and it may be mechanistically applicable to DFSP.

DFSP is driven by the COL1A1-PDGFB fusion gene. This fusion produces constitutive PDGFB autocrine activation of PDGFR-beta. Because nintedanib inhibits PDGFR, it plausibly targets this pathway. Its antifibrotic and antiangiogenic activity adds a general biological rationale.

However, the link is indirect. The only supporting item is a 2018 review on small-molecule PDGFR inhibitors, and there are no nintedanib-specific clinical data for DFSP. Imatinib is already the established PDGFR-directed therapy for DFSP, so nintedanib would need to show a clear advantage, for example in imatinib-resistant disease.

Other top-ranked predictions (liposarcoma, fibrosarcoma subtypes, fibroblastic neoplasm) have no trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors in neoplastic disorders. It supports PDGFR as a target but contains no nintedanib-specific DFSP data. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02443066 | OFEV | Not listed | Not listed |
| 02443074 | OFEV | Not listed | Not listed |
| 02526891 | AURO-NINTEDANIB | Not listed | Not listed |
| 02526905 | AURO-NINTEDANIB | Not listed | Not listed |
| 02550849 | JAMP NINTEDANIB | Not listed | Not listed |

One further licence (DIN 02540762, JAMP NINTEDANIB) is also valid, giving 6 valid single-ingredient licences in total.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase / angiokinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total. The 20 reviewed include one Major and 19 Moderate interactions.
  - **Major**: Dexamethasone.
  - **Moderate, bleeding-risk related (antithrombotics and anticoagulants)**: acetylsalicylic acid, abciximab, alteplase, antithrombin III human, apixaban, betrixaban, bivalirudin, cangrelor, caplacizumab, cilostazol, clopidogrel, dalteparin, defibrotide, desirudin and dipyridamole.
  - **Moderate, other**: clarithromycin, cobicistat, naltrexone and rolapitant.

Package-insert warnings and contraindications were not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a plausible mechanism through PDGFR inhibition in COL1A1-PDGFB-driven DFSP. However, the evidence is limited to one indirect review, with no clinical trials. Imatinib is already the established therapy, so the added value of nintedanib is unclear.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical data (for example, DFSP cell lines or imatinib-resistant models) or case series with nintedanib
- A defined clinical niche, such as imatinib-resistant or unresectable DFSP
- Review of the bleeding-risk interactions with antithrombotic drugs

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

