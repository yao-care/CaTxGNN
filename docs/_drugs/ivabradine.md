---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ivabradine: From Heart-Rate Control (HCN Channel Inhibition) to Hypertrichosis

## One-Sentence Summary

Ivabradine is a cardiac drug that inhibits HCN channels (the cardiac If current) and is marketed in Canada under the brand LANCORA.
The TxGNN model predicts it may be effective for **hypertrichosis** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
It is a model-only signal, and hypertrichosis may in fact be a safety signal rather than a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data (no approved indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ivabradine inhibits HCN channels, which carry the cardiac If current, and this lowers heart rate. Detailed mechanism-of-action data was not available in the source record, so this description comes only from the pack's rationale notes.

No established mechanistic link connects HCN channel inhibition to hair growth regulation. The score is a knowledge-graph prediction only. It is likely driven by graph proximity to other hair-related disease nodes rather than by drug-specific evidence.

Directionality is also unclear. Hypertrichosis is more plausibly an adverse-effect or safety signal than a condition ivabradine would treat. Until that is clarified, the prediction should not be read as a therapeutic opportunity.

The other five predictions are also unsupported (scores 99.1% to 99.7%). They include Ambras-type hypertrichosis universalis congenita, a malformation syndrome with odontal and/or periodontal component, a Dandy-Walker malformation syndrome, isolated genetic hair shaft abnormality, and nephrogenic syndrome of inappropriate antidiuresis. None has a plausible link to HCN inhibition, and none has trial or drug-specific literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

The only literature retrieved in this pack (20 papers) belongs to the rank 3 prediction, a periodontal malformation syndrome. It consists of general periodontitis guidelines and reviews that do not mention ivabradine, so it is a non-specific keyword match and does not count as supporting evidence.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2459981 | LANCORA |
| 2459973 | LANCORA |

Dosage form and approved indication text are not recorded in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no drug-specific literature and no plausible mechanistic link. Hypertrichosis may be an adverse-effect signal rather than a therapeutic target, so the direction of effect is unresolved.

**To proceed, the following is needed:**
- Ivabradine's mechanism-of-action data from DrugBank
- The Health Canada package insert (warnings, contraindications, approved indications) for the LANCORA products
- A check of whether hypertrichosis is reported as an adverse effect of ivabradine
- Preclinical or mechanistic evidence linking HCN channels to hair follicle biology, if the therapeutic direction is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

