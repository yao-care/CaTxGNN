---
layout: default
title: Lifitegrast
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 6
---

# Lifitegrast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lifitegrast: From Dry Eye Disease to Diabetic Retinopathy

## One-Sentence Summary

Lifitegrast (DrugBank DB11611, developed as SAR 1118) is an LFA-1 antagonist originally developed for **dry eye disease**. The TxGNN model's highest-ranked candidates (penile/palmar fibromatosis, Ledderhose disease, infantile digital fibromatosis) all score above 99.5% but have **zero supporting clinical or literature evidence** and are recommended Hold. The one candidate with actual supporting evidence is **Diabetic Retinopathy** (score 99.03%), backed by **1 completed Phase 1/2 trial** and **2 publications**, though none were designed specifically to test DR efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry Eye Disease (per mechanistic rationale; no Canadian license record exists) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 (observational/non-confirmatory clinical + literature data) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question — hypothesis-generating stage) |

*Note: Five other TxGNN candidates for this drug — penile fibromatosis, palmar fibromatosis, Ledderhose disease, infantile digital fibromatosis, and severe nonproliferative diabetic retinopathy — scored higher (99.2–99.6%) but returned no clinical trials or literature on targeted search. These are model-only predictions (L5) with independent "Hold" recommendations and are not further evaluated below.*

---

## Why is This Prediction Reasonable?

Lifitegrast is a lymphocyte function-associated antigen-1 (LFA-1) antagonist. It blocks LFA-1/ICAM-1–mediated T-cell adhesion, the inflammatory pathway implicated in ocular surface inflammation in dry eye disease. Detailed structured MOA data was not available in this evidence pack, but this mechanism is described consistently across the supporting literature (see PMID 22538219 below).

Diabetic retinopathy shares a related vascular-inflammatory mechanism: chronic hyperglycemia upregulates ICAM-1 on retinal vascular endothelium, promoting leukocyte adhesion via LFA-1/ICAM-1 ("leukostasis"), which contributes to microvascular occlusion and leakage — a recognized driver of DR progression. This gives the TxGNN prediction plausible mechanistic grounding, distinct from the fibromatosis-type predictions above, which have no known connection to LFA-1 biology.

However, the existing evidence was generated in dry-eye-disease and diabetic-macular-edema development programs, not in trials designed with DR-specific endpoints. The mechanistic link is therefore reasonable but unconfirmed in the target indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04030962](https://clinicaltrials.gov/study/NCT04030962) | Phase 1/2 | Completed | 292 | Vehicle-controlled, double-masked, randomized study of AGN-242428/AGN-231868 assessing safety, tolerability, pharmacokinetics, and exploratory efficacy in dry eye disease (DED); tagged to diabetic retinopathy in the source database but not designed with DR-specific endpoints (relevance grade: B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22538219](https://pubmed.ncbi.nlm.nih.gov/22538219/) | 2012 | Phase 1 (Safety/Tolerability/PK) | Eye (London, England) | Phase 1b study of topical SAR 1118 (lifitegrast), a novel LFA-1 antagonist; establishes LFA-1/ICAM-1-mediated inflammation as a mechanism in diabetic macular oedema pathogenesis and confirms safety/tolerability/PK of topical administration. |
| [41158172](https://pubmed.ncbi.nlm.nih.gov/41158172/) | 2025 | Genetic/Proteomic (Mendelian randomization) | International Journal of Ophthalmology | Proteome-wide Mendelian randomization integrating plasma proteomics and GWAS data to identify novel protein/drug targets for retinal neurodegenerative diseases in Europeans. |

---

## Canada Market Information

Lifitegrast is **not currently marketed in Canada** — no Drug Identification Number (DIN) has been issued (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between LFA-1/ICAM-1-mediated leukostasis and diabetic retinopathy is biologically plausible, but the only supporting clinical trial and literature evidence originate from dry-eye-disease and diabetic-macular-edema safety studies rather than DR-specific efficacy trials — this is a hypothesis-generating signal (L3/S1), not confirmatory evidence.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (flagged as a **Blocking** data gap — required before any S1 safety screening can complete)
- Structured mechanism-of-action data from DrugBank (flagged as a **High**-severity data gap)
- A DR-specific clinical trial (efficacy endpoints in retinopathy progression, not DED/DME safety endpoints)
- Drug-drug interaction data (current DDI query returned no results)
- Re-evaluation of the five higher-scoring fibromatosis-type predictions only if independent mechanistic or clinical evidence emerges — none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

