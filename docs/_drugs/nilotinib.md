---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 646
evidence_level: L5
indication_count: 1
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Nilotinib: From Chronic Myeloid Leukaemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor (TKI) that is generally known for treating BCR-ABL-driven leukaemia. The supplied licence records do not state its approved indication, so this is background knowledge rather than Evidence Pack data. The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but only **1 publication** (a mechanism-level review) and **no clinical trials** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian licence records (generally known as a BCR-ABL inhibitor for chronic myeloid leukaemia) |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (mechanism-level literature only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nilotinib is not available in the supplied data. Based on general pharmacology, nilotinib inhibits several tyrosine kinases, including BCR-ABL, PDGFR and KIT.

DFSP is typically driven by a COL1A1-PDGFB gene fusion. This fusion produces a growth signal that continuously activates the PDGFRB receptor. A PDGFR-blocking TKI is therefore biologically plausible for this tumour. Imatinib, which acts through the same class mechanism, is the established PDGFR inhibitor for DFSP, and nilotinib shares that target profile.

The TxGNN score of 0.993 is a computational prediction only and is not clinical evidence. No nilotinib-specific DFSP trial data were supplied. The mechanistic link is inferred from general pharmacology and has not been verified against nilotinib-specific studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors in neoplastic disorders, covering PDGF biology and receptor signalling. It supports the PDGFR-inhibition rationale but is not nilotinib-specific clinical evidence. |

---

## Canada Market Information

Six licences are recorded in total. The five below were supplied; dosage form and approved-indication text were not available in the records.

| DIN | Product Name |
|---------|------|
| 2368250 | TASIGNA |
| 2315874 | TASIGNA |
| 2550903 | APO-NILOTINIB |
| 2556634 | REDDY-NILOTINIB |
| 2556642 | REDDY-NILOTINIB |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for nilotinib in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, because DFSP is PDGFRB-driven and nilotinib inhibits PDGFR. However, the evidence is limited to a single mechanism-level review and a model score, with no nilotinib-specific clinical trials. The Health Canada safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications), obtained and parsed to unblock safety screening
- Mechanism-of-action data for nilotinib (e.g., via the DrugBank API) and the approved indications from the licence records
- A targeted search for nilotinib-specific DFSP evidence (case series, trials, ICTRP registries)
- A comparison against imatinib, the established DFSP therapy, including imatinib-resistant or imatinib-intolerant populations
- A safety and monitoring plan once the monograph data are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

