---
layout: default
title: Amcinonide
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 8
---

# Amcinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amcinonide: From Topical Corticosteroid Use to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Amcinonide is a topical corticosteroid marketed in Canada. The supplied data do not list its original approved indication.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone and should be treated as a low-confidence hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general class knowledge, amcinonide is a topical corticosteroid, and drugs in this class act through anti-inflammatory and immunosuppressive effects. This reasoning does not come from the supplied data.

The link to the predicted indication is weak. Vulvar inverted follicular keratosis is a benign keratinocytic lesion that is normally treated by excision, and an anti-inflammatory steroid has no clear disease-directed role in it. The high score (rank 4185) may reflect knowledge-graph proximity to dermatologic terms rather than a true therapeutic signal.

Other TxGNN predictions for this drug fit the corticosteroid mechanism better, though they have no supporting evidence either:
- **Lichen planus variants** (hypertrophic, pigmentosus, annular atrophic, pemphigoides; scores 99.6–99.7%): T-cell-mediated inflammatory conditions where potent topical steroids are plausible. The identical scores across variants suggest shared graph neighbours rather than variant-specific signal.
- **Dermatitis** (99.3%): a strong mechanistic fit, but it may already be a labelled use that is missing from the dataset. The label should be checked first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2246714 | TARO-AMCINONIDE | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score, with no trials or publications. Its mechanistic link is weak for a benign lesion normally managed by excision, so there is no basis to advance it.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indications, dosage form), which blocks safety screening
- Mechanism of action data from DrugBank
- Confirmation of the original labelled indications, to separate true repurposing from existing labelled use
- Any clinical or observational evidence for the predicted indication
- Consideration of the lichen planus variants and dermatitis as better-supported research questions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

