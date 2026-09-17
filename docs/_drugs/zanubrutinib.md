---
layout: default
title: Zanubrutinib
parent: Model Prediction Only (L5)
nav_order: 836
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Zanubrutinib: From B-Cell Malignancies to Myeloid Leukemia

## One-Sentence Summary

Zanubrutinib is a Bruton's tyrosine kinase (BTK) inhibitor used internationally for B-cell malignancies such as CLL/SLL, but it is not yet marketed in Canada. The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with a prediction score of 99.65%, but currently only **2 clinical trials** (neither testing zanubrutinib directly for this indication) and **no dedicated literature** support this specific link. This is a model-only signal with a weak mechanistic rationale at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established via Canada regulatory data (drug not marketed); internationally used for B-cell malignancies (e.g., CLL/SLL, per supporting literature) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on supporting information from the evidence collected, zanubrutinib is a next-generation, highly selective BTK inhibitor whose pharmacology centers on blocking B-cell receptor (BCR) signaling. Its established clinical use is in **lymphoid** malignancies — CLL/SLL, Waldenström's macroglobulinemia (WM), and mantle cell lymphoma (MCL) — where BCR signaling drives disease pathogenesis.

Myeloid leukemia arises from a distinct hematopoietic lineage with a fundamentally different set of driver pathways (e.g., FLT3, BCR-ABL1, epigenetic regulators), and BTK's pathogenic role in myeloid cells is not well established in the literature. The two clinical trials returned by the evidence search (NCT05665530, NCT04477291) both study **other** investigational agents (PRT2527, a CDK9 inhibitor; CG-806/luxeptinib, a multi-kinase inhibitor) in relapsed/refractory hematologic malignancies, and only reference zanubrutinib as a combination comparator or background context — not as monotherapy for myeloid leukemia. No literature record specifically evaluates zanubrutinib in myeloid leukemia.

In short, the TxGNN score reflects a graph-based similarity signal rather than a validated mechanistic or clinical hypothesis. The mechanistic link between BTK inhibition and myeloid leukemia is currently considered weak, and this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Studies PRT2527 (a CDK9 inhibitor), alone or combined with zanubrutinib/venetoclax, in relapsed/refractory hematologic malignancies. Zanubrutinib is a combination arm, not the primary study drug; not myeloid-leukemia-specific evidence for zanubrutinib. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/1b | Terminated | 45 | Evaluates CG-806 (luxeptinib), a multi-kinase/FLT3 inhibitor, in relapsed/refractory AML or high-risk MDS. Zanubrutinib is not the investigational agent; trial was terminated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | 5-year follow-up of SEQUOIA phase 3 trial comparing zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL — confirms zanubrutinib's established efficacy in lymphoid, not myeloid, malignancy. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Updated results of phase 2 BGB-3111-215 study: zanubrutinib is well tolerated and effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study: zanubrutinib in B-cell malignancy patients intolerant of prior BTK inhibitors (ibrutinib/acalabrutinib), showing reduced treatment-related toxicity. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Review | Blood Advances | Pooled analysis across SEQUOIA/ALPINE trials of zanubrutinib efficacy/safety in high-risk del(17p)/TP53-mutated CLL/SLL. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Reviews the tyrosine kinase inhibitor era in chronic leukemias (CML, CLL), covering BCR-ABL1 and BCR pathway biology generally. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Review of BTK inhibitor management (including zanubrutinib) in Waldenström's macroglobulinemia. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | Reviews hepatitis B reactivation risk in patients receiving BTK inhibitors (ibrutinib, acalabrutinib, zanubrutinib) for B-cell malignancies. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | Reviews synthetic chemistry methodology of FDA-approved anticancer drugs (2018–2021), mentions zanubrutinib only in a synthesis context. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | Case report of coexisting Waldenström's macroglobulinemia and B-cell ALL with KMT2D/MECOM mutations; not related to myeloid leukemia or zanubrutinib treatment. |

None of the retrieved literature directly evaluates zanubrutinib for myeloid leukemia; the corpus consistently supports its established lymphoid-malignancy indications instead.

---

## Canada Market Information

Zanubrutinib currently has **no Health Canada Drug Identification Number (DIN)** and is not marketed in Canada according to this Evidence Pack. No authorization records are available for review.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor) |
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
The TxGNN score for myeloid leukemia is high, but this is currently a model-prediction-only signal (Evidence Level L5, Decision Stage S0) with no direct clinical trial or literature support, and the underlying mechanistic hypothesis (BTK's role in myeloid leukemia) is weak. Zanubrutinib is also not marketed in Canada, adding a regulatory gap on top of the evidentiary gap.

**To proceed, the following is needed:**
- Official mechanism of action (MOA) data from DrugBank or the product label
- TFDA/Health Canada product monograph, including warnings, contraindications, and drug interactions (currently blocking per data gap DG001)
- Preclinical or mechanistic studies establishing a BTK–myeloid leukemia pathogenic link
- A clinical trial or case series testing zanubrutinib specifically in myeloid leukemia patients
- Canada market entry/regulatory status confirmation, should this program advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

