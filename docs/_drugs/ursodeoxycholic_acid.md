---
layout: default
title: Ursodeoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 952
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: From Its Approved Use to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a hydrophilic bile acid marketed in Canada, but the supplied data does not state its original approved indication.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**.
This is a model prediction only: **0 clinical trials** and **0 publications** currently support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.86% (model rank 3386) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, UDCA is a hydrophilic bile acid. Its original indication is not recorded in the supplied data, so no direct link between the original and predicted indications can be drawn.

One plausible but unverified explanation is that UDCA may modestly reduce intestinal cholesterol absorption and hepatic cholesterol synthesis. It may also influence bile acid signaling (FXR/TGR5). The very high TxGNN score may simply reflect closeness between bile acid and cholesterol metabolism in the knowledge graph, rather than a real therapeutic effect.

There is also a mechanistic caution. Homozygous familial hypercholesterolemia is caused mainly by loss of LDL receptor function, or by defects in APOB, PCSK9 or LDLRAP1. Any LDL-lowering effect that relies on LDL receptor upregulation would therefore probably be limited in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage form and approved indication text are not available for these authorizations. Five of the 8 authorizations are shown.

| DIN | Product Name |
|---------|------|
| 02273500 | PMS-URSODIOL C |
| 02544024 | NRA-URSODIOL |
| 02426919 | GLN-URSODIOL |
| 02472392 | JAMP-URSODIOL |
| 02544032 | NRA-URSODIOL |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no registered trials or publications. The expected mechanism (LDL receptor-dependent LDL lowering) is also doubtful in a disease defined by LDL receptor loss.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (e.g., from DrugBank) to test the proposed link to cholesterol metabolism
- Approved indication text for the Canadian products, to establish the original-to-new indication relationship
- Supporting evidence, such as preclinical or early clinical data on LDL-cholesterol lowering in homozygous familial hypercholesterolemia
- A route and formulation compatibility assessment, which is currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

