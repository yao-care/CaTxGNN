---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 811
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

Using the evidence pack as provided — no invented facts, all gaps stated plainly.

# Tyrosine: From Original Indication Not Available to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine (DrugBank DB00135) is an amino acid for which the evidence pack contains no recorded original indication, no mechanism-of-action data, and no Canadian marketing authorization. The TxGNN model's top-ranked prediction is **Cauda Equina Syndrome**, but this is supported by **0 clinical trials** and only **1 unrelated case report**, and the pack's own rationale states there is no credible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no data in `original_indications` or `taiwan_regulatory.licenses`) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Mechanism-of-action data for Tyrosine is not available in this evidence pack (flagged as a High-severity data gap), and no original indication is on file, so the usual comparison between "original use" and "predicted use" cannot be made here.

More importantly, the evidence pack's own assessment of this specific prediction concludes it is **not** reasonable: *"無可信機轉關聯；唯一文獻與馬尾症候群或酪胺酸治療無關（為透明細胞肉瘤/神經鞘瘤案例報告）"* — i.e., there is no credible mechanistic link, and the single supporting publication is a case report about clear cell sarcoma/schwannoma at the S1 nerve root, unrelated to tyrosine treatment or cauda equina syndrome management.

This pattern is consistent across the other nine TxGNN-predicted indications for Tyrosine in this pack (see Conclusion below): several (hyperthyroidism, POTS) are driven by literal name-overlap between "Tyrosine" and unrelated "Tyrosine Kinase Inhibitor" drugs, and others are mechanistically implausible or directionally opposite to the proposed indication. This candidate should be treated as a low-confidence knowledge-graph signal, not a validated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical focus | Case of clear cell sarcoma originating at the S1 nerve root, previously misdiagnosed as schwannoma; a spinal tumor case report, not a study of tyrosine treatment or cauda equina syndrome management. |

## Canada Market Information

No DIN records found. `taiwan_regulatory` data indicates Tyrosine is not currently marketed as an approved drug product in Canada (0 total licenses).

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are available in this evidence pack; the TFDA/Health Canada label data gap is flagged as Blocking, meaning safety cannot be formally assessed at this stage.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The featured prediction (cauda equina syndrome) has an L5 evidence level — no clinical trials and a single unrelated case report — and the evidence pack's own mechanistic rationale explicitly rejects a credible link.
- This is not an isolated issue: all 10 TxGNN-predicted indications for Tyrosine in this pack are scored "Hold" at decision stage S0. Several (hyperthyroidism, POTS) appear driven by name confusion between "Tyrosine" (amino acid) and unrelated "Tyrosine Kinase Inhibitor" drugs; others (hyperthyroidism, hyperthyroxinemia) are mechanistically directionally opposite to the proposed therapeutic use, since tyrosine is a biosynthetic precursor of thyroid hormone rather than a treatment for hyperthyroid states.
- A Blocking data gap exists for TFDA/Health Canada label warnings and contraindications (DG001), and a High-severity gap exists for mechanism of action (DG002), so no candidate from this pack can proceed to safety review (S1) as-is.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/Health Canada label warnings and contraindications) and DG002 (mechanism of action) before any candidate advances past S0.
- Disambiguate the knowledge-graph entity for "Tyrosine" to ensure it is not conflated with "Tyrosine Kinase Inhibitor" drug-class evidence in future predictions.
- If pursuing further, identify indications with genuine mechanistic plausibility and re-query literature/trials specifically for tyrosine (not TKI) interventions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

