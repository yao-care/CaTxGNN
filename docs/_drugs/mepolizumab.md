---
layout: default
title: Mepolizumab
parent: Model Prediction Only (L5)
nav_order: 590
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-05
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). In Canada: 3 DINs (3 marketed)"
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Mepolizumab: Thrombocytopenia due to immune destruction
{: .text-alpha }

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody, originally associated with eosinophilic pneumonia and pulmonary eosinophilia.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but the current evidence is very limited: **0 clinical trials** and **1 publication** (a case report) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mepolizumab: "Mepolizumab is an IL-5 antagonist (IgG1 kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Mepolizumab binds to IL-5 with a dissociation constant of 100 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil cell surface." ([DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea), label version 2025-08-06; accessed 2026-11-19.) Based on known information, mepolizumab is an anti-IL-5 monoclonal antibody that depletes eosinophils. Its role in eosinophil-driven conditions such as eosinophilic pneumonia is consistent with this mechanism.

The link to immune-mediated thrombocytopenia is weak and indirect. The only linked publication is a case report in which a steroid-resistant hypereosinophilic immune disorder, accompanied by a mixed thrombotic microangiopathy, improved with mepolizumab plus concomitant therapy. This suggests that eosinophil-driven immune dysregulation may coexist with immune-mediated cytopenias.

There is no direct evidence that IL-5 blockade treats immune thrombocytopenia itself. Its pathogenesis is mainly autoantibody-mediated platelet destruction and impaired platelet production. The high TxGNN score is a computational prediction and should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells Mol Dis | A steroid-resistant hypereosinophilic immune disorder resolved with mepolizumab, with concurrent improvement of a mixed thrombotic microangiopathy. Single patient; indirect relevance to immune thrombocytopenia. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02530821 | NUCALA | Not specified | Not specified |
| 02492997 | NUCALA | Not specified | Not specified |
| 02492989 | NUCALA | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found, and no contraindication records were found in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a single indirect case report. There are no clinical trials, and there is no established mechanistic link between IL-5 blockade and immune-mediated platelet destruction. Mepolizumab is marketed in Canada, but for other uses.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic assessment
- Health Canada package insert warnings, contraindications and approved indication text, which are required before safety screening
- Preclinical or mechanistic studies showing a role for IL-5 or eosinophils in immune thrombocytopenia
- Observational data or clinical trials in patients with immune thrombocytopenia, particularly those with coexisting hypereosinophilia

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

