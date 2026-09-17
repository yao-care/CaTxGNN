---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: From NSAID Anti-Inflammatory Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone (DrugBank DB00461) is a non-selective COX-1/COX-2 inhibitor prodrug of the NSAID class, per the mechanistic notes accompanying this Evidence Pack; its specific original approved indication is not recorded in the pack, and the drug is not currently marketed in Canada.
The TxGNN model's top-ranked prediction is **acromesomelic dysplasia, Hunter-Thompson type**, a rare GDF5-related skeletal developmental disorder, but this pairing has **zero supporting clinical trials or literature**, and the pack's own rationale states there is no plausible mechanistic link to NSAID pharmacology.
This is a pure model-score prediction (L5, decision stage S0) — it should not be confused with several lower-ranked candidates in the same pack (spondyloarthropathy susceptibility, rheumatoid nodulosis) that have real, if indirect, pharmacological rationale as NSAID-class indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and Canada has no licenses on file; rationale text in the pack identifies the drug only as an NSAID (COX-1/COX-2 inhibitor prodrug) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% (0.99993, model rank 251) |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available (`original_moa: [Data Gap]`). Based on the mechanistic annotations included elsewhere in this Evidence Pack, nabumetone is a non-selective COX-1/COX-2 inhibitor NSAID prodrug — a drug class whose pharmacology centers on suppressing prostaglandin-mediated inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, by contrast, is a rare autosomal-recessive skeletal disorder caused by GDF5 gene mutations affecting limb bone growth. It is a **structural/developmental** condition, not an inflammatory one. The Evidence Pack's own repurposing rationale is explicit on this point: *"GDF5 基因相關之骨骼發育異常，屬結構性/發育性疾病，與 NSAID 之消炎鎮痛機轉無合理關聯，僅為模型預測"* — i.e., there is no reasonable mechanistic bridge between NSAID pharmacology and this disease's underlying biology. The high TxGNN score here reflects a knowledge-graph pattern match rather than a plausible pharmacological hypothesis.

Worth flagging: several **lower-ranked** candidates in the same pack are mechanistically more coherent for an NSAID — notably rank 8 (spondyloarthropathy, susceptibility to) and rank 10 (rheumatoid nodulosis), both scored L4/S1 with an explicit drug-class rationale (NSAIDs are standard symptomatic therapy for spondyloarthropathies and RA-spectrum disease). These may warrant more attention than the top-ranked score alone suggests.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Nabumetone has no active Canadian market authorizations on file (0 DINs, market status: Not Marketed), so no license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this Evidence Pack — DDI query returned `not_found`.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked pairing (nabumetone → acromesomelic dysplasia, Hunter-Thompson type) has no clinical, literature, or mechanistic support — it is a pure L5 model-score prediction with an explicitly acknowledged mechanistic mismatch. There is no basis to advance this specific pairing beyond exploratory screening.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety evaluation can begin)
- Confirmed mechanism of action (High-severity data gap; currently unavailable via DrugBank)
- If pursuing NSAID-class indications instead, prioritize evaluation of the higher-rationale candidates in this pack (spondyloarthropathy susceptibility, rheumatoid nodulosis), which are already at decision stage S1 with drug-class-level pharmacological support, rather than the top TxGNN-score pairing reported here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

