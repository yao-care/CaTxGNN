---
layout: default
title: Tenapanor
parent: Model Prediction Only (L5)
nav_order: 883
evidence_level: L5
indication_count: 10
---

# Tenapanor
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

# Tenapanor: From an Unrecorded Original Indication to Candidiasis

## One-Sentence Summary

Tenapanor is marketed in Canada as IBSRELA, but the approved indication text is not recorded in the data provided.
The TxGNN model predicts it may be effective for **candidiasis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone, and a clear mechanistic rationale is lacking.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available Canadian licence data |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 97.17% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, tenapanor is a minimally absorbed, gut-restricted inhibitor of the sodium/hydrogen exchanger NHE3. It acts locally on intestinal sodium and phosphate absorption. It has no known antifungal activity.

On this basis, a mechanistic link to candidiasis is **not supported**. The high TxGNN score of 0.972 reflects the structure of the knowledge graph only. No clinical or literature data back it up, so it should be treated as a hypothesis-generating signal, not a finding.

The other top-ranked predictions are equally unsupported, including adrenocortical insufficiency, primary cutaneous T-cell lymphoma, Stevens-Johnson syndrome, and aphthous stomatitis. The most biologically proximate one is **Crohn's colitis** (rank 10, score 94.29%). Even there the link is weak. NHE3 inhibition would be expected to change fluid and electrolyte handling rather than treat inflammation, and it could worsen diarrhoea.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2498049 | IBSRELA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidate is supported only by a graph-based model score. There are no trials or publications, and the known pharmacology of a gut-restricted NHE3 inhibitor offers no plausible link to candidiasis. The score alone does not justify further investment.

**To proceed, the following is needed:**
- Health Canada product monograph (indication, warnings, contraindications), to confirm the original indication and complete the safety screening
- Mechanism of action data from DrugBank to allow a proper mechanistic-link analysis
- A literature review of NHE3 in inflammatory bowel disease, as the first step if Crohn's colitis is pursued
- Any preclinical or clinical evidence linking tenapanor to candidiasis, before reconsidering this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

