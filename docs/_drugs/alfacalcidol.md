---
layout: default
title: Alfacalcidol
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
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

# Alfacalcidol: From Approved Vitamin D Analogue Use to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Alfacalcidol is a vitamin D analogue (a 1-alpha-hydroxylated vitamin D prodrug) that is marketed in Canada.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**.
So far there are **0 clinical trials** and **0 publications** for this specific prediction, so it rests on the model score and general pharmacology alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, alfacalcidol is a vitamin D prodrug that is activated in the liver and bypasses renal 1-alpha-hydroxylase. Its active metabolite could therefore act as a vitamin D replacement.

In familial isolated hypoparathyroidism, PTH secretion is impaired, so PTH-driven calcitriol production is lost and serum calcium falls. An already-activated vitamin D form could plausibly replace the missing calcitriol and raise serum calcium. This is biologically plausible, but it is inference rather than demonstrated evidence. The submitted data contain no trials or literature for this disease, and the original mechanism-of-action field is empty.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

## Other Predicted Indications

Other predictions in the pack are weaker or unsupported, except renal tubular acidosis.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Dahlberg-Borer-Newcomer syndrome | 99.60% | L5 | No mechanistic rationale, no evidence, very rare disease |
| 3 | Craniofacial conodysplasia | 99.55% | L5 | No clear link to vitamin D or calcium homeostasis, graph-based output only |
| 4 | Acromesomelic dysplasia, Campailla Martinelli type | 99.53% | L5 | Genetic skeletal dysplasia with no known vitamin D pathway, likely a graph artifact |
| 5 | Renal tubular acidosis | 99.27% | L4 | 8 publications, mostly single-patient case reports |

**Renal tubular acidosis (rank 5)** has the strongest supporting evidence in this pack. The published items are mostly case reports, with one small 1980 clinical series in Fanconi syndrome (PMID 6893175). Examples include:

- [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) (2013, Modern Rheumatology): Osteomalacia due to RTA with Sjögren's syndrome resolved after treatment with bicarbonate, risedronate, alfacalcidol and prednisolone.
- [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) (2001, Internal Medicine): Rapid improvement of osteomalacia in a patient with RTA type 1 after alkali plus alfacalcidol-based therapy.
- [6893175](https://pubmed.ncbi.nlm.nih.gov/6893175/) (1980, Contributions to Nephrology): In Fanconi syndrome, 1-alpha-OH-vitamin D3 raised low plasma 1,25-(OH)2 vitamin D3 rapidly.

The signal concerns managing complications (osteomalacia, hypophosphatemia), not correcting the tubular acidification defect. Alfacalcidol was given alongside alkali and phosphate therapy, so its independent contribution cannot be separated.

## Canada Market Information

Six authorizations are recorded; five are listed below. Dosage form and approved indication text are not available in the supplied data.

| DIN | Product Name |
|---------|------|
| 2533324 | SANDOZ ALFACALCIDOL |
| 2240329 | ONE-ALPHA |
| 474525 | ONE-ALPHA |
| 474517 | ONE-ALPHA |
| 2242502 | ONE-ALPHA |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.
- **Renal tubular acidosis context**: Hypercalciuria and nephrocalcinosis need monitoring, since RTA already predisposes to them.

For warnings and contraindications, please refer to the Health Canada package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction scores very high (99.61%) but is evidence level L5, with no trials and no literature for familial isolated hypoparathyroidism. The mechanistic argument is plausible but rests on general pharmacology. Renal tubular acidosis has more published support, but that support is limited to case reports.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- A targeted literature and trial search for alfacalcidol in hypoparathyroidism, including PTH-deficient forms
- Approved indication text and dosage forms for the Canadian DINs, to confirm the original indication and route compatibility
- For renal tubular acidosis, a review of whether alfacalcidol contributes independently of alkali and phosphate therapy, plus a hypercalciuria and nephrocalcinosis monitoring plan

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

