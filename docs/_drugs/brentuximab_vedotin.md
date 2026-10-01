---
layout: default
title: Brentuximab Vedotin
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From CD30-Positive Lymphomas (Hodgkin Lymphoma, sALCL) to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (Adcetris) is a CD30-directed antibody-drug conjugate. The trial records in the Evidence Pack describe it as registered for Hodgkin lymphoma, relapsed systemic anaplastic large cell lymphoma (sALCL) and CD30+ mycosis fungoides. The TxGNN model predicts it may be useful for **follicular lymphoma**, but the support is thin: **6 registered trials** (none completed, three withdrawn or terminated, none with results) and **20 publications**, mostly about peripheral T-cell lymphoma (PTCL) rather than follicular lymphoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data. Trial descriptions in the pack cite Hodgkin lymphoma, relapsed sALCL and CD30+ cutaneous T-cell lymphoma (mycosis fungoides) |
| Predicted New Indication | Follicular lymphoma |
| TxGNN Prediction Score | 99.89% (model rank 2693) |
| Evidence Level | L5 (the pack lists L2, but no completed randomized trial in follicular lymphoma supports it, so I rated it conservatively) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The pack has no formal mechanism-of-action entry for this drug. From the pack's rationale notes, brentuximab vedotin is an antibody-drug conjugate. The antibody binds CD30 and delivers the cytotoxic payload MMAE into CD30-expressing cells. This works well in Hodgkin lymphoma and anaplastic large cell lymphoma, where CD30 is strongly expressed.

Follicular lymphoma is a B-cell lymphoma, so the link to the original indications is disease-family similarity rather than a shared target. CD30 is expressed only variably or at low levels in follicular lymphoma, so the mechanistic rationale is weaker than in Hodgkin lymphoma or ALCL. The KG prediction is therefore plausible as a hypothesis but not mechanistically strong.

No follicular-lymphoma-specific efficacy data are in the pack. The one on-indication trial is a small, still-recruiting phase 2 study of brentuximab vedotin plus bendamustine. Other candidates in the same prediction list have much stronger support, for example the broad "B-cell neoplasm" term (Hodgkin lymphoma, DLBCL, PMBCL), which has phase 3 data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | Brentuximab vedotin plus bendamustine in relapsed/refractory follicular lymphoma. Directly on-indication, no results yet |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | Brentuximab vedotin plus rituximab as frontline therapy in CD30+ and/or EBV+ lymphomas. Follicular lymphoma is likely only one eligible histology |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized rituximab-bendamustine with or without brentuximab vedotin in CD30+ DLBCL. The only randomized design, but underpowered |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin plus pembrolizumab in recurrent PTCL. No participants enrolled |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Sequential rituximab, brentuximab vedotin and bendamustine in post-transplant lymphoproliferative disorder. No participants enrolled |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin, bendamustine and rituximab in CD30+ relapsed/refractory B-cell NHL. No participants enrolled |

## Literature Evidence

No randomized controlled trials were retrieved. Most items concern PTCL and are only indirect support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2 study | Blood Adv | LYSA study of brentuximab vedotin plus gemcitabine, then brentuximab vedotin maintenance, in relapsed/refractory CD30+ PTCL. Indirect for follicular lymphoma |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Clinical study | Eur J Haematol | Brentuximab vedotin added to ICE chemotherapy in relapsed/refractory PTCL. Indirect |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Retrospective real-world study | Adv Ther | Brentuximab vedotin plus cyclophosphamide, epirubicin and prednisone in untreated CD30+ PTCL. Indirect |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Treatment approaches for common PTCL subtypes, including brentuximab vedotin plus CHP for CD30+ disease |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology ASH Educ Program | Incorporating brentuximab vedotin and novel agents into PTCL management |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leuk Res Rep | Immunotherapy in indolent NHL, including follicular lymphoma. The only item that covers the target disease |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case report | Gulf J Oncol | Grade I follicular lymphoma transformed to CD30+ ALK1− ALCL, with complete response to brentuximab vedotin and high-dose methotrexate. The response was in the transformed T-cell disease, not follicular lymphoma |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplant | Post-autologous-transplant maintenance in lymphoma. Mentions rituximab maintenance in follicular lymphoma |
| [38028985](https://pubmed.ncbi.nlm.nih.gov/38028985/) | 2023 | Case report | Case Rep Hematol | Follicular lymphoma transformation to EBV+ DLBCL and EBV+ classic Hodgkin lymphoma. Diagnostic report |
| [41409526](https://pubmed.ncbi.nlm.nih.gov/41409526/) | 2025 | Case report | Skin Appendage Disord | Follicular mucinosis (a skin condition, not follicular lymphoma) responding to brentuximab vedotin. Weak relevance because of the name similarity |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2401347 | ADCETRIS |

## Cytotoxicity

The pack has no toxicity data, so the entries below are general class knowledge and should be checked against the current package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy: CD30-directed antibody-drug conjugate with a cytotoxic MMAE payload |
| Myelosuppression Risk | Medium (neutropenia is a recognized toxicity) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, peripheral neuropathy, infusion reactions, signs of infection (including JC virus/PML) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only on-indication trial is a small phase 2 study (n=23) that is still recruiting, and the other follicular-lymphoma-adjacent trials were withdrawn or terminated. CD30 expression in follicular lymphoma is low and variable, and the literature is mostly about PTCL. The 99.89% TxGNN score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Results from NCT04587687 (brentuximab vedotin plus bendamustine in relapsed/refractory follicular lymphoma)
- Data on CD30 expression and response in follicular lymphoma patients
- The Canadian package insert (warnings, contraindications, approved indications, dosage form) and the DrugBank mechanism-of-action entry, both missing from the current pack
- A comparison with the "B-cell neoplasm" candidate, which has stronger evidence (phase 3 data), and a check on whether that use is already on-label

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

