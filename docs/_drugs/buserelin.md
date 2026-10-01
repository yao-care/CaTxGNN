---
layout: default
title: Buserelin
parent: Model Prediction Only (L5)
nav_order: 135
evidence_level: L5
indication_count: 5
---

# Buserelin
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

# Buserelin: From a GnRH Agonist (Original Indication Not Recorded) to Hypertrichosis

## One-Sentence Summary

Buserelin is a GnRH agonist that suppresses the pituitary-gonadal axis and lowers sex steroids. It is marketed in Canada as SUPREFACT, but no approved indication text is recorded in the evidence pack.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and only **1 publication**, an unrelated case report that does not mention buserelin.
This is essentially a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available regulatory data |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (the pack lists L4, but its only paper does not involve buserelin, so it does not count as evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Buserelin is a GnRH agonist. It suppresses the pituitary-gonadal axis and lowers sex steroid levels.

**No direct mechanistic link between buserelin and hypertrichosis has been established.** The only related paper describes pituitary hormone deficiencies in Cantu syndrome, a genetic disorder in which hypertrichosis is one feature. It does not test or discuss buserelin for hypertrichosis. Hair growth is influenced by hormones, so an endocrine link is conceivable. However, this is speculation, not supported by any evidence in this pack.

The high score (99.75%, rank 5344) comes from the model's knowledge-graph network patterns alone. It should be treated as a hypothesis-generating signal only.

The other four predictions (Ambras-type hypertrichosis universalis congenita, a malformation syndrome with a dental/periodontal component, a Dandy-Walker malformation syndrome, and an isolated genetic hair shaft abnormality) have no trials and no relevant literature. Most are congenital or genetic conditions with no plausible GnRH-axis mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Case report/Review | Endocrinology, Diabetes & Metabolism Case Reports | A Cantu syndrome patient (hypertrichosis is a syndromic feature) with slowed growth had multiple pituitary hormone deficiencies. The authors recommend endocrine monitoring. Buserelin is not mentioned. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2225166 | SUPREFACT | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, and the single publication is an unrelated case report that does not involve buserelin. No mechanism links a GnRH agonist to hypertrichosis.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism-of-action data from DrugBank to assess a plausible hormonal link to hair growth
- Any evidence (case series, trials, or preclinical data) testing GnRH agonists in hypertrichosis
- Confirmation of the original approved indication and dosage form for SUPREFACT (DIN 2225166)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

