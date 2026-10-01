---
layout: default
title: Norelgestromin
parent: Model Prediction Only (L5)
nav_order: 658
evidence_level: L5
indication_count: 1
---

# Norelgestromin
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is a progestin and the active metabolite of norgestimate, marketed in Canada as the EVRA product. The TxGNN model predicts it may be relevant to **amenorrhea**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The only support is the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data (the EVRA product is a contraceptive patch, so contraception is inferred) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norelgestromin is a progestin and the active metabolite of norgestimate, used in a contraceptive patch. Mechanistically, it may be applicable to amenorrhea, but this link is unverified.

Other progestins, such as medroxyprogesterone and norethindrone, are used for secondary amenorrhea, where they induce withdrawal bleeding or regulate the endometrium. This is class-level inference, not evidence for norelgestromin itself.

There are two reasons for caution:
- Hormonal contraceptives containing norelgestromin can cause amenorrhea as an adverse effect. The model's drug-disease association may therefore reflect this side effect rather than a therapeutic benefit.
- Amenorrhea is a symptom with many causes (pregnancy, hypothalamic, ovarian, hyperprolactinemia, etc.), and treatment depends on the underlying cause.

The very high score should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2248297 | EVRA |

Dosage form and approved indication text are not recorded for this license.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score, with no clinical trials, no literature, and no recorded original indication or mechanism. The prediction may also reflect amenorrhea as a known side effect of the drug rather than a treatment benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- The approved indication text for the EVRA license
- A targeted search for trials and literature on norelgestromin and amenorrhea
- Clarification of whether the association is therapeutic or an adverse effect
- Route compatibility assessment for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

