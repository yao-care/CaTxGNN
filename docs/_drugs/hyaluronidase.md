---
layout: default
title: Hyaluronidase
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Hyaluronidase: From Injectable Diffusion Adjuvant to Diabetic Retinopathy

## One-Sentence Summary

Hyaluronidase (DrugBank DB14740) has no recorded original approved indication in this evidence pack and is **not currently marketed in Canada** (0 DINs); it is best known as an enzyme that depolymerizes hyaluronic acid/proteoglycans and has historically been used as an injectable "spreading agent" (e.g., the ophthalmic product **Vitrase**). Among 10 TxGNN-predicted indications for this drug, **Diabetic Retinopathy** carries by far the strongest supporting evidence — **4 clinical trials (including two completed Phase 3 RCTs, n=750 and n=510)** and **20 publications** — for its use in clearing vitreous hemorrhage via pharmacologic vitreolysis. Several other top-scoring TxGNN predictions (esotropia, amenorrhea, renal tubular acidosis, acrodermatitis chronica atrophicans, non-syndromic esophageal malformation) have **zero corroborating evidence** and are flagged as likely knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (Data Gap). Historically used as an injectable diffusion/spreading adjuvant enzyme (brand: Vitrase) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this drug (flagged as a High-severity data gap, DG002). Based on the literature evidence collected in this pack, however, hyaluronidase is a naturally occurring enzyme that digests hyaluronic acid and related glycosaminoglycans (PMID 12757408). This depolymerizing activity is the basis for its ophthalmic formulation Vitrase (ovine hyaluronidase for intravitreal injection), which was specifically developed to induce **pharmacologic vitreolysis** — enzymatic liquefaction of the vitreous gel and induction of posterior vitreous detachment (PVD).

Diabetic retinopathy, particularly its proliferative and hemorrhagic complications, is mechanistically linked to an abnormal vitreoretinal interface: incomplete PVD and a persistently attached vitreous cortex are associated with progression of diabetic macular edema and proliferative diabetic retinopathy (PMID 20939804, 17245084). By enzymatically clearing vitreous hyaluronic acid, hyaluronidase can accelerate PVD and clearance of vitreous hemorrhage, reducing traction-related complications — this is a distinct, well-characterized mechanism rather than a repurposing "leap."

