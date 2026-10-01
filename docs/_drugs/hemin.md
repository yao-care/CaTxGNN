---
layout: default
title: Hemin
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Hemin
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

# Hemin: From Acute Porphyria to Thrombocytopenic Purpura

## One-Sentence Summary

Hemin (marketed in Canada as PANHEMATIN) is generally used for acute porphyria attacks. The Canadian license record supplied here does not state an indication.
The TxGNN model predicts it may be effective for **thrombocytopenic purpura**, but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Thrombocytopenic purpura |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hemin is a heme preparation, and the data pack does not record its original indication or mechanism. The porphyria use noted in the title comes from the drug's general background and from the retrieved literature context, not from the Canadian license record.

A speculative link is that hemin induces heme oxygenase-1 (HO-1), an enzyme with anti-inflammatory and immune-modulating activity. Immune-mediated platelet destruction could in principle respond to this pathway. No trial or publication in the supplied data tests this idea. The very high TxGNN score reflects knowledge-graph proximity only, and it should not be read as evidence of efficacy.

For context, the second-ranked prediction, hemophilia, has one mouse study (PMID 19890094). It found that HO-1 induction reduced the immune response to therapeutic factor VIII. That paper does not concern thrombocytopenic purpura, and it did not test hemin in humans.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2478765 | PANHEMATIN |

Dosage form and approved indication text are not available in the supplied license record.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found. Other predicted indications in this pack note that hemin has been associated with coagulation effects and thrombophlebitis. Any use in a bleeding or platelet disorder would need a careful safety review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-derived only (L5), with no clinical trials, no publications, and no documented mechanism. The safety data are also missing, so the candidate cannot advance past the initial screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data, for example from DrugBank
- A literature and trial search specific to hemin and immune thrombocytopenia or thrombocytopenic purpura
- Confirmation of the approved indication and dosage form for DIN 2478765
- A safety assessment of hemin's coagulation effects and thrombophlebitis risk in a platelet-disorder population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

