---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Midodrine is an oral vasopressor that is marketed in Canada. It is known clinically for treating low blood pressure, although the Evidence Pack does not record its original indication.
The TxGNN model ranks **variably protease-sensitive prionopathy** as its top prediction, but this is a graph-based score only, with **0 clinical trials** and **0 publications** behind it.
The evidence review therefore recommends **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (inferred from general knowledge: orthostatic hypotension) |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Based on known pharmacology, midodrine is a prodrug. Its active metabolite, desglymidodrine, is a selective peripheral alpha-1 adrenergic agonist that raises vascular tone and blood pressure.

**This prediction is not mechanistically plausible.** Variably protease-sensitive prionopathy is a rare prion disease of the brain, and alpha-1 agonism has no known relationship to prion pathology. Midodrine also acts mainly outside the central nervous system. The very high score (0.9999) most likely reflects patterns in the knowledge graph rather than real biology, and no trial or paper supports it.

**A more credible direction exists among the other predictions.** The rank 4 prediction, **hypotensive disorder**, is the only one with substantial evidence. It has 9 linked trials, several of which test midodrine directly. These include post-spinal-anaesthesia hypotension, intradialytic hypotension, and hypotension in heart failure. It also has multiple reviews and one RCT. This is probably an established use of midodrine rather than true repurposing. The empty original-indication field is likely a data gap.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ten licenses are on record. The first five are shown below. The Evidence Pack lists no dosage form or approved-indication text for them.

| DIN | Product Name |
|---------|------|
| 02473984 | MAR-MIDODRINE |
| 02473992 | MAR-MIDODRINE |
| 02517701 | JAMP MIDODRINE |
| 02547112 | M-MIDODRINE |
| 02533219 | MIDODRINE |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

For context, the Evidence Pack notes these general cautions for midodrine:
- **Supine hypertension**
- **Bradycardia**
- **Urinary retention**
- **Caution in heart failure, renal impairment and hepatorenal settings**

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no supporting trials or publications and no plausible mechanism, so it rests on the model score alone (L5). The other top-10 predictions are similarly unsupported, except hypotensive disorder, which is likely an existing use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism-of-action data from DrugBank
- Original indication data for midodrine, to confirm whether hypotensive disorder is an on-label use rather than a repurposing candidate
- If a hypotension-related direction is pursued, verification of which drug was tested in the trials whose arms are unconfirmed (NCT02307565, NCT02893553, NCT01030874, NCT05839652)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

