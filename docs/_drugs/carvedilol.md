---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carvedilol: From Heart Failure & Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a combined α1- and non-selective β-adrenergic receptor blocker widely established in heart failure and hypertension management.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, ranking it as the top candidate with a prediction score of **99.55%**.
However, no clinical trials or directly relevant literature currently support this specific repurposing direction — evidence remains at **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure, hypertension (standard pharmacological use; no Health Canada DIN records in dataset) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (no DIN records in current dataset) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carvedilol exerts its cardiovascular effects through a dual mechanism: **α1-adrenergic receptor blockade** reduces peripheral vascular resistance, while **non-selective β-blockade** suppresses renin secretion from the juxtaglomerular apparatus. Additionally, carvedilol possesses antioxidant properties that may mitigate oxidative stress-driven vascular injury. These combined actions are mechanistically relevant to malignant renovascular hypertension, a hypertensive emergency characterised by markedly elevated blood pressure driven by renal artery stenosis and excess renin–angiotensin–aldosterone system (RAAS) activation.

The α1-blocking component offers additive antihypertensive benefit beyond pure renin suppression, addressing the peripheral vasoconstriction that pure beta-blockers may inadequately control in RAAS-driven crises. Furthermore, carvedilol's established renal-protective profile in heart failure patients with chronic kidney disease — reducing glomerular perfusion pressure and attenuating oxidative glomerular injury — provides a mechanistic rationale for its use in malignant hypertensive renal disease (rank 2, identical TxGNN score).

That said, important caveats exist: acute malignant hypertension typically requires intravenous agents (e.g., IV labetalol, nicardipine) for titratable blood pressure control, and the role of oral carvedilol in the acute phase is clinically unclear. The mechanistic link is rated **moderate** — plausible but contested, particularly regarding beta-blocker efficacy in predominantly RAAS-driven pathology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carvedilol in Malignant Renovascular Hypertension.

---

## Literature Evidence

Currently no directly relevant literature available for Carvedilol in Malignant Renovascular Hypertension.

> **Note on Rank 4 Literature (Pulmonary Hypertension / Hypoxia):** PubMed returned 20 results for the query (Carvedilol + pulmonary hypertension owing to lung disease/hypoxia), but all retrieved articles are general reviews of hypoxia biology (brain aging, cancer metabolism, HIF-1α signalling, etc.) with no direct connection to carvedilol pharmacology in pulmonary hypertension. These papers are classified as **not relevant** to the repurposing hypothesis and are excluded from the evidence table.

---

## Canada Market Information

No Health Canada DIN records are present in the current dataset for Carvedilol. The market status is recorded as **Not marketed** based on available regulatory data.

> **Data Note:** This finding may reflect an incomplete data extract rather than true market absence — carvedilol (Coreg® and generics) has established cardiovascular indications and is typically available in Canada. Manual verification against the Health Canada Drug Product Database is recommended before drawing conclusions.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) are not available in the current Evidence Pack.

Please refer to the product monograph and Health Canada drug label for complete safety information. Key clinically known considerations for carvedilol include:

- **Contraindications**: Decompensated heart failure requiring IV inotropes; severe bradycardia or heart block; cardiogenic shock; severe hepatic impairment; bronchial asthma or severe reactive airway disease (β2-blockade risk).
- **Pulmonary Hypertension Caution**: β2-blockade may cause bronchoconstriction and potentially exacerbate pulmonary vasoconstriction in hypoxic patients — a particular concern for ranks 3 and 4 predictions.
- **Drug Interactions**: Known interactions with CYP2D6 inhibitors (fluoxetine, paroxetine) and CYP2C9 inhibitors; additive hypotension with other antihypertensives and anaesthetic agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for carvedilol are rated **L5** — model prediction only, with zero clinical trials and no directly relevant literature. While the mechanistic link to malignant renovascular hypertension is conceptually plausible (dual α/β blockade addressing both vasoconstriction and renin excess), the absence of any supporting clinical or preclinical data, combined with unresolved safety questions about oral carvedilol in acute hypertensive emergencies, does not justify proceeding at this stage.

**To proceed, the following is needed:**

- **MOA data (DrugBank API)**: Retrieve complete mechanism of action, pharmacodynamic targets, and drug class categorisation to strengthen mechanistic rationale analysis
- **Health Canada DIN verification**: Cross-check against the Health Canada Drug Product Database to confirm actual market status and retrieve approved indications
- **Safety profile (product monograph)**: Download and parse the full Health Canada monograph for warnings, contraindications, and special populations
- **Focused literature search**: Commission a targeted PubMed/EMBASE search specifically for "carvedilol AND (renovascular hypertension OR malignant hypertension)" to confirm absence of evidence
- **Preclinical evidence scan**: Search for animal models or in vitro studies on carvedilol in malignant hypertension or RAAS-driven hypertensive nephropathy — this would determine whether the hypothesis merits an L4 upgrade
- **Clinical context assessment**: Consult nephrology/cardiology literature on the role of oral beta-blockers (vs. IV agents) in acute malignant hypertension management to assess route compatibility and clinical feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

