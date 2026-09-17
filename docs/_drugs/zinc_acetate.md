---
layout: default
title: Zinc Acetate
parent: Model Prediction Only (L5)
nav_order: 838
evidence_level: L5
indication_count: 10
---

# Zinc Acetate
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

# Zinc Acetate: From Unspecified Original Indication to Severe Nonproliferative Diabetic Retinopathy (and 9 Additional Candidates)

## One-Sentence Summary

Zinc Acetate (DrugBank DB14487) has no original indication or mechanism-of-action data recorded in this Evidence Pack, and it is not currently marketed in Canada. The TxGNN model surfaces **10 candidate indications**, topped by **Severe Nonproliferative Diabetic Retinopathy** (score 99.97%), but only two candidates — **bronchitis** and **urinary tract infection** — have any supporting clinical trial or literature evidence, and even that evidence is indirect. Nine of the ten candidates are pure model predictions (L5) with no clinical or literature support at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack (data gap) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy (top-ranked of 10 candidates) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (no clinical trials or literature for this indication) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

### All Predicted Indications at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|:-----------:|:---------------:|:---------------:|:----------------|
| 1 | Severe nonproliferative diabetic retinopathy | 99.97% | L5 | S0 | Hold |
| 2 | Bronchitis | 99.97% | L4 | S1 | Research Question |
| 3 | Diabetic retinopathy | 99.92% | L5 | S0 | Hold |
| 4 | Acrodermatitis chronica atrophicans | 99.83% | L5 | S0 | Hold |
| 5 | Neonatal dermatomyositis | 99.81% | L5 | S0 | Hold |
| 6 | Acne keloidalis | 99.80% | L5 | S0 | Hold |
| 7 | Hydroa vacciniforme, familial | 99.79% | L5 | S0 | Hold |
| 8 | Childhood interstitial lung disease (connective tissue disease-associated) | 99.78% | L5 | S0 | Hold |
| 9 | Amyopathic dermatomyositis | 99.77% | L5 | S0 | Hold |
| 10 | Urinary tract infection | 99.57% | L4 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for zinc acetate is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). No original indication is recorded either, so a direct comparison between an established use and the predicted new indications cannot be made.

That said, the model's own rationale fields point to well-known general biological properties of zinc ions that plausibly connect to several of the candidates:
- **Antioxidant cofactor role** — zinc is a cofactor for Cu/Zn-superoxide dismutase (SOD), which underlies the rationale for both diabetic retinopathy candidates (ranks 1 and 3), though this is theoretical and unsupported by any trial or publication.
- **Antiviral / immune-modulatory activity** — zinc ions are known to inhibit rhinovirus replication and support immune function, which is the basis for the bronchitis candidate (rank 2); this has direct clinical evidence in the *common cold* (a related but distinct condition) but no direct evidence in bronchitis itself.
- **Antimicrobial / immune-support activity** — cited as the rationale for the urinary tract infection candidate (rank 10), but the supporting literature is drawn from a sickle-cell-disease infection-rate study, not a UTI-specific study.
- **Dermatologic precedent** — zinc has established use in acne vulgaris, which is used to rationalize the acne keloidalis candidate (rank 6), but no trial or literature evidence exists for this specific condition.

The remaining candidates (acrodermatitis chronica atrophicans, neonatal/amyopathic dermatomyositis, familial hydroa vacciniforme, childhood connective-tissue-disease-associated interstitial lung disease) are, per the model's own notes, weakly justified — the mechanistic links are generic "antioxidant/anti-inflammatory/immune-modulatory" statements without disease-specific rationale, and the high TxGNN scores may reflect non-specific graph proximity between zinc and dermatology/immunology nodes rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Only one candidate indication (bronchitis) has an associated clinical trial. No trials were found for any other predicted indication, including the top-ranked severe nonproliferative diabetic retinopathy.

| Predicted Indication | Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---------|------|------|------|---------|
| Bronchitis | [NCT03309995](https://clinicaltrials.gov/study/NCT03309995) | NA | Completed | 87 | Randomized, double-blind trial of zinc acetate lozenges (13 mg elemental zinc) for recovery from the **common cold**, not bronchitis specifically. Relevance graded "B" — disease overlap (viral upper/lower respiratory illness) but not the same indication. |

For the remaining 9 candidate indications: **Currently no related clinical trials registered.**

---

## Literature Evidence

Literature was only identified for two candidate indications (bronchitis and urinary tract infection); all are indirect (tier 3) evidence.

| Predicted Indication | PMID | Year | Type | Journal | Key Findings |
|---|------|-----|------|------|---------|
| Bronchitis | [10398312](https://pubmed.ncbi.nlm.nih.gov/10398312/)* | — | — | — | See UTI row below (same study) |
| Urinary tract infection | [10398312](https://pubmed.ncbi.nlm.nih.gov/10398312/) | 1999 | Cohort/RCT | American Journal of Hematology | Zinc supplementation in sickle cell disease patients was associated with reduced overall infection rate and hospital admissions. Not UTI-specific; indirect evidence only. |
| Bronchitis | [32679246](https://pubmed.ncbi.nlm.nih.gov/32679246/) | 2020 | Other (nanoparticle materials science) | Microbial Pathogenesis | Compared biogenic vs. wet-chemical synthesis of ZnO nanoparticles against *S. aureus* in animal models; bronchitis mentioned only as a disease effect of the infection model, not as a treatment outcome. |
| Bronchitis | [23782414](https://pubmed.ncbi.nlm.nih.gov/23782414/) | 2014 | Animal study | Journal of Animal Physiology and Animal Nutrition | Zinc-induced moulting and immune response study in broiler breeders; not relevant to human bronchitis. |

*(Row duplicated for clarity since the study is cross-tagged to both bronchitis and UTI evidence sets in the source data; it does not directly address either condition.)*

For the remaining 8 candidate indications: **Currently no related literature available.**

---

## Canada Market Information

Zinc acetate (DB14487) is currently **not marketed** in Canada — there are no Health Canada authorizations (DINs) on record for this product in the Evidence Pack (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

- No product label warnings, contraindications, or drug-interaction data are available in this Evidence Pack (all fields are marked as data gaps or "not found").
- **Note:** the absence of Health Canada/TFDA label warnings and contraindications (DG001) is flagged as a **Blocking** data gap in this Evidence Pack — it prevents any formal Stage 1 (S1) safety assessment for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (severe nonproliferative diabetic retinopathy) has zero supporting clinical trials or literature (L5, pure model prediction), and the drug is not currently marketed in Canada.
- The only two candidates with any supporting evidence (bronchitis, urinary tract infection) rely on indirect studies (common cold, sickle-cell-disease infection rates) rather than disease-specific data, and remain at L4/Research-Question status at best.
- A Blocking data gap (missing label warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Health Canada / regulatory product label data (warnings, contraindications, drug interactions) to resolve the Blocking data gap (DG001).
- DrugBank mechanism-of-action data to substantiate or refute the mechanistic rationales offered for each candidate (DG002).
- Disease-specific clinical evidence for bronchitis and urinary tract infection before elevating either candidate beyond "Research Question" status.
- If pursuing the top-ranked diabetic retinopathy candidates, dedicated preclinical or clinical studies are needed, as no evidence currently exists beyond graph-based model inference.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

