---
layout: default
title: Lumacaftor
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Lumacaftor
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

# Lumacaftor: From Cystic Fibrosis to Leprosy

## One-Sentence Summary

Lumacaftor is a CFTR (cystic fibrosis transmembrane conductance regulator) corrector, historically used as part of combination therapy for cystic fibrosis. The TxGNN model's top-ranked prediction is **Leprosy**, with a very high similarity score (**99.44%**), but **0 clinical trials** and **0 publications** currently support this specific pairing — and the evidence pack itself flags the prediction as lacking biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via Canadian license data (no marketed licenses on file); evidence context identifies Lumacaftor as a CFTR corrector, the class historically indicated for Cystic Fibrosis |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no supporting clinical or literature data) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Lumacaftor is not available in the evidence pack (flagged as data gap **DG002**, High severity). Based on the context available, Lumacaftor is a CFTR corrector, typically combined with a CFTR potentiator (e.g., ivacaftor) for cystic fibrosis; its role is to correct misfolded CFTR protein trafficking and restore chloride-channel function at the epithelial cell membrane.

The top TxGNN-predicted indication, **leprosy**, has no established mechanistic connection to CFTR biology. The evidence pack's own rationale is explicit on this point: *"無已知機轉關聯。Lumacaftor 為 CFTR 矯正劑，與痲瘋桿菌感染的免疫/抗菌機轉無交集，僅為 TxGNN 圖譜嵌入相似度預測，缺乏生物學合理性"* — i.e., there is no known mechanistic link, and this is purely a knowledge-graph embedding similarity result lacking biological plausibility. Leprosy's pathophysiology (Mycobacterium leprae infection, host immune response, and peripheral nerve damage) sits in a therapeutic domain entirely distinct from CFTR-mediated chloride transport.

For transparency: this candidate pack evaluated 10 TxGNN-predicted indications for Lumacaftor overall, and every single one carries an **L5 / Hold** verdict. Where corroborating data existed (e.g., 20 PubMed hits for "migraine with or without aura, susceptibility to," or 1 clinical trial for rheumatoid arthritis, or 1 publication for pulmonary hypertension), the evidence pack's own review judged them irrelevant — the literature concerned epilepsy genetics unrelated to Lumacaftor, and the trial/literature involved cystic fibrosis patients as a study population rather than evidence of therapeutic efficacy in the new indication. In short, no candidate in this scan currently rises above a pure model-prediction signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Lumacaftor currently holds **no Health Canada market authorization** — 0 DINs on file, market status "Not Marketed." No product licenses are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack. Notably, TFDA/Health Canada label warnings and contraindications are flagged as data gap **DG001**, Blocking severity — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.44%), but it is unsupported by any clinical trial or literature evidence, and the evidence pack's own mechanistic review explicitly concludes there is no biological plausibility linking a CFTR corrector to leprosy pathophysiology. Combined with the drug's non-marketed status in Canada and missing safety/MOA data, this candidate does not meet the bar to advance past model-prediction stage (S0).

**To proceed, the following is needed:**
- Health Canada / TFDA label data — key warnings and contraindications (Blocking data gap DG001)
- Verified mechanism-of-action documentation for Lumacaftor (High-priority data gap DG002)
- Any preclinical or mechanistic study directly linking CFTR modulation to Mycobacterium leprae infection or leprosy-related neuropathy, should this hypothesis be pursued further
- Given that all 10 predicted indications in this scan scored L5/Hold, consider deprioritizing this drug-candidate pack pending stronger corroborating evidence, or revisit lower-ranked candidates only if new clinical/literature data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

