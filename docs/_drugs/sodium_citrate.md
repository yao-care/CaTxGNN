---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 9
---

# Sodium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Sodium Citrate: From No Documented Original Indication to Papillary Conjunctivitis

## One-Sentence Summary

> Sodium citrate (DB09154) has no documented original indication or Canadian market authorization in the available data set.
> The TxGNN model's top-ranked prediction is **Papillary Conjunctivitis**, with a score of 99.95%,
> but this candidate is supported by **0 clinical trials** and **0 publications**, and is flagged in the source data as likely graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Canadian market licenses and no original indication data provided |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium citrate in this evidence pack. Based on general pharmacological knowledge, sodium citrate functions systemically as an alkalinizing agent and calcium-chelating anticoagulant; no mechanistic pathway connecting these properties to papillary conjunctivitis (an allergic/contact-mediated ocular surface inflammatory condition) has been identified.

The supplied rationale for this candidate explicitly states there is no known mechanistic link, and with zero clinical trials and zero publications retrieved, the prediction is assessed as likely **TxGNN knowledge-graph noise** rather than a biologically grounded repurposing signal.

For context, of the 9 predicted indications returned for this drug, 7 (including this top-ranked one) have zero supporting evidence (L5) and are similarly flagged as noise. The only candidate reaching beyond model-prediction-only status is rank 4, "stomach disease" (L4/S1), where in-vitro evidence shows sodium citrate combined with 3-bromopyruvate can induce apoptosis in a gastric cancer cell line — but other literature in that same evidence set also reports sodium-containing solutions causing acute gastric/esophageal mucosal injury, meaning the directionality of effect (therapeutic vs. harmful) is unresolved. This candidate does not offset the weakness of the rank-1 prediction being reported here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sodium citrate has no Health Canada market authorizations on record in this data set (total licenses: 0). No DIN, product name, or approved indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all marked as data gaps in the source evidence pack. TFDA/Health Canada label warnings are flagged as a **Blocking** data gap — item DG001 — that must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (papillary conjunctivitis) has zero clinical trial or literature support and is explicitly assessed as likely model noise. Combined with the absence of MOA data, absence of Canadian market authorization, and absence of any safety/label data, there is no basis to advance this candidate. Even the best-evidenced alternative among the 9 predictions (stomach disease, L4) shows conflicting safety/efficacy signals and relies on combination-therapy in-vitro data, not monotherapy indication evidence.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: TFDA/Health Canada label warnings and contraindications
- Resolve High-severity data gap DG002: mechanism of action (DrugBank API query)
- Confirm Canadian regulatory/market status for sodium citrate (currently 0 licenses on record)
- If pursuing further, redirect evaluation toward mechanistically plausible candidates (e.g., rank 4 "stomach disease") with dedicated safety review to reconcile conflicting in-vitro signals, rather than the noise-flagged rank-1 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

