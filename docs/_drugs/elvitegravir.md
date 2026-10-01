---
layout: default
title: Elvitegravir
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Elvitegravir is an HIV-1 integrase inhibitor sold in Canada as part of combination antiretroviral products. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection)**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the license records provided contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, elvitegravir is an HIV-1 integrase strand transfer inhibitor. It blocks the step in which viral DNA is inserted into the host genome, and this is its established use in HIV-1 treatment.

Feline immunodeficiency virus (FIV) is also a lentivirus and encodes its own integrase enzyme. Mechanistically, a drug that blocks HIV-1 integrase could plausibly act on FIV. The very high TxGNN score most likely reflects the drug's closeness to other retroviral-disease nodes in the knowledge graph. It is not evidence that elvitegravir inhibits FIV integrase or FIV replication.

No trials or publications were provided for this indication. FIV is also a veterinary disease, while the Canadian licenses listed here are for human products. The prediction is therefore a hypothesis only.

**Related finding:** The second-ranked prediction, simian immunodeficiency virus (SIV) infection, has 7 preclinical publications, mainly in vitro integrase-inhibitor susceptibility and resistance studies and macaque or mouse models. It is still indirect evidence and does not support a human clinical indication. Some of these papers may test other integrase inhibitors rather than elvitegravir, and this could not be confirmed from the truncated titles.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2449498 | GENVOYA | Not listed | Not listed |
| 2397137 | STRIBILD | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and a plausible lentiviral-integrase similarity. No trials, literature, or mechanistic data show that elvitegravir acts against FIV. The indication is veterinary, and the available Canadian licenses are for human combination products.

**To proceed, the following is needed:**
- In vitro data showing elvitegravir inhibits FIV integrase or FIV replication
- Mechanism of action data (MOA) and the original approved indication text from Health Canada
- Package insert warnings and contraindications from Health Canada
- A veterinary regulatory and formulation assessment, since the current licenses are for human products
- Confirmation of which SIV-related papers actually test elvitegravir, if the SIV research-model question is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

