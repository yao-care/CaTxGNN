---
layout: default
title: Luspatercept
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Luspatercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Luspatercept: From Indication Data Unavailable to Monosomy X (Low-Confidence Prediction)

## One-Sentence Summary

> Luspatercept's original approved indication cannot be determined from this evidence pack — Health Canada licensing data and DrugBank indication fields are both empty. TxGNN's top-ranked prediction is **Monosomy X** (score 96.00%), but the model's own mechanistic rationale explicitly flags this link as weak with **no supporting clinical trials or literature**. This is a data-gap-heavy pack (2 flagged gaps, one Blocking) that does not yet support a positive repurposing case.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Health Canada license record; DrugBank indication field empty) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 96.00% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Luspatercept is not available in this pack (flagged as a High-severity data gap, DG002). Based on general knowledge of the drug class, Luspatercept is an activin receptor ligand trap that modulates TGF-β/SMAD2/3 signaling to promote late-stage erythroid maturation — but this pack does not confirm or link that mechanism to the top-ranked candidate below, so it should be treated as background context only, not as validated support.

For the rank-1 prediction, **Monosomy X**, the evidence pack's own repurposing rationale states the link is weak: *"monosomy X（Turner 症候群相關染色體異常）與紅血球成熟調控機轉無直接關係，屬於染色體/發育性疾病，機轉連結薄弱，無支持證據"* — i.e., a chromosomal/developmental disorder with no direct connection to erythroid maturation pathways. No clinical trials or literature were found for this drug-disease pair (query IDs 2–4 all returned zero results). The high TxGNN score likely reflects a knowledge-graph proximity artifact rather than a causal mechanistic signal.

Notably, further down the ranked list, **thalassemia, beta+, silent allele** (rank 7, score 93.32%) carries a much stronger mechanistic rationale per the pack itself — Luspatercept's known activin receptor IIB ligand-trap mechanism aligns with treatment of ineffective erythropoiesis in beta-thalassemia — though it likewise has zero supporting trials or literature in this pack. This suggests the pack's mechanistic annotations, not the raw TxGNN score, may be the more informative signal for prioritization in a future review cycle.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Luspatercept is currently **not marketed** in Canada — the evidence pack records 0 total licenses and no DIN entries.

## Safety Considerations

Please refer to the package insert for safety information. (Note: the underlying data gap here — DG001, missing Health Canada product monograph warnings/contraindications — is flagged **Blocking**, meaning this candidate cannot proceed to a formal S1 safety assessment until that data is obtained.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (prediction only) with zero clinical trials or literature for the top-ranked indication, and the pack's own rationale text characterizes the Monosomy X mechanistic link as weak/unsupported. Combined with a Blocking data gap on regulatory safety information, there is no basis to proceed at this time.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications) — resolves Blocking gap DG001
- DrugBank/primary-source MOA and original indication confirmation — resolves High-severity gap DG002
- Targeted literature/clinical trial search for higher-mechanistic-plausibility candidates in this list (e.g., thalassemia beta+ silent allele, Hb Bart's hydrops fetalis) rather than relying on TxGNN score rank alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

