---
layout: default
title: Clotrimazole
parent: Moderate Evidence (L3-L4)
nav_order: 217
evidence_level: L4
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Clotrimazole: From Superficial Fungal Infections to Acne

## One-Sentence Summary

Clotrimazole is an azole antifungal, originally used for skin and mucosal fungal infections such as tinea pedis (athlete's foot), cutaneous candidiasis and vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **acne**, but the evidence is thin: **1 clinical trial** (suspended, combination product) and **no publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis and other superficial fungal infections, including cutaneous, oral and vulvovaginal candidiasis |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Clotrimazole blocks fungal CYP51 (lanosterol 14-alpha-demethylase), an enzyme needed to make ergosterol. Without ergosterol the fungal cell membrane loses its integrity, and fungal growth is inhibited. Clotrimazole has also been reported to have anti-inflammatory and antimicrobial activity on the skin. Detailed mechanism-of-action data were not available in the data compiled for this report.

The link to acne is plausible but indirect. Reducing Malassezia or Candida colonization, and calming inflammation around hair follicles, might help some acne-like lesions. Acne is mainly driven by sebum, follicular blockage, *Cutibacterium acnes* and inflammation, so an antifungal is not an obvious fit.

The high score (0.999) is a computational prediction from a knowledge graph. It is not clinical evidence. The only related trial tested a fixed combination product, so no effect can be attributed to clotrimazole itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a topical cream combining beclomethasone 0.025%, gentamicin 0.1% and clotrimazole 1% in patients with contaminated dermatosis. No results reported. The steroid and antibiotic components confound any clotrimazole-specific effect. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Clotrimazole has 20 valid single-ingredient authorizations in Canada. The records compiled for this report do not include dosage form or approved indication text. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229378 | Clotrimazole Vaginal 6 | — | — |
| 02150859 | Canesten Comfortab 1 | — | — |
| 02229380 | Clotrimazole Topical | — | — |
| 02462397 | Clotrimazole External Antifungal Cream | — | — |
| 02264102 | Canesten Combi 1 Day | — | — |

---

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (from drug-disease links, not package insert text): adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent claudication and peripheral arterial disease. Several of these are relevant to long-term topical use, especially in combination with a corticosteroid.
- **Drug Interactions**: The interaction query returned 100 records. Among those reviewed, the **Major** interactions were fentanyl, alfentanil, hydrocodone and amiodarone. Many **Moderate** interactions were also listed, including paclitaxel, abemaciclib, acalabrutinib, nifedipine, amlodipine, apixaban, alprazolam, aliskiren, alfuzosin, aprepitant, estradiol, levonorgestrel and norethisterone. Dolutegravir and amphotericin B are **Minor**. Because the Major interactions involve CYP3A4 substrates, any systemic or high-exposure use would need an interaction review.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests on a high model score and one suspended combination-product trial with no results. Clotrimazole's antifungal mechanism has only an indirect link to acne. No publications support this direction.

Two other predictions in the same analysis are worth noting:
- **Vulvovaginitis (candidal)** has L1-level evidence, including several completed Phase 3 trials. It is effectively an existing indication rather than true repurposing, and it would qualify as Proceed with Guardrails. Guardrails would cover pregnancy exposure data, azole resistance and recurrent disease.
- **Postmenopausal atrophic vaginitis** has no trials or literature and no mechanistic rationale, so it stays at Hold.

**To proceed, the following is needed:**
- Clotrimazole-only controlled trials in acne, since the existing trial is a combination product
- Preclinical or mechanistic data linking clotrimazole to acne pathophysiology
- Health Canada package insert warnings and contraindications
- Detailed mechanism-of-action data from DrugBank
- Dosage form and approved indication details for the Canadian products
- A review of interaction risks and topical safety in the skin conditions of interest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

