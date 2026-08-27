---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid Replacement Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a physiological glucocorticoid classically used as systemic replacement therapy for adrenal insufficiency and as an anti-inflammatory/immunosuppressive agent in topical and systemic forms. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **1 directly-relevant completed Phase 3 RCT** (plus 3 supporting trials in related dermatologic/endocrine contexts) and **20 publications** currently supporting this direction, including a head-to-head randomized trial against clobetasol propionate in children.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (TFDA label data pending — see Data Gap DG001) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (1 completed Phase 3 RCT directly using hydrocortisone) |
| Canada Market Status | Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology, hydrocortisone is a naturally-occurring glucocorticoid used therapeutically as a physiological corticosteroid replacement and as an anti-inflammatory/immunosuppressive agent in both systemic and topical formulations. Its efficacy in these established uses is well documented, and mechanistically this same anti-inflammatory/immunosuppressive action may be applicable to alopecia areata.

Alopecia areata is now understood to be a T-cell–mediated autoimmune disease that targets the hair follicle, producing a peri-follicular inflammatory infiltrate ("swarm of bees" pattern histologically). As a corticosteroid, hydrocortisone can suppress this T-cell–driven inflammation and exert local immunosuppression around the follicle, thereby permitting hair regrowth. Topical corticosteroids — as a class — are already established as a first-line treatment option in alopecia areata management guidelines, which gives this prediction a more direct mechanistic grounding than many purely network-inferred TxGNN candidates.

This link is further reinforced by a long historical record of clinical use: intradermal and intracutaneous hydrocortisone injections for alopecia areata were reported as early as the 1950s–1960s, and a modern randomized trial has directly tested hydrocortisone (1% cream) against a higher-potency steroid (clobetasol propionate 0.05%) in pediatric patients, indicating sustained clinical interest in hydrocortisone specifically — not just corticosteroids as a class — for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized controlled trial in children with alopecia areata directly comparing hydrocortisone 1% cream vs. clobetasol propionate 0.05% cream — the primary head-to-head evidence for hydrocortisone in this indication |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluated adrenal-axis (HPA) effects of intralesional triamcinolone acetonide in alopecia areata patients; same corticosteroid class but not hydrocortisone itself — class-level supporting evidence only |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | NA | Not Yet Recruiting | 72 | Four-arm dose-response study of hair growth products vs. placebo in androgenic (not areata) alopecia; not yet started, low direct relevance |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studied effects of abnormal steroid metabolome on bone density/strength in mild autonomous cortisol secretion (MACS); not focused on treating alopecia areata — indirect relevance only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Published results of the RCT comparing hydrocortisone 1% vs. clobetasol propionate 0.05% for alopecia areata in children (corresponds to NCT01453686) |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort | Clinical and Experimental Dermatology | Retrospective single-center analysis of topical corticosteroid occlusion therapy for severe alopecia areata in children |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | J Eur Acad Dermatol Venereol | Reviews evidence on HPA-axis activity and cortisol production in alopecia areata patients |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Historical series treating alopecia areata, partialis, and totalis with cortisone, hydrocortisone, prednisone, and prednisolone |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case report | Der Hautarzt | Hair regrowth in alopecia areata/maligna following intracutaneous hydrocortisone injection |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case series | Vestnik Dermatologii i Venerologii | Treatment of alopecia areata and total alopecia via intracutaneous hydrocortisone injections |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case report | Actas Dermo-Sifiliográficas | Treatment of alopecia areata with intradermal hydrocortisone injections |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case series | J Am Acad Dermatol | Four cases of congenital alopecia areata, treated with topical agents including corticosteroids |
| [5696522](https://pubmed.ncbi.nlm.nih.gov/5696522/) | 1968 | Observational | British Journal of Dermatology | Scalp blood vessel changes in alopecia areata before and after corticosteroid therapy |
| [22381765](https://pubmed.ncbi.nlm.nih.gov/22381765/) | 2012 | Mechanistic | J Southern Medical University | Serum cortisol levels and PBMC glucocorticoid receptor mRNA expression in severe alopecia areata |

---

## Canada Market Information

Hydrocortisone currently has **no approved product license on file** for this market (**0 DINs**; market status: **Not Marketed**). No dosage form or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (TFDA label data is a **Blocking** data gap — DG001 — required before any Stage S1 safety review can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single completed Phase 3 RCT (NCT01453686 / PMID 24226568) directly compares hydrocortisone against an active corticosteroid comparator in pediatric alopecia areata, and this is reinforced by decades of case-level literature on intradermal and topical hydrocortisone use in the same indication. However, the trial had no placebo arm, evidence is limited to a single controlled trial (L2, not L1), and hydrocortisone is not currently marketed in this jurisdiction — so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Data Gap DG001, Blocking — required before S1 safety review)
- Detailed mechanism of action documentation (Data Gap DG002)
- Confirmation of which route/formulation (topical vs. systemic) is intended for the alopecia areata indication, and its compatibility with available product forms
- Additional placebo-controlled or larger-scale RCTs to strengthen the evidence base beyond the single existing Phase 3 trial
- A market-entry/licensing assessment, since hydrocortisone currently holds no approved license in this jurisdiction (0 DINs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

