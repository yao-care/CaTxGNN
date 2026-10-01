---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 857
evidence_level: L5
indication_count: 1
---

# Sorbitol
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

# Sorbitol: From Osmotic and Irrigation Uses to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is a sugar alcohol used as an osmotic agent, sweetener and pharmaceutical excipient. In Canada it appears in irrigation-solution products. The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this, so the prediction rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no approved indication text is recorded for the two Canadian products. Sorbitol is known as an osmotic laxative, sweetener and excipient. Its Canadian products are sorbitol/mannitol-type irrigation solutions.

No supported mechanistic link between sorbitol and this condition was identified. Malignant hyperthermia and its exertional variants are generally attributed to dysregulated calcium release in skeletal muscle (for example, RYR1-related). Standard management is dantrolene plus supportive cooling. Sorbitol has no established action on this pathway.

The high score (0.994) is a knowledge-graph output, not clinical evidence. It may reflect graph artifacts, such as shared neighbours with other polyol or sugar compounds, or the broad connectivity of a common excipient. This explanation is an inference and has not been verified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 498807 | SORBITOL MANNITOL IRRIGATION |
| 799963 | CYSTOSOL W 3% HEXITOLS |

Dosage form and approved indication text are not recorded for these products.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no trials, no publications and no plausible mechanistic link to the calcium-handling pathway behind malignant hyperthermia, and established treatment (dantrolene) is unrelated to sorbitol.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and the original approved indications
- Any preclinical or clinical evidence linking sorbitol or related polyols to this condition
- Review of the knowledge-graph paths behind the prediction, to rule out excipient or polyol connectivity artifacts
- Route compatibility assessment, once a credible rationale exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

