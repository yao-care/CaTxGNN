---
layout: default
title: Metreleptin
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: From Leptin Deficiency in Generalized Lipodystrophy to Familial Generalized Lentiginosis

## One-Sentence Summary

Metreleptin is a recombinant leptin analog, used for leptin deficiency in generalized lipodystrophy.
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**, but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leptin deficiency in generalized lipodystrophy (from general drug knowledge; the Canadian licence records list no indication text) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Metreleptin is a leptin-receptor agonist that replaces missing leptin in people with generalized lipodystrophy. Detailed mechanism-of-action data is not available in the source records, so this description is based on general drug knowledge.

**The mechanistic link is weak to absent.** Lentiginosis is a pigmentary skin disorder with no known involvement of the leptin pathway. The high TxGNN score most likely reflects proximity in the knowledge graph (shared genes or phenotypes) rather than a biological rationale.

The same pattern appears across the top-ranked predictions. Several are rare pigmentary syndromes with near-identical scores, for example acromelanosis and the congenital café-au-lait macules syndrome (both 99.61%). This suggests a shared graph neighbourhood rather than independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2544563 | MYALEPTA |
| 2544555 | MYALEPTA |
| 2544571 | MYALEPTA |

Dosage form and approved-indication text are not listed for these licences.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Lymphoma warning**: The metreleptin label carries a lymphoma warning. Leptin signalling has also been reported to promote proliferation in some cancer models. Both points matter for any new indication, especially the tumour-related predictions on this list (rhabdoid tumor, benign adrenal neoplasm, peripheral nerve schwannoma).

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials, no literature, and no plausible mechanistic link. The full top-10 list for this drug is also at L5 with the same Hold recommendation.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are needed for any safety screening
- Confirmed mechanism-of-action data from DrugBank
- Original approved-indication text from the Canadian licence records
- A credible biological rationale linking leptin signalling to pigmentary disorders, backed by preclinical evidence
- Any published case reports or registered studies, which would move the evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

