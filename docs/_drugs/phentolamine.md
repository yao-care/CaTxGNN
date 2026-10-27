---
layout: default
title: Phentolamine
parent: Model Prediction Only (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phentolamine: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Pheochromocytoma, peripheral vascular disease…"
monitor_inn: "Phentolamine"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "blue toe syndrome", "angiodysplasia of stomach", "hemangioendothelioma", "atheroembolism of kidney", "idiopathic spontaneous coronary artery dissection"]
---

# Phentolamine
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

## Phentolamine: From Pheochromocytoma and Peripheral Vascular Disease to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Phentolamine is an alpha-adrenergic blocker originally used for pheochromocytoma-related hypertensive crises and peripheral vascular disease.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction.
The evidence is model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pheochromocytoma, peripheral vascular disease, peripheral arterial disease, cerebral ischaemia (the Canadian licence records contain no indication text) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, phentolamine is a non-selective alpha-adrenergic antagonist that causes vasodilation. Its efficacy in pheochromocytoma-related hypertensive crises and in peripheral vascular disease is well established.

Visceral calciphylaxis (calcific uremic arteriolopathy) involves microvascular occlusion and ischaemia. This gives a theoretical link to a vasodilator. However, the disease is driven mainly by mineral metabolism disturbance, vascular calcification and thrombosis, so alpha-blockade is not a recognised mechanism for treating it. The high model score is not matched by any trial or publication, and the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

For context, the second-ranked prediction, "vascular disease", is a broad label that largely overlaps with phentolamine's existing indications. It returned the following trials, none of which tests phentolamine as a treatment for the predicted calciphylaxis indication. They are shown only as background:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06286059](https://clinicaltrials.gov/study/NCT06286059) | Phase 2/3 | Unknown | 60 | Phentolamine to prevent contrast-associated acute kidney injury after complex PCI in high-risk patients |
| [NCT05997732](https://clinicaltrials.gov/study/NCT05997732) | Phase 4 | Recruiting | 30 | Sex differences in sympathetic neurovascular transduction and adrenergic receptor role |
| [NCT05219799](https://clinicaltrials.gov/study/NCT05219799) | Early Phase 1 | Recruiting | 72 | Sex differences in hypoxic vasodilation and the impact of obesity |
| [NCT05525416](https://clinicaltrials.gov/study/NCT05525416) | NA | Completed | 17 | Sex differences in sympathetic vascular reactivity at high altitude |

The large stroke blood-pressure trials matched to this term (NCT01422616, NCT00716079, NCT00226096) do not appear to test phentolamine and are not counted as evidence.

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243737 | Phentolamine Mesylate Injection Sandoz Standard | Not specified | Not specified |
| 02421666 | Oraverse | Not specified | Not specified |

---

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text)**: liver disease, gallbladder disease, hypotensive disorders, coronary artery disease, myocardial infarction, coronary thrombosis, haemoglobinopathy, sudden cardiac arrest, heart conduction disease, glaucoma, atrioventricular block.
- **Drug Interactions**: 100 interactions were identified. Moderate-level interactions include bupropion, morphine, dronabinol and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Minor-level interactions include many insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro and others).

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is very high, but there are no trials or publications for visceral calciphylaxis, and the proposed mechanism (alpha-blockade) does not address the main drivers of the disease. The evidence is L5, model prediction only.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Detailed mechanism of action data
- Preclinical or case-level evidence of phentolamine in calcific uremic arteriolopathy
- An assessment of hypotension risk in patients with renal failure
- Confirmation of the approved indications and dosage forms for the two Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

