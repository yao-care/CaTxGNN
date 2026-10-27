---
layout: default
title: Goserelin
parent: Model Prediction Only (L5)
nav_order: 440
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Goserelin: predicted new indication Amenorrhea (evidence level L5). Approved use: Endometriosis"
monitor_inn: "GOSERELIN"
predicted_indications: ["amenorrhea (disease)", "renal hypoplasia (disease)", "renal hypoplasia, bilateral"]
---

# Goserelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Goserelin: From Endometriosis to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Goserelin is a GnRH agonist originally used to treat endometriosis.
The TxGNN model predicts it may be effective for **amenorrhea**,
with **1 clinical trial** and **15 publications** currently associated with this direction. Most of this evidence concerns breast cancer, where amenorrhea is an expected drug effect rather than a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the Canadian licence indication text is not available, so this comes from the knowledge graph) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (as graded in the compiled data; the only trial is indirectly relevant and has unknown status, so this is a generous reading) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, goserelin is a GnRH agonist. Continuous administration desensitizes pituitary GnRH receptors and suppresses LH and FSH. This lowers ovarian estradiol production and produces a reversible hypogonadal state.

This is how it works in endometriosis: lowering estrogen reduces the growth of estrogen-dependent lesions. The same estrogen suppression stops menstruation, so amenorrhea follows directly. That explains why the model scores this link so highly.

However, amenorrhea here is mostly a pharmacodynamic effect or an outcome measure, not a separate disease to be treated. The "new indication" framing is therefore ambiguous. More meaningful uses would be deliberate menstrual suppression or ovarian protection during chemotherapy, and these are different clinical questions from the one the model predicted.

Two other predictions, renal hypoplasia and bilateral renal hypoplasia (both about 99.06%), have no plausible mechanistic link, no trials and no literature. They are model artefacts and should not be pursued.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene with or without goserelin in premenopausal women with hormone receptor-positive stage I-IIIA breast cancer, with or without chemotherapy-induced amenorrhoea. The endpoints concern breast cancer outcomes, so relevance to amenorrhea as an indication is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | Goserelin vs CMF chemotherapy as adjuvant therapy in premenopausal node-positive breast cancer (ZEBRA study) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | Chemotherapy followed by goserelin vs either alone in premenopausal node-negative breast cancer (IBCSG Trial VIII) |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs low-dose oral contraceptive for endometriosis-associated pelvic pain |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT (secondary analysis) | J Clin Oncol | Effects of chemotherapy, goserelin or both on amenorrhea, hot flashes and quality of life (IBCSG Trial VIII) |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis/Review | Ann Oncol | OPTION trial: GnRH agonist protection against chemotherapy-induced ovarian toxicity in early breast cancer |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Therapeutic induction of amenorrhoea, including goserelin, for female personnel mobilised for war |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | LHRH agonists in early breast cancer and the benefits of reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Methods of ovarian ablation in adjuvant breast cancer treatment |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin ovarian ablation improved survival in stage II/III HR-positive breast cancer without chemotherapy-induced amenorrhea |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort/Observational | J Clin Oncol | Whether estradiol monitoring is needed during ovarian suppression for breast cancer |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02225905 | ZOLADEX LA | Not specified | Not specified |
| 02049325 | ZOLADEX | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (GnRH agonist), not a conventional cytotoxic |
| Myelosuppression Risk | Not a typical feature of this drug class |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: hypertensive disorder, hypertension, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, obesity disorder, monogenic obesity, urinary tract obstruction.
- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: dolasetron.
  - **Moderate**: antidiabetic agents (acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, albiglutide, empagliflozin, glimepiride, linagliptin, metformin, saxagliptin), clarithromycin, famotidine, loperamide, palonosetron, bisacodyl, picosulfuric acid, and polyethylene glycol with electrolytes.

The Health Canada package insert warnings were not available, so the label should be consulted directly.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score reflects a pharmacological effect that is already expected: estrogen suppression leads to amenorrhea. It does not represent a new therapeutic use. The only trial concerns breast cancer, and the literature is mostly breast cancer or endometriosis work in which amenorrhea is a secondary outcome. The renal hypoplasia predictions have no support at all.

**To proceed, the following is needed:**
- A clear definition of the clinical question (for example menstrual suppression or ovarian protection during chemotherapy) instead of amenorrhea as a disease
- Health Canada package insert warnings and contraindications, which are currently a blocking gap
- Mechanism of action data from DrugBank
- Approved indication text for the two Canadian DINs
- A review of the cardiometabolic contraindications and the antidiabetic interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

