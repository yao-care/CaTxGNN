---
layout: default
title: Venetoclax
parent: High Evidence (L1-L2)
nav_order: 824
evidence_level: L1
indication_count: 10
---

# Venetoclax
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

# Venetoclax: From B-Cell Malignancies (CLL/SLL) to Acute Myeloid Leukemia

## One-Sentence Summary

> Venetoclax (DrugBank DB11581) is a selective BCL-2 inhibitor whose established core indication is chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL). Among 10 TxGNN-predicted new indications in this evidence pack, **Acute Myeloid Leukemia (myeloid leukemia)** stands out as the most actionable — not the top-ranked TxGNN score, but the one supported by dozens of Phase 2/3 clinical trials and real-world data, several already reflecting near-standard-of-care venetoclax + hypomethylating-agent regimens.
>
> ⚠️ Note: this candidate is a **multi-indication evidence pack**. The disease with the highest TxGNN score (rank 1, CLL/SLL with IGHV hypermutation, 99.55%) has **zero supporting trials or literature**. This report focuses on the disease with the strongest evidence tier (rank 4, AML) for decision usefulness, and summarizes all 10 candidates below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in Canadian regulatory filings for this candidate (venetoclax is listed as not marketed in this evidence pack); embedded literature rationale identifies CLL/SLL as venetoclax's established core indication |
| Predicted New Indication | Acute Myeloid Leukemia (myeloid leukemia) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Multi-Indication Candidate Landscape

This evidence pack scored venetoclax against 10 candidate diseases. Evidence strength does **not** track TxGNN score rank — the two are largely decoupled here.

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Recommendation |
|------|-------------------|:-----------:|:---------------:|-----------------|
| 1 | CLL/SLL (IGHV-mutated subtype) | 99.55% | L5 | Hold |
| 2 | Pregerminal-center CLL/SLL | 99.55% | L4 | Hold |
| 3 | Hodgkin lymphoma ⚠️ | 99.51% | L4 | Hold |
| 4 | **Acute myeloid leukemia** | **99.47%** | **L1** | **Proceed with Guardrails** |
| 5 | CML, BCR-ABL1 positive | 99.36% | L3 | Research Question |
| 6 | Ewing sarcoma | 99.21% | L4 | Hold |
| 7 | Follicular lymphoma | 99.15% | L2 | Research Question |
| 8 | Metastatic neoplasm | 99.14% | L3 | Hold |
| 9 | Malignant spiradenoma | 99.12% | L5 | Hold |
| 10 | AML with t(8;21) | 99.08% | L4 | Hold |

⚠️ **Data quality flag (rank 3):** nearly all cited trials/literature for "Hodgkin lymphoma" actually describe Non-Hodgkin lymphoma subtypes (DLBCL, FL, MCL, CLL). This looks like a disease-label mapping error and should be corrected before any use of this candidate.

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (DrugBank `original_moa`) is flagged as a data gap (DG002) in this evidence pack. However, the evidence-embedded rationale consistently identifies venetoclax as a **selective, oral BCL-2 inhibitor (BH3-mimetic)** that restores apoptosis in malignant cells that are pathologically dependent on BCL-2 for survival — this is the mechanistic basis behind its established use in CLL/SLL.

Acute myeloid leukemia (AML), and specifically AML leukemic stem cells, are well documented to be highly dependent on BCL-2 anti-apoptotic signaling for survival. Venetoclax inhibition of BCL-2 induces apoptosis in these cells, and the combination of **venetoclax + azacitidine (or decitabine/low-dose cytarabine)** is already established as a standard-of-care regimen for AML patients ineligible for intensive induction chemotherapy. This mechanistic continuity — BCL-2 dependency shared across CLL/SLL and AML — is what makes this repurposing signal biologically coherent, independent of the raw TxGNN score.

By contrast, several other high-scoring candidates in this pack (Ewing sarcoma, malignant spiradenoma) rest only on cell-line/xenograft data or no evidence at all, illustrating why evidence tier — not model score alone — should drive prioritization.

---

## Clinical Trial Evidence

