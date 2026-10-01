---
layout: default
title: Cabozantinib
parent: Model Prediction Only (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is an oral multi-kinase inhibitor marketed for renal cell carcinoma. The TxGNN model predicts it may be effective for **liposarcoma**, but only **1 clinical trial** (a randomized Phase 2 in broad soft tissue sarcoma) and **1 publication** (a Phase 1 safety study) currently support this direction, and neither reports liposarcoma-specific efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (the licence text was not supplied, so this comes from the evidence pack's rationale notes) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 (as scored in the Evidence Pack; no completed Phase 2/3 RCT exists for this indication) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. From general knowledge, cabozantinib inhibits several receptor tyrosine kinases, including VEGFR2, MET, AXL and RET. Blocking these pathways suppresses tumour angiogenesis and may reduce tumour growth and immune evasion.

Cabozantinib's efficacy in renal cell carcinoma is well established. Liposarcoma is a soft tissue sarcoma, and cabozantinib has shown activity in several soft tissue sarcoma subtypes. Anti-angiogenic and MET/AXL blockade is therefore a plausible rationale. However, the supplied data does not support any liposarcoma-specific mechanism, and the link remains a hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomized comparison of ipilimumab + nivolumab alone versus the same combination plus cabozantinib in advanced soft tissue sarcoma. Liposarcoma is only a possible subset, and no results were provided. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | American Journal of Clinical Oncology | Evaluated the safety of neoadjuvant cabozantinib with radiation therapy in extremity sarcomas. Concern about fistula or perforation risk with concurrent radiation had limited this combination. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2480824 | CABOMETYX |
| 2480832 | CABOMETYX |
| 2480840 | CABOMETYX |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: The only safety signal in the supplied liposarcoma-related evidence is a concern about fistula or perforation risk when cabozantinib is combined with radiation therapy. The Phase 1 study above was designed to test this.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The liposarcoma prediction has a high model score, but the supporting evidence is thin: one ongoing Phase 2 in mixed soft tissue sarcoma and one Phase 1 safety study. Neither reports liposarcoma-specific efficacy.

**To proceed, the following is needed:**
- Results from NCT05836571, ideally with liposarcoma subgroup data
- Efficacy data specific to liposarcoma histology
- Health Canada package insert warnings and contraindications (currently a blocking data gap)
- Mechanism-of-action data from DrugBank
- A safety plan for fistula and perforation risk, especially with concurrent radiation

**Other predicted indications in the pack:**
- Non-clear cell and unclassified renal cell carcinoma carry more mature evidence: several Phase 2 trials, published Phase 2 results and retrospective cohorts (L2, Proceed with Guardrails).
- General renal carcinoma is supported by Phase 3 RCTs such as METEOR and CheckMate 9ER (L1). It reflects an existing marketed use rather than true repurposing.
- Predictions with no supporting trials or literature (ovarian myxoid liposarcoma, amyotrophic lateral sclerosis, polymicrogyria, angiolipoma) should stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

