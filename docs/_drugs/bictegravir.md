---
layout: default
title: Bictegravir
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 3
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Bictegravir is an HIV-1 integrase strand transfer inhibitor, marketed in Canada as BIKTARVY.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection)** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license record (drug class: HIV-1 integrase strand transfer inhibitor) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, bictegravir belongs to the integrase strand transfer inhibitor (INSTI) class, whose efficacy against HIV-1 is established, and mechanistically it may be applicable to related lentiviruses.

Feline immunodeficiency virus (FIV) is a lentivirus that, like HIV-1, encodes an integrase enzyme. That makes the prediction biologically plausible. However, this link is inferred from drug class alone. No data on bictegravir inhibiting FIV integrase were provided, and the high TxGNN score is a computational output, not experimental evidence.

Two other predictions for this drug are worth noting:
- **Simian immunodeficiency virus (SIV) infection** (score 99.82%, evidence level L4): preclinical work supports the mechanism. An in vitro study (PMID 28923862) tested bictegravir against INSTI-resistant SIVmac239, and structural work on HIV/SIV intasomes (PMID 32506843) explains how INSTIs bind. SIV is a nonhuman primate pathogen, so its value is mainly as a preclinical model for HIV research, not as a human indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.76%, evidence level L5): no credible mechanistic link. This is a rare genetic disorder with no known viral or integrase-related cause, and the prediction is likely a false positive from knowledge-graph topology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2478579 | BIKTARVY |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and a class-based mechanistic inference, with no trials, no literature, and no cross-species enzyme inhibition data (evidence level L5). Feline AIDS is also a veterinary condition, so any development would follow a veterinary rather than human-drug pathway.

**To proceed, the following is needed:**
- Mechanism of action data for bictegravir (e.g., from DrugBank)
- In vitro data on bictegravir activity against FIV integrase or FIV replication
- Health Canada package insert warnings and contraindications
- Confirmation of the regulatory and development pathway for a veterinary indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

