---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 900
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "TERIPARATIDE"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
description: "Teriparatide: predicted new indication Duodenal ulcer (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Teriparatide: Duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) analog, originally used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model's top-ranked prediction is **duodenal ulcer**, but **no clinical trials and no publications** currently support it. The best-supported candidate among the model's top 10 predictions is **pregnancy-associated osteoporosis**, which has **no registered trials but 20 publications**, mostly observational studies and reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal ulcer (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 (duodenal ulcer); L4 (pregnancy-associated osteoporosis) |
| Canada Market Status | Marketed (valid licenses: 3 of 4) |
| Number of DINs | 4 (valid: 3) |
| Recommended Decision | Hold (duodenal ulcer); a research question for pregnancy-associated osteoporosis |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology records show that teriparatide is a peptide ligand of the **PTH1 receptor** and also acts at the **PTH2 receptor**. It is a PTH(1-34) analog that stimulates osteoblast activity and bone formation, which underlies its established use in osteoporosis.

**Duodenal ulcer (top prediction).** No mechanistic link between a bone-anabolic PTH analog and duodenal ulcer healing is supported by the data. The high score is a model output only. The other top-ranked predictions have the same problem: esophageal malformation, duodenal obstruction, duodenogastric reflux, esophageal disease, an inborn error of ketone metabolism and a retinal disease. None has a plausible mechanistic rationale or supporting evidence. The two papers retrieved for "esophageal disease" cover osteoporosis drug adverse events and worsening calcinosis cutis under teriparatide. They look like incidental keyword matches rather than support. Worth syndrome is a high-bone-mass disorder, so anabolic bone stimulation would be mechanistically counterproductive. The disease identity should also be verified, because the name is ambiguous.

**Pregnancy-associated osteoporosis (rank 8).** This is a close extension of the approved indication. The condition causes severe bone loss and vertebral fragility fractures, which teriparatide's bone-forming action directly addresses. The supporting literature includes meta-analyses, a teriparatide-focused review and several teriparatide cohort studies. There are no registered clinical trials.

**Amenorrhea (rank 10).** Amenorrhea itself is not a plausible target. The rationale applies to the low bone density seen in functional hypothalamic amenorrhea, so any benefit would be to the bone complication rather than to the amenorrhea.

## Clinical Trial Evidence

Currently no related clinical trials registered, for any of the top 10 predicted indications.

## Literature Evidence

Literature for the top-ranked prediction (duodenal ulcer): currently no related literature available.

The tables below cover the two predictions that have meaningful literature.

**Pregnancy-associated osteoporosis (rank 8)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic review / meta-analysis | J Clin Endocrinol Metab | Compares therapeutic interventions for pregnancy and lactation-associated osteoporosis (PLO); the best management has not been established |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic review / meta-analysis | Osteoporos Int | 35 studies, 943 patients; vertebral fractures and back pain were common, and treatment response analysis was inconclusive because of limited data |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Focuses on teriparatide use in PLO; notes that treatment strategies remain poorly defined because of the lack of clinical trials |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Retrospective cohort | Calcif Tissue Int | Teriparatide (20 μg/day) plus calcium vs. conventional management in PLO, assessing bone density and trabecular bone score |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Cohort | Geburtshilfe Frauenheilkd | 47 women with PLO and vertebral fractures treated with teriparatide; effect on subsequent fractures and bone density |
| [42113234](https://pubmed.ncbi.nlm.nih.gov/42113234/) | 2026 | Observational study | Osteoporos Int | Starting teriparatide less than 12 months postpartum gave two- to three-fold larger bone density gains than starting at 12 months or later |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Retrospective study | Calcif Tissue Int | Bone density after stopping teriparatide, with or without antiresorptive therapy, in PLO |
| [37819437](https://pubmed.ncbi.nlm.nih.gov/37819437/) | 2023 | Single-centre case series | Calcif Tissue Int | 16 patients over 20 years; reviews presentation, risk factors and treatment response |
| [42234275](https://pubmed.ncbi.nlm.nih.gov/42234275/) | 2026 | Patient survey | Arch Osteoporos | Teriparatide was the most commonly prescribed anti-osteoporosis drug among respondents |
| [36676643](https://pubmed.ncbi.nlm.nih.gov/36676643/) | 2022 | Case report | Medicina (Kaunas) | PLO successfully treated with romosozumab, an alternative to teriparatide |

**Amenorrhea (rank 10)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41505334](https://pubmed.ncbi.nlm.nih.gov/41505334/) | 2026 | Systematic review / network meta-analysis of RCTs | J Clin Endocrinol Metab | Pharmacological interventions to improve bone density in functional hypothalamic amenorrhea; comparative efficacy was previously unclear |
| [36303862](https://pubmed.ncbi.nlm.nih.gov/36303862/) | 2022 | Review | Front Endocrinol | Bone health in functional hypothalamic amenorrhea; estrogen deficiency is only part of the cause of skeletal fragility |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02254689 | FORTEO | Not listed | Not listed |
| 02486423 | TEVA-TERIPARATIDE INJECTION | Not listed | Not listed |
| 02498804 | APO-TERIPARATIDE INJECTION | Not listed | Not listed |
| 02495589 | OSNUVO | Not listed | Not listed |

All four licences are valid single-ingredient products.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): hypercalcemia, hyperparathyroidism, nephrocalcinosis, urolithiasis, phosphorus metabolism disease, bone osteosarcoma, bone Paget disease, juvenile Paget disease, osteomalacia, rickets, renal osteodystrophy, osteitis fibrosa and hypotensive disorder.

**Drug Interactions** (8 records found; the first six are drug-drug interactions, the last two are receptor target records):
- **Moderate:** topical calcitriol, topical calcipotriol, digoxin, digitoxin
- **Minor:** hydrochlorothiazide, furosemide
- Target records (not interactions): PTH1 receptor and PTH2 receptor

**Literature-reported cautions:**
- Osteoporosis treatments have been associated with atrial fibrillation, bone pain, osteonecrosis of the jaw, atypical fractures and osteosarcoma (2009 review).
- Two case reports describe worsening of calcinosis cutis in osteoporotic patients with autoimmune disease treated with teriparatide.
- For pregnancy-associated osteoporosis, safety during lactation and in any subsequent pregnancy needs careful consideration.

Official package insert warnings and contraindications were not available for this report. Please refer to the Health Canada package insert.

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction, duodenal ulcer. Pregnancy-associated osteoporosis can be treated as a **research question** (L4), and amenorrhea-related bone loss as a lower-priority research question.

**Rationale:**
- The top-ranked predictions are model outputs only. They have no trials or literature and no plausible mechanism, so they cannot support a repurposing decision.
- Pregnancy-associated osteoporosis is mechanistically consistent with teriparatide's approved bone indication and has a sizeable body of observational evidence. That evidence is not RCT-grade, so it does not meet the L1–L3 criteria.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm approved indications, warnings and contraindications. This is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Confirmation of the study designs for pregnancy-associated osteoporosis, because the supplied abstracts are truncated.
- A prospective or comparative study in pregnancy-associated osteoporosis, along with a lactation and subsequent-pregnancy safety assessment.
- Verification of the disease identity for Worth syndrome, if that prediction is pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

