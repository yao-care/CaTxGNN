---
layout: default
title: Clotrimazole
parent: Moderate Evidence (L3-L4)
nav_order: 215
evidence_level: L4
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Clotrimazole: From Topical Antifungal Use to Acne

## One-Sentence Summary

Clotrimazole is an azole antifungal, widely used for candidiasis and tinea infections. The TxGNN model predicts it may be effective for **acne**, but the support is weak: only **1 clinical trial** (suspended, testing a triple combination) and **no publications** are linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections such as candidiasis and tinea pedis (from the literature; the license records list no indication text) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Clotrimazole is an imidazole antifungal that inhibits ergosterol synthesis in fungi, and its efficacy in fungal skin and mucosal infections is well established.

The link to acne is speculative. It would rest on activity against *Malassezia* yeasts or on anti-inflammatory effects, and neither is supported by direct evidence here. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than a demonstrated mechanism.

The only linked trial tests a fixed combination of a steroid, an antibiotic and clotrimazole. Any effect therefore cannot be attributed to clotrimazole alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1% cream, in patients with contaminated dermatosis with bilateral symmetrical lesions (title mentions acne). No results reported; indirect evidence only. |

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2229378 | CLOTRIMAZOLE VAGINAL 6 |
| 2150859 | CANESTEN COMFORTAB 1 |
| 2229380 | CLOTRIMAZOLE TOPICAL |
| 2462397 | CLOTRIMAZOLE EXTERNAL ANTIFUNGAL CREAM |
| 2264102 | CANESTEN COMBI 1 DAY |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by mechanism or clinical data. The single trial is suspended, has no results, and cannot isolate clotrimazole's contribution. There is no supporting literature.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank, plus evidence of a plausible anti-acne mechanism
- Controlled data on clotrimazole alone in acne

**Note on other predictions:** The rank 2 prediction, **vulvovaginitis**, is much better supported. It has multiple completed trials, including a Phase 3 trial of a clotrimazole ovule versus tablet and Phase 4 trials with clotrimazole as a comparator, plus several RCTs. It is most likely an established use rather than true repurposing, and its assigned decision is Proceed with Guardrails (L2). The rank 3 prediction, postmenopausal atrophic vaginitis, is not mechanistically plausible (L5, Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

