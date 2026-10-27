---
layout: default
title: Trolamine Salicylate
parent: Model Prediction Only (L5)
nav_order: 952
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Trolamine Salicylate: predicted new indication Exostosis (evidence level L5). Approved use: Not stated in the licence records. Product names suggest topical pain…"
monitor_inn: "TROLAMINE SALICYLATE"
predicted_indications: ["exostosis", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "fibromyalgia", "inclusion body myositis", "exostoses, multiple,", "rheumatoid arthritis", "headache disorder", "gout"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Trolamine Salicylate: From Topical Musculoskeletal Pain Relief to Exostosis
{: .text-alpha }

## One-Sentence Summary

Trolamine salicylate is a topical salicylate marketed in Canada in creams and rubs for muscle, joint and arthritis pain. The TxGNN model predicts it may be effective for **exostosis** (score 99.75%), but **no clinical trials and no publications** were found to support this prediction. It is a model-only signal (evidence level L5), and the most biologically coherent prediction in the list is tendinitis, not exostosis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records. Product names suggest topical pain relief (muscle, joint, arthritis) |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, trolamine salicylate is a topical salicylate with analgesic and anti-inflammatory activity. It is applied to the skin to relieve local musculoskeletal pain.

Such an action could ease pain, but it has no plausible effect on the bony outgrowth that defines exostosis. The high score therefore looks like a model-level association rather than a verified mechanistic link, and similarity to the original indication has not yet been assessed.

**Other predictions from the model** (all with no trials or literature, all evidence level L5, all Hold):

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Tendinitis | 99.70% | Most coherent: symptomatic relief of local musculoskeletal inflammation and pain. This is general pharmacology, not evidence from the data |
| 3 | Myositis fibrosa | 99.65% | At most symptomatic analgesia. Tied score with rank 4 suggests a graph-neighbourhood artifact |
| 4 | Idiopathic granulomatous myositis | 99.65% | Immune-mediated, so topical salicylate is unlikely to address the pathology |
| 5 | Fibromyalgia | 99.59% | Central sensitization, so limited benefit from a topical peripheral analgesic |
| 6 | Inclusion body myositis | 99.46% | Poorly responsive to anti-inflammatory therapy. No disease-modifying role |
| 7 | Exostoses, multiple | 99.43% | Hereditary (EXT1/EXT2). No mechanistic link to salicylates |
| 8 | Rheumatoid arthritis | 99.25% | At best adjunctive relief of localized joint pain. No disease-modifying effect |
| 9 | Headache disorder | 99.23% | Minimal systemic absorption from the topical form, so extrapolation is weak |
| 10 | Gout | 99.18% | Urate effects apply to systemic dosing, not topical use |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02074702 | Extra Strength Aspercreme Creme Rub 15% | Not listed | Not listed |
| 02473143 | Muscle & Joint No Odour Regular Strength | Not listed | Not listed |
| 02473135 | Muscle & Joint No Odour Extra Strength | Not listed | Not listed |
| 02226022 | Myoflex Extra Strength | Not listed | Not listed |
| 02358131 | Pain Relief Cream Regular Strength | Not listed | Not listed |

These are 5 of 11 valid single-ingredient licences. The remaining six are Myoflex Maximum Strength, Pain Relief Cream Extra Strength, Flexacrème Pain Relief Rub, Myoflex Regular Strength, Pain Relief Rub Triethanolamine Salicylate Cream and Arthritis Pain Relief. No licences are cancelled.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications support it, and the mechanism does not plausibly link a topical analgesic to bony outgrowth. Safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism of action data for trolamine salicylate
- A systematic literature and trial-registry search, prioritizing tendinitis as the most plausible candidate and, secondarily, localized joint pain in rheumatoid arthritis
- Approved indication text and dosage forms for the Canadian licences
- Assessment of route compatibility and similarity to the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

