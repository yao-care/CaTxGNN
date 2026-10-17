---
layout: default
title: Efinaconazole
parent: Model Prediction Only (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Efinaconazole: predicted new indication Astigmatism (evidence level L5). Approved use: Tinea unguium (onychomycosis)"
monitor_inn: "Efinaconazole"
predicted_indications: ["astigmatism (disease)", "dermatitis, atopic", "dislocated elbows, bowed tibias, scoliosis, deafness, cataract, microcephaly, and intellectual disability", "nasal cavity olfactory neuroblastoma", "apraxia of eyelid opening", "spastic paraplegia, optic atrophy, microcephaly, and 10Y sex reversal", "craniosynostosis-anal anomalies-porokeratosis syndrome", "macular degeneration", "tumor suppressor gene on chromosome 11", "nasal cavity lymphoma"]
---

# Efinaconazole
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

# Efinaconazole: From Tinea Unguium to Astigmatism

## One-Sentence Summary

Efinaconazole is a topical triazole antifungal originally used to treat tinea unguium (nail fungal infection, onychomycosis).
The TxGNN model lists **astigmatism** as its top predicted new indication, but the score is non-discriminating (0.5), and **0 clinical trials** and **0 publications** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea unguium (onychomycosis) |
| Predicted New Indication | Astigmatism |
| TxGNN Prediction Score | 50% (non-discriminating) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, efinaconazole is a topical triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (sterol 14α-demethylase), blocking ergosterol synthesis. Its efficacy in nail fungal infection is established.

For astigmatism, no plausible mechanistic link exists. Astigmatism is a refractive error of the cornea or lens, unrelated to fungal ergosterol biosynthesis. The score of 0.5 is uninformative, and there are no clinical or literature data supporting the prediction. In practical terms, this prediction should be regarded as a model artifact rather than a credible repurposing signal.

The other nine predictions generated for this drug share the same 0.5 score and the same lack of evidence. The most notable is atopic dermatitis, where a tenuous link can be argued (azoles may reduce fungal colonization such as Malassezia), but efinaconazole has no demonstrated activity in this setting. The other predicted indications are rare genetic syndromes, tumours, and eye or neurological disorders, none with a plausible mechanism for a topical nail antifungal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for astigmatism.

For reference, the only publication linked to any of the drug's predicted indications (listed under atopic dermatitis) concerns the approved use, not a new indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24850511](https://pubmed.ncbi.nlm.nih.gov/24850511/) | 2014 | Review | Expert Rev Anti Infect Ther | Review of efinaconazole 10% nail solution (Jublia) for onychomycosis: it inhibits sterol 14α-demethylase and has lower MICs than terbinafine, ciclopirox, itraconazole and amorolfine against *T. rubrum*, *T. mentagrophytes* and *C. albicans*. It contains no atopic dermatitis evidence. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02413388 | JUBLIA | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for astigmatism rests on a non-discriminating model score (0.5) alone. It has no clinical trials, no literature, and no plausible mechanism, and the same holds for the other nine predicted indications. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for efinaconazole (e.g., from DrugBank)
- Health Canada package insert warnings and contraindications
- A new prediction run or independent evidence that gives discriminating scores before any new indication is pursued
- If a secondary direction is of interest, preclinical or clinical evidence for atopic dermatitis (the only indication with even a tenuous rationale)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

