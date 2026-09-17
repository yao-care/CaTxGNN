---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

Using superpowers:using-superpowers to confirm no other skill overrides — this is a direct report-writing task fully specified by the prompt itself, so I'll proceed to draft the report per the given template.

One data note before the report: `predicted_indications` has 10 ranked candidates, not one. The evidence pack's own scoring already flags rank #1 (acne, highest TxGNN score) as a likely false positive (mismatched literature), while only **alveolar echinococcosis** (rank 5) reaches L3/S2 with real trial + literature support and a "Proceed with Guardrails" recommendation. I built the report around that candidate rather than blindly following array index 0, and added a screened-out table for transparency.

---

# Mebendazole: From Anthelmintic Use to Alveolar Echinococcosis

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic that works by inhibiting parasite β-tubulin polymerization. Among 10 TxGNN-predicted indications screened in this evidence pack, only **Alveolar Echinococcosis** is backed by real, drug-specific evidence — **1 clinical trial** and **20 publications** — while the remaining candidates (including the top-scoring "acne" prediction) show no relevant supporting literature and are likely false positives.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (no Canadian marketing authorization on record). Pharmacologically classified as a benzimidazole anthelmintic. |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 94.20% |
| Evidence Level | L3 (observational/cohort studies and reviews; no RCT) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not separately available for mebendazole in this evidence pack, but the mechanism is described consistently across the literature evidence: mebendazole is a **benzimidazole** that inhibits β-tubulin polymerization in parasite cells, blocking microtubule formation and glucose uptake, leading to parasite death or growth arrest.

Alveolar echinococcosis (AE) is caused by the larval (metacestode) stage of *Echinococcus multilocularis*, a cestode (tapeworm) parasite — the same broad parasite class mebendazole's mechanism targets. This is not a novel biological hypothesis: mebendazole, alongside albendazole, is already the WHO-recognized standard chemotherapy for AE, used either as a primary treatment when surgery is not feasible or as adjuvant therapy after resection. Multiple decades of literature (1981–2025) confirm this established use, though the benzimidazoles are noted to be largely **parasitostatic rather than parasiticidal** in AE, meaning long-term/lifelong therapy and monitoring are typically required.

In short, this TxGNN prediction reflects a well-established clinical use rather than a speculative new mechanism — the evidence base is real, but the "new indication" framing overstates the novelty since mebendazole is already a guideline-recommended AE therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A (observational) | Completed | 50 | Prospective follow-up study of hepatic alveolar echinococcosis patients treated with benzimidazole therapy (albendazole), evaluating parasite viability markers and imaging to guide treatment-withdrawal decisions. Graded "B" relevance — a monitoring/biomarker study, not a mebendazole efficacy RCT. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Reviews albendazole/mebendazole as the established AE chemotherapy and surveys novel compounds in development. |
| [19254162](https://pubmed.ncbi.nlm.nih.gov/19254162/) | 2009 | Review | Expert Rev Anti Infect Ther | Consensus review on benzimidazole use for cystic and alveolar echinococcosis. |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Cohort/Comparative | J Antimicrob Chemother | 35 patients treated with mebendazole or albendazole followed ~39 months; compares treatment regimens and outcomes. |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Cohort (animal/human PK) | Eur J Clin Pharmacol | Mebendazole plasma concentrations correlated with parasite weight reduction in infected animal models and humans. |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Case Report | J Hepatology | 13-year continuous mebendazole therapy in a non-resectable AE patient; suggests long-term therapy may be parasitocidal, not just parasitostatic. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management of liver echinococcosis; surgery remains cornerstone, benzimidazoles as adjunct. |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current status of drug therapy for AE; discusses limitations of benzimidazole-only regimens. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Surveys chemotherapy progress for AE; benzimidazoles remain the only recommended compounds but are parasitostatic. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | Status/prospects of novel treatments for AE and CE; notes no nonsurgical alternative has replaced albendazole/mebendazole. |
| [16044412](https://pubmed.ncbi.nlm.nih.gov/16044412/) | 2005 | Retrospective Cohort | Br J Surg | 25-year prospective data comparing benzimidazole-alone, curative resection + adjuvant benzimidazole, and debulking + continuous benzimidazole strategies. |

---

## Canada Market Information

Mebendazole currently has **no marketing authorization on record in Canada** (0 DINs/licenses in this evidence pack), so no product listing table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags a **Blocking data gap** for TFDA/regulatory label warnings and contraindications (drug monograph not yet retrieved), which must be resolved before any formal safety assessment can proceed.

---

## Other TxGNN Predictions (Screened Out)

For transparency, the other 9 predicted indications in this evidence pack scored higher or comparably by TxGNN but had **no matching or relevant clinical/literature evidence**, and are not recommended for further action:

| Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Acne (disease) | 99.20% | L5 | Hold | Rank-1 by score, but sole literature match (a sparganosis case report) is unrelated to acne — assessed as a false positive. |
| Echinococcus granulosus infectious disease | 95.61% | L4 | Research Question | Same drug class rationale as AE (cestode infection), but no direct trials/literature captured for this specific term. |
| Demodicidosis of sebaceous gland | 92.99% | L5 | Research Question | Mechanistically plausible (mite microtubule sensitivity) but zero supporting evidence. |
| Leishmaniasis (diffuse cutaneous), Hordeolum, Inhalational/toxin-mediated botulism, Impetigo, Sorsby's fundus dystrophy | 93–98% | L5 | Hold | No mechanistic plausibility and no supporting evidence found. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alveolar echinococcosis is the only candidate in this evidence pack supported by an actual clinical trial and a substantial, drug-specific literature base (20 publications spanning 1981–2025). It also reflects an already-established WHO-recognized clinical use of mebendazole rather than a speculative new mechanism, though efficacy is parasitostatic rather than curative and mebendazole is not currently marketed in Canada.

**To proceed, the following is needed:**
- Regulatory/label safety data (warnings, contraindications) — currently a **Blocking** data gap preventing formal safety assessment
- Confirmed mechanism-of-action documentation from DrugBank (currently missing at the drug level)
- Canadian market-access pathway assessment, since mebendazole holds no current DIN/license in Canada
- Direct evidence review for the related "echinococcus granulosus infectious disease" prediction, which shares mebendazole's established mechanism but lacks captured trial/literature data in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

