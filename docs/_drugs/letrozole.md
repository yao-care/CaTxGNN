---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 457
evidence_level: L1
indication_count: 10
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Letrozole: From Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation aromatase inhibitor established worldwide for the treatment of hormone receptor-positive breast cancer in postmenopausal women. The TxGNN model's top-ranked prediction, **Female Breast Carcinoma**, is a broader disease-ontology label that substantially overlaps with letrozole's existing global indication rather than representing a genuinely novel use — but it is strongly supported, with **50 clinical trials** and **20 curated publications** in this Evidence Pack, and it serves as a useful calibration check on the model's outputs. Regulatory data specific to the Canadian market are currently missing (drug not marketed, 0 DINs on file).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (ER+ postmenopausal breast cancer) — well documented in the supporting literature, though formal local approved-indication text is not on file |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not yet on file for this drug entry. Based on the supporting literature captured in this Evidence Pack, letrozole is a third-generation, non-steroidal aromatase inhibitor: it blocks peripheral conversion of androgens to estrogens, cutting off the estrogen supply that drives proliferation of estrogen-receptor-positive (ER+) breast tumors. This mechanism is explicitly described in several of the attached publications (e.g., PMID 20095792, PMID 36243120).

"Female breast carcinoma" is a broad disease-ontology label that, in practice, largely coincides with letrozole's current, well-established approved use — it is not a distinct new organ or pathway target. The repurposing rationale for this candidate explicitly notes the overlap, describing the prediction as evidence-equivalent to letrozole's existing indication rather than a novel signal. As such, this candidate is best read as a **calibration/confirmatory case**: it demonstrates that TxGNN correctly recovers a drug's known indication with very high confidence, which is a useful sanity check on the model but does not itself constitute a new repurposing opportunity requiring de novo clinical development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02246621](https://clinicaltrials.gov/study/NCT02246621) | Phase 3 | Active, not recruiting | 493 | Randomized, double-blind trial of NSAI (anastrozole/letrozole) plus abemaciclib vs. placebo in HR+/HER2- locoregionally recurrent or metastatic breast cancer with no prior systemic therapy |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3B | Completed | 301 | Everolimus + exemestane in postmenopausal ER+ breast cancer progressing after non-steroidal aromatase inhibitor therapy |
| [NCT02142868](https://clinicaltrials.gov/study/NCT02142868) | N/A (Expanded Access) | No longer available | N/A | Expanded access program providing palbociclib + letrozole to postmenopausal women with HR+/HER2- advanced breast cancer |
| [NCT00004205](https://clinicaltrials.gov/study/NCT00004205) | Phase 3 | Completed | 8,028 | Landmark randomized double-blind trial comparing letrozole vs. tamoxifen as adjuvant endocrine therapy in receptor-positive postmenopausal breast cancer |
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3B | Completed | 3,246 | COMPLEEMENT-1: safety/efficacy of ribociclib + letrozole in men and pre/postmenopausal women with HR+/HER2- advanced breast cancer, no prior hormonal therapy |
| [NCT00171340](https://clinicaltrials.gov/study/NCT00171340) | Phase 3 | Completed | 1,065 | Upfront vs. delayed-start zoledronic acid for prevention of letrozole-associated bone loss in postmenopausal HR+ breast cancer |
| [NCT00050011](https://clinicaltrials.gov/study/NCT00050011) | Phase 3 | Completed | 602 | Zoledronic acid for prevention of cancer treatment-related bone loss in patients receiving adjuvant letrozole |
| [NCT00171314](https://clinicaltrials.gov/study/NCT00171314) | Phase 3 | Completed | 527 | Upfront vs. delayed-start zoledronic acid to prevent bone loss during adjuvant letrozole therapy |
| [NCT02918084](https://clinicaltrials.gov/study/NCT02918084) | Phase 3 | Active, not recruiting | 1,000 | Concurrent vs. sequential chemotherapy and aromatase inhibitors as adjuvant treatment of endocrine-responsive early breast cancer |
| [NCT04852887](https://clinicaltrials.gov/study/NCT04852887) | Phase 3 | Recruiting | 1,670 | De-escalation of breast radiation for low-risk, hormone-sensitive, HER2-negative Stage I breast cancer treated with endocrine therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | The New England Journal of Medicine | Landmark trial (BIG 1-98) comparing letrozole and tamoxifen as adjuvant treatment for steroid-hormone-receptor-positive breast cancer in postmenopausal women |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Research and Treatment | Overall survival results of palbociclib + letrozole vs. letrozole alone as first-line treatment for ER+/HER2- advanced breast cancer (PALOMA-1) |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT | The Lancet Oncology | CORALLEEN trial: neoadjuvant ribociclib + letrozole vs. chemotherapy in luminal B HR+/HER2- breast cancer |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Overview of letrozole pharmacology, toxicity, and potential therapeutic effects, including use in ovulation induction |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Comparative review of anastrozole, letrozole, and exemestane in management of early breast cancer |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh, Scotland) | Review of letrozole's development and use in advanced and neoadjuvant breast cancer |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opinion on Pharmacotherapy | Present and future role of letrozole in breast cancer treatment |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacodynamic, pharmacokinetic, efficacy, and safety review of letrozole |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | Review | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial |
| [18829517](https://pubmed.ncbi.nlm.nih.gov/18829517/) | 2008 | Clinical study | Clinical Cancer Research | Letrozole shown to be superior to anastrozole in suppressing breast tissue and plasma estrogen levels |

---

## Canada Market Information

No product licenses are on file for letrozole in this dataset. The Evidence Pack records the drug as **Not Marketed** in Canada, with **0 DINs** and no license entries, so a market summary table cannot be produced. This is flagged as a blocking data gap (DG001) — the absence of a Health Canada product listing should be verified directly against the Health Canada Drug Product Database before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently on file for this drug entry (flagged as data gap DG001, Blocking severity — remediation requires downloading and parsing the official product monograph).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by a very large and mature body of Phase 2/3 clinical evidence (L1), but this evidence largely reflects letrozole's *existing* global breast cancer indication rather than a genuinely new therapeutic use — the repurposing signal should be treated as a model-calibration confirmation rather than a novel opportunity. Progression is also currently blocked by the absence of Canadian regulatory and safety data.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data via DrugBank API — currently a High-severity data gap (DG002)
- Verification of current Canadian market/licensing status, since this Evidence Pack shows 0 DINs despite letrozole being a globally marketed drug
- Clarification of whether "female breast carcinoma" should be treated as a distinct repurposing candidate or reclassified as a confirmatory/calibration case, given its near-total overlap with the known indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

