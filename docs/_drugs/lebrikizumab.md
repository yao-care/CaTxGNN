---
layout: default
title: Lebrikizumab
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From Atopic Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is an anti-IL-13 monoclonal antibody, marketed in Canada as EBGLYSS and used for moderate-to-severe atopic dermatitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (inferred from the drug's trial programme; the Canadian licence records contain no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lebrikizumab is a high-affinity monoclonal antibody that neutralizes IL-13. It blocks formation of the IL-4Rα/IL-13Rα1 heterodimer signaling complex, a central type 2 inflammatory pathway in atopic dermatitis. Formal mechanism-of-action data are not available in the source record, so this description comes from the trial and literature context.

The link to diabetic retinopathy is weak. The disease is driven mainly by retinal inflammation and VEGF-mediated angiogenesis, and a role for IL-13 is speculative. The high score most likely reflects the model's knowledge-graph associations rather than an established biological rationale. No trials or publications were found to support it.

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
| 2549131 | EBGLYSS |
| 2549123 | EBGLYSS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature, and the mechanistic link between IL-13 blockade and retinal microvascular disease is hypothetical. Other high-scoring predictions for this drug are also weak, for example drug-induced osteoporosis, where IL-13 blockade could plausibly worsen bone loss. The only prediction with strong evidence is dermatitis (rank 5, L1), which is the drug's own marketed indication and not a true repurposing case.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence that IL-13 contributes to diabetic retinopathy
- Confirmation of the original indication from the Canadian product monograph, since the licence records contain no indication text
- Safety data from the Health Canada package insert, including ocular adverse events, which matter for a retinal indication
- Formal mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

