---
layout: default
title: Oxaliplatin
parent: Model Prediction Only (L5)
nav_order: 685
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a platinum-based chemotherapy drug, best known for colorectal cancer. The Canadian licence entries in the Evidence Pack do not include indication text, so this original use comes from general drug knowledge.
The TxGNN model predicts it may be effective for **malignant pleural mesothelioma**. **5 registered clinical trials** (only 2 directly relevant) and **20 publications** touch on this direction, but the evidence is small, early-phase and has no phase 3 confirmation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data provided; colorectal cancer by general knowledge |
| Predicted New Indication | Malignant pleural mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 (as assigned in the Evidence Pack; the trials are single-arm phase 2 studies, not randomized, so this sits at the low end of L2) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank. Based on its known class, oxaliplatin is a DACH-platinum compound that forms DNA adducts and crosslinks, which block DNA synthesis and trigger cancer cell death.

Mesothelioma is a platinum-responsive tumour. Cisplatin or carboplatin combined with pemetrexed is the established first-line backbone. Because oxaliplatin shares the platinum DNA-damage mechanism, it is a plausible substitute or partner in this setting. Small phase 2 studies have tested it with gemcitabine, raltitrexed, vinorelbine and bortezomib, in both pretreated and chemotherapy-naive patients.

The results are mixed, and no phase 3 randomized trial shows oxaliplatin is better than standard platinum regimens. Two other predictions in the same family have weaker support:
- **Malignant epithelioid mesothelioma:** evidence comes mainly from peritoneal disease treated with HIPEC or PIPAC, and is retrospective or feasibility-level.
- **Sarcomatoid mesothelioma and malignant visceral pleura tumor:** no disease-specific oxaliplatin data were found.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin plus gemcitabine as first- or second-line chemotherapy in pleural or peritoneal mesothelioma. The primary question is response rate. Direct match, but small and single-arm. |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib plus oxaliplatin in previously treated pleural or peritoneal mesothelioma. No results available. |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | International PIPAC registry for peritoneal and pleural malignancies. Indirect procedural and safety context only. |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | Dose escalation of the CBL-B inhibitor NX-1607 in advanced cancers. Oxaliplatin is not the tested drug, so this is a spurious match. |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant cadonilimab plus chemotherapy in esophagogastric junction and gastric cancer. A different disease, so no mesothelioma evidence. |

---

## Literature Evidence

No randomized controlled trials were found. The table lists phase 2 studies first, then reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 | J Clin Oncol | Raltitrexed plus oxaliplatin in 70 patients (15 pretreated, 55 chemotherapy-naive). Reported as an active regimen in mesothelioma. |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 | Clin Lung Cancer | Multicenter gemcitabine plus oxaliplatin study in 25 patients, up to 6 cycles. |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 | Lung Cancer | Vinorelbine plus oxaliplatin as first-line therapy in untreated pleural mesothelioma. |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 | Lung Cancer | Raltitrexed plus oxaliplatin as second-line therapy was inactive. Among 14 patients there were no objective responses, and 4 had stable disease. |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Pilot phase 2 | Tumori | Oxaliplatin plus raltitrexed in inoperable pleural mesothelioma. |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Observational | J Occup Med Toxicol | Oxaliplatin with or without gemcitabine in patients pretreated with pemetrexed. Efficacy and safety were assessed. |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | Chemotherapy for pleural mesothelioma. Response rates above 30% were rarely reached with established cytotoxic drugs. |
| [15261443](https://pubmed.ncbi.nlm.nih.gov/15261443/) | 2004 | Review | Lung Cancer | Update of the same review, with newer agents and combinations looking somewhat more promising. |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Antifolate-based regimens, including raltitrexed/oxaliplatin and pemetrexed/cisplatin, as emerging options. |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | Effect of cisplatin, oxaliplatin and pemetrexed on immune checkpoint expression, to guide combination with immunotherapy. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2458403 | OXALIPLATIN INJECTION, USP |
| 2444763 | OXALIPLATIN |
| 2435071 | OXALIPLATIN INJECTION |
| 2457423 | OXALIPLATIN INJECTION, USP |
| 2436957 | OXALIPLATIN INJECTION |

---

## Cytotoxicity

The Evidence Pack has no DrugBank categories or toxicity data for this drug. The entries below reflect general platinum-class knowledge, and the package insert should be consulted for confirmation.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | Medium (neutropenia and thrombocytopenia are common) |
| Emetogenicity Classification | Medium |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, and neurological assessment for peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mesothelioma evidence consists of small phase 2 studies, two of which have no reported results. One second-line study found raltitrexed plus oxaliplatin inactive. No phase 3 trial shows an advantage over the established platinum plus pemetrexed standard. The safety data is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Indication text and dosage forms for the Canadian licences
- Results or publication of NCT00859469 and NCT00996385
- A comparative trial against the standard platinum plus pemetrexed regimen, or a justification of a niche such as pemetrexed-pretreated patients
- Histology-specific data for epithelioid, sarcomatoid and visceral pleura tumours
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

