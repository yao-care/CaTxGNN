---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Latanoprost: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
---

# Latanoprost
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2-alpha analogue originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 (mechanistic reasoning only; no trials or literature) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known pharmacology, latanoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure (IOP) by increasing uveoscleral outflow of aqueous humour.

Primary hereditary glaucoma (for example, primary congenital glaucoma or juvenile open-angle glaucoma) shares raised IOP as its core problem. This is the same target as in the approved indication, so a link is plausible.

There is an important caveat. Congenital and paediatric glaucomas often involve developmental abnormalities of the eye's drainage angle (trabeculodysgenesis), which may reduce how well prostaglandin analogues work. The case for this prediction is therefore indirect and class-based.

Other predictions in the list include hair-growth conditions (hypotrichosis simplex of the scalp, congenital hypotrichosis milia). These have a plausible class-level rationale, because prostaglandin analogues prolong the hair growth phase and stimulate eyelash growth. Vascular and structural conditions such as thoracic outlet syndromes, visceral calciphylaxis, gastric angiodysplasia, blue toe syndrome and lymphangiectasis have no credible mechanistic link and look like network artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Latanoprost has 17 valid single-entry licences in Canada and no cancelled ones. Dosage form and approved indication text were not available for these products. Five main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02231493 | XALATAN | Not specified | Not specified |
| 02246619 | XALACOM | Not specified | Not specified |
| 02296527 | APO-LATANOPROST | Not specified | Not specified |
| 02254786 | TEVA-LATANOPROST | Not specified | Not specified |
| 02341085 | RIVA-LATANOPROST | Not specified | Not specified |

Other licences include latanoprost/timolol combination products (for example, MED-LATANOPROST-TIMOLOL and TEVA-LATANOPROST-TIMOLOL), which are listed in the data as single entries.

## Safety Considerations

- **Conditions flagged in the drug–disease knowledge graph (not label text)**: uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, and conjunctivitis (including acute contagious conjunctivitis). These are signals to check against the package insert, not confirmed label contraindications.
- **Drug Interactions**: The interaction query returned 100 records. The 20 shown have an unclassified severity level, so none can be ranked as clinically significant. Examples include calcitriol, glimepiride, doxycycline, atropine, morphine, metformin, prednisone, triamcinolone and simvastatin. The severity and clinical relevance of these entries need confirming, especially given the minimal systemic exposure of topical ocular dosing.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.88%), but there are no registered trials and no publications for primary hereditary glaucoma. The mechanistic link is plausible but weakened by the developmental drainage-angle abnormalities typical of congenital forms. At this stage it is a research question, not a candidate ready for development.

**To proceed, the following is needed:**
- A systematic literature search for prostaglandin analogues in primary congenital and juvenile glaucoma, including paediatric efficacy and safety data
- Detailed mechanism-of-action data
- Health Canada package insert warnings and contraindications, to complete safety screening
- Product-level dosage form and approved indication details for the Canadian licences
- Review of the knowledge-graph–flagged ocular conditions (uveitis, macular oedema, conjunctivitis) against label text
- Severity classification of the drug interaction records
- A dedicated assessment of the hair-growth predictions (hypotrichosis simplex of the scalp, congenital hypotrichosis milia) as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

