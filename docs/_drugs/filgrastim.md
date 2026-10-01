---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a G-CSF analog, generally used to raise neutrophil counts. The Canadian license data in this pack do not state an indication, so this is background knowledge. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the evidence is very weak. The **14 matched clinical trials** (10 shown) are keyword matches to transplant, CMV and oncology studies, and **no publications** were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (filgrastim is generally used for neutropenia) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (the pack labels it L4, but no mechanistic or preclinical study was found, so L5 fits better) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Based on general pharmacology, filgrastim acts on the G-CSF receptor to drive neutrophil progenitor proliferation and to mobilize CD34+ stem cells.

Primary release disorder of platelets is a functional platelet defect (impaired granule secretion). No known G-CSF pathway addresses it, and G-CSF is not a thrombopoietic agent. The very high TxGNN score reflects a knowledge-graph association only, with no supporting mechanism.

The matched trials are mostly stem cell transplant and oncology studies where filgrastim is likely only a mobilization or supportive agent. They are indirect evidence at best. The other nine predicted indications (including pseudo-von Willebrand disease, Glanzmann thrombasthenia and Scott syndrome) are weaker still, mostly with no trials or literature at all.

## Clinical Trial Evidence

All trials shown were graded as low relevance (Grade C). None tests filgrastim for platelet disorders.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous stem cell transplant vs best available therapy in relapsing multiple sclerosis. Filgrastim is at most a mobilization component. |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis to prevent CMV reactivation in critically ill patients. Unrelated to platelet function. |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Cord blood transplant in myeloid leukemia. Small and terminated. |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Lymphodepletion plus autologous stem cell transplant in severe lupus. |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs unselected autologous transplant in mantle cell and diffuse large B-cell lymphoma. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide GVHD prophylaxis platform. Filgrastim is not the studied intervention. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding of post-transplant cyclophosphamide for GVHD prophylaxis. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic transplant in hematologic malignancies. Filgrastim is supportive only. |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Oral dapansutrile in moderate COVID-19. Unrelated to filgrastim. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation in acute lung injury. Not relevant. |

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form, manufacturer and approved indication text are not provided in the pack. Five of the 13 authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 2441489 | GRASTOFIL |
| 1968017 | NEUPOGEN |
| 2521008 | NYPOZI |
| 2485591 | NIVESTYM |
| 2485656 | NIVESTYM |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the pack's DDI query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a graph-based prediction with no plausible mechanism. No matched trial addresses platelet release disorders, and there is no literature. Investing further is not justified on current evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Mechanism of action data (e.g., from DrugBank) to test any link between G-CSF signaling and platelet granule secretion
- Preclinical or case-level evidence of a filgrastim effect on platelet function
- Approved indication text and dosage forms for the Canadian licenses, to confirm the original indication and route compatibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

