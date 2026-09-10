---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 3
---

# Ivosidenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ivosidenib: From IDH1-Mutated AML/MDS to Bulbar Polio

## One-Sentence Summary

Ivosidenib is an IDH1 mutant-enzyme inhibitor with US approval in IDH1-mutated acute myeloid leukemia (AML) and myelodysplastic syndrome (MDS), and it is not currently marketed in this jurisdiction. The TxGNN model's top-ranked prediction is **Bulbar Polio**, but this pairing has **zero supporting clinical trials or literature** and no plausible biological mechanism — it is most likely a knowledge-graph embedding artifact. Two lower-ranked, mechanistically far more coherent predictions (treatment-related AML/MDS following alkylating-agent or radiation exposure) exist in the same evidence pack and are better candidates for further research.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | IDH1-mutated AML / MDS (US-approved; per repurposing rationale in this evidence pack — not separately confirmed in `drug.original_indications`) |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the drug-level record (`original_moa` is a data gap). However, the evidence pack's own repurposing rationale describes Ivosidenib as a selective inhibitor of mutant IDH1, which suppresses production of the oncometabolite 2-hydroxyglutarate (2-HG) — a mechanism relevant to IDH1-mutant cancer cells, not to viral neuromuscular disease.

Bulbar polio is an acute viral disease caused by poliovirus infection of brainstem motor neurons. There is no known biological pathway connecting IDH1 enzyme inhibition to poliovirus pathophysiology, viral replication, or motor neuron protection. The evidence pack itself flags this explicitly: the high TxGNN score (0.993) is very likely an artifact of the knowledge-graph embedding space rather than a genuine biological signal, and no clinical trials, literature, or mechanistic hypothesis support it.

By contrast, two other predictions in this same evidence pack — treatment-related AML/MDS following alkylating-agent exposure and following radiation exposure — are mechanistically well-grounded: eligibility for Ivosidenib's existing approved indications is defined by IDH1 mutation status rather than disease etiology, so these represent an etiological subgroup extension of an already-approved indication rather than a novel mechanism. These are staged as "Research Question" (S1) rather than "Hold," reflecting materially higher plausibility despite also lacking subgroup-specific trials or literature in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No authorizations found — Ivosidenib is not marketed in this jurisdiction (0 licenses on record).

---

## Cytotoxicity

Ivosidenib is an antineoplastic agent (approved indication: IDH1-mutated AML/MDS).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule IDH1 mutant-enzyme inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: label warnings/contraindications (DG001) are flagged as a **Blocking** data gap in this evidence pack — a formal safety review (S1) cannot proceed for any candidate until TFDA/label data is obtained.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Bulbar Polio) has no clinical, literature, or mechanistic support and is assessed as a likely model artifact; it does not warrant further investment. Separately, a Blocking data gap on label warnings/contraindications (DG001) means no candidate from this drug can advance to a safety evaluation stage regardless of efficacy signal strength.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (DG001, Blocking) — required before any S1 safety review
- Formal mechanism-of-action documentation (DG002)
- If pursuing the more plausible signals instead: targeted literature/trial search for IDH1-mutant treatment-related AML/MDS (alkylating-agent and radiation-induced subgroups), since this dataset returned zero subgroup-specific records despite mechanistic overlap with an approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

