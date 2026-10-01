---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 115
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Biotin: From Multivitamin Supplementation to Dyspepsia

## One-Sentence Summary

Biotin is a B-vitamin that in Canada appears in multivitamin products (MULTI 12 and MULTI-12/K1 PEDIATRIC). The TxGNN model predicts it may be effective for **dyspepsia**. Only **2 clinical trials** and **7 publications** were retrieved, and **none of them tests biotin as a treatment for dyspepsia**, so the prediction rests almost entirely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records; the products are multivitamin formulations |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, biotin is a cofactor for carboxylase enzymes involved in carbohydrate, fat and amino acid metabolism. Biotin deficiency can cause gastrointestinal symptoms.

Any link to dyspepsia is therefore indirect. If biotin helps at all, the most plausible route is correcting a deficiency state, not treating dyspepsia itself. Without the original indication or mechanism data, the graph prediction cannot be cross-checked against known pharmacology.

A second predicted indication, gastroparesis (score 99.42%), has no supporting trials or literature at all.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Serum micronutrient levels and deficiencies in bariatric surgery patients using transdermal vitamin patches. It measures absorption, not dyspepsia, and gives no efficacy evidence. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs pregabalin as preemptive analgesia for postoperative pain. It involves neither biotin nor dyspepsia and appears to be a retrieval artifact. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review | Eksp Klin Gastroenterol | A prebiotic supplement (inulin, oligofructose, vitamins including biotin, zinc, selenium) for gut microbiota disorders in patients on antibiotics for lung disease. Biotin is only one component, and dyspepsia is not the target. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | A 5-month-old infant diagnosed with dyspepsia as a neonate and fed only amino acid formula developed biotin deficiency, with alopecia and scaly dermatitis. This shows that biotin deficiency can arise in a dyspepsia setting, not that biotin treats dyspepsia. |
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical study | Minerva Gastroenterol Dietol | An open multicentre study of a food supplement for functional dyspepsia after *H. pylori* treatment. Biotin is not among the listed ingredients. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Stomach antral endocrine cells in irritable bowel syndrome patients. Not related to biotin. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Endocrine cells in the stomach's oxyntic mucosa in irritable bowel syndrome. Not related to biotin. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathol | Interleukin-10 in *H. pylori*-associated gastritis. Not related to biotin. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney Int | Small bowel T cells and stress proteins in IgA nephropathy. Not related to biotin. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2100606 | MULTI 12 |
| 2242529 | MULTI-12/K1 PEDIATRIC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no retrieved trial or publication tests biotin for dyspepsia. The two trials are unrelated, and the literature consists of one case report, one review and observational studies. Any biological link is indirect, most likely deficiency correction. Safety data are also missing, so the candidate cannot yet pass safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism of action data for biotin, for example from DrugBank
- The approved indication text, dosage forms and manufacturer for the two Canadian licences
- Trials or studies that directly test biotin for dyspepsia, or evidence that dyspepsia patients have biotin deficiency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

