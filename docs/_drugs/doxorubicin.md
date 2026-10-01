---
layout: default
title: Doxorubicin
parent: High Evidence (L1-L2)
nav_order: 302
evidence_level: L1
indication_count: 10
---

# Doxorubicin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Doxorubicin: From Established Anthracycline Chemotherapy to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is an anthracycline chemotherapy drug marketed in Canada. Its original approved indication is not recorded in the licence data provided.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **48 clinical trials** and **20 publications** currently supporting this direction.
Doxorubicin is already a backbone drug in standard Ewing sarcoma regimens (VDC/IE), so this prediction mainly confirms existing practice rather than proposing a new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data (established anthracycline anticancer agent) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Doxorubicin is a topoisomerase II inhibitor and DNA intercalator. It causes DNA double-strand breaks in rapidly dividing tumour cells. The DrugBank record supplied lists no original indications or mechanism entry. This is a database gap, not evidence against use.

Ewing sarcoma is an aggressive bone and soft tissue tumour of children, adolescents and young adults. Standard treatment combines vincristine, doxorubicin and cyclophosphamide (VDC) alternating with ifosfamide and etoposide (IE), together with surgery and/or radiotherapy. Many of the trials below use doxorubicin as part of this backbone. Others test add-on agents on top of it, so doxorubicin's independent contribution cannot always be isolated.

The main safety concern is cumulative cardiotoxicity, which requires dose caps and cardiac monitoring.

---

## Clinical Trial Evidence

The 10 most relevant of 48 retrieved trials are listed below. Relevance grades come from the Evidence Pack where available.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification vs standard treatment in non-metastatic Ewing sarcoma; disease-specific, anthracycline-containing chemotherapy is the core backbone (grade A) |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to a standard 5-drug regimen (including doxorubicin) in non-metastatic Ewing sarcoma |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Chemotherapy intensification through interval compression in Ewing sarcoma and related tumours |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: randomised European study of chemotherapy with radiotherapy, surgery and/or stem cell transplantation in Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multiagent chemotherapy (including doxorubicin) in newly diagnosed metastatic Ewing sarcoma |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | N/A | EICESS 92: randomised comparison of combination chemotherapy regimens plus surgery and radiotherapy |
| [NCT00002898](https://clinicaltrials.gov/study/NCT00002898) | Phase 3 | Completed | 400 | MMT 95: childhood rhabdomyosarcoma and other soft tissue tumours; only partly overlaps with Ewing sarcoma (grade B) |
| [NCT06669013](https://clinicaltrials.gov/study/NCT06669013) | Phase 3 | Recruiting | 40 | Dinutuximab beta with investigator's choice chemotherapy in GD2-positive sarcomas; doxorubicin's contribution cannot be isolated (grade B) |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 2 | Vincristine-irinotecan-regorafenib added to VDC/IE in newly diagnosed metastatic Ewing sarcoma |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | Completed | 24 | Ewing sarcoma family tumours and desmoplastic small round cell tumour; disease-relevant but small (grade B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Tested whether adding ifosfamide and etoposide to standard chemotherapy improves survival in newly diagnosed Ewing sarcoma and primitive neuroectodermal tumour of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012: open-label phase 3 comparing the two standard chemotherapy strategies used in Europe and the USA |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | Children's Oncology Group phase 3 of ganitumab added to interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Children's Oncology Group trial of interval-compressed chemotherapy (alternating VDC and IE) in localised Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | EURO EWING 2012 protocol comparing two induction/consolidation chemotherapy regimens |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board recommendations on standard-of-care management |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management: risk-adapted intensive chemotherapy plus surgery and/or radiotherapy |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Chemotherapy raised survival from about 10% to about 75% in localised disease; metastatic disease still fares badly |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Cohort | J Natl Cancer Inst | Dose-intensity analysis of published trials, examining doxorubicin dose intensity against response and outcome in osteosarcoma and Ewing sarcoma |
| [28710342](https://pubmed.ncbi.nlm.nih.gov/28710342/) | 2017 | Retrospective review | Oncologist | Vincristine, ifosfamide and doxorubicin (VID) for initial treatment of Ewing sarcoma in adults at a single institution |

---

## Canada Market Information

Seven DINs are on record; five are shown. Dosage forms and approved indication text were not available in the data.

| DIN | Product Name |
|---------|------|
| 02194465 | Doxorubicin Hydrochloride for Injection USP |
| 02194473 | Doxorubicin Hydrochloride for Injection USP |
| 02410397 | Doxorubicin |
| 02238389 | Caelyx (liposomal doxorubicin) |
| 02493020 | Taro-Doxorubicin Liposomal |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor and DNA intercalator) |
| Myelosuppression Risk | High (neutropenia is the main dose-limiting haematological toxicity) |
| Emetogenicity Classification | Moderate; high when combined with cyclophosphamide, as in VDC |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (baseline and serial LVEF), cumulative anthracycline dose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack. Cumulative dose-related cardiotoxicity is the key known concern for this drug class.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least four completed Phase 3 trials (NCT02063022, NCT01231906, NCT00006734, NCT00002898) and several RCT publications place doxorubicin-containing regimens as standard care in Ewing sarcoma. The guardrails are the drug's cumulative cardiotoxicity, myelosuppression, and the fact that few trials isolate doxorubicin's own contribution.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications, which are missing from the Evidence Pack
- Confirmation of the approved indications and dosage forms for each Canadian DIN
- A cardiac monitoring plan with a cumulative dose cap
- Protocol-level confirmation of the doxorubicin dose and schedule in the key Phase 3 trials
- Mechanism of action data in DrugBank

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

