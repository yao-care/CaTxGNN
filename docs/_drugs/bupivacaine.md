---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Bupivacaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is an amide local anesthetic that blocks voltage-gated sodium channels. The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans** (score 99.23%), but **no clinical trials and no publications** currently support this direction. The prediction is model output only, with no plausible pharmacological rationale, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data (drug class: amide local anesthetic) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Bupivacaine is known as an amide local anesthetic that blocks voltage-gated sodium channels. Its efficacy in local anesthesia and nerve block is well established, but the Evidence Pack does not record its original indications.

**The prediction is not mechanistically supported.** Acrodermatitis chronica atrophicans is the late skin manifestation of *Borrelia* infection (Lyme borreliosis), so the treatment target is the pathogen. Sodium channel blockade does not address that target. The high score (0.992) reflects a knowledge-graph association only.

The other top predictions for this drug are also unsupported:

- **Neonatal dermatomyositis** (score 99.15%)
- **Childhood secondary interstitial lung disease associated with a connective tissue disease** (score 99.11%)
- **Amyopathic dermatomyositis** (score 99.03%)

Three of the four predictions are dermatomyositis-spectrum diseases. This clustering suggests a shared knowledge-graph neighborhood artifact rather than independent biological signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Bupivacaine has 16 licences in Canada. The five main ones are listed below. Dosage form and approved indication text are not available for these entries.

| DIN | Product Name |
|---------|------|
| 2241917 | MARCAINE |
| 2443694 | BUPIVACAINE INJECTION BP |
| 2460645 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP |
| 2512424 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP |
| 1976168 | SENSORCAINE |

---

## Safety Considerations

- **Myotoxicity:** Bupivacaine is known to be myotoxic. This is a specific concern for the predicted dermatomyositis-spectrum indications, which involve inflammatory muscle disease.
- **Drug Interactions:** No interaction records were found for this drug.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials or publications, and no plausible mechanism links sodium channel blockade to a *Borrelia*-driven skin condition. The score is high, but nothing independent supports it.

**To proceed, the following is needed:**
- Mechanism of action and original indication data (from DrugBank)
- Health Canada package insert warnings and contraindications, needed before any safety screening
- Any independent clinical or literature evidence linking bupivacaine to the predicted indication
- Route compatibility assessment, which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

