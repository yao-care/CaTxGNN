---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 540
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
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

## Leuprolide: From Endometriosis to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Leuprolide is a GnRH (gonadotropin-releasing hormone) agonist originally used for endometriosis and precocious puberty.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are currently **0 clinical trials** and only **1 publication** (an unrelated case report), so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (other listed indications: precocious puberty, aromatase excess syndrome, familial male-limited precocious puberty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 12 of 12) |
| Number of DINs | 12 (marketed: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for leuprolide: "Leuprolide acetate, a gonadotropin releasing hormone (GnRH) agonist, acts as an inhibitor of gonadotropin secretion when given continuously in therapeutic doses. Animal and human studies indicate that after an initial stimulation, chronic administration of leuprolide acetate results in suppression of testicular and ovarian steroidogenesis." ([DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f), label version 2026-04-30; accessed 2026-11-19.) Based on known information, leuprolide is a GnRH agonist. After an initial stimulation phase it suppresses gonadal sex hormones, and this effect underlies its use in endometriosis and precocious puberty.

Sex-hormone changes could plausibly influence joint tissue or pain, which is one possible way to connect the original indications to osteoarthritis. However, this link is speculative. Suppressing sex hormones (as in androgen-deprivation therapy) is more commonly associated with bone loss than with joint benefit. The high model score should therefore be treated as a hypothesis only, not as evidence of efficacy.

The second-ranked prediction, pseudoachondroplasia (score 0.9969), has no supporting trials or literature. It is a skeletal dysplasia caused by COMP gene mutations, and GnRH agonism has no known direct link to that pathway.

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

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00836273 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |
| 00884502 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02230248 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02239833 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02239834 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02248239 | ELIGARD | LEUPROLIDE ACETATE | Marketed |
| 02248240 | ELIGARD | LEUPROLIDE ACETATE | Marketed |
| 02248999 | ELIGARD | LEUPROLIDE ACETATE | Marketed |
| 02268892 | ELIGARD | LEUPROLIDE ACETATE | Marketed |
| 02429977 | ZEULIDE DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02462699 | ZEULIDE DEPOT | LEUPROLIDE ACETATE | Marketed |
| 02562855 | LUPRON DEPOT | LEUPROLIDE ACETATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Twelve valid single-ingredient licenses are on record in total (LUPRON DEPOT, ELIGARD and ZEULIDE DEPOT).

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

