---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Axitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Axitinib: From Advanced Renal Cell Carcinoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Axitinib (brand name Inlyta) is a potent and selective oral inhibitor of vascular endothelial growth factor receptors (VEGFR-1, -2, and -3), approved by the FDA for the treatment of advanced renal cell carcinoma, though not currently registered in Taiwan. The TxGNN model predicts it may also be effective for **unclassified renal cell carcinoma (uRCC)** — a heterogeneous "diagnosis of exclusion" accounting for approximately 3–5% of all RCC cases — with **2 observational studies** providing indirect supporting evidence but **no dedicated published literature** for this specific histological subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (FDA-approved globally; not registered in Taiwan) |
| Predicted New Indication | Unclassified renal cell carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for axitinib is not available in this evidence pack. Based on known information, axitinib is a second-generation tyrosine kinase inhibitor (TKI) that selectively and potently targets VEGFR-1, -2, and -3, with inhibitory concentrations approximately 10-fold lower than first-generation TKIs such as sorafenib or sunitinib. By blocking VEGF receptor signaling, it disrupts the tumor angiogenesis that most RCC subtypes depend upon for growth and metastasis. This mechanism has been robustly validated in major Phase 3 trials (KEYNOTE-426, JAVELIN Renal 101), leading to FDA approval of axitinib in combination with immune checkpoint inhibitors as a first-line treatment for advanced RCC.

Unclassified RCC (uRCC) is defined purely by exclusion — it encompasses all kidney carcinomas that cannot be placed into any recognized histological category such as clear cell, papillary, or chromophobe. This molecular heterogeneity means that VEGFR pathway activation varies substantially between individual uRCC cases. Some uRCC tumors may behave similarly to clear cell RCC and respond to VEGFR inhibition; others may harbor fundamentally different molecular drivers that would not benefit from axitinib.

The two currently available studies are entirely observational in design: a post-marketing surveillance registry of Inlyta across broad RCC populations (NCT02156895, n=111) and a large UK retrospective database study examining sunitinib and axitinib in metastatic/advanced RCC (NCT04033991, n=684). Neither was specifically designed for uRCC, and no prospective data or uRCC-specific subgroup analyses have been published. The TxGNN prediction score likely derives from axitinib's strong performance across the broader RCC disease node in the knowledge graph, and should be interpreted as hypothesis-generating rather than indicative of proven efficacy in this specific subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02156895](https://clinicaltrials.gov/study/NCT02156895) | N/A (Post-marketing) | Completed | 111 | Post-marketing surveillance of Inlyta® in real-world RCC clinical practice; monitors adverse events and efficacy across RCC subtypes; uRCC subgroup data potentially extractable but not a designated endpoint |
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | N/A (Real-world study) | Completed | 684 | UK retrospective database study of sunitinib (1st line) and axitinib (2nd line) in metastatic/advanced RCC; evaluates progression-free survival stratified by MSKCC/IMDC risk; uRCC patients likely represented in the cohort but without dedicated subgroup analysis |

---

## Literature Evidence

Currently no related literature available specifically for unclassified renal cell carcinoma and axitinib.

---

## Taiwan Market Information

Axitinib is not currently registered or marketed in Taiwan. No drug licenses are on record with the Taiwan FDA (TFDA), and there are no approved indications or product registrations in the local market.

---

## Cytotoxicity

Axitinib is an antineoplastic agent targeting tumor angiogenesis and classified as a targeted therapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective VEGFR-1/2/3 tyrosine kinase inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low — axitinib does not cause significant myelosuppression; primary toxicities include hypertension, fatigue, diarrhea, and palmar-plantar erythrodysaesthesia (hand-foot syndrome) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure (before initiation and frequently during treatment), liver function (ALT, AST, bilirubin), thyroid function (TSH), CBC with differential, renal function (creatinine, eGFR) |
| Handling Protection | Follow institutional cytotoxic drug handling protocols; standard precautions for oral targeted therapy apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Available evidence consists entirely of two observational studies with no dedicated uRCC-specific design or endpoint analysis; no published clinical trials or literature have specifically evaluated axitinib in unclassified renal cell carcinoma, making it premature to advance this indication beyond hypothesis generation.

**To proceed, the following is needed:**
- Subgroup analysis of existing broad RCC clinical datasets to extract uRCC-specific efficacy and safety data for axitinib-based regimens
- Design of a prospective basket trial or signal-finding study explicitly enrolling uRCC patients
- Molecular profiling of uRCC cases to assess VEGFR pathway activation status and identify the subset most likely to respond to VEGFR inhibition
- Retrieval of the full TFDA-reviewed package insert (warnings, contraindications, and drug interactions) for complete safety evaluation before any local clinical consideration
- Assessment of the Taiwan regulatory pathway (TFDA) for introducing axitinib if clinical evidence matures sufficiently

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application in patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

