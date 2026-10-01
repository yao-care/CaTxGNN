---
layout: default
title: Enalaprilat
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 1
---

# Enalaprilat
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

# Enalaprilat: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Enalaprilat is an injectable ACE inhibitor. The licence record does not state its approved indication, but it is generally used for hypertension when oral therapy is not practical.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with a high score of 99.09%.
There are currently **no clinical trials and no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence record (general pharmacology: hypertension) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.09% (model rank 15082) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, enalaprilat is the active metabolite of enalapril and belongs to the ACE inhibitor class. Its blood-pressure-lowering effect is established. Mechanistically, a plausible but unverified hypothesis is that modulating the local renin-angiotensin system could affect aqueous humour dynamics and intraocular pressure.

The link to the new indication is weak. Primary hereditary glaucoma is a developmental or genetic disorder of the anterior chamber angle (for example, CYP1B1-related). It has no clear connection to ACE inhibition. The only support is the high TxGNN knowledge-graph score, which is a computational prediction and not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2388499 | Enalaprilat Injection USP | Not listed (injection by product name) | Not listed in the licence record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (L5), and there is no clear mechanistic link between ACE inhibition and a genetic developmental glaucoma. A high model score alone does not justify further investment at this stage.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) and a review of whether renin-angiotensin modulation plausibly affects intraocular pressure
- Package insert warnings and contraindications from Health Canada, to complete safety screening
- Preclinical or literature evidence for ACE inhibitors in glaucoma
- Route compatibility assessment, since the only licensed product is an injection and glaucoma treatment would likely need a different route (such as topical ocular)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

