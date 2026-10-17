---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 540
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Leuprolide: predicted new indication Osteoarthritis (evidence level L5). Approved use: Endometriosis (other listed indications: precocious puberty…"
monitor_inn: "Leuprolide"
predicted_indications: ["osteoarthritis", "pseudoachondroplasia"]
---

# Leuprolide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Leuprolide: From Endometriosis to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH (gonadotropin-releasing hormone) agonist originally used for endometriosis and precocious puberty.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are currently **0 clinical trials** and only **1 publication** (an unrelated case report), so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (other listed indications: precocious puberty, aromatase excess syndrome, familial male-limited precocious puberty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leuprolide is a GnRH agonist. After an initial stimulation phase it suppresses gonadal sex hormones, and this effect underlies its use in endometriosis and precocious puberty.

Sex-hormone changes could plausibly influence joint tissue or pain, which is one possible way to connect the original indications to osteoarthritis. However, this link is speculative. Suppressing sex hormones (as in androgen-deprivation therapy) is more commonly associated with bone loss than with joint benefit. The high model score should therefore be treated as a hypothesis only, not as evidence of efficacy.

The second-ranked prediction, pseudoachondroplasia (score 99.69%), has no supporting trials or literature. It is a skeletal dysplasia caused by COMP gene mutations, and GnRH agonism has no known direct link to that pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostate adenocarcinoma presenting with skin changes that mimicked inflammatory breast cancer in a 78-year-old man. It does not address osteoarthritis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230248 | LUPRON DEPOT | Not specified | Not specified |
| 02248239 | ELIGARD | Not specified | Not specified |
| 02268892 | ELIGARD | Not specified | Not specified |
| 00836273 | LUPRON DEPOT | Not specified | Not specified |
| 02248240 | ELIGARD | Not specified | Not specified |

Twelve valid single-ingredient licenses are on record in total (LUPRON DEPOT, ELIGARD and ZEULIDE DEPOT); the five above are shown as examples.

---

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (these come from the model's knowledge graph, not from the product label): hypertension, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, obesity, stroke and other cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, hemoglobinopathy, and urinary tract obstruction.
- **Drug Interactions**: 100 interactions were identified in the interaction database. Examples shown:
  - **Major**: dolasetron, cisapride
  - **Moderate**: antidiabetic agents (acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, linagliptin, metformin, saxagliptin, chlorpropamide, albiglutide, dulaglutide), famotidine, loperamide, clarithromycin, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, castor oil)

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no clinical trials support it, the only retrieved publication is unrelated to osteoarthritis, and the mechanism is speculative. Hormone suppression is more commonly linked to bone loss than to joint benefit. This is a model hypothesis only (Evidence Level L5).

**To proceed, the following is needed:**
- Mechanism of action data for leuprolide
- A literature review of sex hormones and GnRH agonists in osteoarthritis, including preclinical studies
- Health Canada package insert warnings and contraindications, plus approved indication text and dosage forms for each DIN
- Review of the cardiometabolic and bone-density safety signals for a chronic joint condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

