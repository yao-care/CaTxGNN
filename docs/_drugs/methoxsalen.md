---
layout: default
title: Methoxsalen
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From Unspecified Original Indication to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen (a psoralen photosensitizer) is marketed in Canada as UVADEX, but the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **localized pagetoid reticulosis**, a rare epidermotropic T-cell lymphoma of the skin.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on general pharmacological knowledge rather than the supplied data, methoxsalen is a psoralen. When activated by UVA light, psoralens crosslink DNA and can trigger apoptosis in target cells. This is the basis of psoralen-plus-UVA photochemotherapy (PUVA) and extracorporeal photopheresis (ECP).

Localized pagetoid reticulosis belongs to the mycosis fungoides spectrum, in which malignant T cells sit in the skin. A photoactivated drug that targets skin-homing T cells is a plausible fit, which may explain the very high model score. This link comes from general knowledge, not from evidence supplied for this indication, and it needs a dedicated literature search before any upgrade.

**Related lead:** the second-ranked prediction, *indolent primary cutaneous T-cell lymphoma* (score 99.91%, L3), has two supporting publications on photopheresis in cutaneous T-cell lymphoma. It is closer to confirming an existing use than to true repurposing, and it is the stronger lead to follow.

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
| 2406233 | UVADEX |

Dosage form and approved indication text were not provided for this license.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trials or literature support this indication, so it stays at L5 (model prediction only). The mechanistic link is plausible but unverified.

**To proceed, the following is needed:**
- A targeted literature and trial search for PUVA or photopheresis in localized pagetoid reticulosis
- Health Canada package insert or product monograph review, covering the approved indication and warnings (currently blocking for safety screening)
- Mechanism of action data from DrugBank
- Resolution of the empty original-indication field
- Consideration of prioritizing the indolent primary cutaneous T-cell lymphoma prediction (rank 2), which already has supporting publications

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