*(Focused on Acute Myeloid Leukemia — the highest-evidence-tier candidate; 10 of 45+ retrieved trials shown, prioritized by phase, status, and direct relevance)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03466294](https://clinicaltrials.gov/study/NCT03466294) | Phase 2 | Active, not recruiting | 42 | Azacitidine + venetoclax induction with venetoclax maintenance in previously untreated elderly AML |
| [NCT06903702](https://clinicaltrials.gov/study/NCT06903702) | Phase 2 | Recruiting | 100 | Randomized: maintenance azacitidine+venetoclax vs. allogeneic stem cell transplant in older AML patients achieving MRD-negative CR |
| [NCT04253314](https://clinicaltrials.gov/study/NCT04253314) | Observational | Completed | 51 | Real-world (Russia) effectiveness of venetoclax in AML patients ineligible for standard induction |
| [NCT05177731](https://clinicaltrials.gov/study/NCT05177731) | Phase 3 | Active, not recruiting | 188 | Venetoclax + decitabine vs. conventional "7+3" induction in young adults with AML |
| [NCT05356169](https://clinicaltrials.gov/study/NCT05356169) | Phase 2/3 | Active, not recruiting | 312 | Randomized controlled trial of intensive chemotherapy + venetoclax vs. standard 3+7 in newly diagnosed adult AML |
| [NCT04801797](https://clinicaltrials.gov/study/NCT04801797) | Phase 2 | Recruiting | 172 | Randomized: venetoclax+azacitidine vs. induction chemotherapy in fit, newly diagnosed AML adults |
| [NCT04267081](https://clinicaltrials.gov/study/NCT04267081) | Phase 2 | Completed | 104 | Venetoclax + azacitidine in AML patients selected via ex vivo drug-sensitivity screening |
| [NCT06990321](https://clinicaltrials.gov/study/NCT06990321) | Phase 3 | Recruiting | 68 | Intermediate-dose cytarabine + venetoclax as consolidation for intermediate/high-risk elderly AML |
| [NCT06220162](https://clinicaltrials.gov/study/NCT06220162) | Phase 2 | Recruiting | 32 | Chidamide added to venetoclax+azacitidine in AML patients with suboptimal response to VA alone |
| [NCT03862157](https://clinicaltrials.gov/study/NCT03862157) | Phase 1/2 | Active, not recruiting | 40 | Azacitidine + venetoclax + pevonedistat in newly diagnosed secondary/therapy-related AML |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37036307](https://pubmed.ncbi.nlm.nih.gov/37036307/) | 2023 | Systematic review/meta-analysis | Hematology (Amsterdam) | Confirms efficacy and safety of venetoclax + azacitidine in AML and MDS across pooled studies |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Cohort | Clin Cancer Res | Venetoclax + azacitidine shows strong efficacy in treatment-naïve AML with IDH1/2 mutations |
| [34329576](https://pubmed.ncbi.nlm.nih.gov/34329576/) | 2021 | Single-arm Phase 2 trial | Lancet Haematology | Venetoclax + intensive chemotherapy (cladribine/idarubicin/cytarabine) active in newly diagnosed AML/high-risk MDS |
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomedicine & Pharmacotherapy | Comprehensive review of venetoclax preclinical and clinical activity in adult AML |
| [39246164](https://pubmed.ncbi.nlm.nih.gov/39246164/) | 2024 | Review | Expert Review of Hematology | Venetoclax+azacitidine established as standard of care for unfit AML; discusses resistance/relapse management |
| [31203996](https://pubmed.ncbi.nlm.nih.gov/31203996/) | 2019 | Review | Best Practice & Research Clin Haematol | Venetoclax-based therapies in the broader context of new AML drug approvals |
| [32031033](https://pubmed.ncbi.nlm.nih.gov/32031033/) | 2020 | Review | Leukemia & Lymphoma | Venetoclax + HMA/LDAC as new standard of care for frontline AML in older/unfit patients |
| [34966123](https://pubmed.ncbi.nlm.nih.gov/34966123/) | 2022 | Review | Current Opinion in Hematology | Overview of venetoclax combination regimens in newly diagnosed/relapsed AML and MDS |
| [41143709](https://pubmed.ncbi.nlm.nih.gov/41143709/) | 2025 | Review | Expert Opinion on Pharmacotherapy | Venetoclax and next-generation BCL-2 inhibitors in AML management |
| [36933006](https://pubmed.ncbi.nlm.nih.gov/36933006/) | 2023 | Review | Expert Opinion on Investigational Drugs | Venetoclax's evolving role in AML treatment landscape |

---

## Canada Market Information

No Canadian market authorizations (DINs) were identified in this evidence pack — `total_licenses = 0`, `licenses = []`. Venetoclax is recorded as **not marketed** under this dataset. This should be independently verified against Health Canada's Drug Product Database, as venetoclax (Venclexta) is a globally marketed oncology product; a zero-DIN result here may reflect a data-collection gap rather than true non-availability.

---

## Cytotoxicity

*(Venetoclax is an antineoplastic agent — a molecularly targeted BCL-2 inhibitor used across the hematologic malignancies covered in this evidence pack.)*

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (selective BCL-2 inhibitor / BH3-mimetic), not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | High — literature in this evidence pack explicitly identifies tumor lysis syndrome and myelosuppression (including neutropenia and thrombocytopenia) as the most commonly encountered toxicities of venetoclax-based regimens (PMID 35659041); one combination trial reported thrombocytopenia in 80% of patients (PMID 38264906) |
| Emetogenicity Classification | Low (based on general classification of oral BCL-2 inhibitors; please confirm against the package insert as specific data was not provided in this evidence pack) |
| Monitoring Items | CBC with differential; tumor lysis syndrome panel (potassium, phosphate, calcium, uric acid) especially during dose ramp-up; renal function |
| Handling Protection | As an oral antineoplastic/targeted agent, handling should follow institutional hazardous/cytotoxic drug handling protocols per local pharmacy policy |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, and drug–drug interactions) were not available in this evidence pack — this is recorded as a **Blocking** data gap (DG001: TFDA/Health Canada label warnings and contraindications) that must be resolved before any S1 safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for the Acute Myeloid Leukemia candidate specifically — other candidates in this pack remain Hold or Research Question)*

**Rationale:**
Venetoclax + hypomethylating agent (azacitidine/decitabine) regimens are supported by an extensive body of Phase 2/3 trials and real-world evidence for AML, and are already near-standard-of-care in several jurisdictions for patients unfit for intensive chemotherapy. This is the strongest-evidenced indication among the 10 candidates in this pack, despite not carrying the highest raw TxGNN score.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/Health Canada package insert warnings and contraindications
- Resolve DG002 (High): obtain formal DrugBank-sourced mechanism-of-action documentation
- Verify the Canadian market/DIN status discrepancy (0 DINs recorded vs. known global marketing of venetoclax)
- Correct the disease-mapping anomaly flagged for rank 3 ("Hodgkin lymphoma" vs. actual Non-Hodgkin lymphoma evidence)
- Obtain a formal drug–drug interaction profile (currently `not_found`; venetoclax is a known CYP3A4 substrate)
- Deprioritize rank 1, 2, 9, and 10 candidates pending emergence of actual clinical or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

