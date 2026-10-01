---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the Canadian licence records provide no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Doravirine is an NNRTI approved for HIV-1, and it is sold in Canada as a single agent (PIFELTRO) and in a combination product (DELSTRIGO).

The high score likely reflects the fact that HIV-1 and feline immunodeficiency virus are both lentiviruses with a reverse transcriptase target, which places them close together in the knowledge graph. The mechanistic link is weak, however. NNRTIs generally have poor activity against FIV reverse transcriptase because the NNRTI binding pocket differs structurally. FIV is also a veterinary condition, so it falls outside the scope of human drug repurposing.

The other top predictions are no stronger:
- **Simian immunodeficiency virus infection** (score 99.93%): SIV is closely related to HIV, but many SIV strains and HIV-2 are naturally resistant to NNRTIs. The only linked paper covers islatravir, a different drug class, so it is indirect evidence at best. SIV is also mainly an animal-model infection.
- **A rare neurodevelopmental disorder with ataxic gait and absent speech** (score 99.91%): There is no plausible mechanistic link, and the score is probably a knowledge-graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2481545 | PIFELTRO |
| 2482592 | DELSTRIGO |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no trials or literature, and NNRTIs are known to be poorly active against FIV. FIV is a veterinary indication and not a human repurposing target.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- In vitro evidence of doravirine activity against FIV or SIV reverse transcriptase
- A decision on whether veterinary indications are in scope for this programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

