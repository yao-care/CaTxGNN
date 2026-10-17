---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Levothyroxine: predicted new indication Nodular goiter (evidence level L5). Approved use: Hypothyroidism"
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
---

# Levothyroxine
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

# Levothyroxine: From Hypothyroidism to Nodular Goiter

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone, originally used to treat hypothyroidism and related thyroid conditions.
The TxGNN model predicts it may be effective for **nodular goiter**, and the data compiled for this report include **2 clinical trials** (one randomized, placebo-controlled Phase 4 trial with 1,024 patients) and **20 publications**.
The benefit is modest and the safety trade-offs are real, so any use needs clear guardrails.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (also myxedema, congenital hypothyroidism, goiter, Hashimoto thyroiditis, thyroid cancer; source: knowledge-graph indication records, since no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Nodular goiter |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L1 per the compiled scoring, with a caveat: the two trials are not Phase 3 (one Phase 4, one phase N/A), so a conservative reading would be L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

**Note on the ranking:** Nodular goiter is the third-ranked prediction by TxGNN score, but it is the one with the strongest trial evidence. Endemic goiter (rank 1, 99.81%) has literature only and no registered trials. Several higher-ranked predictions (renal hypodysplasia/aplasia, bilateral renal agenesis, Potter sequence) have no plausible mechanism and look like knowledge-graph artifacts. This report focuses on nodular goiter.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, levothyroxine replaces thyroid hormone and suppresses pituitary TSH secretion. TSH drives growth of thyroid follicular cells, so lowering it may limit the growth of nodules and the thyroid as a whole.

The original indications already include goiter and thyroid disease, so nodular goiter is a close relative of conditions the drug is used for. This makes the repurposing gain limited rather than a leap into a new disease area. The mechanism is plausible, but the clinical benefit has been modest and inconsistent. Radioiodine (with or without recombinant human TSH) and surgery are the main alternatives, and current guidance generally does not favour routine suppression.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277589](https://clinicaltrials.gov/study/NCT00277589) | Phase 4 | Completed | 1024 | Randomized, observer-blind, placebo-controlled study of TSH-adapted levothyroxine therapy in nodular goiter. The primary objective was change in total nodule volume; secondary objectives were goiter volume at 12 months, nodule number and echogenicity. Directly relevant. |
| [NCT00941551](https://clinicaltrials.gov/study/NCT00941551) | N/A | Completed | 150 | Five-year follow-up of a randomized trial of unilateral lobectomy with or without postoperative levothyroxine. It examines prevention of recurrent nodular goiter after surgery, not medical shrinkage of the goiter. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11238476](https://pubmed.ncbi.nlm.nih.gov/11238476/) | 2001 | RCT | J Clin Endocrinol Metab | Compared radioiodine with suppressive levothyroxine (TSH 0.01–0.1 mU/L) in 64 patients with sporadic nontoxic nodular goiter. |
| [10426591](https://pubmed.ncbi.nlm.nih.gov/10426591/) | 1999 | Clinical study | Endocr J | Six months of levothyroxine in 35 diffuse and 35 nodular euthyroid goiter patients, evaluating thyroid and nodule volume and thyroglobulin. |
| [8299711](https://pubmed.ncbi.nlm.nih.gov/8299711/) | 1993 | Clinical study | Exp Clin Endocrinol | Suppressive levothyroxine in 104 patients with nontoxic benign multinodular goiter. |
| [20683172](https://pubmed.ncbi.nlm.nih.gov/20683172/) | 2010 | Clinical study | Endocr J | Short-term levothyroxine effects in 71 premenopausal women with multinodular disease. |
| [10382684](https://pubmed.ncbi.nlm.nih.gov/10382684/) | 1999 | Retrospective cohort | Endocr Res | Compared suppressive and replacement levothyroxine in solitary nodular disease and multinodular goiter. |
| [19636201](https://pubmed.ncbi.nlm.nih.gov/19636201/) | 2009 | Retrospective study | J Endocrinol Invest | Levothyroxine for preventing nodular recurrence after hemithyroidectomy. |
| [34961921](https://pubmed.ncbi.nlm.nih.gov/34961921/) | 2021 | Systematic review | Cochrane Database Syst Rev | rhTSH-aided radioiodine for non-toxic multinodular goitre, an alternative to levothyroxine suppression. |
| [27242669](https://pubmed.ncbi.nlm.nih.gov/27242669/) | 2016 | Review | Front Endocrinol | Notes that levothyroxine for goiter volume reduction remains controversial; surgery is needed for compressive symptoms. |
| [19106244](https://pubmed.ncbi.nlm.nih.gov/19106244/) | 2009 | Review | Eur J Endocrinol | Levothyroxine was once the preferred non-surgical option but is not recommended for routine use because of low efficacy and potential side effects. |
| [8844728](https://pubmed.ncbi.nlm.nih.gov/8844728/) | 1996 | Review | Otolaryngol Clin North Am | Overview of the evaluation and management of multinodular goiter. |

---

## Canada Market Information

Levothyroxine has 20 valid single-ingredient authorizations in Canada. Dosage form, manufacturer and approved indication text are not available in the compiled records.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02550792 | APO-LEVOTHYROXINE | Not available | Not available |
| 02461714 | LEVOTHYROXINE SODIUM FOR INJECTION | Not available | Not available |
| 02172119 | SYNTHROID | Not available | Not available |
| 02213214 | ELTROXIN | Not available | Not available |
| 02499924 | LEVOTHYROXINE SODIUM INJECTION | Not available | Not available |

The full list also includes further SYNTHROID, APO-LEVOTHYROXINE, ELTROXIN and injectable products.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** hypertension, pituitary hormone deficiencies (hypopituitarism and related forms), Kallmann syndrome and other hypogonadotropic hypogonadism, osteoporosis (including postmenopausal), diabetes mellitus and diabetic ketoacidosis, coronary artery disease, myocardial infarction, and thymus gland disease.
- **Risks specific to suppressive therapy:** subclinical hyperthyroidism, including atrial fibrillation and bone loss. Older and postmenopausal patients are particularly at risk.
- **Drug interactions:** 100 interactions were identified in the data compiled for this report. Those listed are mostly moderate:
  - Antidiabetic drugs: metformin, pioglitazone, canagliflozin, dapagliflozin, empagliflozin, alogliptin, albiglutide, dulaglutide and chlorpropamide
  - Acid-reducing drugs: omeprazole, rabeprazole and dexlansoprazole (cimetidine is minor)
  - Calcium and magnesium products: calcium phosphate, calcium acetate and magnesium oxide
  - Sympathomimetics: epinephrine, isometheptene and diethylpropion

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nodular goiter has the strongest evidence of the predictions reviewed, including a large randomized, placebo-controlled Phase 4 trial and a randomized comparison with radioiodine. However, the benefit is modest, goiter often regrows after stopping, and suppression carries cardiac and bone risks. The mechanism is plausible, but the repurposing gain over the existing goiter indication is limited.

**To proceed, the following is needed:**
- Review the published results of NCT00277589 and NCT00941551 to quantify the effect on nodule and goiter volume
- Define guardrails: target TSH, patient selection, and avoiding suppression in older, postmenopausal and cardiac-risk patients
- Compare against radioiodine (with or without rhTSH) and surgery
- Obtain the Health Canada package insert warnings and contraindications, which are currently missing and block formal safety screening
- Obtain detailed mechanism of action data
- Confirm approved indication text and dosage forms for the Canadian licences

**Other predictions:** Endemic goiter (Proceed with Guardrails, L3) and nontoxic goiter (Proceed with Guardrails, L2) are reasonable follow-ups. Dyshormonogenic goiter is a research question only. Substernal goiter and lingual goiter should be held for lack of efficacy data. Renal hypodysplasia/aplasia, bilateral renal agenesis, Potter sequence and Carney complex should be held, with no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

