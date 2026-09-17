---
layout: default
title: Letermovir
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Letermovir: From CMV Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a CMV (human cytomegalovirus) terminase complex inhibitor, a narrow-spectrum antiviral with no known antifungal activity, and it currently holds no market authorization in Canada.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis** with a score of **99.88%**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic analysis flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Canadian market license); mechanistically, letermovir targets the CMV terminase complex, consistent with use in cytomegalovirus infection/prophylaxis |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap in the source record, but the evidence pack's own rationale note describes letermovir as an inhibitor of the CMV terminase complex (pUL51/pUL56/pUL89), a mechanism specific to packaging DNA during human cytomegalovirus replication. This is a narrow-spectrum antiviral mechanism with no known activity against fungal targets — it does not act on ergosterol synthesis, cell-wall β-glucan, or any other pathway relevant to *Candida* species.

Vulvovaginal candidiasis is a fungal infection caused by *Candida*, a pathogen with no biological overlap with letermovir's known target. The evidence pack itself concludes that the two indications share no mechanistic link, and that the high TxGNN score (99.88%) most likely reflects topological similarity within the knowledge graph rather than genuine pharmacological plausibility.

Given this, the prediction should be treated as **high-risk for false positive** rather than a biologically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Letermovir currently has no marketed products in Canada (0 DINs on file), so no Canadian licensing table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5) with zero clinical trials or literature, and the mechanistic review explicitly finds no biological plausibility linking an antiviral CMV-terminase inhibitor to an antifungal indication. The drug also has no current market presence in Canada, so there is no regulatory or safety foundation to build on.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently marked as a blocking/high-severity data gap)
- TFDA/Health Canada product labeling (warnings, contraindications) — currently unavailable and blocking safety review (S1)
- Any in vitro or preclinical evidence of anti-*Candida* activity to establish biological plausibility before further clinical evidence search
- DDI data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

