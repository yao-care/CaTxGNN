---
layout: default
title: Abatacept
parent: Moderate Evidence (L3-L4)
nav_order: 12
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Abatacept: predicted new indication Rheumatoid vasculitis (evidence level L4). Approved use: Rheumatoid arthritis"
---

# Abatacept
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Abatacept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Abatacept is a biologic originally used to treat rheumatoid arthritis, juvenile idiopathic arthritis and spondyloarthropathy.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
but the support is thin: **1 registered clinical trial** (which does not test abatacept in vasculitis) and **20 publications**, most of them case reports or general reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (the approved-indication text for the Canadian licences is not available; based on the original indications from the knowledge graph) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Abatacept is a CTLA4-Ig fusion protein. It blocks CD28–CD80/86 T-cell co-stimulation, which is how it works in rheumatoid arthritis.

Rheumatoid vasculitis is a serious complication of rheumatoid arthritis, driven by T cells and immune complexes. Because the drug acts on the T-cell pathway behind the disease it is already used for, the prediction is mechanistically plausible.

The evidence is mostly case-level. One report describes rapid improvement in a patient who had failed methotrexate, TNF inhibitors, an IL-6 inhibitor and plasmapheresis. Another describes abatacept as a therapeutic option in a patient with common variable immunodeficiency. However, other reports describe new-onset vasculitis, orbital vasculitis or ANCA-associated nephritis arising during abatacept therapy. That is a signal that the drug may not be uniformly protective.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients having shoulder arthroplasty. It does not test abatacept efficacy in vasculitis. |

No trial directly tests abatacept in rheumatoid vasculitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | Case report/Review | Cureus | Abatacept as a treatment option for rheumatoid vasculitis in a patient with RA and common variable immunodeficiency |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | Case report | Modern Rheumatology | Rapid improvement of rheumatoid vasculitis after abatacept, following failure of methotrexate, TNF inhibitors, IL-6 inhibition and plasmapheresis |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | Case report | Joint Bone Spine | New-onset rheumatoid vasculitis during abatacept therapy, improved after rituximab |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | Case report | Ophthalmic Plast Reconstr Surg | Orbital vasculitis in an RA patient on abatacept; progressed despite cyclophosphamide |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case report | Internal Medicine | ANCA-associated nephritis during abatacept and adalimumab therapy; attenuated by tocilizumab |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort | Ann Rheum Dis | Routine ANA testing to predict biologic-induced lupus and vasculitis in RA |
| [24840285](https://pubmed.ncbi.nlm.nih.gov/24840285/) | 2014 | Systematic review and cohort | Autoimmun Rev | Biologics-induced autoimmune renal disorders in rheumatic diseases |
| [33595833](https://pubmed.ncbi.nlm.nih.gov/33595833/) | 2021 | Systematic review | BioDrugs | Biologics and targeted synthetic drugs can induce immune-mediated glomerular disorders |
| [34474172](https://pubmed.ncbi.nlm.nih.gov/34474172/) | 2022 | Systematic review/Meta-analysis | Autoimmun Rev | Response to SARS-CoV-2 vaccination in immune-mediated inflammatory diseases |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Update on biologic therapy for autoimmune diseases |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02282097 | ORENCIA | Not specified | Not specified |
| 02402475 | ORENCIA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 73 interactions were recorded. Those flagged **Major** include:
  - adalimumab
  - baricitinib
  - certolizumab pegol
  - BCG live vaccine

  **Moderate** interactions include:
  - anakinra
  - canakinumab
  - azathioprine
  - alemtuzumab
  - alefacept
  - roflumilast
  - several live vaccines (e.g., adenovirus type 4, anthrax, cholera)

  Zinc salts are Minor. These are mostly additive immunosuppression or live-vaccine concerns.
- **Signal from the literature**: several reports describe vasculitis or ANCA-associated nephritis arising during abatacept therapy, which needs attention in this indication.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a few case reports. No trial tests abatacept in rheumatoid vasculitis, and some reports describe vasculitis emerging during treatment. The mechanism is plausible but unproven.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this is currently a blocking gap for safety screening)
- Mechanism of action data
- Systematic case-series or controlled data on abatacept in rheumatoid vasculitis, including how to reconcile the cases of vasculitis arising during therapy

**Other predicted indications, for context:**
- **Polyarticular juvenile rheumatoid arthritis** (score 99.83%, L1, Proceed with Guardrails). This is essentially a rediscovery of the approved juvenile arthritis use, supported by completed Phase 3 trials such as the randomized-withdrawal study NCT00095173. Guardrails: confirm age and dosing labelling, monitor infection, and note the product process-control issue raised in the literature.
- **Inflammatory spondylopathy** (L2, Research Question). A completed Phase 3 placebo-controlled trial of subcutaneous abatacept (NCT01860976, n=489) appears to be in psoriatic arthritis, but the trial title is truncated and the population needs confirmation. A Phase 2b trial (NCT00534313) was terminated.
- **Ankylosing spondylitis** (L3, Research Question). The only abatacept-specific study is a small open-label pilot (n=30). Reviews state that T-cell-targeting biologics such as abatacept are not effective in axial disease.
- **Remaining predictions** (hypermobility of coccyx, Kummell disease, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, vertebral disease, spondyloarthropathy susceptibility): no plausible mechanistic link or direct evidence. These are Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

