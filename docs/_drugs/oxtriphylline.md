---
layout: default
title: Oxtriphylline
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 3
---

# Oxtriphylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxtriphylline: From Xanthine-Class Bronchodilator to Migraine Disorder

## One-Sentence Summary

Oxtriphylline (choline theophyllinate) is a theophylline salt in the xanthine drug class; structured original-indication data is not available in this evidence pack, but xanthines are pharmacologically known as bronchodilators. The TxGNN model predicts it may be effective for **Migraine Disorder**, but currently **no clinical trials** and **no published literature** directly support this specific drug–indication link — the prediction rests solely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no approved licenses on file); pharmacologically a xanthine-class agent |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not officially available (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale accompanying this prediction, Oxtriphylline is a choline salt of theophylline, a xanthine-class compound whose pharmacology includes non-selective phosphodiesterase (PDE) inhibition and adenosine receptor (A1/A2A) antagonism.

The proposed link to migraine is a mechanistic analogy rather than direct evidence: adenosine signaling is theoretically involved in trigeminovascular pain modulation, and caffeine — another xanthine — is a common adjuvant in migraine analgesic combinations. However, this reasoning is class-based pharmacological extrapolation, not evidence specific to oxtriphylline itself.

Two closely related candidate indications were also flagged by TxGNN for this drug — "migraine with brainstem aura" (99.55%) and "migraine with or without aura, susceptibility to" (99.32%) — the latter supported by 20 publications, though those papers concern shared epilepsy–migraine genetic/molecular susceptibility mechanisms rather than any therapeutic evidence for oxtriphylline or theophylline.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

No marketing authorization found. The drug's Canada market status is **Not Marketed**, with **0 DINs** on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/label warnings and contraindications are recorded as a Blocking data gap (DG001) — this is required before any S1 safety pre-assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-evidence prediction — supported only by the TxGNN model score, with no clinical trials or literature directly evaluating oxtriphylline (or theophylline) for migraine. Combined with a Blocking-severity data gap on regulatory safety information, there is insufficient basis to advance beyond model prediction.

**To proceed, the following is needed:**
- TFDA/product label warnings, precautions, and contraindications (DG001, Blocking)
- Confirmed mechanism of action documentation from DrugBank or equivalent source (DG002, High)
- Direct preclinical or clinical evidence linking oxtriphylline/theophylline to migraine treatment
- Route and dosage-form compatibility assessment, given the drug is not currently marketed in Canada (0 DINs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

