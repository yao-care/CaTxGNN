---
layout: default
title: Gilteritinib
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Gilteritinib: predicted new indication Bulbar polio (evidence level L5). Approved use: Acute myeloid leukemia (including multiple AML subtypes)"
---

# Gilteritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Gilteritinib: From Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Gilteritinib is a targeted kinase inhibitor, originally used to treat acute myeloid leukemia (AML).
The TxGNN model predicts it may be effective for **bulbar polio**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukemia (including multiple AML subtypes) |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, gilteritinib is a dual FLT3/AXL tyrosine kinase inhibitor, and its efficacy in relapsed or refractory FLT3-mutated AML is established.

The link to bulbar polio is weak. Poliomyelitis is a viral infection of motor neurons, including those in the brainstem, and it is mainly prevented by vaccination. No antiviral therapy is established for it. No known mechanism connects FLT3/AXL inhibition to poliovirus infection. One speculative idea is that AXL has been implicated in the entry and replication of some viruses and in the regulation of innate immune responses. However, nothing in the compiled data supports this idea for poliovirus.

The high score (0.991) should therefore be treated as a computational hypothesis only. It could also reflect an artifact of the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02495058 | XOSPATA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FLT3/AXL tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically blood counts, liver and renal function) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records. The first 20 are listed in the data compiled for this report. Main ones by severity:
  - **Major**: Clarithromycin, Dolasetron
  - **Moderate**: Famotidine, Aprepitant, Bisacodyl, Cimetidine, Eliglustat, Loperamide, Dexamethasone, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Palonosetron, Sodium sulfate, Naltrexone, Levofloxacin, Linagliptin, Metformin, Metreleptin, Miconazole
  - **Minor**: Metronidazole

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this indication is the model score. There are no clinical trials or publications, no mechanistic data, and no plausible biological link between FLT3/AXL inhibition and poliovirus infection. Safety label information is also incomplete.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data, for example from DrugBank
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical evidence, such as in vitro poliovirus infection models testing AXL or FLT3 involvement
- A review of whether the prediction is a knowledge-graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

