---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an antiparasitic drug, and the retrieved literature refers to its approved use against strongyloidiasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parasitic infections (e.g., strongyloidiasis). The Canadian label text was not supplied. |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ivermectin is not available in this evidence pack. Ivermectin acts mainly on glutamate-gated chloride channels in invertebrates. Fungi such as *Candida* do not have these channels, so no antifungal mechanism is established.

The original indication is parasitic (helminth) infection, while the predicted indication is a fungal infection of the vulva and vagina. The two conditions share no obvious pathophysiology or drug target. The very high score (99.95%) most likely reflects proximity in the knowledge graph to other anti-infective drugs rather than a real biological link.

The same pattern appears across the top 10 predictions. Nine of the ten are candidiasis, vaginitis or vulvitis conditions, and all are L5 with a Hold recommendation. This clustering suggests one graph-driven signal rather than ten independent findings.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For context, the only paper retrieved for any of the top 10 predictions (PMID [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/), a 2022 *BMJ Case Reports* case report) was linked to esophageal candidiasis. It describes disseminated strongyloidiasis after prolonged corticosteroid treatment. It does not show ivermectin activity against *Candida*.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2480557 | STROMECTOL |
| 2440342 | ROSIVER |

Dosage form, manufacturer and approved indication text were not provided for either authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

One point from the prediction analysis is relevant. Pediatric and neonatal safety data for ivermectin are limited. This matters for the congenital and neonatal candidiasis predictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, no supporting literature, and no plausible antifungal mechanism. Effective approved antifungals already exist for candidiasis, so there is no clear unmet need to justify pursuing this prediction now.

**To proceed, the following is needed:**
- The Health Canada package insert warnings, contraindications and approved indications, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical evidence of ivermectin activity against *Candida* species, such as in vitro susceptibility data
- Route and formulation compatibility assessment, since none has been done
- Prospective clinical studies if preclinical data turn out to be supportive

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

