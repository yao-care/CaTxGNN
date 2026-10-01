---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Severe Acne to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is a retinoid marketed in Canada under several brand names. The approved indication text was not supplied in the Evidence Pack, so its usual use, severe acne, is general knowledge and not taken from the pack.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (commonly severe recalcitrant acne, per general knowledge) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack, and the approved indication text for the Canadian licences is blank. No mechanistic link can be confirmed from the supplied data. The high TxGNN score (99.01%) reflects a knowledge-graph signal only.

One speculative link is that retinoid signalling may influence renin expression in preclinical settings. No evidence in this pack supports it, so it should be treated as a hypothesis to test, not a rationale.

A second prediction, **malignant hypertensive renal disease**, has an identical score (99.01%) and probably reflects the same or an overlapping knowledge-graph signal. It should not count as independent support. Both diseases sit in the malignant hypertension cluster and should be reviewed together.

Isotretinoin is not an established treatment for renovascular hypertension. Its known safety profile, including teratogenicity and lipid effects, would need careful review before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 12 authorisations are listed below. Dosage form and approved-indication text were not provided for any of them.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02396998 | EPURIS | Not listed | Not listed |
| 02257955 | CLARUS | Not listed | Not listed |
| 02257963 | CLARUS | Not listed | Not listed |
| 02539071 | ABSORICA LD | Not listed | Not listed |
| 00582344 | ACCUTANE | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. The Health Canada package insert warnings and contraindications have not yet been reviewed, and this must be done before any safety screening. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials, no publications, and no confirmed mechanism. The two predicted diseases are effectively one signal, and the known safety profile of isotretinoin raises concerns for any new use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- The approved indication text and dosage forms for the Canadian licences
- Mechanism of action data, to test whether retinoid effects on renin or vascular pathways are plausible
- A targeted literature and trial search for retinoids in renovascular or malignant hypertension
- A safety review of teratogenicity and lipid effects against the proposed patient population

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

