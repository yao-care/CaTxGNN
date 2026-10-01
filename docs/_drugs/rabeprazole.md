---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 781
evidence_level: L5
indication_count: 2
---

# Rabeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Rabeprazole: From Acid-Related Gastric Conditions to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor that suppresses stomach acid. It is generally used for acid-related conditions, although the Canadian licence records provided list no indication text.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, but currently **0 clinical trials** and **0 publications** support this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data. Generally acid-related gastric conditions (general drug-class knowledge) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

A second predicted indication, lymphoadenopathic mastocytosis with eosinophilia (score 99.35%), is also at L5 with a Hold recommendation.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied records. Rabeprazole belongs to the proton pump inhibitor class, which blocks the H+/K+ ATPase in the stomach lining and reduces acid secretion. Its efficacy in acid-related conditions is well established, and mechanistically it may offer indirect benefit in mastocytosis.

In systemic mastocytosis, abnormal mast cells release mediators such as histamine. This can drive excess stomach acid and gastrointestinal symptoms such as reflux, abdominal pain, and ulcers. Suppressing acid could therefore relieve some of these symptoms.

This link is **symptomatic only**. Rabeprazole would not be expected to act on the underlying clonal mast cell disease (for example, KIT-driven proliferation). The same reasoning applies to the second prediction, lymphoadenopathic mastocytosis with eosinophilia: there is no evidence of an effect on lymph node enlargement, eosinophilia, or disease biology. The high TxGNN scores should be read as hypotheses, not clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the eight authorizations are listed below. Dosage form and approved indication text are not provided in the records.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2385449 | RABEPRAZOLE | — | — |
| 2356538 | RABEPRAZOLE EC | — | — |
| 2385457 | RABEPRAZOLE | — | — |
| 2314177 | SANDOZ RABEPRAZOLE | — | — |
| 2356511 | RABEPRAZOLE EC | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. There are no registered trials or publications, and the plausible mechanism is limited to symptomatic acid suppression. It would not treat the underlying mast cell disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- A targeted literature and trial search on proton pump inhibitors in mastocytosis, particularly for GI symptom control
- Approved indication text and dosage forms for the Canadian DINs
- Clinical validation, since the candidate is currently for research reference only and not medical advice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

