---
layout: default
title: Desogestrel
parent: Moderate Evidence (L3-L4)
nav_order: 262
evidence_level: L4
indication_count: 10
---

# Desogestrel
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Desogestrel: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a progestin used in oral contraceptives, both alone (75 µg progestin-only pill) and combined with ethinylestradiol.
The TxGNN model predicts it may be effective for **amenorrhea**, but this rests on only **2 loosely related clinical trials** and **16 publications**, none of which show desogestrel treating amenorrhea directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormonal contraception (inferred from the literature; the license records contain no indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, desogestrel is a progestin that suppresses ovulation and acts on the endometrium. Its efficacy in contraception is well established, and mechanistically it may influence menstrual cycle regulation.

The link to amenorrhea is weak and possibly reversed. Progestin-only use often *causes* amenorrhea rather than treating it. In combined pills, desogestrel may help regulate withdrawal bleeding. A therapeutic role in hypothalamic or athletic amenorrhea has not been established. The very high TxGNN score probably reflects a drug-disease association in the knowledge graph (amenorrhea as an effect of the drug) rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Hormonal and body-composition differences in young athletes with and without amenorrhea. Tests transdermal or oral estrogen versus none for bone density. Desogestrel is not shown as the studied drug, so this is not direct evidence. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | Contraceptive pill versus vaginal ring on hormonal and metabolic parameters in women with PCOS. Endpoints are not amenorrhea treatment, and desogestrel is not confirmed as an arm. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Systematic review (Cochrane) | Cochrane Database Syst Rev | 20 µg versus >20 µg estrogen combined pills: effectiveness and bleeding patterns. Contraception focus, not amenorrhea treatment. |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Update of the review above, with the same contraception focus. |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical study | J Reprod Med | Bone mineral density in young women with hypothalamic oligoamenorrhea on oral contraceptives with decreasing ethinylestradiol doses. |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical study | Georgian Med News | Management of central oligomenorrhea and amenorrhea in 159 infertile women, compared with conventional hormone therapy. Desogestrel's role is not specified. |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Cohort/clinical study | Gynecol Endocrinol | Drospirenone-only pill versus desogestrel 75 µg on bleeding profile. Desogestrel showed poor cycle control, and progestin-only pills are associated with irregular bleeding including amenorrhea. |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative clinical study | Br J Obstet Gynaecol | Two desogestrel pills (20 µg vs 30 µg ethinylestradiol) compared on reliability, cycle control and side effects. |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic study | Acta Obstet Gynecol Scand Suppl | Androgenicity of progestins, with focus on desogestrel alone and combined with ethinylestradiol. |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Clinical tolerability study | Am J Obstet Gynecol | Tolerability of desogestrel/ethinyl estradiol. Notes non-contraceptive benefits of oral contraceptives, such as reduced dysmenorrhea. |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstet Gynecol Surv | Overview of pills containing gestodene, norgestimate and desogestrel. |
| [2956054](https://pubmed.ncbi.nlm.nih.gov/2956054/) | 1987 | Clinical study | Contraception | Postponement of withdrawal bleeding using low-dose combined pills with an extended cycle. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2410257 | MIRVALA 28 |
| 2272903 | LINESSA 21 |
| 2257238 | LINESSA 28 |
| 2556561 | MILEY 28 |
| 2556553 | MILEY 21 |

Dosage form and approved indication text are not available in the license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study shows desogestrel treating amenorrhea. The two registered trials are indirect, and the literature mostly covers contraception, cycle control and tolerability. Progestin-only desogestrel commonly causes amenorrhea rather than treating it, so the high TxGNN score is likely a graph artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Direct clinical evidence of desogestrel in amenorrhea, such as hypothalamic or athletic amenorrhea
- Clarification of whether the effect comes from the combined-pill formulation (estrogen component) rather than desogestrel itself

For reference, the same evidence pack shows stronger support for **acne** (L3, with a completed Phase 4 trial and several clinical studies of desogestrel/ethinylestradiol pills). That effect is mostly attributed to the combined formulation, so it may be a better candidate to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

