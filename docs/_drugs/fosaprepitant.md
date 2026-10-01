---
layout: default
title: Fosaprepitant
parent: Model Prediction Only (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is an intravenous prodrug of aprepitant, an NK1 receptor antagonist used to prevent chemotherapy-induced nausea and vomiting.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (the Canadian license text was not provided; this is taken from the evidence pack's description of the approved use) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, fosaprepitant is converted in the body to aprepitant, which blocks the substance P / NK1 receptor. Its efficacy in preventing chemotherapy-induced nausea and vomiting is established.

The link to the predicted indication is weak. NSIAD is caused by a gain-of-function mutation in the vasopressin V2 receptor (AVPR2), and NK1 receptor antagonism has no known role in that pathway. The high score comes from the knowledge-graph model alone, with no trials or literature behind it. At this stage the prediction should be treated as a hypothesis, not a mechanistically supported opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2363356 | EMEND IV |
| 2549379 | FOSAPREPITANT FOR INJECTION |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a very high model score but no clinical, literature, or mechanistic support (L5). NK1 antagonism has no known connection to the AVPR2-driven pathology of NSIAD.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- A plausible pharmacological rationale, or any preclinical evidence, connecting NK1 antagonism to NSIAD
- Confirmation of the Canadian approved indication text, which is missing from the licence records

**Other candidates worth noting:** Among the other nine predictions, only retinitis (rank 7, L4) has any supporting evidence. A single 2021 preclinical mouse study reports that fosaprepitant blocks UVR-B-induced NK1R expression in ocular tissues. This is indirect and does not involve clinical retinitis, so it is best treated as a research question. The multiple endocrine neoplasia (rank 5) trials only test antiemetic supportive care and do not evaluate treatment of the disease.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

