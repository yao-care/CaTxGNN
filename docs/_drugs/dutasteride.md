---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha reductase inhibitor, marketed in Canada mainly for benign prostatic hyperplasia (BPH) and also used to reduce androgen-driven hair loss.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The mechanistic rationale is weak, and the predicted direction may be opposite to the drug's known effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (not stated in the Canadian license records provided; based on the drug's generally known labelled use) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dutasteride inhibits 5-alpha reductase types 1 and 2, the enzymes that convert testosterone to dihydrotestosterone (DHT). Lowering DHT shrinks the prostate in BPH. It also reduces hair-follicle miniaturisation in androgenetic alopecia, so the drug is used to reduce hair loss.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital condition linked to genomic rearrangements near *TRPS1*, and it is not androgen-driven. In addition, dutasteride's known hair effect is to preserve hair, whereas the predicted disease involves excessive hair growth, so the predicted direction may be opposite to the drug's effect. The high score likely reflects a knowledge-graph association with hair phenotypes rather than a genuine therapeutic direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sixteen licenses are on record; the five main ones are listed below. Dosage form and approved-indication text were not available in the records provided.

| DIN | Product Name |
|---------|------|
| 02247813 | AVODART |
| 02408287 | TEVA-DUTASTERIDE |
| 02484870 | JAMP DUTASTERIDE |
| 02443058 | DUTASTERIDE |
| 02485672 | AG-DUTASTERIDE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or literature. The mechanism does not fit a non-androgen-driven congenital disorder, and the effect may run in the opposite direction, so there is no basis to advance this indication.

**To proceed, the following is needed:**
- A plausible mechanistic rationale connecting DHT reduction to the *TRPS1*-related pathology, or preclinical data supporting one
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank

**Other predictions worth noting:** Among the other nine predictions, only **hypotrichosis simplex of the scalp** (score 99.77%, evidence level L4) is biologically adjacent. Dutasteride has clinical evidence in androgenetic alopecia, so this is better framed as a research question than as a recommendation. Any extrapolation would need a genotype-specific rationale.

The 20 periodontitis papers retrieved for the third prediction (10 shown) are general periodontal literature. None mention dutasteride, so they should not be counted as drug-specific evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

