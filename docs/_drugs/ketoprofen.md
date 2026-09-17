---
layout: default
title: Ketoprofen
parent: Moderate Evidence (L3-L4)
nav_order: 434
evidence_level: L4
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From NSAID Pain/Inflammation Use to Spondyloarthropathy

## One-Sentence Summary

Ketoprofen is a classic propionic-acid NSAID with no formal original-indication text on file in this evidence pack. Among 10 TxGNN-predicted indications, only one — **Spondyloarthropathy (susceptibility to)** — has any supporting literature; it scores **99.86%** and is backed by **1 review-level publication**, while the remaining 9 candidates are unsupported and largely implausible mechanistically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (no `original_indications` or license data available). Ketoprofen is generally known as a propionic-acid NSAID used for pain/inflammation. |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record (flagged as a High-severity data gap, DG002). Based on known pharmacology, however, ketoprofen is a conventional non-selective NSAID that inhibits COX-1/COX-2, reducing prostaglandin synthesis and producing systemic anti-inflammatory and analgesic effects.

Spondyloarthropathies — including reactive arthritis (Fiessinger-Leroy-Reiter syndrome) — present with joint swelling, morning stiffness, and enthesitis, all of which are standard indications for NSAID symptom control. This is therefore best understood as a **drug-class-level extension** of ketoprofen's known anti-inflammatory activity rather than a novel mechanistic hypothesis.

It's worth noting that 8 of the other 9 top-10 TxGNN predictions for this drug (e.g., acromesomelic dysplasia, brachyolmia, WHIM syndrome, pseudoachondroplasia) are rare monogenic skeletal or developmental disorders with no inflammatory basis and no supporting trials or literature — these are annotated in the source data as likely noise from sparse knowledge-graph connectivity for orphan diseases. The one partial exception, juvenile arthritis due to LACC1 defect (rank 10, L4/S1, "Research Question"), shares an inflammatory joint mechanism but lacks any direct evidence and involves a pediatric population with limited ketoprofen safety data. This report focuses on spondyloarthropathy as the only candidate with both a plausible mechanism and cited evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20470931](https://pubmed.ncbi.nlm.nih.gov/20470931/) | 2010 | Review | Annales de dermatologie et de venereologie | Review of reactive arthritis (Fiessinger-Leroy-Reiter syndrome); abstract text not available in this evidence pack |

---

## Canada Market Information

Ketoprofen is currently not marketed in Canada under this record — no DIN or product license data is available (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently on file; product-monograph retrieval is tracked as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single review-level publication supports NSAID use in reactive arthritis/spondyloarthropathy, consistent with ketoprofen's established drug-class role — but this reflects existing NSAID practice rather than new evidence, and no clinical trials specific to this indication exist. Combined with the drug's "not marketed" status in Canada and missing label/safety data, guardrails are warranted before any further action.

**To proceed, the following is needed:**
- Health Canada product monograph / label data (key warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Controlled clinical evidence (RCT or cohort study) specific to spondyloarthropathy/reactive arthritis, since current support is limited to one review article
- A market-authorization assessment, given the drug currently has zero DINs in Canada
- Continued monitoring of the LACC1-related juvenile arthritis signal (rank 10) as a lower-priority research question, pending pediatric safety data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

