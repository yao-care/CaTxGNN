---
layout: default
title: Cinchocaine
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 7
---

# Cinchocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cinchocaine: From Topical Anesthesia to Bronchitis

## One-Sentence Summary

Cinchocaine (dibucaine) is an amide local anesthetic marketed in Canada in topical products (Proctol suppositories and ointment, Teva-Proctosone).
The TxGNN model predicts it may be effective for **bronchitis**, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction (L5), and the proposed link is speculative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (the indication text is not listed in the Canadian licence records) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Cinchocaine is an amide local anesthetic that blocks voltage-gated sodium channels. Its use in local anesthesia is established, but the source record lists no original indications.

Any link to bronchitis would be symptomatic only, for example by dampening airway sensory nerve activity and the cough reflex. Cinchocaine has no known anti-infective or anti-inflammatory effect, so it would not treat the cause of bronchitis. The high score (0.998) reflects proximity in the knowledge graph. No trial or publication supports it, so the mechanistic rationale is weak.

The other six predictions (acrodermatitis chronica atrophicans, neonatal dermatomyositis, childhood connective-tissue-disease-associated interstitial lung disease, acne keloid, familial hydroa vacciniforme, amyopathic dermatomyositis) score 99.6–99.8%. All are L5 with no trials or literature, and all have the same problem. At best, a topical anesthetic could relieve local pain or itch, and it would not modify the disease.

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
| 02247882 | PROCTOL SUPPOSITORIES |
| 02247322 | PROCTOL OINTMENT |
| 02226383 | TEVA-PROCTOSONE |

Dosage form and approved indication text are not provided for these licences. All three are topical or rectal products. There is no inhaled or systemic formulation that would suit a respiratory indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5), and the sodium channel blocking mechanism offers no disease-modifying rationale for bronchitis. The marketed products are topical or rectal, so the route does not fit a respiratory indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (from DrugBank)
- Approved indication text and dosage forms for the three Canadian licences
- Route compatibility assessment (topical or rectal versus respiratory use)
- Any preclinical or clinical evidence linking cinchocaine to airway disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

