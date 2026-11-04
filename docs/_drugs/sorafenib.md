---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 863
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-04
monitor_inn: "SORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor (RAF/MEK/ERK, VEGFR, PDGFR, KIT) marketed in Canada as NEXAVAR.
The TxGNN model predicts it may be relevant to **liposarcoma**, with a score of 0.9982.
The evidence level is **L5**: the one registered trial and the literature address soft tissue sarcoma in general or other cell types, and none tests sorafenib in liposarcoma itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, sorafenib inhibits the RAF/MEK/ERK pathway as well as VEGFR and PDGFR, so it acts on both tumour-cell signalling and tumour blood supply.

Angiogenesis and MAPK signalling are plausible drivers in soft tissue sarcomas, which gives a theoretical basis for testing sorafenib in liposarcoma. Preclinical work in nerve sheath tumour cells and dedifferentiated liposarcoma cell lines suggests the pathway is relevant. However, the clinical signal comes from a mixed soft tissue sarcoma population and is not specific to liposarcoma. For that reason the prediction is a research hypothesis, not an established use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm trial of sorafenib in advanced soft tissue sarcomas; mixed histologies, liposarcoma only a subset; not randomized |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Phase 2 intergroup trial of sorafenib in advanced soft tissue sarcomas |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven therapy of soft tissue sarcomas |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Treatment of soft tissue sarcomas by histological subtype |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signalling in nerve sheath tumour cells; dedifferentiated liposarcoma cell lines were also studied |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models; response to PI3K pathway inhibition |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02284227 | NEXAVAR | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; typically blood counts, liver and renal function, and blood pressure |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Examples of those rated Major or Moderate include dolasetron (Major), and clarithromycin, levofloxacin, dexamethasone, famotidine, loperamide, palonosetron and naltrexone (Moderate).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests sorafenib in liposarcoma itself. The available trial and publications cover soft tissue sarcoma in general or non-liposarcoma cells, so the evidence level is L5. The high TxGNN score alone is not enough to move forward.

**To proceed, the following is needed:**
- Liposarcoma-specific clinical data, such as subgroup results from the soft tissue sarcoma trials
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A review of the interaction profile against likely co-medications

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

