---
layout: default
title: Tezacaftor
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Tezacaftor: predicted new indication HIV infectious disease (evidence level L5). Approved use: Cystic fibrosis"
monitor_inn: "Tezacaftor"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
---

# Tezacaftor
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

## Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Tezacaftor is a CFTR corrector, originally used in combination therapies for cystic fibrosis.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 7 of 7) |
| Number of DINs | 7 (marketed: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for vanzacaftor, tezacaftor, and deutivacaftor (a combination product containing tezacaftor): "Vanzacaftor and tezacaftor bind to different sites on the CFTR protein and have an additive effect in facilitating the cellular processing and trafficking of select mutant forms of CFTR (including F508del- CFTR) to increase the amount of CFTR protein delivered to the cell surface compared to either molecule alone. The combined effect of vanzacaftor, tezacaftor and deutivacaftor is increased quantity and function of CFTR at the cell surface, resulting in increased CFTR activity as measured both by CFTR-mediated chloride transport in vitro and by sweat chloride in patients with CF." ([DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20), label version 2026-08-26; accessed 2026-11-19.) Based on known information, tezacaftor is a CFTR corrector that helps the F508del-CFTR protein fold and traffic to the cell surface. It is marketed in combination with ivacaftor (Symdeko) and in triple combinations (Trikafta, Alyftrek) for cystic fibrosis patients with specific gene mutations.

No established mechanistic link between CFTR correction and HIV pathogenesis is supported by the available data. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated as speculative.

Other high-scoring predictions for this drug include leprosy and multiple endocrine neoplasia. Neither has clinical trial or literature support in the data compiled.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02478080 | SYMDEKO | IVACAFTOR; TEZACAFTOR | Marketed |
| 02517140 | TRIKAFTA | ELEXACAFTOR; IVACAFTOR; TEZACAFTOR | Marketed |
| 02526670 | TRIKAFTA | ELEXACAFTOR; IVACAFTOR; TEZACAFTOR | Marketed |
| 02542277 | TRIKAFTA | ELEXACAFTOR; IVACAFTOR; TEZACAFTOR | Marketed |
| 02542285 | TRIKAFTA | ELEXACAFTOR; IVACAFTOR; TEZACAFTOR | Marketed |
| 02559676 | ALYFTREK | DEUTIVACAFTOR; TEZACAFTOR; VANZACAFTOR (VANZACAFTOR CALCIUM) | Marketed |
| 02559684 | ALYFTREK | DEUTIVACAFTOR; TEZACAFTOR; VANZACAFTOR (VANZACAFTOR CALCIUM) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Seven valid authorizations in total are listed, all for tezacaftor-containing products.

---

## Safety Considerations

Please refer to the package insert for safety information.

The only interaction data compiled is a pharmacological target record: tezacaftor acts on the CFTR protein. No drug-drug interaction entries with other medicines are available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction is based on a model score alone (L5), with no registered clinical trials, no literature, and no plausible mechanistic link to CFTR correction in the available data. A high score by itself is not enough to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to support or refute a link to HIV biology
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Preclinical evidence, such as in vitro antiviral activity of tezacaftor against HIV
- A review of whether the HIV, SIV and feline immunodeficiency predictions are one correlated signal
- Approved indication text and dosage forms for the Canadian licenses, which are currently missing

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

