---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 535
evidence_level: L5
indication_count: 2
---

# Leuprolide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Leuprolide: From Hormone-Suppression Therapy to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH agonist that suppresses sex hormones, and it is marketed in Canada under brands such as Lupron Depot and Eligard.
The TxGNN model predicts it may be effective for **osteoarthritis**, but only **1 clinical trial** and **1 publication** were retrieved, and neither studies osteoarthritis.
This prediction rests on the model score alone, with no supporting clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data and the original indications are not available in the input. Leuprolide is known to be a GnRH agonist. Continuous exposure suppresses gonadal sex hormones (estrogen and androgen).

We could not identify a credible mechanistic link to osteoarthritis. Chronic hypoestrogenism and hypoandrogenism are generally associated with bone loss and possible joint adverse effects. A benefit in osteoarthritis is therefore implausible. The score of 0.997 is a graph-based output only, and no clinical signal supports it.

The second-ranked prediction, **pseudoachondroplasia** (score 99.69%), has no trials or literature at all. This skeletal dysplasia is caused by COMP gene mutations that lead to chondrocyte ER stress. Leuprolide does not target this pathway. The only speculative link is that GnRH agonists delay pubertal growth plate closure, which is not disease-modifying. It is not evaluated further here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | N/A | Orchiectomy/LHRH analog + flutamide, with or without suramin and hydrocortisone, in metastatic prostate cancer. It does not study osteoarthritis (relevance grade C), so its Phase 3 label is not evidence for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostatic adenocarcinoma mimicking inflammatory breast carcinoma. It is unrelated to osteoarthritis. |

---

## Canada Market Information

Showing 5 of 12 authorizations. Dosage form and approved indication text are not available in the input.

| DIN | Product Name |
|---------|------|
| 2230248 | LUPRON DEPOT |
| 2248239 | ELIGARD |
| 2268892 | ELIGARD |
| 836273 | LUPRON DEPOT |
| 2248240 | ELIGARD |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The one retrieved trial and one publication are both prostate-cancer-related and give no direct or indirect evidence for osteoarthritis. The known pharmacology (sex hormone suppression, with bone-loss risk) argues against benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data and the original indications
- Any preclinical or clinical evidence linking GnRH agonists to osteoarthritis outcomes
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