Notably, this is not a purely theoretical extrapolation: the branded product Vitrase was directly developed and tested for exactly this purpose, and a more granular sub-population — **severe non-proliferative diabetic retinopathy** (rank 3, L2, one completed Phase 2 open-label trial, NCT00198471) — shows a consistent, mechanistically identical signal. In contrast, several other top-ranked TxGNN predictions (esotropia, amenorrhea, renal tubular acidosis, acrodermatitis chronica atrophicans, non-syndromic esophageal malformation) show **no plausible mechanistic link and no evidence at all**, and are best explained as co-occurrence artifacts in the knowledge graph (e.g., hyaluronidase's frequent use as an anesthetic-adjuvant in ophthalmic surgery, which may create spurious associations with unrelated ophthalmic/endocrine/structural conditions).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Pivotal trial testing intravitreal Vitrase (ovine hyaluronidase) for clearance of severe vitreous hemorrhage; largest and highest-quality trial in this evidence set |
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Companion pivotal trial replicating NCT00198510, confirming efficacy/safety of intravitreal Vitrase for vitreous hemorrhage clearance |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label study assessing Vitrase to induce posterior vitreous detachment specifically in moderate-to-severe non-proliferative diabetic retinopathy |
| [NCT04311606](https://clinicaltrials.gov/study/NCT04311606) | Phase 2 | Completed | 11 | Sub-tenon aflibercept ± hyaluronidase in acute thyroid eye disease — **low relevance**, likely a keyword-match artifact rather than a diabetic retinopathy study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Current Pharmaceutical Biotechnology | Reviews pharmacologic vitreolysis in diabetic retinopathy; confirms intravitreal ovine hyaluronidase effectively clears vitreous hemorrhage |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug profile | Drugs in R&D | Describes development of Vitrase (ovine hyaluronidase) specifically for vitreous hemorrhage and diabetic retinopathy |
| [19199900](https://pubmed.ncbi.nlm.nih.gov/19199900/) | 2009 | Review | Current Diabetes Reviews | Reviews enzymatic vitreolysis and the vitreoretinal interface's role in proliferative diabetic retinopathy and macular edema |
| [17245084](https://pubmed.ncbi.nlm.nih.gov/17245084/) | 2007 | Review | Developments in Ophthalmology | Reviews pharmacologic approaches (including hyaluronidase) to induce posterior vitreous detachment in diabetic retinal disease |
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Mechanistic study | Frontiers in Immunology | Shows dysregulated hyaluronan metabolism (including hyaluronidase pathway enzymes) drives inflammation and angiogenesis in proliferative diabetic retinopathy |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Mechanistic study | Investigative Ophthalmology & Visual Science | Enzyme-induced vitreolysis alleviates progression of diabetic retinopathy via the HIF-1α pathway |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Animal study | Retina | Pharmacologic vitreolysis with plasmin and hyaluronidase induces PVD in diabetic rats |
| [19349793](https://pubmed.ncbi.nlm.nih.gov/19349793/) | 2009 | Review | International Ophthalmology Clinics | Reviews pharmacologic vitreodynamics, including enzymatic approaches relevant to diabetic retinopathy |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Experimental Diabetes Research | Broader review of pharmacotherapies for diabetic retinopathy, situating enzymatic vitreolysis among treatment options |
| [19668479](https://pubmed.ncbi.nlm.nih.gov/19668479/) | 2007 | Review | Clinical Ophthalmology | General review of diabetic retinopathy management and emerging therapies |

---

## Canada Market Information

Hyaluronidase currently has **no active drug licenses on file in Canada** (0 DINs; market status: Not Marketed). No products are available to summarize in this section.

---

## Other TxGNN-Predicted Indications (Overview)

For transparency, this evidence pack scored hyaluronidase against 10 candidate indications. Diabetic retinopathy (above) is the only one with strong, direct supporting evidence. The others are summarized below:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Esotropia | 99.89% | L5 | Hold | No trials/literature; likely surgical-adjuvant co-occurrence artifact |
| 2 | Amenorrhea | 99.83% | L5 | Hold | No mechanistic link, no evidence |
| 3 | Severe NPDR | 99.79% | L2 | Research Question | One completed Phase 2 open-label trial (n=10); subgroup of the diabetic retinopathy signal above |
| 4 | Renal tubular acidosis | 99.76% | L5 | Hold | No mechanistic link, no evidence |
| 5 | Dermatitis | 99.73% | L3 | Hold | Evidence is contradictory/safety-signal in nature (hyaluronidase-associated hypersensitivity dermatitis), not a treatment signal |
| 7 | Acrodermatitis chronica atrophicans | 99.58% | L5 | Hold | No mechanistic link, no evidence |
| 8 | Diabetic cataract | 99.55% | L4 | Hold | Literature reflects hyaluronidase's role as a surgical/anesthetic adjuvant, not disease-modifying treatment |
| 9 | Neonatal dermatomyositis | 99.51% | L4 | Hold | Sole reference is an unrelated 1972 methodology paper |
| 10 | Non-syndromic esophageal malformation | 99.51% | L5 | Hold | No mechanistic link, no evidence |

---

## Safety Considerations

Please refer to the package insert for safety information — no structured warnings, contraindications, or drug-drug interaction data are currently available for this evidence pack (flagged as Blocking data gap DG001: TFDA-equivalent label warnings/contraindications not yet retrieved).

**Additional advisory note (from literature, not structured safety data):** evidence collected under the dermatitis-indication search flagged hyaluronidase-associated allergic and hypersensitivity reactions, including a 2024 review of allergic complications from hyaluronidase injection ([PMID 37145319](https://pubmed.ncbi.nlm.nih.gov/37145319/)). This should be factored into future safety assessment even though it does not appear in the structured DDI/warning fields.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Diabetic Retinopathy specifically; all other predicted indications in this bundle should remain **Hold**)

**Rationale:**
Two completed Phase 3 RCTs (n=750 and n=510) plus multiple supportive mechanistic reviews establish a credible, already-productized use case (Vitrase) for intravitreal hyaluronidase in clearing diabetic retinopathy-related vitreous hemorrhage. However, the drug is not currently marketed in Canada and lacks structured safety labeling data, which are blocking issues that must be resolved before any regulatory or clinical advancement.

**To proceed, the following is needed:**
- Official product label / TFDA-equivalent warnings and contraindications (Blocking data gap DG001) — currently prevents S1 safety screening
- Confirmed structured mechanism-of-action data from DrugBank (High-severity data gap DG002)
- Clarification of the regulatory pathway for a drug with 0 Canadian DINs (e.g., Special Access Programme vs. new DIN submission) before any clinical use can be considered
- A dedicated evidence review (or Phase 3 trial) specifically for the severe NPDR subgroup (rank 3) to consolidate the diabetic retinopathy body of evidence
- No further action on the remaining Hold-status indications (esotropia, amenorrhea, renal tubular acidosis, dermatitis, acrodermatitis chronica atrophicans, diabetic cataract, neonatal dermatomyositis, non-syndromic esophageal malformation) unless new clinical or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

