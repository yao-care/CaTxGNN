---
layout: default
title: Indomethacin
parent: High Evidence (L1-L2)
nav_order: 403
evidence_level: L2
indication_count: 10
---

# Indomethacin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Indomethacin: From Inflammatory Pain Conditions to Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Indomethacin is a classic non-selective COX-1/COX-2 inhibitor traditionally used for inflammatory and rheumatic pain conditions. Among the 10 TxGNN-predicted indications in this evidence pack, the top-ranked candidates (e.g., brachydactyly-syndactyly syndrome) are congenital/structural disorders with no biological plausibility and zero supporting evidence — the model itself flags them as noise. This report instead focuses on **Juvenile Idiopathic Arthritis (JIA)**, ranked #8 by TxGNN score, which is the only candidate backed by a mechanistically coherent rationale, an indomethacin-specific RCT, and **20 supporting publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured as structured data in this evidence pack; indomethacin is generically known as an NSAID for inflammatory/rheumatic pain |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.84% (rank 3794 of full candidate list) |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, indomethacin is a potent non-selective NSAID that inhibits COX-1/COX-2, reducing prostaglandin synthesis and producing systemic anti-inflammatory and analgesic effects.

JIA is a chronic inflammatory arthritis of childhood driven by synovial inflammation — the same pathological process NSAIDs are designed to target. The evidence pack's own repurposing rationale for this candidate describes it as "a classic NSAID mechanism for treating arthritis, not a novel hypothesis," which is consistent with the fact that indomethacin already has a documented history of off-label/established use in juvenile rheumatic disease dating back to the 1960s–1990s literature below.

In other words, TxGNN is not proposing a speculative new mechanism here — it is re-discovering a pharmacologically well-grounded, historically supported use. This stands in contrast to the model's top-ranked predictions for this drug (e.g., congenital skeletal dysplasias), which the evidence pack explicitly scores as Evidence Level L5 with a "Hold" recommendation due to lack of any inflammatory component.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT | S Afr Med J | Double-blind crossover trial in 30 children with juvenile chronic arthritis; indomethacin and ketoprofen both effective, with indomethacin the preferred agent and few mild side effects |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | Unclassified | Arzneimittel-Forschung | Long-term indomethacin therapy specifically in juvenile rheumatoid arthritis and Still's disease (abstract not available) |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Unclassified | Br J Rheumatol | Reviews NSAID use in paediatric rheumatic disease; indomethacin and salicylates used for fever control in systemic JCA, noted as no more effective but more toxic than newer agents |
| [4678956](https://pubmed.ncbi.nlm.nih.gov/4678956/) | 1972 | Unclassified | JAMA | Commentary specifically on indomethacin (abstract not available) |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Review | Drugs | Review of JRA pharmacotherapy; indomethacin listed among NSAIDs used to control synovitis, pain, and systemic inflammation |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Review | Balkan Med J | Overview of JIA subtypes, clinical features, treatment modalities, and prognosis |
| [22573189](https://pubmed.ncbi.nlm.nih.gov/22573189/) | 2012 | Review | Swiss Med Wkly | Review of systemic-onset JIA (Still's disease), its clinical course and response to conventional therapy |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Unclassified | Clin Pharmacokinet | Review of clinical pharmacokinetics of NSAIDs and other drugs used in juvenile arthritis |
| [28086918](https://pubmed.ncbi.nlm.nih.gov/28086918/) | 2017 | Cohort | Pediatr Rheumatol Online J | Case series of atypical monoarthritis presentations in oligoarticular JIA outside the knees/ankles |
| [7417361](https://pubmed.ncbi.nlm.nih.gov/7417361/) | 1980 | Cohort | Arthritis Rheum | Comparative cohort of JRA patients in USSR vs. USA showing similar disease course despite differing NSAID/aspirin-based treatment approaches |

---

## Canada Market Information

Indomethacin currently has no DIN license records in this evidence pack — the drug is not marketed in Canada (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are marked as Blocking-severity data gaps — DG001 — and must be obtained from the official label before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The JIA candidate has a mechanistically coherent rationale, an indomethacin-specific RCT, and a substantial historical literature base (L2 evidence, decision stage S3) — unlike the model's top-scored candidates, which are unsupported structural/congenital syndromes correctly flagged as noise (L5, Hold). However, a Blocking-severity gap (DG001: TFDA/label warnings and contraindications unavailable) means this candidate cannot yet pass safety pre-screening (S1), and the drug is currently unmarketed in Canada.

**To proceed, the following is needed:**
- Official product label / TFDA safety data (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- A defined Canadian market-entry or licensing pathway, since no DIN currently exists
- Drug interaction (DDI) data, currently unavailable (`query_status: not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

