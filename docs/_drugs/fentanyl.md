---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 379
evidence_level: L5
indication_count: 2
---

# Fentanyl
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

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist, marketed in Canada in several injectable and oral products. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone, and the mechanistic review found no credible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (Health Canada indication text is empty); fentanyl is generally known as an opioid analgesic |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Fentanyl is a mu-opioid receptor agonist. No known pharmacology connects it to the pathway that drives NSIAD.

NSIAD is caused by gain-of-function variants in *AVPR2* (for example R137C/L) or, in some cases, *GNAS*. These variants make the vasopressin V2 receptor signal constantly, regardless of circulating vasopressin. Fentanyl has no known action on the V2 receptor or its downstream pathway.

Opioids are more often associated with increased vasopressin release and hyponatremia, which could worsen NSIAD rather than treat it. The high TxGNN score (99.46%) is most likely an artifact of proximity in the knowledge graph, not a biologically supported signal. Because the Evidence Pack has no original mechanism data or original indications, the score cannot be checked against known pharmacology.

The second-ranked prediction, Tourette syndrome (score 99.05%), is also weak. Endogenous opioid modulation of striatal dopamine circuits offers only an indirect rationale, and it does not extend to a potent full mu-agonist like fentanyl.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and approved-indication text are not available in the data.

| DIN | Product Name |
|---------|------|
| 2408015 | FENTORA |
| 2496186 | FENTANYL INJECTION BP |
| 2506963 | FENTANYL CITRATE INJECTION |
| 2282976 | TEVA-FENTANYL |
| 2311925 | TEVA-FENTANYL |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results, so this is not evidence of no interactions.

The mechanistic review raised these fentanyl-related concerns for the predicted use:
- Opioids tend to increase vasopressin release and cause hyponatremia, which could aggravate NSIAD.
- Fentanyl carries risks of respiratory depression, abuse liability, tolerance and dependence.

Please refer to the package insert for full safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or literature. The mechanistic review found no credible link between mu-opioid agonism and the V2 receptor pathway in NSIAD, and opioid effects on vasopressin could worsen the condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking fentanyl to V2 receptor signaling or NSIAD; without it, this candidate should not advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

