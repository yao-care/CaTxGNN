---
layout: default
title: Levofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 539
evidence_level: L4
indication_count: 10
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibacterial, originally used to treat bacterial infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 clinical trials** and only **1 publication**, which is an outbreak report that does not support the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (general antibacterial use; Canadian label text not available in the Evidence Pack) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, levofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy against bacterial infections is well established.

In principle, it could help prevent bacterial superinfection of a damaged corneal epithelium. However, the only linked paper concerns microsporidial keratoconjunctivitis. Microsporidia are not bacteria and are not a levofloxacin target, so the paper gives no support for treating this disease. The high TxGNN score is not backed by clinical evidence and is best treated as a model signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Outbreak of microsporidial keratoconjunctivitis linked to swimming pool water contamination in Taiwan. It does not evaluate levofloxacin, and the causative organism is not a levofloxacin target. |

## Canada Market Information

Five of the 17 authorizations are shown below. Dosage form and approved indication text were not provided for these products.

| DIN | Product Name |
|---------|------|
| 2442302 | QUINSAIR |
| 2537079 | LEVOFLOXACIN IN 5% DEXTROSE INJECTION |
| 2298651 | SANDOZ LEVOFLOXACIN |
| 2315440 | TEVA-LEVOFLOXACIN |
| 2298643 | SANDOZ LEVOFLOXACIN |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only linked evidence is an outbreak report on a non-bacterial pathogen, so it gives no clinical support. The high model score is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Evidence that bacterial superinfection contributes to this condition, for example clinical or microbiological studies in ocular surface disease
- Health Canada package insert warnings and contraindications, which are currently missing
- Detailed mechanism of action data from DrugBank
- Route compatibility assessment, since an ophthalmic use would need a suitable formulation

**Note on other predictions for this drug:**
Two other predicted indications in the pack have stronger support and would be better first candidates for a separate evaluation:
- **Monoclonal gammopathy (myeloma infection prophylaxis)**: L1, based on the TEAMM Phase 3 RCT (PMID 31668592). Proceed with Guardrails.
- **Septicemic plague**: L4, based on non-human primate studies. Proceed with Guardrails.

The remaining predictions have no clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

