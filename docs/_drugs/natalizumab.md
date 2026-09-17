---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody whose approved use — based on the recurring clinical context in the literature evidence gathered here — is relapsing-remitting multiple sclerosis; a formal original-indication record was not provided in this evidence pack. The TxGNN model's top-ranked prediction is **Bronchitis**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale argues against biological plausibility. (Note: this evidence pack scored 5 candidate indications for natalizumab in total — bronchitis, parapsoriasis, psoriasis, severe nonproliferative diabetic retinopathy, and acute lichenoid pityriasis — and every one of them received a **Hold** recommendation.)

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (`original_indications` empty); literature context repeatedly references relapsing-remitting multiple sclerosis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for natalizumab was not available in this evidence pack. Based on the literature context surfaced during evidence collection, natalizumab is an anti-α4-integrin (VLA-4/α4β7) monoclonal antibody that blocks leukocyte migration across the blood–brain barrier and gut mucosa — a systemic immunosuppressive mechanism, historically used for autoimmune/inflammatory conditions such as multiple sclerosis.

For the top-ranked prediction, **bronchitis**, this mechanism does not translate favorably. Bronchitis is predominantly infectious or irritant in etiology, and the model's own rationale is explicit: there is no clinical trial or literature evidence linking natalizumab to bronchitis, the immune-suppressive mechanism runs counter to what would be needed to treat an infection-driven airway condition, and systemic immunosuppression could plausibly *increase* the risk of infectious bronchitis rather than treat it. The TxGNN score here reflects a statistical association in the model's embedding space, not a validated pharmacological hypothesis.

It is also worth noting that the richest body of evidence in this pack (19 PubMed records) concerns a different candidate, **psoriasis** — but that evidence is predominantly case reports of natalizumab *inducing or aggravating* psoriasiform reactions (a paradoxical inflammatory adverse effect), plus a substantial cluster of reviews on progressive multifocal leukoencephalopathy (PML) risk. Only one case series reported psoriasis *improvement*. This is a safety signal, not a repurposing opportunity, and reinforces that none of the five candidates in this pack currently supports a "Go" pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Structured safety fields for warnings, contraindications, and drug interactions were not populated in this evidence pack. Separately, literature gathered while evaluating other candidate indications — not part of the formal safety dataset — repeatedly flagged progressive multifocal leukoencephalopathy (PML) as a known risk associated with natalizumab, and multiple case reports described treatment-emergent/aggravated psoriasis. These are noted here for context but should be confirmed against the official product label before any clinical use.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (bronchitis) has zero supporting clinical trials or literature, and the mechanistic rationale itself argues against plausibility — this is an L5, model-only signal. No other candidate in this evidence pack (parapsoriasis, psoriasis, diabetic retinopathy, acute lichenoid pityriasis) fared better; several are actually adverse-event signals rather than efficacy signals.

**To proceed, the following is needed:**
- TFDA-equivalent product label / warnings and contraindications (currently a Blocking data gap per this pack)
- Confirmed mechanism of action and approved original indication (currently a High-severity data gap)
- If any candidate is pursued further, primary clinical evidence (trials or controlled studies) specific to that indication — none currently exists for bronchitis
- Clarification on whether the psoriasis-related literature represents a safety exclusion criterion rather than a repurposing lead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

