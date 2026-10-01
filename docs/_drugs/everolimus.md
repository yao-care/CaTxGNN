---
layout: default
title: Everolimus
parent: Model Prediction Only (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Established mTOR-Inhibitor Use to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR inhibitor marketed in Canada under 20 DINs. The TxGNN model predicts it may be effective for **liposarcoma**, and the supporting evidence is thin: **1 clinical trial** (a Phase 2 combination study) and **4 publications**, only one of which reports clinical results. Health Canada indication text was not available in the source data.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

*Evidence level note:* The Evidence Pack labels this candidate L2. Strictly applying the level rules, L2 requires a completed Phase 2/3 RCT. The only trial here is single-arm, combination-based and still active, so I rated it L3. Only one published clinical report and mostly preclinical or pathway studies support the prediction.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for everolimus are not available in the Evidence Pack. Based on known information, everolimus belongs to the mTOR inhibitor class, and its efficacy in other cancers, such as renal cell carcinoma, has been established.

Activation of the Akt-mTOR and MAPK pathways has been described in dedifferentiated liposarcoma (99 specimens analysed; PMID 26518767). This supports the idea that blocking mTOR could be relevant in this tumour type. Dedifferentiated liposarcoma is also typically driven by CDK4 amplification. The one clinical trial therefore pairs everolimus with the CDK4/6 inhibitor ribociclib, on the hypothesis that the two agents are synergistic.

The main limitation is that everolimus's own contribution cannot be separated from the combination. No everolimus-alone data exist for liposarcoma in this dataset.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after at least 1 prior systemic therapy. It is a two-centre, single-arm, combination study of anti-tumour activity, so it is not confirmatory and cannot isolate the everolimus effect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial report | Clin Cancer Res | Report of the ribociclib + everolimus study in dedifferentiated liposarcoma and leiomyosarcoma. The abstract provided is truncated, so outcome figures were not available. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Preclinical / tissue study | Tumour Biol | Akt-mTOR and MAPK pathway activation in 99 dedifferentiated liposarcoma specimens, with an in vitro test of an mTOR inhibitor. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Sarcoma patient-derived xenograft models used to find combinations with the CDK inhibitor palbociclib. Indirect relevance. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin combinations with other anticancer agents. Indirect relevance, since it does not concern everolimus. |

---

## Canada Market Information

Everolimus has 20 DINs in total. The five main authorizations are listed below. Dosage form, manufacturer and approved-indication text were not available in the source data.

| DIN | Product Name |
|---------|------|
| 02339501 | AFINITOR |
| 02463237 | TEVA-EVEROLIMUS |
| 02492938 | SANDOZ EVEROLIMUS |
| 02492946 | SANDOZ EVEROLIMUS |
| 02504677 | PMS-EVEROLIMUS |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor), not a conventional cytotoxic |
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
The liposarcoma signal rests on one active, single-arm Phase 2 combination trial plus pathway and preclinical data. The contribution of everolimus alone is unknown, and there is no randomized or Phase 3 evidence. The Health Canada safety review has also not been done. By comparison, unclassified renal cell carcinoma (rank 9) has much stronger Phase 2 support, including the randomized ASPEN trial, and is a better candidate to advance first.

**To proceed, the following is needed:**
- Outcome data from NCT03114527 and PMID 37967116 (response rate, progression-free survival), ideally with any everolimus-specific signal
- Health Canada package insert warnings and contraindications, to complete the safety screening
- Detailed mechanism-of-action data for everolimus, to support the mechanistic link
- Health Canada approved-indication text, to confirm the original indication and any overlap with sarcoma
- Everolimus-alone or randomized evidence in liposarcoma, if the combination result is positive

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

