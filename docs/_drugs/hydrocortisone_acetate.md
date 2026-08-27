---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
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

Using data-report discipline (present exactly what's in the Evidence Pack, no fabrication, mark data gaps honestly) since this task is generating a report from supplied JSON data — no other skill applies to drafting this document.

# Hydrocortisone Acetate: From No Canadian Market Authorization to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate (DrugBank DB14539) currently has no recorded original indication and is not marketed in Canada in this dataset. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **1 clinical trial** and **2 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not currently marketed in Canada) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data and original indication information for hydrocortisone acetate are not available in this dataset. Based on known pharmacology, hydrocortisone acetate is a corticosteroid (glucocorticoid receptor agonist) with well-established topical and intralesional anti-inflammatory and immunosuppressive activity, and it is already used in dermatologic practice.

Alopecia areata is a T-cell–mediated autoimmune disease in which immune cells attack hair follicles within their normally immune-privileged niche, producing peribulbar inflammatory infiltration. Corticosteroids such as hydrocortisone suppress local T-cell activity and cytokine release, reducing this perifollicular inflammation — which is why topical/intralesional corticosteroids are already a standard or adjunct treatment option for alopecia areata in clinical dermatology.

Because the drug's anti-inflammatory mechanism directly addresses the immune-mediated pathology of alopecia areata, and because hydrocortisone has already been evaluated head-to-head against a higher-potency steroid (clobetasol) in this exact condition, the TxGNN prediction is mechanistically plausible even though hydrocortisone-acetate-specific efficacy data remain limited.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized controlled trial in children comparing Clobetasol Propionate 0.05% cream vs. Hydrocortisone 1% cream for alopecia areata; hydrocortisone served as the lower-potency active comparator, providing direct clinical data on topical steroid efficacy boundaries in this condition. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Case Series | Przeglad dermatologiczny | Reports treatment of severe alopecia areata using intralesional/subcutaneous injections of hydrocortisone acetate suspension. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | Review of topical corticosteroid therapy in skin disease; references hydrocortisone acetate's anti-inflammatory potency as a comparator benchmark for newer agents. |

## Canada Market Information

Hydrocortisone acetate currently has no recorded market authorization in Canada — no DINs or product licenses are on file in this dataset.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT directly compares hydrocortisone to a higher-potency corticosteroid in pediatric alopecia areata, and topical/intralesional corticosteroids are already an established treatment class for this condition — giving the prediction reasonable mechanistic and clinical grounding despite the limited volume of hydrocortisone-acetate-specific trial data.

**To proceed, the following is needed:**
- Health Canada product monograph warnings/contraindications (currently a Blocking data gap — required before any safety pre-screen can proceed)
- Mechanism of action documentation from DrugBank (currently a High-severity data gap)
- Confirmation of Canadian market authorization status, since the drug is currently listed as not marketed
- Additional hydrocortisone-acetate-specific trials or literature focused on efficacy in alopecia areata (existing evidence is largely a comparator trial and older case reports)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

