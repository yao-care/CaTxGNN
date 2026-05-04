---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Domperidone: From Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripherally-acting dopamine D2 receptor antagonist widely used as a prokinetic and antiemetic agent for nausea, vomiting, and gastroparesis.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
however, with **0 clinical trials** and **0 publications** currently supporting this direction, and a mechanistic rationale assessed as extremely weak, this candidate warrants caution before further investment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (drug not marketed in Canada; no DIN on record) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Domperidone is a peripherally-acting dopamine D2 receptor antagonist that does not cross the blood-brain barrier. Its therapeutic effects are confined primarily to the gastrointestinal tract and the chemoreceptor trigger zone, where D2 blockade accelerates gastric emptying and suppresses nausea.

NSIAD is a rare X-linked genetic disorder caused by gain-of-function mutations in the *AVPR2* gene, leading to constitutive activation of the V2 vasopressin receptor independent of circulating ADH levels. This drives sustained intracellular cAMP elevation, persistent upregulation of aquaporin-2 (AQP2) water channels in the renal collecting duct, and consequently chronic, dilutional hyponatremia that does not respond to standard SIADH treatments such as fluid restriction.

The mechanistic connection between Domperidone and NSIAD is extremely tenuous. While the renal dopamine D1/D2 system is known to modulate AQP2 membrane trafficking under normal physiological conditions, this compensatory pathway is overwhelmed by the constitutive *AVPR2* mutation in NSIAD, leaving minimal therapeutic space for dopaminergic intervention. Since Domperidone does not cross the blood-brain barrier, it cannot modulate hypothalamic ADH release — a route irrelevant to NSIAD in any case, given that ADH is already suppressed. Critically, there is a theoretical adverse risk: blocking renal dopamine's compensatory downregulation of AQP2 could *worsen* hyponatremia rather than relieve it. The TxGNN high score (99.08%) most likely reflects indirect graph connections between D2 receptor nodes and water-electrolyte regulation nodes in the knowledge graph, rather than a genuine therapeutic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Domperidone currently holds no Drug Identification Numbers (DINs) in Canada. No approved product licenses are on record.

> **Note:** Domperidone has a complex regulatory history in North America. Health Canada has restricted its availability due to cardiac safety concerns (QT prolongation and risk of sudden cardiac death), and it is not approved for routine sale. This regulatory context is an additional barrier relevant to any repurposing strategy.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable for this evidence pack. Please refer to the package insert and Health Canada product monograph for safety information.

> **Known class concern:** Domperidone carries a well-documented risk of **QT interval prolongation and ventricular arrhythmia**, particularly at higher doses or in patients with pre-existing cardiac conditions or electrolyte imbalances. NSIAD patients are characteristically hyponatremic; hyponatremia itself prolongs the QT interval, potentially compounding cardiac risk if Domperidone were used in this population. This interaction deserves specific attention in any future evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported exclusively by a computational model prediction (L5 evidence), with zero clinical trials, zero observational data, and zero published literature linking Domperidone to NSIAD. The mechanistic rationale is not merely weak — it identifies a plausible pathway toward harm (worsening hyponatremia via D2-mediated AQP2 upregulation), and the drug's known cardiac safety profile (QT prolongation) presents additional risk in a population with baseline electrolyte disturbance. The high TxGNN score appears to be a knowledge-graph artefact rather than a signal of genuine therapeutic opportunity.

**To proceed, the following is needed:**

- Formal MOA documentation from DrugBank to confirm or refute the D2/AQP2 interaction hypothesis
- Safety data package: full warnings, contraindications, and drug interaction profile (package insert / Health Canada monograph)
- A preclinical proof-of-concept study demonstrating measurable, beneficial effect of D2 antagonism in an *Avpr2*-gain-of-function animal model before any human hypothesis is entertained
- Cardiac safety assessment specifically addressing QT risk in hyponatremic patients, given the known electrolyte abnormality in NSIAD
- Expert nephrology consultation (rare electrolyte disorders) to evaluate whether any biological rationale exists that the current evidence pack does not capture
- Re-evaluation of the TxGNN knowledge graph path to determine whether the high score is driven by a spurious multi-hop connection

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All findings should be interpreted in the context of regulatory requirements and clinical oversight.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

