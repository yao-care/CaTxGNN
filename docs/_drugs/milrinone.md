---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Milrinone
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

# Milrinone: From Congestive Heart Failure to Alopecia

## One-Sentence Summary

Milrinone is a selective phosphodiesterase-3 (PDE3) inhibitor, used as a short-term intravenous inotropic agent for acute decompensated heart failure, and is currently not marketed in Canada.
The TxGNN model predicts it may be effective for **Alopecia** (prediction score 99.91%),
however **0 clinical trials** and **0 publications** currently support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Short-term IV management of acute decompensated congestive heart failure |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, milrinone selectively inhibits PDE3 in cardiac myocytes and vascular smooth muscle cells, blocking the hydrolysis of cyclic AMP (cAMP). Elevated intracellular cAMP activates protein kinase A (PKA), producing a combination of positive inotropy (enhanced cardiac contractility), positive lusitropy (accelerated myocardial relaxation), and vasodilation of both systemic and pulmonary vascular beds. This "inodilator" mechanism precisely addresses the hemodynamic derangements of acute heart failure.

The predicted link to alopecia lacks mechanistic grounding. Hair follicle cycling is governed primarily by WNT/β-catenin, Sonic Hedgehog (Shh), and BMP/FGF signaling pathways. While PDE4 isoforms have been associated with adenylyl cyclase activity in limited hair follicle preclinical data, PDE3 inhibition has no established role in follicular stem cell activation, dermal papilla cell biology, or the hair growth cycle in any published model.

Notably, four of the top five TxGNN predictions for milrinone cluster around hair loss conditions (alopecia, hypotrichosis simplex, congenital hypotrichosis milia, diffuse alopecia areata), all with near-identical scores (~99.9%). This pattern strongly suggests a shared knowledge-graph artifact — the cAMP signaling hub is topologically adjacent to follicular ontology terms in the graph — rather than independent mechanistic signals for each condition. The 99.91% score reflects distant network connectivity, not direct biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Milrinone is not currently marketed in Canada. No Drug Identification Numbers (DINs) have been issued for any milrinone-containing product.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.91% for alopecia is almost certainly a knowledge-graph artifact. Four consecutive top predictions all cluster around hair loss conditions with virtually identical scores, pointing to a single shared network effect rather than four independent signals. There are no clinical trials, no published literature, and no preclinical data supporting milrinone's PDE3 inhibition mechanism in any hair growth pathway. Beyond the lack of efficacy evidence, milrinone's well-documented cardiovascular risks — including proarrhythmia, systemic hypotension, and a 28% increase in all-cause mortality observed in the PROMISE trial with long-term oral use — create an unacceptable risk profile for a non–life-threatening dermatological indication.

**To proceed, the following would be needed:**
- Preclinical in vitro or in vivo data demonstrating that PDE3 inhibition (distinct from PDE4) promotes hair follicle cycling or dermal papilla cell proliferation
- Identification of a topical or intradermal delivery route that eliminates systemic cardiovascular exposure
- Mechanistic differentiation from existing PDE4-targeting approaches already explored for hair loss (e.g., apremilast, roflumilast)
- Formal pharmacological justification for why a PDE3-selective agent would outperform or complement PDE4 inhibitors in follicular biology

---

> **Note on secondary predictions in this multi-indication pack:** Of the 10 predictions reviewed, the most evidence-supported *novel* repurposing signal is **Acute Pulmonary Heart Disease** (rank 10, Evidence Level L2, Proceed with Guardrails), where inhaled milrinone has accumulated Phase 2–3 clinical data for selective pulmonary vasodilation and right ventricular support in cardiac surgery and pulmonary hypertension settings. A separate focused report on that indication is recommended as the higher-priority repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

