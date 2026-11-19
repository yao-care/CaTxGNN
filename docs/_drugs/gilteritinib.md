---
layout: default
title: Gilteritinib
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
description: "Gilteritinib: predicted new indication Bulbar polio (evidence level L5). Approved use: Acute myeloid leukemia (including multiple AML subtypes)"
monitor_inn: "GILTERITINIB"
predicted_indications: ["bulbar polio"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Gilteritinib: From Acute Myeloid Leukemia to Bulbar Polio
{: .text-alpha }

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
| TxGNN Prediction Score | 0.9910 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for gilteritinib: "Gilteritinib is a small molecule that inhibits multiple receptor tyrosine kinases, including FMS-like tyrosine kinase 3 (FLT3). Gilteritinib demonstrated the ability to inhibit FLT3 receptor signaling and proliferation in cells exogenously expressing FLT3 including FLT3-ITD, tyrosine kinase domain mutations (TKD) FLT3-D835Y and FLT3-ITD-D835Y, and it induced apoptosis in leukemic cells expressing FLT3-ITD." ([DailyMed: Xospata (gilteritinib) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5ff59aa-9c0d-49a8-9053-1f179b482383), label version 2026-10-01; accessed 2026-11-19.) Based on known information, gilteritinib is a dual FLT3/AXL tyrosine kinase inhibitor, and its efficacy in relapsed or refractory FLT3-mutated AML is established.

The link to bulbar polio is weak. Poliomyelitis is a viral infection of motor neurons, including those in the brainstem, and it is mainly prevented by vaccination. No antiviral therapy is established for it. No known mechanism connects FLT3/AXL inhibition to poliovirus infection. One speculative idea is that AXL has been implicated in the entry and replication of some viruses and in the regulation of innate immune responses. However, nothing in the compiled data supports this idea for poliovirus.

The high score (0.9910) should therefore be treated as a computational hypothesis only. It comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

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
- A review of whether the prediction is a TxGNN model (deep learning) artifact

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xospata (gilteritinib) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5ff59aa-9c0d-49a8-9053-1f179b482383) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

