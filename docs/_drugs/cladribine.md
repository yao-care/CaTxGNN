---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 199
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cladribine: From Its Currently Approved Uses (Not Recorded in the Data) to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog marketed in Canada under four licences, but the supplied data does not record its approved indications.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma** (score 99.77%).
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Cladribine is a purine nucleoside analog. Its cytotoxicity depends on activation by deoxycytidine kinase, and it acts mainly on lymphoid cells.

Embryonal rhabdomyosarcoma is a mesenchymal solid tumour, so the supplied data supports no direct mechanistic link to cladribine's lymphocyte-directed activity. The high score most likely reflects the disease's neighbourhood in the knowledge graph rather than a drug-specific mechanism.

The top six predictions are all rhabdomyosarcoma terms: parameningeal embryonal, botryoid-type of the vagina, embryonal extrahepatic bile duct, prostate embryonal, extrahepatic bile duct, and the parent disease term. They probably share one graph signal and should not be counted as six independent lines of evidence. A seventh prediction, liver sarcoma, is also prediction-only.

Any hypothesis would need preclinical support first, such as deoxycytidine kinase expression in rhabdomyosarcoma cells or in vitro sensitivity of rhabdomyosarcoma cell lines. Neither is in the supplied data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top prediction.

For reference, the only publication retrieved for any prediction is a 2004 case report on cladribine in smoldering systemic mastocytosis ([PMID 15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/)). It was linked to the liver sarcoma prediction, but it concerns a haematologic mast cell neoplasm and is not relevant to rhabdomyosarcoma.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2470179 | MAVENCLAD |
| 2494574 | CLADRIBINE INJECTION |
| 2319918 | CLADRIBINE INJECTION |
| 2553295 | APO-CLADRIBINE |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for cladribine in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or supporting literature. The rhabdomyosarcoma predictions are likely one correlated graph signal, not independent evidence. No mechanistic link to this solid tumour is supported by the available data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the four Canadian licences
- Preclinical evidence, such as deoxycytidine kinase expression and in vitro sensitivity of rhabdomyosarcoma cell lines
- A targeted literature and trial search specific to cladribine in rhabdomyosarcoma

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

