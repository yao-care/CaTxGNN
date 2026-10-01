---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 193
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Cimetidine: From Acid-Related Gastric Conditions to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is an H2 receptor antagonist that reduces stomach acid, and it is best known for ulcer-type conditions.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**,
but currently **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian licence records (acid-related gastric conditions inferred from drug class) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cimetidine belongs to the H2 receptor antagonist class. Its efficacy in acid-related gastric disease is well established, and mechanistically it may be applicable to mast cell disease.

Mastocytosis involves excess mast cells that release histamine. Histamine drives gastric acid hypersecretion and gastrointestinal symptoms such as pain and reflux. Blocking H2 receptors could therefore ease these symptoms.

This would be symptom control, not disease modification. Nothing in the supplied data shows that cimetidine changes the course of smouldering systemic mastocytosis. The prediction is likely driven by shared mast cell and histamine biology, and no clinical data back it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 584215 | CIMETIDINE |
| 487872 | CIMETIDINE |

Dosage form and approved indication text were not available for these two licences.

---

## Safety Considerations

- **Drug Interactions**: The interaction database returned no records for cimetidine, which is probably a data gap rather than proof of no interactions. Separate pharmacokinetic studies in the wider literature report that cimetidine raised blood levels of proguanil and mefloquine (PMIDs 10701981, 11420885), which fits its known inhibition of drug metabolism.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (99.80%) but no supporting trials or publications. At best, the mechanism would give symptom relief, not disease control.

**To proceed, the following is needed:**
- A targeted literature search on H2 blockers, including cimetidine, in mastocytosis
- Mechanism of action data from DrugBank
- The Health Canada package insert (warnings, contraindications, labeled indications)
- A complete drug interaction check, since cimetidine is a known inhibitor of drug metabolism
- A clear clinical question: symptom control in mast cell patients, or a disease-modifying claim (no evidence supplied)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

