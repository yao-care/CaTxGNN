---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 272
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Cough to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a cough suppressant, and the Canadian products on the market are dry cough and cold formulations.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there is currently **no directly relevant clinical trial and no publication** supporting this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough (inferred from product names such as "Dry Cough"; no approved indication text was supplied) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

The source data labels this candidate L4. Under the level rules, L4 requires preclinical or mechanism studies, and none were supplied, so L5 applies.

---

## Why is This Prediction Reasonable?

Dextromethorphan acts centrally as an NMDA receptor antagonist and sigma-1 receptor agonist. It has no established action on nasal mucosa. Detailed mechanism-of-action data were not supplied.

Cough and nasal cavity disease both belong to upper-respiratory symptom clusters, and dextromethorphan is commonly sold in cough and cold products. The TxGNN score is a graph-based prediction. The link to nasal cavity disease is most likely indirect, arising from this symptom overlap rather than from a therapeutic effect on the nasal tissue itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Dextromethorphan + bupropion sustained-release tablets vs placebo in Chinese adults with **major depressive disorder**. This is not a nasal cavity disease trial, and it has no results yet. |

This trial was graded C for relevance. It does not count as direct evidence for the predicted indication.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 1944738 | BENYLIN EXTRA STRENGTH DRY COUGH |
| 2511320 | BUCKLEY'S DRY COUGH EXTRA STRENGTH |
| 2534754 | DRY COUGH RELIEF EXTRA STRENGTH |
| 1928775 | BALMINIL DM (3MG/ML SUCROSE FREE) |
| 2549360 | DAYQUIL KIDS HONEY |

These are 5 of 20 licences. Dosage form and approved indication text were not supplied for them.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. The only registered trial is a depression study unrelated to nasal cavity disease, there is no literature, and no plausible direct mechanism has been shown. The other five predicted indications (acute laryngopharyngitis, faucial diphtheria, trigeminal autonomic cephalalgia, cervical disc degenerative disorder and allergic urticaria) are also L5 with no supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- A literature search for dextromethorphan in nasal and upper-airway conditions
- Approved indication text and dosage forms for the Canadian licences
- Confirmation of the registered conditions in any additional trials relevant to nasal cavity disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

