---
layout: default
title: Alitretinoin
parent: Model Prediction Only (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alitretinoin: predicted new indication Amenorrhea (evidence level L5). Approved use: Severe chronic hand eczema refractory to potent topical corticosteroi…"
monitor_inn: "Alitretinoin"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "aortic malformation", "postmenopausal osteoporosis", "autosomal dominant neovascular inflammatory vitreoretinopathy", "breast fibrocystic disease", "benign mammary dysplasia", "Worth syndrome"]
---

# Alitretinoin
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

# Alitretinoin: From Chronic Hand Eczema to Amenorrhea

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a retinoid that binds retinoid receptors (RAR and RXR). It is used for severe chronic hand eczema that does not respond to potent topical corticosteroids, and for Kaposi sarcoma.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no publications** currently support this prediction.
This is a model-only prediction, and no mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe chronic hand eczema refractory to potent topical corticosteroids; Kaposi sarcoma (the Canadian licence records contain no indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on the pharmacology data compiled for this report, alitretinoin is a pan-agonist of retinoid receptors. It acts on RARα, RARβ and RARγ, as well as RXRα, RXRβ and RXRγ. It is also linked to vitamin K epoxide reductase (VKORC1) in the data.

Amenorrhea is a hormonal or structural reproductive disorder, and alitretinoin has no established role in treating it. The very high TxGNN score comes from graph-based inference only. Retinoids are also strongly teratogenic, so use in women of reproductive age is a serious safety concern.

**In summary, this prediction is not mechanistically supported by the available data.**

The other top-ranked predictions are also weak:
- **Acne** (score 99.92%, evidence level L4): a plausible class-level rationale, since retinoids act on keratinocyte differentiation and sebaceous activity. Only two general dermatology reviews support it, and established alternatives exist.
- **Atypical coarctation of aorta, aortic malformation, pregnancy-associated osteoporosis, postmenopausal osteoporosis, autosomal dominant neovascular inflammatory vitreoretinopathy, breast fibrocystic disease, benign mammary dysplasia and Worth syndrome**: all L5, with no clinical evidence. For several (pregnancy-associated and postmenopausal osteoporosis, congenital vascular defects), retinoid effects on bone or development argue against benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for amenorrhea (nor for any of the other top 10 predicted indications).

---

## Literature Evidence

Currently no related literature available for amenorrhea.

For the second-ranked prediction (acne), two general reviews were retrieved. They provide indirect, class-level support only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clinics in Dermatology | Overview of vitamin A and retinoids in dermatology; lists alitretinoin among oral retinoids |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacology and Applied Skin Physiology | Retinoids act on nuclear retinoid receptors with relatively selective targeting of skin structures; discusses future dermatological indications |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02477432 | HANZEMA | Not stated | Not stated |
| 02477440 | HANZEMA | Not stated | Not stated |

---

## Cytotoxicity

Alitretinoin is used for Kaposi sarcoma, but it is a retinoid receptor agonist rather than a conventional cytotoxic drug. The data compiled for this report do not classify it as a cytotoxic antineoplastic, so a full cytotoxicity profile is not provided. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Teratogenicity**: Retinoids are strongly teratogenic. Alitretinoin is contraindicated in pregnancy, and use in women of reproductive age is a serious concern, particularly relevant to an indication such as amenorrhea.
- **Knowledge-graph contraindications** (from the TxGNN knowledge graph, not label text): mycosis fungoides and variants, primary cutaneous T-cell lymphoma, folliculotropic mycosis fungoides, localized pagetoid reticulosis, and granulomatous slack skin disease.
- **Pharmacological interactions**: The data list 7 pharmacological targets or interactions rather than drug-drug interactions with graded severity. They are retinoic acid receptors α, β and γ, retinoid X receptors α, β and γ, and VKORC1. The VKORC1 link may be relevant when co-prescribing vitamin K antagonists such as warfarin, but this needs verification.
- **Bone effects**: Retinoid excess is associated with increased bone resorption and fracture risk.

The Health Canada package insert warnings were not available for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction rests on a graph-based score alone (L5), with no trials, no literature and no identifiable mechanistic link. Teratogenicity is a substantial safety obstacle for women of reproductive age. Among the top 10 predictions, only acne has indirect class-level support, and established retinoid alternatives already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Indication text, dosage forms and manufacturer details for the two HANZEMA DINs
- Any preclinical or clinical evidence for amenorrhea; if none exists, consider deprioritising this candidate
- If the team wants to pursue another candidate, a focused literature search on alitretinoin in acne, plus a pregnancy-prevention risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

