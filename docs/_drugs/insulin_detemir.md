---
layout: default
title: Insulin Detemir
parent: High Evidence (L1-L2)
nav_order: 407
evidence_level: L1
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

Using the Evidence Pack as given. Note: for this candidate, `original_indications` is empty and `original_moa` is a data gap, and the "predicted" indication (T1DM) is actually insulin detemir's own established use — the pack's own `repurposing_rationale` flags this as a market-access case (drug unmarketed in Canada) rather than a novel mechanistic hypothesis. I've reflected that explicitly rather than forcing a false narrative.

# Insulin Detemir: From Diabetes Mellitus (Basal Insulin Therapy) to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir is a long-acting basal insulin analogue already used internationally for diabetes mellitus; detailed original-indication records are not on file for this jurisdiction. The TxGNN model scores it highly for **Type 1 Diabetes Mellitus**, but this is not a novel mechanistic hypothesis — it reflects the drug's own core approved use, which is currently **unmarketed in Canada**, with **50+ clinical trials** and **19 publications** already supporting efficacy/safety in T1DM globally.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack; insulin detemir is internationally approved as a basal insulin for diabetes mellitus (type 1 and type 2) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not recorded in this evidence pack (`original_moa` is missing), but the supporting literature is informative: insulin detemir is a soluble long-acting human insulin analogue acylated with a 14-carbon fatty acid, which allows it to reversibly bind albumin and thereby achieve slow, protracted absorption and a stable ~24-hour glucose-lowering profile (PMID 15516157, PMID 17326333).

This mechanism is a direct, on-label replacement of endogenous insulin deficiency in Type 1 Diabetes Mellitus — it is not an indirect or repurposed pharmacological pathway. As the evidence pack's own rationale notes, this connection is a "direct mechanistic link" reflecting a standard, already-approved use rather than a genuine old-drug/new-use hypothesis.

The reason this candidate surfaces at all is regulatory, not mechanistic: insulin detemir is currently **not marketed in Canada** (0 licenses on file). The evaluation focus for this candidate should therefore be the market-authorization pathway (Health Canada submission status, product monograph availability) rather than mechanistic plausibility, which is already well established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00312104](https://clinicaltrials.gov/study/NCT00312104) | Phase 3 | Completed | 325 | Head-to-head RCT: detemir vs. glargine (both + aspart) in T1DM |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | Detemir+aspart vs. glargine+aspart basal/bolus therapy in T1DM |
| [NCT00659295](https://clinicaltrials.gov/study/NCT00659295) | N/A | Completed | 51,170 | PREDICTIVE™ global post-marketing safety study of Levemir® in T1DM/T2DM |
| [NCT00655044](https://clinicaltrials.gov/study/NCT00655044) | N/A | Completed | 3,637 | European observational safety study of Levemir® in T1DM/T2DM |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Detemir vs. NPH insulin (+aspart) in pregnant women with T1DM |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Degludec/aspart vs. detemir+aspart in children/adolescents with T1DM |
| [NCT00604344](https://clinicaltrials.gov/study/NCT00604344) | Phase 3 | Completed | 401 | Detemir vs. NPH insulin in basal-bolus regimen, Japan |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Detemir vs. NPH: hypoglycaemic episode frequency in well-controlled T1DM |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Detemir+aspart vs. NPH+aspart efficacy/safety in adults with T1DM |
| [NCT00605137](https://clinicaltrials.gov/study/NCT00605137) | Phase 3 | Completed | 83 | Safety of detemir vs. NPH insulin in children with T1DM, Japan |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: degludec non-inferior to detemir (both + aspart) in pregnant women with T1DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review/Meta-analysis | Pol Arch Med Wewn | Detemir vs. NPH insulin in T1DM: glycaemic control benefits, mixed confirmation across studies |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review/Network Meta-analysis | Value Health | Comparative efficacy/safety of basal insulin regimens (incl. detemir) in adults with T1DM |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Review/Meta-analysis | Clin Ther | Degludec vs. other long-acting analogues (glargine, detemir) in T1DM/T2DM |
| [21361858](https://pubmed.ncbi.nlm.nih.gov/21361858/) | 2011 | Cost analysis | J Med Econ | Lifetime cost modelling of glargine vs. detemir in T1DM/T2DM patients **in Canada** |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Update on T1DM/T2DM treatment, focused on insulin detemir |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin detemir: pharmacology and use in T1DM/T2DM |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Insulin detemir mechanism and use in T1DM/T2DM |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Insulin detemir review of use in diabetes mellitus management |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Update on management of T1DM in pregnancy (lifestyle, pharmacotherapy, technology) |

---

## Canada Market Information

No Drug Identification Numbers (DINs) are currently on file for insulin detemir in this evidence pack — the product is recorded as **not marketed** in Canada (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Product-specific warnings, contraindications, and drug-interaction data were not available in this evidence pack (flagged as a **Blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin detemir's efficacy and safety in Type 1 Diabetes Mellitus are robustly supported by multiple completed Phase 3 RCTs and large-scale post-marketing safety studies (meeting the L1 evidence bar), but this reflects the drug's already-established international use rather than a novel repurposing hypothesis. The open question is regulatory: the product is currently unmarketed in Canada, and product-specific label data (warnings/contraindications) is missing — a blocking gap for any S1 safety review.

**To proceed, the following is needed:**
- Health Canada product monograph or equivalent label data (warnings, contraindications) — resolves DG001 (Blocking)
- DrugBank-sourced mechanism-of-action documentation — resolves DG002 (High)
- Confirmation of current Health Canada market-authorization/submission status for insulin detemir
- Given the strength of existing evidence, treat this primarily as a **market-access review**, not a discovery candidate; ranks 2–10 in this pack (autoimmune oophoritis, opsismodysplasia, stiff-person-syndrome spectrum, lipodystrophy variants, etc.) are L5/Hold, with several likely reflecting reversed causality (insulin injection as a *cause* of localized lipoatrophy rather than a treatment) and should not be pursued without independent mechanistic verification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

