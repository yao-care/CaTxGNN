---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 942
evidence_level: L5
indication_count: 2
---

# Trimethoprim
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

# Trimethoprim: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a bacterial dihydrofolate reductase inhibitor, an antibacterial marketed in Canada as a single agent and in combination products.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**.
However, there are currently **no clinical trials and no publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Trimethoprim is known to inhibit bacterial dihydrofolate reductase, which blocks folate synthesis and gives it antibacterial activity. It is used in combination products such as sulfamethoxazole/trimethoprim and polymyxin B/trimethoprim.

The mechanistic link to this predicted indication is weak. Punctate epithelial keratoconjunctivitis is frequently viral (for example, adenoviral) or immune-mediated, so a direct therapeutic effect from an antibacterial is not plausible. At most, trimethoprim could help with secondary bacterial involvement. The high score is probably driven by proximity in the knowledge graph to bacterial conjunctivitis rather than a true mechanistic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Approved indication text and dosage forms are not available in the source record. Five of the 8 authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 2243116 | Trimethoprim Tablets |
| 2243117 | Trimethoprim Tablets |
| 2525917 | Sulfamethoxazole and Trimethoprim for Injection, USP |
| 445266 | Sulfatrim Pediatric |
| 2239234 | Sandoz Polytrimethoprim |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trials or literature support this indication. The proposed mechanism is also implausible for a condition that is mostly viral or immune-mediated.

**Note on a related prediction:** The second-ranked prediction, **conjunctivitis**, has a score of 99.17%, 3 clinical trials and 20 literature records. The most relevant trial is a completed Phase 4 comparison of polymyxin B/trimethoprim ophthalmic solution with moxifloxacin in bacterial conjunctivitis. It is graded L2 with a "Proceed with Guardrails" recommendation. That use looks closer to an established topical combination use than to novel repurposing, and it merits a separate evaluation.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Approved indication text for each DIN, to confirm on-label status
- Any clinical or observational evidence specific to punctate epithelial keratoconjunctivitis
- Confirmation of route compatibility, since the predicted use would likely require a topical ophthalmic formulation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

