---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line antitubercular prodrug, standardly used as part of combination therapy against *Mycobacterium tuberculosis* infection. The TxGNN model predicts it may be effective for **Infectious Otitis Media**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-based association with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (antitubercular combination therapy) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal, sourced mechanism-of-action documentation (e.g., a DrugBank MOA record) is currently a data gap. Based on the pharmacological description embedded in this evidence pack's own analysis, pyrazinamide is a prodrug converted by bacterial pyrazinamidase into pyrazinoic acid, which is bactericidal against *Mycobacterium tuberculosis* specifically in the acidic intracellular environment of granulomas and phagolysosomes. This is a narrow-spectrum, pathogen-specific mechanism rather than a general anti-infective or anti-inflammatory action.

For the top-ranked prediction, "Infectious Otitis Media," no clinical trial or literature evidence links pyrazinamide to this indication directly — the model's high score is not corroborated by any real-world data for this specific disease label.

Notably, several closely related sibling predictions in this same evidence pack (middle ear disease, chronic otitis media, suppurative otitis media, infectious otitis interna) *do* carry supporting literature — but that literature consists exclusively of case reports and small case series describing **tuberculous otitis media (TOM)**, a rare extrapulmonary manifestation of tuberculosis treated with the standard four-drug anti-TB regimen (including pyrazinamide). This is mechanistically informative but is not equivalent to a novel repurposing signal: it reflects pyrazinamide treating an existing TB infection that happens to present in the ear, not a new pharmacological application against non-tuberculous otitis media. Whether "Infectious Otitis Media" as coded here refers to TB-related or general bacterial otitis media is itself unresolved and should be clarified before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction ("Infectious Otitis Media") has no clinical trial or literature support (L5, model prediction only), and the drug is not currently marketed in Canada. While sibling predictions in this evidence pack show case-report-level evidence for tuberculous otitis media, that evidence describes existing TB treatment rather than a genuine new indication, and does not directly substantiate this specific prediction.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently blocking (DG001)
- Verified mechanism-of-action documentation from DrugBank or equivalent primary source (DG002)
- Targeted literature/trial search to clarify whether "Infectious Otitis Media" refers to tuberculous or general bacterial etiology
- If tuberculous etiology is confirmed, reclassify this as an extrapulmonary-TB treatment context rather than a novel repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

