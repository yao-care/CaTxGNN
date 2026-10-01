---
layout: default
title: Isoprenaline
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 10
---

# Isoprenaline
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

# Isoprenaline: From Its Established Use to Nasal Cavity Disease

## One-Sentence Summary

Isoprenaline (isoproterenol) is a non-selective beta-1/beta-2 adrenergic agonist that is marketed in Canada as an injection.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **0 clinical trials** and **1 publication**, and that publication is an unrelated case report.
This is a model-only prediction with no direct supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in this dataset. Isoprenaline is known as a non-selective beta-1/beta-2 agonist. Beta-2 effects on nasal mucosa (vasoconstriction or decongestion) are conceivable in principle.

No nasal-specific evidence was provided. The only linked paper is a 2003 case report of perioperative ventricular tachycardia and coronary artery spasm in a young man. In that report, the nasal cavity was soaked with epinephrine before nasal intubation. The paper does not evaluate isoprenaline for nasal disease. The high TxGNN score reflects graph-based proximity only, and the mechanistic rationale is speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Case report | Japanese Heart Journal | Perioperative ventricular tachycardia and coronary artery spasm in a 26-year-old man after nasal epinephrine soaking and nasal intubation. Not evidence of isoprenaline efficacy in nasal disease. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2502623 | ISOPROTERENOL HYDROCHLORIDE INJECTION USP |
| 897639 | ISOPROTERENOL HYDROCHLORIDE INJECTION USP |
| 2502615 | ISOPROTERENOL HYDROCHLORIDE INJECTION USP |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The nasal cavity disease prediction has no supporting trials and no relevant literature, so it rests on a graph-based score alone. The only linked paper concerns epinephrine, not isoprenaline. There is also no plausible advantage for an injectable, non-selective beta agonist in nasal disease.

**To proceed, the following is needed:**
- Nasal-specific mechanistic or preclinical evidence for isoprenaline
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Route compatibility assessment (available products are injections only)
- Original approved indication text, which is missing from the licence records

**Other predictions in the pack (for context):**
- **Bronchial disease** (rank 6) has the strongest support, at L3. Multiple 1960s–1970s human studies compared isoprenaline with salbutamol and aminophylline in asthma. This is historical use rather than new repurposing, and beta-2 selective agents largely replaced isoprenaline because of cardiac effects. The one linked trial (NCT02230332) studies alendronate, not isoprenaline.
- **Headache disorder** (rank 2) has old, small, mostly mechanistic evidence, including a 1979 report of inhaled isoproterenol for visual symptoms in migraine. It would need a rationale for agonism rather than blockade.
- **Pharyngitis, acute laryngopharyngitis, endobronchial leiomyoma, endobronchial lipoma, bronchus adenoma, allergic urticaria and trigeminal autonomic cephalalgia** have little or no supporting evidence and no plausible direct mechanism. All are Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

