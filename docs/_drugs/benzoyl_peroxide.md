---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
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

# Benzoyl Peroxide: From Acne to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide is a topical agent marketed in Canada mainly in acne-care products. The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **0 clinical trials** and **0 publications** currently support this prediction. It is a graph-based signal only and should be treated as a hypothesis, not a treatment lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (inferred from product names such as acne cleansers and BenzaGel; the licence records contain no indication text) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzoyl peroxide is a topical keratolytic and antibacterial agent. Its efficacy in acne is established, and mechanistically it may be applicable to follicular conditions. However, no mechanistic rationale specific to vulvar inverted follicular keratosis could be identified.

This is a benign follicular lesion of the vulva. The 99.92% score is a graph-based prediction only, with no trials, no literature, and no confirmed original-indication or mechanism data to check it against. A topical keratolytic and antibacterial agent is an unlikely fit for this lesion, so the prediction should not be read as a treatment signal.

The other predictions in the pack are also weak:

- **Acne keloidalis (rank 4, L4):** This is the most plausible direction. It is a folliculitis-related, scarring condition, and benzoyl peroxide's effect on follicular bacteria and its comedolytic activity may help the folliculitis component. There is no direct evidence for scarring outcomes. The one trial and two publications found concern related conditions, not benzoyl peroxide in this disease. It remains a research question.
- **2-Hydroxyethyl methacrylate sensitization (rank 2):** This likely reflects shared chemistry, since benzoyl peroxide is a radical initiator in acrylate systems and a known contact sensitizer. It is a hazard association, not a therapeutic one.
- **Acrodermatitis chronica atrophicans (rank 3):** This is a late Borrelia skin infection. Topical benzoyl peroxide has no established effect on it, and systemic antibiotics are the appropriate care.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Main authorizations (5 of 20 shown). The records contain no dosage form or approved-indication text.

| DIN | Product Name |
|---------|------|
| 2508745 | ACNE FOAMING CLEANSER |
| 2411245 | PROACTIV+ PORE TARGETING SOLUTION |
| 2162121 | BENZAGEL 5 WASH |
| 2236396 | CLEAN & CLEAR PERSA-GEL 5 |
| 2533715 | ACNE FOAMING CLEANSER |

## Safety Considerations

- **Known hazard:** Benzoyl peroxide is a known contact sensitizer. This is noted in the pack's rationale for the sensitization prediction, not in the structured safety fields.

No warnings, contraindications, or drug interactions were retrieved. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, and no plausible mechanistic link to a benign vulvar follicular lesion. Nothing supports moving forward. If any direction is pursued, acne keloidalis is the more credible one, but only as an extrapolation from acne and folliculitis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original indication text from the licence records
- Any clinical or case-level evidence of benzoyl peroxide in vulvar inverted follicular keratosis (or, for the more plausible direction, in acne keloidalis)
- Route and formulation compatibility assessment for vulvar or mucosal-adjacent use, given the sensitization and irritation risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

