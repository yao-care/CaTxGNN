---
layout: default
title: Carbon Monoxide
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Carbon Monoxide
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

# Carbon Monoxide: From Investigational Agent to Sclerosing Cholangitis

## One-Sentence Summary

Carbon monoxide (CO) is an endogenous gaseous signalling molecule (DrugBank DB11588) with no currently approved therapeutic indication; it is primarily being explored pharmacologically through CO-releasing molecules (CORMs) in preclinical settings.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis** via the HO-1/CO anti-inflammatory axis,
however, **no clinical trials and no published literature** currently support this specific direction, placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None (no approved therapeutic indications exist) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known biology, carbon monoxide is an endogenous gaseous mediator produced enzymatically by heme oxygenase-1 (HO-1) from heme catabolism. The HO-1/CO signalling axis is broadly cytoprotective: CO activates soluble guanylyl cyclase (sGC), raises intracellular cGMP, and suppresses NF-κB-driven inflammatory gene expression. It also promotes anti-proliferative and anti-oxidant responses, all of which have been characterised in cardiovascular and pulmonary vascular preclinical models.

Sclerosing cholangitis — both primary (PSC) and secondary forms — is driven by chronic biliary inflammation leading to concentric periductal fibrosis, progressive bile duct stricturing, and eventual cirrhotic liver failure. The theoretical appeal of CO here lies in its anti-fibrotic potential: HO-1-derived CO has been shown in other hepatic contexts to reduce stellate cell activation and collagen deposition. If a similar mechanism were operative in the biliary epithelium, CO or CO-releasing molecules (CORMs) might slow the fibroinflammatory cascade underlying sclerosing cholangitis.

However, this rationale is entirely speculative. No preclinical animal model studies (e.g., Mdr2-knockout mice, which develop PSC-like lesions) and no human clinical data exist for this indication. The TxGNN prediction most likely reflects indirect knowledge graph co-occurrence between CO-related biological pathways and cholangiopathy disease nodes, rather than a direct experimentally validated mechanistic link. This prediction must be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for investigators:** Carbon monoxide is a potent cellular toxin at supraphysiological concentrations, causing haemoglobin saturation (carboxyhaeamoglobinaemia) and inhibiting cytochrome c oxidase. Any therapeutic development programme must establish a safe therapeutic window — most CORM and inhaled CO research uses concentrations of 250 ppm or below. Full toxicological profiling and a dedicated safety monitoring plan would be prerequisite before any first-in-human studies.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Carbon monoxide has no approved therapeutic indication anywhere in the world, and there is a complete absence of clinical or preclinical evidence specifically addressing its use in sclerosing cholangitis; the TxGNN prediction at L5 represents model-inferred association only and cannot support any actionable development decision at this time.

**To proceed, the following is needed:**
- Retrieve complete mechanism of action data from DrugBank API and primary pharmacology literature to confirm or refute the HO-1/CO anti-fibrotic rationale in the biliary context
- Commission or identify proof-of-concept preclinical studies using CORMs (e.g., CORM-2, CORM-3) or inhaled CO in established PSC animal models (Mdr2−/−, DDC-diet mice)
- Define a safe therapeutic concentration window and delivery route (inhaled CO vs. CORM prodrug) before any investigational new drug (IND) pathway is considered
- Consult Health Canada on regulatory classification of CO as a drug substance
- **Prioritise the Rank 8 prediction (Pulmonary Hypertension, L4, "Research Question")** over this indication: it has direct mechanistic data (PMID 16908624 demonstrating CO reversing established PAH in animal models; PMID 35318039 on CO in hypertension-induced vascular smooth muscle injury) and at least one Phase 1 clinical signal (NCT01818843 — inhaled CO in neonatal pulmonary hypertension), making it a significantly more tractable near-term research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

