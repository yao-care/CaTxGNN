---
layout: default
title: Methyl Aminolevulinate
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Methyl Aminolevulinate: From Actinic Keratosis and Non-Melanoma Skin Cancers to Acne Vulgaris

## One-Sentence Summary

Methyl aminolevulinate (MAL, marketed as Metvix) is a topical photosensitizer prodrug used in photodynamic therapy (PDT). The literature describes it as approved for actinic keratosis, basal cell carcinoma and Bowen's disease.
The TxGNN model predicts it may be effective for **acne (disease)**, supported by **5 clinical trials** (4 of them acne-focused, all completed) and **14 publications**.
This is the best-supported of the 10 predictions in the Evidence Pack. The TxGNN rank-1 prediction, hereditary hemochromatosis, has no supporting evidence and is very likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence record. The literature describes approval for actinic keratosis, basal cell carcinoma and Bowen's disease |
| Predicted New Indication | Acne (disease), TxGNN rank 3 of 10 |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 (several completed Phase 2 studies; no completed Phase 3 trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails (research use only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on the known PDT mechanism, MAL is applied to the skin and converted inside cells to protoporphyrin IX, a light-sensitive compound. Red light then activates it and produces reactive oxygen species, which damage the treated cells.

In its approved skin-cancer uses, this selectively destroys abnormal, fast-growing skin cells. In acne, MAL is taken up by the pilosebaceous units (hair follicle and oil gland). Light activation can damage the sebaceous glands and reduce *C. acnes* bacteria. This gives a direct, biologically coherent rationale for the prediction, and it is supported by several randomized Phase 2 studies.

Open questions remain on dose, incubation time, light dose, and tolerability (pain and erythema). MAL is not approved for acne.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00594425](https://clinicaltrials.gov/study/NCT00594425) | Phase 2 | Completed | 150 | MAL-PDT cream in moderate to severe facial acne. Open-label dose-escalation phase, then a randomized, vehicle-controlled dose-response phase. The most directly relevant and largest study. |
| [NCT00673933](https://clinicaltrials.gov/study/NCT00673933) | Phase 2 | Completed | 20 | Randomized, intra-individual, vehicle-controlled multicentre study of MAL-PDT versus placebo-PDT in acne vulgaris, in skin types V–VI. |
| [NCT00206895](https://clinicaltrials.gov/study/NCT00206895) | NA | Completed | 24 | Randomized, investigator-blinded study of MAL and ALA PDT in moderate to severe facial acne. Small sample. |
| [NCT01245946](https://clinicaltrials.gov/study/NCT01245946) | Phase 2 | Completed | 46 | ALA-PDT versus adapalene gel plus doxycycline in moderate acne. Uses ALA, not MAL, so it is indirect evidence for this drug. |
| [NCT02075671](https://clinicaltrials.gov/study/NCT02075671) | Phase 4 | Completed | 30 | PDT in papulopustular rosacea. Adjacent evidence only (a different disease with a shared inflammatory pilosebaceous mechanism). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18280335](https://pubmed.ncbi.nlm.nih.gov/18280335/) | 2008 | RCT | J Am Acad Dermatol | Long-pulsed dye laser alone versus laser-assisted PDT in acne vulgaris. Tests whether adding PDT to laser is superior. The abstract does not name the photosensitizer. |
| [22949035](https://pubmed.ncbi.nlm.nih.gov/22949035/) | 2013 | Cohort | Photochem Photobiol Sci | Retrospective analysis of off-label MAL-PDT for inflammatory and aesthetic indications in 20 Italian dermatology departments. Assesses effectiveness, tolerability and safety in real-life practice. |
| [32554971](https://pubmed.ncbi.nlm.nih.gov/32554971/) | 2021 | Review | Dermatology | Critical reappraisal of off-label PDT in non-neoplastic skin conditions. Results are variable and many studies are poorly designed. |
| [38243786](https://pubmed.ncbi.nlm.nih.gov/38243786/) | 2024 | Review | J Cutan Med Surg | Update on approved and emerging topical PDT indications. PDT is superior or non-inferior to other options for actinic keratoses and low-risk non-melanoma skin cancers, with a growing range of emerging uses. |
| [17598868](https://pubmed.ncbi.nlm.nih.gov/17598868/) | 2007 | Case series | Photodermatol Photoimmunol Photomed | Seven patients with chronic folliculitis in acne-prone skin were successfully treated with MAL-PDT. |
| [18284396](https://pubmed.ncbi.nlm.nih.gov/18284396/) | 2008 | Clinical study | Br J Dermatol | Pain during PDT is associated with protoporphyrin IX fluorescence and fluence rate. Relevant to tolerability. |
| [15888131](https://pubmed.ncbi.nlm.nih.gov/15888131/) | 2005 | Review | Photodermatol Photoimmunol Photomed | PDT dermatology update. It notes a therapeutic benefit in inflammatory dermatoses, including acne vulgaris. |
| [22123417](https://pubmed.ncbi.nlm.nih.gov/22123417/) | 2011 | Review | Semin Cutan Med Surg | PDT is increasingly used in neoplastic, inflammatory and infectious skin conditions. |
| [20944910](https://pubmed.ncbi.nlm.nih.gov/20944910/) | 2010 | Review | An Bras Dermatol | Overview of PDT. MAL is approved for actinic keratosis, basal cell carcinoma and Bowen's disease. |
| [28809342](https://pubmed.ncbi.nlm.nih.gov/28809342/) | 2013 | Review | Materials (Basel) | Dye sensitizers for PDT. A few have been approved for skin diseases such as acne vulgaris. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2323273 | METVIX | Not listed | Not listed in the licence record |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results for this drug.

Health Canada warnings and contraindications are not available in the Evidence Pack. Please refer to the package insert for safety information. Published PDT studies report pain during illumination as a considerable tolerability issue (PMID 18284396).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 2 studies test MAL-PDT directly in acne, including a 150-patient randomized, vehicle-controlled study, and the mechanism is biologically coherent. However, there are no Phase 3 trials, the drug is not approved for acne, and safety data are missing. This should be treated as a research question and not a treatment recommendation.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Published results of NCT00594425 and NCT00673933, to confirm efficacy and tolerability of MAL-PDT in acne
- Optimization of dose, incubation time, light dose and pain management
- Confirmation of the approved indications and dosage form for the Canadian licence (DIN 2323273)
- Detailed mechanism of action data from DrugBank

**Other predictions in the Evidence Pack (lower priority):**
- **Common wart** (99.42%, L3): MAL-PDT case series and reports only, with no controlled data.
- **Psoriasis** (99.44%, L3): a retrospective off-label series and a small nail psoriasis pilot study.
- **Seborrheic keratosis, vulvar inverted follicular keratosis, pityriasis lichenoides** (L5): prediction only, no trials or literature.
- **Hereditary hemochromatosis, Wilson disease, iron metabolism disease, drug-induced osteoporosis** (L5): no plausible mechanism, likely knowledge-graph artifacts. Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

