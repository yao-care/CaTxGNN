---
layout: default
title: Cromoglicic Acid
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Cromoglicic Acid
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

# Cromoglicic Acid: From Allergic Conditions to Ulcerative Proctosigmoiditis

## One-Sentence Summary

Cromoglicic acid (disodium cromoglycate, DSCG) is a mast cell stabilizer with established international use for IgE-mediated allergic conditions — including allergic asthma, rhinitis, and conjunctivitis — though it holds no approved product registrations in Canada.
The TxGNN model ranks **Ulcerative Proctosigmoiditis** as its top predicted new indication (score 99.99%), supported by **0 registered clinical trials** and **2 publications**.
Critically, one of those two publications is a double-blind controlled trial that demonstrated **no significant benefit** of local rectal DSCG, making this prediction a clear Hold despite the high model score.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Canada; globally used for allergic asthma, allergic rhinitis, allergic conjunctivitis, and food allergy |
| Predicted New Indication | Ulcerative Proctosigmoiditis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published pharmacological knowledge, cromoglicic acid acts as a **mast cell stabilizer**: it prevents mast cell degranulation and blocks the release of inflammatory mediators — including histamine, leukotrienes, and prostaglandins — triggered by IgE-mediated stimulation. This mechanism underpins its established clinical use in allergic disease.

The colonic and rectal mucosa contains resident mast cells, and chronic mucosal inflammation in ulcerative proctosigmoiditis has been associated with mast cell activation in some research contexts. The TxGNN knowledge graph therefore identifies a plausible mechanistic bridge: if mucosal mast cells drive local inflammation, stabilizing them with DSCG delivered rectally could in theory reduce disease activity. The prediction is conceptually coherent.

However, this biological rationale does **not** hold up to clinical scrutiny. A double-blind, placebo-controlled study (PMID 3090860) of 43 patients treated with 600 mg DSCG rectal enemas for 8 weeks found no statistically significant benefit across clinical, endoscopic, laboratory, and biopsy endpoints. The most likely explanations are that DSCG has insufficient rectal mucosal penetration, or that the dominant inflammatory mechanism in ulcerative proctosigmoiditis is mast cell–independent (e.g., driven primarily by neutrophil and T-cell pathways). This is a case where a high TxGNN score reflects network topology rather than translatable biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cromoglicic acid in ulcerative proctosigmoiditis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3090860](https://pubmed.ncbi.nlm.nih.gov/3090860/) | 1986 | Clinical Trial (direct indication match) | *Acta Medica Scandinavica* | Double-blind RCT (n=43): rectal DSCG 600 mg enema vs. placebo for 8 weeks showed **no statistically significant differences** in bowel frequency, rectal bleeding, endoscopy, biopsies, or laboratory tests — local DSCG deemed ineffective for ulcerative proctosigmoiditis |
| [1967326](https://pubmed.ncbi.nlm.nih.gov/1967326/) | 1990 | Review | *Medical Clinics of North America* | Reviews therapeutic options for ulcerative proctosigmoiditis; high-dose 5-ASA enemas may be superior to hydrocortisone enemas; notes that patients failing one therapy may respond to alternatives — DSCG not highlighted as a recommended option |

---

## Canada Market Information

Cromoglicic acid has no approved product registrations in Canada. There are currently **0 Drug Identification Numbers (DINs)** on file. A full regulatory submission would be required before any Canadian marketing or clinical trial authorization could proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model assigning a near-perfect prediction score, a direct double-blind controlled trial has already established that rectal cromoglicic acid is **clinically ineffective** for ulcerative proctosigmoiditis. Proceeding with this specific indication would require overcoming both the existing negative clinical evidence and significant pharmacokinetic barriers (mucosal penetration), without a clear mechanistic advantage over established therapies such as 5-ASA.

**To move forward productively, the following is recommended:**

- **Deprioritize ulcerative proctosigmoiditis** as a repurposing target for rectal DSCG — the negative RCT constitutes sufficient evidence to close this direction without further investment
- **Redirect attention to allergic urticaria (TxGNN Rank #9):** this indication shows a substantially more compelling profile — 19 supporting publications, a mechanistic link highly congruent with DSCG's core mast cell–stabilizing action, and published clinical data supporting benefit in IgE-mediated food allergy with urticaria/angioedema (PMID 3091307)
- **Obtain full MOA data** from DrugBank (currently a data gap) to formally characterize mechanism–indication alignment across all top predictions
- **Download and parse the Health Canada product monograph** if pursuing any Canadian regulatory pathway — no approved labelling, warnings, or contraindications are currently on record
- **If pursuing rosacea conjunctivitis (Rank #3):** ocular DSCG is already well-established for allergic conjunctivitis; small investigator-initiated studies exploring the mast cell component of ocular rosacea would be a low-cost, plausible next step given existing ophthalmic formulation availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

