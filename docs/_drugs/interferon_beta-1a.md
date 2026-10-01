---
layout: default
title: Interferon Beta-1A
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1A
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

# Interferon beta-1a: From Multiple Sclerosis to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Interferon beta-1a is an immunomodulatory protein drug, marketed in Canada as REBIF and AVONEX and known from the literature for treating multiple sclerosis.
The TxGNN model predicts it may be effective for **Jeune syndrome situs inversus**, a congenital ciliopathy-type skeletal disorder.
**No clinical trials and no relevant publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (based on the published literature; the Canadian licence records provide no indication text) |
| Predicted New Indication | Jeune syndrome situs inversus |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for interferon beta-1a. Based on general knowledge, the drug acts through immunomodulatory and antiviral signalling.

Jeune syndrome situs inversus is a congenital skeletal disorder of the ciliopathy type. It is not primarily driven by immune dysregulation or viral infection, and **no plausible mechanistic link was identified** between interferon signalling and this disease. The high score (0.975, rank 36,121) most likely reflects knowledge-graph neighbourhood similarity rather than a therapeutic mechanism.

The other nine top-ranked predictions show the same pattern. They include Pierre Robin syndrome, chromosomal deletion syndromes, orofacial clefting, Laubry-Pezzi syndrome, a congenital glycosylation disorder and two ovarian tumours. All are L5 with no supporting trials. The two ovarian tumours have only a speculative link through interferons' antiproliferative activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For transparency, the 20 publications retrieved for the rank-4 candidate (a glycosylation disorder) are also unrelated to that disease. They appear to have been matched on the drug name only and cover multiple sclerosis, COVID-19, COPD exacerbations, ARDS and other topics. They do not support any predicted indication.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02318261 | REBIF |
| 02237319 | REBIF |
| 02318253 | REBIF |
| 02269201 | AVONEX |
| 02237320 | REBIF |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical or mechanistic support. The disease is a congenital ciliopathy-type disorder with no plausible interferon-responsive pathway. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data for interferon beta-1a (for example from DrugBank)
- Health Canada package insert warnings and contraindications, which are required for any safety screening
- Preclinical or mechanistic evidence linking interferon beta signalling to ciliopathy or skeletal-development pathways
- A review of the other nine candidates, which currently have no supporting evidence either. Only the two ovarian tumours have even a speculative link, through interferons' antiproliferative activity

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

