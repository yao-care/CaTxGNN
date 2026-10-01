---
layout: default
title: Cyclophosphamide
parent: Model Prediction Only (L5)
nav_order: 230
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

# Cyclophosphamide: From Established Antineoplastic Use to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy agent that is marketed in Canada under 10 DINs. The TxGNN model predicts it may be effective for **myeloid leukemia**. The literature includes **50 registered clinical trials** and **20 publications**, but most describe cyclophosphamide as part of transplant conditioning or GVHD prophylaxis regimens rather than as a stand-alone treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data (cyclophosphamide is an alkylating antineoplastic agent) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 (see the note under Clinical Trial Evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cyclophosphamide is a prodrug activated by liver CYP450 enzymes. Its active metabolites cross-link DNA, which kills rapidly dividing cells and also suppresses the immune system. Detailed mechanism-of-action data was not supplied in the source record, so this description comes from the mechanistic rationale in the evidence pack.

These two effects are already used in myeloid leukemia care around stem cell transplantation:

- **Conditioning:** Busulfan-cyclophosphamide (BuCy) is a standard myeloablative conditioning regimen for acute myeloid leukemia (AML) patients receiving allogeneic transplant. Cyclophosphamide is also combined with fludarabine in non-myeloablative regimens.
- **Post-transplant cyclophosphamide (PTCy):** It selectively depletes alloreactive T cells to prevent graft-versus-host disease (GVHD). It is now widely studied in haploidentical and matched-donor transplants for AML.
- **Cytoreduction:** One small series used high-dose cyclophosphamide to reduce blast counts in AML with hyperleukocytosis.

The "new" indication is therefore best read as a role within transplant-based treatment of myeloid leukemia. Cyclophosphamide is not being proposed as a stand-alone leukemia drug.

---

## Clinical Trial Evidence

