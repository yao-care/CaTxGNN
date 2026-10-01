---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 986
evidence_level: L5
indication_count: 4
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Zinc Sulfate: From Marketed Topical Products to Pharyngitis

## One-Sentence Summary

Zinc sulfate is a long-established mineral compound found in Canadian topical products such as hemorrhoid ointments and suppositories and eye drops. The TxGNN model predicts it may be effective for **pharyngitis**, with **4 clinical trials** and **3 publications** retrieved. Only a few of these concern throat symptoms, and none directly studies infectious pharyngitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 (borderline: the supporting studies are indirect and not Phase 2/3 trials in pharyngitis) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general zinc pharmacology, zinc has plausible local mucosal effects: antiviral activity, support for epithelial repair, and anti-inflammatory action. Lozenges or gargles deliver zinc directly to the pharyngeal mucosa, which is where pharyngitis occurs.

The clinical signals so far come from throat symptoms with non-infectious causes: sore throat after intubation, and mucositis and pharyngitis after radiotherapy. Both conditions involve irritated pharyngeal mucosa, so they are a reasonable proxy. They are still not the same disease as infectious pharyngitis. The very high TxGNN score is a model prediction, not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | N/A | Completed | 87 | Randomized, double-blind, placebo-controlled study of zinc lozenges for postoperative sore throat. It is the only trial targeting pharyngeal symptoms, but the population is post-intubation, not infectious pharyngitis. |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Completed | 3 | Placebo-controlled zinc trial in outpatients with COVID-19. With only 3 participants it is effectively uninformative, and the disease differs from the target. |
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Completed | 18 | Hydroxychloroquine and zinc with azithromycin or doxycycline in COVID-19 outpatients. It is a combination therapy in a different disease, so zinc's effect cannot be isolated. |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Completed | 4257 | Open-label COVID-19 prophylaxis trial in migrant workers (DORM). Zinc was part of a multi-agent regimen, and the endpoint is not pharyngitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Randomized, double-blind, placebo-controlled trial of zinc sulfate supplementation for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. |
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT (inferred from title; needs verification) | BMC Anesthesiology | Compared preoperative zinc, magnesium and budesonide gargles for incidence and severity of postoperative sore throat after intubation. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report / clinical observation | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Recovery from long-lasting taste disturbance after tonsillectomy. Zinc deficiency is discussed as a possible factor, so the link to pharyngitis is indirect. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2236399 | ANODAN-HC 10MG SUPPOSITORIES |
| 2290596 | ALLERGY EYE DROPS |
| 2338602 | VISINE MULTI-SYMPTOM |
| 2387239 | JAMPZINC-HC |
| 2128446 | ANODAN-HC OINTMENT |

The records provided list no dosage forms or approved indication text for these products.

---

## Safety Considerations

Please refer to the package insert for safety information.

One caution comes from the other predicted indications. Intranasal zinc sulfate is used experimentally to induce anosmia in animals, so any nasal use would need careful safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct clinical signals come from non-infectious throat conditions (postoperative sore throat and radiation-induced pharyngitis). No trial has tested zinc sulfate in infectious pharyngitis, and the high TxGNN score alone cannot justify moving forward. This is best treated as a research question for now.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Mechanism of action data, for example from DrugBank
- Verification of the study design of PMID 38693477 and its results
- Evidence from trials in infectious pharyngitis
- A route and formulation compatibility assessment, for example lozenge or gargle against the currently marketed topical products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

