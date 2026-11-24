---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 671
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: predicted new indication Disease of orbital region (evidence level L5). In Canada: 11 DINs (10 marketed)"
---

# Nystatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Nystatin: Disease of orbital region
{: .text-alpha }

## One-Sentence Summary

Nystatin is a polyene antifungal medicine marketed in Canada in oral and topical products.
The TxGNN model predicts it may be effective for **disease of orbital region**, but the data compiled for this report contain **no clinical trials and no publications** that study this condition with nystatin. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Disease of orbital region |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 10 of 11; cancelled: 1) |
| Number of DINs | 11 (marketed: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for nystatin: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), label version 2026-02-06; accessed 2026-11-19.) Nystatin belongs to the polyene antifungal class. Polyenes bind ergosterol in fungal cell membranes, which disrupts the membrane and kills the fungus.

No plausible mechanistic link between this antifungal action and orbital disease was identified. Orbital disease covers many non-fungal conditions, such as inflammatory, vascular and neoplastic problems. Nystatin has no recognised effect on these. The high score (0.9990) is a model output only and is not backed by any study of nystatin in the orbit.

## Clinical Trial Evidence

One trial was linked to this prediction. It is not relevant evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | Recruiting | 42 | Tests ASP7317, a cell-based therapy, for geographic atrophy in age-related macular degeneration. It does not involve nystatin and does not address orbital disease. |

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Nystatin products are marketed in Canada. Of the 11 licences on record, 10 are valid and 1 is cancelled. The records contain no indication text or dosage form.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00550507 | TEVA-TRIACOMB | GRAMICIDIN; NEOMYCIN (NEOMYCIN SULFATE); NYSTATIN; TRIAMCINOLONE ACETONIDE | Marketed |
| 00716871 | NYADERM | NYSTATIN | Marketed |
| 00716901 | NYADERM | NYSTATIN | Marketed |
| 00717002 | VIADERM KC CRM | GRAMICIDIN; NEOMYCIN (NEOMYCIN SULFATE); NYSTATIN; TRIAMCINOLONE ACETONIDE | Marketed |
| 00717029 | VIADERM KC ONT | GRAMICIDIN; NEOMYCIN (NEOMYCIN SULFATE); NYSTATIN; TRIAMCINOLONE ACETONIDE | Marketed |
| 00792667 | PMS-NYSTATIN SUSPENSION 100000 UNIT/ML | NYSTATIN | Marketed |
| 01926829 | FLAGYSTATIN | METRONIDAZOLE; NYSTATIN | Marketed |
| 02022818 | THERADERM CREAM | GRAMICIDIN; NEOMYCIN (NEOMYCIN SULFATE); NYSTATIN; TRIAMCINOLONE ACETONIDE | Marketed |
| 02194201 | TEVA-NYSTATIN | NYSTATIN | Marketed |
| 02433443 | JAMP-NYSTATIN ORAL SUSPENSION USP | NYSTATIN | Marketed |
| 02194163 | TEVA-NYSTATIN | NYSTATIN | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the interaction database, but their severity levels are unclassified. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, tramadol, lorazepam and bortezomib. These need review before any new use is considered.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications and no plausible mechanism. The only linked trial is unrelated to nystatin. The evidence level is L5, so the model score alone does not justify moving forward.

**To proceed, the following is needed:**
- A defined mechanistic hypothesis for how an antifungal would act on a specific orbital condition
- Published or registered studies that directly examine nystatin in orbital disease
- Package insert warnings and contraindications for the Canadian products
- Severity classification of the listed drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

