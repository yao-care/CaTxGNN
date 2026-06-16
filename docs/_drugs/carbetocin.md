---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
---

# Carbetocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Based on the Evidence Pack, here is the evaluation report for Carbetocin:

---

# Carbetocin: From Postpartum Haemorrhage Prevention to Isotretinoin-Like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting synthetic analogue of oxytocin, clinically established for preventing uterine atony and postpartum haemorrhage following Caesarean section.
The TxGNN model predicts it may be effective for **Isotretinoin-Like Syndrome**,
however **0 clinical trials** and **0 publications** currently support this direction, and mechanistic analysis strongly identifies this as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum haemorrhage prevention (established clinical use; not recoverable from Canadian licence records) |
| Predicted New Indication | Isotretinoin-Like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the sources queried. Based on established pharmacology, Carbetocin is a synthetic octapeptide analogue of oxytocin that acts as an oxytocin receptor (OXTR) agonist. It promotes sustained uterine contractions and is administered perioperatively to reduce postpartum haemorrhage. It carries no retinoid activity, no affinity at retinoic acid receptors (RAR/RXR), and no embryotoxic pathway that overlaps with retinoid signalling.

Isotretinoin-Like Syndrome — also known as retinoic acid embryopathy — is a pattern of congenital malformations (craniofacial defects, cardiac abnormalities, CNS anomalies) caused exclusively by foetal exposure to retinoid-class compounds. Its pathophysiology is entirely driven by dysregulated retinoic acid signalling during embryogenesis. Carbetocin's pharmacological profile has no known intersection with any of these mechanisms.

Mechanistic analysis indicates this prediction is most likely a **graph topology artefact** — a structural false positive arising from how the TxGNN knowledge graph represents rare syndrome nodes. The high TxGNN score (99.15%) reflects proximity within graph structure rather than biological plausibility. This conclusion is reinforced by a second top-ranked prediction, Goodman syndrome (99.06%), which also shares no credible mechanistic link with oxytocin receptor agonism and independently suggests systematic false-positive clustering on rare congenital disorder nodes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Carbetocin is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on record, and no approved indication text is available from regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction lacks any credible mechanistic connection between carbetocin's oxytocin receptor agonism and isotretinoin-like syndrome; with zero supporting clinical or preclinical evidence (L5), and parallel false-positive signals on Goodman syndrome, this is assessed as a knowledge graph topology artefact rather than a biologically plausible repurposing hypothesis.

**To proceed, the following is needed:**

- Retrieve carbetocin's full mechanism of action from DrugBank API (currently a data gap flagged as High severity)
- Obtain the full product monograph or package insert to complete the safety profile (currently a Blocking data gap)
- Conduct knowledge graph audit to investigate false-positive clustering on rare congenital syndrome nodes in TxGNN
- Independent pharmacologist review to formally rule out any unexpected oxytocin–retinoid pathway interaction before any further investment in this direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

