---
layout: default
title: Triheptanoin
parent: Model Prediction Only (L5)
nav_order: 946
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Triheptanoin: predicted new indication Craniostenosis cataract (evidence level L5). Approved use: Not stated in the Canadian license data (the mechanistic background s…"
monitor_inn: "Triheptanoin"
predicted_indications: ["craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "immature cataract", "tetanic cataract", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "antithrombin deficiency type 2"]
---

# Triheptanoin
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

# Triheptanoin: From Long-Chain Fatty Acid Oxidation Disorders to Craniostenosis Cataract

## One-Sentence Summary

Triheptanoin is a medium odd-chain triglyceride (C7) that supplies heptanoate as an energy substrate, and it is marketed in Canada as DOJOLVI. The TxGNN model predicts it may be effective for **craniostenosis cataract**, but **no clinical trials and no publications** currently support this prediction. It rests on a model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (the mechanistic background suggests long-chain fatty acid oxidation disorders) |
| Predicted New Indication | Craniostenosis cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, triheptanoin supplies heptanoate, which is converted to propionyl-CoA and then succinyl-CoA. This replenishes intermediates of the TCA cycle (anaplerosis). It is marketed for long-chain fatty acid oxidation disorders, where cells have difficulty producing energy from long-chain fats.

The link to the predicted indication is weak. No plausible pathway was identified that connects anaplerotic energy-substrate supply to cataract associated with craniosynostosis. The score of 99.98% is a knowledge-graph prediction. It likely reflects shared network neighbours across the cataract disease family rather than a specific mechanism.

The model also ranks many other cataract types highly, including diabetic, senile, nuclear, cortical, mature, immature and tetanic cataract. Diabetic cataract involves altered lens energy metabolism, so a theoretical argument exists there, but it is untested. No data are available on lens exposure after an oral triglyceride.

Other predicted indications:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Diabetes mellitus type 2 associated cataract | 99.98% | L5 | Speculative link through lens energy metabolism |
| 3 | Mature cataract | 99.98% | L5 | Advanced structural opacity, surgically treated |
| 4 | Immature cataract | 99.98% | L5 | Untested theoretical argument |
| 5 | Tetanic cataract | 99.98% | L5 | Driven by calcium disturbance, no link |
| 6 | Diabetic cataract | 99.97% | L5 | Overlaps with rank 2 |
| 7 | Cortical cataract | 99.97% | L5 | Ion and water balance, no link |
| 8 | Nuclear senile cataract | 99.97% | L5 | Speculative |
| 9 | Senile cataract | 99.97% | L5 | Likely family-level artefact |
| 10 | Antithrombin deficiency type 2 | 99.97% | L5 | No interaction with the coagulation cascade |

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
| 02512556 | DOJOLVI | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: One interaction was identified in the compiled data: **Orlistat** (Major severity, DDInter). Orlistat reduces fat absorption, so it may interfere with absorption of a triglyceride product. Co-administration should be avoided or reviewed carefully.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, no publications and no plausible mechanism linking triheptanoin to craniosynostosis-associated cataract or to any other cataract type. Ocular delivery of an oral triglyceride is also unaddressed.

**To proceed, the following is needed:**
- Mechanism of action data for triheptanoin, to allow a proper mechanistic analysis
- Preclinical evidence (for example, lens culture or animal cataract models) showing a benefit of anaplerotic substrate supply
- Evidence of lens exposure or another rationale for ocular benefit after oral dosing
- The Health Canada package insert, to review the approved indication, warnings and contraindications
- A literature and trial search focused on cataract and metabolic substrate therapy, to confirm whether any supporting evidence exists
- A clinical review of the Major interaction with orlistat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

