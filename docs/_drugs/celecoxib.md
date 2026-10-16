---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Celecoxib: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis…"
---

# Celecoxib
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

# Celecoxib: From Rheumatoid Arthritis and Other Inflammatory Joint Diseases to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Celecoxib is a COX-2-selective anti-inflammatory drug, originally used for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare inherited skeletal disorder.
**No clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis, juvenile idiopathic arthritis |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Celecoxib is a COX-2-selective inhibitor. It reduces prostaglandin-driven inflammation and pain, and its efficacy in arthritic conditions is well established.

The predicted indication is a rare skeletal dysplasia caused by mutations in the CDMP1/GDF5 gene. Its biology involves bone and cartilage development, not prostaglandin-mediated inflammation. No plausible link between COX-2 inhibition and this condition has been established.

The high score is therefore best read as a graph-based association, probably driven by shared connections to skeletal and joint disease. It is not evidence of a real therapeutic effect. The mechanistic rationale is weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Celecoxib is widely available in Canada through the originator brand and many generics. Dosage form and approved-indication text were not available in the data compiled for this report. Five of the 20 valid DINs are shown below.

| DIN | Product Name |
|---------|------|
| 02239942 | CELEBREX |
| 02418932 | APO-CELECOXIB |
| 02445670 | AURO-CELECOXIB |
| 02420058 | MAR-CELECOXIB |
| 02495473 | M-CELECOXIB |

All 20 authorizations are single-ingredient products and currently valid. None are cancelled.

---

## Safety Considerations

- **Disease associations flagged as contraindicated or to be used with caution** (from knowledge-graph associations, not label text):
  - Cardiovascular: hypertension, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, cardiovascular and heart disease
  - Gastrointestinal: peptic ulcer disease (including active ulcer), gallbladder disease
  - Kidney and liver: kidney disease, liver disease
  - Respiratory: asthma (intrinsic and allergic)
  - Blood: anaemia, hemoglobinopathy
  - Other: substance abuse/dependence
- **Drug Interactions** (100 interactions recorded; the first 20 returned are summarized here):
  - **Major:** eliglustat
  - **Moderate:** hydrocortisone, metformin and several sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), nateglinide, exenatide, mesalazine, balsalazide, olsalazine, cimetidine, levofloxacin, metronidazole, kanamycin, naltrexone, fenfluramine and dexfenfluramine

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications. The target disease is a genetic skeletal dysplasia with no plausible COX-2 mechanism. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking COX-2 inhibition or prostaglandin signalling to GDF5-related skeletal development
- Preclinical evidence (cell or animal models) supporting any benefit
- Detailed mechanism of action data for celecoxib
- Package insert warnings and contraindications for the Canadian products, to support a safety screen

**Note on other predictions:**
Among the other predictions for celecoxib, *inflammatory spondylopathy* (rank 9) has by far the strongest support (L1). That support includes completed Phase 3 and Phase 4 randomized trials in ankylosing spondylitis, such as NCT00648141 (n=458) and NCT02528201 (n=330), and a 2024 randomized trial of celecoxib added to anti-TNF therapy. This is largely an already-labeled indication, so it is not a true repurposing finding. If the goal is to prioritize candidates with real evidence, it deserves separate review, with cardiovascular and gastrointestinal risk managed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

