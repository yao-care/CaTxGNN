---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Ocular Redness Relief to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is a topical alpha-adrenergic vasoconstrictor sold in Canada in over-the-counter eye drops for redness relief. The TxGNN model predicts it may be useful for **hypotrichosis simplex of the scalp** with a very high score (99.83%), but **0 clinical trials** and **0 publications** support this prediction. It rests on the model alone, and the available mechanistic reasoning argues against it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular redness relief (inferred from product names and drug class; the license records contain no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, naphazoline is a topical alpha-adrenergic agonist that constricts blood vessels. This effect is why it is used to reduce eye redness.

The prediction is **not mechanistically well supported**. Hair growth disorders have no plausible link to an alpha-agonist decongestant. Vasoconstriction could even reduce scalp perfusion, the opposite of what vasodilators such as minoxidil do. The high score most likely reflects shared neighbourhood in the knowledge graph with other hair-related indications, not a pharmacological rationale.

The other top-ranked predictions show the same pattern. The top 10 are mostly hair disorders (alopecia, alopecia areata, hypertrichosis) and rare congenital malformation syndromes, and none has clinical trial evidence. The two glaucoma predictions (primary hereditary glaucoma and open-angle glaucoma) have a class-level rationale, since other alpha-agonists such as brimonidine and apraclonidine lower intraocular pressure. Naphazoline is not an established pressure-lowering agent, however. Its pupil-dilating effect also raises an angle-closure safety concern in susceptible eyes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For context, the only literature retrieved for the top 10 predictions was for lower-ranked entries, and none of it concerns naphazoline:
- **Open-angle glaucoma (rank 8):** one 1992 paper on topical corticosteroids after laser trabeculoplasty.
- **Malformation syndrome with periodontal component (rank 9):** about 20 general periodontitis papers, which look like keyword matches on the disease term.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2248060 | CLEAR EYES |
| 1147 | ALBALON |
| 2242764 | VISINE FOR ALLERGY WITH ANTIHISTAMINE |
| 674354 | COLLYRE BLEU LAITER |
| 2360837 | CLEAR EYES EXTRA STRENGTH REDNESS RELIEF |

Showing 5 of 8 licenses. Dosage form and approved indication text are not recorded in the current data.

---

## Safety Considerations

Please refer to the package insert for safety information.

One safety point relates to the predicted glaucoma indications. As an ophthalmic decongestant, naphazoline can cause mydriasis and carries an angle-closure warning in susceptible eyes.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or literature. Vasoconstriction is mechanistically unfavourable for hair growth, and the high score looks like a graph artefact from hair-disorder clustering.

**To proceed, the following is needed:**
- Mechanism of action data for naphazoline, from DrugBank
- Health Canada package insert warnings and contraindications
- Any preclinical or clinical evidence linking naphazoline to a predicted indication (none exists now)
- If a candidate is pursued at all, a priority review of the glaucoma predictions, which have a class-level rationale, weighed against the angle-closure risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

