---
layout: default
title: Busulfan
parent: Model Prediction Only (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Hematologic Cancer Chemotherapy to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is an alkylating chemotherapy drug used against blood cancers and as a conditioning agent before stem cell transplant. The Canadian licence data in the pack do not state its approved indications.
The TxGNN model predicts it may be useful for **myelodysplastic syndrome (MDS)**, with **50 clinical trials** and **20 publications** retrieved.
This is mainly a confirmation of existing practice, because busulfan is already used as part of transplant conditioning regimens for MDS. It is not a stand-alone MDS treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence text provided (general use: hematologic malignancy chemotherapy and transplant conditioning) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 (see caveat below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

Only one Phase 3 trial is completed (NCT00469144). The L1 rating rests on the pack's classification and on the several Phase 3 RCTs in the literature. In those trials busulfan is often a comparator or backbone rather than the tested variable.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the pack. Busulfan is a bifunctional alkylating agent: it cross-links DNA and destroys bone marrow cells (myeloablation). This makes it a long-established backbone of the conditioning regimen given before allogeneic hematopoietic stem cell transplantation (allo-HSCT).

Allo-HSCT is the only potentially curative treatment for MDS and the standard of care for eligible higher-risk patients. Conditioning must clear the diseased marrow and prevent rejection of donor cells, which is where busulfan is used. The trial and literature evidence consistently involves busulfan combined with fludarabine or cyclophosphamide, and sometimes with other agents.

Two limits apply. First, the evidence supports busulfan as one component of a regimen, not as stand-alone MDS therapy. Second, the drug is already used this way, so this is not a novel repurposing. The value of the prediction is confirming and documenting a use that may not be in the Canadian labelling.

---

## Clinical Trial Evidence

The pack lists 50 trials for this indication. The table shows the 10 most relevant. Relevance grading is still pending for many trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00469144](https://clinicaltrials.gov/study/NCT00469144) | Phase 3 | Completed | 233 | Randomized comparison of blood-level-guided IV busulfan versus fixed-dose IV busulfan, each with fludarabine, in AML/MDS transplant |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | G-CSF + decitabine + busulfan/cyclophosphamide versus G-CSF + decitabine + busulfan/fludarabine in RAEB-1/2 and secondary AML after MDS |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Melphalan 100 vs 140 mg/m² in a melphalan-busulfan-fludarabine regimen for adult AML/MDS |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | High-dose IV busulfan plus fludarabine before allogeneic transplant for AML and MDS |
| [NCT00582933](https://clinicaltrials.gov/study/NCT00582933) | Phase 2 | Completed | 96 | Chemotherapy-only conditioning with IV busulfan, melphalan and fludarabine before T-cell-depleted transplant |
| [NCT00469014](https://clinicaltrials.gov/study/NCT00469014) | Phase 2 | Completed | 72 | Busulfan-fludarabine-clofarabine conditioning in advanced AML, MDS and CML (randomized Phase 2) |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Completed | 30 | Clofarabine + IV busulfan + thymoglobulin as reduced-intensity conditioning in high-risk AML, MDS or ALL |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Phase 2 | Active, not recruiting | 204 | Timed sequential busulfan and fludarabine with post-transplant cyclophosphamide in blood cancers |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | N/A | Recruiting | 138 | Randomized trial of venetoclax-enhanced BUCY versus standard BUCY conditioning in high-risk AML/MDS |
| [NCT00226512](https://clinicaltrials.gov/study/NCT00226512) | Phase 3 | Withdrawn | 203 | Fludarabine + busulfan with or without anti-lymphocyte antibodies in AML/MDS (withdrawn; no results) |

---

## Literature Evidence

The pack lists 20 publications. The table shows the 10 most relevant, with RCTs first. The abstracts in the pack are truncated, so the findings below describe study design rather than outcomes.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT (Phase 3) | Am J Hematol | Final analysis of treosulfan versus reduced-intensity busulfan conditioning in older AML/MDS patients (n=476 at the interim analysis); busulfan is the comparator |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (Phase 3) | Lancet Haematol | Non-inferiority trial of treosulfan versus reduced-intensity busulfan, each plus fludarabine, in older AML/MDS patients |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (Phase 3) | J Clin Oncol | Myeloablative versus reduced-intensity conditioning in AML/MDS; the regimens are busulfan-based per the trial's general design, which the abstract does not confirm |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Phase 3, per title) | Lancet Haematol | G-CSF + decitabine + busulfan-cyclophosphamide versus busulfan-cyclophosphamide, to reduce relapse in MDS-RAEB or secondary AML |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | Contemporary review of allo-HSCT for MDS and myelofibrosis; HSCT is the only potentially curative option |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis of RCTs | Front Oncol | Reduced-intensity versus myeloablative conditioning before allo-HSCT in AML and MDS |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic review / meta-analysis | Front Oncol | Long-term outcomes of treosulfan- versus busulfan-based conditioning in MDS and AML |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Cohort | Cancer | Fractionated myeloablative busulfan conditioning in older AML/MDS patients, reported to improve survival |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohort (propensity-matched) | Bone Marrow Transplant | Japanese registry comparison of fludarabine/busulfan versus busulfan/cyclophosphamide in MDS |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Cohort (propensity-matched) | Transplant Cell Ther | Myeloablative versus reduced-intensity fludarabine/busulfan in MDS |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2463733 | BUSULFAN FOR INJECTION |
| 4618 | MYLERAN |
| 2477343 | PMS-BUSULFAN |

Dosage form and approved indication text were not provided for these licences. Whether MDS conditioning falls within the Canadian labelling cannot be confirmed from the pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (bifunctional alkylating agent) |
| Myelosuppression Risk | High: the drug is used at myeloablative doses in conditioning, so profound and prolonged marrow suppression is expected |
| Emetogenicity Classification | Moderate (general class knowledge; please verify against the package insert) |
| Monitoring Items | CBC with differential, liver function, renal function, and drug exposure monitoring where used (blood-level-guided dosing appears in NCT00469144) |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full toxicity data.

---

## Safety Considerations

Please refer to the package insert for safety information. The Health Canada warnings and contraindications were not available in the pack, and no drug interaction records were found.

One literature item is relevant to safety. PMID 37856098 is an evidence-based risk assessment of subsequent malignancy after busulfan. It is worth reviewing before any protocol is finalized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan has strong, consistent support as a component of conditioning for allo-HSCT in MDS, including several Phase 3 RCTs. It is not evidence that busulfan works alone against MDS, and the use already exists in practice. The absence of Canadian safety data is a blocking gap.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications) for all three DINs
- Confirmation of whether MDS transplant conditioning is covered by current Canadian labelling
- Mechanism of action data from DrugBank
- Completed relevance grading for the many trials still marked pending
- A defined scope: busulfan as part of a conditioning regimen, with myelosuppression and transplant-specific safety monitoring

The other nine predicted indications are weaker. Refractory cytopenia of childhood has Phase 2 support only, and HIV has small studies only. The rest have no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

