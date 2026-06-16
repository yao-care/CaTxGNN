---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein: From Ophthalmic Diagnostic Dye to Prinzmetal Angina

## One-Sentence Summary

Fluorescein is a fluorescent xanthene dye whose established clinical role is entirely diagnostic — administered intravenously for fluorescein angiography (retinal vascular imaging) or applied topically for corneal epithelial staining — with no approved therapeutic indication in Canada or internationally.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (variant angina caused by coronary artery vasospasm),
with **0 clinical trials** and **0 publications** directly supporting this direction, representing an **L5 (model prediction only)** finding and a probable model false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indication; primary clinical use is ophthalmic diagnostic imaging (fluorescein angiography, corneal staining) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Fluorescein is a small-molecule fluorescent dye (xanthene class) whose pharmacological activity is limited to light absorption in the blue spectrum (~490 nm) and emission in the green spectrum (~520 nm). In clinical practice, it acts as a passive vascular tracer after intravenous injection, enabling real-time imaging of retinal and choroidal perfusion. It has no receptor targets, enzyme inhibition profiles, or ion channel interactions documented in the therapeutic literature.

Prinzmetal angina (variant angina) is driven by transient coronary artery vasospasm and is pharmacologically managed with calcium channel blockers (e.g., amlodipine, diltiazem) and long-acting nitrates that relax vascular smooth muscle. Fluorescein has no known vasodilatory, calcium channel antagonist, nitric oxide-mediated, or anti-spasmodic mechanism that would be relevant to coronary vasomotor tone.

The TxGNN prediction score of 0.9981 is very high, but the evidence review identifies this as a **model false positive**. Across all 10 predicted indications in this pack, the retrieved clinical trials and literature consistently show Fluorescein appearing only as a diagnostic measurement tool (e.g., corneal staining scores, fluorescein angiography imaging), not as a therapeutic intervention. There is no biological plausibility, preclinical data, or clinical signal connecting Fluorescein to Prinzmetal angina or to any of the other predicted indications (thrombophilia, rheumatoid arthritis, hemoglobinopathy, hyperthyroidism, beta-thalassemia, or rare genetic disorders).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Known adverse reactions to intravenous fluorescein in its diagnostic use include nausea (most common), urticaria, and rare anaphylaxis. No drug interaction data relevant to therapeutic repurposing is available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fluorescein has no pharmacological mechanism relevant to Prinzmetal angina or any of the 10 TxGNN-predicted indications; the high prediction score (99.81%) is a systematic model false positive caused by Fluorescein's co-occurrence with disease terms throughout the ophthalmic literature as a **diagnostic dye**, not a therapeutic agent. Additionally, Fluorescein is not marketed in Canada and holds no DINs, meaning even pursuing a diagnostic indication would require a full regulatory pathway.

**To proceed, the following would be needed:**
- Identification of any novel pharmacological target linking Fluorescein to coronary vasospasm, thrombophilia, or autoimmune pathways (currently none known)
- Reassessment of TxGNN knowledge graph inputs to flag diagnostic-only agents and suppress false positive predictions driven by diagnostic co-mention bias
- If any mechanistic hypothesis emerges, in vitro pharmacology studies (receptor binding, functional assays) as a prerequisite to any preclinical model work
- Regulatory pre-consultation if any therapeutic claim is pursued, given zero existing Canadian approvals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

