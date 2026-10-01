---
layout: default
title: Methocarbamol
parent: Model Prediction Only (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol: From Musculoskeletal Conditions to Cauda Equina Syndrome

## One-Sentence Summary

Methocarbamol is a centrally acting skeletal muscle relaxant, marketed in Canada alone and in combination products for muscle spasm and pain.
The TxGNN model predicts it may be useful for **Cauda Equina Syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Painful musculoskeletal conditions and muscle spasm (general drug class knowledge; the licence records provide no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methocarbamol is a centrally acting skeletal muscle relaxant. It is used, alone and in combination with analgesics, for muscle spasm and back pain. Its effect on cauda equina syndrome is unproven.

The only plausible link is symptomatic. Cauda equina syndrome often presents with severe low back pain and muscle spasm, and a muscle relaxant might ease those symptoms. It would not treat the underlying nerve root compression, which is a surgical emergency. The prediction should therefore not be read as a disease-modifying use.

The high score is a model output only, with no trials or literature behind it. Most of the other top predictions for this drug (uveitis, iris disease, conjunctivitis, anaphylaxis and others) also lack a mechanistic rationale and are likely graph-topology artifacts. One of them, "obsolete bundle branch block", is an obsolete ontology term and not a clinically usable indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Methocarbamol appears in 16 licences. The five main ones are listed below. The pack has no dosage form or approved indication text for them.

| DIN | Product Name |
|---------|------|
| 1932187 | ROBAXIN 750 |
| 2377462 | ANALGESIC AND MUSCLE RELAXANT |
| 2239141 | EXTRA STRENGTH MUSCLE & BACK PAIN RELIEF |
| 2230949 | ROBAXISAL EXTRA STRENGTH |
| 2357356 | EXTRA STRENGTH TYLENOL BODY PAIN NIGHT |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature. Any benefit would be symptomatic at best, and cauda equina syndrome needs urgent surgical care. The Health Canada safety data is also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on muscle relaxants for spasm or pain in cauda equina syndrome
- Clinical input on whether symptomatic relief is a meaningful use case, given that the condition is a surgical emergency

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

