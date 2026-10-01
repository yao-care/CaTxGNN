---
layout: default
title: Insulin Degludec
parent: Model Prediction Only (L5)
nav_order: 476
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Insulin Degludec: From Diabetes Mellitus (Basal Insulin Therapy) to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec is a long-acting basal insulin analogue marketed in Canada as Tresiba and, in a combination product, as Xultophy. The TxGNN model predicts it may be effective for **type 1 diabetes mellitus**, with **50 registered clinical trials** and no indexed publications in the Evidence Pack. Type 1 diabetes is very likely already a labeled use, so this is probably not a true repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (the licence records carry no indication text); presumed diabetes mellitus as a basal insulin, to be confirmed against the label |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** By the rules, at least 2 completed Phase 3 trials in type 1 diabetes give L1. Three qualify: NCT01835431, NCT05463744 and NCT03952130. Only NCT01835431 tests a degludec-containing product as the investigational drug. In the other two, degludec is the comparator or background insulin. The Evidence Pack itself scored this as L2, so the level is best treated as L1–L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Insulin degludec is a long-acting basal insulin analogue. It binds the insulin receptor and replaces the endogenous insulin that is missing in type 1 diabetes. The mechanism is direct and physiologically established.

The empty original-indication and mechanism fields look like input gaps rather than evidence of a new use. Type 1 diabetes is very likely already on the label of this marketed product. The high TxGNN score therefore mostly reflects a well-known drug-disease relationship. It does not show a new therapeutic direction. This should be confirmed against the Health Canada label.

The other five predictions are much weaker and are all rated L5 (Hold), with no trials or literature:

- **Autoimmune oophoritis, classic stiff person syndrome and focal stiff limb syndrome:** These link to type 1 diabetes only through co-occurring autoimmunity (autoimmune polyendocrine syndromes and anti-GAD65 antibodies). Insulin is not expected to treat them.
- **Thiamine-responsive dysfunction syndrome:** Diabetes is a feature of the syndrome, so insulin would only manage the diabetic component symptomatically.
- **Opsismodysplasia:** The link runs through SHIP2 in insulin/PI3K signalling and is speculative.

---

## Clinical Trial Evidence

The pack lists 50 trials. Many are type 2 diabetes studies or use degludec only as a comparator. The ten most relevant to type 1 diabetes are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Degludec/aspart once daily plus mealtime aspart vs detemir plus aspart in children and adolescents with T1D |
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Weekly basal insulin efsitora alfa vs degludec (comparator) in T1D on multiple daily injections |
| [NCT03952130](https://clinicaltrials.gov/study/NCT03952130) | Phase 3 | Completed | 354 | LY900014 vs lispro, each with glargine or degludec as basal insulin, in adults with T1D |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Phase 4 | Completed | 343 | Toujeo (glargine U300) vs Tresiba (degludec) on glucose in target range and variability by CGM in T1D |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Phase 2 | Completed | 266 | Randomized, open-label trial of LY3209590 vs a comparator in T1D; degludec is likely the comparator |
| [NCT05434559](https://clinicaltrials.gov/study/NCT05434559) | N/A | Completed | 475 | Retrospective study of glycaemic control 12 months before vs after switching adults with T1D to degludec |
| [NCT04623086](https://clinicaltrials.gov/study/NCT04623086) | Phase 4 | Completed | 59 | Switching from glargine to degludec with a glargine bridging dose vs direct conversion in T1D |
| [NCT03668808](https://clinicaltrials.gov/study/NCT03668808) | Phase 4 | Completed | 25 | Degludec vs glargine U100 in adults with T1D flying across multiple time zones |
| [NCT00961324](https://clinicaltrials.gov/study/NCT00961324) | Phase 1 | Completed | 54 | Randomized, double-blind trial of within-subject variability in glucose-lowering effect, degludec vs glargine, in T1D |
| [NCT00964964](https://clinicaltrials.gov/study/NCT00964964) | Phase 1 | Completed | 18 | Hypoglycaemic episodes and glycaemic variability across two degludec regimens in T1D |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2467887 | TRESIBA |
| 2467879 | TRESIBA |
| 2467860 | TRESIBA |
| 2474875 | XULTOPHY |

Dosage form and approved indication text were not provided for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct and well established, and there are multiple completed Phase 3 trials in type 1 diabetes. However, this looks like confirmation of an existing labeled use rather than a genuine repurposing opportunity. The safety data gap is also blocking.

**To proceed, the following is needed:**
- Confirm the current Canadian label indications for Tresiba and Xultophy, including whether type 1 diabetes is already approved. Xultophy is a degludec/liraglutide combination, so its indication should be checked separately.
- Download the Health Canada product monograph for warnings and contraindications, which is a blocking gap for safety screening.
- Obtain mechanism-of-action data from DrugBank.
- Separate trials that test degludec as the investigational drug from those where it is only a comparator.
- Keep the five other predicted indications (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, focal stiff limb syndrome and classic stiff person syndrome) on Hold, since none has trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

