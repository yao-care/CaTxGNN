---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Insulin Lispro: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue, originally used to control blood sugar in type 1 and type 2 diabetes mellitus and to treat diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction.
Of the nine predicted indications reviewed, none has direct clinical evidence of benefit beyond managing diabetes or insulin deficiency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

*Note: The Canadian licence records compiled for this report contain no approved-indication text. The original indications above come from the TxGNN knowledge graph, not from product labelling.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting insulin analogue whose efficacy in diabetes is well established. It lowers blood glucose by replacing or supplementing insulin.

The top prediction, autoimmune oophoritis, is often associated with polyglandular autoimmune syndromes, which can include autoimmune diabetes. This overlap with the original indication is plausible but unverified. It does not show that insulin lispro treats the ovarian condition itself.

Other predictions follow a similar pattern. Several are linked to the original indication only through coexisting diabetes or insulin signalling:

- **Thiamine-responsive dysfunction syndrome:** insulin may manage the diabetic component, but the underlying disorder is treated with thiamine.
- **Focal stiff limb syndrome and classic stiff person syndrome:** these share autoimmune associations with type 1 diabetes. Insulin would manage only the coexisting diabetes.
- **Opsismodysplasia:** the disease gene (INPPL1/SHIP2) regulates insulin signalling. This is a speculative pathway link with no supporting data.
- **Pancreatic agenesis:** insulin replacement is rational and standard care, but this is the original indication (insulin deficiency) applied to a rare cause, not a novel repurposing.
- **Centrifugal lipodystrophy:** insulin could manage associated hyperglycaemia, but there is no evidence of benefit on the lipodystrophy itself.
- **Drug-induced localized lipodystrophy and pressure-induced localized lipoatrophy:** insulin injections are a known cause of these conditions, so these predictions are likely graph-based artefacts and represent a safety concern, not a treatment opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication, autoimmune oophoritis. The only publication found across the predictions concerns pancreatic agenesis (rank 7):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | Journal of the American Pharmaceutical Association | General review of insulin therapy in type 2 diabetes and how to start it. Not specific to pancreatic agenesis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02403412 | HUMALOG (KWIKPEN) | Not listed | Not listed |
| 02469898 | ADMELOG | Not listed | Not listed |
| 02469901 | ADMELOG | Not listed | Not listed |
| 02439611 | HUMALOG 200 UNITS/ML KWIKPEN | Not listed | Not listed |
| 02469871 | ADMELOG SOLOSTAR | Not listed | Not listed |

All 12 licences are valid single-ingredient products (none cancelled). Other products include HUMALOG cartridges and HUMALOG MIX 25 and MIX 50 formulations.

---

## Safety Considerations

**Drug Interactions:** 100 interactions were identified. The most notable ones in the data compiled for this report are rated Moderate:

- **Other glucose-lowering drugs:** metformin, alogliptin, albiglutide
- **Sympathomimetics and bronchodilators:** epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol
- **Beta-blocker:** acebutolol
- **Corticosteroids:** hydrocortisone
- **Hormonal agents:** estradiol, ethinylestradiol, levonorgestrel
- **Others:** acetazolamide, hydrochlorothiazide, doxycycline, alpelisib, ethanol

Minor interactions include topical hydrocortisone and topical alclometasone.

**Injection-site lipodystrophy:** the predictions for localized lipodystrophy and lipoatrophy reflect a known adverse effect of insulin injections. It should be treated as a safety consideration.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis is based only on a computational score, with no clinical trials or publications. The linkage is indirect, through coexisting autoimmune diabetes. The other predictions are either management of coexisting diabetes, a restatement of the original indication, or an adverse effect of the drug.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada, needed before any safety screening
- Evidence from clinical or preclinical studies showing direct benefit in autoimmune oophoritis, beyond managing coexisting diabetes
- Approved-indication text and dosage-form details for the Canadian licences
- Assessment of the route of administration for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

