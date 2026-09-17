---
layout: default
title: Mannitol
parent: Moderate Evidence (L3-L4)
nav_order: 486
evidence_level: L4
indication_count: 10
---

# Mannitol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic diuretic with a long history of clinical use for reducing intracranial pressure and promoting diuresis, though formal original-indication and regulatory-label data were not available in this dataset. The TxGNN model predicts a possible link to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, a rare genetic disorder, but this direction is currently supported by only **1 non-specific literature review** and **0 clinical trials**. Given the weak, indirect evidence, the recommended decision at this stage is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (mannitol is generally used as an osmotic diuretic, e.g., for elevated intracranial pressure/oliguria, per supporting evidence text) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for mannitol in this evidence pack. Based on known information referenced in the supporting rationale, mannitol acts as an osmotic diuretic — it theoretically could promote free-water excretion, which is mechanistically relevant to correcting hyponatremia.

NSIAD, however, is a rare hereditary disorder caused by a gain-of-function mutation in the AVPR2 (vasopressin V2) receptor, leading to inappropriate water retention independent of ADH levels. The only literature identified for this pairing is a general review on pitfalls in evaluating hyponatremic patients — it does not specifically discuss mannitol's use in NSIAD. The mechanistic connection (osmotic diuresis → correction of dilutional hyponatremia) is plausible in principle, but there is no direct evidence — clinical, preclinical, or case-based — evaluating mannitol specifically in this rare disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | General review of common pitfalls in diagnosing and managing hyponatremia; does not specifically address mannitol or NSIAD |

---

## Canada Market Information

Mannitol currently has **no authorized products (0 DINs)** in the Canadian market for this dataset; no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.97%), but the supporting evidence is a single non-specific review article with no clinical trials or NSIAD-specific data. NSIAD is also a rare, mechanistically distinct genetic disorder, so extrapolating from mannitol's general diuretic effect carries meaningful uncertainty.

**To proceed, the following is needed:**
- TFDA/Health Canada product label data (warnings and contraindications) — currently a **Blocking** data gap (DG001) preventing safety pre-screening
- Confirmed mechanism of action from DrugBank — currently a **High**-severity gap (DG002) needed for mechanistic-link analysis
- Dedicated case reports, preclinical, or pharmacokinetic studies evaluating mannitol specifically in NSIAD or AVPR2 gain-of-function hyponatremia
- Given the noisy/indirect evidence for several other predicted indications in this pack (e.g., trial data for "acute pulmonary heart disease" is largely unrelated COVID-19/HIV studies), a re-screen of higher-ranked candidates for genuine drug-disease relevance before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

