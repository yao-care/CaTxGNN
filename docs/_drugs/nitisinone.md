---
layout: default
title: Nitisinone
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Tyrosinemia to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone was originally used to treat hereditary tyrosinemia.
The TxGNN model predicts it may be effective for **renal tubular acidosis** (score 99.96%), but **no clinical trials and no publications** currently support this specific prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tyrosinemia (from the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general knowledge, nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), an enzyme in the tyrosine breakdown pathway. Blocking it prevents the build-up of toxic upstream metabolites such as succinylacetone.

In hereditary tyrosinemia type 1, these toxic metabolites are thought to cause kidney tubular damage (a Fanconi-type proximal tubulopathy). Nitisinone may therefore improve this *secondary* tubular dysfunction. However, this is not a mechanism for primary renal tubular acidosis, and no direct link has been established. The very high TxGNN score is a computational prediction only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for renal tubular acidosis.

For context, the second-ranked prediction (galactosemia) and the fifth-ranked prediction (glycogen storage disease) retrieved only general reviews of paediatric liver disease. These discuss the conditions side by side and do not show that nitisinone treats them.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02469693 | ORFADIN | Not specified | Not specified |
| 02457733 | MDK-NITISINONE | Not specified | Not specified |
| 02459728 | ORFADIN | Not specified | Not specified |
| 02457725 | MDK-NITISINONE | Not specified | Not specified |
| 02459698 | ORFADIN | Not specified | Not specified |

Eight single-ingredient licences are currently valid (none cancelled). Only the first five are listed above.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): kidney disease, pyoureter, thrombocytopenia, leukopenia, hypophosphatemia, tyrosinemia. These should be verified against the official product monograph.
- **Drug Interactions**: The interaction screen returned 100 potential interactions, mostly of Moderate severity. Examples include abiraterone, amiodarone, amlodipine, nifedipine, ibuprofen, isotretinoin, dexamethasone, pioglitazone, aprepitant, atazanavir, bicalutamide and apalutamide. Armodafinil is rated Minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. The only plausible biology is relief of secondary tubular injury in tyrosinemia type 1, not primary renal tubular acidosis. Nitisinone's kidney-related contraindication signals add further caution.

**To proceed, the following is needed:**
- Official Health Canada product monograph warnings and contraindications
- Confirmed mechanism of action data
- Preclinical or clinical evidence in renal tubular acidosis, or clear separation of primary from secondary forms
- A defined target population and a safety plan that accounts for kidney and blood-count signals
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

