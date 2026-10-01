---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 981
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a viral neuraminidase inhibitor used against influenza A and B.
The TxGNN model predicts it may be effective for **pyelonephritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza A/B (the Canadian license record does not list indication text) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Zanamivir is a neuraminidase (sialidase) inhibitor, a class that acts on influenza A and B viruses.

Pyelonephritis is a kidney infection caused mainly by bacteria, such as uropathogenic *E. coli*. Zanamivir has no established antibacterial activity, and no credible mechanistic link between the two was found. The very high score (99.84%) is a graph-based prediction only. With no trials or literature behind it, it may be an artifact of the knowledge graph. The original indication and mechanism data are also missing from the input, so the prediction cannot be cross-checked against them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2240863 | RELENZA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). No trials or publications exist for pyelonephritis, and the pharmacology (antiviral, neuraminidase inhibition) does not plausibly fit a bacterial kidney infection.

The second-ranked prediction, disorder of tyrosine metabolism (score 99.02%), is also on Hold. Its three retrieved publications concern influenza neuraminidase inhibitor resistance and assays, not that disease, so they give no clinical support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original indication and dosage form details for the Canadian license
- Any direct preclinical or clinical evidence linking zanamivir to pyelonephritis, plus an assessment of route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

