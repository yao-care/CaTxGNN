---
layout: default
title: Cobicistat
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: From HIV-1 Pharmacokinetic Boosting to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Cobicistat is a CYP3A inhibitor used as a pharmacokinetic booster in HIV-1 antiretroviral combination products.
The TxGNN model predicts it may be relevant to **simian immunodeficiency virus infection**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharmacokinetic booster in HIV-1 antiretroviral combinations (the Canadian licence records provide no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Cobicistat is a mechanism-based CYP3A inhibitor. It has no antiviral activity of its own. It raises the exposure of co-administered antiretrovirals such as elvitegravir, darunavir and atazanavir.

SIV is a lentivirus closely related to HIV-1. The high score most likely reflects proximity to HIV-1 therapeutics in the knowledge graph, not a direct effect on SIV. Any benefit in SIV would depend on a co-administered antiretroviral that is active against it. No SIV-specific preclinical or clinical evidence was provided.

The other two predictions are weaker:
- **Feline acquired immunodeficiency syndrome (FIV):** This is a veterinary lentiviral disease, not a human indication. The reasoning is the same as for SIV.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter:** No plausible mechanistic link can be identified. The score (about 99.91%) may be an artifact of sparse disease annotation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2426501 | PREZCOBIX |
| 2473720 | SYMTUZA |
| 2449498 | GENVOYA |
| 2397137 | STRIBILD |

Dosage form and approved indication text were not provided for these licences.

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack contains no drug interaction records. Because cobicistat inhibits CYP3A, any use alongside other drugs requires an interaction review against the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score (L5). Cobicistat has no intrinsic antiviral activity, and there are no SIV-specific trials or publications. The FIV prediction is veterinary, and the neurodevelopmental prediction has no identifiable mechanistic link.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- SIV-specific preclinical evidence for cobicistat combined with an active antiretroviral
- Indication text and dosage forms for the four Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

