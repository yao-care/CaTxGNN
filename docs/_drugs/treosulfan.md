---
layout: default
title: Treosulfan
parent: Model Prediction Only (L5)
nav_order: 938
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Treosulfan"
predicted_indications: ["diabetic cataract"]
description: "Treosulfan: predicted new indication Diabetic cataract (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Treosulfan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Treosulfan: Diabetic cataract
{: .text-alpha }

## One-Sentence Summary

Treosulfan is an alkylating agent used as a conditioning treatment before hematopoietic stem cell transplantation.
The TxGNN model predicts it may be effective for **diabetic cataract** (and several other cataract subtypes), but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model output only, and the available data do not support a plausible mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for treosulfan: "Treosulfan is an alkylating agent. DNA alkylation is thought to be responsible for the cytotoxic activities of treosulfan. Treosulfan showed hematopoietic stem cell depleting activity as well as immunosuppressive and antitumor activity in mouse models of leukemia." ([DailyMed: Grafapex (treosulfan) prescribing information, Medexus Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d06b03c-17aa-0492-e063-6294a90abd8f), label version 2025-01-31; accessed 2026-11-19.) Treosulfan is generally understood to be a bifunctional alkylating agent. It is a prodrug that converts into epoxide species, which damage DNA and cause cytotoxicity, and it is used for conditioning before stem cell transplantation.

Based on the data provided, **no mechanistic link supports this prediction**. Diabetic cataract mainly involves polyol pathway activation and oxidative stress in the lens. DNA alkylation and cytotoxicity have no recognized benefit for lens opacity, and alkylating agents may themselves carry ocular toxicity or cataract risk. The high score (0.9901) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02517388 | TRECONDYV | TREOSULFAN | Marketed |
| 02560585 | TREOSULFAN FOR INJECTION | TREOSULFAN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (myeloablative conditioning use) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the data compiled for this report. This is not evidence of absence of interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, literature, or supported mechanism. The drug's cytotoxic and myelosuppressive profile argues against use in chronic, non-lethal eye conditions such as cataract.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any biological link to lens disease exists
- Package insert warnings and contraindications from Health Canada, including ocular toxicity
- Preclinical or observational evidence of any effect on lens opacity
- Review of the Canadian license data (dosage forms and approved indications are missing)
- A route and formulation assessment for any ocular use, which has not yet been done

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Grafapex (treosulfan) prescribing information, Medexus Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d06b03c-17aa-0492-e063-6294a90abd8f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

