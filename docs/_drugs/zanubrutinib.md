---
layout: default
title: Zanubrutinib
parent: Moderate Evidence (L3-L4)
nav_order: 982
evidence_level: L4
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

Zanubrutinib (marketed in Canada as BRUKINSA) is a next-generation BTK inhibitor. The supplied literature shows it used for B-cell malignancies such as CLL/SLL and Waldenström's macroglobulinemia.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but the evidence is weak: **2 early-phase trials** that do not test zanubrutinib, and **no publications** on myeloid disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell malignancies (CLL/SLL, Waldenström's macroglobulinemia), inferred from the supplied literature. The Canadian license records contain no indication text. |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Zanubrutinib is a covalent inhibitor of Bruton's tyrosine kinase (BTK). It is more selective than ibrutinib or acalabrutinib. Detailed mechanism-of-action data are not available in the record. Based on known information, BTK is expressed in myeloid-lineage cells and has been proposed as a signaling node in some AML settings. This is only a hypothesis, and no clinical data supplied here support it.

The original indications are lymphoid (B-cell) cancers, while the predicted indication is myeloid. The supplied literature covers only CLL/SLL and Waldenström's macroglobulinemia. The high TxGNN score (0.996) most likely reflects the drug's proximity to leukemia nodes in the knowledge graph, not myeloid-specific evidence.

Five other predictions rank below myeloid leukemia: a rare congenital syndrome, ganglioneuroblastoma, retroperitoneal neoplasm, Ewing sarcoma and neuroblastoma. All have no trials and no relevant literature, and none has an identifiable BTK-dependent mechanism. They are model outputs only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose escalation of PRT2527 (a CDK9 inhibitor) alone or combined with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies. Zanubrutinib is only a combination partner, so this gives no direct evidence for it in myeloid leukemia. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Terminated | 45 | Safety and activity of CG-806 (luxeptinib, a multi-kinase inhibitor with BTK and FLT3 activity) in relapsed/refractory AML or higher-risk MDS. A different drug, so at most a weak class-level hint. |

Both trials are graded C for relevance, meaning neither tests zanubrutinib as the studied drug in myeloid leukemia.

---

## Literature Evidence

None of the publications studies zanubrutinib in myeloid leukemia. All relate to lymphoid malignancies or general topics.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA phase 3, median 5-year follow-up: zanubrutinib vs bendamustine + rituximab in treatment-naïve CLL/SLL |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | Updated phase 2 results: zanubrutinib is well tolerated and effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort | Blood Adv | Pooled analysis (N = 301) of efficacy and safety in CLL/SLL with del(17p) and/or TP53 mutations |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Phase 2 trial | Lancet Haematol | Single-arm study of zanubrutinib in B-cell malignancies intolerant of earlier BTK inhibitors |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Managing Waldenström's macroglobulinemia with BTK inhibitors |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Tyrosine kinase inhibitors in chronic leukemias (CML and CLL) |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | Hepatitis B virus reactivation in patients receiving BTK inhibitors |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | Synthetic methods of FDA-approved anticancer drugs (2018–2021). Zanubrutinib is mentioned incidentally. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Rare case of coexisting Waldenström's macroglobulinemia and B-cell ALL |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2512963 | BRUKINSA |
| 2554267 | BRUKINSA |

Dosage form, manufacturer and approved indication text are not recorded for these licenses.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Hepatitis B status deserves attention (see Safety Considerations). |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Hepatitis B reactivation**: The literature (PMID 37150651) reports HBV reactivation in patients receiving BTK inhibitors, including second-generation agents such as zanubrutinib. Screening and monitoring should be considered.

No drug-interaction records were found. Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by direct evidence. The two trials do not test zanubrutinib as the studied drug in myeloid leukemia, and the literature covers only B-cell malignancies. The other five predicted indications have no supporting evidence at all.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Detailed mechanism-of-action data from DrugBank
- Preclinical or clinical data on BTK dependency in AML or other myeloid disease
- Approved indication text, dosage forms and manufacturer for the two DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

