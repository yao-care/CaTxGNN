---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout / Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a well-established xanthine oxidase (XO) inhibitor widely used to manage gout and hyperuricemia by reducing uric acid synthesis. The TxGNN model predicts it may have potential in **Hepatic Porphyria**, supported by **0 clinical trials** and **2 publications** offering only indirect mechanistic hypotheses. Evidence remains at a preclinical hypothesis level (L4), and — critically — allopurinol is itself documented as a potentially porphyrinogenic agent, creating a bidirectional risk that must be resolved before any further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricemia (standard international use; no Canadian DIN records in this Evidence Pack) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, allopurinol inhibits xanthine oxidase (XO) — the enzyme responsible for converting hypoxanthine and xanthine to uric acid — thereby reducing uric acid production. A secondary consequence of XO inhibition is reduced generation of reactive oxygen species (ROS), giving allopurinol a known antioxidant profile beyond its urate-lowering effect.

The proposed connection to hepatic porphyria rests on a theoretical metabolic link: XO inhibition may modulate the purine/heme precursor balance in the liver. 5-Aminolevulinic acid (5-ALA) synthase — the rate-limiting enzyme of hepatic heme biosynthesis — operates under negative feedback control by a small regulatory heme pool in the hepatic cytosol. The hypothesis, as outlined in PMID 31443750, is that upstream modulation of heme utilization pathways could indirectly regulate 5-ALA synthase activity, potentially reducing the toxic accumulation of heme precursors characteristic of hepatic porphyrias.

However, a critical counter-consideration dominates this evaluation: **allopurinol is itself documented in the literature as a potentially porphyrinogenic drug**, capable of precipitating acute porphyric attacks by inducing 5-ALA synthase rather than suppressing it. The mechanistic relationship is therefore bidirectional — allopurinol could plausibly worsen rather than improve porphyria depending on dose, subtype, and metabolic context. Distinguishing between acute and non-acute hepatic porphyria subtypes, and resolving whether the XO–heme biosynthesis link is protective or exacerbating, is a prerequisite for any further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Opinion | Medical Hypotheses | Proposes metabolic targeting of hepatic 5-ALA synthase by inhibiting heme utilization via tryptophan 2,3-dioxygenase (TDO) as a therapy for acute hepatic porphyrias; supports the concept that heme pool regulation can modulate 5-ALA synthase, providing indirect theoretical context for XO inhibitors |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study | Biochemical Pharmacology | Examined carbamazepine's acute effects on hepatic heme metabolism in rats as a model of drug-induced porphyria exacerbation; provides mechanistic framework for how certain drugs disturb the hepatic heme pool — relevant as contextual evidence that drug-induced porphyrinogenicity is a real and measurable risk |

---

## Canada Market Information

No Canadian Drug Identification Numbers (DINs) are on record for Allopurinol in this Evidence Pack. The drug is classified as **not marketed** in the Canadian regulatory database used for this analysis. Regulatory standing should be independently verified against the current Health Canada Drug Product Database, as this data may reflect a gap in the regulatory source rather than confirmed non-availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Safety Signal (derived from mechanistic evidence):** The repurposing rationale retrieved in this Evidence Pack explicitly identifies allopurinol as a potentially **porphyrinogenic drug** — meaning it may *precipitate* rather than treat acute porphyric attacks. This is not a theoretical concern but a pharmacologically documented risk that fundamentally challenges the rationale for this repurposing direction. This signal must be fully characterized before any further development steps are considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for allopurinol in hepatic porphyria consists solely of indirect mechanistic hypotheses (L4), with zero registered clinical trials and two tangentially relevant publications — one of which documents a potential harm signal where allopurinol itself may exacerbate porphyria. The bidirectional risk profile (potential therapeutic effect vs. documented porphyrinogenic risk) has not been resolved in any clinical or preclinical model specifically designed to test this question.

**To proceed, the following is needed:**

- **Safety clarification (blocking):** Conduct a systematic literature review to determine whether allopurinol consistently exacerbates acute hepatic porphyria, and whether this risk is subtype-specific or dose-dependent
- **Subtype stratification:** Define which hepatic porphyria subtype is the target (e.g., acute intermittent porphyria vs. porphyria cutanea tarda), as the mechanistic logic and risk profile differ substantially between subtypes
- **MOA data acquisition:** Retrieve full mechanism of action details from DrugBank or primary pharmacology sources to formally characterize XO inhibition's role in hepatic heme biosynthesis regulation
- **Safety data acquisition:** Obtain full warning, contraindication, and drug-drug interaction data from the Canadian product monograph or WHO drug information summary
- **Preclinical proof-of-concept:** Design or identify in vitro or animal model studies that directly test allopurinol's effect on 5-ALA synthase activity and porphyrin accumulation before any clinical hypothesis can be formed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

