---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract Surgery Ocular Inflammation to Eye Disease

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID prodrug whose well-documented use is controlling inflammation, pain, and macular edema risk after cataract surgery and other intraocular procedures. The TxGNN model flags it for the broad category **Eye Disease**, a prediction supported by **41 clinical trials** and **20 publications** — though most of this evidence documents nepafenac's already-established ophthalmic uses rather than a genuinely novel indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Canadian regulatory data — Nepafenac has no approved Canadian license in this dataset. Trial evidence indicates its established use is prevention/treatment of ocular inflammation and pain associated with cataract surgery. |
| Predicted New Indication | Eye Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not on file for this drug record. However, the evidence pack's own repurposing rationale describes the mechanism: nepafenac is a prodrug that is converted by ocular tissue esterases into its active metabolite, amfenac, which inhibits both COX-1 and COX-2, blocking prostaglandin synthesis. This directly targets the inflammatory and edema-generating pathways in intraocular tissue.

"Eye Disease" is a broad TxGNN disease-category node rather than a single defined condition. The extensive trial evidence in this pack shows nepafenac's use is concentrated in prevention/treatment of inflammation and cystoid macular edema after cataract surgery, with additional exploration in diabetic macular edema, uveitic macular edema, and post-laser-iridotomy inflammation. Because the predicted node aggregates all of "eye disease," the very high score largely reflects re-discovery of nepafenac's already-established ophthalmic uses rather than identification of a novel disease target.

Mechanistically, COX inhibition is broadly applicable across many prostaglandin-mediated ocular inflammatory conditions, which explains why trial support is so extensive and consistent. The practical implication is that this "new indication" should be read as confirmation of known efficacy across a disease category, not as a genuinely new repurposing hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Largest trial in the set; assessed safety/efficacy of nepafenac 0.3% for prevention and treatment of post-cataract-surgery inflammation and pain. |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Compared nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of post-cataract ocular inflammation and pain. |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Randomized, vehicle-controlled trial in diabetic patients showing superiority of nepafenac 0.3% once daily post-cataract surgery. (Relevance grade A) |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Companion vehicle-controlled trial confirming nepafenac 0.3% clinical outcome benefits in diabetic subjects after cataract surgery. |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Prospective, randomized, double-masked, placebo-controlled study of adjunctive nepafenac 0.3% for pseudophakic cystoid macular edema prevention. |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Multicenter bioequivalence study of generic nepafenac 0.3% vs Ilevro for pain/inflammation after cataract surgery. |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Placebo-controlled trial in Chinese subjects confirming nepafenac 0.1% superiority for post-cataract inflammation/pain. |
| [NCT00332774](https://clinicaltrials.gov/study/NCT00332774) | Phase 3 | Completed | 149 | Safety comparison of Nevanac 0.1% vs Acular LS vs vehicle after cataract surgery. (Relevance grade A) |
| [NCT00801905](https://clinicaltrials.gov/study/NCT00801905) | Phase 2 | Terminated | 50 | Evaluated nepafenac for preventing/treating macular thickening after pan-retinal photocoagulation in diabetic retinopathy; terminated, limiting evidence strength. (Relevance grade B) |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Compared macular volume with 3-month topical nepafenac vs placebo after epiretinal membrane surgery. (Relevance grade B) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review | European Journal of Ophthalmology | Meta-analysis of RCTs on nepafenac's effect on foveal thickness, macular volume, and visual outcome after cataract surgery when added to topical steroids. |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT (comparative) | Korean Journal of Ophthalmology | Compared 0.1% nepafenac vs 1% prednisolone acetate for postoperative inflammation control after micro-incisional cataract surgery. |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT (comparative) | Ophthalmology. Glaucoma | Prospective randomized trial comparing 0.1% nepafenac vs 1% prednisolone acetate for inflammation control after laser peripheral iridotomy. |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmology. Glaucoma | Randomized controlled trial of 0.1% nepafenac vs 0.09% bromfenac for inflammation after laser peripheral iridotomy. |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | RCT | American Journal of Ophthalmology | Randomized prospective study of nepafenac 0.1% eye drops' effect on intraocular pressure in cataract eyes. |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | Comparative study | Journal of Cataract and Refractive Surgery | Compared prophylactic ketorolac vs nepafenac vs placebo for macular volume and quality of life after phacoemulsification. |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic agents and therapeutic medications for non-infectious corneal injury, including topical NSAIDs such as nepafenac. |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Comparative clinical study | Acta Ophthalmologica | Compared clinical efficacy and tolerability of nepafenac vs preservative-free diclofenac for postoperative cataract management. |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | Comparative study | International Journal of Ophthalmology | Compared efficacy/safety of bromfenac, nepafenac, and diclofenac for cystoid macular edema prevention after phacoemulsification. |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK/Distribution study | Experimental Eye Research | Characterized distribution of topical ocular nepafenac and its active metabolite amfenac to the posterior segment of the eye. |

## Canada Market Information

Nepafenac currently holds **no active Health Canada Drug Identification Numbers (DINs)** in this dataset (`total_licenses = 0`; `market_status = 未上市 / Not Marketed`). No product-level licensing table can be generated until Canadian regulatory filing data becomes available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, supported by multiple completed Phase 3 (and large Phase 2) RCTs, and the COX-inhibition mechanism plausibly extends across the "eye disease" category. However, this category is broad enough that the evidence largely reconfirms nepafenac's already-known ophthalmic uses rather than establishing a novel indication, and the drug is currently unmarketed in Canada with no formal safety label or MOA record on file.

**To proceed, the following is needed:**
- TFDA/Health Canada product label — warnings, contraindications, and precautions (currently blocking, per data gap DG001)
- Formal mechanism-of-action documentation from DrugBank (data gap DG002)
- Disambiguation of the "Eye Disease" TxGNN node into a specific, clinically actionable indication rather than a broad category
- Canadian regulatory/market status update if a filing is pursued, since no DINs currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

