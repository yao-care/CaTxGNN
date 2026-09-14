---
layout: default
title: Tenapanor
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
---

# Tenapanor
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

Using superpowers? Not applicable here — this is a straightforward document-generation task following the given template with the supplied Evidence Pack data. Proceeding directly.

---

# Tenapanor: From Undocumented Indication to Candidiasis

## One-Sentence Summary

> Tenapanor's original indication and mechanism of action are not documented in this evidence pack, and the drug is not currently marketed in Canada.
> The TxGNN model predicts it may be effective for **Candidiasis**, but this is currently supported by **0 clinical trials** and **0 publications**,
> and the model's own rationale explicitly states there is no known biological mechanism linking Tenapanor to this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (not documented in evidence pack; drug not currently marketed in Canada) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 97.17% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Tenapanor is not available in this evidence pack, and no original indication information was provided. The only mechanistic description available comes from the repurposing rationale attached to the top-ranked prediction itself, which characterizes Tenapanor as a locally-acting, minimally absorbed NHE3 (Na⁺/H⁺ exchanger 3) inhibitor in the gastrointestinal tract.

That same rationale, however, explicitly states there is **no known antifungal activity or immunomodulatory mechanism** that would explain efficacy against candidiasis — the association is described as "purely a TxGNN graph-embedding link, without biological plausibility." This pattern repeats across the full candidate list: 9 of the 10 predicted indications carry rationale text that directly disclaims any credible mechanistic connection to Tenapanor's known GI-tract pharmacology, including several serious drug-reaction phenotypes (Stevens-Johnson syndrome, SJS/TEN overlap) that are typically *caused by* drugs rather than *treated by* them.

The one partial exception is rank 10, Crohn's colitis, where the rationale notes a "system-level" plausibility argument (NHE3 inhibition could theoretically alter luminal sodium absorption and intestinal permeability) — still unproven, but at least conceptually tied to the drug's known site of action. Because no original indication is documented, and because the model's own outputs flag most candidates as low-plausibility or potential database noise, this evidence pack does not currently support a credible repurposing narrative for any of the 10 candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

No Canadian market authorization records found. Tenapanor is not currently marketed in Canada (0 DINs on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are Evidence Level L5 (model prediction only, no clinical trials or literature), and 9 of them carry rationale text from the model's own output explicitly disclaiming biological plausibility — some (SJS, SJS/TEN overlap) describe phenotypes that are drug-induced reactions rather than indications a drug would treat. Combined with two outstanding data gaps — TFDA/Health Canada label warnings (DG001, Blocking) and confirmed mechanism of action (DG002, High) — there is currently no basis to advance any candidate past screening.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings, precautions, and contraindications (DG001 — blocking; required before any S1 safety screen)
- Confirmed mechanism of action from DrugBank (DG002)
- Documentation of Tenapanor's actual original/approved indication(s), currently missing from this evidence pack
- If any candidate is pursued further, prioritize rank 10 (Crohn's colitis) given its comparatively higher mechanistic plausibility, and actively search for clinical trial/literature evidence before re-scoring
- Recommend deprioritizing or removing candidates whose own rationale text states "no biological plausibility" (candidiasis, adrenocortical insufficiency, familial adrenal hypoplasia, primary cutaneous T-cell lymphoma, SJS, PAGOD syndrome, aphthous stomatitis, 46,XY DSD, SJS/TEN overlap) from the active evaluation queue
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

