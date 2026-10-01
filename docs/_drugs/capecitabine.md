---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Capecitabine: From Approved Oncology Use to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)

## One-Sentence Summary

Capecitabine is an oral prodrug of 5-fluorouracil (5-FU) and is marketed in Canada as an anticancer drug. The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**, a rare hereditary syndrome. No evidence supports this specific prediction yet, with **0 clinical trials** and **0 publications** linked.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (the Canadian license entries have no indication text) |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the dataset. From general pharmacology, capecitabine is an oral prodrug converted to 5-FU, which inhibits thymidylate synthase and blocks DNA synthesis in rapidly dividing tumour cells. This mechanism is plausible for tumours of the gastric epithelium.

The prediction rests on the model score alone. GAPPS is a hereditary syndrome with numerous polyps in the proximal stomach and a high risk of gastric adenocarcinoma. It differs biologically and clinically from sporadic gastric cancer, so evidence from sporadic disease cannot be transferred directly. The mechanistic link is therefore plausible, but nothing has been shown for GAPPS.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 11 licenses are shown below. The dataset gives no dosage form, manufacturer, or approved indication text for these entries.

| DIN | Product Name |
|---------|------|
| 02457490 | TARO-CAPECITABINE |
| 02519879 | CAPECITABINE |
| 02426765 | ACH-CAPECITABINE |
| 02457504 | TARO-CAPECITABINE |
| 02514982 | CAPECITABINE |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Low to medium (general class knowledge; please confirm in the package insert) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

The details in this table are not from the Evidence Pack. They are based on general drug-class knowledge and should be checked against the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The GAPPS prediction has a very high model score (99.94%) but no linked trials or literature, and the disease is a hereditary syndrome that differs from sporadic gastric cancer. Health Canada safety data is also missing, which blocks safety screening.

Other gastric predictions for capecitabine have more support. Gastric tubular adenocarcinoma has L1 evidence, including several Phase 3 RCTs such as CLASSIC and RESOLVE. Gastric cardia adenocarcinoma has L2 evidence, with Phase 2 trials of capecitabine plus oxaliplatin. These trials come from broad gastric or GEJ populations, not from GAPPS.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking data gap)
- Mechanism of action data from DrugBank
- Confirmation of the original approved indications from the Canadian product monographs
- A GAPPS-specific literature and trial search, including case series in hereditary gastric cancer syndromes
- A decision on whether to prioritize the better-supported gastric subtypes (tubular adenocarcinoma, cardia adenocarcinoma) for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

