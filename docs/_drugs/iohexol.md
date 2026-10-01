---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol: From Radiographic Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast agent used in X-ray imaging, and no therapeutic indication is recorded for it in the supplied data. The TxGNN model predicts it may be effective for **insomnia**, but **0 clinical trials** and **0 publications** support this prediction. The high score most likely reflects a knowledge-graph artifact rather than a real pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic radiographic contrast agent (no therapeutic indication recorded) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iohexol is a non-ionic iodinated contrast agent. It is pharmacologically inert and is excreted unchanged by the kidney. It has no known effect on the central nervous system or on sleep regulation.

There is no plausible mechanistic bridge between radiographic contrast imaging and insomnia. The TxGNN score is very high, but the drug has no recorded therapeutic indication or mechanism in the knowledge graph. That gap makes the prediction likely to be an artifact of graph structure. The related prediction "sleep disorder, initiating and maintaining sleep" (score 98.61%) looks like the same artifact. It should not be treated as independent support.

The other top-ranked predictions show the same pattern:

- **Anxiety, rheumatoid arthritis and tendinitis:** The retrieved trials and papers involve iohexol only as a GFR marker, an arthrography or procedural contrast agent, or a hypersensitivity-reaction case report. None tests iohexol as a treatment.
- **Antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, fibromyalgia and conjunctivitis:** No mechanism, trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

---

## Literature Evidence

Currently no related literature available for insomnia.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2172739 | OMNIPAQUE 240 |
| 2172747 | OMNIPAQUE 300 |
| 2172755 | OMNIPAQUE 350 |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for iohexol.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There is no mechanism, no trial and no literature supporting iohexol as a treatment for insomnia. Iohexol is a diagnostic agent with no known sleep-related pharmacology. Its Canadian market status does not change this.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any evidence of a plausible sleep-related mechanism or a therapeutic study, which would be required before re-evaluating the prediction
- Review of the knowledge-graph edges behind the score to confirm whether it is an artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

