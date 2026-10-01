---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 387
evidence_level: L5
indication_count: 1
---

# Fluconazole
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

# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an azole antifungal, but the supplied record lists no original indications, so its antifungal use here comes from general drug knowledge.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**.
**No clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (general drug class knowledge; not listed in the supplied record) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Fluconazole is known to inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis and stops fungal cell membranes from forming properly.

Punctate epithelial keratoconjunctivitis is most often caused by adenovirus or by immune-mediated inflammation of the ocular surface. A direct antifungal mechanism therefore does not plausibly apply. The high score may come from indirect links in the knowledge graph to ocular surface or keratitis-related nodes, such as fungal keratitis. This cannot be confirmed from the data provided.

At present the link is computational only. No original indications or mechanism data were supplied, and similarity to the original indication has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorizations are listed below. Dosage form and approved indication text are not available for these products.

| DIN | Product Name |
|---------|------|
| 02141442 | DIFLUCAN ONE |
| 02310686 | PRO-FLUCONAZOLE |
| 02241895 | APO-FLUCONAZOLE-150 |
| 02245643 | PMS-FLUCONAZOLE |
| 02547864 | JAMP FLUCONAZOLE 150 MG |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or literature behind it (Evidence Level L5). The mechanism is also implausible for the likely causes of this condition, so there is not enough support to advance it.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Original indication and approved indication text for the Canadian products
- Any clinical or preclinical evidence linking fluconazole to punctate epithelial keratoconjunctivitis or a related ocular condition
- A route-compatibility check, since ocular use may require a different formulation from the marketed products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

