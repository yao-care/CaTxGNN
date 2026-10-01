---
layout: default
title: Pimecrolimus
parent: High Evidence (L1-L2)
nav_order: 729
evidence_level: L2
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus (Elidel) is a topical calcineurin inhibitor. Its established use is atopic dermatitis, which comes from the supporting trials and literature, since the Canadian licence record supplied no indication text.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**, with **1 clinical trial** (Phase 2, completed) and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (inferred from trials and literature; not stated in the Canadian licence data) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the drug record. From the published literature, pimecrolimus is a calcineurin inhibitor developed for topical therapy of inflammatory skin diseases. It selectively targets T cells and mast cells. It inhibits T-cell proliferation and the release of IL-2, IL-4, interferon-gamma and TNF-α, and it inhibits mast cell degranulation.

Atopic dermatitis and seborrheic dermatitis are both chronic, relapsing inflammatory skin conditions. Seborrheic dermatitis has a clear inflammatory component, and its facial form responds to non-steroidal anti-inflammatory agents. Topical corticosteroids are a mainstay of treatment, but long-term use causes side effects, so steroid-sparing alternatives are needed. A non-steroidal, T-cell-directed agent fits that gap mechanistically.

The TxGNN score (99.73%) is a computational prediction only. The evidence level was set from the actual trials and publications, not from the score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomized, double-blind, parallel-group, active-comparator study of Elidel in seborrheic dermatitis. It is described as exploratory, to determine effectiveness. The comparator and endpoints are not stated in the supplied record, and no results were provided. |

This is the only trial in the dataset for this indication, and no Phase 3 trial is listed. That is why the level is capped at L2.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream appears well tolerated and effective for seborrheic dermatitis, compared with corticosteroids, antimycotics, placebo or no intervention |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic review of RCTs | Cureus | Reviews the efficacy and safety of pimecrolimus in facial seborrheic dermatitis |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clin Exp Dermatol | Randomized blinded trial of pimecrolimus 1% vs sertaconazole 2% cream in facial seborrheic dermatitis |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Ir J Med Sci | Compares sertaconazole 2% cream with pimecrolimus 1% cream in seborrheic dermatitis |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Open-label randomized comparative study | J Dermatol Treat | Pimecrolimus 1% cream vs ketoconazole 2% cream in seborrheic dermatitis |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Clinical study | J Cosmet Dermatol | Compares different regimens (treatment periods) of pimecrolimus 1% cream in facial seborrheic dermatitis |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | Am J Clin Dermatol | Pimecrolimus 1% cream is effective and well tolerated in resistant seborrheic dermatitis of the face |
| [19391059](https://pubmed.ncbi.nlm.nih.gov/19391059/) | 2010 | Clinical study | J Dermatol Treat | Explores effective and safe repetitive use in relapsing seborrheic dermatitis |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | Clinical study | J Dermatol Treat | Close follow-up with mean cure and remission times and side-effect profile; off-label use is increasing |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Clinical study | Drugs Exp Clin Res | Pimecrolimus 1% cream assessed for efficacy, tolerability and safety in adults with seborrheic dermatitis of the face and upper trunk |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2247238 | ELIDEL |

Dosage form and approved indication text were not provided in the licence record.

---

## Safety Considerations

Package-insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for safety information.

Points from the literature that should inform any use in seborrheic dermatitis:
- The topical calcineurin inhibitor class carries a boxed-warning context (malignancy and infection signal). A 2023 systematic review and meta-analysis examined cancer risk with pimecrolimus and tacrolimus ([PMID 36370744](https://pubmed.ncbi.nlm.nih.gov/36370744/)).
- Avoid occlusion and avoid use on infected skin.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 randomized trial (n=113) plus two systematic reviews of RCTs and several head-to-head RCTs support efficacy in facial seborrheic dermatitis. However, no Phase 3 trial is listed, so the evidence stays at L2.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- The Canadian approved indication text, to confirm that seborrheic dermatitis is outside the current label
- Results and comparator details for NCT00403559
- Detailed mechanism of action data
- Guardrails for any use: facial or short-term use, mild-to-moderate disease, no occlusion, no use on infected skin, and review of the long-term malignancy debate

**Other predictions in this dataset (for context):**
- Dermatitis (atopic): L1, supported by Phase 3 trials, but this confirms the existing indication rather than repurposing.
- Exanthem: L2, a research question. The trials cover heterogeneous conditions and are small, so a defined target condition is needed first.
- Acrodermatitis chronica atrophicans: L5, Hold. There is no evidence, and an immunosuppressant has no clear rationale against this infectious condition.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

