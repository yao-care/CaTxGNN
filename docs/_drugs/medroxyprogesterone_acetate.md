---
layout: default
title: Medroxyprogesterone Acetate
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Progestin Therapy to Amenorrhea

## One-Sentence Summary

Medroxyprogesterone acetate (MPA) is a synthetic progestin sold in Canada under 8 licences. The data supplied does not list its original approved indication.
The TxGNN model predicts it may be effective for **amenorrhea**, with **10 clinical trials** and **20 publications** retrieved. Most of these study amenorrhea as an outcome or side effect of MPA rather than as the disease being treated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (the source pack assigned L2, but no completed RCT directly tests MPA for amenorrhea) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Based on known pharmacology, MPA is a synthetic progestin. It converts estrogen-primed endometrium to a secretory state, and stopping it produces a withdrawal bleed. This fits the clinical logic of a progestin challenge in amenorrhea, and of protecting the endometrium during estrogen therapy.

MPA has a widely known labeled use in secondary amenorrhea. The prediction may therefore reflect an existing on-label use rather than true repurposing. This should be checked against the Canadian product monograph before it is treated as a new signal.

The retrieved evidence supports the biology but not a clear efficacy claim. The one trial that measured amenorrhea directly (MPA after endometrial ablation) was stopped early. The other studies deal with contraception or hormone therapy, where amenorrhea is a side effect.

Of the other nine predicted indications, endometriosis variants and benign breast conditions have a plausible progestin rationale but little or no direct evidence. Renal hypoplasia looks like a knowledge-graph artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of MPA after endometrial ablation, with endometrial amenorrhea rate as the outcome. It is the most direct test of amenorrhea induction with MPA, but it is a different clinical context and underpowered after early termination. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Cardiovascular risk markers in young women with functional hypothalamic amenorrhea (low estrogen). MPA's role cannot be confirmed. |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Whether progestin-induced withdrawal bleeding is needed before clomiphene ovulation induction in oligo- or amenorrheic women. The progestin used is not confirmed to be MPA. |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1886 | Bazedoxifene/conjugated estrogens for endometrial protection and osteoporosis prevention in postmenopausal women. Not an amenorrhea study. |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Timing of postpartum depot MPA and its effect on breastfeeding continuation. Contraceptive setting. |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | Recruiting | 120 | Relugolix versus placebo for heavy menstrual bleeding with uterine fibroids. The link to MPA is unverified. |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Tualang honey versus hormone replacement therapy (HRT) on safety profiles in postmenopausal women. Not an amenorrhea indication. |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | Completed | 108 | HRT effect on disease activity, menopausal symptoms and bone density in women with lupus. Indirect relevance only. |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | N/A | Not yet recruiting | 276 | Herbal formula for premature ovarian insufficiency. Little relevance to MPA. |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | Withdrawn | 0 | Estradiol and fear extinction in anorexia nervosa. No data. |

---

## Literature Evidence

Summaries for papers without abstracts are based on titles only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | RCT | Contraception | 100 women with at least 6 months of DMPA-induced amenorrhea were randomized to switch to Cyclofem or stay on DMPA. At 6 months, 82% of Cyclofem users had bleeding versus 10% of DMPA users. This confirms that DMPA induces amenorrhea. |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PloS one | WHICH trial comparing DMPA-IM and NET-EN injectables on estradiol levels, menstrual effects and psychological measures relevant to HIV risk. |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | Comparative clinical study | Acta Obstet Gynecol Scand | Compared endometrial histology and hormone levels in 11 women with DMPA-induced amenorrhea versus 12 women with secondary amenorrhea. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Review | Cochrane Database Syst Rev | Combination injectable contraceptives are highly effective. Bleeding-pattern changes may limit acceptability. |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception should start early because ovulation return is unpredictable, regardless of postpartum amenorrhea duration. |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counseling framework and side-effect management for women using DMPA. |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | Review | Obstet Gynecol Annu | Review of polycystic ovarian disease (title only). |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Drugs that can cause infertility through effects on the hypothalamic-pituitary-gonadal axis or direct gonadal toxicity. |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monogr | Carcinogenic-risk evaluation of medroxyprogesterone acetate. |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | Nursing-oriented overview of Depo-Provera (title only). |

---

## Canada Market Information

Dosage form and approved-indication text are not provided in the licence records.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2267640 | AA-MEDROXY | Not listed | Not listed |
| 2244726 | AA-MEDROXY | Not listed | Not listed |
| 2277298 | AA-MEDROXY | Not listed | Not listed |
| 2244727 | AA-MEDROXY | Not listed | Not listed |
| 2221284 | TEVA-MEDROXYPROGESTERONE | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

Evidence from the predicted indications also raises a concern. Hormone therapy regimens containing MPA have been associated with increased breast density and epithelial proliferation. This matters for any breast-related use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The progestin mechanism fits amenorrhea management, and the drug is already marketed in Canada. However, the trials retrieved mostly treat amenorrhea as an outcome or side effect. The only trial that measured it directly was terminated early. This may also be an existing on-label use rather than a true repurposing signal.

**To proceed, the following is needed:**
- Compare the prediction with the Canadian product monograph to determine whether amenorrhea is already a labeled indication.
- Obtain Health Canada package insert warnings and contraindications, which are needed for safety screening.
- Obtain mechanism-of-action data from DrugBank.
- Retrieve the full records of the trials with truncated titles (NCT03018366, NCT00808132, NCT06671548, NCT03309176) to confirm whether MPA was used.
- Review the literature relevance, which is still pending for all retrieved papers.
- Confirm the licence details for the 8 DINs, including dosage forms, routes and approved indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

