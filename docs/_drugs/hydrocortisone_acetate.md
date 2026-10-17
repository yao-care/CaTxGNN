---
layout: default
title: Hydrocortisone Acetate
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydrocortisone Acetate: predicted new indication Alopecia areata (evidence level L5). Approved use: Autoimmune disease"
monitor_inn: "HYDROCORTISONE ACETATE"
predicted_indications: ["alopecia areata", "telogen effluvium", "alopecia mucinosa", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "seborrheic keratosis"]
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate: From Autoimmune and Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate is a corticosteroid originally used for autoimmune disease, adrenocortical insufficiency, inflammatory bowel disease and several other conditions.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **1 clinical trial** (a Phase 3 trial in which hydrocortisone was the comparator) and **2 older publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune disease (Canadian licence texts contain no indication wording; original indications also include adrenocortical insufficiency, Crohn disease and inflammatory bowel disease) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 by the rules in this report's framework (no completed Phase 3 trial tested hydrocortisone as the investigational agent; the single Phase 3 trial used it as a comparator). The source data label L1, which is not supported by the trial details. |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone acetate is a corticosteroid with anti-inflammatory and immunosuppressive activity. Its efficacy in autoimmune and inflammatory conditions is established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is an autoimmune condition in which T cells attack hair follicles. Because hydrocortisone is already used for autoimmune disease, a link to this disease is biologically plausible. Topical corticosteroids are also commonly used in alopecia areata in children.

There is an important limit. Hydrocortisone is a low-potency steroid, so its effect is expected to be weaker than that of high-potency agents such as clobetasol. This link rests on general corticosteroid pharmacology rather than on drug-specific mechanism data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized trial in children with alopecia areata comparing clobetasol propionate 0.05% cream with hydrocortisone 1% cream. Hydrocortisone was the low-potency comparator, so the trial does not directly show hydrocortisone efficacy. Results and endpoints are not available in the compiled data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Case series / clinical report | Przeglad dermatologiczny | Intralesional injections of hydrocortisone acetate suspension for severe alopecia areata (no abstract available) |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | Review of topical skin disease therapy. It notes that the anti-inflammatory effect of fluocortin butyl ester is roughly equal to that of hydrocortisone acetate. It is not specific to alopecia areata. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236399 | ANODAN-HC 10MG SUPPOSITORIES | Not stated | Not stated |
| 02387239 | JAMPZINC-HC | Not stated | Not stated |
| 02128446 | ANODAN-HC OINTMENT | Not stated | Not stated |
| 02238578 | FUCIDIN H | Not stated | Not stated |
| 00505773 | ANUSOL-HC OINTMENT | Not stated | Not stated |

Three more DINs are also valid (ANUSOL-HC SUPPOSITORIES, PROCTODAN-HC SUPPOSITORIES and PROCTODAN-HC OINTMENT), for 8 in total. The product names suggest that the marketed products are rectal and topical formulations.

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links hydrocortisone to contraindication-type relationships with several conditions, including:
  - hypertension
  - epilepsy
  - gastric ulcer
  - kidney disease
  - liver disease
  - gallbladder disease
  - hyperglycemia
  - measles
  - herpes simplex virus keratitis
  - pituitary hormone deficiencies and hypogonadotropic hypogonadism

  These should be confirmed against the official package insert.

Please refer to the package insert for further safety information, including warnings and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only trial is a small Phase 3 study in which hydrocortisone served as the low-potency comparator, and the two publications are decades old (1973 case series, 1979 review). The data do not show that hydrocortisone works in alopecia areata.
- The Canadian licences supply no indication or label safety text, so the safety review cannot proceed yet.

**To proceed, the following is needed:**
- Results and endpoints of NCT01453686, to see how hydrocortisone 1% performed against clobetasol
- Health Canada package insert warnings and contraindications for the marketed products
- Mechanism of action data for hydrocortisone acetate
- Confirmation of which formulations (topical versus intralesional) are relevant to alopecia areata
- Newer controlled studies of hydrocortisone in alopecia areata, if they exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

