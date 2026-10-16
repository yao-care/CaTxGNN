---
layout: default
title: Pramocaine
parent: Model Prediction Only (L5)
nav_order: 760
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Pramocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Dermatitis, exanthem, tinea infections, otitis externa, hemorrhoids…"
---

# Pramocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Pramocaine: From Dermatitis and Pruritic Skin Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Pramocaine (pramoxine) is a topical surface anesthetic originally used for symptomatic relief of itch and pain in skin and mucosal conditions such as dermatitis, burns and hemorrhoids.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
but **no clinical trials and no publications** currently support this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis, exanthem, tinea infections, otitis externa, hemorrhoids, burns, proctitis and related conditions (approved-indication text is not available for the Canadian licences) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pramocaine is generally known as a topical surface anesthetic that blocks voltage-gated sodium channels in sensory nerve endings, which reduces itch and pain signalling.

Its original indications (dermatitis, rash, burns, hemorrhoids, otitis externa) mostly involve itch or pain. Papillary conjunctivitis, typically allergic or contact lens-related, also involves ocular itching and inflammation. A symptom-relief rationale is therefore plausible in principle.

This link is speculative, though, for three reasons:
- The high TxGNN score is a model-derived prediction, with no supporting trial or publication.
- Numbing the eye would not treat the underlying allergic or immune-mediated inflammation.
- Pramoxine products are not approved for eye use, and topical anesthetics can damage the cornea with repeated use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Twelve single-ingredient licences are currently valid in Canada. The data compiled for this report do not include dosage forms or approved-indication text, so those columns are left blank. The five main products are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02484889 | Itch Relief Moisturizing Cream | Cream (from product name) | Not available |
| 02486881 | Itch Relief Moisturizing Lotion | Lotion (from product name) | Not available |
| 01945912 | Anusol Plus Ointment | Ointment (from product name) | Not available |
| 01954210 | Pramox HC Lotion | Lotion (from product name) | Not available |
| 02236991 | Gold Bond Medicated Anti-Itch Cream | Cream (from product name) | Not available |

All current products are for topical or rectal use, and none is an ophthalmic product.

## Safety Considerations

No label-based warnings, contraindications or drug interaction data were available in the data compiled for this report.

A knowledge-graph analysis flagged potential disease-level contraindication signals. These are model-derived, not label text, and likely reflect the combination products (for example, those containing hydrocortisone) rather than pramocaine alone. The flagged conditions include:
- **Infections:** fungal infections, dermatophytosis, herpes simplex (including herpes simplex keratitis), varicella zoster, measles and other infectious diseases
- **Cardiometabolic:** hypertension, diabetes mellitus and diabetic ketoacidosis, coronary artery disease, sudden cardiac arrest
- **Endocrine and other systemic:** adrenocortical insufficiency, Addison disease, hypothyroidism, osteoporosis, kidney disease
- **Others:** open-angle glaucoma, contact dermatitis, psychotic disorders, benign prostatic hyperplasia

Several of these (herpes simplex keratitis, glaucoma, infections) are especially relevant to any ocular use.

Ocular safety is the main unresolved concern. Repeated use of topical anesthetics on the eye can cause corneal toxicity, and no ophthalmic safety data exist for pramocaine.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5), with no clinical trials or publications. The mechanistic link is speculative, no ophthalmic formulation exists, and the corneal safety risk is significant. Safety screening cannot proceed until the package insert data are obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap)
- Confirmed mechanism of action data from DrugBank
- A literature and trial search for topical anesthetics or antipruritics in allergic or papillary conjunctivitis
- Preclinical ocular tolerability and corneal toxicity data
- An assessment of whether a suitable ophthalmic formulation and route is feasible
- Evidence that symptom relief, rather than treatment of underlying inflammation, would be clinically meaningful, compared with established options such as antihistamines and mast cell stabilizers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

