---
layout: default
title: Methyl Aminolevulinate
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Methyl Aminolevulinate: predicted new indication Hereditary hemochromatosis (evidence level L5). Approved use: Not stated in the Canadian license data. Published reviews describe a…"
monitor_inn: "METHYL AMINOLEVULINATE"
predicted_indications: ["hereditary hemochromatosis", "seborrheic keratosis", "acne (disease)", "vulvar inverted follicular keratosis", "psoriasis", "common wart", "drug-induced osteoporosis", "pityriasis lichenoides", "Wilson disease", "iron metabolism disease"]
---

# Methyl Aminolevulinate
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

## Methyl Aminolevulinate: From Its Marketed Photodynamic Use to Hereditary Hemochromatosis (Top TxGNN Prediction) and Acne (Best-Supported Candidate)
{: .text-alpha }

## One-Sentence Summary

Methyl aminolevulinate (MAL) is a topical photosensitizer precursor that is marketed in Canada as Metvix, and the literature compiled for this report describes its approved dermatology use in photodynamic therapy (PDT).
The TxGNN model's top-ranked prediction is **hereditary hemochromatosis**, but it has **no clinical trials and no publications** behind it. The best-supported candidate among the top 10 predictions is **acne**, with **2 completed Phase 2 trials** and **8 publications**.
The primary prediction is therefore a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data. Published reviews describe approved use for actinic keratosis, basal cell carcinoma and Bowen's disease. |
| Predicted New Indication | Hereditary hemochromatosis (rank 1); acne is the best-supported candidate (rank 3) |
| TxGNN Prediction Score | 0.9986 (hereditary hemochromatosis); 0.9981 (acne) |
| Evidence Level | L5 (hereditary hemochromatosis); L2 (acne) |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold (hereditary hemochromatosis); Hold for the top prediction, with acne as a research question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, MAL is a precursor that cells convert to protoporphyrin IX. When illuminated with red light, protoporphyrin IX generates reactive oxygen species that destroy targeted tissue. This is the basis of topical PDT.

**Hereditary hemochromatosis (rank 1).** MAL sits in the heme biosynthesis pathway, which may explain why the model links it to iron metabolism. However, hemochromatosis is a systemic iron overload disorder, while MAL is used topically with light activation. No evidence was found to connect the two, so this prediction should be treated as speculative. The same applies to the other metabolic predictions (Wilson disease, iron metabolism disease, drug-induced osteoporosis).

**Acne (rank 3).** Here the mechanism is credible. MAL is taken up by pilosebaceous units, converted to protoporphyrin IX, and activated by red light. This can damage sebaceous glands and reduce *C. acnes*. Reviews also note PDT benefit in acne vulgaris and other inflammatory skin diseases.

**Other skin conditions.** Seborrheic keratosis, common wart, psoriasis, pityriasis lichenoides and vulvar inverted follicular keratosis are all hyperproliferative or inflammatory skin conditions where PDT is mechanistically conceivable. Only common wart and psoriasis have any literature, and it is mostly indirect.

---

## Clinical Trial Evidence

Trials for the top-ranked prediction (hereditary hemochromatosis): currently no related clinical trials registered.

