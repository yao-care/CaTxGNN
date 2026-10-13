---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Canadian licence records contain no indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, glimepiride is a sulfonylurea that closes ATP-sensitive potassium channels in pancreatic beta cells and stimulates insulin release. Its efficacy in type 2 diabetes is established.

Stiff person syndrome is an autoimmune neurological disorder linked to GABAergic signalling and anti-GAD65 antibodies. It often occurs together with type 1 diabetes. The high prediction score probably reflects this shared diabetes/autoimmune neighbourhood in the knowledge graph rather than a therapeutic mechanism. No direct mechanistic rationale for benefit has been established.

The same score was given to a closely related condition, focal stiff limb syndrome. This suggests the prediction comes from disease similarity within the graph.

Other predicted indications show the same pattern: opsismodysplasia, thiamine-responsive dysfunction syndrome, several localized lipodystrophies and pancreatic agenesis. All are L5 and Hold. For pancreatic agenesis, glimepiride would be expected to be ineffective because sulfonylureas need functional beta cells.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02269619 | SANDOZ GLIMEPIRIDE | Not specified | Not specified |
| 02269597 | SANDOZ GLIMEPIRIDE | Not specified | Not specified |
| 02269589 | SANDOZ GLIMEPIRIDE | Not specified | Not specified |

## Safety Considerations

**Diseases flagged as contraindications in the knowledge graph** (these come from graph relationships, not from label text):
- Kidney disease, liver disease, gallbladder disease, congestive heart failure
- Pituitary and growth hormone deficiency conditions, and hypogonadotropic hypogonadism conditions (including Kallmann syndrome and Sheehan syndrome)
- Thymus gland disease, osteoporosis, postmenopausal osteoporosis, infectious disease

**Drug Interactions** (100 interactions recorded; examples from the first 20 listed):
- Moderate: phenylephrine, acebutolol, acetazolamide, famotidine, ranitidine, acitretin, formoterol, pseudoephedrine, ketorolac, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, albiglutide, salbutamol, ethanol, nitazoxanide, hydrochlorothiazide
- Minor: topical hydrocortisone, topical alclometasone

For warnings and contraindications from the label, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score. There are no clinical trials or literature for stiff person syndrome, and no plausible therapeutic mechanism has been shown. The link appears to come from the shared diabetes and autoimmune context.

**To proceed, the following is needed:**
- Obtain the Health Canada package insert, so warnings, contraindications, dosage forms and approved indications can be confirmed
- Obtain mechanism of action data, and assess whether any plausible link to GABAergic or autoimmune pathways exists
- Run a systematic literature search for glimepiride or sulfonylureas in stiff person syndrome
- Consider whether drugs with established evidence in stiff person syndrome are better candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

