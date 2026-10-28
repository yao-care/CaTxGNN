---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Insulin Glargine
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

## Insulin Glargine: Autoimmune oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin originally used to treat type 1 and type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-only prediction, and the likely link is a comorbidity association rather than a therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a basal insulin analogue whose efficacy in diabetes mellitus is well established as glucose-lowering replacement therapy.

The prediction for autoimmune oophoritis is most likely explained by disease co-occurrence. Autoimmune oophoritis often appears within autoimmune polyendocrine syndromes, which can include insulin-requiring diabetes. In that setting, insulin glargine would treat the co-existing diabetes, not the ovarian autoimmune process itself. This link is plausible but unvalidated.

Other high-scoring predictions follow a similar pattern: the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a therapeutic mechanism:
- **Thiamine-responsive dysfunction syndrome, focal stiff limb syndrome and classic stiff person syndrome**: insulin would manage the accompanying diabetes only.
- **Pancreatic agenesis**: insulin replacement is mechanistically coherent, but it is the same replacement role as the existing diabetes indication, not a new use. Of the 10 predictions, this is the only one with any retrieved literature, and that literature is indirect.
- **Opsismodysplasia**: a speculative connection through SHIP2 and insulin/PI3K signalling, with no data showing benefit.
- **Localized lipodystrophies** (drug-induced, centrifugal, pressure-induced, idiopathic): insulin injection is itself a known cause of injection-site lipodystrophy, so these predictions may reflect an adverse-effect association and the drug could worsen the condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For reference, the only literature retrieved across the 10 predictions was for pancreatic agenesis (rank 6). It is indirect and does not demonstrate efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Review of insulin therapy in type 2 diabetes and practical aspects of starting it |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes associated with endocrine diseases such as acromegaly and Cushing syndrome |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 case treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Veterinary cohort | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02441829 | TOUJEO SOLOSTAR | Not specified | Not specified |
| 02294338 | LANTUS | Not specified | Not specified |
| 02461528 | BASAGLAR | Not specified | Not specified |
| 02245689 | LANTUS | Not specified | Not specified |
| 02493373 | TOUJEO DOUBLESTAR | Not specified | Not specified |

Nine DINs are valid in total (all single-ingredient products). The other four are LANTUS (02251930), BASAGLAR (02444844), SEMGLEE (02526441) and SOLIQUA (02478293).

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Most of those listed are Moderate, with a few Minor. Main examples:
  - **Other glucose-lowering agents** (metformin, pioglitazone, alogliptin, albiglutide): may add to the glucose-lowering effect.
  - **Beta-agonists and sympathomimetics** (salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine): may alter glycaemic control.
  - **Corticosteroids** (hydrocortisone, plus minor topical interactions with hydrocortisone and alclometasone): may raise blood glucose.
  - **Estrogens** (estradiol, ethinylestradiol), **thiazides** (hydrochlorothiazide), **acetazolamide**, **doxycycline**, **acebutolol**, **alpelisib** and **ethanol**: Moderate-level interactions.
- **Injection-site lipodystrophy**: Insulin injection can cause localized lipohypertrophy or lipoatrophy. This matters especially for the lipodystrophy predictions, where the drug could worsen the condition.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone (0.9988), with no clinical trials or literature. The plausible link is a diabetes comorbidity, not treatment of autoimmune oophoritis. All 10 top predictions are Hold, and for the lipodystrophy conditions the drug may cause harm.

**To proceed, the following is needed:**
- Direct clinical or literature evidence for insulin glargine in autoimmune oophoritis, rather than only in co-existing diabetes
- Package insert warnings and contraindications from Health Canada, which are a blocking gap for safety screening
- Mechanism of action data
- Approved indication text, dosage forms and manufacturers for the Canadian licences
- Clarification of whether any predicted use differs from standard diabetes replacement therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

