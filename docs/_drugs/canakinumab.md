---
layout: default
title: Canakinumab
parent: Model Prediction Only (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Autoinflammatory Periodic Fever Syndromes to Hepatic Infarction

## One-Sentence Summary

Canakinumab (marketed in Canada as ILARIS) is an anti-IL-1β antibody. The literature in the Evidence Pack describes its use in cryopyrin-associated periodic syndrome (CAPS) and related autoinflammatory diseases.
The TxGNN model ranks **hepatic infarction** as its top prediction, but **0 clinical trials** and only **1 unrelated publication** support it, so this looks like a model artifact rather than a real lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence record. Literature describes CAPS and other periodic fever syndromes. |
| Predicted New Indication | Hepatic infarction |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Canakinumab neutralizes interleukin-1β (IL-1β), which suppresses inflammation in diseases driven by IL-1β overproduction. Detailed mechanism-of-action data is not available in the Evidence Pack. This description comes from the retrieved literature, not from a structured MOA record.

The prediction is **not** mechanistically convincing. Hepatic infarction is an ischemic or vascular event, and IL-1β blockade has no established role in treating it. The high TxGNN score (99.86%) is most likely a knowledge-graph artifact, not a genuine repurposing signal. The only retrieved publication is a cardiovascular prevention trial of a different drug, bempedoic acid, which says nothing about canakinumab in liver ischemia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37354546](https://pubmed.ncbi.nlm.nih.gov/37354546/) | 2023 | RCT | JAMA | Bempedoic acid for primary prevention of cardiovascular events in statin-intolerant patients. It does not involve canakinumab or hepatic infarction, so it offers no support for this prediction. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2460351 | ILARIS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, no relevant literature and no plausible IL-1β mechanism in hepatic infarction. Evidence Level L5 does not justify further investment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing, and blocking any safety screening)
- Structured mechanism-of-action data from DrugBank
- Any preclinical or clinical evidence linking IL-1β signalling to hepatic ischemic injury

**Note on other predictions:** Other predictions for canakinumab are far better supported and deserve separate evaluations:
- **Familial Mediterranean fever** (rank 6): Evidence Level L2, with Phase 2/3 trials and disease-specific literature in colchicine-resistant patients. It is currently rated "Proceed with Guardrails". Several of the retrieved trials appear to be CAPS studies, so their populations must be verified.
- **Blau syndrome** (rank 8): Evidence Level L3, with a small study reporting clinical response to canakinumab plus case reports.
- **Periodic fever-infantile enterocolitis-autoinflammatory syndrome** (rank 5): Evidence Level L4. The literature is indirect and covers related periodic fever syndromes.

This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

