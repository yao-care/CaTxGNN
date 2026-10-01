---
layout: default
title: Sonidegib
parent: Model Prediction Only (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: From Advanced Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Sonidegib (Odomzo) is an oral Hedgehog pathway inhibitor, approved for locally advanced basal cell carcinoma (BCC) according to the published literature in this dataset.
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Sonidegib blocks Smoothened (SMO), a key receptor in the Hedgehog signalling pathway. This pathway is abnormally activated in most basal cell carcinomas, which is the basis of sonidegib's use in that cancer. Detailed mechanism-of-action data are not available in the Evidence Pack, so this description comes from the published literature in the dataset.

Medulloblastoma in the SHH (Sonic Hedgehog) subgroup is also driven by this pathway, so the prediction is biologically plausible. Still, no trial or publication in the dataset tests sonidegib in this tumour. The link is a computational prediction only. The "extensive nodularity" subtype also needs confirmation of whether it is SHH-driven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| License Number | Product Name |
|---------|------|
| 2500337 | ODOMZO |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high TxGNN score (99.90%) and a plausible mechanism, but no clinical trials or literature support it (Evidence Level L5). A computational signal alone is not enough to move forward.

**To proceed, the following is needed:**
- Literature and trial searches specific to SHH-subgroup medulloblastoma, including preclinical data and the central nervous system penetration of sonidegib
- Confirmation that the "extensive nodularity" subtype is Hedgehog-driven
- Health Canada package insert warnings and contraindications, which are currently missing and block the safety screen
- Detailed mechanism-of-action data from DrugBank
- Approved indication text, dosage form and route for the Canadian licence

**Note on other predictions:** The sixth-ranked prediction, **skin cancer** (score 99.76%), has much stronger support: a randomized double-blind Phase 2 trial (NCT01327053, n=230) and a 42-month BOLT follow-up. That evidence is specific to BCC and likely overlaps with the existing labelled use, so it may not be true repurposing. It should be reviewed as a separate candidate. The second-ranked prediction, xeroderma pigmentosum, has only a single case report, of sonidegib used for BCCs in that condition.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

