---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 159
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carvedilol: From Established Cardiovascular Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a non-selective beta-blocker with alpha-1 blocking activity, marketed in Canada as a cardiovascular drug.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records (carvedilol is generally known as an antihypertensive and heart failure drug) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Carvedilol is a non-selective beta-blocker with alpha-1 blockade. Its vasodilatory, blood-pressure-lowering action makes it biologically plausible for severe hypertension.

Renovascular hypertension, however, is driven mainly by activation of the renin-angiotensin system, and carvedilol is not a first-line agent for it. The supplied data contain no trials or literature for this condition. The only support is the prediction score (0.995), so the mechanistic link should be treated as a hypothesis, not established evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Twenty licenses (DINs) are recorded; the five main ones are listed below. The supplied records do not include dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2324520 | CARVEDILOL |
| 2368900 | JAMP-CARVEDILOL |
| 2247935 | APO-CARVEDILOL |
| 2252309 | TEVA-CARVEDILOL |
| 2245914 | PMS-CARVEDILOL |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanistic rationale is weak because renovascular hypertension is primarily renin-angiotensin driven. The other top predictions (malignant hypertensive renal disease, pulmonary hypertension subtypes, Braddock syndrome) are also L5. The two top scores are identical (0.99546), suggesting a shared graph neighborhood rather than independent evidence. The literature returned for the hypoxia-related pulmonary hypertension entry is general hypoxia biology, with nothing on carvedilol.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from the DrugBank API)
- A targeted search for clinical or preclinical evidence on beta-blockers or carvedilol in renovascular or malignant hypertension
- Approved indication text and dosage forms for the Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

