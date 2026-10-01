---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 834
evidence_level: L5
indication_count: 1
---

# Selinexor
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

# Selinexor: From an Unspecified Original Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Selinexor is marketed in Canada as XPOVIO, but the supplied data does not state its original approved indication.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the original indication list is empty. A mechanistic link between selinexor and drug-induced osteoporosis therefore cannot be established from the supplied data. The TxGNN score of 99.22% reflects a pattern in the knowledge graph, not confirmed biology or clinical findings.

One hypothesis is that selinexor is known as an XPO1 (exportin-1) inhibitor, and nuclear export pathways could influence bone-remodelling signalling. This idea is not supported by any evidence in this dataset and must be verified independently before it is treated as a rationale.

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
| 2527677 | XPOVIO | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Likely targeted therapy (XPO1 inhibitor); DrugBank category data not supplied, so please confirm |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone (Evidence Level L5). There are no registered trials, no publications, no mechanism data and no safety data to support moving forward.

**To proceed, the following is needed:**
- The Health Canada product monograph, including warnings and contraindications, to allow safety screening
- Mechanism of action data from DrugBank, to test whether a link to bone biology is plausible
- A systematic search of ClinicalTrials.gov, ICTRP and PubMed for selinexor and bone loss or osteoporosis
- Preclinical evidence on the effect of selinexor on bone turnover, since the hypothesis above is untested
- Confirmation of the approved indication, dosage form and manufacturer for DIN 2527677

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

