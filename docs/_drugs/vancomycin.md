---
layout: default
title: Vancomycin
parent: Moderate Evidence (L3-L4)
nav_order: 819
evidence_level: L3
indication_count: 10
---

# Vancomycin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Vancomycin: From Gram-Positive Infections to Streptococcal Pneumonia

## One-Sentence Summary

> Vancomycin is a glycopeptide antibiotic established for treating Gram-positive bacterial infections, including MRSA, by inhibiting bacterial cell wall synthesis.
> Of the **10 TxGNN-predicted indications** evaluated in this pack, only **Streptococcal Pneumonia** carries a mechanistically credible rationale and a "Proceed with Guardrails" recommendation — the remaining 9 candidates (including the top-ranked TxGNN score, diffuse scleroderma) are flagged as mechanistically implausible or lack any supporting evidence and are recommended **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No license record available (Vancomycin is not marketed in Canada). Trial evidence (NCT05395520) confirms established use for Gram-positive bacterial infections, including MRSA |
| Predicted New Indication | Streptococcal Pneumonia (selected as the only mechanistically supported candidate among the 10 screened; see note below) |
| TxGNN Prediction Score | 99.60% (rank 7899 of candidate pool) |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** This evidence pack screened 10 TxGNN-predicted indications for Vancomycin. The literal top-ranked prediction (diffuse scleroderma, score 99.92%) is explicitly annotated in the evidence pack as lacking any mechanistic link and is recommended **Hold** — it is presented here for transparency in the Screening Overview table below rather than as the headline indication.

### Screening Overview of All 10 Candidates

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Reason |
|------|---------|------------|-----------------|-----------------|--------|
| 1 | Diffuse scleroderma | 99.92% | L5 | Hold | No mechanistic link (autoimmune fibrosis, unrelated to cell-wall inhibition) |
| 2 | Paratyphoid fever | 99.85% | L4 | Hold | Gram-negative pathogen — outer membrane blocks vancomycin |
| 3 | Salmonellosis | 99.81% | L4 | Hold | Gram-negative pathogen — no antibacterial activity |
| 4 | Congenital analbuminemia | 99.79% | L5 | Hold | No mechanistic link; no evidence |
| 5 | Polyclonal hyperviscosity syndrome | 99.79% | L5 | Hold | No mechanistic link; no evidence |
| 6 | Hyperamylasemia | 99.79% | L5 | Hold | Lab abnormality, not a disease entity; no mechanistic link |
| 7 | Typhoid fever | 99.75% | L4 | Hold | Gram-negative pathogen — no antibacterial activity |
| 8 | Blood group incompatibility | 99.63% | L5 | Hold | No mechanistic link; immune transfusion reaction |
| **9** | **Streptococcal pneumonia** | **99.60%** | **L3** | **Proceed with Guardrails** | Gram-positive pathogen — mechanistically consistent with existing PRSP guideline use |
| 10 | Premalignant hematological disease | 99.54% | L5 | Hold | No mechanistic link; no evidence |

---

## Why is This Prediction Reasonable?

The official DrugBank mechanism-of-action field for Vancomycin currently has a data gap (High severity, DG002). However, the evidence pack's repurposing rationale — consistently repeated across multiple candidate evaluations — describes Vancomycin as a **glycopeptide antibiotic** that inhibits **D-Ala-D-Ala** cell wall precursor synthesis in Gram-positive bacteria, leading to bactericidal activity. This is corroborated by a clinical trial record (NCT05395520) noting Vancomycin's "broad gram-positive coverage" and use "from streptococcal to methicillin-resistant Staphylococcus aureus (MRSA) infections."

*Streptococcus pneumoniae* is a Gram-positive organism, placing it squarely within Vancomycin's known spectrum of activity. Unlike the other 8 rejected candidates in this screen — most of which involve Gram-negative pathogens (Salmonella, S. typhi) whose outer membrane blocks vancomycin penetration, or conditions with no plausible link to antibacterial mechanisms at all — Streptococcal Pneumonia represents a mechanistically coherent extension.

Importantly, the repurposing rationale notes this is **not a novel indication** but reflects existing clinical guideline use: Vancomycin is already used empirically for penicillin/cephalosporin-resistant *S. pneumoniae* (PRSP) infections, particularly in meningitis. The TxGNN signal here largely reconfirms established practice rather than identifying a genuinely new use, which is why the evidence level is capped at L3 (no direct interventional trial in this dataset targets Vancomycin vs. S. pneumoniae specifically).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05395520](https://clinicaltrials.gov/study/NCT05395520) | N/A | Unknown | 146 | Evaluates whether AUC-based therapeutic drug monitoring for Vancomycin is appropriate beyond serious MRSA infections; confirms drug's broad Gram-positive coverage including streptococcal infections (Relevance: B) |
| [NCT04464291](https://clinicaltrials.gov/study/NCT04464291) | N/A | Completed | 500 | Epidemiological survey of circulating *S. pneumoniae* serotypes in Russia; no Vancomycin intervention (Relevance: C) |
| [NCT02538211](https://clinicaltrials.gov/study/NCT02538211) | N/A | Completed | 63 | Intestinal microbiome effects on rotavirus vaccine immune response; no direct relevance to Vancomycin/S. pneumoniae treatment (Relevance: C) |

None of the listed trials directly test Vancomycin as an interventional treatment for streptococcal pneumonia.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Vancomycin currently holds **no marketing authorization in Canada** (0 total licenses, market status: Not Marketed). No DIN records are available for this evidence pack.

## Safety Considerations

A **Blocking-severity data gap (DG001)** has been identified: TFDA/product label warnings and contraindications for Vancomycin are not yet available in this evidence pack, which prevents completion of the S1 safety pre-assessment. Drug-drug interaction data was also queried with no results found (0 interactions).

Please refer to the package insert for detailed safety information once available; do not proceed to clinical decision-making without resolving this gap.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (applies specifically to Streptococcal Pneumonia; all other 9 screened candidates are **Hold**)

**Rationale:**
Streptococcal pneumonia is the only candidate in this batch with a biologically coherent mechanistic link to Vancomycin's known spectrum of activity, and it aligns with existing clinical guideline use for PRSP rather than representing a speculative new indication. However, no direct interventional trial evidence exists in this dataset, and a Blocking safety data gap prevents full S1 evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/manufacturer label data (warnings, contraindications) to complete S1 safety pre-assessment
- Resolve DG002 (High): confirm official DrugBank MOA reference
- Identify direct interventional evidence (e.g., guideline citations or trials) specifically evaluating Vancomycin in PRSP pneumonia/meningitis
- Given 0 DINs in Canada, assess regulatory pathway/market access feasibility before any further development
- No further action recommended on the remaining 9 candidates (diffuse scleroderma, paratyphoid fever, salmonellosis, congenital analbuminemia, polyclonal hyperviscosity syndrome, hyperamylasemia, typhoid fever, blood group incompatibility, premalignant hematological disease) absent new mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

