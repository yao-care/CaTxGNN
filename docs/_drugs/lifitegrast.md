---
layout: default
title: Lifitegrast
parent: Model Prediction Only (L5)
nav_order: 549
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Lifitegrast: predicted new indication Penile fibromatosis (evidence level L5). Approved use: Dry eye syndrome (xerophthalmia)"
monitor_inn: "LIFITEGRAST"
predicted_indications: ["penile fibromatosis", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Lifitegrast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Lifitegrast: From Dry Eye Syndrome to Penile Fibromatosis
{: .text-alpha }

## One-Sentence Summary

Lifitegrast is a topical eye medicine originally used to treat dry eye syndrome (keratoconjunctivitis sicca).
The TxGNN model predicts it may be effective for **penile fibromatosis**, but this rests only on a model score, with **0 clinical trials** and **0 publications** supporting this specific prediction.
Among the other predictions, only diabetic retinopathy has any related literature (1 paper, indirect).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome (xerophthalmia) |
| Predicted New Indication | Penile fibromatosis |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lifitegrast is an LFA-1 (integrin alpha-L, ITGAL) antagonist. In laboratory assays it blocks T-cell adhesion to ICAM-1 (IC50 about 3 nM in Jurkat cells and 9 nM in HuT 78 cells) and reduces the release of inflammatory mediators. It was designed for minimal systemic exposure, so that it acts mainly at the site of application. Note that the formal mechanism-of-action field was not available in the data compiled for this report. The mechanism described here comes from pharmacology data on the drug's target.

Dry eye disease is driven partly by T-cell-mediated inflammation on the ocular surface. Fibromatoses such as Peyronie's disease involve fibroblast proliferation and chronic inflammation. A link through inflammation is therefore conceivable, but it is speculative. No preclinical or clinical data were found to support it.

The same caution applies to the other top predictions, including palmar fibromatosis (Dupuytren's contracture), Ledderhose disease and infantile digital fibromatosis. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so they are not independent evidence. A further concern is that lifitegrast is a topical eye drop with deliberately low systemic exposure, so reaching tissues such as the penis, palm or foot is doubtful.

The most biologically plausible alternative is **diabetic retinopathy** (score 0.9903). ICAM-1/LFA-1-mediated leukocyte adhesion contributes to retinal inflammation and capillary leukostasis. Delivery to the back of the eye from an eye drop remains a major uncertainty.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for penile fibromatosis or any of the other predicted indications.

---

## Literature Evidence

For the top prediction (penile fibromatosis), currently no related literature is available.

For the diabetic retinopathy prediction, one paper was identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41158172](https://pubmed.ncbi.nlm.nih.gov/41158172/) | 2025 | Genetic/proteomic association study | International Journal of Ophthalmology | Mendelian randomization combining plasma proteomics and genome-wide association data to identify therapeutic targets for retinal neurodegenerative diseases. It is a target-prioritization study, not a clinical study of lifitegrast, so the evidence is indirect. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02471027 | XIIDRA | Not available | Not available (the target is dry eye disease per the original indication) |

---

## Safety Considerations

**Drug Interactions**
- The interaction data compiled for this report contain only a pharmacology entry: lifitegrast's target is LFA-1 (ITGAL, integrin alpha-L). No drug-drug interactions were recorded.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for penile fibromatosis has a very high model score (0.9959) but no trials, no literature and no confirmed mechanistic link. Evidence is at the lowest level (L5). The topical ocular formulation, with minimal systemic exposure, makes reaching the diseased tissue doubtful.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Preclinical proof of concept, for example LFA-1 antagonism in fibroblast or fibrosis models, or in a retinal inflammation model (the most plausible follow-up, for diabetic retinopathy)
- Assessment of a suitable route and formulation for the target tissue, since route compatibility has not yet been evaluated
- Pediatric safety data if infantile digital fibromatosis is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

