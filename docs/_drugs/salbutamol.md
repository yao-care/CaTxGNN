---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 703
evidence_level: L5
indication_count: 10
---

# Salbutamol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the report template supplied to generate the pharmacist-facing evaluation for this candidate. This is a content-formatting task, not a coding/debugging task, so no other skill applies.

# Salbutamol: From Asthma/Bronchospasm to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol (DrugBank DB01001) is a short-acting β2-adrenergic agonist bronchodilator; specific original-indication and Canadian market-authorization data are not available in the current evidence pack (0 licenses recorded, "Not Marketed"). The TxGNN model predicts an extremely high association with **Papillary Conjunctivitis**, but as of today this signal is supported by **zero clinical trials and zero publications**, making it a purely model-driven prediction with no external evidence backing it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no Canadian licenses on file) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, salbutamol is a selective β2-adrenoceptor agonist whose established action is relaxation of bronchial smooth muscle, used clinically for relief of bronchospasm in obstructive airway conditions (this is reflected further down this same candidate's prediction list, e.g. bronchitis and obstructive lung disease, which carry much stronger evidence — see Data Gaps below).

For papillary conjunctivitis specifically, no known direct physiological pathway connects β2-adrenoceptor bronchodilation to papillary (typically contact-lens or allergic) conjunctival surface inflammation. The TxGNN knowledge-graph score is very high, but this appears to be a network-proximity artifact rather than a mechanistically grounded signal — there is no supporting clinical trial or literature evidence in this pack to corroborate it.

Given the absence of both a plausible mechanism and any corroborating evidence, this specific prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

No Health Canada drug licenses are recorded for salbutamol in this evidence pack. Market status is listed as **Not Marketed**, with **0 DINs** on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has an extremely high TxGNN score but Evidence Level L5 — no clinical trials, no literature, and no plausible mechanistic link between β2-agonist bronchodilation and papillary conjunctivitis. There is currently nothing beyond the model score to act on.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for salbutamol
- Canadian regulatory/licensing data (currently 0 licenses on file — confirm whether the drug is genuinely unmarketed or the record is incomplete)
- Original indication documentation to enable proper comparative rationale
- Targeted literature/trial search specific to β2-agonists and ocular surface inflammation, to determine whether this is a true signal or a knowledge-graph artifact
- TFDA/Health Canada label warnings and contraindications (currently missing — flagged as a blocking data gap for safety review)

**Note:** This candidate's evidence pack contains several other predicted indications for salbutamol with substantially stronger support (e.g., *bronchitis* — L2, Proceed with Guardrails; *anaphylaxis* — L2, Proceed with Guardrails; *obstructive lung disease* — L1, Proceed with Guardrails). Those may warrant separate evaluation reports, as they represent materially different risk/evidence profiles than the top-ranked prediction covered here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

