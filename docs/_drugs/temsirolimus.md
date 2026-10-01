---
layout: default
title: Temsirolimus
parent: Model Prediction Only (L5)
nav_order: 882
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Temsirolimus: From Its Current Oncology Use to Liposarcoma

## One-Sentence Summary

Temsirolimus (brand name TORISEL) is an mTOR inhibitor marketed as an anticancer drug.
The TxGNN model predicts it may be effective for **liposarcoma**,
with **5 clinical trials** and **1 publication** currently supporting this direction. Only one trial tests temsirolimus directly in sarcoma with liposarcoma patients (a small combination study).

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

*Evidence level note: the upstream scoring labelled this L2. Under the rules used here, L2 requires a completed Phase 2/3 randomized trial. All five trials found are single-arm or non-randomized Phase 1/2 studies, and the only literature item is a review, so L3 is the more defensible level.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From general knowledge of the drug class, temsirolimus inhibits mTOR (mammalian target of rapamycin) by binding FKBP12, which blocks signaling that drives tumour cell growth and survival.

The PI3K/AKT/mTOR pathway is active in many soft tissue sarcomas. Dedifferentiated liposarcoma typically carries CDK4/MDM2 amplification and frequently shows mTOR pathway activation. This makes mTOR inhibition a plausible strategy.

This rationale is class-level reasoning plus the knowledge-graph prediction, not drug-specific validation. Two of the five supporting trials used other mTOR inhibitors (ridaforolimus, everolimus), and one used sirolimus. Two further predictions, ovarian myxoid liposarcoma (score 99.47%) and vulva sarcoma (score 99.09%), have no trials or literature and are model predictions only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus plus liposomal doxorubicin in recurrent soft tissue and bone sarcoma. Aims to find a safe dose and assess efficacy. The most direct evidence, but small and combination-based. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab plus temsirolimus in pediatric recurrent or refractory solid tumours including sarcoma. Weak relevance, since liposarcoma is mainly an adult disease. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. Supports the mTOR-class rationale. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor) in advanced sarcoma. Class-level evidence, not specific to temsirolimus. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib plus everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma. Exact disease match, but a different mTOR inhibitor and results may not be available yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Review of targeted treatments for rare connective tissue tumours and sarcomas, organized by six molecularly defined subgroups. It does not specifically evaluate temsirolimus. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2304104 | TORISEL |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is high, but direct evidence is thin. Only one small combination trial (n=24) tested temsirolimus in a sarcoma population, and the other supporting studies used different mTOR inhibitors. Safety data (warnings, contraindications) is also missing, which blocks safety screening. This is best treated as a research question rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, from the Health Canada product monograph
- Mechanism of action data, for example from DrugBank
- Results of NCT00949325 (temsirolimus plus liposomal doxorubicin), including the liposarcoma subgroup if reported
- Confirmation of the regulatory source for the license record. The pack lists TFDA as the input, and the license number format may not be a Canadian DIN.
- The approved indication text and dosage form for the marketed product, to assess route and indication compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

