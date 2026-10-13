---
layout: default
title: Pilocarpine
parent: Model Prediction Only (L5)
nav_order: 735
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine was originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but this is a model prediction only, with **no registered clinical trials and no publications** currently supporting it. The predicted indication also overlaps heavily with the existing glaucoma indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (from the knowledge-graph indication data, as Canadian license indication text is not available) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, pilocarpine is a muscarinic (M3) receptor agonist. It contracts the ciliary muscle and increases trabecular outflow of aqueous humour, which lowers intraocular pressure (IOP). This is the basis of its use in open-angle glaucoma and ocular hypertension.

Primary hereditary glaucoma is also centred on impaired aqueous outflow and raised IOP, so a mechanistic link is plausible. However, the prediction may largely reflect how close the diseases are in the disease ontology rather than a truly new repurposing opportunity, because the new indication substantially overlaps with the existing glaucoma indications.

There are important caveats. Hereditary forms such as primary congenital glaucoma (for example, those linked to CYP1B1 variants) typically arise from developmental abnormalities of the trabecular meshwork or drainage angle and are usually treated surgically. Miotics like pilocarpine may have limited efficacy in these patients and raise paediatric safety concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00000868 | ISOPTO CARPINE | Not available | Not available |
| 02496119 | M-PILOCARPINE | Not available | Not available |
| 02148463 | MINIMS PILOCARPINE NITRATE | Not available | Not available |
| 02216345 | SALAGEN | Not available | Not available |
| 02509571 | JAMP PILOCARPINE | Not available | Not available |

---

## Safety Considerations

- **Disease-related cautions (from knowledge-graph contraindication links, not label text)**:
  - Eye conditions: angle-closure (closed-angle) glaucoma, keratitis, keratoconjunctivitis, iritis, iridocyclitis, uveitis, retinal detachment
  - Respiratory conditions: asthma, chronic obstructive pulmonary disease, bronchial disease
  - Biliary and liver conditions: cholelithiasis, cholecystolithiasis, choledocholithiasis, cholecystitis, biliary tract disease, obstructive jaundice, liver failure
  - Kidney conditions: nephrolithiasis, acute urate nephropathy
- **Drug Interactions**: The interaction search returned 100 records. The ones listed as Moderate are mainly anticholinergic (antimuscarinic) agents, which may oppose pilocarpine's effect: hyoscyamine, atropine (including ophthalmic), glycopyrronium (including topical), clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, scopolamine (including ophthalmic) and trospium. Several others (e.g., pantoprazole, omeprazole, lansoprazole, clotrimazole, morphine, metformin, epinephrine) are listed with an unknown severity level.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score (99.83%) with no clinical trials or publications. It overlaps with approved glaucoma uses, and hereditary glaucoma is usually managed surgically, so the added value of pilocarpine is uncertain.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Clarification of which hereditary glaucoma subtypes are targeted, and whether they differ meaningfully from the approved indications
- Literature and trial searches for pilocarpine in hereditary or congenital glaucoma, including paediatric safety
- Approved indication text and dosage forms for the Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

