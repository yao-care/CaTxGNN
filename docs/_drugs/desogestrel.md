---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: From Oral Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a third-generation synthetic progestogen widely used as a component of combined oral contraceptives and as a progestogen-only pill (75 mcg/day) for contraception.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **2 clinical trials** and **16 publications** currently supporting this direction.
However, the evidence is largely indirect — the drug is known to *induce* amenorrhea as a pharmacological side effect rather than directly treating the underlying condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada (widely known as oral contraceptive progestogen) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, desogestrel is a third-generation gonane progestogen and a prodrug; its active metabolite **etonogestrel** binds selectively to progesterone receptors with very low androgenic and estrogenic activity. It modulates the hypothalamic-pituitary-ovarian (HPO) axis primarily by suppressing the LH surge and inhibiting ovulation, while also exerting direct effects on the endometrium. These same HPO-suppressive properties underlie its potential connection to amenorrhea.

The relationship between desogestrel and amenorrhea is well-established clinically — but in an important paradox: the desogestrel-only pill (75 mcg/day) *induces* amenorrhea in approximately 20–30% of users through potent endometrial suppression, rather than resolving it. Theoretically, this HPO axis modulation could be redirected therapeutically — for example, in hyperandrogenic amenorrhea (where restoring hormonal balance could trigger cycle resumption), or when used alongside estrogen in hypothalamic amenorrhea to protect the endometrium. A 2001 study (PMID 11725730) directly evaluated low-dose OC formulations including desogestrel-containing pills for bone preservation in hypothalamic amenorrheic women, providing the most direct evidence link.

Overall, the TxGNN score of 99.96% most likely reflects strong graph-level co-occurrence between desogestrel and amenorrhea-related nodes in the knowledge graph (the drug causes amenorrhea; it is used clinically in populations with amenorrhea features such as PCOS and athletic menstrual suppression). A direct therapeutic application — treating pathological amenorrhea — would require a carefully framed clinical rationale and has no direct RCT support to date.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Evaluates estrogen therapy (transdermal vs. oral vs. none) in adolescent athletes with exercise-associated amenorrhea (athletic amenorrhea) to assess bone density outcomes; desogestrel not the study drug — indirect relevance through athletic amenorrhea population |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | 59-week comparison of oral combined contraceptive vs. hormonal vaginal ring on androgen, lipid, and metabolic parameters in PCOS women; amenorrhea not a primary endpoint; trial status unknown, limiting data reliability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Cochrane Systematic Review | Cochrane Database Syst Rev | 20 mcg vs. >20 mcg estrogen COC comparison; amenorrhea and bleeding patterns analysed across multiple desogestrel-containing formulations (Mercilon, Marvelon) |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Cochrane Systematic Review (Update) | Cochrane Database Syst Rev | Updated analysis; confirms low-estrogen desogestrel pills have different amenorrhea and unscheduled bleeding profiles vs. higher-dose formulations |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Clinical Study | Gynecol Endocrinol | Desogestrel 75 mcg vs. drospirenone 4 mg POP in women with cardiovascular risk factors; desogestrel showed poorer cycle control with significantly higher amenorrhea rates over 9 cycles, confirming its endometrial suppression profile |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Study | J Reprod Med | OC therapy (including desogestrel-containing formulations) in young hypothalamic oligoamenorrheic women; evaluates whether different EE doses protect against bone loss — most direct evaluation of OC use in an amenorrheic population |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstet Gynecol Scand Suppl | Androgenicity comparison of progestogens; study population included PCO women with amenorrhea features; desogestrel demonstrated favourable anti-androgenic and HPO-modulating profile |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative Clinical Study | Br J Obstet Gynaecol | Desogestrel 150 mcg with 20 mcg vs. 30 mcg EE head-to-head comparison; amenorrhea and breakthrough bleeding rates compared across dose groups |
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Implanon (etonogestrel implant, desogestrel's active metabolite) vs. Norplant over 2–4 years in 200 women; amenorrhea rates documented per 90-day reference periods, directly linking etonogestrel exposure to amenorrhea induction |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Clinical Tolerability Study | Am J Obstet Gynecol | Comprehensive tolerability profile of desogestrel/EE combination; non-contraceptive benefits including cycle regularity, dysmenorrhea reduction, and endometrial effects discussed |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Study | Georgian Med News | Pathogenetic management of central-genesis oligomenorrhea and amenorrhea in 159 infertile women; hormone therapy vs. standard approaches compared — provides context for hormonal treatment of amenorrhea |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Narrative Review | Obstet Gynecol Surv | Review of desogestrel, norgestimate, and gestodene; covers pharmacokinetics, HPO axis modulation, and clinical differentiation — relevant mechanistic background for amenorrhea prediction |

---

## Canada Market Information

Desogestrel is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are registered under the Health Canada drug product database. No approved indications are available through the Canadian licensing system.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence supporting desogestrel as a direct *treatment* for amenorrhea is at best L3 and predominantly indirect — desogestrel pharmacologically *induces* amenorrhea through HPO suppression rather than resolving its underlying pathology, and there are no direct RCTs evaluating it as a therapeutic agent for this indication. Additionally, with zero Health Canada DINs and no existing regulatory framework in Canada, proceeding requires establishing the drug's presence in the market before any repurposing effort can be structured.

**To proceed, the following is needed:**
- **Clarify the clinical question**: Distinguish between (a) *inducing controlled amenorrhea* for menorrhagia or endometriosis management, versus (b) *treating pathological amenorrhea* (e.g., functional hypothalamic amenorrhea or PCOS-associated amenorrhea) — these require entirely different development strategies
- **Obtain full MOA data** from DrugBank (DrugBank ID: DB00304) to complete mechanistic analysis and strengthen the repurposing rationale
- **Retrieve product monograph / prescribing information** (Health Canada or EMA) for complete safety assessment including key warnings, contraindications, and drug interactions
- **Verify Canadian regulatory status**: Confirm whether desogestrel products (e.g., Cerazette/Azalia as progestogen-only pill, or Marvelon/Mercilon as combined OC) have any pending or historical Health Canada submissions
- **Consider prioritising Rank 4 – Acne (Evidence Level L2)** for a stronger repurposing case: 1 completed Phase 4 RCT (n=201, NCT01466673) directly evaluates a desogestrel-containing formulation for acne vulgaris, supported by multiple clinical trials and over 20 publications with a clear anti-androgenic mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