The 10 most relevant of the 50 registered trials are shown. Relevance grades come from the evidence pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | Completed | 20 | Decitabine, total-body irradiation, bone marrow transplant and high-dose cyclophosphamide in relapsed/refractory AML. Cyclophosphamide is a core component (Grade A). |
| [NCT02294552](https://clinicaltrials.gov/study/NCT02294552) | Phase 2 | Completed | 200 | High-dose post-transplant cyclophosphamide as GVHD prophylaxis after allogeneic transplant, with a risk-adapted design. |
| [NCT02094794](https://clinicaltrials.gov/study/NCT02094794) | Phase 2 | Active, not recruiting | 108 | Total marrow and lymphoid irradiation plus cyclophosphamide and etoposide as conditioning in high-risk ALL or AML. |
| [NCT03246906](https://clinicaltrials.gov/study/NCT03246906) | Phase 2 | Terminated | 150 | Randomized comparison of cyclosporine and sirolimus with MMF versus PTCy for GVHD prophylaxis in hematologic malignancies. |
| [NCT02759822](https://clinicaltrials.gov/study/NCT02759822) | N/A | Unknown | 30 | Observational cohort of haploidentical transplant with PTCy for acute leukemias. |
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | Recruiting | 700 | International randomized pediatric AML trial. Cyclophosphamide is not confirmed as the randomized variable, so it is not counted as direct evidence (Grade B). |
| [NCT00356928](https://clinicaltrials.gov/study/NCT00356928) | Phase 1 | Terminated | 14 | Cyclophosphamide plus haploidentical CD8+ T-cell-depleted transplant in MDS, AML, lymphoma and myeloproliferative disorders. |
| [NCT00005804](https://clinicaltrials.gov/study/NCT00005804) | Phase 2 | Completed | Not reported | Unrelated-donor marrow transplant in hematologic cancers. Cyclophosphamide is probably part of conditioning but this is unconfirmed (Grade B). |
| [NCT00047060](https://clinicaltrials.gov/study/NCT00047060) | Phase 1/2 | Completed | 5 | Stem cell transplant for mycosis fungoides/Sezary syndrome. Very small sample, indirect (Grade B). |
| [NCT03349502](https://clinicaltrials.gov/study/NCT03349502) | Phase 2 | Completed | 11 | Fludarabine-cyclophosphamide lymphodepletion followed by NK cells in refractory/relapsed AML. Cyclophosphamide is an adjunct only. |

**Evidence level note:** The evidence pack assigns L2. Strictly, no completed randomized Phase 2/3 trial with cyclophosphamide as the tested variable is shown. The completed trials are mostly single-arm or list cyclophosphamide only as part of a regimen. The L2 label should be treated as a ceiling rather than a firm grade.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compared myeloablative conditioning regimens in adult AML in remission. Bu/Cy is the commonly used reference regimen. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | BuCy is the standard myeloablative regimen for AML allo-HSCT. Compared with fludarabine-busulfan, which appears similarly effective with less toxicity. |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Cohort | Bone Marrow Transplant | EBMT study of 1,823 AML patients in first remission given PTCy. Examined conditioning intensity by cytogenetic and molecular risk. |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Not classified | Hematol Oncol Stem Cell Ther | Compared busulfan/cyclophosphamide with busulfan/fludarabine in AML and MDS, with a focus on quality of life. |
| [32428903](https://pubmed.ncbi.nlm.nih.gov/32428903/) | 2021 | Not classified | Acta Haematol | PTCy plus ATG compared with other GVHD prophylaxis regimens in high-risk AML/MDS. |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Not classified | Am J Hematol | Cy/Flu non-myeloablative transplant versus myeloablative transplant in 165 AML patients. Survival was not different in univariate analysis. |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohort | Transplant Immunol | Cladribine added to BuCy conditioning in relapsed/refractory AML. |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohort | Eur J Haematol | Reduced-intensity versus myeloablative conditioning in AML patients under 65 given ATG plus PTCy. |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Not classified | Leuk Lymphoma | High-dose cyclophosphamide (60 mg/kg) for cytoreduction in 27 patients with AML or blast-phase CML with hyperleukocytosis or leukostasis. |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Not classified | Pediatr Hematol Oncol | Clofarabine, cyclophosphamide and etoposide in 17 children with relapsed/refractory AML. 7 patients (41%) responded. |

---

## Canada Market Information

Ten authorizations are on record. Dosage form and approved indication text were not available in the licence data. The first five are shown.

| DIN | Product Name |
|---------|------|
| 02546744 | Cyclophosphamide for Injection USP |
| 02547686 | Cyclophosphamide for Injection USP |
| 02241798 | Procytox |
| 02546736 | Cyclophosphamide for Injection USP |
| 02241795 | Procytox Tab 25 mg |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, oxazaphosphorine class, prodrug) |
| Myelosuppression Risk | High, dose-dependent (neutropenia is the main concern, especially at conditioning doses) |
| Emetogenicity Classification | Moderate, rising to high at high intravenous doses |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis for hematuria (hemorrhagic cystitis) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are drug-class information and are not drawn from the evidence pack. Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Secondary malignancy:** One case report (PMID 25612567) describes acute myeloid leukemia arising early after cyclophosphamide treatment. Cyclophosphamide is a recognized cause of therapy-related AML and MDS. This is relevant when the same drug is proposed for myeloid leukemia.
- **Drug interactions:** No interaction records were found in the queried database.

Health Canada package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is well established in AML transplant conditioning (BuCy) and post-transplant GVHD prophylaxis, with several completed Phase 2 trials and many cohort studies. However, the direct evidence is mostly single-arm or regimen-level. Cyclophosphamide is rarely the isolated tested variable, so this supports a role within transplant regimens rather than a stand-alone leukemia indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Indication text for the Canadian DINs, to confirm the original approved uses and whether leukemia is already covered.
- Detailed mechanism-of-action data from DrugBank.
- Confirmation from full trial protocols of which trials test cyclophosphamide directly (for example NCT02724163, NCT03246906).
- A defined scope: conditioning and PTCy in transplant settings versus cytoreduction, with a safety plan covering myelosuppression, hemorrhagic cystitis and secondary malignancy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

