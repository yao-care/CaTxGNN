---
layout: default
title: Trolamine Salicylate
parent: Model Prediction Only (L5)
nav_order: 945
evidence_level: L5
indication_count: 10
---

# Trolamine Salicylate
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

# Trolamine Salicylate: From Topical Muscle and Joint Pain Relief to Exostosis

## One-Sentence Summary

Trolamine salicylate is a topical salicylate marketed in Canada in creams and rubs for muscle and joint pain relief, based on the product names.
The TxGNN model predicts it may be effective for **exostosis** (a bony outgrowth) with a very high score, but **0 clinical trials** and **0 publications** currently support this prediction.
The prediction rests on the model alone, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence data (product names suggest topical muscle and joint pain relief) |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known drug class, trolamine salicylate is a topical salicylate, and salicylates are generally understood to reduce pain and inflammation by inhibiting cyclooxygenase. Its Canadian products are sold for muscle and joint discomfort.

Exostosis is a bony outgrowth, and the multiple hereditary form is a bone-growth disorder driven by EXT1/EXT2 genes. A topical analgesic is not expected to affect bone formation. The high score most likely reflects network proximity to musculoskeletal terms in the knowledge graph, not a real mechanistic link. The prediction should be treated as a model output only.

Other predictions for this drug have a more plausible fit. Tendinitis and rheumatoid arthritis are consistent with an anti-inflammatory, analgesic action. The rheumatoid arthritis prediction also has one supporting study (see the note in the conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 11 authorizations are listed below. The supplied data does not include dosage form or approved indication text for them.

| DIN | Product Name |
|---------|------|
| 2074702 | EXTRA STRENGTH ASPERCREME CREME RUB 15% |
| 2473143 | MUSCLE & JOINT NO ODOUR REGULAR STRENGTH |
| 2473135 | MUSCLE & JOINT NO ODOUR EXTRA STRENGTH |
| 2226022 | MYOFLEX EXTRA STRENGTH |
| 2358131 | PAIN RELIEF CREAM REGULAR STRENGTH |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The exostosis prediction has a high model score but no clinical trials, no literature, and no plausible mechanism linking a topical salicylate analgesic to bony outgrowth. Evidence is at L5 (model prediction only).

Note: the lower-ranked prediction **rheumatoid arthritis** (score 99.25%, evidence level L4) has one supporting study. It is a 1982 human tissue-absorption study (PMID 6977559) showing that topical triethanolamine salicylate penetrates knee joint tissue. This is indirect pharmacokinetic evidence, not proof of efficacy. It would be a more sensible candidate to pursue than exostosis, as adjunctive symptom relief only.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for any safety screening)
- Mechanism of action data (for example from DrugBank)
- Approved indication text and dosage forms for the Canadian products, to confirm the original indication
- Route compatibility assessment (topical use against any new indication)
- For a more credible direction, such as tendinitis or rheumatoid arthritis, a targeted literature and trial search with clinical efficacy evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

