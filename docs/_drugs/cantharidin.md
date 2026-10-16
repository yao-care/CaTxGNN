---
layout: default
title: Cantharidin
parent: Model Prediction Only (L5)
nav_order: 152
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Cantharidin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not specified in the Canadian license data"
---

# Cantharidin
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

# Cantharidin: From Topical Dermatologic Use to Amenorrhea

## One-Sentence Summary

Cantharidin is a natural-product vesicant (blistering agent) that is used topically for skin conditions such as warts and molluscum contagiosum. The TxGNN model predicts it may be relevant to **amenorrhea**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data (the topical use for warts and molluscum contagiosum comes from pharmacology reference data) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for the original indication is not currently available. Based on the pharmacology data compiled for this report, cantharidin inhibits protein phosphatase 2A (PPP2CA) and protein phosphatase 1 (PPP1CA). Inhibition of these enzymes is thought to disrupt cell-to-cell connections in the skin, which produces blistering. The same pathway has been linked to its anticancer activity in laboratory reports.

No plausible link has been established between these mechanisms and amenorrhea. Nothing in the data connects cantharidin to the hypothalamic-pituitary-ovarian axis or to uterine and endometrial physiology. Systemic cantharidin is also highly toxic, with renal, gastrointestinal and genitourinary irritation, which is a serious concern for any systemic use.

The high score (0.994) reflects a pattern in the knowledge graph, not clinical evidence. The prediction should be treated as hypothesis-generating only.

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
| 00772011 | CANTHARONE PLUS | Not specified | Not specified |

---

## Safety Considerations

- **Drug Targets (pharmacology data)**: Cantharidin inhibits protein phosphatase 2 catalytic subunit alpha (PPP2CA) and protein phosphatase 1 catalytic subunit alpha (PPP1CA). These are target interactions, not classified drug–drug interactions, and no severity level is assigned.
- **Systemic toxicity**: Systemic exposure is associated with renal, gastrointestinal and genitourinary irritation. This comes from the expert assessment in this report, not from label text.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and no mechanistic link to amenorrhea. The known systemic toxicity of cantharidin adds a significant safety concern.

**To proceed, the following is needed:**
- The Health Canada package insert, to obtain warnings, contraindications and the approved indication of CANTHARONE PLUS
- Mechanism of action data from DrugBank
- A literature search and a preclinical rationale linking PP2A/PP1 inhibition to reproductive physiology
- A route and dosage form compatibility assessment, since the available product's route is unknown and systemic exposure carries toxicity risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

