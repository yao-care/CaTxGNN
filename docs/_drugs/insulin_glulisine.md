---
layout: default
title: Insulin Glulisine
parent: High Evidence (L1-L2)
nav_order: 409
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (Apidra) is a rapid-acting recombinant human insulin analogue already used broadly for glycaemic control in diabetes mellitus. The TxGNN model's top prediction is **Type 1 Diabetes Mellitus** specifically, with **50 clinical trials** and **19 publications** currently supporting this direction. This is best understood as a confirmatory / on-label signal rather than a novel repurposing opportunity, since insulin therapy is already the standard-of-care treatment for type 1 diabetes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (glycaemic control) — no Canadian DIN license text available; drug not currently marketed in Canada |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source pack (marked as a High-severity data gap). Based on the supporting literature in this pack, insulin glulisine is a rapid-acting human insulin analogue (modified at positions B3 and B29) that mimics endogenous mealtime insulin, providing faster onset and shorter duration of action than regular human insulin. It is used to control post-prandial (bolus) glucose excursions, typically combined with a basal insulin such as glargine or detemir.

Type 1 diabetes mellitus is caused by autoimmune destruction of pancreatic β-cells, resulting in absolute insulin deficiency. Exogenous insulin replacement — including rapid-acting analogues like glulisine — is the core physiological treatment for this disease, not a repurposed mechanism. The `original_indications` field being empty in this dataset reflects a Canadian regulatory data gap (the product is not currently marketed/licensed in Canada), not an absence of mechanistic rationale.

Because of this, the "prediction" here should be read as the model correctly recovering an established, guideline-level use of the drug rather than surfacing a new therapeutic hypothesis. The extensive clinical trial and literature base below confirms efficacy and safety in T1DM populations specifically, which is why the evidence level is high (L1) despite this not being a true novel indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week multicenter trial of insulin glulisine (HMR1964) + glargine in T1DM; assessed HbA1c change, hypoglycemia, and insulin dose |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | Completed | 88 | Crossover non-inferiority trial comparing glucose variability with glargine+glulisine vs detemir+glulisine bolus regimens in T1DM |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: 26-week randomized trial of inhaled insulin vs rapid-acting analogs (incl. glulisine) + basal insulin in pediatric T1DM/T2DM |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | 28-week open randomized parallel non-inferiority trial of glulisine (HMR1964) vs insulin lispro on HbA1c change in T1DM |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Open-label non-randomized study evaluating efficacy/safety of subcutaneous glulisine combined with glargine in T1DM |
| [NCT02910518](https://clinicaltrials.gov/study/NCT02910518) | Phase 1 | Completed | 44 | Randomized double-blind crossover bioequivalence study of glulisine 300 U/mL vs 100 U/mL formulations via euglycemic clamp in T1DM |
| [NCT00913497](https://clinicaltrials.gov/study/NCT00913497) | Phase 4 | Completed | 16 | Crossover study comparing glulisine vs aspart on breakfast postprandial glucose in prepubertal children with T1DM |
| [NCT02914886](https://clinicaltrials.gov/study/NCT02914886) | Phase 4 | Completed | 14 | Investigated whether zinc-free glulisine improves injection-site lipoatrophy in T1DM patients on insulin pump therapy |
| [NCT00489190](https://clinicaltrials.gov/study/NCT00489190) | Phase 4 | Completed | 45 | 12-week open non-randomized study collecting effectiveness/safety data for subcutaneous glulisine (HMR1964) in T1DM |
| [NCT00368394](https://clinicaltrials.gov/study/NCT00368394) | Phase 1 | Completed | 18 | Dose-exposure-response study of glulisine using the euglycemic clamp technique in T1DM (doses 0.075–0.3 U/kg) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multinational RCT (n=683 randomized) comparing glulisine vs lispro efficacy/safety in T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Randomized 3-way crossover comparing glulisine vs aspart vs lispro via CSII in T1DM; trend toward fewer catheter occlusions with glulisine |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | Trial | Diabetes Technol Ther | 26-week trial in pediatric T1DM showing comparable efficacy/safety of glulisine vs lispro in basal-bolus regimen |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Trial | Diabetes Obes Metab | Compared glulisine vs lispro (with glargine as basal) for efficacy/safety in Japanese T1DM patients |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | Study | Diabetes Care | Assessed pharmacokinetics, postprandial glucose control, and safety of glulisine vs regular human insulin in pediatric T1DM |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Cohort/Comparative | Acta Diabetol | Real-world CSII cohort comparing glulisine vs lispro/aspart on HbA1c, fasting glucose, hypoglycemia and DKA rates |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine's pharmacology and clinical efficacy across diabetes populations |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Review | Drugs Today | Reviews rapid- and long-acting insulin analogues, including glulisine, for T1DM management in children/adolescents |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | PK/PD Review | Clin Pharmacokinet | Reviews clinical pharmacokinetics/pharmacodynamics of insulin glulisine vs other rapid-acting analogues |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Study | Pediatr Int | Evaluated efficacy/safety of glulisine for CSII in 20 pediatric T1DM patients over 1 year; improved postprandial glucose |

---

## Canada Market Information

Insulin glulisine currently has no Health Canada Drug Identification Number (DIN) on record in this dataset — the product is **not marketed in Canada** (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for insulin glulisine in type 1 diabetes is extensive and mature (L1, ≥2 completed Phase 3 RCTs), but this reflects confirmation of an established on-label use rather than a novel repurposing opportunity — insulin replacement is already the standard treatment for T1DM. The main open item is that Canadian regulatory and safety-labeling data are entirely missing, which blocks a formal safety review.

**To proceed, the following is needed:**
- Health Canada product monograph / package insert (key warnings, contraindications) — currently a blocking data gap
- Drug interaction (DDI) data, currently returning no results
- Confirmation of whether this candidate is intended as a genuine repurposing signal or should be reclassified as an existing-indication confirmation, given the mechanistic overlap with the drug's core use
- If commercial launch in Canada is being considered, a DIN application/licensing pathway assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

