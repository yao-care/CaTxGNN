---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 935
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Travoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "idiopathic spontaneous coronary artery dissection", "lymphangiectasis", "hemangioendothelioma"]
---

# Travoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Travoprost is a prostaglandin F2-alpha analog originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** directly supporting this indication.
The top-ranked prediction therefore sits at the lowest evidence level (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.99985% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, travoprost is a prostaglandin F2-alpha analog applied to the eye. It lowers intraocular pressure in glaucoma and ocular hypertension, and its efficacy in those conditions is well established.

For visceral calciphylaxis, no trials or publications connect travoprost to the disease. Any link would be speculative, for example prostaglandin receptor-mediated vasodilation or microvascular effects, and the data do not support it. The prediction score is very high (close to 1.0), but several other top-ranked predictions are also implausible. These include thoracic outlet syndromes, which are mechanical compression disorders. This suggests the score reflects knowledge-graph patterns and not a verified pharmacological rationale.

The other nine top predictions are all vascular or related conditions, and none has clinical support. "Vascular disease" (rank 5) is the only one with retrieved studies, and those studies cover travoprost in glaucoma, not vascular disease. The single trial with a vascular readout (NCT00308945) measured retinal and choroidal blood flow in the eye. It did not treat a vascular disease.

## Clinical Trial Evidence

Currently no related clinical trials are registered for visceral calciphylaxis.

For context, the broader "vascular disease" prediction (rank 5) retrieved the trials below. They concern travoprost in its original eye indication, not a new indication. Only the first one has a vascular physiology readout.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | Completed | 20 | Travoprost vs latanoprost effects on retinal vascular diameter and choroidal blood flow in glaucoma patients |
| [NCT02136589](https://clinicaltrials.gov/study/NCT02136589) | Phase 4 | Completed | 40 | NSAID pretreatment and travoprost-induced conjunctival hyperemia and IOP reduction |
| [NCT02140060](https://clinicaltrials.gov/study/NCT02140060) | Phase 2 | Completed | 327 | Travoprost/brinzolamide fixed combination vs its components for IOP lowering |
| [NCT00293800](https://clinicaltrials.gov/study/NCT00293800) | Phase 3 | Completed | 173 | Glaucoma therapy in open-angle glaucoma or ocular hypertension |
| [NCT00293761](https://clinicaltrials.gov/study/NCT00293761) | Phase 3 | Completed | 109 | Glaucoma therapy safety and efficacy |
| [NCT00293787](https://clinicaltrials.gov/study/NCT00293787) | Phase 3 | Completed | 156 | Glaucoma therapy safety and efficacy |
| [NCT00760539](https://clinicaltrials.gov/study/NCT00760539) | Phase 3 | Completed | 87 | Travoprost/timolol BAC-free vs standard combination |
| [NCT00672997](https://clinicaltrials.gov/study/NCT00672997) | Phase 3 | Completed | 301 | Travoprost/timolol BAC-free vs standard combination |
| [NCT01510145](https://clinicaltrials.gov/study/NCT01510145) | Phase 4 | Completed | 191 | BAK-free travoprost tolerability after switching from latanoprost |
| [NCT00047554](https://clinicaltrials.gov/study/NCT00047554) | N/A | Terminated | 336 | Five-year safety study of iris pigmentation changes with Travatan |

## Literature Evidence

No literature is available for visceral calciphylaxis. The most relevant items retrieved for related predictions are listed below. None tests travoprost as a treatment for a vascular disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22167538](https://pubmed.ncbi.nlm.nih.gov/22167538/) | 2012 | Meta-analysis | Eur J Ophthalmol | IOP-lowering and tolerability of prostaglandin-timolol fixed combinations |
| [23231442](https://pubmed.ncbi.nlm.nih.gov/23231442/) | 2013 | Meta-analysis | J Ocul Pharmacol Ther | Prostaglandin analogs with timolol, fixed vs unfixed combinations, in open-angle glaucoma |
| [31335731](https://pubmed.ncbi.nlm.nih.gov/31335731/) | 2019 | Review | Medicine | Protocol for evaluating travoprost efficacy in glaucoma |
| [25867658](https://pubmed.ncbi.nlm.nih.gov/25867658/) | 2015 | Systematic Review | Curr Med Res Opin | Updated review of prostaglandin-timolol fixed combinations |
| [19019922](https://pubmed.ncbi.nlm.nih.gov/19019922/) | 2009 | Systematic Review | Br J Ophthalmol | Conjunctival hyperaemia with latanoprost vs travoprost and bimatoprost |
| [12648301](https://pubmed.ncbi.nlm.nih.gov/12648301/) | 2003 | Review | J Ocul Pharmacol Ther | Hyperemia occurs in up to 50% of patients treated with travoprost |
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Case report | J Fr Ophtalmol | Uveal effusion with retinal detachment induced by topical travoprost in a patient with Sturge-Weber-Krabbe syndrome (a safety signal) |
| [26847553](https://pubmed.ncbi.nlm.nih.gov/26847553/) | 2016 | Cohort | Jpn J Ophthalmol | Quantified conjunctival injection with glaucoma eye drops |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02457997 | IZBA | Not specified | Not specified |
| 02318008 | TRAVATAN Z | Not specified | Not specified |
| 02548089 | JAMP TRAVOPROST Z | Not specified | Not specified |
| 02413167 | SANDOZ TRAVOPROST | Not specified | Not specified |
| 02415305 | APO-TRAVOPROST-TIMOP PQ | Not specified | Not specified |

A sixth authorization, DUOTRAV PQ (DIN 02278251), is also valid. All six are valid single-ingredient authorizations, and none is cancelled.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: uveitis, iris disease, ciliary body disease, panuveitis, iritis, cystoid macular edema, and macular retinal edema. These are drug-disease contraindication edges and should be confirmed against the package insert.
- **Drug Interactions**: 49 potential interactions were identified, all with an unknown severity level. Examples include prednisone, prednisolone, triamcinolone, acetylsalicylic acid, metformin, simvastatin, and omeprazole. Their clinical significance has not been classified.
- **Case report signal**: topical travoprost was linked to uveal effusion with retinal detachment in a patient with a vascular malformation syndrome (PMID 19107053).
- **Common ocular effect**: conjunctival hyperemia, reported in up to about 50% of treated patients in a published review.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for visceral calciphylaxis rests on the model score alone. No trials or publications support it, and no plausible mechanism links an ocular prostaglandin analog to the disease. The same is true of all ten top predictions, none of which is above L5 except hemangioendothelioma at L4. That L4 item is only an adverse-event case report and argues against use.

**To proceed, the following is needed:**
- Mechanism of action data for travoprost, and a mechanistic analysis of any link to calcific vascular disease
- Preclinical evidence (for example, in vitro or animal models of vascular calcification)
- Package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Assessment of route compatibility, since travoprost is an ophthalmic product and the predicted condition is systemic
- Classification of the 49 drug interactions, which currently have unknown severity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

