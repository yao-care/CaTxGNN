---
layout: default
title: Deoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 258
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Deoxycholic Acid: From Submental Fat Reduction (Local Injection) to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Deoxycholic acid is a secondary bile acid that disrupts cell membranes. It is marketed in Canada as an injectable (BELKYRA) for local use under the chin.
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, a rare inherited vascular disorder.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian license data (the marketed injectable is intended for local submental use) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Deoxycholic acid is a secondary bile acid. In its marketed injectable form it acts as a membrane-disrupting agent that destroys fat cells (adipocytolysis) at the injection site.

We could not identify a credible link between this pharmacology and the predicted disease. The predicted disease is a rare single-gene disorder of the small blood vessels and their surrounding basement membrane. Nothing in the known actions of deoxycholic acid connects to that biology. The high score (99.49%) is a graph-based prediction only. No trials or publications were found to support it, so it should be treated as a model output, not as evidence of benefit.

Two other predictions in the same analysis are worth noting:
- **Brain small vessel disease 1 with or without ocular anomalies (99.49%):** This has the same problem. The 19 retrieved articles are general reviews of congenital eye anomalies. None mention deoxycholic acid or bile acids.
- **Diabetic nephropathy (99.32%):** This is the most plausible of the three, but the link is indirect. Deoxycholic acid activates the bile acid receptors TGR5 (strongly) and FXR (weakly). Signaling through these receptors has been protective in animal models of diabetic kidney disease. However, the retrieved studies tested other agents, such as a synthetic FXR/TGR5 dual agonist, UDCA and herbal formulas. None tested deoxycholic acid itself. Deoxycholic acid is also cytotoxic and its levels are often raised in metabolic disease, so the direction of effect is uncertain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2443910 | BELKYRA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials, no literature and no identifiable mechanistic link, so the evidence level is L5 (model prediction only). The injectable product is designed for local use under the chin, not for systemic exposure, which further limits its relevance to a systemic vascular disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data for deoxycholic acid (for example, from DrugBank)
- For diabetic nephropathy, which is best treated as a separate research question (evidence level L4): direct preclinical testing of deoxycholic acid, including its dose and its effect on TGR5 and FXR signaling, before any clinical consideration
- A review of whether a local-use injectable can reach the exposure a systemic indication would need

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

