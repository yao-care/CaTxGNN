---
layout: default
title: Guanfacine
parent: Model Prediction Only (L5)
nav_order: 441
evidence_level: L5
indication_count: 7
---

# Guanfacine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Guanfacine: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Guanfacine is an extended-release alpha-2A adrenergic agonist marketed in Canada (for example as INTUNIV XR), and it is generally used for ADHD. The supplied record lists no original indication, so this is based on known labeling. The TxGNN model predicts it may be effective for **faciodigitogenital syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (from known product labeling; the supplied Canadian license records contain no indication text) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known pharmacology, guanfacine is a selective alpha-2A adrenergic agonist. It strengthens prefrontal cortical regulation of attention and impulse control, which is the basis for its efficacy in ADHD.

The link to faciodigitogenital syndrome is unclear. This is a rare developmental condition with facial, digital and genital anomalies. The evidence review found no identifiable pharmacological rationale, and no trials or literature connect guanfacine to this condition. The very high score (0.9997) is a model prediction only and should not be read as clinical support.

One possible explanation is that the model is picking up behavioural or attention-related features that overlap with ADHD. That is unverified and is not supported by anything in the evidence pack.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

12 licenses are registered in total. The records supplied contain product names only, with no dosage form or approved indication text. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02523736 | APO-GUANFACINE XR |
| 02409127 | INTUNIV XR |
| 02523558 | JAMP GUANFACINE XR |
| 02523574 | JAMP GUANFACINE XR |
| 02523582 | JAMP GUANFACINE XR |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Level L5). There are no trials, no literature and no plausible mechanistic link to guanfacine, so the score is more likely a knowledge-graph artifact than a real repurposing signal.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence linking guanfacine to faciodigitogenital syndrome
- Mechanism of action data (DrugBank) to test whether a mechanistic link exists
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Canadian licenses

**Note on other candidates:** This report covers only the top-ranked prediction. The same evidence pack contains a far better supported candidate, **Tourette syndrome** (rank 7, Level L1). It has a completed Phase 3 placebo-controlled trial ([NCT00004376](https://clinicaltrials.gov/study/NCT00004376), n=35), a completed Phase 4 study ([NCT01547000](https://clinicaltrials.gov/study/NCT01547000), n=34), and guideline and systematic review literature. It should be evaluated in a separate report.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

