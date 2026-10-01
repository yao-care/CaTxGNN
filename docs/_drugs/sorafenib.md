---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 856
evidence_level: L5
indication_count: 10
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sorafenib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor, described in the supplied trial records as registered for advanced renal cell carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**.
Support is thin and indirect: **1 sorafenib Phase 2 trial** in mixed soft tissue sarcomas (not liposarcoma-specific), **1 regorafenib trial** that gives class-level context only, and **8 publications**, mostly preclinical or review articles.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (from trial descriptions; the Canadian licence record has no indication text) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 as assigned in the Evidence Pack, but effectively weaker (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

**Note on evidence level:** The only sorafenib trial in the liposarcoma record is a single-arm Phase 2 study in advanced soft tissue sarcomas. It is not an RCT, and no liposarcoma-specific results were supplied. The liposarcoma-specific literature is preclinical.

---

## Why is This Prediction Reasonable?

Sorafenib inhibits the RAF/MEK/ERK signaling pathway. It also inhibits the receptor tyrosine kinases VEGFR-2/3 and PDGFR-beta, which drive angiogenesis and tumor cell proliferation. This is the basis of its use in renal cell carcinoma, a highly vascular tumor.

Soft tissue sarcomas, including liposarcoma, also depend on these pathways. Preclinical work in dedifferentiated liposarcoma models points to MAPK signaling and PTEN loss. A 2008 study tested sorafenib in malignant peripheral nerve sheath tumor cells and in two dedifferentiated liposarcoma cell lines (LS141 and DDLS). It reported growth and MAPK-signaling inhibition in the MPNST cells, but the supplied abstract excerpt does not show the liposarcoma results.

Liposarcoma-specific clinical activity has not been shown in the supplied data. Current reviews describe histology-driven treatment of soft tissue sarcoma, with trabectedin and doxorubicin-based regimens highlighted for liposarcoma. Sorafenib is not highlighted for it. The prediction is therefore mechanistically plausible but unproven.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) in advanced soft tissue sarcomas. Direct drug evidence, but not liposarcoma-specific. No histology-level response breakdown was supplied. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 tested **regorafenib**, not sorafenib, in selected sarcoma subtypes. It is a related multikinase inhibitor and gives class-level context only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib in advanced soft tissue sarcomas. The supplied excerpt describes the rationale (raf, VEGFR, PDGFR, FLT3, c-kit inhibition) but no outcome data. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Treatment of soft tissue sarcomas by histological subtype. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven therapy. Trabectedin is highlighted for liposarcoma, especially the myxoid subtype. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (preclinical models) | Front Oncol | Patient-derived orthotopic xenograft (PDOX) sarcoma models and palbociclib combinations. Not sorafenib-specific. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibits growth and MAPK signaling in MPNST cells. Two dedifferentiated liposarcoma lines were also tested. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models show PTEN down-regulation and response to PI3K pathway inhibition. Not a sorafenib study. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Trabectedin in synovial sarcoma. Not relevant to sorafenib. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2284227 | NEXAVAR |

The licence record does not include the dosage form or approved indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor of RAF, VEGFR, and PDGFR) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction records were found in the supplied data.

One publication in the evidence set ([PMID 22016478](https://pubmed.ncbi.nlm.nih.gov/22016478/)) describes hand-foot skin reaction with sorafenib combined with cytotoxic chemotherapy. This is a known toxicity to plan for in any combination study.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible, but there is no liposarcoma-specific clinical evidence. The only sorafenib trial covers mixed soft tissue sarcomas without a histology breakdown, and the liposarcoma-specific literature is preclinical. Canadian safety information is also missing.

**To proceed, the following is needed:**
- Subtype-level results from NCT00217620 and SWOG S0505 (PMID 21751200), to see whether any liposarcoma patients responded
- Health Canada package insert warnings and contraindications
- Mechanism-of-action data from DrugBank
- A comparison against established liposarcoma options such as trabectedin and doxorubicin-based regimens, since sorafenib has no demonstrated advantage

**Other predictions in this pack:** Several have more clinical activity than liposarcoma. Female breast carcinoma has more than 10 registered sorafenib trials, mostly early phase, with no confirmed benefit. Unclassified renal cell carcinoma has a completed Phase 3 trial in advanced renal cell carcinoma, but whether unclassified histology was analyzed separately is unconfirmed. These may merit separate evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

