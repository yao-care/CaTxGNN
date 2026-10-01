---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Antifungal Therapy to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal marketed in Canada, but the supplied data does not list its approved indications.
The TxGNN model predicts it may be effective for **vulvovaginitis**, but **0 clinical trials** and **0 publications** support this specific prediction.
Because this may already be an established antifungal use rather than true repurposing, the entry needs label verification first.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (all licence indication fields are empty) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, nystatin is a polyene antifungal that binds ergosterol and disrupts the membrane of *Candida* cells. Candidal vulvovaginitis is therefore mechanistically plausible.

The main caveat is that the original indications are also missing from the data. Candidal vaginal infection may already be an established use of nystatin, in which case this prediction is not true repurposing. The retrieved literature itself notes that nystatin was introduced in the 1950s for vulvovaginal candidiasis and has since been surpassed by azoles as first choice. The prediction should be checked against the Health Canada label before it is treated as a candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: The separate prediction "vulvitis" (rank 8, score 99.83%) has 19 retrieved publications, mostly reviews of vulvovaginal candidiasis with nystatin as one comparator. It is rated L4 and is outside the scope of this entry.*

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 792667 | PMS-NYSTATIN SUSPENSION 100000 UNIT/ML | Not listed | Not listed |
| 716871 | NYADERM | Not listed | Not listed |
| 2194201 | TEVA-NYSTATIN | Not listed | Not listed |
| 2194163 | TEVA-NYSTATIN | Not listed | Not listed |
| 2433443 | JAMP-NYSTATIN ORAL SUSPENSION USP | Not listed | Not listed |

*Five of 11 licences shown.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is purely model-derived (L5), with no trials or literature for this entry. The mechanism is plausible, but the indication may already be an established antifungal use, so it cannot be judged as repurposing without the label.

**To proceed, the following is needed:**
- Health Canada product monograph (indications, warnings, contraindications) for the nystatin products
- Confirmation of whether vulvovaginitis (candidal) is already a labelled indication
- Mechanism of action data from DrugBank
- Dosage form and route data per product, to check route compatibility
- Direct trial or literature evidence, if the indication is confirmed to be new
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

