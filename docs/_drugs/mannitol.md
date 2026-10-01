---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic diuretic marketed in Canada as injectable and inhaled products.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and only **1 publication**, a general hyponatremia review that does not study mannitol.
The prediction rests on model output alone and is not supported mechanistically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local licence records (mannitol is an osmotic diuretic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic diuretic. It raises plasma osmolality, pulls water out of tissues and increases urine output.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor. These cause water retention and hyponatremia even when vasopressin levels are low. Mannitol's osmotic load can shift water and could worsen hyponatremia, so a beneficial mechanism is not supported.

The high graph score appears to reflect network proximity between mannitol and related conditions, not a therapeutic rationale. No mannitol-specific clinical evidence for NSIAD was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | Eur J Intern Med | Common pitfalls in evaluating hyponatremia. It covers diagnosis and the risks of under- or over-treatment, and does not assess mannitol. |

---

## Canada Market Information

Five of the 10 authorizations are listed below. The records do not include dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2243176 | MANNITOL INJECTION, USP | — | — |
| 38016 | MANNITOL INJECTION USP | — | — |
| 2489562 | ARIDOL | — | — |
| 60410 | OSMITROL INJECTION 10% | — | — |
| 60437 | OSMITROL INJECTION 20% | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data, and warnings and contraindications from the Health Canada product monograph have not yet been reviewed.

Mannitol's volume expansion has been linked to pulmonary edema in case-level literature. This is relevant to the lower-ranked prediction of acute pulmonary heart disease, not to NSIAD.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no mannitol-specific literature. Mannitol's osmotic action would be expected to aggravate, not treat, the water retention and hyponatremia of NSIAD. The other top-10 predictions are also at evidence level L4–L5. Several are supported only by mannitol's role as an excipient or vehicle (malignant hyperthermia, periodic paralysis), and none shows a therapeutic benefit.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indications), which blocks safety screening
- Mechanism of action data for mannitol from DrugBank
- Any mannitol-specific preclinical or clinical evidence in NSIAD, ideally showing why an osmotic diuretic would not worsen hyponatremia
- A mechanistic review of the predicted candidates, since the current scores appear to reflect graph proximity

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

