---
layout: default
title: Cyclophosphamide
parent: Model Prediction Only (L5)
nav_order: 232
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Cyclophosphamide: From Lymphoma and Other Cancers to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy drug originally used for lymphomas (including cutaneous T-cell lymphoma), plasma cell myeloma, neuroblastoma, breast cancer and retinoblastoma.
The TxGNN model predicts it may be effective for **myeloid leukemia**, with **33 clinical trials** and **20 publications** currently supporting this direction. Most of this evidence comes from transplant conditioning and combination regimens, not from cyclophosphamide used alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mycosis fungoides and other cutaneous T-cell lymphomas, plasma cell myeloma, neuroblastoma, lymphoma, breast carcinoma, retinoblastoma (the Canadian label text was not available in the data compiled for this report) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 (the prediction-level rating assigned in the data compiled for this report; see the note under Clinical Trial Evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclophosphamide is an alkylating prodrug. It is activated to phosphoramide mustard, which cross-links DNA and kills rapidly dividing cells. That gives it direct cytotoxicity against leukemic blasts.

Its approved indications (lymphoma, myeloma, neuroblastoma) are also rapidly proliferating malignancies of blood and nervous-system origin. The same cytotoxic mechanism is therefore plausibly applicable to myeloid leukemia.

Cyclophosphamide also provides lymphodepletion and immunosuppression. This is why it is widely used in conditioning before allogeneic stem cell transplant (for example busulfan-cyclophosphamide) and as post-transplant cyclophosphamide. The post-transplant use selectively depletes alloreactive T cells and reduces graft-versus-host disease (GVHD), which supports haploidentical and mismatched-donor transplants in myeloid malignancies.

---

## Clinical Trial Evidence

The data compiled for this report list 33 trials. The table shows the 10 most relevant, favouring those graded most relevant in the data. Cyclophosphamide is almost always one component of a regimen, so these trials do not isolate its individual effect.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Completed | 19 | Randomized comparison of conventional vs T-cell-depleted unrelated donor marrow transplant; conditioning commonly includes cyclophosphamide. Small study. |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Completed | 50 | Clofarabine + etoposide + cyclophosphamide in pediatric relapsed/refractory acute leukemias. |
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Completed | 25 | Reduced-intensity haploidentical transplant with post-transplant cyclophosphamide and GVHD prevention (AML, ALL, MDS and others). |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Completed | 107 | Hyper-CVAD (contains cyclophosphamide) plus dasatinib in Ph+ ALL. Mostly lymphoid disease, so only partly relevant to myeloid leukemia. |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | Completed | 28 | Two-step haploidentical transplant for hematologic malignancies in remission; mixed myeloid population. |
| [NCT02441803](https://clinicaltrials.gov/study/NCT02441803) | Phase 2 | Completed | 11 | Allogeneic transplant as salvage for primary induction-failure AML. Very small; cyclophosphamide's contribution is hard to isolate. |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant with cyclophosphamide/fludarabine/total body irradiation myeloablative conditioning. |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Active, not recruiting | 300 | HLA-mismatched unrelated donor transplant with post-transplant cyclophosphamide, tacrolimus and mycophenolate for GVHD prophylaxis. |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | Active, not recruiting | 56 | Post-transplant cyclophosphamide with abatacept, vedolizumab and a calcineurin inhibitor in children and young adults. |
| [NCT00939653](https://clinicaltrials.gov/study/NCT00939653) | Phase 2 | Terminated | 6 | Clofarabine + etoposide + cyclophosphamide in relapsed/refractory AML. Terminated early with very few patients. |

**Note on the evidence level:** the L1 rating comes from the data compiled for this report. In practice, the trials listed above are mostly small Phase 1/2 studies or transplant studies in which cyclophosphamide is one part of the regimen. Only one Phase 3 trial (NCT05515029, 56 patients) appears, and it is still active. The strict criterion of two completed Phase 3 RCTs is therefore not clearly met for myeloid leukemia. Treat L1 with caution.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compared myeloablative conditioning regimens (including Bu/Cy) in adult AML in complete remission. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Busulfan-cyclophosphamide vs fludarabine-busulfan for allogeneic transplant in AML. |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Registry study | Cancer | Post-transplant cyclophosphamide vs ATG vs combination for GVHD prevention in haploidentical transplant for AML. |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Prognostic factors in haploidentical transplant with post-transplant cyclophosphamide for AML. |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | In 217 AML patients in remission, 2-year overall survival was 77% with myeloablative conditioning and post-transplant cyclophosphamide. |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Cohort | Bone Marrow Transplant | Single-unit cord blood vs haploidentical transplant with post-transplant cyclophosphamide in AML in first remission. |
| [42373850](https://pubmed.ncbi.nlm.nih.gov/42373850/) | 2026 | Cohort | Bone Marrow Transplant | Haploidentical vs mismatched unrelated donor transplant with post-transplant cyclophosphamide in secondary AML. |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cyclophosphamide/fludarabine nonmyeloablative vs myeloablative transplant in 165 AML patients; survival outcomes did not differ in the analysis. |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | Busulfan-cyclophosphamide vs total body irradiation-cyclophosphamide conditioning in AML; results are conflicting. |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | Post-transplant cyclophosphamide after matched donor transplant in pediatric AML. |

---

## Canada Market Information

Ten single-ingredient authorizations are valid. The dosage form and approved indication text were not available in the data compiled for this report. The five main authorizations are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02546744 | Cyclophosphamide for Injection USP | Injection (per product name) | Not available |
| 02547686 | Cyclophosphamide for Injection USP | Injection (per product name) | Not available |
| 02546736 | Cyclophosphamide for Injection USP | Injection (per product name) | Not available |
| 02241795 | Procytox Tab 25 mg | Tablet (per product name) | Not available |
| 02241796 | Procytox Tab 50 mg | Tablet (per product name) | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (leukopenia and neutropenia are expected; detailed toxicity data were not available in the data compiled for this report) |
| Emetogenicity Classification | Moderate to high, depending on dose (general drug-class knowledge) |
| Monitoring Items | CBC with differential, liver and renal function, urinalysis (bladder toxicity), electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified. Those shown are mostly Moderate, with a few Minor. The main ones are:
  - Amphotericin B products (conventional, lipid complex, cholesteryl sulfate, liposomal): Moderate
  - Sulfonylurea and related antidiabetics (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide), plus nateglinide, repaglinide, troglitazone: Moderate
  - Bupropion, aprepitant, metronidazole, nitisinone: Moderate
  - Levofloxacin, ondansetron: Minor
- **Bladder toxicity:** the literature compiled for the retroperitoneal neoplasm prediction describes drug-induced bladder and urinary disorders, which is relevant to cyclophosphamide.

Package insert warnings and contraindications were not available in the data compiled for this report; please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is already marketed in Canada and is a long-standing backbone of transplant conditioning and post-transplant GVHD prophylaxis in myeloid leukemia. Many Phase 1–3 trials and cohort studies support this use, but cyclophosphamide is almost always combined with other agents and the trials are mostly small. Guardrails are therefore needed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the evidence level for myeloid leukemia, ideally from randomized comparisons that isolate cyclophosphamide's contribution (for example post-transplant cyclophosphamide vs other GVHD prophylaxis)
- Review of Canadian approved indication text and whether the label already covers leukemia
- A safety monitoring plan (myelosuppression, bladder toxicity, the interactions listed above)

---

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Ganglioneuroblastoma | 99.43% | L3 | Research Question. Neuroblastoma is an approved indication, so the mechanism is plausible; evidence is mostly case reports and small series. |
| 3 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 99.38% | L5 | Hold. No mechanistic rationale; immunosuppression could be harmful in a T-cell dysfunction syndrome. |
| 4 | Retroperitoneal neoplasm | 99.37% | L4 | Research Question. Indirect, histology-dependent link; case reports only. |
| 5 | Lymph node cancer | 99.31% | L1 | Proceed with Guardrails. Supported by large Phase 3 adjuvant breast cancer trials and the approved lymphoma indication; the category mixes lymphoma and node-positive breast cancer, so read the evidence by sub-disease. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

