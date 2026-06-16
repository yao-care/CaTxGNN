---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clotrimazole: From Fungal Infections to Acne

## One-Sentence Summary

Clotrimazole is a broad-spectrum imidazole antifungal well-established for treating candidal and dermatophyte infections including tinea pedis, oropharyngeal candidiasis, and vulvovaginal candidiasis. The TxGNN model's highest-ranked prediction is **Acne (disease)** with a score of 99.86%, yet this direction is supported by only **1 suspended multi-component trial** and **no published literature**, yielding a **Hold** recommendation. Critically, the second-ranked prediction — **Vulvovaginitis** — carries far stronger support with **22 clinical trials** and **20 publications** at Evidence Level **L1**, warranting a **Proceed with Guardrails** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal/candidal infections (tinea pedis, oropharyngeal candidiasis, vulvovaginal candidiasis) |
| Predicted New Indication (Rank 1) | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs on file — likely data gap) |
| Number of DINs | 0 |
| Recommended Decision | Hold (Acne) / Proceed with Guardrails (Vulvovaginitis) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published literature (Crowley & Gallagher, *J Applied Microbiology*, 2014), Clotrimazole is a synthetic imidazole that inhibits cytochrome P450-dependent lanosterol 14α-demethylase, blocking ergosterol biosynthesis and disrupting fungal cell membrane integrity. This mechanism underpins its proven efficacy against *Candida albicans* and dermatophytes.

The mechanistic link to **acne** is biologically weak. Acne vulgaris is primarily driven by *Cutibacterium acnes* (a Gram-positive bacterium), excess sebum production, follicular hyperkeratinization, and inflammation — not fungal organisms. While *Malassezia* species (a yeast) cause *Malassezia folliculitis*, a condition that can mimic acne, this is a clinically distinct entity and not typical acne vulgaris. The high TxGNN score likely reflects shared knowledge-graph features — sebaceous glands, follicular units, skin microbiome signatures — rather than a direct pharmacological relationship.

**Key observation for the second-ranked prediction (Vulvovaginitis):** Clotrimazole's antifungal mechanism directly targets *Candida albicans*, the pathogen responsible for 70–90% of vulvovaginal candidiasis cases. The repurposing rationale in this Evidence Pack explicitly notes this represents Clotrimazole's **original indication** rather than a novel use. The Guardrails caveat stems from the fact that "vulvovaginitis" is a broader clinical category encompassing bacterial vaginosis and trichomoniasis, conditions where Clotrimazole has no antifungal efficacy.

---

## Clinical Trial Evidence — Acne (Rank 1 · L4 · Hold)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | **Suspended** | 80 | Evaluates triple combination (Beclomethasone 0.025% + Gentamicin 0.1% + Clotrimazole 1%) for contaminated dermatosis with bilateral symmetrical lesions; Clotrimazole is one of three components and not the primary agent; trial was suspended prior to completion — no efficacy conclusions possible |

Currently no dedicated standalone Clotrimazole trials for acne vulgaris are registered on ClinicalTrials.gov.

---

