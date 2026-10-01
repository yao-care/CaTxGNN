---
layout: default
title: Icodextrin
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Icodextrin
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

# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a high-molecular-weight glucose polymer used as an osmotic agent in peritoneal dialysis.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal (Evidence Level L5) and should not be read as clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritoneal dialysis (osmotic agent; the Canadian licence record contains no indication text) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, icodextrin is a glucose polymer that acts as an osmotic agent in peritoneal dialysis solutions, which are used in patients with kidney failure. No plausible mechanism linking it to irritable bowel syndrome (IBS) can be established from the data provided.

The high TxGNN score (0.985) reflects the model's knowledge-graph patterns, not biological or clinical evidence. Peritoneal dialysis and IBS are pharmacologically unrelated, and no trials or literature were found.

The other nine top predictions have the same weakness:
- Several are structurally unrelated to a dialysis osmotic agent, such as non-syndromic esophageal malformation, familial visceral myopathy and renal tubular acidosis.
- Three overlap in the same disease family: C1 inhibitor deficiency, hereditary angioedema with C1Inh deficiency and serpinopathy. Their scores are likely not independent, because they share a graph neighbourhood.
- Two overlap in the esophagus: esophageal disease and non-syndromic esophageal malformation.

Overall, the candidate list looks driven by graph topology rather than pharmacology.

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
| 2240806 | EXTRANEAL |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no identifiable mechanism. The score should not be treated as clinical support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for icodextrin (e.g., from DrugBank), followed by a mechanistic assessment against IBS
- A literature and trial search specific to icodextrin and IBS
- The approved indication text and dosage form for DIN 2240806
- Route compatibility assessment: icodextrin is a peritoneal dialysis solution, and any IBS use would need a de novo route and formulation rationale

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

