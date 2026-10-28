---
layout: default
title: Metreleptin
parent: Model Prediction Only (L5)
nav_order: 610
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Metreleptin: predicted new indication Familial generalized lentiginosis (evidence level L5). Approved use: Berardinelli-Seip congenital lipodystrophy / congenital generalized l…"
monitor_inn: "Metreleptin"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "Moynahan syndrome", "rhabdoid tumor", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "acromelanosis", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "benign neoplasm of adrenal gland", "peripheral nerve schwannoma"]
---

# Metreleptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Metreleptin: From Lipodystrophy to Familial Generalized Lentiginosis
{: .text-alpha }

## One-Sentence Summary

Metreleptin is a recombinant leptin analog, originally used to treat lipodystrophy (including congenital generalized lipodystrophy and Berardinelli-Seip syndrome).
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Berardinelli-Seip congenital lipodystrophy / congenital generalized lipodystrophy / lipodystrophy |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metreleptin is a recombinant analog of leptin that replaces deficient leptin in lipodystrophy, and its use in that condition is established. Mechanistically, there is no clear link to familial generalized lentiginosis.

Lentiginosis is a pigmentary disorder, and leptin signaling has no established role in it. The very high TxGNN score (0.9971) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as lipodystrophy-related syndromes, not biological evidence. The prediction should therefore be treated as a hypothesis-generating signal only.

Other top-ranked predictions show the same pattern. They include gastrocutaneous syndrome, Moynahan syndrome, acromelanosis and several other rare pigmentary or genetic syndromes. None has a documented leptin-related mechanism, and none has clinical trials or literature behind it.

Two predictions, rhabdoid tumor (rank 4) and peripheral nerve schwannoma (rank 10), raise a theoretical safety concern. Leptin signaling has been discussed as pro-proliferative in some cancers, so leptin supplementation could carry risk rather than benefit in tumour settings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02544563 | MYALEPTA | Not specified | Not specified |
| 02544555 | MYALEPTA | Not specified | Not specified |
| 02544571 | MYALEPTA | Not specified | Not specified |

All three authorizations are valid single-ingredient products.

## Safety Considerations

**Drug Interactions**: The interaction screen was completed and returned 100 interacting drugs. The 20 shown in the data compiled for this report are almost all rated Moderate, with one Minor (bortezomib). Examples include:
- Abemaciclib, acalabrutinib, alpelisib, avapritinib, brigatinib, cabozantinib, capmatinib, ceritinib (oncology agents)
- Fentanyl, alfentanil, butorphanol, benzhydrocodone (opioids)
- Ethinylestradiol, norethisterone, desogestrel (hormonal agents)
- Buspirone, cariprazine, bictegravir, chlorpropamide

Interaction details were not available beyond severity level. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or publications. No plausible mechanistic link to familial generalized lentiginosis was identified, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data for metreleptin
- Package insert warnings and contraindications from Health Canada, which is currently a blocking gap for safety screening
- Approved indication text and dosage form for the Canadian authorizations
- A biological rationale connecting leptin signaling to the predicted disease, supported by preclinical or observational evidence
- For the oncology-related predictions, a specific assessment of the theoretical risk from pro-proliferative leptin signaling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

