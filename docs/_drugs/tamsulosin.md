---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 874
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Its Marketed Use to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is an alpha-1A/1D adrenergic antagonist marketed in Canada. The Evidence Pack does not record its approved indication.
The TxGNN model ranks **Ambras type hypertrichosis universalis congenita** as its top predicted new use, with a very high graph score.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tamsulosin is known to be an alpha-1A/1D adrenergic antagonist, but its original indication is not recorded, so the prediction cannot be cross-checked against it.

Ambras syndrome is a rare congenital disorder of hair-follicle development. No known pathway connects alpha-1 adrenergic blockade to hair-follicle development. The very high TxGNN score (0.99996) most likely reflects proximity in the knowledge graph, not a pharmacological rationale.

The other top predictions show the same pattern. They are mostly hair and hair-shaft disorders (hypertrichosis, hypotrichosis, alopecia, genetic hair shaft abnormality), plus rare congenital malformation syndromes and migraine with brainstem aura. All are rated L5 with a Hold recommendation, and none has an identified mechanistic link to alpha-1 blockade.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For other candidates, the retrieved literature is only indirect background:
- **Malformation syndrome with odontal and/or periodontal component (rank 3):** 20 publications on periodontitis in general (guidelines, microbiology, diabetes association). None mention tamsulosin.
- **Alopecia (rank 9):** 2 publications. PMID [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) concerns finasteride, a different drug class. PMID [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) reports meibomian gland changes in men with BPH. Neither shows tamsulosin treating hair loss.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2413612 | TAMSULOSIN CR |
| 2427117 | TAMSULOSIN CR |
| 2545179 | AURO-TAMSULOSIN CR |
| 2368242 | TEVA-TAMSULOSIN CR |
| 2319217 | SANDOZ TAMSULOSIN |

Showing 5 of 10 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials, no relevant literature, and no plausible mechanism. It is a graph-based signal only (L5), and the same holds for the other nine predicted indications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data (for example from DrugBank), to enable a cross-check of the prediction
- Any mechanistic or preclinical evidence linking alpha-1 adrenergic blockade to hair-follicle biology, before further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

