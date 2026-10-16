---
layout: default
title: Dexpanthenol
parent: Model Prediction Only (L5)
nav_order: 271
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Dexpanthenol: predicted new indication Anorectal stricture (evidence level L5). Approved use: Paralytic ileus, intestinal obstruction, gastroparesis, atopic eczema…"
---

# Dexpanthenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Dexpanthenol: From Paralytic Ileus and Skin Disease to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol is a provitamin of pantothenic acid, and in the knowledge graph it is linked to gastrointestinal motility disorders (paralytic ileus, gastroparesis) and skin conditions (dermatitis, eczema, keratosis).
The TxGNN model predicts it may be effective for **anorectal stricture** with a very high score, but no clinical trials or publications currently support this prediction.
The strongest related signal in the data compiled for this report is for a different prediction, **exanthem**, which has **1 Phase 3 clinical trial** (indirect evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paralytic ileus, intestinal obstruction, gastroparesis, atopic eczema, dermatitis, and other skin diseases (from the knowledge graph; Health Canada indication text is not available) |
| Predicted New Indication | Anorectal stricture |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexpanthenol is a provitamin of pantothenic acid (a coenzyme A precursor) and is thought to support epithelial repair, hydration, and wound healing. This is the main basis for its use in skin conditions.

A plausible but unproven link exists to mucosal healing in anorectal tissue. However, the drug's original gastrointestinal indications (paralytic ileus, gastroparesis) concern motility, not fibrotic stricture. The prediction is therefore a model-based hypothesis rather than a mechanism-supported conclusion.

Other top predictions show a similar pattern:
- **Proctitis**: indirect plausibility through mucosal repair and anti-inflammatory properties, with no supporting studies.
- **Vulvar inverted follicular keratosis**: likely reflects overlap with the drug's keratotic skin indications, but this is a benign lesion usually treated by excision.
- **Punctate epithelial keratoconjunctivitis**: dexpanthenol is used in some ophthalmic gels for corneal epithelial healing, giving a plausible link but no data here.
- **Imperforate anus and anal polyp**: structural conditions treated surgically, with no mechanism by which dexpanthenol would address them.
- **Exanthem**: a skin eruption setting that is mechanistically plausible (barrier support, hydration), with one related trial (see below).

---

## Clinical Trial Evidence

No clinical trials are registered for the lead prediction, anorectal stricture. The only trial in the data compiled for this report relates to the sixth-ranked prediction, exanthem:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Randomized, double-blind comparison of Bepanthen® (dexpanthenol) cream versus cetomacrogol cream for preventing papulopustular eruption in patients receiving EGFR inhibitors. The aim was to reduce grade ≥2 skin side effects and support treatment adherence and quality of life. No results were provided. |

This trial studies an EGFR-inhibitor-related skin eruption, not exanthem in general, so it is indirect evidence.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02100606 | MULTI 12 | Not specified | Not specified |
| 02242529 | MULTI-12/K1 PEDIATRIC | Not specified | Not specified |

Both products are valid single-ingredient authorizations.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: Hemophilia is listed as a contraindicated disease in the knowledge graph. This comes from model data, not from label text, and needs verification.
- **Drug Interactions**: No interaction records were found.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (anorectal stricture) rests on a model score alone, with no trials or literature and a mechanism that is plausible but unproven. The only related trial is indirect evidence for a different condition (exanthem), and Health Canada label information is missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indications for both DINs
- Detailed mechanism of action data (MOA)
- A literature search on dexpanthenol in anorectal and mucosal healing, including proctitis
- Results and endpoint details for NCT01136005, if exanthem or skin-reaction prevention is pursued as a research question
- Verification of the hemophilia contraindication signal
- Confirmation of available routes of administration against those required for anorectal use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

