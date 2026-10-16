---
layout: default
title: Cabozantinib
parent: Moderate Evidence (L3-L4)
nav_order: 144
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Cabozantinib: predicted new indication Liposarcoma (evidence level L3). Approved use: Renal cell carcinoma (nonpapillary, clear cell)"
---

# Cabozantinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is an oral multikinase inhibitor originally used to treat renal cell carcinoma and medullary thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, but the support so far is early: **1 clinical trial** (Phase 2, in soft tissue sarcoma generally) and **1 publication** (Phase 1) are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (nonpapillary, clear cell); medullary thyroid carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold (treat as a research question) |

The original indications come from the TxGNN knowledge graph, because the Canadian licence records compiled for this report contain no indication text.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the analysis in the data, cabozantinib inhibits MET, VEGFR2 and AXL. These kinases drive angiogenesis and tumour progression, and they are implicated in soft tissue sarcomas.

Cabozantinib's activity in renal cell carcinoma is well established. Liposarcoma is a soft tissue sarcoma subtype, so a mechanistic link is plausible. However, the available data are not specific to liposarcoma, and efficacy in this subtype remains unknown.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomized comparison of ipilimumab + nivolumab alone versus combined with cabozantinib in advanced soft tissue sarcoma. Liposarcoma is probably among the enrolled histologies, but no results are posted. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | American Journal of Clinical Oncology | Evaluated the safety of neoadjuvant cabozantinib with concurrent radiation therapy in extremity sarcomas. Cabozantinib shows activity in several soft tissue sarcoma subtypes, but combining it with radiation raised concern about fistula or perforation. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02480824 | CABOMETYX | Not listed | Not listed |
| 02480832 | CABOMETYX | Not listed | Not listed |
| 02480840 | CABOMETYX | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine monitoring typically includes CBC, liver and renal function, and blood pressure |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen found 100 interacting drugs in total. The 20 reviewed include:
  - **Major**: acetylsalicylic acid, cisapride, clarithromycin, dolasetron, granisetron, levofloxacin
  - **Moderate**: loperamide, aprepitant, dexamethasone, bisacodyl, castor oil, clotrimazole, fenfluramine, dexfenfluramine, lactulose, lactitol, glycerin, glycerol phenylbutyrate, magnesium citrate
  - **Minor**: fidaxomicin

  Several of the major interactions involve drugs that prolong the QT interval or affect CYP3A4 metabolism. Concomitant use needs a pharmacist's review.

Warnings and contraindications from the Canadian package insert were not available in the data compiled for this report. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence for liposarcoma is a Phase 2 trial in soft tissue sarcoma overall (no results posted) and a Phase 1 safety study. Neither shows efficacy specific to liposarcoma. The package insert safety data are also missing, which blocks the safety screening step. The TxGNN score is high (99.83%), but the evidence supports further investigation rather than clinical adoption.

**To proceed, the following is needed:**
- Results from NCT05836571, especially the liposarcoma subgroup
- Liposarcoma-specific efficacy data (e.g., a dedicated Phase 2 trial)
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data
- A review of the interaction risks listed above

## Other Predicted Indications Worth Noting

The same prediction list contains candidates with stronger evidence than liposarcoma:

- **Unclassified renal cell carcinoma** (score 99.75%, L2, Proceed with Guardrails): Several Phase 2 trials (e.g., NCT04413123, NCT03635892, NCT03541902) and published Phase 2 results (PMID 35298296, 38782695) in non-clear cell RCC support activity. Unclassified RCC is a heterogeneous subgroup and no Phase 3 evidence exists.
- **Renal carcinoma** (score 99.66%, L1, Proceed with Guardrails): This is the approved indication family. Phase 3 trials (METEOR, CheckMate 9ER, CONTACT-03, COSMIC-313) support benefit, so it is on-label use rather than true repurposing.
- **Low-evidence predictions** (ovarian myxoid liposarcoma, RCC associated with neuroblastoma, amyotrophic lateral sclerosis, polymicrogyria, angiolipoma): No trials or literature were found, and the recommendation is Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

