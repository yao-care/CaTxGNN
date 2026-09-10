---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol: From Radiocontrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated radiocontrast agent used for X-ray and CT imaging, with no established pharmacological indication for CNS or sleep disorders. The TxGNN model predicts a **99.87% score** for **Insomnia**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags this as likely knowledge-graph topological noise rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Radiocontrast agent for X-ray/CT imaging (diagnostic use, not a treatment indication) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this evaluation (blocking data gap — MOA not yet retrieved from DrugBank). Based on known information, Iohexol is a non-ionic iodinated contrast medium whose only established clinical role is as an imaging agent (intravascular, intrathecal, or intra-articular administration for radiographic visualization). It has no known receptor, enzyme, or neurotransmitter-pathway activity that would plausibly affect sleep onset or maintenance.

The evidence pack's own rationale for this candidate is explicit: there is "no known pharmacological mechanism to explain a sedative/hypnotic effect," and the high TxGNN score is attributed to knowledge-graph topological similarity rather than any biological or clinical signal. This assessment is corroborated by the pattern across the other nine top-ranked predictions for this drug (anxiety, rheumatoid arthritis, antithrombin deficiency, fibromyalgia, tendinitis, etc.) — in every case where trial or literature evidence exists, Iohexol appears only as a diagnostic tool (e.g., GFR measurement via iohexol clearance, or contrast arthrography/myelography), never as a therapeutic intervention. This consistent pattern across the full candidate set reinforces that the model's high scores for this drug should be treated with caution rather than as an actionable repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Iohexol currently has no Drug Identification Numbers (DINs) on file and is not marketed in Canada under this evidence pack (market status: Not Marketed, 0 total licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The Insomnia prediction has no supporting clinical trials or literature (L5, model-only), and the drug's known mechanism (radiocontrast imaging) offers no plausible pathway to a hypnotic/sedative effect; the same noise pattern recurs across all other top-10 predicted indications for this drug.

**To proceed, the following is needed:**
- MOA data from DrugBank (currently a High-severity gap affecting mechanistic-link analysis)
- TFDA/Health Canada label warnings and contraindications (currently a Blocking gap preventing any S1 safety pre-assessment)
- Preclinical or mechanistic studies specifically testing Iohexol in sleep-related endpoints, if this candidate is to be pursued further
- Given the absence of any supporting evidence and implausible mechanism, deprioritizing this candidate in favor of higher-evidence-level predictions is recommended unless new data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

