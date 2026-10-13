---
layout: default
title: Guselkumab
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Psoriasis to Drug-Induced Osteoporosis

## One-Sentence Summary

Guselkumab is an IL-23 p19 inhibitor marketed in Canada as TREMFYA, with psoriasis as an established use.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis (established use of the marketed drug; the Canadian license records compiled for this report contain no indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Guselkumab selectively blocks the p19 subunit of IL-23. This cytokine drives Th17 cell differentiation and the IL-17/IL-22 inflammatory axis, which is central to psoriatic plaque development. IL-23/IL-17 signaling has also been implicated in bone remodeling, which is the only conceptual bridge to osteoporosis.

The data compiled for this report do not support a direct link between IL-23 inhibition and drug-induced osteoporosis. No trials, publications, or similarity analysis to the original indication are available. The high TxGNN score (99.84%) reflects a pattern found in the knowledge graph and should not be read as clinical evidence. At this stage the prediction is a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02559153 | TREMFYA I.V. |
| 02559145 | TREMFYA |
| 02469758 | TREMFYA |
| 02487314 | TREMFYA ONE-PRESS |

All four authorizations are valid single-ingredient products. Dosage form and approved indication details are not available in the data compiled for this report.

## Safety Considerations

- **Drug Interactions:** 100 interactions are recorded. The most notable are listed below.
  - **Major:** adalimumab.
  - **Moderate:** warfarin, apixaban, rivaroxaban, dicoumarol, simvastatin, tacrolimus, theophylline, aminophylline, oxtriphylline, roflumilast, nifedipine, lidocaine, fentanyl, hydrocodone, and the tetanus toxoid vaccine.
  - **Minor:** zinc salts (sulfate, acetate, gluconate, chloride).

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature, and no clear mechanistic link between IL-23 blockade and drug-induced osteoporosis. Evidence is at the lowest level (L5).

For context, the same analysis found far better-supported predictions for this drug:
- **Psoriasis** (L1, Proceed with Guardrails): this is already an approved use, so it confirms existing use rather than repurposing.
- **Ulcerative colitis** (L1, Proceed with Guardrails): supported by Phase 2b/3 (QUASAR) and Phase 3 (ASTRO) trials.

These two are better candidates for further evaluation than drug-induced osteoporosis.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking IL-23/IL-17 signaling to bone loss in drug-induced osteoporosis
- A literature review for any clinical or observational signal on bone outcomes in patients treated with IL-23 inhibitors
- Package insert warnings and contraindications for the Canadian products
- Detailed mechanism of action data and a similarity analysis against the original indication
- Confirmation of the approved indication text for each DIN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

