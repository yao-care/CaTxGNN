---
layout: default
title: Beta Carotene
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Beta Carotene
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

# Beta Carotene: From Nutritional Supplement to Acne

## One-Sentence Summary

Beta carotene is a provitamin A carotenoid found naturally in plant-based foods, widely used as a dietary antioxidant supplement with no currently registered therapeutic indications in Canada.
The TxGNN model predicts it may be effective for **Acne**, with **0 clinical trials** and **7 publications** currently supporting this direction.
Given the indirect mechanistic link and predominantly observational evidence, confidence in this prediction remains preliminary.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record (provitamin A nutritional supplement) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, beta carotene is a provitamin A carotenoid that serves as a dietary precursor to retinol (vitamin A). Its biological relevance to acne stems from two theoretical pathways: (1) conversion to retinol, which can be further metabolized to retinoic acid — a signalling molecule known to regulate keratinocyte proliferation and sebaceous gland activity; and (2) direct antioxidant activity, which may attenuate the local oxidative stress implicated in the pathogenesis of acne vulgaris.

A critical mechanistic limitation must be acknowledged upfront. The conversion efficiency of beta carotene to active retinoic acid is estimated at approximately 1:12, far less potent than direct retinoids such as isotretinoin (13-cis-retinoic acid), which acts directly on retinoic acid receptors to suppress sebum production and normalize follicular keratinization. This fundamental gap means that beta carotene cannot be considered a functional equivalent of therapeutic retinoids for acne treatment.

Supporting a cautious biological plausibility, observational studies (PMID 20049267; PMID 22517509) confirm that oxidant/antioxidant imbalance plays a measurable role in acne vulgaris, and that antioxidant vitamin levels including beta carotene are altered in acne patients and during retinoid therapy. This is consistent with a role for antioxidant supplementation in the disease biology — but falls well short of demonstrating therapeutic efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20049267](https://pubmed.ncbi.nlm.nih.gov/20049267/) | 2009 | Cross-sectional | Indian Journal of Dermatology | Evaluated oxidant/antioxidant status in obese adolescent females with acne vulgaris; found measurable alterations in antioxidant levels — including beta carotene — in acne patients, supporting a role for oxidative imbalance in disease pathogenesis |
| [22517509](https://pubmed.ncbi.nlm.nih.gov/22517509/) | 2012 | Clinical Observational | Cell Biochemistry and Function | Investigated oxidative toxicity induced by isotretinoin (a direct retinoic acid analogue) in acne patients; antioxidant vitamins including beta carotene were measured before and after treatment, highlighting the retinoid–antioxidant axis in acne biology |
| [7618499](https://pubmed.ncbi.nlm.nih.gov/7618499/) | 1995 | Narrative Review | Journal of the American Board of Family Practice | Broad review of vitamins used as therapeutic modalities in the 1990s, including dermatological applications of vitamin A precursors such as beta carotene |
| [2073211](https://pubmed.ncbi.nlm.nih.gov/2073211/) | 1990 | Case Series | Australasian Journal of Dermatology | Documented elevated beta carotene levels in patients with anorexia nervosa; a subset unexpectedly developed acne, suggesting a potentially complex relationship between elevated carotenoid levels and acne presentation |
| [4230169](https://pubmed.ncbi.nlm.nih.gov/4230169/) | 1967 | Cross-sectional | Dermatologische Wochenschrift | Compared serum vitamin A and beta carotene levels between individuals with and without skin diseases; early observational data on carotenoid status in dermatological conditions |
| [39459015](https://pubmed.ncbi.nlm.nih.gov/39459015/) | 2024 | In vitro / Phytochemistry | Pharmaceuticals (Basel) | Investigated ylang-ylang essential oil for dermatological applications including acne; beta carotene cited as one of several antioxidant constituents relevant to skin health |
| [23625436](https://pubmed.ncbi.nlm.nih.gov/23625436/) | 2013 | In vitro / Phytochemistry | Pakistan Journal of Pharmaceutical Sciences | Examined Helichrysum oligocephalum for acne and related conditions; antioxidant and antibacterial activities attributed in part to carotenoid-class compounds |

---

## Canada Market Information

Beta carotene (DB06755) currently has **no Drug Identification Numbers (DINs)** issued in Canada. The drug is not marketed in Canada under any product authorization, and no approved indications, dosage forms, or product licences are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** As beta carotene is not currently approved or marketed in Canada (0 DINs), no Canadian product monograph is available. Key safety signals that should be proactively investigated before any clinical development include: potential pro-oxidant effects at high supplementation doses; carotenodermia (reversible skin yellowing) at sustained high intake; and — most critically — the significantly increased risk of lung cancer in smokers documented in both the ATBC trial and the CARET trial with high-dose beta carotene supplementation. Any future development plan must clearly define the target population and exclude high-risk groups.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigned a very high prediction score (99.999%), but supporting evidence for the acne indication reaches only Level L4 — comprising observational and in vitro studies with indirect relevance, and no registered clinical trials. The biological link through provitamin A conversion is plausible in principle but functionally weaker than established retinoid therapies, and at least one case series raises the counterintuitive possibility that elevated beta carotene levels may associate with acne onset rather than prevention.

**To proceed, the following is needed:**
- Retrieve detailed mechanism of action data from DrugBank (unresolved data gap DG002)
- Conduct at least one controlled pilot clinical study evaluating beta carotene supplementation in an acne patient population with standardized outcome measures (e.g., lesion count, GAGS score)
- Clarify the effective dose range required for meaningful retinol conversion in the target population, and benchmark against dietary intake levels
- Conduct a full safety review with explicit exclusion criteria for smokers and populations at risk for hypervitaminosis A
- Determine the regulatory pathway: would this be pursued as a nutraceutical/natural health product or as a pharmaceutical drug in Canada?

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

