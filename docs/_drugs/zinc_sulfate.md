---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 993
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L5). In Canada: 14 DINs (14 marketed)"
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Zinc Sulfate: Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is a zinc salt found in a range of single-ingredient products marketed in Canada.
The TxGNN model predicts it may be effective for **pharyngitis**, with a score of **0.9985**, but the only randomized trial in pharyngitis itself found no benefit, so evidence remains at **L5**.
One trial of zinc lozenges addressed postoperative sore throat, a related but different condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 14 of 14) |
| Number of DINs | 14 (marketed: 14) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for zinc sulfate: "Zinc is an essential trace element. Zinc functions as a cofactor of various enzymes including DNA polymerases, RNA polymerases, alcohol dehydrogenase, and alkaline phosphatases. Zinc is a coordinator of protein structural folding, such as folding of “Zinc finger” motif that interacts with a variety of proteins, lipids, and nucleic acids." ([DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757), label version 2026-03-04; accessed 2026-11-19.) Zinc is generally thought to act locally on mucous membranes, with possible antiviral and anti-inflammatory effects and support of epithelial repair. This is a plausible but unproven rationale for the throat.

The high TxGNN score is a computational output and is not clinical evidence. The only randomized placebo-controlled trial in pharyngitis itself tested zinc sulfate for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients (PMID 23720981), and it did not show a benefit. The lozenge trial concerns sore throat after intubation, which is a different cause from infectious pharyngitis. Because no study showing benefit directly addresses the predicted disease, the evidence level is L5.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomized, double-blind, placebo-controlled study of preoperative zinc lozenges for postoperative sore throat after intubation. This is a related condition, not pharyngitis, and the product is a lozenge rather than zinc sulfate. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | Journal of the Medical Association of Thailand | Placebo-controlled trial of zinc sulfate for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients; no benefit was found for pharyngitis. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/Other | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Discusses long-lasting taste disturbance after tonsillectomy and a possible role of zinc deficiency; not a study of pharyngitis treatment. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236399 | ANODAN-HC 10MG SUPPOSITORIES | Not specified | Not specified |
| 02290596 | ALLERGY EYE DROPS | Not specified | Not specified |
| 02338602 | VISINE MULTI-SYMPTOM | Not specified | Not specified |
| 02387239 | JAMPZINC-HC | Not specified | Not specified |
| 02128446 | ANODAN-HC OINTMENT | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: Interaction data were compiled for 100 interacting drugs. Moderate-level interactions include alendronic acid, risedronic acid, ibandronate, tetracycline and baloxavir marboxil. Most other listed interactions, such as immunosuppressants and corticosteroids, are minor.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but the only randomized trial in pharyngitis itself showed no benefit, and the lozenge trial addresses a related but different condition. Evidence therefore stays at L5.

**To proceed, the following is needed:**
- A well-designed controlled trial in infectious pharyngitis with a defined zinc formulation and dose
- Mechanism-of-action data for zinc in the pharynx
- Package insert warnings and contraindications for the relevant products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

