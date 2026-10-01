---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
---

# Olsalazine
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

# Olsalazine: From Ulcerative Colitis to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is an azo-linked dimer of 5-aminosalicylic acid (5-ASA), a gut-acting anti-inflammatory generally used for ulcerative colitis. The TxGNN model predicts it may be effective for **myelodysplastic syndrome (MDS)**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (general drug knowledge; the Canadian licence record contains no indication text) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Olsalazine is an azo-linked 5-ASA dimer with anti-inflammatory activity (NF-κB, COX/LOX, PPAR-γ and ROS-scavenging effects). Chronic inflammatory signalling is implicated in MDS, which gives a speculative rationale for the prediction.

That rationale is weak. Olsalazine is poorly absorbed and is cleaved mainly in the colon, so little drug reaches the bone marrow. No direct link between olsalazine or 5-ASA and MDS was found. The high score is best read as a model output reflecting knowledge-graph neighbourhood similarity, not as clinical support.

The other top-ranked predictions are also weak:
- **MDS-related terms** (unclassified MDS, partial deletion of the long arm of chromosome 5, refractory cytopenia of childhood): these likely overlap with the MDS prediction through shared graph neighbours. A drug targeting inflammation does not address del(5q) haploinsufficiency.
- **Hair disorders** (alopecia, diffuse alopecia areata, hypotrichosis simplex of the scalp, congenital hypotrichosis milia): only alopecia areata has a conceptual immunomodulation link, and 5-ASA is not an established treatment for it. The genetic hair disorders have no plausible link.
- **Anaemias** (aregenerative anaemia, severe congenital hypochromic anaemia with ringed sideroblasts): no plausible therapeutic link.

All ten predictions are at evidence level L5, with scores between 99.88% and 99.91%.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2063808 | DIPENTUM | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

One point from the prediction analysis is worth noting: 5-ASA compounds have rare reports of bone marrow suppression. For marrow-failure conditions such as aregenerative anaemia, a safety signal is therefore more plausible than a therapeutic benefit.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. There are no registered trials, no literature, and no established mechanistic link. Low systemic absorption further weakens the case for a bone marrow target.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism-of-action data from DrugBank
- Approved indication text and dosage form for DIN 2063808
- A systematic literature search on 5-ASA or olsalazine in MDS and in inflammation-driven marrow disorders
- Evidence that adequate systemic or marrow exposure is achievable, given olsalazine's colon-targeted release
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

