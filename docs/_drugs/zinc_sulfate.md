---
layout: default
title: Zinc Sulfate
parent: High Evidence (L1-L2)
nav_order: 993
evidence_level: L2
indication_count: 4
last_modified_at: 2026-11-04
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L2). Approved use: Not recorded in the local data"
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

Zinc sulfate is a zinc salt found in a number of single-ingredient products marketed in Canada.
The TxGNN model predicts it may be useful for **pharyngitis**, a prediction with a score of 0.9985.
Supporting evidence is **1 clinical trial** and **2 publications**, and it is mixed: a randomized trial of zinc lozenges reduced postoperative sore throat, while a randomized trial in radiation-induced pharyngitis found no benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L2 |
| Canada Market Status | Marketed (valid licenses: 14 of 14) |
| Number of DINs | 14 (valid: 14) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Zinc is plausibly active in the throat through local mucosal effects: antiviral activity, anti-inflammatory action, and support of epithelial repair.

A randomized, double-blinded, placebo-controlled trial of zinc lozenges (NCT02405832, n=87) reported fewer and milder cases of sore throat after intubation. This is a post-surgical, intubation-related sore throat rather than infectious pharyngitis, and the product was a lozenge rather than zinc sulfate, so the fit is partial. A randomized trial of zinc sulfate in head and neck cancer patients receiving radiotherapy (PMID 23720981) tested relief of radiation-induced mucositis and pharyngitis, and found no benefit. The very high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Zinc lozenges vs placebo before surgery; reduced incidence and severity of postoperative sore throat |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | Journal of the Medical Association of Thailand | Zinc sulfate vs placebo for radiation-induced oral mucositis and pharyngitis in head and neck cancer; no benefit found |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/Other | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Long-lasting taste disturbance after tonsillectomy; discusses a possible role of zinc deficiency |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236399 | ANODAN-HC 10MG SUPPOSITORIES | Not specified | Not specified |
| 02290596 | ALLERGY EYE DROPS | Not specified | Not specified |
| 02338602 | VISINE MULTI-SYMPTOM | Not specified | Not specified |
| 02387239 | JAMPZINC-HC | Not specified | Not specified |
| 02128446 | ANODAN-HC OINTMENT | Not specified | Not specified |

All 14 licences are valid.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Examples include moderate-level interactions with alendronic acid, risedronic acid, ibandronate, tetracycline and baloxavir marboxil. Many other listed interactions are minor, such as those with hydrocortisone, dexamethasone, betamethasone, triamcinolone, azathioprine and adalimumab.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed randomized placebo-controlled trial supports zinc in reducing postoperative sore throat, which places the evidence at L2. However, that setting differs from infectious pharyngitis, and the radiation-induced pharyngitis trial found no benefit. The high TxGNN score alone is not enough.

**To proceed, the following is needed:**
- A trial in infectious pharyngitis using the intended zinc sulfate formulation and route
- Confirmation of the design and results of the published trials
- Mechanism-of-action data
- Package insert warnings and contraindications from Health Canada

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

