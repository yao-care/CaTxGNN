---
layout: default
title: Norethindrone Enanthate
parent: 僅模型預測 (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Norethindrone Enanthate
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

Using the report template above to synthesize this drug's evidence pack. Note upfront: this case is unusual — every one of the 10 TxGNN-predicted indications in this pack carries a "Hold" recommendation, and the rationale text attached to several of them explicitly flags a likely **inverted signal** (the model may be picking up an adverse-effect association, not a treatment relationship). I've written the report to reflect that honestly rather than force a positive spin.

---

# Norethindrone Enanthate: From Contraception to Antithrombin Deficiency Type 2

## One-Sentence Summary

> Norethindrone enanthate is a long-acting injectable progestin used for hormonal contraception (this is established only through the literature captured in this evidence pack — formal regulatory indication text is not available). The TxGNN model's top prediction links it to **Antithrombin Deficiency Type 2** with a **98.93%** prediction score, but **zero clinical trials and zero literature entries** currently support this specific pairing, and evidence elsewhere in this same pack shows the drug is associated with **inducing** thrombosis rather than treating it — the opposite pharmacological direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception (inferred only from literature context in this pack; no formal regulatory indication text on file) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug (flagged as a High-severity data gap — DG002, pending DrugBank API lookup). Based on the information available in this pack, norethindrone enanthate is a long-acting injectable progestogen used for contraception.

Antithrombin deficiency type 2 is an inherited thrombophilia — a condition of *excessive* clotting tendency. Elsewhere in this same evidence pack, literature tied to this drug's other predicted indications (cardiovascular disease, thrombophilia) shows the opposite pharmacological profile: a documented case report of norethisterone enanthate–induced cerebral venous sinus thrombosis (PMID 29141931), and cohort studies noting reduced HDL cholesterol with long-term use — both consistent with a **prothrombotic**, not antithrombotic, effect.

Mechanistically, a drug that shifts coagulation toward a prothrombotic state would not be expected to correct an inherited antithrombin deficiency. The high TxGNN score more plausibly reflects the knowledge graph detecting proximity between this drug and thrombosis-related disease nodes through an **adverse-effect relationship**, not a genuine treatment relationship. This prediction should be read as a caution flag, not a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Antithrombin Deficiency Type 2 specifically.

---

## Canada Market Information

Not currently marketed in Canada; no DIN records available (0 licenses on file).

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) is not on file for this drug — this is a Blocking data gap (DG001, pending TFDA label review). Please refer to the package insert for safety information once available.

**Literature-derived signal worth flagging separately:** although not part of the structured safety dataset, literature gathered for *other* predicted indications in this same pack directly implicates this drug in thrombotic risk:
- [29141931](https://pubmed.ncbi.nlm.nih.gov/29141931/) — case report of norethisterone enanthate–induced cerebral venous sinus thrombosis (CVST).
- [1424623](https://pubmed.ncbi.nlm.nih.gov/1424623/) / [1533383](https://pubmed.ncbi.nlm.nih.gov/1533383/) — cohort studies noting lipid/lipoprotein shifts (reduced HDL) with long-term use, a cardiovascular risk factor.

This reinforces that the top-ranked predicted indication (a thrombophilia) is mechanistically implausible as a treatment target and should be treated as a safety caution rather than a repurposing opportunity.

---

## Note on the Other 9 Predicted Indications

All 10 predicted indications in this pack carry a "Hold" recommendation. Only two (cardiovascular disease, thrombophilia) reached decision stage S1 with literature evidence — and both are annotated in this pack's own rationale as safety signals (drug-induced thrombotic risk), not efficacy evidence. The remaining 8, including the top-ranked antithrombin deficiency type 2, are pure L5 model output with no clinical or literature support. This is a pattern consistent with the knowledge graph clustering this drug near thrombosis/coagulation-disorder nodes via an adverse-effect pathway rather than a therapeutic one.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical or literature support (L5, decision stage S0), and the drug's documented pharmacological profile — reinforced by evidence tied to other predictions in this same pack — points toward a prothrombotic effect that conflicts mechanistically with treating a thrombophilic condition. No predicted indication in this pack reached a stage or evidence level that would support advancing to further evaluation.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- Independent confirmation of directionality (treatment vs. adverse-effect) before staging any of the 10 candidates further
- Formal original-indication and regulatory license text, currently absent from this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

