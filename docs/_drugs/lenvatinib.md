---
layout: default
title: Lenvatinib
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: From Approved Oncology Use to Liposarcoma

## One-Sentence Summary

Lenvatinib is an oral multi-kinase inhibitor marketed in Canada as LENVIMA for cancer treatment. The pack does not record its original indications.
The TxGNN model predicts it may be effective for **liposarcoma**, supported by **1 completed Phase Ib/II trial** and **4 publications**.
The clinical data come from a combination with eribulin, so lenvatinib's own contribution cannot be isolated.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L2 (as assigned in the Evidence Pack; the supporting trial is single-arm and non-randomized) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level mechanism-of-action field is not populated in the Evidence Pack. The pack's repurposing rationale describes lenvatinib as a multi-kinase inhibitor targeting VEGFR1-3, FGFR1-4, PDGFRα, KIT and RET. By blocking these receptors it suppresses tumour angiogenesis, which is relevant in soft tissue sarcoma.

Liposarcoma is a soft tissue sarcoma with limited treatment options. Anti-angiogenic activity is a plausible way to slow tumour growth.
Preclinical work supports combining a kinase inhibitor with eribulin, a mitosis-targeting chemotherapy. The LEADER study tested this pairing in adipocytic sarcoma and leiomyosarcoma.

The main caveat is that all clinical data so far come from the lenvatinib + eribulin combination. There is no lenvatinib-alone data in liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | LEADER study: single-arm test of lenvatinib + eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma. It gives direct safety and efficacy data but has no randomized comparator. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II single-arm trial | Clin Cancer Res | Publication of the LEADER study (NCT03526679), assessing safety and efficacy of lenvatinib + eribulin in advanced liposarcoma and leiomyosarcoma. |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/biomarker study | Exp Hematol Oncol | CDK4 as a prognostic biomarker in soft tissue sarcoma, with a synergistic effect of CDK4 inhibition in dedifferentiated liposarcoma. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical combination study | Anticancer Res | Eribulin combined with mechanistically different anticancer agents showed broad-spectrum preclinical antitumour activity. |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Rep Oncol | Marked tumour shrinkage in a patient with dedifferentiated liposarcoma and lung metastasis given individualized targeted therapy, surgery and chemotherapy. |

---

## Canada Market Information

The pack lists 8 licenses in total. The 5 below have no recorded dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 02450313 | LENVIMA |
| 02484129 | LENVIMA |
| 02450291 | LENVIMA |
| 02468239 | LENVIMA |
| 02484056 | LENVIMA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure (hypertension is a recognized class effect of multi-kinase inhibitors, per PMID 31547602); for other parameters, please refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical support for liposarcoma is one small (n=30), single-arm Phase Ib/II study of a lenvatinib + eribulin combination. Safety data are also missing, and the Evidence Pack flags the Health Canada label data as a blocking gap.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Drug-level mechanism-of-action data from DrugBank
- Randomized or lenvatinib-specific data in liposarcoma, to separate its effect from eribulin's
- Approved indication text for the Canadian licenses, so the original indication can be documented

**Note on other predictions:**
Among the other predicted indications, renal carcinoma has the strongest support. It has L1 evidence, including the Phase 3 CLEAR trial, and the pack suggests it is an established approved use rather than true repurposing. The input record's empty original-indication field should be checked.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

