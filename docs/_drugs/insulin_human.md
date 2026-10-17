---
layout: default
title: Insulin Human
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Insulin Human: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
monitor_inn: "Insulin human"
predicted_indications: ["autoimmune oophoritis", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
---

# Insulin Human
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

# Insulin Human: From Type 2 Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is a replacement hormone originally used to control blood glucose in type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
This looks like a model-based association rather than a true therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin human is a recombinant replacement hormone whose efficacy in diabetes is well established. It lowers blood glucose by replacing deficient insulin.

Autoimmune oophoritis often occurs alongside autoimmune polyglandular syndromes, which include type 1 diabetes. The model score most likely reflects this shared autoimmune background. Insulin treats the diabetic component, but it has no known effect on the ovarian autoimmune process itself. This is probably a knowledge-graph association artifact rather than a real treatment signal.

The other top predictions follow similar patterns:
- **Stiff person syndrome (classic and focal forms):** linked through anti-GAD65 autoimmunity and its frequent coexistence with type 1 diabetes. This is comorbidity, not treatment.
- **Thiamine-responsive dysfunction syndrome:** diabetes is a core feature, but the underlying disorder is treated with thiamine. Insulin would only manage the diabetes.
- **Pancreatic agenesis:** insulin replacement is standard care for the resulting insulin deficiency. This extends the approved use rather than being new repurposing, and it cannot be verified from the data compiled for this report.
- **Opsismodysplasia:** INPPL1 (SHIP2) regulates insulin/PI3K signalling, so there is a pathway-level link. There is no evidence that insulin would help skeletal outcomes.
- **Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic):** insulin injections themselves are a recognized cause of localized lipohypertrophy and lipoatrophy. Insulin would be expected to cause these conditions, not treat them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02529602 | MYXREDLIN | Not specified | Not specified |
| 00795879 | HUMULIN 30/70 (INSULIN HUMAN BIOSYNTH INJ) | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified, and the 20 listed in the data compiled for this report are mostly Moderate, with a few Minor. Main ones:
  - **Other antidiabetic agents (additive hypoglycaemia risk):** metformin, pioglitazone, alogliptin, albiglutide
  - **Sympathomimetics (may reduce glucose-lowering effect):** epinephrine, phenylephrine, pseudoephedrine, salbutamol
  - **Corticosteroids (may raise blood glucose):** hydrocortisone (Moderate); topical hydrocortisone and topical alclometasone (Minor)
  - **Beta-blockers (may mask hypoglycaemia symptoms):** acebutolol
  - **Others:** ethanol, hydrochlorothiazide, acetazolamide, estradiol, ethinylestradiol, doxycycline, benazepril, alpelisib
- **Injection-site effects:** insulin injections can cause localized lipohypertrophy and lipoatrophy. This is directly relevant to the lipodystrophy predictions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or literature. The plausible explanation is shared autoimmune comorbidity with type 1 diabetes, not a treatment effect on the ovarian disease. Package insert safety data are also not yet available.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for insulin human
- Indication text and dosage forms for the two Canadian authorizations
- Targeted literature and trial searches on insulin in autoimmune oophoritis, to rule out a comorbidity artifact
- If any lead is pursued, pancreatic agenesis is the only prediction where insulin has a clear role. It is best treated as an extension of the existing indication, not new repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

