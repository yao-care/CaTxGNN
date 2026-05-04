---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Digoxin: From Heart Failure to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a well-established cardiac glycoside with decades of clinical use in managing heart failure and atrial fibrillation.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, with **0 clinical trials** and **2 publications** currently supporting this direction.
Critically, the available mechanistic evidence suggests this prediction may be **physiologically contraindicated** rather than beneficial — warranting a firm Hold recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack (Digoxin is classically used for heart failure and atrial fibrillation) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump in cardiomyocytes, causing an accumulation of intracellular sodium. This in turn drives calcium influx via the Na⁺/Ca²⁺ exchanger, producing a positive inotropic effect that improves myocardial contractility in heart failure. Its vagotonic (parasympathomimetic) properties also slow the ventricular rate in atrial fibrillation.

Prinzmetal angina (variant angina) is caused by transient coronary artery *spasm* rather than fixed obstructive disease. First-line treatments — calcium channel blockers and nitrates — work by relaxing vascular smooth muscle to relieve and prevent vasospasm. Digoxin's mechanism of increasing intracellular calcium concentration may theoretically do the *opposite*, potentially intensifying smooth muscle contraction and worsening coronary vasospasm. The Evidence Pack's own mechanistic rationale explicitly states there is "no positive mechanistic support" for this repurposing, and that Digoxin may **aggravate** coronary artery spasm through both direct calcium effects and indirect sympathetic activation.

The two retrieved publications address circadian pharmacology of antihypertensives and angina decubitus physiology — neither directly supports Digoxin as a therapy for Prinzmetal angina. This high TxGNN score most likely reflects a shared knowledge-graph node (e.g., cardiovascular disease ontology) rather than a genuine therapeutic signal. This prediction is likely a graph artifact and should not be pursued clinically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | Overview of circadian rhythms and antihypertensive treatment timing — not specific to Digoxin or Prinzmetal angina |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review / Mechanism | Chinese Medical Sciences Journal | Hemodynamic study of 30 patients with angina decubitus; identifies increased myocardial oxygen consumption before onset — not directly related to Digoxin or coronary vasospasm |

---

## Canada Market Information

Digoxin has no registered products (DINs) in the Canadian market according to this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.81%), the mechanistic rationale not only fails to support this repurposing — it raises an active safety concern. Digoxin's calcium-raising mechanism is directly contrary to the vasodilatory treatment principle required for Prinzmetal angina, and no clinical trials or disease-specific literature exist to counterbalance this risk.

**To proceed, the following is needed:**
- Inspect the TxGNN knowledge-graph path connecting Digoxin to Prinzmetal angina to identify the likely spurious shared node driving this prediction
- Obtain the complete safety profile for Digoxin, including package insert warnings, contraindications, and drug–drug interactions (all currently marked as Data Gap)
- Retrieve Digoxin's mechanism of action from DrugBank (DB00390) to formally document the calcium-increasing pathway and its vascular implications
- Commission an independent pharmacological review specifically addressing Digoxin's effects on coronary vasomotor tone before any further evaluation
- If the graph-level investigation reveals an unexpected mechanistic pathway (e.g., HIF-1α inhibition, which has been explored for other cardiac glycosides), re-evaluate with a focused preclinical literature search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

