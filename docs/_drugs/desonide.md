---
layout: default
title: Desonide
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: From Inflammatory Dermatoses to Polyp of Vocal Cord

## One-Sentence Summary

Desonide is a low-potency (Class VI) topical corticosteroid originally used to treat mild-to-moderate inflammatory skin conditions such as atopic dermatitis and eczema.
The TxGNN model predicts it may be effective for **Polyp of Vocal Cord**, with the mechanistic premise that corticosteroids suppress the inflammatory component (Reinke's edema) underlying some vocal cord polyps.
However, there are currently **0 clinical trials** and **0 publications** directly supporting this specific application, making this a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory skin conditions (atopic dermatitis, contact dermatitis, eczema) |
| Predicted New Indication | Polyp of Vocal Cord |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Desonide is a synthetic glucocorticoid receptor (GR) agonist that suppresses inflammatory mediators — including cytokines, prostaglandins, and leukotrienes — through transcriptional regulation. As a Class VI (low-potency) topical corticosteroid, it is designed primarily for application to sensitive skin areas and has an established safety profile in dermatological use.

Vocal cord polyps — particularly those associated with Reinke's edema — have a recognized inflammatory component, and intralesional corticosteroid injections (using agents such as triamcinolone or dexamethasone) are already part of clinical practice as an adjunct or alternative to surgical intervention. The conceptual bridge is therefore the anti-inflammatory mechanism: reducing edema, eosinophilic infiltration, and vascular permeability in the laryngeal mucosa.

The critical weakness of this prediction is that Desonide has **no established topical formulation suited for laryngeal administration**, and the evidence base for Desonide specifically in vocal cord polyps is entirely absent. The mechanistic plausibility is rated moderate at best. The TxGNN model likely captures the class-level relationship between corticosteroids and polyp inflammation rather than predicting Desonide as uniquely suitable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Desonide has no approved products registered in Canada (0 DINs). Accordingly, there is no Health Canada–approved indication or product labelling available through this dataset.

---

## All Predicted Indications — Mechanistic Summary

Because the top-ranked indication is a model-only prediction with no clinical data, the following table provides context across all 10 predicted indications to assist prioritisation decisions:

| Rank | Indication | TxGNN Score | Mechanistic Plausibility | Key Concern |
|------|-----------|------------|--------------------------|-------------|
| 1 | Polyp of vocal cord | 99.91% | Moderate — inflammatory (Reinke's edema) component | No Desonide-specific delivery route established |
| 2 | Polyp of middle ear | 99.91% | Moderate — corticosteroid ear drops (dexamethasone) used in chronic otitis | Tympanic membrane perforation risk; no otic formulation for Desonide |
| 3 | Polyp of external auditory canal | 99.91% | Low-to-moderate — topical steroids used in otitis externa | No direct polyp studies; external canal access is easier |
| 4 | **Polyp of frontal sinus** | **99.91%** | **Highest in group** — nasal corticosteroids are standard of care for sinonasal polyps | Desonide potency (Class VI) far below clinical nasal steroids; no direct frontal sinus data |
| 5 | Polyp of ureter | 99.90% | Very low — fibroepithelial polyps are not inflammation-driven | No mechanistic basis; systemic use of a topical-only drug poses major safety concerns |
| 6 | Polyp of vulva | 99.90% | Low — fibroepithelial; Desonide used in vulvar inflammatory skin disease only | No evidence of polyp size reduction |
| 7 | Fibroepithelial polyp | 99.90% | Near zero — benign fibrous proliferation, not inflammatory | No literature support |
| 8 | **Neoplastic polyp** | **99.90%** | ⚠️ **Contraindication candidate** — immunosuppression may promote cancer progression | Pre-malignant lesions; corticosteroids potentially harmful |
| 9 | Epulis | 99.90% | Low-to-moderate — pyogenic granuloma subtype has inflammatory component | Case reports only for corticosteroid injection; no Desonide data |
| 10 | Uterine polyp | 99.90% | Low — oestrogen-driven proliferation; corticosteroids have no anti-oestrogenic effect | HPA axis interference; intrauterine delivery not established |

> **Note on Rank 4 (Polyp of Frontal Sinus):** This indication has the strongest mechanistic rationale within this set. Intranasal corticosteroids are guideline-endorsed for sinonasal polyps. While Desonide is underpowered relative to fluticasone or mometasone, this subgroup warrants closer review if the investigation is expanded.
>
> **Note on Rank 8 (Neoplastic Polyp):** This should be treated as a potential contraindication rather than a repurposing opportunity.

---

## Safety Considerations

Please refer to the package insert for safety information. Full warning and contraindication data was not available in this Evidence Pack. Key areas to review before any further evaluation:

- **Systemic absorption risk**: Even topical corticosteroids carry HPA axis suppression risk with prolonged use, particularly on occluded or mucosal surfaces.
- **Site-specific formulation safety**: Any non-dermatological application (laryngeal, otic, sinonasal, or intrauterine) requires dedicated formulation and safety assessment.
- **Drug interactions**: No DDI data was identified in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are at Evidence Level L5 — supported only by model prediction with zero clinical trials and zero publications. The mechanistic plausibility ranges from near-zero (uterine polyp, neoplastic polyp, fibroepithelial polyp) to moderate (vocal cord polyp, frontal sinus polyp), but no indication has sufficient evidence to proceed without further investigation. Additionally, Desonide is not marketed in Canada, removing any regulatory shortcut through a label-extension pathway.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full Desonide pharmacology from DrugBank or published sources to formally document GR agonism and potency classification
- **Indication triage**: Prioritise Rank 4 (polyp of frontal sinus) for deeper review, as class-level evidence for nasal corticosteroids in sinonasal polyps is substantial; determine whether Desonide's specific potency and formulation could be adapted
- **Formulation feasibility assessment**: Evaluate whether a nasal or laryngeal-compatible Desonide formulation exists or could be developed
- **Safety data retrieval**: Obtain the full TFDA/Health Canada product monograph or package insert to complete contraindication and warning review (currently Data Gap — Blocking severity)
- **Exclusion of Rank 8**: Formally document Neoplastic Polyp as a contraindicated direction, not a repurposing candidate
- **Broader literature search**: Expand PubMed search to corticosteroid class (not Desonide-specific) for each indication to establish class-level evidence before dismissing TxGNN predictions entirely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

