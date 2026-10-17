---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Canadian license records contain no indication text; this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, empagliflozin is an SGLT2 inhibitor that lowers blood glucose by reducing renal glucose reabsorption, and its efficacy in type 2 diabetes is established.

Stiff person syndrome is an autoimmune neurological disorder characterised by anti-GAD65 antibodies and impaired GABAergic signalling. A possible link is the shared association with autoimmune diabetes (GAD65 autoimmunity). This is an inference from the knowledge graph, not a demonstrated pharmacological mechanism, and no evidence shows that SGLT2 inhibition affects stiff person syndrome.

Two other predictions deserve mention:
- **Focal stiff limb syndrome** (score 99.06%): a variant within the stiff person syndrome spectrum. It received an identical score, so it is likely not an independent prediction.
- **Opsismodysplasia** (score 99.03%): a rare skeletal dysplasia caused by INPPL1 mutations, which affect insulin/PI3K signalling. The link to glucose metabolism is speculative, and the paediatric rare-disease setting adds safety considerations.

All three predictions are hypothesis-generating only.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02443945 | JARDIANCE | Not specified | Not specified |
| 02443937 | JARDIANCE | Not specified | Not specified |
| 02456591 | SYNJARDY | Not specified | Not specified |
| 02456575 | SYNJARDY | Not specified | Not specified |
| 02456605 | SYNJARDY | Not specified | Not specified |

Eight valid single-ingredient authorisations are on record in total; the five above are shown.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 potential interactions. Most of those listed are Moderate, and a few are Minor. Examples of Moderate interactions include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Cardiovascular drugs: acebutolol, nifedipine, fosinopril
  - Diuretics: furosemide, acetazolamide
  - Others: ethinylestradiol, hydrocortisone, ethanol, fosphenytoin
  - Minor interactions: topical hydrocortisone, topical alclometasone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (99.06%), with no clinical trials or literature. The proposed mechanism is speculative, and the Canadian license records lack indication and warning text. This is Evidence Level L5.

**To proceed, the following is needed:**
- Retrieve the Health Canada package insert (warnings, contraindications, approved indications), which is required before any safety screening
- Obtain mechanism of action data from DrugBank
- Conduct a literature and clinical trial search on SGLT2 inhibitors in stiff person syndrome and GAD65-related autoimmunity
- Assess whether the stiff person syndrome and focal stiff limb syndrome predictions are independent
- Look for preclinical or mechanistic evidence connecting SGLT2 inhibition to the neurological or autoimmune pathology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

