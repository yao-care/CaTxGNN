---
layout: default
title: Efinaconazole
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Efinaconazole
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

# Efinaconazole: From Onychomycosis to Astigmatism

## One-Sentence Summary

Efinaconazole is a topical triazole antifungal (brand name Jublia®), approved for the treatment of distal and lateral subungual onychomycosis (nail fungal infection) in multiple markets, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Astigmatism**, receiving a score of only **50%** (the minimum threshold), ranked **2,225,939th** among all predictions — with **0 clinical trials** and **0 relevant publications** supporting this direction.
The overall evidence picture across all 10 predicted indications is uniformly weak, with every candidate returning the minimum prediction score and no supporting clinical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Distal and lateral subungual onychomycosis (nail fungal infection) |
| Predicted New Indication (Rank 1) | Astigmatism |
| TxGNN Prediction Score | 50.00% (minimum threshold; rank 2,225,939) |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 licensed products) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published literature retrieved during evidence collection, efinaconazole is a topical triazole antifungal that works by inhibiting **sterol 14α-demethylase (CYP51)**, an enzyme essential for ergosterol biosynthesis in fungal cell membranes. By depleting ergosterol, it disrupts fungal membrane integrity and inhibits growth. Its 10% nail solution formulation is specifically designed with low surface tension and minimal keratin binding to improve nail penetration.

Astigmatism, the top-ranked predicted indication, is a refractive error caused by irregular curvature of the cornea or lens — a purely **anatomical and optical defect**. There is no known physiological pathway connecting CYP51 inhibition, ergosterol biosynthesis, or antifungal activity to corneal curvature. This mechanistic mismatch is fundamental, not peripheral.

The TxGNN model score of 0.5 represents the **minimum possible output**, and the prediction rank of 2,225,939 places this candidate at the very bottom of the model's output space. This pattern strongly suggests a non-specific graph neural network output rather than a biologically meaningful signal. Importantly, the same minimum score (0.5) and similarly extreme ranks apply to **all 10 predicted indications** in this Evidence Pack, none of which have a plausible pharmacological link to a topical CYP51 inhibitor with negligible systemic absorption.

---

## Clinical Trial Evidence

No clinical trials are currently registered for efinaconazole in any of the 10 predicted indications.

---

## Literature Evidence

Only 2 publications were retrieved across all 10 predicted indications, both associated with the "dermatitis, atopic" prediction (Rank 2). Neither publication provides evidence for efinaconazole in atopic dermatitis — they concern its approved indication (onychomycosis).

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24850511](https://pubmed.ncbi.nlm.nih.gov/24850511/) | 2014 | Review | Expert Review of Anti-infective Therapy | Comprehensive review of efinaconazole 10% nail solution for onychomycosis; describes CYP51 inhibition mechanism and MIC advantages over terbinafine, ciclopirox, itraconazole, and amorolfine against *T. rubrum*, *T. mentagrophytes*, and *C. albicans* |
| [24691669](https://pubmed.ncbi.nlm.nih.gov/24691669/) | 2014 | Conference Proceedings | American Journal of Clinical Dermatology | Summary of 72nd Annual Meeting of the American Academy of Dermatology; not specific to efinaconazole or atopic dermatitis |

> **Note:** Neither publication supports efinaconazole for atopic dermatitis. The indirect mechanistic hypothesis (antifungal targeting *Malassezia* as an AD trigger) remains unexplored for this specific drug.

---

## Taiwan Market Information

Efinaconazole currently has **no approved products in Taiwan**. No DIN/license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for efinaconazole received the minimum possible prediction score (0.5) at extreme ranking positions (2,225,939–2,225,948), with zero supporting clinical trials and zero relevant literature for any new indication. The top prediction, astigmatism, has no pharmacologically plausible connection to a topical CYP51 inhibitor, and the uniform minimum-score pattern across all candidates suggests these are non-specific model outputs rather than actionable repurposing signals.

**To proceed, the following would be needed:**

- **Reassess TxGNN inputs:** Verify that the drug node for efinaconazole in the knowledge graph is correctly linked to its known targets (CYP51/ERG11) and approved indication (onychomycosis); minimum scores across all predictions suggest a data pipeline or graph connectivity issue
- **Mechanistic data (MOA):** Obtain full DrugBank profile including drug targets, pathways, and categories to enable proper mechanistic filtering
- **Taiwan regulatory package insert:** Download from the TFDA website (if efinaconazole is approved in future) to complete safety screening — currently blocking entry to Stage S1
- **Hypothesis-driven repurposing:** If investigating efinaconazole beyond onychomycosis, a rational starting point would be **Malassezia-associated dermatological conditions** (e.g., seborrheic dermatitis, pityriasis versicolor, or Malassezia-sensitive atopic dermatitis subtypes) where the antifungal mechanism has biological plausibility — this requires a separate, targeted evidence search
- **Do not advance any current TxGNN prediction to clinical feasibility review** until model output quality is confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

