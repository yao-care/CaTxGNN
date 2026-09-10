---
layout: default
title: Lemborexant
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 1
---

# Lemborexant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lemborexant: From Unapproved Status in Canada to Insomnia (Difficulty Initiating and Maintaining Sleep)

## One-Sentence Summary

> Lemborexant is a dual orexin receptor antagonist (DORA) that is not currently marketed in Canada (0 DIN, market status: Not Marketed), so no original approved indication is on record in this dataset.
> The TxGNN model predicts it may be effective for **Insomnia (Sleep Disorder, Initiating and Maintaining Sleep)**,
> with **1 registered clinical trial** and **20 publications** — including multiple completed Phase 3 RCTs — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently authorized in Canada; no license/indication text on file |
| Predicted New Indication | Insomnia (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs reported in literature) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for lemborexant is not available in the structured drug record (original MOA field is empty). However, the supporting literature consistently identifies it as a **dual orexin receptor antagonist (DORA)**, competitively blocking OX1R and OX2R (with greater affinity for OX2R) to suppress orexin-mediated wake-promoting signaling, thereby facilitating sleep onset and maintenance.

Because no original indication is recorded for the Canadian market in this dataset, this is not a conventional "repurposing" case — it appears instead to reflect a drug that is approved and used elsewhere (the literature references first approval and subsequent regulatory use) but has not yet entered the Canadian market. The "predicted" indication (insomnia) aligns with the drug's already-established global therapeutic use as a DORA, which is mechanistically coherent: orexin antagonism is a well-validated pathway for treating both sleep-onset and sleep-maintenance insomnia, as shown across the cited Phase 3 trials and multiple network meta-analyses comparing DORAs (lemborexant, daridorexant, suvorexant) with standard hypnotics.

This mechanistic plausibility, combined with a substantial and mature literature base (including long-term Phase 3 safety/efficacy data), is why the TxGNN model assigns a very high prediction score (99.75%) — the evidence gap here is regulatory/market presence in Canada, not scientific rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not Yet Recruiting | 15 | Double-blind, placebo-controlled RCT (ELOSA) evaluating eszopiclone plus lemborexant in patients with obstructive sleep apnoea (OSA) and a low arousal threshold who have difficulty maintaining or falling asleep (COMISA population) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Lemborexant vs placebo and zolpidem tartrate ER in older adults with insomnia disorder |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3, SUNRISE 2) | Sleep | Long-term efficacy and tolerability of lemborexant vs placebo in adults with insomnia disorder |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Phase 3, follow-up of Study 303) | Sleep Medicine | 12-month continuous lemborexant treatment shows sustained effectiveness and safety in insomnia |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | RCT (post-hoc, polysomnography-defined subtypes) | J Clin Sleep Med | Lemborexant vs zolpidem ER differ by insomnia phenotype (short vs normal sleep duration) |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Review | Drugs | Overview of lemborexant's first regulatory approval and pharmacologic profile as a DORA |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic Review / Network Meta-analysis | Lancet | Comparative effectiveness of pharmacological treatments for acute and long-term insomnia |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Systematic Review / Network Meta-analysis | Translational Psychiatry | Comparative efficacy and safety of daridorexant, lemborexant, and suvorexant for insomnia |
| [37229388](https://pubmed.ncbi.nlm.nih.gov/37229388/) | 2023 | Expert Consensus | Frontiers in Psychiatry | Japanese expert consensus on insomnia treatment strategy, including hypnotic selection |
| [39277609](https://pubmed.ncbi.nlm.nih.gov/39277609/) | 2024 | Systematic Review | Translational Psychiatry | Orexin receptor antagonists (lemborexant, suvorexant) for insomnia comorbid with psychiatric disorders |
| [41071053](https://pubmed.ncbi.nlm.nih.gov/41071053/) | 2025 | Review | Expert Review of Clinical Pharmacology | Comprehensive review of lemborexant's role in insomnia treatment vs traditional hypnotics |

---

## Canada Market Information

Currently no Health Canada authorization on file — the drug has 0 registered DINs and market status is "Not Marketed." No licensed product/indication text is available for this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. No local (Canada) safety warnings, contraindications, or drug-interaction data are currently on file — this is flagged as a **Blocking** data gap (DG001: TFDA/Health Canada label warnings and contraindications not yet retrieved), which prevents a full safety pre-assessment at this stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Global literature evidence for lemborexant in insomnia is strong (multiple completed Phase 3 RCTs plus extensive review/meta-analysis support), but the drug has no current Canadian market presence (0 DIN) and no local label/safety data, so a Canada-specific go/no-go decision cannot be finalized yet.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain Health Canada product monograph / label warnings and contraindications
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to formally document MOA
- Confirm whether a Health Canada submission for lemborexant is planned or in progress
- Once label data is available, complete the S1 safety pre-assessment before any regulatory or clinical recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

