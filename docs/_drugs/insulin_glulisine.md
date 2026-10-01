---
layout: default
title: Insulin Glulisine
parent: High Evidence (L1-L2)
nav_order: 479
evidence_level: L1
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Mealtime Glycaemic Control in Diabetes to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (brand name APIDRA) is a rapid-acting human insulin analogue used for mealtime blood glucose control in diabetes.
The TxGNN model predicts it for **type 1 diabetes mellitus (T1DM)**, backed by **50 clinical trials** and **19 publications**, including several completed Phase 3 trials in T1DM.
This is very likely an approved use rather than true repurposing, so the result should be read as a validation of the model, not a new discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian licence records. Published reviews describe it as improving glycaemic control in adults, adolescents and children with diabetes mellitus. |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Insulin glulisine is a rapid-acting insulin analogue that activates the insulin receptor. In T1DM it replaces the missing endogenous insulin. Published reviews describe a faster onset and shorter duration of action than regular human insulin, and glucose-lowering effects similar to insulin lispro. This is why it is used as a mealtime (bolus) insulin alongside a basal insulin.

The relationship between the original and predicted indications is direct. T1DM is a form of diabetes mellitus characterised by insulin deficiency, so it falls within the drug's general use. The very high TxGNN score most likely reflects existing drug-disease links in the knowledge graph rather than a novel finding. **Guardrail:** confirm the Health Canada label indication before presenting this as repurposing.

The other nine predictions (ranks 2–10) have no trials or literature and are all graded L5. Most look like comorbidity or adverse-effect associations, not treatment rationales:

- **Comorbidity associations:** stiff person syndrome, focal stiff limb syndrome and autoimmune oophoritis (T1DM/autoimmune links). Insulin would treat only the coexisting diabetes.
- **Injection-site lipodystrophy and lipoatrophy** (drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy): these are known injection-site reactions, so they are safety signals.
- **Pancreatic agenesis:** insulin replacement is mechanistically coherent for the insulin-deficient diabetes, but no evidence was supplied. This is worth a targeted literature search, including neonatal dosing and formulation limits.
- **Thiamine-responsive dysfunction syndrome:** insulin could treat the diabetic component but not the underlying thiamine transport defect.
- **Opsismodysplasia:** there is only a speculative pathway link (INPPL1/SHIP2) and no therapeutic rationale.

---

## Clinical Trial Evidence

Fifty trials were retrieved. The 10 most relevant are listed below. Two completed Phase 3 randomised trials in T1DM (NCT00271284 and NCT00290979) support the L1 rating.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | Randomised, open-label, non-inferiority trial of glulisine vs insulin lispro over 28 weeks in T1DM. The primary endpoint was change in HbA1c. |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | Completed | 88 | Randomised crossover trial of glargine vs detemir, each combined with glulisine as bolus, in T1DM. It compared variability of fasting glucose. |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | Open-label, non-randomised 26-week study of glulisine with glargine in T1DM. It assessed HbA1c change and safety. |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Non-randomised controlled study of efficacy, safety and patient satisfaction of glulisine in T1DM patients also using glargine. |
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | Completed | 100 | Apidra plus Lantus basal-bolus regimen in children and adolescents with T1DM. Outcomes were the proportion reaching HbA1c targets, hypoglycaemia rate and dose. |
| [NCT01678235](https://clinicaltrials.gov/study/NCT01678235) | Phase 4 | Completed | 64 | Double-blind crossover of glulisine vs aspart on postprandial glucose after a high-glycaemic-index meal in children on pump therapy. |
| [NCT00913497](https://clinicaltrials.gov/study/NCT00913497) | Phase 4 | Completed | 16 | Crossover comparison of glulisine vs aspart on breakfast postprandial glucose in prepubertal children with T1DM. |
| [NCT02685449](https://clinicaltrials.gov/study/NCT02685449) | Phase 4 | Unknown | 70 | Randomised crossover study of insulin dosing for a pure-protein meal in children with T1DM on pump therapy. |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: Afrezza vs rapid-acting insulin injections (aspart, lispro or glulisine) in paediatric diabetes. Glulisine is one of several comparators, so direct relevance is limited. |
| [NCT02914886](https://clinicaltrials.gov/study/NCT02914886) | Phase 4 | Completed | 14 | Tests whether zinc-free glulisine helps lipoatrophy in T1DM patients on insulin pump therapy. |

---

## Literature Evidence

Nineteen publications were retrieved. The 10 most relevant are listed below, with randomised trials first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multinational, open-label, randomised trial comparing glulisine with lispro in adults with T1DM (683 randomised). It assessed efficacy and safety. |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Three-way crossover of glulisine, aspart and lispro delivered by continuous subcutaneous insulin infusion (CSII) in T1DM. |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | Clinical trial | Diabetes Technol Ther | 26-week trial in children and adolescents with T1DM. Glulisine had efficacy and safety comparable to lispro in a basal-bolus regimen. |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Comparative study | Diabetes Obes Metab | Glulisine vs lispro in Japanese T1DM patients using glargine as basal insulin. |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative study | Acta Diabetol | Compared glulisine with lispro and aspart in T1DM pump users. It described HbA1c, fasting glucose, dose, and rates of hyperglycaemia, hypoglycaemia and diabetic ketoacidosis (DKA). |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Clinical study | Pediatr Int | In 20 children on CSII, post-breakfast and post-dinner glucose improved significantly after one year of glulisine. |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | Clinical study | Diabetes Care | Pharmacokinetics, postprandial glucose excursions and safety of glulisine vs regular human insulin in paediatric T1DM. |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Review | Drugs Today | Review of insulin analogues, including glulisine, for T1DM in children and adolescents. |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Review of glulisine in diabetes. It has a faster onset than regular human insulin and is effective against other short- and rapid-acting insulins. |
| [26838553](https://pubmed.ncbi.nlm.nih.gov/26838553/) | 2016 | Case report | Acta Diabetol | A T1DM patient whose localised insulin allergy was markedly alleviated after switching to glulisine. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2279479 | APIDRA |
| 2294346 | APIDRA |
| 2279460 | APIDRA |

The dosage form and approved-indication text were not available in the supplied licence records.

---

## Safety Considerations

- **Injection-site reactions:** The knowledge graph links insulin to localised lipodystrophy and lipoatrophy (ranks 8–10). These are recognised injection-site effects of injected insulins and should be treated as a safety signal, not a therapeutic use.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 randomised trials in T1DM, several randomised trials in the literature, and Canadian marketing under three DINs give strong evidence for use in T1DM (L1). However, this is very likely an approved use rather than true repurposing, and the Canadian label indication and safety data have not been verified.

**To proceed, the following is needed:**
- Confirm the approved indication on the Health Canada label and monograph, to establish whether T1DM is already covered.
- Obtain the monograph warnings, contraindications and interaction data. Safety screening cannot start without them.
- Retrieve mechanism of action data from DrugBank.
- Run a targeted literature search for pancreatic agenesis (neonatal dosing and formulation limits).
- Treat the lipodystrophy and lipoatrophy predictions as adverse-effect signals, not repurposing candidates.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

