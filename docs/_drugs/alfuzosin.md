---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic antagonist (uroselective), used for benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH). The Canadian licence records provide no indication text, so this comes from the drug's known class use. |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Alfuzosin is a selective alpha-1 adrenergic antagonist that relaxes smooth muscle in the prostate and bladder neck, which is why it is used for BPH.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital disorder of hair-follicle development, and no mechanism connects alpha-1 blockade to it. The high score (~0.99999) reflects graph proximity in the knowledge graph, not clinical or literature evidence.

The other top predictions are also unsupported, so none is a strong lead. Some are hair-related (hypertrichosis, hypotrichosis, hair shaft abnormality), possibly through proximity to vasodilator hair-growth agents such as minoxidil. Persistent fetal circulation syndrome is the most biologically plausible, but it remains a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Six licences are recorded; the five with details are listed below. The records contain no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 02245565 | XATRAL |
| 02447576 | ALFUZOSIN |
| 02443201 | AURO-ALFUZOSIN |
| 02519844 | ALFUZOSIN |
| 02304678 | SANDOZ ALFUZOSIN |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for alfuzosin in the queried source.

A general pharmacological caution applies: alpha-1 blockade carries a risk of systemic hypotension, and alfuzosin has no neonatal safety or pharmacokinetic data. This matters for any speculative use in newborn conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials, no relevant literature, and no plausible mechanism. The 20 publications retrieved for a related periodontal-malformation prediction are general periodontitis papers, not alfuzosin studies, so they do not raise the evidence level. The direction of benefit for hair-related predictions is also doubtful, because vasodilator-type mechanisms are more often linked to excess hair growth than to its treatment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A drug-specific literature and trial search for alfuzosin with each predicted disease, in place of disease-term matching
- A mechanistic rationale, or preclinical evidence, linking alpha-1 blockade to hair-follicle or developmental pathways
- If the biologically more plausible persistent fetal circulation syndrome is pursued, neonatal safety and pharmacokinetic data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

