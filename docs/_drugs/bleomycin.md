---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 118
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Bleomycin: From Cytotoxic Cancer Chemotherapy to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a cytotoxic anticancer drug, and the literature in this pack shows it used in lymphoma and germ cell tumour regimens.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, but there are **0 clinical trials** and only **3 publications** (a case report and two cohort studies) that mention the disease. None of them tests bleomycin for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; bleomycin is a cytotoxic antineoplastic used in lymphoma and germ cell tumour regimens |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on general pharmacology, bleomycin causes DNA strand breaks through an iron-dependent free-radical mechanism. This is plausible against rapidly proliferating tumours.

There is no bleomycin-specific link to cauda equina neoplasm in the retrieved evidence. The three publications only mention the cauda equina in other contexts:
- A Hodgkin lymphoma patient with paraneoplastic neuropathy showed cauda equina enhancement on MRI.
- A CNS germinoma cohort was treated with a regimen containing bleomycin.
- An autopsy finding of cauda equina involvement in non-Hodgkin lymphoma.

The very high score (0.993) most likely reflects graph proximity to lymphoma and germ cell tumour nodes in the knowledge graph. It does not reflect direct evidence.

Bleomycin also penetrates the central nervous system poorly, which is a further obstacle for a spinal-canal tumour.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case report | Rinsho Shinkeigaku | Paraneoplastic sensory neuropathy in a 17-year-old with Hodgkin lymphoma; MRI showed enhancement of the trigeminal nerves and cauda equina. |
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Retrospective cohort | J Clin Oncol | Radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy (carboplatin, etoposide, bleomycin). |
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Cohort | Am J Clin Oncol | CNS involvement in 277 patients with aggressive non-Hodgkin lymphoma; one case involved the cauda equina, found at autopsy. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2131692 | BLEOMYCIN FOR INJECTION USP |
| 2265982 | BLEOMYCIN FOR INJECTION |

---

## Cytotoxicity

The pack contains no DrugBank category or toxicity data. The entries below are general background knowledge, so please confirm them against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (glycopeptide antibiotic) |
| Myelosuppression Risk | Low relative to most cytotoxics (described in the literature as "marrow-sparing") |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function (main dose-limiting toxicity), CBC, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature also describes dose-related pulmonary toxicity (fibrosis, pneumonitis) with bleomycin, and a case of fatal hyperpyrexia in a lymphoma patient.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trial or study tests bleomycin in cauda equina neoplasm, and its poor CNS penetration and pulmonary toxicity argue against pursuing it without new evidence.

**To proceed, the following is needed:**
- Bleomycin-specific evidence in primary spinal or cauda equina tumours, such as case series, preclinical work or intrathecal/intratumoral delivery studies
- Mechanism of action data and a feasibility assessment of CNS or spinal delivery
- Health Canada package insert warnings and contraindications, and approved indication text for both DINs

The same Evidence Pack contains five other predictions. Reticulum cell sarcoma (an older term for diffuse large-cell non-Hodgkin lymphoma) has the strongest support in the pack (L1, with completed Phase 3 trials of bleomycin-containing regimens). It is worth evaluating as a separate candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

