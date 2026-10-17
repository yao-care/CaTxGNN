---
layout: default
title: Bimatoprost
parent: Model Prediction Only (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bimatoprost: predicted new indication Malformation syndrome with odontal and/or periodontal component (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "BIMATOPROST"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "genetic alopecia", "pulmonary arteriovenous malformation (disease)"]
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma and Ocular Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a prostamide (prostaglandin F2-alpha analog) originally used to lower eye pressure in open-angle glaucoma and ocular hypertension, and to grow eyelashes in eyelash hypotrichosis.
The TxGNN model's top-ranked prediction is **malformation syndrome with odontal and/or periodontal component**, but this is a graph-based signal only, with **0 clinical trials** and **0 publications** supporting it.
A different prediction in the same list, **alopecia**, has far stronger support (see "Better-Supported Candidate" below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension; eyelash hypotrichosis |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, bimatoprost is a prostamide/prostaglandin F2-alpha analog. It lowers intraocular pressure and also prolongs the hair-growth (anagen) phase.

For this specific prediction, no mechanistic link could be identified. A developmental malformation syndrome involving the teeth and periodontium has no recognizable connection to prostamide pharmacology. The high score reflects a pattern in the knowledge graph rather than biological or clinical reasoning, so this prediction should be treated as a computational artifact until independent evidence appears.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Better-Supported Candidate: Alopecia (Rank 8)

Among the ten predicted indications, **alopecia** (TxGNN score 99.993%) is the only one with substantial trial evidence. It has an evidence level of L2, and its mechanism is coherent. Bimatoprost extends anagen via prostanoid receptor signalling, and eyelash hypotrichosis is already an approved use.

**Key clinical trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Three doses of bimatoprost vs vehicle and OTC minoxidil 5% in men with androgenetic alopecia |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Three doses of bimatoprost vs vehicle and OTC minoxidil 2% in women with female pattern hair loss |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy in men with androgenetic alopecia |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Effect of topical bimatoprost on scalp hair growth and androgen-dependent follicles |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Safety and efficacy for eyelash hypotrichosis in children |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | Bimatoprost 0.03% plus CO2 fractional laser in alopecia areata (combination design confounds the bimatoprost effect) |

**Selected literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Bimatoprost for eyelash, eyebrow and scalp alopecia |
| [38794131](https://pubmed.ncbi.nlm.nih.gov/38794131/) | 2024 | Review | Pharmaceuticals (Basel) | Overview of bimatoprost from ocular use to hair growth |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective study | Dermatol Ther | Open-label study of bimatoprost for eyelash loss in alopecia totalis/universalis |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Non-randomized trial | Indian Dermatol Online J | Bimatoprost vs clobetasol propionate in scalp alopecia areata |

**Caveat:** Scalp efficacy has not been confirmed in a Phase 3 trial, and the evidence is stronger for eyelashes and eyebrows than for scalp.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02429063 | VISTITAN |
| 02350939 | LATISSE |
| 02324997 | LUMIGAN RC |
| 02533464 | ZIMED PF |

All four are valid single-ingredient authorizations. Dosage form and approved-indication text were not available in the compiled data.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (graph-derived associations, not label text): liver disease, gallbladder disease, uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis.
- **Drug Interactions:** 66 potential interactions were identified, all with an unclassified severity level. Examples include calcitriol, phentermine, pantoprazole, morphine, metformin, omeprazole, simvastatin, prednisone, and ondansetron. Clinical significance needs to be confirmed against an authoritative interaction source.

Official warnings and contraindications from the Health Canada package insert were not retrieved. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature, and no plausible mechanism, so it is a model artifact and not a repurposing opportunity. The lower-ranked **alopecia** prediction is the one worth pursuing. It has several completed Phase 2 trials, but it has no Phase 3 confirmation yet.

**To proceed, the following is needed:**
- Re-prioritize the candidate list so that alopecia (androgenetic alopecia and female pattern hair loss) is evaluated as the lead indication, with a separate decision of "Proceed with Guardrails".
- Mechanism of action data to be added to the compiled record.
- Package insert warnings and contraindications from Health Canada.
- Efficacy results from the Phase 2 androgenetic alopecia trials, and a Phase 3 plan for scalp use.
- A topical scalp formulation and route assessment, since the approved Canadian products are ophthalmic or eyelash products.
- Review of the 66 potential drug interactions with severity classification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

