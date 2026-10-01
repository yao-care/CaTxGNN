---
layout: default
title: Fludarabine
parent: Model Prediction Only (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From B-Cell Leukemia and Lymphoma Chemotherapy to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside analog chemotherapy. The literature describes it as a major drug for B-cell lymphocytic leukemia, hairy cell leukemia and indolent lymphomas.
The TxGNN model predicts it may be useful in **plasma cell myeloma**, with **50 registered clinical trials** and **20 publications** retrieved.
Fludarabine appears in these studies mainly as a supporting component of transplant conditioning or CAR-T lymphodepletion, not as a standalone myeloma treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data; literature describes B-cell chronic lymphocytic leukemia, hairy cell leukemia and indolent lymphoma |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 (the pipeline labelled L2, but no randomized Phase 2/3 trial in the myeloma-specific set isolates fludarabine's effect; the support is single-arm trials, cohorts and a preclinical study) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available from DrugBank. Based on the evidence retrieved, fludarabine is a purine analog that inhibits DNA synthesis and is strongly lymphodepleting. Its efficacy in B-cell malignancies is established, and mechanistically it may be applicable to myeloma, another B-lineage cancer.

Myeloma and chronic lymphocytic leukemia are described in the literature as closely related B-cell cancers (PMID 1415309). A preclinical study also found that fludarabine inhibited a human myeloma cell line in vitro and in vivo (PMID 17976186).

In practice, however, fludarabine's role in myeloma is supportive:
- It is used in reduced-intensity conditioning before allogeneic stem cell transplant, usually with melphalan, busulfan or low-dose radiation.
- It is used with cyclophosphamide as lymphodepletion before BCMA-, FcRL5- and GPRC5D-directed CAR-T therapy.

Because it is always given with other therapies, its independent anti-myeloma effect cannot be separated from the transplant or the cellular therapy.

---

## Clinical Trial Evidence

Of the 50 trials retrieved, the 10 most relevant are listed. All involve fludarabine only as part of a regimen.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453101](https://clinicaltrials.gov/study/NCT01453101) | Phase 2 | Completed | 54 | Allogeneic transplant for myeloma with fludarabine, melphalan and bortezomib conditioning, compared against historical fludarabine/melphalan controls |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | Completed | 20 | Fludarabine plus methoxyamine (TRC102) in relapsed or refractory hematologic malignancies; fludarabine is the backbone agent |
| [NCT00054353](https://clinicaltrials.gov/study/NCT00054353) | Phase 1/2 | Completed | 16 | Reduced-intensity transplant in myeloma with fludarabine, melphalan and total-body irradiation |
| [NCT00802568](https://clinicaltrials.gov/study/NCT00802568) | Phase 2 | Completed | 48 | Myeloma pilot of reduced-intensity transplant with fludarabine, busulfan and antithymocyte globulin |
| [NCT01503242](https://clinicaltrials.gov/study/NCT01503242) | Phase 1 | Completed | 15 | 90Y-BC8 antibody, fludarabine and total-body irradiation before donor transplant in myeloma |
| [NCT00006251](https://clinicaltrials.gov/study/NCT00006251) | Phase 1/2 | Completed | 21 | Fludarabine and low-dose total-body irradiation to induce mixed chimerism in hematologic cancers |
| [NCT01408563](https://clinicaltrials.gov/study/NCT01408563) | Phase 2 | Completed | 33 | Reduced-intensity double cord blood transplant using fludarabine, melphalan and low-dose radiation |
| [NCT05594797](https://clinicaltrials.gov/study/NCT05594797) | Phase 2 | Recruiting | 100 | BCMA CAR-T in relapsed or refractory myeloma; fludarabine and cyclophosphamide used only as lymphodepletion |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | Recruiting | 20 | Anti-FcRL5 CAR-T in relapsed or refractory myeloma; fludarabine used only as lymphodepletion |
| [NCT02447055](https://clinicaltrials.gov/study/NCT02447055) | Early Phase 1 | Withdrawn | 0 | Planned Flu/Mel allogeneic transplant with post-transplant cyclophosphamide and tocilizumab; never enrolled |

---

## Literature Evidence

No randomized controlled trial specific to fludarabine in myeloma was found. The 10 most relevant publications are listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | Fludarabine inhibited the RPMI8226 myeloma cell line in vitro and in vivo, with decreased Akt phosphorylation |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective multicenter cohort | Bone Marrow Transplant | Fludarabine and treosulfan conditioning before allogeneic transplant was feasible in 34 myeloma patients |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | Bortezomib, fludarabine and melphalan, with or without total marrow irradiation, as transplant conditioning in high-risk or refractory myeloma |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 (very small) | Leuk Res Rep | Split-dose busulfan, fludarabine and post-transplant cyclophosphamide in 4 myelofibrosis and 2 myeloma patients; 1-year overall survival 50% |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer J | Compares bendamustine with fludarabine/cyclophosphamide lymphodepletion before BCMA CAR-T; no abstract available |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Not classified | Eur J Haematol | Fludarabine in plasma cell leukemia; no abstract available |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | Review | Am J Med | Parallels and contrasts between myeloma and chronic lymphocytic leukemia |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Cohort | J Clin Oncol | Long-term follow-up of combined BCMA and CD19 CAR-T in myeloma; fludarabine is only the lymphodepletion backdrop |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Real-world cilta-cel CAR-T outcomes in relapsed or refractory myeloma; fludarabine is only lymphodepletion |
| [31378662](https://pubmed.ncbi.nlm.nih.gov/31378662/) | 2019 | Single-arm Phase 2 | Lancet Haematol | Combined anti-CD19 and anti-BCMA CAR-T in relapsed or refractory myeloma; fludarabine is only lymphodepletion |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2438577 | FLUDARABINE PHOSPHATE INJECTION, USP |
| 2283859 | FLUDARABINE PHOSPHATE FOR INJECTION |
| 2246226 | FLUDARA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog) |
| Myelosuppression Risk | High; myelosuppression is a monitored risk in this evidence |
| Emetogenicity Classification | Low (general drug-class knowledge, not from the Evidence Pack) |
| Monitoring Items | CBC with differential, renal function, neurological status |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert for warnings and precautions.

---

## Safety Considerations

The Health Canada package insert warnings and contraindications have not yet been retrieved, and no drug-interaction records were found. The following points come from the evidence analysis, not from the label:

- **Renal clearance**: fludarabine is renally cleared and needs dose reduction, or is contraindicated, in significant renal impairment.
- **Toxicity**: myelosuppression, immunosuppression and neurotoxicity are the main risks.
- **Setting**: use should be limited to transplant or cellular-therapy programs.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence shows fludarabine is widely used as a conditioning or lymphodepletion component in myeloma. It does not show that fludarabine itself treats myeloma, because every trial and cohort combines it with other therapies. The Health Canada safety review is also still blocked by missing package insert data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism-of-action data from DrugBank
- Comparative evidence isolating fludarabine's contribution, for example a randomized comparison of conditioning regimens with and without fludarabine in myeloma
- Renal dose-adjustment and neurotoxicity monitoring plans for a transplant-program setting

The same pack shows stronger support for **myelodysplastic syndrome** (rank 7). There, fludarabine is a shared backbone in randomized Phase 3 conditioning trials (treosulfan/fludarabine vs busulfan/fludarabine), and the pack rates that indication "Proceed with Guardrails". It may be the better first candidate to pursue.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

