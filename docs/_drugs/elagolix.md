---
layout: default
title: Elagolix
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 1
---

# Elagolix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Elagolix: From Endometriosis-Associated Pain to Amenorrhea

## One-Sentence Summary

Elagolix is an oral GnRH receptor antagonist. The Canadian licence records provided contain no indication text, so its original use is taken from general knowledge and trial titles (endometriosis-associated pain). The TxGNN model predicts it may be effective for **amenorrhea**, but the **3 clinical trials** and **4 publications** found study heavy menstrual bleeding in uterine fibroids and endometriosis, not amenorrhea itself, so the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 (indirect evidence only; no study targets amenorrhea as the indication) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Based on general pharmacology, elagolix blocks GnRH receptors in the pituitary. This lowers LH and FSH and, in turn, ovarian estradiol and progesterone. With less hormonal stimulation, the endometrium proliferates less, and menstrual bleeding is reduced or stops.

Amenorrhea is therefore a plausible pharmacodynamic effect of the drug rather than a separate disease target. The high TxGNN score (99.75%) most likely reflects this hormonal-suppression link. In the trials below, bleeding reduction is the main outcome and amenorrhea is at most a secondary outcome. The prediction is biologically reasonable but has not been tested as a treatment goal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2b | Completed | 571 | Randomized, double-blind, placebo-controlled study of elagolix alone or with add-back therapy for heavy menstrual bleeding in premenopausal women with uterine fibroids. Indirect support for bleeding suppression. |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2a | Completed | 271 | Proof-of-concept study of elagolix vs placebo for reducing uterine bleeding, fibroid volume and uterine volume. Menstrual suppression is relevant, but amenorrhea is not the target. |
| [NCT00797225](https://clinicaltrials.gov/study/NCT00797225) | Phase 2 | Completed | 174 | Placebo- and leuprorelin-controlled study of elagolix (NBI-56418) in endometriosis over 3 months, followed by 3 months of elagolix. Low relevance to amenorrhea. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37769311](https://pubmed.ncbi.nlm.nih.gov/37769311/) | 2023 | RCT (design to be verified) | Obstet Gynecol | Safety and efficacy of elagolix 150 mg once daily as monotherapy for heavy menstrual bleeding associated with uterine leiomyomas. |
| [32702363](https://pubmed.ncbi.nlm.nih.gov/32702363/) | 2021 | Post hoc analysis of RCT data | Am J Obstet Gynecol | Predictors of response to elagolix with add-back therapy in women with fibroid-related heavy menstrual bleeding. |
| [31695514](https://pubmed.ncbi.nlm.nih.gov/31695514/) | 2019 | Review | Int J Womens Health | Short report on emerging efficacy data for elagolix as an oral treatment for uterine fibroids. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstet Gynecol | Overview of oral GnRH antagonists for uterine leiomyomas, including use with add-back hormones or at doses that avoid complete hypothalamic suppression. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2481332 | ORILISSA |
| 2481340 | ORILISSA |

---

## Safety Considerations

Please refer to the package insert for safety information. Health Canada warnings and contraindications were not included in the evidence provided, and no drug interactions were found in the query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism makes amenorrhea a plausible effect, and the drug is marketed in Canada. However, no trial or publication tests amenorrhea as a treatment goal. The available evidence covers bleeding reduction in fibroids and endometriosis and is indirect. Safety data are also missing, so the prediction is best treated as a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- Original approved indication text for the Canadian DINs
- Amenorrhea rates from the fibroid and endometriosis trials, or a study that targets amenorrhea directly
- Review of whether amenorrhea is a desirable outcome or only an expected effect of hormonal suppression

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

