---
layout: default
title: Osilodrostat
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
---

# Osilodrostat
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

Using the report template directly (this is a document-generation task from a provided Evidence Pack, not a coding task — no skill applies here).

# Osilodrostat: From Cortisol-Synthesis Inhibition to Familial Generalized Lentiginosis

## One-Sentence Summary

Osilodrostat is a CYP11B1 (11β-hydroxylase) inhibitor that blocks adrenal cortisol synthesis; the evidence pack does not record its approved original indication directly, but its mechanism is consistent with use in endogenous hypercortisolism (e.g. Cushing's disease). The TxGNN model's top-ranked prediction is **familial generalized lentiginosis**, a rare pigmentation disorder with **no clinical trials and no literature** currently supporting the link, and the drug's own repurposing rationale explicitly states there is no known mechanistic connection between cortisol-synthesis inhibition and this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` empty); mechanism (adrenal cortisol synthesis inhibition) is consistent with hypercortisolism/Cushing's disease |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 98.19% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap (DG002, High severity) in this evidence pack. Based on the mechanistic notes attached to the predictions themselves, Osilodrostat is a CYP11B1 (11β-hydroxylase) inhibitor acting on the adrenal cortisol biosynthesis pathway — the pharmacology underlying its known use in cortisol-excess conditions.

Familial generalized lentiginosis is an autosomal pigmentation disorder with no established connection to cortisol synthesis or adrenal steroidogenesis. The evidence pack's own rationale is explicit on this point: the TxGNN score likely reflects proximity through indirect graph nodes (e.g. shared gene-regulation nodes) rather than any pharmacological mechanism.

This pattern repeats across all 10 ranked candidates in this pack (acromelanosis, several rare pigmentary/dysmorphic syndromes, and two oncology diagnoses — rhabdoid tumor and peripheral nerve schwannoma). Every candidate carries an evidence level of L5, decision stage S0, and an explicit "no known mechanistic link" statement. This is a case where the knowledge-graph model surfaced high similarity scores without any corroborating pharmacological, trial, or literature signal — the predictions should be treated as hypothesis-generating only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Osilodrostat is not currently marketed in Canada (0 DINs on file), so no product listing table is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as blocking/unavailable in this evidence pack — DG001, Blocking severity — so no drug-specific safety statements can be made at this time.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support, an explicit absence of mechanistic plausibility per the model's own rationale, and a blocking safety data gap (no TFDA/product-label warnings or contraindications available). Evidence level is L5 — score-only — which does not meet the bar to proceed even under guardrails.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) product label with warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action and original approved indication (DG002)
- Independent mechanistic rationale connecting cortisol-synthesis inhibition to pigmentation disorders, or reprioritization toward a candidate indication with biological plausibility
- If pursued further, consider re-screening the remaining 9 ranked candidates in this pack — all currently share the same L5/Hold status and lack of mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

