---
layout: default
title: Fesoterodine Fumarate
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 0
---

# Fesoterodine Fumarate
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

# Fesoterodine Fumarate: From Overactive Bladder — Repurposing Prediction Unavailable

## One-Sentence Summary

Fesoterodine fumarate is a muscarinic receptor antagonist used internationally for overactive bladder (OAB), addressing symptoms of urinary urgency, frequency, and urge urinary incontinence.
The TxGNN model did not generate any repurposing predictions for this drug in the current run — most likely due to incomplete pipeline inputs (empty `inputs_received`, missing DrugBank ID, and no mapped original indications).
No clinical trial or literature evidence for novel indications is available from this Evidence Pack; the analysis cannot advance until the data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Overactive bladder (urinary urgency, frequency, urge urinary incontinence) |
| Predicted New Indication | None — TxGNN prediction not generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions available) |
| Canada Market Status | Not Marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Drug Background and Mechanism

Detailed mechanism of action data is not available from this Evidence Pack. Based on established pharmacology, fesoterodine fumarate is a prodrug that is rapidly and non-specifically hydrolysed by plasma esterases to its active metabolite **5-hydroxymethyl tolterodine (5-HMT)**. The active metabolite competitively antagonises **muscarinic M2 and M3 receptors** in the detrusor smooth muscle, suppressing involuntary bladder contractions and reducing OAB symptoms.

Antimuscarinics as a class have previously been explored beyond OAB in conditions driven by cholinergic overactivity — including hyperhidrosis, sialorrhea, irritable bowel syndrome (diarrhoea-predominant), and certain neurological disorders such as Parkinson's disease with bladder dysfunction. However, these represent class-level observations and do not substitute for drug-specific TxGNN predictions.

Because no predictions were generated in this run, no mechanistic link to a new indication can be drawn or evaluated at this stage.

---

## Canada Market Information

No DINs are recorded for fesoterodine fumarate in this Evidence Pack.

> **Verification Required:** This is likely a data collection gap rather than a true absence of approval. Fesoterodine fumarate (brand name **Toviaz®**, Pfizer) is known to be approved by Health Canada. Manual verification via the [Health Canada Drug Product Database (DPD)](https://health-canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) is strongly recommended before reporting market status as negative.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for fesoterodine fumarate in this run. The pipeline received empty inputs (`inputs_received: []`), the DrugBank ID was not resolved, and no original indications were mapped — making knowledge graph traversal impossible. There is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Query the DrugBank API for fesoterodine fumarate (likely `DB06702`) to enable KG linkage and populate MOA, categories, and toxicity data
- **Map original indication**: Confirm "Overactive Bladder (OAB)" as the canonical indication entry for the TxGNN pipeline input
- **Re-run TxGNN pipeline**: With complete inputs, rerun KG and DL prediction to generate repurposing candidates
- **Retrieve package insert**: Download and parse the Health Canada–approved Toviaz® monograph to extract key warnings, contraindications, and DDI profile
- **Verify DIN records**: Cross-check Canada market status via Health Canada DPD and correct the current "Not Marketed / 0 DINs" record if inaccurate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

