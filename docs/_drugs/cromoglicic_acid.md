---
layout: default
title: Cromoglicic Acid
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Cromoglicic Acid
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

# Cromoglicic Acid: From Allergic and Mast Cell Conditions to Ulcerative Proctosigmoiditis

## One-Sentence Summary

Cromoglicic acid is a mast cell stabilizer, originally used for asthma, allergic rhinitis, allergic and vernal conjunctivitis, and mastocytosis.
The TxGNN model predicts it may be effective for **ulcerative proctosigmoiditis**,
but **no clinical trials and no relevant publications** currently support this direction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, allergic rhinitis, allergic and vernal conjunctivitis, mastocytosis (from the knowledge graph; no approved indication text was available in the Canadian licence records) |
| Predicted New Indication | Ulcerative proctosigmoiditis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cromoglicic acid is a mast cell stabilizer. Its use in allergic and mast cell-related conditions is established, and mechanistically it may be applicable to inflammation of the distal colon.

The link is plausible but unvalidated. Mast cell activation may contribute to mucosal inflammation in distal ulcerative colitis. Oral absorption of the drug is poor (under 1%), so it could in principle act locally in the gut. However, no trial or literature evidence was compiled to support this, and the high TxGNN score reflects a computational prediction only.

Other candidates in the prediction list include allergic urticaria, which has the strongest mechanistic rationale because urticaria is mast cell and histamine mediated. It is also at evidence level L5 and warrants a systematic literature review. Several other predictions, such as nocardiosis and pneumocystosis, have no plausible mechanism and are likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for ulcerative proctosigmoiditis.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02009277 | CROMOLYN EYE DROPS | Not specified | Not specified |
| 00500895 | NALCROM | Not specified | Not specified |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease edges, not package insert text): liver failure, kidney disease, pyoureter, liver disease, gallbladder disease, nasal cavity polyp.

**Drug Interactions**: The interaction screen returned 100 potential interactions. Only one was rated Moderate: inhaled rapid-acting human insulin. The others listed, including theophylline, valproic acid, tramadol, erythromycin, fluconazole, and citalopram, have an unknown severity level and need further review.

Please refer to the package insert for warnings and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or supporting publications, so it sits at evidence level L5. The mechanistic rationale (mast cell involvement in colonic inflammation) is plausible but unproven, and the drug's poor oral absorption and available dosage forms (eye drops, and the NALCROM product) leave route compatibility unresolved.

**To proceed, the following is needed:**
- A systematic literature search on mast cell stabilizers in ulcerative colitis and proctitis
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada
- Assessment of route and formulation suitability for local colonic delivery
- Review of allergic urticaria as a possibly stronger alternative candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