## Clinical Trial Evidence — Vulvovaginitis (Rank 2 · L1 · Proceed with Guardrails)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Completed | 150 | Head-to-head: Dequalinium chloride 10 mg vs **Clotrimazole 100 mg vaginal tablet** for VVC; direct efficacy, safety, and patient satisfaction comparison — highest direct relevance |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Completed | 1,524 | Large RCT in West Africa: single-dose Tinidazole+Fluconazole vs **Metronidazole+Clotrimazole** (3-day vaginal course) for vaginal discharge syndrome; Clotrimazole is a core component of the active treatment arm |
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Completed | 466 | Non-inferiority: **Clotrimazole ovule 500 mg** vs vaginal tablet 500 mg for vaginal candidiasis; demonstrates formulation flexibility |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Completed | 240 | **Clotrimazole vaginal tablet vs Fluconazole** for severe VVC; evaluates efficacy and safety in severe presentation |
| [NCT03562156](https://clinicaltrials.gov/study/NCT03562156) | Phase 3 | Completed | 438 | Oteseconazole vs placebo for recurrent VVC; Clotrimazole serves as standard-of-care reference, establishing benchmark efficacy for comparison |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | Completed | 1,033 | Post-marketing safety surveillance of **Empecid L Cream (Clotrimazole 1%)** under pharmacist guidance; real-world safety profile |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | Completed | 100 | Cumin seed extract vs **Clotrimazole** vaginal suppositories for candidal VVC; Clotrimazole serves as gold-standard active comparator |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Completed | 140 | **Clotrimazole vaginal tablet** ± oral *Lactobacillus* for preventing RVVC recurrence; evaluates adjunct microbiome strategy |
| [NCT02860845](https://clinicaltrials.gov/study/NCT02860845) | Phase 4 | Completed | 48 | Boric acid + probiotics vs standard antifungal for VVC/bacterial vaginosis; provides management context for refractory cases |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | Recruiting | 264 | **Clotrimazole + Lactulose** vs Clotrimazole monotherapy for candidal vulvovaginitis; superiority trial — ongoing |

---

## Literature Evidence — Vulvovaginitis (Rank 2 · L1)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | *Complementary Therapies in Medicine* | **Clotrimazole** vaginal cream vs *Prangos ferulacea* for VVC; comparative clinical and mycological cure rates |
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | RCT (triple-blind) | *Scientific Reports* | Mycozin vs **Clotrimazole 1% cream** for vaginal candidiasis (n=126); non-inferiority design; confirms Clotrimazole as benchmark standard |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | *Mycoses* | Probiotics + lactoferrin as maintenance therapy for recurrent VVC; **Clotrimazole** as backbone treatment in trial context |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | Clinical Trial | *Obstetrics & Gynecology* | **Clotrimazole 500 mg** weekly for recurrent VVC (n=42): 90.4% clinical remission, 83% mycologic cure; monthly prophylaxis evaluated prospectively |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | *American Journal of Obstetrics & Gynecology* | Single-dose **Clotrimazole 500 mg** vs 6-day 100 mg course for candidal VVC (n=199); both regimens comparable in cure rates |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | *Journal of Applied Microbiology* | Comprehensive review: **Clotrimazole** as pharmaceutical — mechanism, VVC/tinea indications, resistance patterns, and emerging uses |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | Observational | *Journal of Applied Microbiology* | **Clotrimazole**-induced shifts in vaginal bacteriome and lipid metabolism post-treatment; mechanistic insights into microbiome recovery |
| [31106557](https://pubmed.ncbi.nlm.nih.gov/31106557/) | 2019 | Review | *Minerva Ginecologica* | Combined fluconazole (systemic) + **metronidazole + clotrimazole** (topical) strategy for RVVC long-term prophylaxis |
| [1877264](https://pubmed.ncbi.nlm.nih.gov/1877264/) | 1991 | Clinical Study | *DICP: Annals of Pharmacotherapy* | Fluconazole vs **Clotrimazole** vaginal tablets for Candida vaginitis (n=90 evaluable/arm); comparable asymptomatic rates at 7–10 days |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | *Journal of Women's Health* | Boric acid evidence review for RVVC; positions **Clotrimazole** as the established first-line azole against which alternatives are measured |

---

## Canada Market Information

No Drug Identification Numbers (DINs) are recorded in the current dataset, and market status is listed as **Not marketed**.

> **Important data gap:** Clotrimazole-containing products — most notably Canesten® (Bayer Consumer Health) — are widely available in Canada as both prescription and OTC products. The 0-DIN result almost certainly reflects a collection gap rather than true absence from the Canadian market. A direct search of the Health Canada Drug Product Database (DPD) at [health-products.canada.ca](https://health-products.canada.ca/dpd-bdpp/) is required before making any regulatory decisions.

---

## Safety Considerations

Please refer to the package insert for safety information. Full key warnings, contraindications, and drug interaction data were not available in this Evidence Pack and must be retrieved from the Health Canada product monograph or the TFDA package insert PDF.

---

## Conclusion and Next Steps

**Decision: Hold (Acne · Rank 1) | Proceed with Guardrails (Vulvovaginitis · Rank 2)**

**Rationale:**

- **Acne (Rank 1 TxGNN, L4):** Despite the highest prediction score (99.86%), the mechanistic basis for Clotrimazole in acne vulgaris is biologically weak. *Cutibacterium acnes* is not a fungal target. The only supporting trial was suspended, enrolled 80 patients, and evaluated Clotrimazole as one of three combination ingredients. No standalone evidence exists. The high score likely reflects knowledge-graph proximity between fungal folliculitis and acne rather than pharmacological relevance.

- **Vulvovaginitis (Rank 2 TxGNN, L1):** Multiple completed Phase 3 and Phase 4 RCTs, large post-marketing datasets, and a mechanistically direct link (Clotrimazole targets *Candida*, the pathogen in 70–90% of VVC cases) make this an immediately actionable candidate. The Guardrails caveat: the "vulvovaginitis" ICD category includes bacterial vaginosis and trichomoniasis where Clotrimazole is ineffective — product labeling must specify the candidal subtype. Notably, the repurposing rationale identifies this as Clotrimazole's **core indication**, meaning any Canadian registration effort is a label expansion or market entry, not a novel repurposing.

- **Postmenopausal atrophic vaginitis (Rank 3 TxGNN, L4):** Weak mechanistic link and no direct supporting evidence. Only one indirectly related trial was retrieved. This remains a research question pending primary driver characterization (estrogen deficiency vs. secondary Candida colonization).

**To proceed, the following is needed:**

- Verify Canada market status via Health Canada DPD — resolve the 0-DIN data gap before any regulatory strategy is defined
- Retrieve the Health Canada product monograph (or TFDA package insert PDF) for key warnings, contraindications, and drug interactions — currently a blocking data gap
- Retrieve MOA data from DrugBank API (DB00257) to complete mechanistic sections for all three predicted indications
- For **acne**: determine whether the intended clinical question is *Malassezia folliculitis* (stronger mechanistic case, potentially actionable) vs. acne vulgaris (weak case, Hold maintained) before committing further resources
- For **vulvovaginitis**: if Canesten® is already registered in Canada, confirm whether the label explicitly covers *candidal* vulvovaginitis and evaluate whether a new DIN or label variation is needed; if not registered, assess the regulatory pathway for a vaginal antifungal product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

