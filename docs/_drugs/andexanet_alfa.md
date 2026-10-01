---
layout: default
title: Andexanet Alfa
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant antidote that neutralizes factor Xa (FXa) inhibitor anticoagulants. The TxGNN model predicts it may be useful for **Glanzmann thrombasthenia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data. Andexanet alfa is known as a reversal agent for FXa inhibitors. |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, curated mechanism of action data is not available in the Evidence Pack. Based on the pack's rationale text, andexanet alfa is a recombinant, catalytically inactive FXa decoy. It binds and neutralizes FXa inhibitors, which restores the activity of the coagulation cascade.

Glanzmann thrombasthenia is an inherited platelet aggregation defect. It is caused by deficient or dysfunctional GPIIb/IIIa (integrin alphaIIb-beta3). Andexanet alfa acts on the coagulation cascade, not on platelet function, so **no plausible mechanistic link was identified**. The high TxGNN score (0.998) is a knowledge-graph prediction only. No trial or publication backs it up, and the original MOA field is empty, so the prediction cannot be cross-checked.

Other predicted indications show the same pattern:
- **Primary release disorder of platelets** (99.76%): a platelet granule secretion defect, and andexanet has no known effect on it.
- **Pseudo-von Willebrand disease** (99.65%): a GPIb-alpha gain-of-function defect, and andexanet does not act on the GPIb-VWF axis.
- **Hemophilia** (99.10%): 10 publications were retrieved, but none evaluates andexanet as a hemophilia treatment. They cover anticoagulant-associated bleeding, DOAC interference in FVIII/FIX assays, and reviews of reversal agents. One speculative, unverified angle is that andexanet has been reported to bind TFPI, which is a validated hemostatic target in hemophilia. It would need dedicated preclinical work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Glanzmann thrombasthenia.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2538539 | ONDEXXYA |

---

## Safety Considerations

- **Key Warnings**: Thromboembolic risk. This weighs against advancing the drug into conditions where it has no clear rationale.

Please refer to the package insert for the full set of warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. It has no clinical or literature support and no plausible mechanistic link to platelet-function disorders. The thromboembolic risk warning further argues against advancing without a clear rationale.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Curated mechanism of action data (for example from DrugBank)
- Preclinical evidence of an effect on platelet function or hemostasis in the target disease (for example the TFPI-binding hypothesis for hemophilia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

