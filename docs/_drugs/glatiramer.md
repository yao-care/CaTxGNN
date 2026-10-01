---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Glatiramer
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer is an immunomodulator used to treat multiple sclerosis (MS). The TxGNN model predicts it may be effective for **hemoglobinopathy**, but this is a graph-based prediction with **0 clinical trials** and only **1 loosely related publication**. The available evidence does not support the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (the Canadian license records contain no indication text; MS is taken from the drug's known use) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Glatiramer is known as an immunomodulator for MS, and its Th2-shifting and regulatory T-cell effects are the usual explanation for its benefit there.

Hemoglobinopathies are inherited disorders of globin structure or production, such as beta-thalassemia. Nothing in glatiramer's immunomodulatory action addresses defective globin synthesis, so **no plausible mechanistic link was identified**. The high TxGNN score likely reflects network proximity in the knowledge graph rather than supporting biology.

The other top-ranked predictions show the same pattern. They include plasma cell myeloma, beta-thalassemia, red-cell enzyme and membrane disorders, and gastric linitis plastica. All have no trials and no mechanistic support. Female breast carcinoma is the only one with several publications, and those are epidemiological studies of cancer risk in MS patients on disease-modifying therapies. They address safety, not anti-tumor efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Review (classified); content is a single case report | Revue neurologique | Describes a 35-year-old MS patient with a history of beta-thalassemia who developed multiple immune disorders after stopping natalizumab. It does not test glatiramer in hemoglobinopathy, so it is not evidence of efficacy. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2245619 | COPAXONE |
| 2456915 | COPAXONE |
| 2460661 | GLATECT |
| 2541440 | GLATIRAMER ACETATE INJECTION |

Dosage form, manufacturer and approved indication text are not recorded for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, no mechanistic rationale, and the single publication is an unrelated MS case report. Glatiramer is marketed in Canada for its original use, but nothing supports moving it toward hemoglobinopathy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank) to test whether any biological link to globin disorders exists
- Preclinical or clinical evidence in hemoglobinopathy, none of which currently exists
- Confirmation of the approved indication text for the four Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

