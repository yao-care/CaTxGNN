---
layout: default
title: Thyroid Porcine
parent: Model Prediction Only (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Thyroid Porcine
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

# Thyroid, porcine: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Porcine thyroid is a desiccated animal thyroid preparation supplying thyroid hormones (T4/T3), but no original indication is recorded in the source data.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (the license entries contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Porcine thyroid is a desiccated thyroid preparation containing T4 and T3, and its presumed role is thyroid hormone replacement. The source data does not document any original indication or mechanism, and no mechanistic link to migraine has been identified. The very high score (99.91%) comes from the knowledge-graph model alone, and no trials or literature back it.

The other top-ranked predictions are also unsupported by clinical evidence:

- **Migraine with brainstem aura** and **migraine with or without aura, susceptibility to**: These are probably neighbours of the generic migraine prediction in the knowledge graph. The 20 papers retrieved for the susceptibility term cover epilepsy and migraine genetics. None studies thyroid hormone or porcine thyroid as an intervention.
- **Raynaud disease**: The only link is speculative. Untreated hypothyroidism can cause cold intolerance, so replacement would correct a coexisting deficiency rather than treat Raynaud itself.
- **Atrophoderma vermiculata** and **ulerythema ophryogenesis**: These are rare follicular skin disorders with no known thyroid-hormone pathway, likely knowledge-graph artifacts.
- **Prinzmetal angina**: Thyroid hormone raises cardiac oxygen demand and heart rate, so a safety concern is more plausible than a benefit.
- **Sciatic neuropathy** and **lesion of sciatic nerve**: No documented link to thyroid replacement. Hypothyroid neuropathy is a different entity.
- **Hyperthyroidism**: This is pharmacologically contradictory, because exogenous T4/T3 would worsen it. The retrieved papers use porcine thyroid tissue only as an assay reagent or are animal models, and none tests the drug as a treatment.

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
| 23949 | THYROID |
| 23957 | THYROID |
| 23965 | THYROID |

Dosage form, manufacturer and approved indication text are not available for these authorizations.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for safety information.

Note: the prediction notes point to cardiac risk with thyroid preparations in patients with coronary disease, and to iatrogenic thyrotoxicosis on overdose. These come from the pharmacological reasoning in the evidence pack, not from label text.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a model score alone, with no trials, no literature, no documented mechanism and no recorded original indication. Several other top predictions are implausible or contradictory, such as hyperthyroidism, which suggests the high scores reflect knowledge-graph artifacts rather than therapeutic signal.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications), which is required before any safety screening
- Mechanism of action data from DrugBank, to assess whether any thyroid-hormone link to migraine is plausible
- A targeted literature search on thyroid hormone or thyroid status and migraine
- A review of whether a more clinically coherent candidate exists among the predictions, for example thyroid-related indications, before investing further in migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

