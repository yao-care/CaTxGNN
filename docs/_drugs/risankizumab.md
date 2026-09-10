---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Plaque Psoriasis to Dermatitis

## One-Sentence Summary

> Risankizumab is an anti-IL-23 (p19 subunit) monoclonal antibody originally developed and globally approved for moderate-to-severe plaque psoriasis and related psoriatic conditions.
> The TxGNN model predicts it may be effective for the broader category **Dermatitis**,
> with **7 clinical trials** and **17 publications** currently identified as supporting evidence — though only one of these trials is a completed randomized controlled trial specifically testing this indication (atopic dermatitis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via Canadian regulatory data (drug not marketed in Canada); globally first approved for plaque psoriasis, psoriatic arthritis, generalized pustular psoriasis, and erythrodermic psoriasis (Japan, 2019) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the DrugBank record supplied (flagged as a High-severity data gap). Based on known information from the supporting literature (e.g. PMID 31098898), risankizumab is a humanized IgG monoclonal antibody that selectively blocks the p19 subunit of interleukin-23 (IL-23), inhibiting the Th17 inflammatory axis. Its efficacy in plaque psoriasis — a disease strongly driven by IL-23/Th17 signaling — is well established and forms the basis of its original approval.

"Dermatitis" as predicted by TxGNN is a broad, heterogeneous category. It encompasses several distinct disease entities with differing mechanistic fit to IL-23 blockade: at one end, **erythrodermic psoriasis** and **acrodermatitis continua of Hallopeau** are Th17/IL-23-driven and mechanistically close to the approved indication (supported by case reports and cohort data). At the other end, **atopic dermatitis** is predominantly a Th2-mediated disease, making the mechanistic rationale for IL-23 blockade weaker — yet a completed Phase 2 RCT (NCT03706040, corroborated by PMID 36588137) demonstrated clinical benefit, suggesting a partial but real IL-22/Th17 contribution in a subset of AD patients.

Because the "dermatitis" label mixes mechanistically strong and mechanistically weak sub-indications, the aggregate evidence should be interpreted with caution: the strongest, most direct evidence applies narrowly to atopic dermatitis (one completed Phase 2 RCT), not to dermatitis as a whole.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | RCT, placebo-controlled, evaluating risankizumab for moderate-to-severe atopic dermatitis in adults/adolescents |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Risankizumab for moderate-to-severe genital or scalp psoriasis (approved-indication extension) |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Open-label comparison of risankizumab vs. apremilast in moderate plaque psoriasis |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Taiwan real-world observational cohort on durability of risankizumab response (PASI 90) vs. other biologics in plaque psoriasis |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective pharmacogenetic study on 10-year survival of biologic therapies in cutaneous psoriasis ± psoriatic arthritis |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Observational biomarker profiling study across six inflammatory skin diseases, including atopic dermatitis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice-based skin delivery testing of FDA-approved atopic dermatitis/psoriasis drugs |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 RCT showing risankizumab efficacy in moderate-to-severe atopic dermatitis, supporting a role for IL-23/IL-22 blockade in AD |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Cohort | Int J Dermatol | Effectiveness/safety of combined dupilumab + risankizumab in patients with concomitant AD and psoriasis |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Cohort | Experimental Dermatology | Retrospective study of risankizumab in patients with history of erythrodermic psoriasis; identifies predictors of response |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" review describing risankizumab's mechanism (anti-IL-23 p19) and initial approved indications |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules for pediatric alopecia areata, psoriasis, AD, and hidradenitis suppurativa |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opin Biol Ther | Review of emerging biologics for pediatric atopic dermatitis |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Review | Am J Clin Dermatol | Systematic review of systemic therapies for erythrodermic psoriasis |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraisal of systemic immunomodulators for psoriasis and eczema in military personnel |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Review | Inflammopharmacology | Systematic review of interleukin inhibitors in lichen planus, including therapeutic and paradoxical effects |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | J Dermatol Treat | Case report of acrodermatitis continua of Hallopeau successfully treated with risankizumab |

---

## Canada Market Information

Risankizumab is not currently marketed in Canada; no DIN registrations are available in the regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A Blocking-severity data gap (DG001) exists — TFDA/manufacturer label warnings and contraindications have not yet been retrieved, meaning this candidate cannot currently complete an initial (S1) safety assessment. Drug interaction data query also returned no results.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication "dermatitis" bundles mechanistically strong (erythrodermic psoriasis, Hallopeau acrodermatitis — Th17-driven) and mechanistically weaker (atopic dermatitis — Th2-driven) sub-conditions, with only one completed Phase 2 RCT directly supporting a single sub-indication (atopic dermatitis). Combined with a Blocking-severity gap preventing initial safety assessment and the drug's current non-marketed status in Canada, the evidence is not yet sufficient to proceed.

**To proceed, the following is needed:**
- Retrieve TFDA/manufacturer package insert (warnings, contraindications) to unblock the S1 safety assessment
- Confirm detailed mechanism of action (MOA) directly from DrugBank
- Narrow the target indication from the broad "dermatitis" category to a single, mechanistically justified disease (e.g., atopic dermatitis or erythrodermic psoriasis) before advancing
- Await Phase 3 confirmatory data for the atopic dermatitis signal, given current evidence is limited to a single completed Phase 2 RCT
- Obtain drug-drug interaction (DDI) data, currently unavailable (query_status: not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

