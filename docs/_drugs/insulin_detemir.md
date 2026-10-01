---
layout: default
title: Insulin Detemir
parent: High Evidence (L1-L2)
nav_order: 477
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

# Insulin Detemir: From Diabetes Mellitus (Basal Insulin Therapy) to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir is a long-acting basal insulin analog, marketed as Levemir and used to treat diabetes mellitus.
The TxGNN model predicts it is effective for **type 1 diabetes mellitus**, backed by **50 clinical trials** and **19 publications**.
This prediction matches the drug's established use, so it validates the model's recall and is **not a new repurposing finding**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (the literature describes basal insulin use in type 1 and type 2 diabetes) |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. From the published literature, insulin detemir is a soluble long-acting human insulin analog acylated with a 14-carbon fatty acid. The fatty acid lets it bind reversibly to albumin, which slows absorption and gives a prolonged, more predictable glucose-lowering effect of up to 24 hours. It acts at the insulin receptor and replaces the endogenous insulin that is missing in type 1 diabetes.

The predicted disease is the core condition this class of drug treats, so the model's high score is consistent with known clinical practice. Reviews report a more predictable profile than NPH insulin, with less within-patient variability and a lower risk of hypoglycaemia, especially nocturnal hypoglycaemia.

**Guardrail:** The other nine predictions for this drug (for example autoimmune oophoritis, opsismodysplasia, stiff person spectrum disorders and lipodystrophies) have no trials or literature and rest on model prediction alone (L5). Several appear to reflect comorbidity, standard diabetes care, or known injection-site adverse effects rather than a therapeutic mechanism.

---

## Clinical Trial Evidence

The pack lists 50 trials. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00312104](https://clinicaltrials.gov/study/NCT00312104) | Phase 3 | Completed | 325 | Twice-daily detemir vs once-daily glargine, each with mealtime aspart, in type 1 diabetes |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | Detemir + aspart vs glargine + aspart in basal-bolus therapy; tests whether detemir is at least as effective |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Detemir + aspart vs NPH + aspart in adults with type 1 diabetes |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | Completed | 88 | Crossover, glargine vs detemir with glulisine bolus; fasting glucose variability in type 1 diabetes |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Detemir vs NPH on hypoglycaemic episode frequency in well-controlled type 1 diabetes |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Detemir vs NPH insulin in pregnant women with type 1 diabetes |
| [NCT00604344](https://clinicaltrials.gov/study/NCT00604344) | Phase 3 | Completed | 401 | 48-week Japanese trial, detemir vs NPH on a basal-bolus regimen |
| [NCT00605137](https://clinicaltrials.gov/study/NCT00605137) | Phase 3 | Completed | 83 | Safety of detemir vs NPH in children with type 1 diabetes (Japan) |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Degludec/aspart vs detemir + aspart in children and adolescents with type 1 diabetes |
| [NCT00659295](https://clinicaltrials.gov/study/NCT00659295) | N/A (observational) | Completed | 51,170 | PREDICTIVE study: real-world incidence of serious adverse reactions across 26 countries |

---

## Literature Evidence

The pack lists 19 publications. The 10 most relevant are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: non-inferiority trial of degludec vs detemir with aspart in pregnant women with type 1 diabetes |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network meta-analysis | Value Health | Relative efficacy and safety of basal insulin regimens in adults with type 1 diabetes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Meta-analysis | Clin Ther | Degludec vs other long-acting analogues, including detemir, in type 1 and type 2 diabetes |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Meta-analysis | Pol Arch Med Wewn | Detemir vs NPH insulin in type 1 diabetes |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Detemir as basal insulin in type 1 and 2 diabetes; protracted action from self-association and albumin binding, with less variability than NPH |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | More predictable, consistent effect than NPH, with less intra-patient variability |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Effective option in type 1 and 2 diabetes; no significant HbA1c difference vs comparators, lower hypoglycaemia rate |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Less variable pharmacokinetics than NPH or ultralente; reduced hypoglycaemia risk |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Update on managing type 1 diabetes in pregnancy, including pharmacological treatment |
| [21361858](https://pubmed.ncbi.nlm.nih.gov/21361858/) | 2011 | Cost analysis | J Med Econ | Lifetime cost comparison of glargine and detemir in Canada |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2271842 | LEVEMIR PENFILL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least 8 completed Phase 3 trials in type 1 diabetes, including head-to-head comparisons with glargine and NPH insulin, support this indication (L1). The prediction reflects the drug's established use, so it should be counted as validation of the model, not as a new repurposing discovery.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Confirmation of the approved indication text for DIN 2271842, which is blank in the license record
- Separate review of the lower-ranked predictions, which are L5 (Hold). Injection-site lipodystrophy should be handled as a safety signal, not a therapeutic candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

