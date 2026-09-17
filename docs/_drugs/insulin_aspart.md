---
layout: default
title: Insulin Aspart
parent: High Evidence (L1-L2)
nav_order: 405
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart (DB01306) is a rapid-acting insulin analog used to manage diabetes mellitus; the drug's original-indication record itself is a data gap, not evidence of "no indication." The TxGNN model's top prediction — **Type 1 Diabetes Mellitus** (score 99.95%) — is supported by **10 curated clinical trials** and **10 curated publications**, but this signal reflects the drug's existing, well-established core use as insulin-replacement therapy rather than a novel repurposing opportunity. A **blocking data gap** on local product-label safety information (warnings/contraindications) means this candidate cannot yet clear an initial safety screen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory license data (data gap); insulin aspart is internationally labeled for glycemic control in diabetes mellitus (type 1 and type 2) requiring insulin therapy |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (data gap, DG002). Based on known pharmacology, insulin aspart is a rapid-acting human insulin analog that binds the insulin receptor, promoting cellular glucose uptake and suppressing hepatic glucose output — mimicking physiological prandial insulin release.

Importantly, the model's own evidence annotation for this candidate flags a critical caveat: the empty `original_indications` field in this Evidence Pack is a **data-collection gap**, not a true absence of indication. Insulin aspart's replacement of deficient endogenous insulin secretion in Type 1 Diabetes is its **core, already-approved pharmacological action** — not a repurposing hypothesis. In other words, TxGNN has correctly re-identified the drug's known primary use rather than surfaced a new therapeutic opportunity.

Mechanistically this makes the prediction highly reasonable (absolute insulin deficiency in T1DM is treated by exogenous insulin replacement, full stop), but strategically it should be read as a **validation signal** confirming the model's ability to recover known drug–disease relationships, rather than as a candidate for a repurposing pipeline.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | Insulin detemir + aspart vs. insulin glargine + aspart for glycemic control in Type 1 Diabetes |
| [NCT00312104](https://clinicaltrials.gov/study/NCT00312104) | Phase 3 | Completed | 325 | Insulin detemir vs. glargine, both combined with mealtime aspart, in Type 1 Diabetes |
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Safety/efficacy of insulin aspart vs. lispro in insulin pumps, pediatric/adolescent Type 1 Diabetes |
| [NCT00598793](https://clinicaltrials.gov/study/NCT00598793) | Phase 3 | Completed | 242 | Biphasic insulin aspart 30 + metformin vs. glargine + metformin in insulin-naïve diabetes (Grade A relevance) |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Insulin detemir + aspart vs. NPH + aspart: hypoglycemia frequency in Type 1 Diabetes |
| [NCT00821795](https://clinicaltrials.gov/study/NCT00821795) | Phase 4 | Completed | 120 | Inpatient insulin analog therapy and transition to outpatient regimen (Grade B relevance) |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Insulin detemir + aspart vs. NPH + aspart, efficacy/safety in adult Type 1 Diabetes |
| [NCT00832182](https://clinicaltrials.gov/study/NCT00832182) | Phase 3 | Completed | 75 | Long-term extension trial assessing safety of insulin aspart in basal-bolus regimen, Type 1 Diabetes |
| [NCT00888732](https://clinicaltrials.gov/study/NCT00888732) | Phase 3 | Completed | 24 | PK/PD comparison of insulin aspart formulations in Type 1 Diabetes (Grade A relevance) |
| [NCT01467141](https://clinicaltrials.gov/study/NCT01467141) | Phase 4 | Completed | 26 | Meal-related insulin aspart vs. human insulin in children aged 2–6 with Type 1 Diabetes (Grade A relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: insulin degludec vs. detemir, both with aspart, in pregnant women with Type 1 Diabetes |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT/Systematic Review | Diabetes Metab | Systematic review: efficacy/safety of insulin aspart vs. regular human insulin in Type 1/2 Diabetes |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec (basal-bolus with aspart) in Type 1 Diabetes |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes Obes Metab | Double-blind crossover trial: faster-acting aspart vs. aspart with pump + CGM in Type 1 Diabetes |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster aspart vs. aspart in pregnancy/post-delivery, Type 1/2 Diabetes |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Comprehensive review of Type 1 Diabetes pathophysiology and insulin-based management |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Spotlight review on insulin aspart efficacy in Type 1 and 2 Diabetes |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Review of insulin aspart's role in management of Type 1 and 2 Diabetes |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vasc Health Risk Manag | Insulin degludec/aspart combination for Type 1 and 2 Diabetes |
| [39115159](https://pubmed.ncbi.nlm.nih.gov/39115159/) | 2024 | Cohort (post hoc) | Diabet Med | Safety/effectiveness of aspart vs. other bolus insulins in Type 1 Diabetes pregnancy |

---

## Canada Market Information

Insulin aspart currently holds **no Health Canada Drug Identification Number (DIN)** on record — the product is **not marketed in Canada** (0 licenses). No authorization or approved-indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

⚠ A **blocking data gap** (DG001) exists: local product-label warnings and contraindications could not be retrieved, which prevents this candidate from clearing an initial (S1) safety pre-assessment. Drug interaction search also returned no results (`query_status: not_found`). These gaps must be closed before any safety judgment is made.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ten completed Phase 3/4 trials and multiple RCTs/reviews directly support insulin aspart's use in Type 1 Diabetes (L1 evidence), but this reflects the drug's already-established core indication rather than a novel repurposing signal — the model is effectively re-confirming known pharmacology. A blocking gap on Health Canada label safety data means guardrails must be resolved before any downstream action.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the Health Canada/manufacturer product monograph for warnings, contraindications, and DDI data
- Resolve DG002: confirm detailed mechanism of action via DrugBank API
- Clarify the `original_indications` data gap to formally document that Type 1 Diabetes is a known, existing use rather than a new indication
- If used within a repurposing screening pipeline, flag this candidate as a **model-validation case** rather than a novel opportunity, and prioritize review of this drug's lower-ranked candidates (ranks 2–10), most of which scored L4/L5 and were recommended "Hold"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

