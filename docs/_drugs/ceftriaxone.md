---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 168
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ceftriaxone: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic, used for bacterial infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**,
but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (the approved indication text is empty for all listed licences); ceftriaxone is a systemic antibacterial |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Ceftriaxone is a third-generation cephalosporin, and this class inhibits bacterial cell-wall synthesis.

This prediction is not mechanistically plausible. Polyclonal hyperviscosity syndrome involves raised serum viscosity from excess polyclonal immunoglobulins. Ceftriaxone has no known effect on serum viscosity or immunoglobulin levels. The high score of 0.994 reflects a model-level association only, and no trial or publication supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Five main authorizations are listed below. Dosage form and approved indication text are not available in the supplied record.

| DIN | Product Name |
|---------|------|
| 2325632 | CEFTRIAXONE SODIUM FOR INJECTION BP |
| 2409968 | CEFTRIAXONE FOR INJECTION |
| 2325616 | CEFTRIAXONE SODIUM FOR INJECTION BP |
| 2292270 | CEFTRIAXONE SODIUM FOR INJECTION BP |
| 2292262 | CEFTRIAXONE SODIUM FOR INJECTION BP |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism. It is a model-only signal (L5) and should not advance.

**To proceed, the following is needed:**
- Any mechanistic or clinical rationale linking ceftriaxone to serum hyperviscosity or polyclonal immunoglobulin excess (none identified)
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences

**Note on other predictions for this drug:**
Infectious otitis media (score 99.26%) has the strongest support among the candidates in this pack. It is rated L2 with a "Proceed with Guardrails" recommendation, based on comparative ceftriaxone studies in acute otitis media. It may reflect an existing labeled or guideline use rather than true repurposing, so it should be confirmed against the local label and evaluated as a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

