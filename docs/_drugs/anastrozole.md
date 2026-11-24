---
layout: default
title: Anastrozole
parent: Model Prediction Only (L5)
nav_order: 60
evidence_level: L5
indication_count: 5
monitor_inn: "Anastrozole"
predicted_indications: ["neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia"]
last_modified_at: 2026-11-24
description: "Anastrozole: predicted new indication Neuroblastoma (evidence level L5). In Canada: 19 DINs (18 marketed, 1 dormant)"
---

# Anastrozole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Anastrozole: aromatase inhibitor → Neuroblastoma
{: .text-alpha }

## One-Sentence Summary

Anastrozole is an aromatase inhibitor (an oral hormonal therapy) that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **Neuroblastoma**, with a score of 0.9953.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Neuroblastoma |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 18 of 19; dormant: 1) |
| Number of DINs | 19 (marketed: 18) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for anastrozole: "The growth of many cancers of the breast is stimulated or maintained by estrogens. In postmenopausal women, estrogens are mainly derived from the action of the aromatase enzyme, which converts adrenal androgens (primarily androstenedione and testosterone) to estrone and estradiol. […] Anastrozole is a selective non-steroidal aromatase inhibitor." ([DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de), label version 2026-03-02; accessed 2026-11-19.) Anastrozole is known as an aromatase inhibitor, a drug class that lowers oestrogen production.

No established mechanistic link between aromatase inhibition and neuroblastoma has been identified. Neuroblastoma is a paediatric tumour of neural-crest origin and is not classically driven by oestrogen. The high score is a computational prediction only. No trials or publications in the compiled data study anastrozole in neuroblastoma, so the prediction should be treated as a hypothesis to test, not as support for clinical use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02224135 | ARIMIDEX | ANASTROZOLE | Marketed |
| 02320738 | PMS-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02338467 | SANDOZ ANASTROZOLE | ANASTROZOLE | Marketed |
| 02339080 | JAMP-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02351218 | ACH-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02365650 | TARO-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02374420 | APO-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02379562 | MAR-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02392259 | RIVA-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02392488 | BIO-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02393573 | MINT-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02394898 | TEVA-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02395649 | PRO-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02417855 | NAT-ANASTROZOLE | ANASTROZOLE | Marketed |
| 02442736 | ANASTROZOLE | ANASTROZOLE | Marketed |
| 02529904 | ANASTROZOLE | ANASTROZOLE | Marketed |
| 02540584 | JAMP ANASTROZOLE TABLETS | ANASTROZOLE | Marketed |
| 02553686 | AG-ANASTROZOLE TABLETS | ANASTROZOLE | Marketed |
| 02534118 | AG-ANASTROZOLE | ANASTROZOLE | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interacting drugs. All shown entries have an unclassified severity level. Examples include bupropion, omeprazole, pantoprazole, metformin, simvastatin, prednisone, morphine and acetylsalicylic acid. Their clinical significance needs pharmacist review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials, no literature and no established mechanism, so the evidence level is L5. The drug is widely marketed in Canada, but that does not support its use in neuroblastoma.

**To proceed, the following is needed:**
- Preclinical studies (e.g. neuroblastoma cell-line or animal models) testing whether aromatase inhibition has any effect
- Mechanism of action data to assess whether oestrogen or aromatase pathways are relevant to neuroblastoma biology
- Health Canada package insert warnings and contraindications for the safety review
- Paediatric safety and dosing considerations, since neuroblastoma mainly affects young children

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for anastrozole is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

