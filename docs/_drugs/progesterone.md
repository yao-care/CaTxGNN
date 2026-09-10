---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Endogenous Hormone Therapy to Amenorrhea

## One-Sentence Summary

Progesterone is a naturally occurring female steroid hormone widely used across reproductive endocrinology; however, this evidence pack contains no recorded original-indication or Canadian licensing data for the drug (it is not currently marketed in Canada). The TxGNN model predicts relevance to **Amenorrhea**, with **50 clinical trials** and **18 publications** identified, though most trials studied related reproductive-endocrine conditions or other compounds rather than progesterone itself as a direct amenorrhea treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Canadian license records exist for this drug in this evidence pack |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% (rank 25) |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on well-established pharmacology, progesterone is a naturally occurring female sex steroid hormone that regulates the menstrual cycle, drives secretory transformation of the endometrium, and maintains pregnancy. Its clinical use across reproductive endocrinology is longstanding, and mechanistically it is directly applicable to amenorrhea through the classic "progesterone withdrawal" principle (the progesterone challenge test): administering exogenous progesterone and then withdrawing it induces endometrial shedding and bleeding in women with adequate endogenous estrogen, a mechanism used both diagnostically and therapeutically in secondary amenorrhea.

Because no original indication is recorded for this drug in the current data set, the relationship to amenorrhea cannot be framed as an indication extension from a documented use — it instead rests on progesterone's core, textbook reproductive physiology. Amenorrhea sits at the center of that physiology, which is why the biological plausibility of this prediction is high even without a formal Canadian regulatory anchor.

That said, the supporting trial evidence in this pack is largely indirect: most of the 50 clinical trials involve other compounds (elagolix, relugolix, kisspeptin, romosozumab, mibavademab) studied in amenorrhea-adjacent populations rather than progesterone itself, and were graded "C" (low relevance) or left ungraded. Only a handful of trials — e.g., progesterone-induced withdrawal bleeding studies and medroxyprogesterone acetate trials — test progesterone directly against an amenorrhea-related endpoint. This is why the evidence level is rated L3 (observational/indirect) rather than L1/L2, despite the strong mechanistic rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Tests whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction with clomiphene citrate in women with oligo-/amenorrhea |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-ablation medroxyprogesterone acetate and its effect on endometrial amenorrhea rates |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1845 | Estradiol + progesterone combination for vasomotor symptoms in postmenopausal women; provides background safety data for progesterone co-therapy |
| [NCT05967819](https://clinicaltrials.gov/study/NCT05967819) | N/A | Recruiting | 54 | Observational study of physical/psychosocial stress effects on reproductive hormones (including progesterone) and menstrual cycles in functional hypothalamic amenorrhea |
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Reproductive/endocrine function study in amenorrheic young athletes; evaluates estrogen (not progesterone) but relevant to disease population |
| [NCT01674426](https://clinicaltrials.gov/study/NCT01674426) | N/A | Completed | 17 | Pilot RCT of cognitive behavior therapy vs. observation for functional hypothalamic amenorrhea |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | Romosozumab plus transdermal estradiol and cyclic progesterone for bone density in functional hypothalamic amenorrhea |
| [NCT07235917](https://clinicaltrials.gov/study/NCT07235917) | Phase 2 | Recruiting | 34 | Mibavademab safety/efficacy study in functional hypothalamic amenorrhea |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Cardiovascular risk markers in functional hypothalamic amenorrhea (hypoestrogenemia) |
| [NCT01927432](https://clinicaltrials.gov/study/NCT01927432) | N/A | Completed | 73 | Ultrasound characterization of ovarian follicle dynamics in women with amenorrhea |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Diagnostic and therapeutic use of oral micronized progesterone in endocrinology, including its role via hypothalamic kisspeptin/neurokinin B/dynorphin neurons |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Etiology and management of amenorrhea in adolescent/young adult women, centered on HPO-axis dysfunction affecting estrogen and progesterone |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Current understanding of etiology, symptoms, and treatment options for Premature Ovarian Insufficiency |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of vaginal bleeding in postmenopausal women; discusses estrogen/progesterone withdrawal physiology |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | Endocrine background of hormonal treatments for endometriosis, including progesterone-resistance mechanisms |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Primary Ovarian Insufficiency: current concepts, including secondary amenorrhea and hormone replacement |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Neuroendocrine control of ovulation; hypothalamic-pituitary-ovarian axis failure resulting in anovulation/amenorrhea |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Chemotherapy-induced amenorrhea and its prognostic significance in premenopausal breast cancer patients |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Classic evaluation-of-amenorrhea review describing the progesterone challenge test in diagnostic work-up |
| [945033](https://pubmed.ncbi.nlm.nih.gov/945033/) | 1976 | Case Series | Annals of Internal Medicine | Galactorrhea-amenorrhea syndromes: describes failure of ovulatory LH/progesterone peaks and response to treatment |

---

## Canada Market Information

Progesterone is currently **not marketed in Canada** under this evidence pack — no Drug Identification Numbers (DINs) or license records were found (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were available in this evidence pack, and this is flagged as a **Blocking** data gap that prevents completion of an initial safety review (TFDA/product-label warnings and contraindications need to be sourced before evaluation can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for progesterone in amenorrhea is strong and textbook-grounded (progesterone withdrawal induces endometrial bleeding), but the supporting evidence in this pack is largely indirect — most trials involve other compounds or amenorrhea-adjacent populations rather than progesterone-specific efficacy data — and a **Blocking** data gap on regulatory safety information (warnings/contraindications) currently prevents even an initial safety assessment. The drug also has no active Canadian market presence (0 DINs) to anchor a repurposing pathway.

**To proceed, the following is needed:**
- TFDA/regulatory package-insert data (warnings, contraindications) to clear the Blocking data gap and enable an S1 safety review
- Confirmed mechanism-of-action (MOA) documentation from DrugBank to support the mechanistic rationale
- A focused literature/trial screen isolating studies that test progesterone itself (not co-administered hormones or unrelated compounds such as elagolix, relugolix, or kisspeptin) specifically for amenorrhea treatment efficacy
- Clarification of the regulatory pathway if progesterone is intended for future use/marketing in Canada, given it currently holds no license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

