---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 870
evidence_level: L5
indication_count: 8
---

# Tadalafil
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

# Tadalafil: From PDE5 Inhibitor Therapy to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor that is marketed in Canada under 20 DINs.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital hair disorder.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records provided (tadalafil is described as a PDE5 inhibitor) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tadalafil is a PDE5 inhibitor, a class that raises cGMP signalling. Ambras syndrome is a congenital genetic disorder of hair growth.

We found no plausible pharmacological link between PDE5 inhibition and this condition. The very high TxGNN score (99.98%) most likely reflects proximity in the knowledge graph to hair-phenotype nodes, not a real mechanism. Without supporting trials or literature, the prediction should be treated as a computational artifact until shown otherwise.

The other top-ranked predictions show the same pattern. Hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly, Dandy-Walker malformation syndromes and a periodontal malformation syndrome all lack a credible mechanism or any supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Tadalafil holds 20 DINs in Canada. Five are shown below. Dosage form and approved indication text are not provided in the records.

| DIN | Product Name |
|---------|------|
| 2410656 | MYLAN-TADALAFIL |
| 2457016 | TADALAFIL |
| 2512289 | PRZ-TADALAFIL |
| 2481405 | AG-TADALAFIL |
| 2455366 | TADALAFIL |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

One signal from the broader prediction list is worth noting. A 2006 case report ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*) linked tadalafil to typical migraine aura without headache. This is a possible adverse-event signal, not a therapeutic benefit. It relates to a lower-ranked prediction (migraine with brainstem aura), not to the lead candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism, so the high model score cannot be turned into a development case. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for tadalafil, followed by a mechanistic-link assessment for hair-growth disorders
- Health Canada product monograph, covering approved indications, warnings and contraindications
- A review of lower-ranked candidates with at least a hypothetical pharmacological basis, such as kyphoscoliotic heart disease via the PAH/cor pulmonale pathway
- A safety review of the migraine aura signal before any further work on neurological indications

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

