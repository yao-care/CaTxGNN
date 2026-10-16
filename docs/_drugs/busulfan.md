---
layout: default
title: Busulfan
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Busulfan: predicted new indication Myelodysplastic syndrome (evidence level L5). Approved use: Not stated in the Canadian licence records compiled for this report"
monitor_inn: "BUSULFAN"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
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

# Busulfan: From Conditioning Therapy in Hematologic Malignancy to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is an alkylating chemotherapy agent marketed in Canada in three products (injection, oral and generic). The TxGNN model predicts it may be effective for **myelodysplastic syndrome (MDS)**, with **40 clinical trials** and **20 publications** compiled for this prediction. Evidence supports busulfan as a conditioning agent before allogeneic stem cell transplantation, not as a standalone MDS therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records compiled for this report |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 (at least two completed Phase 3 RCTs are listed, e.g. NCT00005866 and NCT00822393, and Phase 3 publications) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, busulfan is an alkylating agent that cross-links DNA and is myeloablative.

Allogeneic hematopoietic stem cell transplantation (HSCT) is the only potentially curative treatment for MDS. Busulfan-based conditioning eliminates malignant clones and creates marrow space for donor engraftment. Busulfan is therefore used as part of a transplant conditioning regimen (for example with fludarabine or cyclophosphamide), not as a stand-alone MDS drug.

Other predictions follow the same logic. Refractory cytopenia of childhood (a paediatric MDS subtype), unclassified MDS and aplastic-type anaemia (aregenerative anaemia) are treated with transplant, and busulfan-containing regimens are used there. Several lower-ranked predictions have no supporting evidence or no credible mechanistic link (see below).

## Clinical Trial Evidence

The table shows the most relevant trials for MDS (the top prediction). Most trials test busulfan as part of a combination conditioning regimen, so the benefit of busulfan alone cannot be separated out.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | Completed | 240 | Busulfan-TBI vs cyclophosphamide-TBI conditioning in advanced MDS or MDS-related AML |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | Completed | 570 | Treosulfan-based vs reduced-intensity busulfan-based conditioning in AML/MDS patients ineligible for standard conditioning |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | Venetoclax added to fractionated busulfan regimen in high-risk AML and MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | G-CSF + decitabine + BUCY vs G-CSF + decitabine + BF in high-risk MDS |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Same comparison in RAEB-1, RAEB-2 and AML secondary to MDS |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | High-dose IV busulfan plus fludarabine with allogeneic transplant in AML and MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax with timed sequential busulfan, cladribine and fludarabine before donor transplant |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Azacitidine added to busulfan/fludarabine reduced-intensity conditioning for MDS and older AML |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | Single-arm FLU-BU-MEL conditioning for MDS |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | Completed | 34 | Reduced-intensity busulfan/clofarabine conditioning; small single-arm study |

Over 40 trials were compiled for MDS in total, and the table lists the 10 most relevant. A withdrawn trial with zero enrolment (NCT06337331) provides no evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | Lancet Haematol | Treosulfan + fludarabine vs reduced-intensity busulfan + fludarabine in older AML/MDS patients (non-inferiority, phase 3) |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT | Am J Hematol | Final analysis of the same trial; treosulfan improved outcomes compared with reduced-intensity busulfan |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT | Transplant Cell Ther | Two fractionation schedules of myeloablative busulfan with fludarabine and cladribine in AML/MDS (phase 2) |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 trial | Lancet Haematol | G-CSF + decitabine + BU/CY vs BU/CY conditioning to reduce relapse in MDS-RAEB or secondary AML |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | Allogeneic transplant is the only potentially curative therapy for MDS and myelofibrosis |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis | Front Oncol | Reduced-intensity vs myeloablative conditioning in AML and MDS |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Meta-analysis | Front Oncol | Long-term outcomes of treosulfan- vs busulfan-based conditioning in MDS and AML |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registry analysis | Bone Marrow Transplant | Fludarabine/busulfan vs busulfan/cyclophosphamide myeloablative conditioning for MDS (propensity-matched) |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Risk assessment | Pediatr Blood Cancer | Busulfan and subsequent malignancy risk |
| [38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/) | 2024 | Cohort | Transplant Cell Ther | Long-term complications of treosulfan vs busulfan conditioning in children with leukaemia or MDS |

