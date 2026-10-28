---
layout: default
title: Zanubrutinib
parent: Model Prediction Only (L5)
nav_order: 989
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Zanubrutinib: predicted new indication Myeloid leukemia (evidence level L4). Approved use: Mantle cell lymphoma, B-cell neoplasm, lymphosarcoma"
monitor_inn: "ZANUBRUTINIB"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "Ewing sarcoma", "neuroblastoma"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Zanubrutinib: From Mantle Cell Lymphoma to Myeloid Leukemia
{: .text-alpha }

## One-Sentence Summary

Zanubrutinib is a BTK inhibitor originally used for B-cell malignancies such as mantle cell lymphoma.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but this is mainly a computational prediction.
Only **1 clinical trial** (Phase 1, where zanubrutinib is a combination partner) and **10 publications**, mostly about B-cell diseases, are linked to it, so direct supporting evidence is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma, B-cell neoplasm, lymphosarcoma |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zanubrutinib is a next-generation Bruton tyrosine kinase (BTK) inhibitor. Its efficacy in B-cell malignancies has been established, and the data compiled for this report suggest that it may be mechanistically relevant to other blood cancers.

The link to myeloid leukemia is indirect. BTK is expressed in some myeloid cells and AML blasts and may contribute to survival signaling. However, there is no direct clinical evidence of benefit. The publications compiled for this report concern chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL), Waldenström macroglobulinemia and BTK inhibitor safety. These are all B-cell diseases, not myeloid leukemia. The high score (0.9965) should be read as a model prediction, not as proof of efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Safety and efficacy of PRT2527 (a CDK9 inhibitor) alone and combined with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies. Zanubrutinib is only a combination partner, probably in a B-cell cohort, so this is not direct evidence in myeloid leukemia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA phase 3, 5-year follow-up: zanubrutinib vs bendamustine + rituximab in treatment-naïve CLL/SLL |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study in B-cell malignancy patients intolerant of earlier BTK inhibitors |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | Updated results: zanubrutinib well tolerated and effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort | Blood Adv | Pooled analysis across studies in CLL/SLL with del(17p) and/or TP53 mutations (N = 301) |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Tyrosine kinase inhibitors in chronic leukemias (CML and CLL) |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Managing Waldenström macroglobulinemia with BTK inhibitors |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | Hepatitis B virus reactivation in patients receiving BTK inhibitors |
| [42192981](https://pubmed.ncbi.nlm.nih.gov/42192981/) | 2026 | Review | Cancers | BTK inhibitors in CLL: hypogammaglobulinemia and infection risk |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anti-Cancer Agents Med Chem | Synthetic methods of FDA-approved anticancer drugs (2018–2021) |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Rare coexistence of Waldenström macroglobulinemia and B-cell ALL |

None of these studies tests zanubrutinib in myeloid leukemia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02512963 | BRUKINSA | Not specified | Not specified |
| 02554267 | BRUKINSA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Complete blood count and liver function are commonly monitored for oncology drugs of this type. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Major-level examples include aprepitant, acetylsalicylic acid, dexamethasone, clarithromycin, cobicistat, deferasirox, deferiprone, samarium (153Sm) lexidronam, ibritumomab tiuxetan and tositumomab (I-131). Moderate-level examples include cimetidine, miconazole, clotrimazole, fenfluramine, sibutramine and troglitazone.
- **Other safety signals from the literature**: Reports describe hepatitis B virus reactivation in patients on BTK inhibitors, and hypogammaglobulinemia with increased infection risk.

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on the model score. The only linked trial is a Phase 1 combination study with no direct myeloid leukemia data, and the literature concerns B-cell diseases. Evidence level is L4, and the mechanistic link to myeloid leukemia is indirect.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer analysis of BTK dependence in myeloid leukemia (AML)
- Preclinical studies or clinical data on zanubrutinib in myeloid leukemia
- Verification of the actual cohort composition of NCT05665530
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Approved indication and dosage form details for the two Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

