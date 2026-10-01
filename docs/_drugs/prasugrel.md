---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
---

# Prasugrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Prasugrel: From Acute Coronary Syndrome (PCI) to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is an oral antiplatelet drug (a P2Y12 inhibitor) used with aspirin after percutaneous coronary intervention (PCI) in acute coronary syndrome. The TxGNN model predicts it may be useful for **pulmonary hypertension**. The two clinical trials and two publications retrieved concern other conditions, so **no direct evidence** supports this prediction and it rests on the graph model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome with PCI (inferred from the retrieved literature; the Canadian label text is not in the Evidence Pack) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in structured form. The repurposing rationale describes prasugrel as an irreversible P2Y12 receptor antagonist, so it blocks ADP-driven platelet activation and aggregation.

Platelet activation and in situ thrombosis are proposed contributors to pulmonary vascular remodelling in pulmonary hypertension. On that view, an antiplatelet drug is a theoretical fit.

This link is hypothetical. No prasugrel-specific data support it, and the high TxGNN score is a graph-based prediction only. Prasugrel is also known for a relatively high bleeding risk, which would need careful weighing in any new population.

## Clinical Trial Evidence

Two trials were retrieved. Both were graded low relevance (Grade C), as neither involves prasugrel or pulmonary hypertension.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational study of non-vitamin K oral anticoagulant (NOAC) management in elderly Spanish patients with non-valvular atrial fibrillation. Not related to prasugrel or pulmonary hypertension. |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study of how many patients with cancer-associated thrombosis would be ineligible for a CARAVAGGIO-type trial. Not related to prasugrel or pulmonary hypertension. |

## Literature Evidence

Both publications are cohort studies, and neither addresses pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Factors associated with clopidogrel use and adherence in ACS patients after PCI. Prasugrel is mentioned only as a guideline-recommended alternative. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | ACTIVE COVID-19 registry analysis of how prior drug therapy for comorbidities affects COVID-19 outcomes. Not related to this indication. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2502429 | JAMP PRASUGREL |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.88%), but it comes from the knowledge graph alone. The retrieved trials and publications have no connection to prasugrel in pulmonary hypertension (Evidence Level L5). The platelet-driven vascular remodelling hypothesis is plausible but untested for this drug.

**To proceed, the following is needed:**
- Preclinical or clinical studies of P2Y12 inhibition (prasugrel or the same class) in pulmonary hypertension
- Structured mechanism-of-action data and the Health Canada package insert warnings and contraindications, which are still missing
- A bleeding-risk review for the target population
- Consideration of the better-supported **migraine disorder** prediction (rank 2, Evidence Level L3). It rests on class-level evidence (a ticagrelor pilot study and a retrospective thienopyridine review in migraine with patent foramen ovale), not prasugrel-specific trials, and it is a more realistic research question than pulmonary hypertension.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

