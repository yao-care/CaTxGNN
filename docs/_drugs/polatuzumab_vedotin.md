---
layout: default
title: Polatuzumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From Its Original Use to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an antibody-drug conjugate (marketed in Canada as POLIVY), and the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**,
but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, polatuzumab vedotin is an anti-CD79b antibody-drug conjugate that delivers the microtubule inhibitor MMAE to cells. CD79b is a component of the B-cell receptor, so the drug's targeting is built around B-cell biology.

CD79b is not a recognized target in HER2-positive breast carcinoma, so the data do not support a direct mechanistic link. Any activity would have to come from the MMAE payload, for example through non-specific uptake or a bystander effect. That explanation is speculative and is not supported by this dataset. HER2-positive breast cancer also already has approved HER2-directed antibody-drug conjugates, such as trastuzumab emtansine and trastuzumab deruxtecan.

The very high TxGNN score (99.34%) is a model prediction only. It likely reflects knowledge-graph proximity between antibody-drug conjugates or tubulin-inhibitor payloads and breast cancer, not target-level biology. It should not be read as evidence of efficacy.

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
| 2515431 | POLIVY |
| 2499614 | POLIVY |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (MMAE, a microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert; follow institutional cytotoxic drug handling procedures |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. There are no registered trials or publications, and no mechanistic link is supported by the provided data. Approved HER2-directed antibody-drug conjugates already exist in this disease setting.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to test whether any plausible link to HER2-positive breast carcinoma exists
- Package insert warnings and contraindications from Health Canada, to complete safety screening
- Preclinical or clinical evidence, such as cell-line or xenograft data on MMAE-mediated activity in HER2-positive breast cancer
- Comparison against the approved HER2-directed antibody-drug conjugates to define any unmet need
- The original approved indication and approved indication text for the Canadian licences, which are missing from the Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

