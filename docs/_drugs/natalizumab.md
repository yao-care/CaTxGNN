---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 639
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is marketed in Canada as TYSABRI. The licence record in the Evidence Pack does not state an approved indication, although the supporting literature places it in multiple sclerosis (MS) care. The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and **0 publications** for this prediction, so the evidence rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record (literature context: multiple sclerosis) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Natalizumab is known to block alpha4 integrins (alpha4beta1/alpha4beta7). This limits leukocyte trafficking into inflamed tissue, so a role in inflammatory airway disease is conceivable.

This link is speculative. Bronchitis is frequently infectious, and natalizumab's immunosuppressive profile raises infection concerns. The high model score is not backed by any trial or publication, so the prediction should be treated as a hypothesis only.

### Other Predicted Indications

Four other indications were predicted. Only psoriasis has meaningful literature, and its signal is contradictory.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Parapsoriasis | 99.37% | L4 | Hold |
| 3 | Psoriasis | 99.19% | L4 | Research Question |
| 4 | Severe nonproliferative diabetic retinopathy | 99.18% | L5 | Hold |
| 5 | Acute lichenoid pityriasis | 99.04% | L4 | Hold |

- **Parapsoriasis and acute lichenoid pityriasis:** the only evidence is one case report (PMID 32470781). It describes dermatologic adverse events with fingolimod and natalizumab, a safety signal rather than a benefit. It is the same publication for both indications, so it is not independent evidence.
- **Severe nonproliferative diabetic retinopathy:** prediction only. Leukocyte adhesion contributes to retinal microvascular injury, but no supporting data were found.
- **Psoriasis:** several case reports describe new-onset or aggravated psoriasis during natalizumab. One 2021 observational report describes improvement of comorbid psoriasis in 18 MS patients. The direction of effect is unresolved.

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis. None are registered for the other four predicted indications either.

## Literature Evidence

Currently no related literature available for bronchitis.

The table below lists selected publications for the best-supported alternative, psoriasis. Study types are inferred from titles.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Observational | Neurol Neuroimmunol Neuroinflamm | Improvement of comorbid psoriasis in 18 MS patients treated with natalizumab |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | Treatment options for MS comorbid with psoriasis, RA and IBD |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case report | Dermatol Pract Concept | Natalizumab-induced pustular psoriasis of palms and soles |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case study + review | Case Rep Neurol | Plaque psoriasis developed during natalizumab; limited evidence that it induces or aggravates psoriasis |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case report + review | Neurol Sci | Arthritic psoriasis during natalizumab treatment |
| [23096069](https://pubmed.ncbi.nlm.nih.gov/23096069/) | 2012 | Case report | J Neurol | Severe, drug-resistant psoriasis worsening during natalizumab in a patient with MS |
| [28765121](https://pubmed.ncbi.nlm.nih.gov/28765121/) | 2018 | Review | Ann Rheum Dis | Novel therapies for immune-mediated inflammatory diseases, including psoriasis |

The list also contains several reviews on progressive multifocal leukoencephalopathy (PML) with monoclonal antibodies, including natalizumab. These address safety rather than psoriasis efficacy.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2286386 | TYSABRI |

## Safety Considerations

- **Drug Interactions:** no interactions were found in the query.
- **PML risk:** multiple reviews in the literature link natalizumab to progressive multifocal leukoencephalopathy, a rare and often fatal brain infection caused by JC virus.
- **Skin reactions:** case reports describe new-onset or aggravated psoriasis and other dermatologic adverse events.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has no trials or literature, so it is supported only by the model score (Level L5). Natalizumab's immunosuppressive profile and PML risk argue against an infectious airway indication without a strong rationale. Psoriasis is the only alternative with notable literature, and the case-level signals conflict, so it is a research question rather than a candidate for action.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action and original indication data from DrugBank or the Canadian licence record
- A dedicated observational or pharmacovigilance analysis of psoriasis, to resolve whether natalizumab induces or improves it
- A mechanistic and safety justification before any bronchitis or diabetic retinopathy work

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

