---
layout: default
title: Fluorometholone
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluorometholone: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Uveitis, iritis/iridocyclitis, conjunctivitis (atopic, vernal…"
monitor_inn: "FLUOROMETHOLONE"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Fluorometholone
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

# Fluorometholone: From Uveitis and Ocular Surface Inflammation to Postinfectious Vasculitis

## One-Sentence Summary

Fluorometholone is a topical corticosteroid, originally used for ocular inflammatory conditions such as uveitis, iritis and conjunctivitis.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model alone.
Among the other predictions, the more biologically plausible ones are punctate epithelial keratoconjunctivitis, lens-induced iridocyclitis and glaucomatocyclitic crisis, which are all eye conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uveitis, iritis/iridocyclitis, conjunctivitis (atopic, vernal, papillary), corneal ulcer and related ocular inflammation (the Canadian licence records contain no indication text) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, fluorometholone acts on the glucocorticoid receptor (NR3C1). It suppresses inflammatory mediators and immune activity, which is why it is used for inflammatory eye conditions.

For postinfectious vasculitis, there is a theoretical link, because immune-mediated vasculitis involves inflammation that corticosteroids can dampen. However, fluorometholone is an ophthalmic product with limited systemic exposure, so it is unlikely to treat a systemic vascular disease. The high TxGNN score is a computational prediction only.

Other predictions in the list vary in plausibility:

- **More plausible (eye-related, L4, "Research Question"):**
  - Punctate epithelial keratoconjunctivitis is an immune-mediated ocular surface condition close to the approved uses.
  - Lens-induced iridocyclitis is an anterior segment inflammation similar to the approved iritis and iridocyclitis indications.
  - Glaucomatocyclitic crisis is a recurrent anterior inflammation in which topical steroids are standard care. Fluorometholone's relatively lower tendency to raise intraocular pressure is a plausible rationale.
- **Less plausible (L5):** otitis externa (the ophthalmic suspension is not formulated for ear use), infective urethral stricture, infection-related hemolytic uremic syndrome and Chagas cardiomyopathy. There is no sensible delivery route or mechanistic link for these. The remaining predictions (post-bacterial disorder and post-infectious syndrome) are too vague to assess.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for postinfectious vasculitis. None were found for any of the other top 10 predicted indications either.

---

## Literature Evidence

Currently no related literature available for postinfectious vasculitis.

For reference, two indirect papers were retrieved for the predicted indication punctate epithelial keratoconjunctivitis. Neither tests fluorometholone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Review | Indian Journal of Ophthalmology | Describes the sequelae of microsporidial keratoconjunctivitis and outlines its management |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Cohort | Journal of Current Ophthalmology | Uses anterior segment OCT to describe the phases of epidemic keratoconjunctivitis and the effect of topical steroid on its course |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00247855 | FML | Not listed | Not listed |
| 00432814 | SANDOZ FLUOROMETHOLONE | Not listed | Not listed |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** herpes simplex virus keratitis, viral eye infection, fungal infection of eye, ocular tuberculosis, eye infectious disease, conjunctivitis (infectious), open-angle glaucoma, ocular hypertension, diabetes mellitus, diabetic ketoacidosis, porphyria (including inherited porphyria and porphyrin metabolism disease), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia and corneal pigmentation.
- **Drug interactions:** 11 interacting drugs were identified in the DDInter database, but none has a severity level assigned. They are doxycycline, salbutamol, cyclosporine, acetaminophen, digoxin, brimonidine, cephalexin, alendronic acid, acyclovir, diazepam and fenofibrate.
- **Caution with steroid use in infectious eye conditions:** corticosteroids may prolong viral shedding, increase the risk of secondary infection and raise intraocular pressure. Intraocular pressure monitoring is important.

Please refer to the package insert for label-based warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for postinfectious vasculitis has no supporting trials or literature, and the ophthalmic formulation has limited systemic exposure. Evidence is at the model-prediction level only (L5). If this drug is pursued further, the eye-related predictions (punctate epithelial keratoconjunctivitis, lens-induced iridocyclitis, glaucomatocyclitic crisis) are better candidates for investigation as research questions.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Dosage form and route information for the Canadian products
- Any clinical or preclinical studies of fluorometholone or topical corticosteroids in the predicted indication
- A review of whether the ophthalmic route could reach the target tissue, and a separate assessment of the eye-related predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

