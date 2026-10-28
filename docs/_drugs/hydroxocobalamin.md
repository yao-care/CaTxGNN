---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 459
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Hydroxocobalamin: predicted new indication Esophageal varices without bleeding (a second prediction… (evidence level L5). Approved use: Vitamin B12 deficiency, cyanide poisoning, pernicious anemia"
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
---

# Hydroxocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Hydroxocobalamin: From Vitamin B12 Deficiency and Cyanide Poisoning to Esophageal Varices Without Bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, originally used to treat vitamin B12 deficiency, pernicious anemia and cyanide poisoning.
The TxGNN model predicts it may be useful for **esophageal varices (with and without bleeding)**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, cyanide poisoning, pernicious anemia (the Canadian licence record contains no indication text) |
| Predicted New Indication | Esophageal varices without bleeding (a second prediction, esophageal varices with bleeding, has the same score) |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroxocobalamin is a vitamin B12 form. Its efficacy in B12 deficiency and cyanide poisoning (by binding cyanide) is established. However, no established mechanistic link to esophageal varices has been identified.

One speculative hypothesis is that hydroxocobalamin scavenges nitric oxide (NO), which could theoretically reduce splanchnic vasodilation and portal hypertension, the underlying driver of varices. **No evidence in the data compiled for this report supports this idea.** The same NO-scavenging effect could also raise systemic blood pressure, which would need a separate safety evaluation.

The two predictions share an identical score (0.9923). This suggests the model is scoring a disease cluster rather than a mechanism specific to bleeding. Acute variceal bleeding is life-threatening and already has well-established standard care (vasoactive agents such as terlipressin or octreotide, endoscopic band ligation, antibiotic prophylaxis). Any repurposed agent would need strong evidence to be considered.

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
| 02375370 | CYANOKIT | Not listed | Not listed |

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph links hydroxocobalamin to hypertensive disorder and hypertension as contraindications. This comes from graph edges, not label text. It is relevant because patients with portal hypertension are hemodynamically sensitive, and a blood pressure rise would be a concern.
- **Drug Interactions**: 32 potential interactions were identified. Most are of unknown severity. The following are rated **Moderate**:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Other listed drugs, all of unknown severity, include omeprazole, lansoprazole, simvastatin, loperamide, prednisolone, ranitidine, acetylsalicylic acid, budesonide, folic acid, valsartan, ramipril, lorazepam, citalopram, acetaminophen, mirtazapine and levothyroxine.

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone (Evidence Level L5). There are no clinical trials, no publications, and no established mechanistic link. The possible blood pressure effect adds a safety concern in this patient population, and effective standard treatments already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for hydroxocobalamin (for example, from DrugBank)
- Preclinical or mechanistic evidence for NO scavenging and portal pressure effects
- Literature and trial searches targeting portal hypertension and variceal disease
- Separate evaluation of blood pressure risk in patients with portal hypertension
- Review of the severity of the "Unknown" and Moderate interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

