---
layout: default
title: Imiglucerase
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
monitor_inn: "Imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
description: "Imiglucerase: predicted new indication Hurler syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Imiglucerase
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

## Imiglucerase: Hurler syndrome
{: .text-alpha }

## One-Sentence Summary

Imiglucerase is a recombinant enzyme replacement therapy originally used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, but there are **0 clinical trials** and only **1 general review article** supporting this direction.
The prediction appears to reflect similarity within the lysosomal storage disease family rather than a real enzymatic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, imiglucerase is a recombinant form of human glucocerebrosidase. It breaks down glucosylceramide, which builds up in Gaucher disease, and its efficacy in that condition is established.

Hurler syndrome (MPS I) and Gaucher disease are both lysosomal storage disorders treated with enzyme replacement therapy (ERT). However, Hurler syndrome is caused by a deficiency of alpha-L-iduronidase, which leads to accumulation of glycosaminoglycans (dermatan and heparan sulfate). Glucocerebrosidase does not act on these substrates, so there is no substrate overlap. The only link is the shared ERT class.

The high TxGNN score most likely reflects network proximity within the lysosomal storage disease family. The specific approved ERT for MPS I is laronidase. The same reasoning applies to Scheie syndrome (an attenuated form of MPS I), the second-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT in lysosomal storage diseases. It describes the development of imiglucerase for Gaucher disease and ERT for Fabry disease. It does not provide specific evidence for MPS I. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02241751 | CEREZYME | Not stated | Not stated in the compiled data |

---

## Safety Considerations

- **Drug Interactions**: One interaction was recorded: **Miglustat** (Moderate severity). Miglustat is a substrate reduction therapy used in Gaucher disease.

Please refer to the package insert for other warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to a single general review, with no clinical trials. There is no enzymatic link between glucocerebrosidase and the substrates that accumulate in MPS I. The prediction is better explained by disease-class similarity than by a real mechanism, and a specific approved ERT (laronidase) already exists.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and any preclinical evidence of activity against MPS I substrates
- Package insert warnings and contraindications from Health Canada
- Approved indication text and dosage form for the Canadian product
- Evidence that imiglucerase offers any benefit over laronidase in MPS I

---

### Note on Other Predictions

The other top-10 predictions are also supported by weak or no evidence (mostly L5, with no trials and no literature):

- Scheie syndrome has the same limitations as Hurler syndrome.
- Cholesteryl ester storage disease and Wolman disease are caused by LIPA deficiency, for which sebelipase alfa is the appropriate ERT.
- This is not a new repurposing signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

