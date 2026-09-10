---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 585
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum-based cytotoxic agent long used in colorectal cancer chemotherapy (e.g. FOLFOX regimens), though the formal indication text was not present in this evidence pack. The TxGNN model predicts it may be effective for **Malignant Pleural Mesothelioma**, with **5 clinical trials** and **20 publications** currently supporting this direction — including several completed Phase II combination trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (per general drug information for Eloxatin®/oxaliplatin; not confirmed by Canadian regulatory data in this evidence pack) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, oxaliplatin is a diaminocyclohexane platinum compound that forms DNA platinum-crosslinks, blocking DNA replication and transcription and inducing apoptosis — the same general mechanism shared by other platinum agents (e.g. cisplatin) that are the current standard of care for malignant pleural mesothelioma (MPM).

Oxaliplatin's original use is as a cytotoxic backbone in gastrointestinal cancers (notably colorectal cancer). MPM shares a reliance on platinum-based cytotoxic chemotherapy as first-line treatment (typically cisplatin/pemetrexed), so substituting or combining oxaliplatin as an alternative platinum agent is mechanistically plausible.

This mechanistic plausibility is further supported by real clinical experience: multiple completed Phase II trials have directly tested oxaliplatin combined with gemcitabine, raltitrexed, or vinorelbine in MPM patients, showing measurable (if modest) response rates. This existing clinical body of evidence — rather than TxGNN's knowledge-graph link alone — is what elevates this candidate above a pure prediction-only signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin + gemcitabine as first- or second-line therapy for pleural/peritoneal mesothelioma; response rate evaluation |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | VELCADE (bortezomib) + Eloxatin (oxaliplatin) in previously treated pleural/peritoneal mesothelioma |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | Multicenter international registry of PIPAC (pressurized intraperitoneal aerosol chemotherapy, commonly oxaliplatin-based) for malignant pleural/peritoneal disease |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | First-in-human study of CBL-B inhibitor NX-1607 in advanced malignancies; mesothelioma is only a minor sub-population, not oxaliplatin-specific |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant cadonilimab + chemotherapy for gastroesophageal junction/gastric cancer; disease mismatch, low relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase II trial | Tumori | Pilot study of oxaliplatin + raltitrexed in inoperable MPM, following earlier Phase I signal of activity |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II multicenter trial | Clinical Lung Cancer | Gemcitabine + oxaliplatin in 25 MPM patients, doublet regimen evaluated over 6 cycles |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase II/Cohort | J Occup Med Toxicol | Oxaliplatin ± gemcitabine in pretreated MPM patients after pemetrexed failure |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II trial | J Clin Oncol | Raltitrexed + oxaliplatin in 70 MPM patients (naive and pretreated), open-label |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II trial | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in untreated MPM |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II trial | Lung Cancer | Raltitrexed-oxaliplatin as second-line therapy; trial closed early — no objective responses observed |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Case series/review | Eur J Cancer | Institut Gustave Roussy 9-year experience across 7 chemo/chemo-immunotherapy trials in mesothelioma, including raltitrexed-oxaliplatin |
| [15625372](https://pubmed.ncbi.nlm.nih.gov/15625372/) | 2005 | Retrospective validation | J Clin Oncol | Validation of EORTC prognostic model across three Phase II MPM trials (includes oxaliplatin-based regimens) |
| [26526504](https://pubmed.ncbi.nlm.nih.gov/26526504/) | 2015 | Review | Cancer Treat Rev | Reviews vinca alkaloid and platinum-based (incl. oxaliplatin) regimens in MPM management |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | Summary of Phase II-III MPM chemotherapy trials, situates oxaliplatin combinations among emerging options |

---

## Canada Market Information

No Canadian marketing authorizations (DINs) are recorded for oxaliplatin in this evidence pack — market status is "Not Marketed" with 0 total licenses.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum-based agent, diaminocyclohexane class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard cytotoxic drug handling precautions apply, consistent with other platinum chemotherapy agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase II trials directly test oxaliplatin-based combinations (with gemcitabine, raltitrexed, or vinorelbine) in MPM patients, supporting an L2 evidence level. However, results are mixed — including at least one negative second-line trial — and no Phase III confirmation exists, so guardrails are warranted rather than an unconditional Go.

**To proceed, the following is needed:**
- TFDA/Canadian regulatory package insert data (warnings, contraindications) — currently a Blocking data gap preventing safety screening (S1)
- Confirmed mechanism of action documentation from DrugBank
- Confirmation of the original approved indication text via formal Canadian regulatory source (currently based on general drug knowledge only)
- A myelosuppression/emetogenicity monitoring plan before any clinical consideration in MPM
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

