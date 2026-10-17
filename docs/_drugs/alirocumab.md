---
layout: default
title: Alirocumab
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alirocumab: predicted new indication Ichthyosis, X-linked, without steroid sulfatase deficiency (evidence level L5). Approved use: Dyslipidemia and atherosclerotic disease (syndromic dyslipidemia…"
monitor_inn: "Alirocumab"
predicted_indications: ["ichthyosis, X-linked, without steroid sulfatase deficiency", "disorder of other vitamins and cofactors metabolism and transport", "xanthomatosis (disease)", "46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect", "cholesterol catabolic process disease", "46,XY disorder of sex development due to a cholesterol synthesis defect", "dappled diaphyseal dysplasia", "neutral lipid storage disease", "3-hydroxyacyl-CoA dehydrogenase deficiency", "spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder"]
---

# Alirocumab
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

# Alirocumab: From Dyslipidemia and Atherosclerosis to Ichthyosis, X-linked, without Steroid Sulfatase Deficiency

## One-Sentence Summary

Alirocumab is a PCSK9-inhibiting monoclonal antibody, originally used to lower cholesterol in dyslipidemia and atherosclerotic disease.
The TxGNN model predicts it may be effective for **X-linked ichthyosis (without steroid sulfatase deficiency)**,
but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidemia and atherosclerotic disease (syndromic dyslipidemia, arteriosclerosis disorder, atherosclerosis, arteriolosclerosis); the Canadian licence records contain no indication text |
| Predicted New Indication | Ichthyosis, X-linked, without steroid sulfatase deficiency |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alirocumab is a fully human antibody that binds PCSK9 (proprotein convertase subtilisin/kexin type 9). Blocking PCSK9 increases the number of LDL receptors available on liver cells and lowers circulating LDL cholesterol. Its efficacy in lipid lowering is established.

The link to the predicted indication is weak. X-linked ichthyosis is a skin disorder associated with cholesterol sulfate accumulation. No supported pathway connecting PCSK9 inhibition to this condition is evident from the available data. The high TxGNN score reflects a graph-based association only and should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02453835 | PRALUENT | Not listed | Not listed |
| 02547732 | PRALUENT | Not listed | Not listed |
| 02453819 | PRALUENT | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned one entry, which is a pharmacological target relationship rather than a drug-drug interaction. Alirocumab binds its target, PCSK9 (human). No interacting drugs with a defined severity level were identified.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications for this disease, and the mechanistic link between PCSK9 inhibition and X-linked ichthyosis is speculative.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking PCSK9 inhibition to the pathophysiology of X-linked ichthyosis
- Mechanism of action data and Health Canada package insert warnings and contraindications, to support safety screening
- Route compatibility assessment, since this is a skin disease and alirocumab is a systemic injectable
- Comparison with other predicted indications. For example, xanthomatosis has indirect, case-level literature and a plausible LDL-lowering rationale, and "cholesterol catabolic process disease" has review-level literature, though that largely overlaps with alirocumab's existing lipid-lowering use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

