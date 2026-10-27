---
layout: default
title: Fomepizole
parent: Model Prediction Only (L5)
nav_order: 409
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Fomepizole: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not stated in the Canadian license records"
monitor_inn: "FOMEPIZOLE"
predicted_indications: ["sclerosing cholangitis"]
---

# Fomepizole
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

## Fomepizole: From Methanol/Ethylene Glycol Poisoning to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Fomepizole is an alcohol dehydrogenase inhibitor, and the Canadian license records compiled for this report do not state an approved indication. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records (general pharmacological knowledge: methanol and ethylene glycol poisoning) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, fomepizole is a competitive inhibitor of alcohol dehydrogenase. It is used to block the conversion of methanol and ethylene glycol into their toxic metabolites.

A possible link to sclerosing cholangitis is that blocking alcohol dehydrogenase might change oxidative or aldehyde stress in the liver and bile ducts. This is speculative, and nothing in the compiled data supports it. The high score may reflect network proximity or shared gene associations in the knowledge graph rather than a true therapeutic mechanism. A high prediction score alone is not enough to conclude biological relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242980 | ANTIZOL | Not specified | Not specified |
| 02435667 | FOMEPIZOLE FOR INJECTION | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: Ethanol, rated **Major** (DDInter). Fomepizole and ethanol both act on alcohol dehydrogenase, so co-administration needs careful review.
- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph links fomepizole to contraindication edges for kidney disease, pyoureter, liver disease and gallbladder disease. These come from model data and not from the package insert, so they should be verified. The liver and gallbladder links are particularly relevant to a hepatobiliary indication.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model prediction score. There are no clinical trials or publications, the mechanism of action data is missing, and the knowledge graph flags liver and gallbladder disease as potential contraindications. Evidence is at level L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank, to assess any link to sclerosing cholangitis.
- Literature and clinical trial searches on fomepizole in hepatobiliary or cholestatic disease, plus preclinical evidence if available.
- Approved indication text, dosage forms and route information for the two Canadian licenses.
- Review of the hepatobiliary safety signals and the ethanol interaction before any further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

