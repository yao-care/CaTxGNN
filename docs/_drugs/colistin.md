---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
monitor_inn: "COLISTIN"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
last_modified_at: 2026-10-27
description: "Colistin: predicted new indication postinfectious vasculitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Colistin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Colistin: polymyxin antibiotic (outer-membrane disruptor) → postinfectious vasculitis
{: .text-alpha }

## One-Sentence Summary

Colistin is a polymyxin antibiotic that acts against Gram-negative bacteria.
The TxGNN model predicts it may be useful for **postinfectious vasculitis**, but the data compiled for this report contain **no clinical trials and no publications** on this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | postinfectious vasculitis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Colistin is a polymyxin that disrupts the outer membrane of Gram-negative bacteria, which explains its antibacterial use.

Postinfectious vasculitis is an immune-mediated inflammatory condition of blood vessels that follows an infection. Colistin has no known immunomodulatory action relevant to vasculitis, and an antibacterial effect would not be expected to treat inflammation once the infection has resolved. It is also nephrotoxic and neurotoxic, which weighs against use in a condition that can involve the kidneys.

The high model score therefore appears to reflect a statistical association with infection-related diseases rather than a plausible biological rationale. No trials or literature were found to test it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244849 | COLISTIMETHATE FOR INJECTION U.S.P. | Not recorded | Not recorded |
| 00476420 | COLY-MYCIN M | Not recorded | Not recorded |
| 02403544 | COLISTIMETHATE FOR INJECTION, USP | Not recorded | Not recorded |

All three licences are single-ingredient products and currently valid.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

Colistin is generally known for kidney and nerve toxicity. Conditions recorded as contraindicated for colistin in the model's source data include kidney disease, myasthenia gravis and other neuromuscular junction diseases. These are not label text and should be verified against the product monograph. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications for postinfectious vasculitis, no plausible mechanistic link, and a notable kidney and nerve toxicity profile. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence that colistin affects postinfectious vasculitis
- A mechanistic rationale for immune-mediated vascular inflammation
- Product monograph warnings and contraindications from Health Canada
- Mechanism-of-action data from DrugBank
- A benefit–risk assessment given nephrotoxicity and neurotoxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

