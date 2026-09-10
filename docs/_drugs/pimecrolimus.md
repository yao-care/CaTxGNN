---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 620
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus (DrugBank DB00337) is a topical calcineurin inhibitor originally developed and approved (as Elidel®) for atopic dermatitis.
The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
with **1 clinical trial** and **18 publications** — including two systematic reviews of RCTs — currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (per international product labeling referenced in the trial evidence; no Canadian DIN license data is available) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Canada Market Status | 未上市 (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Pimecrolimus is a calcineurin inhibitor developed for topical therapy of inflammatory skin disease. Per literature in the evidence pack (PMID 16033622), it selectively targets T cells and mast cells — inhibiting T-cell proliferation and the production/release of IL-2, IL-4, interferon-gamma and TNF-alpha, as well as mast cell degranulation. The drug's `original_moa` field itself is a data gap; this mechanistic description is derived from the supporting literature rather than a structured DrugBank MOA record.

Atopic dermatitis (the original indication) and seborrheic dermatitis (the predicted new indication) are both chronic, relapsing inflammatory skin conditions driven substantially by cutaneous immune dysregulation, though seborrheic dermatitis additionally involves an inflammatory response to *Malassezia* yeast overgrowth. Both conditions present with erythema, scaling and pruritus, and both are conventionally managed with topical anti-inflammatory agents.

Because pimecrolimus's anti-inflammatory, T-cell-suppressing action is not disease-specific, it is mechanistically plausible that it would also reduce the inflammatory component of seborrheic dermatitis. This is no longer purely theoretical: it is already used off-label for this purpose, and the evidence pack contains a completed Phase 2 RCT plus two systematic reviews of RCTs (PMID 22142161, 36072203) concluding that pimecrolimus 1% cream has efficacy comparable to topical corticosteroids and antifungals, with a better long-term tolerability profile.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | Randomized, double-blind, parallel-group, active-comparator-controlled study of Elidel (pimecrolimus) for seborrheic dermatitis; graded "A" relevance — direct evidence for this exact indication |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream is a well-tolerated, effective treatment for seborrheic dermatitis, with efficacy comparable to corticosteroids/antimycotics |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review of RCTs | Cureus | Confirms efficacy and safety of pimecrolimus for facial seborrheic dermatitis across RCTs; calcineurin inhibitors are one of four main drug classes used |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Topical pimecrolimus reviewed among first-line topical agents for facial seborrheic dermatitis, alongside antifungals, keratolytics and corticosteroids |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | RCT (open, comparative vs ketoconazole) | J Dermatolog Treat | Open, randomized, prospective, comparative study of pimecrolimus 1% cream vs ketoconazole 2% cream for seborrheic dermatitis |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT (comparative vs sertaconazole) | Ir J Med Sci | Compared efficacy of sertaconazole 2% cream vs pimecrolimus 1% cream in treatment of seborrheic dermatitis |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT (randomized, blinded, comparative) | Clin Exp Dermatol | Randomized, blinded trial of pimecrolimus 1% vs sertaconazole 2% cream for facial seborrheic dermatitis; both effective |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | Am J Clin Dermatol | Pimecrolimus 1% cream effective and well tolerated for resistant facial seborrheic dermatitis in an open-label study |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Clinical comparative study | J Cosmet Dermatol | Compared different treatment regimens/durations of pimecrolimus 1% cream for facial seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Reviews current status and therapeutic horizons for facial seborrheic dermatitis, including calcineurin inhibitors |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | Int J Clin Pract | Describes pimecrolimus MOA as a calcineurin inhibitor targeting T cells/mast cells; reviews use beyond atopic dermatitis |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications and drug interaction data are not yet available in Health Canada regulatory sources — flagged as a blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT plus two systematic reviews of RCTs (L2 evidence) support pimecrolimus's efficacy in seborrheic dermatitis, but the drug is currently unmarketed in Canada (0 DINs) and safety labeling/MOA data are blocking gaps, so the recommendation cannot advance beyond guardrailed evaluation.

**To proceed, the following is needed:**
- Health Canada product monograph warnings/contraindications (DG001, blocking)
- Detailed mechanism of action confirmation from DrugBank/primary sources (DG002, high)
- Assessment of a Canadian market/access pathway given 未上市 status (0 DIN)
- Independent evidence review for the lower-confidence secondary predictions (dermatitis, exanthem, acrodermatitis chronica atrophicans) before any broader indication claims
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

