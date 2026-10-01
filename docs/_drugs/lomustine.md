---
layout: default
title: Lomustine
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
---

# Lomustine
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

# Lomustine: From Cancer Chemotherapy (Original Indication Not Recorded) to Lymphosarcoma

## One-Sentence Summary

Lomustine is an oral nitrosourea alkylating agent used in cancer chemotherapy, and it is marketed in Canada as CEENU.
The TxGNN model predicts it may be effective for **lymphosarcoma** (an older term for non-Hodgkin lymphoma), with **15 retrieved clinical trials** and **20 publications**.
Most of the evidence is small phase 2 studies, older combination-regimen reports and veterinary or animal work, so it supports further research rather than clinical adoption.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Lymphosarcoma |
| TxGNN Prediction Score | 99.90% (model rank 2568) |
| Evidence Level | L2 (weak: the only randomized phase 2 trial enrolled 7 patients) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

The approved indication text is empty in the input, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Based on known information, lomustine is a lipophilic nitrosourea alkylating agent. It chloroethylates DNA, forms interstrand crosslinks and carbamoylates proteins. Lymphoid cancers are generally sensitive to this kind of DNA damage. Lomustine's lipophilicity also lets it cross the blood-brain barrier, which is relevant to primary CNS lymphoma.

Lomustine has been used as one component of multi-drug lymphoma regimens for decades. Examples include LEMP, CAMP, PACET, CIBO-P, and an oral regimen of lomustine, etoposide, cyclophosphamide and procarbazine for AIDS-related lymphoma. It also appears in the procarbazine/methotrexate/lomustine backbone for elderly primary CNS lymphoma. This history makes the prediction biologically plausible.

The very high TxGNN score (0.999) does not distinguish this indication from the other nine predicted for lomustine, so it should not be read as extra confidence. No single-agent lomustine lymphoma data appear in the evidence, so the benefit cannot be separated from that of the companion drugs.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Phase 2 | Completed | 54 | Dose-modified oral lomustine, etoposide, cyclophosphamide and procarbazine in AIDS-related non-Hodgkin lymphoma (US and Africa) |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Unknown | 56 | Rituximab, high-dose methotrexate, lomustine and procarbazine, then procarbazine maintenance, in primary CNS lymphoma over age 65 |
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Phase 2 | Completed | 7 | Randomized CHOP vs oral chemotherapy (including lomustine) with antiretroviral therapy in HIV-associated lymphoma in sub-Saharan Africa; too small to interpret |
| [NCT00003114](https://clinicaltrials.gov/study/NCT00003114) | Phase 2 | Completed | 5 | Oral lomustine, etoposide, cyclophosphamide and procarbazine in AIDS-related Hodgkin disease |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Phase 2 | Completed | 1 | Methotrexate, procarbazine and CCNU (lomustine) with intraventricular cytarabine in primary CNS lymphoma; a single patient gives no efficacy information |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy plus G-CSF in elderly intermediate/high-grade non-Hodgkin lymphoma; the summary does not name lomustine |
| [NCT00003929](https://clinicaltrials.gov/study/NCT00003929) | Phase 2 | Withdrawn | 0 | Lomustine, procarbazine, filgrastim and radiation in primary CNS lymphoma; never enrolled |

These trials are mostly small, and several were terminated or withdrawn. None reports results in the input, and lomustine is always part of a combination.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | Randomized comparison | Cancer | CALGB trial of CCNU vs methyl-CCNU in advanced Hodgkin disease, lymphosarcoma and reticulum cell sarcoma; the provided excerpt gives the design but no results |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Phase 2 | Eur J Haematol | LEMP (lomustine, etoposide, methotrexate, prednisone) in 22 patients with relapsed or refractory non-Hodgkin lymphoma; results not in the provided excerpt |
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Phase 2 pilot | Ann Oncol | Adding rituximab to methotrexate, procarbazine and lomustine (R-MCP) in elderly primary CNS lymphoma; results not in the provided excerpt |
| [2259920](https://pubmed.ncbi.nlm.nih.gov/2259920/) | 1990 | Phase 2 | Semin Oncol | CAMP in 30 patients with doxorubicin-resistant intermediate/high-grade non-Hodgkin lymphoma: 27% complete and 20% partial remission |
| [8422281](https://pubmed.ncbi.nlm.nih.gov/8422281/) | 1993 | Cohort | Eur J Cancer | PACET in 27 patients with relapsed or refractory non-Hodgkin lymphoma: 26% complete response, median survival 6 months, intensely myelosuppressive |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Clinical study | Cancer | CIBO-P regimen for refractory or recurrent aggressive non-Hodgkin lymphoma; reported as effective, details not in the excerpt |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Review | Drugs | Oral lomustine, etoposide, cyclophosphamide and procarbazine in 38 patients with AIDS-related lymphoma |
| [30197327](https://pubmed.ncbi.nlm.nih.gov/30197327/) | 2018 | Cohort | J Cancer Res Ther | LACE conditioning (lomustine, cytarabine, cyclophosphamide, etoposide) before autologous transplant in relapsed or refractory lymphoma |
| [17134114](https://pubmed.ncbi.nlm.nih.gov/17134114/) | 2006 | Review | Neurosurg Focus | High-dose methotrexate is the most effective drug for primary CNS lymphoma; lomustine is one of several combination partners |
| [22888657](https://pubmed.ncbi.nlm.nih.gov/22888657/) | 2012 | Preclinical (mouse) | Vopr Onkol | Oral lomustine extended survival 1.6-fold, and combined with gemcitabine 3.3-fold, in mice with transplanted lymphosarcoma LIO-1 |

Several further papers (PMIDs 28508557, 30117253, 34464024, 29380942, 36503518, 28222789) report lomustine-containing regimens such as LOPP in dogs with lymphoma. They are veterinary cohorts and do not establish efficacy in humans.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 360422 | CEENU |
| 360430 | CEENU |

The approved indication text, dosage form and manufacturer are not recorded in the input.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent) |
| Myelosuppression Risk | High; lomustine-containing regimens are described as intensely myelosuppressive, and bone marrow aplasia has been reported after overdose |
| Emetogenicity Classification | Moderate to high (general class knowledge; confirm with the product monograph) |
| Monitoring Items | CBC with differential and platelets, liver and renal function, and pulmonary status (nitrosourea lung toxicity is documented in the literature) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

The literature also links nitrosourea-containing regimens to secondary myelodysplastic syndrome and leukemia.

---

## Safety Considerations

Please refer to the package insert for safety information. The Health Canada warnings and contraindications were not retrieved, and no drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Lomustine has a plausible mechanism and a long history in lymphoma combination regimens. The supporting trials, however, are small and often terminated or withdrawn, and the literature is older, veterinary or preclinical. Its own contribution cannot be separated from the companion drugs, and the Canadian safety data needed for screening are missing.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indication, dosage form)
- The original DrugBank mechanism-of-action data
- Confirmation that the truncated-title trials (NCT00003113 and others) actually include lomustine, and their reported results
- Controlled human data on lomustine-containing regimens in lymphoma, especially primary CNS lymphoma
- A safety monitoring plan covering delayed myelosuppression, pulmonary toxicity and cumulative dosing

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

