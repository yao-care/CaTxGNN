---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 2
---

# Heparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the Evidence Pack provided, here is the evaluation report.

---

# Heparin: From Thromboembolic Disease to Thrombophilia Due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

> Heparin is a well-known anticoagulant historically used for the prevention and treatment of thromboembolic disorders.
> The TxGNN model predicts it may be effective for **Thrombophilia Due to Protein C Deficiency, Autosomal Recessive**,
> but currently **no clinical trials** and **no publications** in this Evidence Pack directly support this specific link — the rationale rests on known anticoagulant pharmacology and clinical bridging practice rather than direct study data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (Heparin is generically known as an anticoagulant for thromboembolic disease; no Health Canada license record was returned) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on generally known pharmacology, heparin activates antithrombin III, which in turn inhibits thrombin (Factor IIa) and Factor Xa. Critically, this antithrombotic mechanism does **not** depend on the Protein C / Protein S pathway.

In patients with hereditary Protein C deficiency, the coagulation system loses one of its natural anticoagulant checks, creating a prothrombotic state (thrombophilia). Because heparin's mechanism bypasses the Protein C/Protein S axis entirely, it is pharmacologically well-suited to compensate for this specific deficiency. In fact, heparin is already widely used in clinical hematology practice as a **bridging anticoagulant** in Protein C-deficient patients — particularly during the period when starting warfarin carries a risk of warfarin-induced skin necrosis (a paradoxical hypercoagulable complication seen in Protein C deficiency). This is an accepted clinical convention rather than a novel hypothesis.

No clinical trials or literature records in this Evidence Pack directly matched this drug–disease pair (0 trials, 0 publications; see `query_log` entries 2–4). This is most plausibly explained by an overly narrow search term — "autosomal recessive" thrombophilia due to protein C deficiency is a rare subtype, and broader queries (e.g., "heparin AND protein C deficiency" or "heparin AND thrombophilia bridging") were not run in this cycle. Absence of hits should therefore be read as a search-coverage gap, not as evidence against the mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Health Canada authorization (DIN) records were found for Heparin in this dataset (`total_licenses: 0`, `market_status: 未上市`). This indicates either a data-collection gap or that the product is not currently marketed under the queried identifiers — this should be confirmed directly against the Health Canada Drug Product Database before proceeding further.

---

## Safety Considerations

Please refer to the package insert for safety information. No specific warnings, contraindications, or drug interaction data were returned for this candidate (key warnings, contraindications, and DDI query all came back empty/unresolved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for heparin in Protein C-deficiency-related thrombophilia is biologically sound and reflects existing clinical bridging practice, but this specific indication is currently supported only at the mechanism level (L4) with zero direct trials or publications in this Evidence Pack. In addition, a **Blocking** data gap (DG001: missing Health Canada/product-monograph warnings and contraindications) prevents this candidate from completing even the S1 safety pre-screen, and no Canadian market/license data was found to confirm current availability.

**To proceed, the following is needed:**
- Health Canada product monograph data — key warnings and contraindications (resolves DG001, currently blocking)
- Confirmed mechanism-of-action record via formal DrugBank query (resolves DG002)
- Broader literature/trial search using expanded terms (e.g., "heparin AND protein C deficiency", "heparin bridging anticoagulation") to check whether the zero-hit result is a true evidence gap or a search-term limitation
- Hematology/clinical expert review of existing bridging-therapy literature and guidelines, since this practice is likely documented outside the structured trial/PubMed search terms used here
- Verification of current Health Canada market/license status for Heparin

---

### Note on Secondary Candidate Screened (Rank 2, Not Recommended)

A second TxGNN candidate — **"primary release disorder of platelets"** (score 99.06%) — was also screened but should **not** be pursued. Despite a high TxGNN score and 30 associated clinical trials plus 20 publications, review of the actual evidence shows it is dominated by studies on **heparin-induced thrombocytopenia (HIT)** — an adverse immune reaction to heparin — general anticoagulation trials, and unrelated cardiovascular/imaging studies. None of the reviewed evidence supports using heparin to *treat* a primary platelet release/storage defect; if anything, heparin's known interaction with platelets in this context is pathogenic (HIT), not therapeutic. This candidate is assessed as **Hold** (Evidence Level L5, likely a knowledge-graph node-proximity false positive between HIT and platelet-disorder nodes) and is not recommended for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

