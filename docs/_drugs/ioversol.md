---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Ioversol
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

Using the report as a direct content-generation task (this prompt itself is the full spec for a drug repurposing evaluation report — no additional skill needed for a single evidence-pack write-up).

I need to flag something before writing: the evidence pack for Ioversol is unusually thin and self-contradicting in a specific way. The top-ranked prediction (osteoarthritis susceptibility) has zero supporting evidence, and the evidence attached to the #2 prediction (osteoarthritis) explicitly belongs to a different drug (Lipiodol, an embolization agent), not Ioversol. I'm reporting this transparently rather than dressing it up as a viable candidate — that's what the underlying data supports.

---

# Ioversol: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is a non-ionic iodinated radiographic contrast agent used for diagnostic imaging, not a therapeutic drug with an established indication. The TxGNN model's top-ranked prediction is **Osteoarthritis Susceptibility** (score 99.67%), but this prediction — and the nine others returned — currently have **no supporting clinical trials or literature specific to Ioversol**; the only substantive evidence retrieved in this evidence pack turns out to belong to a different drug entirely.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Ioversol is a diagnostic contrast agent; no therapeutic indication or MOA data is on file (DG002) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only, no corroborating studies) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on known information, Ioversol is a non-ionic iodinated contrast medium administered intravascularly for diagnostic imaging — it has no established pharmacodynamic activity directed at joint tissue, cartilage, or inflammatory pathways, and no known pharmacological rationale connects it to osteoarthritis or osteoarthritis susceptibility.

Critically, when this evidence pack's own analysts traced the clinical trial and literature hits returned for the related "osteoarthritis" prediction (rank 2), all of them turned out to concern **Lipiodol** (ethiodized oil), a distinct iodinated agent used for arterial embolization — not Ioversol. This is flagged in the source data as a likely drug-confusion false positive rather than genuine repurposing signal. Several other top-10 predictions (brachyolmia, acromesomelic dysplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, myosclerosis) are rare skeletal/developmental disorders with no literature at all, and are flagged as likely artifacts of TxGNN's embedding clustering rather than real pharmacological signal.

Taken together, none of the top 10 predictions for Ioversol currently have a credible mechanistic or empirical basis. The one prediction with genuinely relevant literature (hemoglobinopathy, rank 5, L4) concerns the *safety* of using iodinated contrast in sickle cell disease patients undergoing imaging — a diagnostic-safety consideration, not evidence of therapeutic efficacy for hemoglobinopathy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Note: Clinical trials were returned for the related "osteoarthritis" prediction (rank 2 — NCT06497140, NCT04733092, NCT06611007, NCT06859164), but all four use Lipiodol-based embolization, not Ioversol, and are excluded here as drug-mismatched.*

## Literature Evidence

Currently no related literature available for the top-ranked prediction (osteoarthritis susceptibility).

*Note: The most relevant Ioversol-specific publication found across all 10 predictions is [22195536](https://pubmed.ncbi.nlm.nih.gov/22195536/) (2012, Review, *The American Journal of Medicine*) — a review of the safety of iodinated IV contrast administration in sickle cell disease. It addresses imaging safety, not a therapeutic indication, and was attached to the "hemoglobinopathy" prediction (rank 5), not osteoarthritis susceptibility.*

## Canada Market Information

Ioversol is not currently marketed in Canada under this evidence pack's data (0 licenses / DINs on file).

## Safety Considerations

Please refer to the package insert for safety information.

*The evidence pack notes a blocking data gap (DG001): official label warnings/contraindications have not yet been retrieved, which prevents even a preliminary (S1) safety screen for any of these predictions.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the top 10 TxGNN-predicted indications for Ioversol have credible supporting evidence specific to this drug — the top prediction has none at all, and the most substantial-looking evidence (osteoarthritis trials/literature) belongs to a different agent (Lipiodol), not Ioversol. Combined with a blocking gap in safety labeling data, there is no basis to advance any candidate past S0/S1.

**To proceed, the following is needed:**
- Official product label / warnings and contraindications (DG001, blocking)
- DrugBank mechanism-of-action data for Ioversol (DG002)
- Re-run evidence retrieval with stricter drug-name disambiguation to eliminate Lipiodol/Ioversol cross-contamination in trial and literature matching
- If no Ioversol-specific evidence emerges after reprocessing, deprioritize this candidate in favor of higher-scoring, evidence-backed drugs in the pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