## Other Predicted Indications

| Rank | Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| 2 | Refractory cytopenia of childhood | L2 | Proceed with Guardrails | Paediatric MDS subtype; Phase 2 transplant trials, with one paediatric cohort study (PMID 25498905) |
| 3 | Unclassified MDS | L3 | Research Question | Only one old (1994) report |
| 4 | Partial deletion of chromosome 5q | L4 | Hold | No direct trials or literature |
| 5 | Aregenerative anaemia | L1 | Proceed with Guardrails | Evidence is mostly general transplant-conditioning literature; the disease label is broad and mixed |
| 6 | Severe congenital hypochromic anaemia with ringed sideroblasts | L5 | Hold | Prediction only |
| 7 | HIV infection | L2 | Research Question | Busulfan only conditions marrow for gene-modified cell therapy; small early-phase trials; not an antiviral |
| 8 | Neurodevelopmental disorder with ataxic gait | L5 | Hold | No plausible link |
| 9 | Seborrheic keratosis | L5 | Hold | No credible link; systemic myelotoxic therapy would be inappropriate for a benign lesion |
| 10 | Simian immunodeficiency virus infection | L5 | Hold | Animal-model disease; no direct evidence |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02463733 | BUSULFAN FOR INJECTION | Not stated | Not stated |
| 00004618 | MYLERAN | Not stated | Not stated |
| 02477343 | PMS-BUSULFAN | Not stated | Not stated |

All three are valid single-ingredient licences. Dosage form, manufacturer and approved indication text were not available in the compiled data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (myeloablative at conditioning doses). This is consistent with the knowledge-graph warnings on neutropenia, thrombocytopenia, anaemia and agranulocytosis |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function; pharmacokinetic (targeted) dosing is used in some trials |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

**Contraindication signals (from a drug–disease knowledge graph, not label text):** epilepsy, thrombocytopenia, hyperglycaemia, fungal and other infectious disease, dermatophytosis, potassium deficiency, hyperuricaemia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia and Fanconi anaemia), pulmonary fibrosis and post-inflammatory pulmonary fibrosis. These must be checked against the official label.

**Drug interactions:** The interaction screen returned 100 interacting drugs. The main ones listed:
- **Major:** metronidazole
- **Moderate:** aprepitant, miconazole
- **Minor:** levofloxacin
- **Unrated:** amphotericin B, mannitol, proton-pump inhibitors, morphine, vancomycin, corticosteroids, H2 blockers and antiemetics (granisetron, ondansetron, metoclopramide)

**Literature safety signal:** A published risk assessment addresses secondary malignancy after busulfan exposure (PMID 37856098), and conditioning toxicity is a major concern in transplant populations.

Please refer to the package insert for label warnings and contraindications; these were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 randomised trials and several Phase 2 studies support busulfan-based conditioning before allogeneic transplant in MDS, and the drug is already marketed in Canada. However, busulfan is only one part of combination regimens, the evidence concerns transplant conditioning rather than disease-modifying treatment, and the recent randomised comparison favoured treosulfan over reduced-intensity busulfan in older patients. The Canadian licence data also lack indication and label information.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication and dosage form for each DIN
- Mechanism of action data
- Clarification that use is limited to conditioning within transplant regimens, with dose monitoring and a plan for myelosuppression and secondary malignancy risk
- Review of the knowledge-graph contraindication signals and the major interaction (metronidazole) before any use

Predictions for HIV infection and for lower-ranked indications without evidence should remain research questions or on hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

