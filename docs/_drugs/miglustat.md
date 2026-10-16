---
layout: default
title: Miglustat
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Miglustat: predicted new indication Autosomal ichthyosis syndrome with fatal disease course (evidence level L5). Approved use: Gaucher disease"
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Autosomal Ichthyosis Syndrome with Fatal Disease Course

## One-Sentence Summary

Miglustat is an oral drug originally used for Gaucher disease and Niemann-Pick disease. The TxGNN model predicts it may be effective for **autosomal ichthyosis syndrome with fatal disease course**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease; Niemann-Pick disease |
| Predicted New Indication | Autosomal ichthyosis syndrome with fatal disease course |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Pharmacology data do show that miglustat targets UDP-glucose ceramide glucosyltransferase (glucosylceramide synthase, gene *UGCG*). By inhibiting this enzyme, it reduces the production of glucosylceramide-based glycosphingolipids. This is the basis for its use in Gaucher disease.

The original indications are lysosomal storage disorders, where lipids build up because they cannot be broken down. Ichthyosis syndromes affect the skin barrier, which depends on ceramides and related lipids. A link through glycosphingolipid or ceramide metabolism is conceivable. Reducing glucosylceramide synthesis could in principle influence the lipid balance in the skin.

This link is speculative. The data compiled for this report contain no clinical or literature evidence for this condition. The high score of 0.998 is a computational output only and should not be read as proof of efficacy.

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
| 02456257 | SANDOZ MIGLUSTAT |
| 02556812 | OPFOLDA |
| 02250519 | ZAVESCA |

All three are valid single-ingredient authorizations, with none cancelled.

---

## Safety Considerations

- **Conditions linked to contraindications in the knowledge graph** (these are graph associations, not label text): peripheral nervous system disease, peripheral neuropathy, and impaired renal function disease.
- **Drug Interactions**: Imiglucerase, rated Moderate.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for this condition has the highest model score but no supporting trials or publications, so it remains at the L5 (model prediction only) level. The proposed mechanism is plausible but unproven.

**To proceed, the following is needed:**
- Literature and trial searches specific to ichthyosis syndromes and ceramide or glycosphingolipid pathway biology
- Detailed mechanism of action data and a mechanistic comparison with the original indications
- Package insert warnings and contraindications from Health Canada
- Route and formulation compatibility assessment (oral drug versus skin-targeted disease)

**Additional observation:** Among the other predictions, **Tay-Sachs disease** (rank 7, score 99.75%) has considerably more support. It has 4 registered trials, including small Phase 2 and Phase 3 pharmacokinetic and safety studies and two terminated studies. It also has a randomized controlled study in late-onset Tay-Sachs (PMID 19346952) and a 2023 systematic review of GM2 gangliosidosis (PMID 37209042). This evidence is graded L2 and the stage is "Research Question". The trials are small and clear clinical benefit is not shown, so efficacy outcomes should be confirmed from the full publications. If the aim is to prioritize candidates, Tay-Sachs is the more evidence-supported direction and would merit its own report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

