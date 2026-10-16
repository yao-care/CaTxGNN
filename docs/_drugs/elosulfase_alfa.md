---
layout: default
title: Elosulfase Alfa
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Elosulfase Alfa: predicted new indication Scheie syndrome (evidence level L5). Approved use: Mucopolysaccharidosis (MPS IVA, Morquio A syndrome)"
---

# Elosulfase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Elosulfase Alfa: From Mucopolysaccharidosis to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa is an enzyme replacement therapy originally used to treat mucopolysaccharidosis (specifically MPS IVA, Morquio A syndrome).
The TxGNN model predicts it may be effective for **Scheie syndrome**, but there are currently **no clinical trials and no publications** supporting this specific prediction.
The score reflects network proximity within the MPS disease family, not demonstrated efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis (MPS IVA, Morquio A syndrome) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, elosulfase alfa replaces the enzyme N-acetylgalactosamine-6-sulfatase (GALNS), which breaks down keratan sulfate and chondroitin-6-sulfate. Its efficacy in MPS IVA is established.

Scheie syndrome (attenuated MPS I) is caused by a deficiency of a different enzyme, alpha-L-iduronidase. This leads to accumulation of dermatan sulfate and heparan sulfate, not the substrates that elosulfase alfa acts on. The two diseases therefore have different enzyme defects and different substrates. The only shared feature is that both are lysosomal storage disorders treated by enzyme replacement.

The high TxGNN score most likely reflects the closeness of these diseases within the MPS family in the knowledge graph, rather than a shared enzymatic mechanism. The prediction is plausible only as a class-level association and is not mechanistically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Scheie syndrome.

For context, the next-ranked prediction, Hurler syndrome (severe MPS I), has one registered trial: [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) (PEARL), a Phase 1 trial of prenatal enzyme replacement for lysosomal storage disorders (recruiting, 10 participants). It is an early safety study, the enzymes tested are likely disease-specific, and it does not show elosulfase alfa efficacy in MPS I.

---

## Literature Evidence

Currently no related literature available for Scheie syndrome.

The literature retrieved for other predicted indications concerns almost entirely Morquio A syndrome (MPS IVA), the original indication. It supports the existing use and not a new one. Key examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24810369](https://pubmed.ncbi.nlm.nih.gov/24810369/) | 2014 | RCT | J Inherit Metab Dis | Phase 3 randomised placebo-controlled study of elosulfase alfa in Morquio A syndrome |
| [25284089](https://pubmed.ncbi.nlm.nih.gov/25284089/) | 2015 | RCT | Mol Genet Metab | Multi-domain impact of elosulfase alfa in the pivotal Phase 3 trial |
| [27380995](https://pubmed.ncbi.nlm.nih.gov/27380995/) | 2016 | Cohort | Mol Genet Metab | Long-term endurance and safety over 96 weeks in a Phase 3 extension study |
| [41088244](https://pubmed.ncbi.nlm.nih.gov/41088244/) | 2025 | Review | Orphanet J Rare Dis | Recent advances in MPS IVA treatment; ERT is currently the only approved therapy |
| [42363262](https://pubmed.ncbi.nlm.nih.gov/42363262/) | 2026 | Cohort | Orphanet J Rare Dis | Long-term follow-up and response to elosulfase alfa in a Czech MPS IVA cohort |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02427184 | VIMIZIM | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Scheie syndrome prediction has no clinical trials or publications behind it (L5). Elosulfase alfa targets GALNS and its substrates, whereas Scheie syndrome involves alpha-L-iduronidase deficiency and different substrates, so there is no direct mechanistic rationale. Other top predictions are either the original indication (MPS IVA) or are unsupported by mechanism or evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Detailed mechanism-of-action data
- Preclinical evidence on whether GALNS replacement has any effect on dermatan sulfate or heparan sulfate accumulation
- Any clinical or literature evidence of elosulfase alfa use in MPS I; established MPS I enzyme therapy (alpha-L-iduronidase replacement) should be the comparator
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

