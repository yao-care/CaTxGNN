---
layout: default
title: Insulin Aspart
parent: High Evidence (L1-L2)
nav_order: 475
evidence_level: L1
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Approved Insulin Therapy to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart is a rapid-acting insulin analogue marketed in Canada under brand names such as NovoRapid, Fiasp and Trurapi.
The TxGNN model predicts it may be effective for **type 1 diabetes mellitus**, with **50 clinical trials** and **20 publications** currently supporting this direction.
This is an established, on-label use of the drug, so the prediction confirms standard of care rather than pointing to a new therapeutic area.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records provided (insulin therapy for diabetes) |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, insulin aspart is a rapid-acting analogue of human insulin. Type 1 diabetes is defined by autoimmune destruction of pancreatic beta cells and the resulting insulin deficiency. Exogenous insulin replaces the missing hormone, so the mechanism fits the disease directly.

Because this is standard-of-care use, the high TxGNN score mostly reflects an already known relationship. The literature supports this: reviews describe insulin aspart, taken immediately before meals, as giving lower HbA1c and better postprandial control than regular human insulin in type 1 diabetes.

The other nine predictions are weaker. Only permanent neonatal diabetes mellitus (rank 5) has a plausible insulin-replacement rationale, and its evidence is a single indirect review. Several others (autoimmune oophoritis, stiff person syndrome variants) look like graph proximity through autoimmune diabetes comorbidity, not a therapeutic effect. Drug-induced localized lipodystrophy is a known adverse effect of injected insulin, so it is a safety flag rather than a candidate.

---

## Clinical Trial Evidence

The table lists the 10 most relevant of the 50 trials found.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Insulin aspart vs insulin lispro in insulin pumps in children and adolescents with type 1 diabetes |
| [NCT00888732](https://clinicaltrials.gov/study/NCT00888732) | Phase 3 | Completed | 24 | Quadruple crossover of PK/PD for aspart, biphasic aspart 70/50 and human insulin. Small, so it supports exposure-response more than clinical outcomes |
| [NCT00832182](https://clinicaltrials.gov/study/NCT00832182) | Phase 3 | Completed | 75 | Non-randomised extension assessing long-term safety of insulin aspart in a basal-bolus regimen |
| [NCT01467141](https://clinicaltrials.gov/study/NCT01467141) | Phase 4 | Completed | 26 | Meal-related aspart vs human insulin in children aged 2–6 years, randomised crossover |
| [NCT04772729](https://clinicaltrials.gov/study/NCT04772729) | Phase 4 | Unknown | 77 | Faster aspart vs aspart on time in range in children using pumps and CGM. Status unverified |
| [NCT04149262](https://clinicaltrials.gov/study/NCT04149262) | N/A | Completed | 44 | Real-world retrospective comparison of Fiasp vs NovoRapid in paediatric pump users |
| [NCT02035371](https://clinicaltrials.gov/study/NCT02035371) | Phase 1 | Completed | 41 | Pharmacokinetics of faster aspart in children, adolescents and adults with type 1 diabetes |
| [NCT02003677](https://clinicaltrials.gov/study/NCT02003677) | Phase 1 | Completed | 67 | PK/PD of faster aspart in geriatric vs younger adults with type 1 diabetes |
| [NCT03215498](https://clinicaltrials.gov/study/NCT03215498) | Phase 1 | Completed | 58 | Faster aspart vs NovoRapid as pump bolus in type 1 diabetes |
| [NCT03993366](https://clinicaltrials.gov/study/NCT03993366) | N/A | Completed | 8 | Pilot of Fiasp-plus-pramlintide closed-loop delivery. Very small |

---

## Literature Evidence

The table lists 10 of the 20 publications found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes Obes Metab | Double-blind crossover of faster aspart vs insulin aspart in adults with type 1 diabetes using a non-automated pump and CGM |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster aspart vs aspart on fetal growth in type 1 or type 2 diabetes during pregnancy and post-delivery |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs detemir, both with aspart, in pregnant women with type 1 diabetes. Aspart is background therapy, so this is indirect evidence |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: weekly icodec vs daily degludec in a basal-bolus regimen in type 1 diabetes. Aspart is background therapy, so this is indirect evidence |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic review | Diabetes Metab | Efficacy and safety of insulin aspart vs regular human insulin in type 1 and type 2 diabetes |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Pre-meal aspart gave lower HbA1c than regular human insulin in most randomised trials in type 1 diabetes |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Spotlight on insulin aspart: faster absorption and better postprandial control than regular human insulin |
| [29978361](https://pubmed.ncbi.nlm.nih.gov/29978361/) | 2019 | Review | Clin Pharmacokinet | Faster insulin aspart as a new bolus option, with PK/PD comparison against insulin aspart |
| [39115159](https://pubmed.ncbi.nlm.nih.gov/39115159/) | 2024 | Cohort (post hoc) | Diabet Med | Safety and glycaemic control of aspart vs other bolus insulins in pregnancy with type 1 diabetes |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Observational | Acta Diabetol | Glulisine vs lispro and aspart in pump-treated type 1 diabetes: HbA1c, dose, and rates of hypo-/hyperglycaemia and DKA |

---

## Canada Market Information

Ten authorisations are on record; the five main ones are shown. The records provided do not include dosage form or approved-indication text.

| DIN | Product Name |
|---------|------|
| 02506564 | TRURAPI |
| 02529254 | TRURAPI |
| 02460424 | FIASP |
| 02460408 | FIASP |
| 02245397 | NOVORAPID |

---

## Safety Considerations

Please refer to the package insert for safety information.

Two points come from the predictions themselves: injected insulin is a known cause of injection-site lipodystrophy, and paediatric dosing and hypoglycaemia risk need explicit review in young children.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least two completed Phase 3 trials and several Phase 4 paediatric studies support insulin aspart in type 1 diabetes, and the mechanism is straightforward insulin replacement. However, this is an existing standard-of-care use rather than true repurposing. The evidence is also uneven: the Phase 3 PK/PD study is small (n=24), and several supportive trials and papers use aspart only as background therapy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing, and blocking safety screening)
- Approved-indication text and dosage forms for the Canadian DINs, so the original indication can be stated
- Mechanism of action data from DrugBank
- A paediatric hypoglycaemia and dosing review
- Targeted aspart-specific evidence before advancing permanent neonatal diabetes mellitus (rank 5). The other predictions (ranks 2–4 and 6–10) should stay on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

