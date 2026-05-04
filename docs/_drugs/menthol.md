---
layout: default
title: Menthol
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 0
---

# Menthol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Menthol: Repurposing Evaluation Inconclusive — Insufficient Evidence Pack Data

## One-Sentence Summary

Menthol is a naturally occurring cyclic terpene alcohol found in mint plants, widely used in over-the-counter topical and inhalation products.
The current Evidence Pack contains **no TxGNN-predicted new indications**, and the Canadian regulatory lookup returned **zero DINs**.
Without a valid prediction target or baseline safety profile, this candidate cannot be evaluated at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Below L5 — no predictions generated |
| Canada Market Status | Not marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Two probable causes explain the empty `predicted_indications` list:

**1. DrugBank ID not resolved.**
The Evidence Pack records `drugbank_id: null`. The TxGNN knowledge graph indexes compounds by DrugBank ID; without a confirmed mapping, the pipeline cannot locate the node for Menthol and therefore produces no candidate diseases. Menthol's DrugBank entry is **DB14783** — this ID must be injected before re-running the prediction step.

**2. Zero Health Canada DINs returned.**
The regulatory lookup found no licensed products with Menthol as the sole active ingredient. Menthol in Canada is most commonly a secondary ingredient in combination OTC products (topical analgesics, throat lozenges, inhalants), which may not be captured by single-ingredient DIN queries. A combination-product search against the Health Canada Drug Product Database is needed.

Because neither a prediction score nor an original approved indication is available, the standard evidence evaluation framework cannot be applied.

---

## Canada Market Information

No DINs are currently on record for Menthol as a standalone active ingredient.

> A targeted search of the Health Canada Drug Product Database using ingredient-level filtering (rather than product-level) is recommended. As a reference, Menthol appears as an active or medicinal ingredient in at least 200+ combination products (e.g., muscle rubs, cough syrups, lozenges).

---

## Safety Considerations

No TFDA package-insert warnings, contraindications, or drug interaction data are present in this Evidence Pack. Before any clinical or market assessment can proceed, the following must be retrieved:

- Health Canada Product Monograph (if a standalone DIN exists) or representative combination product monographs
- DrugBank safety profile for DB14783 (known issues include mucosal irritation, contraindication in infants under 2 years for nasal applications)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing the three minimum data points required to generate a repurposing evaluation: a confirmed DrugBank ID, at least one TxGNN predicted indication, and a baseline safety profile. No assessment of mechanistic plausibility, clinical evidence, or benefit-risk can be made without these inputs.

**To proceed, the following is needed:**

1. **Resolve DrugBank mapping** — Confirm DrugBank ID as `DB14783` and re-run the KG prediction pipeline to populate `predicted_indications`
2. **Fix DIN lookup** — Re-query Health Canada DPD using ingredient-level search to recover combination-product DINs and associated approved indications
3. **Retrieve MOA data** — Pull mechanism of action from DrugBank API (`/v1/drugs/DB14783`) to enable mechanistic plausibility analysis
4. **Retrieve safety data** — Download and parse at least one representative Health Canada product monograph to populate `key_warnings` and `contraindications`
5. **Re-run evidence collection** — Once a target indication is available from TxGNN, trigger ClinicalTrials.gov and PubMed collectors to populate the evidence tables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

