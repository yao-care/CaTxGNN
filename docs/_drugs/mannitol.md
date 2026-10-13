---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 572
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

# Mannitol: From Intracranial Pressure and Edema Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain edema, intracranial hypertension, ocular hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are currently **no registered clinical trials** and only **1 general review article** behind this prediction, so the prediction is essentially model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain edema, intracranial hypertension, ocular hypertension, congestive heart failure, pseudotumor cerebri, cystic fibrosis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, mannitol is an osmotic diuretic. It is filtered by the kidney but poorly reabsorbed, so it draws water into the urine and pulls fluid out of tissues such as the brain.

Nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations lead to water retention and low blood sodium (hyponatremia). In theory, osmotic diuresis could increase free-water excretion. However, this is not a recognized treatment; fluid restriction and urea are the usual approaches. The one retrieved paper is a general review of pitfalls in evaluating hyponatremia and contains no mannitol-specific evidence. The very high prediction score is therefore not supported by clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in diagnosing and treating hyponatremia. It is general background and does not evaluate mannitol. |

## Canada Market Information

Mannitol holds 10 valid single-ingredient authorizations in Canada. Dosage form and approved indication text are not available for these products. The five main ones are:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243176 | Mannitol Injection, USP | Not available | Not available |
| 00038016 | Mannitol Injection USP | Not available | Not available |
| 02489562 | Aridol | Not available | Not available |
| 00060410 | Osmitrol Injection 10% | Not available | Not available |
| 00060437 | Osmitrol Injection 20% | Not available | Not available |

The remaining five include another Mannitol Injection USP (00038024), Sorbitol Mannitol Irrigation, Cystosol W 3% Hexitols, SAG-M, and an additive solution of sodium, adenine, glucose and mannitol (SAGM).

## Safety Considerations

- **Contraindication signals (from the knowledge graph, not label text):** liver failure and liver disease, hepatic coma and encephalopathy, anuria, impaired renal function, pulmonary edema, intracranial hemorrhage, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anemia, sleep apnea syndromes, substance abuse or dependence, and several anxiety and mood-related disorders. These should be checked against the official package insert.
- **Drug Interactions:** 100 interactions are recorded. Among those listed, the one rated **Major** is **amikacin**. Many are **Moderate**, including lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, desvenlafaxine, canagliflozin, dapagliflozin, cisatracurium, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid, diatrizoate and amifostine. Doxycycline is **Minor**.
- Mannitol's volume-expanding effect may worsen pulmonary edema or heart failure, and in nephrogenic diabetes insipidus its diuretic effect may worsen free-water loss and hypernatremia.

Please also refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. There are no clinical trials, and the single retrieved review is general and not specific to mannitol. Mannitol is also not a recognized treatment for this condition. Other top-ranked predictions (such as malignant hyperthermia and periodic paralysis) show only supportive or incidental use of mannitol, not disease-modifying benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Mechanistic or preclinical evidence that osmotic diuresis improves water handling in AVPR2 gain-of-function disease
- Approved indication text and dosage forms for the Canadian licences
- Expert review of the safety risks, particularly fluid and electrolyte effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

