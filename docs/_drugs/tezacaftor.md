---
layout: default
title: Tezacaftor
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tezacaftor: predicted new indication HIV infectious disease (evidence level L5). Approved use: Cystic fibrosis"
monitor_inn: "Tezacaftor"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "female breast carcinoma", "homozygous familial hypercholesterolemia", "amyotrophic lateral sclerosis"]
---

# Tezacaftor
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

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

Tezacaftor is a CFTR corrector, originally used in combination therapies for cystic fibrosis.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tezacaftor is a CFTR corrector that helps the F508del-CFTR protein fold and traffic to the cell surface. It is marketed in combination with ivacaftor (Symdeko) and in triple combinations (Trikafta, Alyftrek) for cystic fibrosis patients with specific gene mutations.

No established mechanistic link between CFTR correction and HIV pathogenesis is supported by the available data. The prediction appears to rest on network-level associations in the TxGNN knowledge graph and should be treated as speculative.

Other high-scoring predictions for this drug include leprosy, multiple endocrine neoplasia, simian immunodeficiency virus infection, feline acquired immunodeficiency syndrome, rheumatoid arthritis, female breast carcinoma, homozygous familial hypercholesterolemia, and amyotrophic lateral sclerosis. None has clinical trial or literature support in the data compiled. The SIV and feline immunodeficiency predictions share nearly identical scores with the HIV prediction (about 0.990), which suggests a correlated knowledge-graph signal rather than independent evidence. Neither is a human indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02478080 | SYMDEKO | Not specified | Not specified |
| 02542285 | TRIKAFTA | Not specified | Not specified |
| 02559676 | ALYFTREK | Not specified | Not specified |
| 02517140 | TRIKAFTA | Not specified | Not specified |
| 02526670 | TRIKAFTA | Not specified | Not specified |

Seven valid authorizations in total are listed, all for tezacaftor-containing products. The five above are the first five.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

