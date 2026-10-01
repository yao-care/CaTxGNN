---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 893
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide is a parathyroid hormone (PTH 1-34) analogue, an anabolic bone agent marketed in Canada for osteoporosis.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but there are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model score alone.
Among the other predictions, **pregnancy-associated osteoporosis** is the only one with meaningful supporting literature (observational and review level).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (not stated in the Canadian licence records; inferred from the drug class and the supplied literature) |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Teriparatide is known to be a PTH1R agonist that stimulates osteoblast-mediated bone formation, and its efficacy in osteoporosis is established.

For duodenal ulcer, the review found no plausible PTH1R-mediated pathway to ulcer healing. The score of 99.86% (graph rank 3,373) most likely reflects proximity within the knowledge graph rather than a biological rationale. The same applies to several other top-ranked predictions (esophageal malformation, duodenal obstruction, duodenogastric reflux), which are structural or gastrointestinal conditions an anabolic bone agent is unlikely to modify. This prediction should be treated as a hypothesis only.

By contrast, the **pregnancy-associated osteoporosis** prediction (rank 8, score 99.55%) has a clear biological rationale. PTH(1-34) builds bone, and that addresses the skeletal fragility in this condition. This is the most credible direction in this candidate set.

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenal ulcer.

For the best-supported alternative prediction, pregnancy-associated osteoporosis, two registered trials were retrieved. Neither studies the condition directly, so both give only indirect support:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | PTH(1-34) with periodontal surgery for oral bone regeneration; shows anabolic activity but does not address pregnancy-associated osteoporosis |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | NA | Completed | 141 | Renal osteodystrophy in chronic kidney disease; a different bone disease context |

## Literature Evidence

Currently no related literature available for duodenal ulcer.

For pregnancy-associated osteoporosis, the retrieved literature is observational, case-series and review level. No RCT was found, and relevance was judged from titles and abstracts only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic review | J Clin Endocrinol Metab | Comparative effectiveness of interventions in pregnancy and lactation-associated osteoporosis |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic review / meta-analysis | Osteoporos Int | 35 studies, 943 patients; treatment response analysis inconclusive due to limited data |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Cohort | Calcif Tissue Int | Retrospective multicentre study of teriparatide vs conventional management on bone density and trabecular bone score in premenopausal women |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Strategies for pregnancy and lactation-associated osteoporosis, with a focus on teriparatide |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Case series | Geburtshilfe Frauenheilkd | Teriparatide and subsequent fractures and bone density in 47 women with vertebral fractures |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Retrospective | Calcif Tissue Int | Bone density after teriparatide discontinuation, with or without antiresorptive therapy |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2254689 | FORTEO |
| 2486423 | TEVA-TERIPARATIDE INJECTION |
| 2495589 | OSNUVO |
| 2498804 | APO-TERIPARATIDE INJECTION |

Dosage form and approved indication text are not recorded for these licences.

## Safety Considerations

Please refer to the package insert for safety information.

One literature signal is worth noting. A 2016 case report (PMID 26992073) describes worsening of calcinosis cutis during teriparatide treatment in two osteoporotic patients with systemic autoimmune disease. For pregnancy-associated osteoporosis, safety around lactation and pregnancy planning would need guardrails.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction is supported only by a graph score. It has no trials, no literature and no plausible mechanism, so it should not be advanced. Most other top-ranked predictions are likely false positives, and Worth syndrome (a sclerosing bone disorder) is mechanistically counter-indicated for an anabolic bone agent. Pregnancy-associated osteoporosis (L3, "Research Question") is the one direction worth pursuing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Abstract-level review of the pregnancy-associated osteoporosis literature, since the current assessment is based on titles and short abstracts
- A decision on whether to re-prioritise the candidate from duodenal ulcer to pregnancy-associated osteoporosis
- A lactation and pregnancy-planning safety assessment before any repurposing step for that indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

