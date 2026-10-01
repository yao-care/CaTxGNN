---
layout: default
title: Gramicidin D
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Gramicidin D
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

# Gramicidin D: From Topical Antibacterial Use to Postinfectious Vasculitis

## One-Sentence Summary

Gramicidin D is a topical antibacterial peptide used in Canadian products such as antibiotic creams and eye and ear drops. The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but this prediction has **no clinical trials and no publications** behind it. It rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; product names suggest topical antibacterial use (skin, eye and ear) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Gramicidin D is a membrane-active antibacterial peptide limited to topical use, often in fixed-dose combinations. Its role in bacterial skin, eye and ear infections is established, but a mechanistic link to the predicted indication is weak.

Postinfectious vasculitis is an immune-mediated process that follows an infection. No plausible antibacterial mechanism was identified that would let a topical antibiotic treat it. The high score most likely reflects graph proximity to infection-related terms rather than a specific biological rationale.

Systemic use is not realistic. Gramicidin D is hemolytic and toxic when given systemically, which is why it is restricted to topical products. Only topical routes are relevant, and vasculitis is not a topical-treatment target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Gramicidin D appears in 19 Canadian authorizations. Five main ones are listed below; dosage form and approved indication text are not recorded in the licence data.

| DIN | Product Name |
|---------|------|
| 2552418 | SOOTHE ANTIBIOTIC DROPS |
| 2230844 | POLYSPORIN ANTIBIOTIC CREAM |
| 2239156 | POLYSPORIN EYE AND EAR DROPS STERILE |
| 2317656 | ORIGINAL ANTIBIOTIC CREAM |
| 701785 | OPTIMYXIN |

---

## Safety Considerations

- **Systemic toxicity:** Gramicidin is hemolytic when given systemically, so use is limited to topical products. This is a mechanistic concern for any non-topical repurposing.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Postinfectious vasculitis is an immune-mediated condition with no plausible antibacterial mechanism and no clinical or literature support. The high TxGNN score is not backed by any actual study, and the systemic toxicity of gramicidin D rules out non-topical use.

**Other predicted indications worth noting:**
- **Otitis externa** (rank 7, evidence L3) is the only prediction with real support: 10 publications, including RCTs of topical combinations containing gramicidin (framycitin/gramicidin, and Triadcortyl). This is closer to an established topical use than to true repurposing. Because the studies use combination products, gramicidin's own contribution cannot be isolated.
- **Post-bacterial disorder** (rank 2) has one Phase 3 trial (NCT00534391, hordeolum after incision and curettage). It is only indirectly related.
- **Infection-related hemolytic uremic syndrome** (rank 6) should be deprioritized, since gramicidin's hemolytic activity is a mechanistic contraindication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data (e.g., from DrugBank)
- The original approved indication, reconciled against Canadian labeling
- If pursuing otitis externa, a review of the combination-product evidence against current Canadian labeling
- For any ophthalmic candidate, a review of eye-specific safety and efficacy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