Trials for acne (the best-supported candidate):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00594425](https://clinicaltrials.gov/study/NCT00594425) | Phase 2 | Completed | 150 | MAL-PDT cream in moderate to severe facial acne. Two-part design: open-label dose escalation, then blinded, randomized, vehicle-controlled dose-response. Results were not supplied. |
| [NCT00673933](https://clinicaltrials.gov/study/NCT00673933) | Phase 2 | Completed | 20 | Blinded, randomized, intra-individual, vehicle-controlled study of MAL-PDT in acne vulgaris in patients with skin type V or VI. Results were not supplied. |

No registered clinical trials were provided for the other predicted indications.

---

## Literature Evidence

Literature for the top-ranked prediction (hereditary hemochromatosis): currently no related literature available.

Literature for acne (up to 10 most relevant):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22949035](https://pubmed.ncbi.nlm.nih.gov/22949035/) | 2013 | Retrospective cohort | Photochem Photobiol Sci | Real-life off-label MAL-PDT in 20 Italian dermatology departments for inflammatory and aesthetic indications, assessing effectiveness, tolerability and safety |
| [17598868](https://pubmed.ncbi.nlm.nih.gov/17598868/) | 2007 | Case series | Photodermatol Photoimmunol Photomed | Seven patients with chronic folliculitis in acne-prone skin, successfully treated with MAL-PDT |
| [38243786](https://pubmed.ncbi.nlm.nih.gov/38243786/) | 2024 | Review | J Cutan Med Surg | Update on approved and emerging topical PDT indications. PDT is superior or noninferior to other treatments for several conditions. |
| [15888131](https://pubmed.ncbi.nlm.nih.gov/15888131/) | 2005 | Review | Photodermatol Photoimmunol Photomed | Topical PDT is established for actinic keratosis, Bowen's disease and basal cell carcinoma, with evident benefit in acne vulgaris and other inflammatory dermatoses |
| [28809342](https://pubmed.ncbi.nlm.nih.gov/28809342/) | 2013 | Review | Materials (Basel) | Dye sensitizers for PDT, including approved use in skin diseases such as acne vulgaris |
| [20944910](https://pubmed.ncbi.nlm.nih.gov/20944910/) | 2010 | Review | An Bras Dermatol | PDT review. MAL is approved for actinic keratosis, basal cell carcinoma and Bowen's disease. |
| [23986167](https://pubmed.ncbi.nlm.nih.gov/23986167/) | 2013 | Review | J Drugs Dermatol | MAL/PDT has efficacy similar to ALA/PDT in actinic keratosis, SCC and Bowen's disease, with shorter incubation time |
| [16566733](https://pubmed.ncbi.nlm.nih.gov/16566733/) | 2006 | Review | J Environ Pathol Toxicol Oncol | PDT in in situ neoplasias and skin tumours, with MAL postulated as highly selective and efficacious |

Several of these are general PDT reviews rather than acne-specific studies.

Other predicted indications with literature (indirect evidence only):
- **Common wart (Level L3):** a retrospective off-label analysis ([22949076](https://pubmed.ncbi.nlm.nih.gov/22949076/)), case series of recalcitrant warts ([31209587](https://pubmed.ncbi.nlm.nih.gov/31209587/), 51 patients; [37707554](https://pubmed.ncbi.nlm.nih.gov/37707554/)), and case reports ([19614904](https://pubmed.ncbi.nlm.nih.gov/19614904/)). Some retrieved articles use ALA rather than MAL or address other conditions, which weakens relevance.
- **Psoriasis (Level L4):** only general PDT reviews, a retrospective off-label analysis and a mycosis fungoides case report. None is a psoriasis-specific trial.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02323273 | METVIX | Not specified | Not specified in the license data |

---

## Safety Considerations

- **TxGNN model contraindication signals (deep learning):** the TxGNN model links methyl aminolevulinate to *photoparoxysmal response* and *photosensitivity disease*. These signals come from the TxGNN model (deep learning), not from label text, and may reflect similarities the model learned between related diseases, not biological evidence. They are consistent with its photosensitizing action.
- **Drug interactions:** no interaction records were found.

Please refer to the package insert for full warnings and contraindications. The label text could not be obtained for this report.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, hereditary hemochromatosis). Acne is flagged as a **research question** rather than a Go decision.

**Rationale:**
- The top prediction, hereditary hemochromatosis, rests only on a model score of 0.9986, with no trials or literature, and no evident link between a topical photosensitizer and systemic iron overload.
- Acne has a credible mechanism and two completed Phase 2 trials (n=150 and n=20), but no results, no Phase 3 evidence and mostly review-level literature, so the size and direction of benefit cannot be confirmed.

**To proceed, the following is needed:**
- Results from NCT00594425 and NCT00673933 (efficacy, dose-response, tolerability)
- A Phase 3 or otherwise confirmatory study in acne
- The Health Canada package insert (warnings and contraindications), the approved indications for Metvix, and its dosage form
- Mechanism of action data, such as from DrugBank
- A route-compatibility assessment (currently pending) to confirm topical plus light delivery fits the new indication
- For common wart, MAL-specific controlled studies, since much of the existing evidence is ALA-based or case-level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

