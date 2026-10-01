---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 858
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sotalol: From Arrhythmia Management to Sick Sinus Syndrome 2 (Autosomal Dominant)

## One-Sentence Summary

Sotalol is a beta-blocker with class III antiarrhythmic activity, used for heart rhythm control.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** currently support this prediction.
The pharmacology points the other way, because sick sinus syndrome is a recognized bradycardia-related contraindication for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arrhythmia management (the Canadian licence records contain no indication text, so this is inferred from the drug's pharmacology) |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Based on known pharmacology, sotalol combines beta-adrenergic blockade with class III (potassium channel-blocking) activity. Together these slow the sinus rate and AV conduction.

Sick sinus syndrome is a disorder of sinus node function, and it is closely tied to slow heart rates. A drug that further slows the sinus rate would be expected to worsen the condition rather than treat it. Sotalol is used to control abnormal rhythms, but sick sinus syndrome is a recognized bradycardia-related contraindication. The pharmacology therefore argues against benefit.

The high TxGNN score most likely reflects the structure of the knowledge graph, not a real mechanistic link. We consider this prediction a probable graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2210428 | APO-SOTALOL |
| 2167794 | APO-SOTALOL |
| 2238326 | PMS-SOTALOL - 80 MG |
| 2238327 | PMS-SOTALOL - 160 MG |

---

## Safety Considerations

- **Bradycardia-related contraindication**: Sick sinus syndrome is a recognized bradycardia-related contraindication for sotalol, so using it for this condition carries a direct safety concern.
- **Proarrhythmic risk**: As a class III antiarrhythmic, sotalol carries QT prolongation and torsades de pointes risk, which would need evaluation in any new population.

No drug interaction records were found. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature. Sotalol's pharmacology (slowing of the sinus rate and AV conduction) argues against benefit in sick sinus syndrome.

**To proceed, the following is needed:**
- Mechanism-of-action data (MOA) to support or refute any mechanistic link
- Health Canada package insert warnings and contraindications
- Any clinical or genetic evidence that sotalol benefits this specific autosomal dominant form (none has been identified)

**Other candidates for this drug:**
Among the other predicted indications, **stroke disorder** (rank 4) has the most supporting material: 24 retrieved trials and 20 publications, rated L4 with a "Research Question" recommendation. The link is indirect, since sotalol is used for rhythm control in atrial fibrillation, a major stroke risk factor. No retrieved trial tests stroke prevention with sotalol, and anticoagulation remains the established strategy. It is better evaluated as its own report than under this entry.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

