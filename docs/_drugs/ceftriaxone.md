---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 5
monitor_inn: "CEFTRIAXONE"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-24
description: "Ceftriaxone: predicted new indication polyclonal hyperviscosity syndrome (evidence level L5). In Canada: 13 DINs (13 marketed)"
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ceftriaxone: Third-generation cephalosporin antibiotic → polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Ceftriaxone is an injectable cephalosporin antibiotic that is already marketed in Canada.
The TxGNN model predicts it may be relevant to **polyclonal hyperviscosity syndrome**, with a score of **0.9939**.
The data compiled for this report contain **no clinical trials and no publications** on this prediction, so the evidence is **model prediction only**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 13 of 13) |
| Number of DINs | 13 (marketed: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for ceftriaxone: "Ceftriaxone is an antibacterial drug. […] Ceftriaxone is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftriaxone has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467), label version 2022-01-13; accessed 2026-11-19.) Ceftriaxone is a bactericidal beta-lactam antibiotic that kills bacteria by interfering with cell-wall synthesis.

Polyclonal hyperviscosity syndrome is a different kind of problem. It is a rheologic disorder in which high levels of immunoglobulins or other proteins make the blood abnormally thick. It is not an infection, and an antibacterial would not be expected to act on the cause.

We found **no plausible mechanistic link** between the drug and this condition. The high TxGNN score comes from network-based pattern matching and has no clinical or literature support. It should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02289695 | CEFTRIAXONE FOR INJECTION | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02289709 | CEFTRIAXONE FOR INJECTION | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02292262 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02292270 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02292289 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02292297 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02325594 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02325616 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02325624 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02325632 | CEFTRIAXONE SODIUM FOR INJECTION BP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02409968 | CEFTRIAXONE FOR INJECTION | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02499711 | CEFTRIAXONE INJECTION, USP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |
| 02499738 | CEFTRIAXONE INJECTION, USP | CEFTRIAXONE (CEFTRIAXONE SODIUM) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Ceftriaxone is marketed in Canada as a single-ingredient injectable product. All licences on record are valid, and none are cancelled. The licence table is generated separately by the site program.

## Safety Considerations

- **Drug Interactions** (100 interactions were found in total; the main ones are listed below):
  - **Major:** calcium-containing products (calcium chloride, calcium gluconate, calcium glucoheptonate).
  - **Moderate:** aminoglycosides (kanamycin, neomycin, streptomycin) and picosulfuric acid.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no credible mechanism links an antibacterial to a protein-driven hyperviscosity disorder. At Evidence Level L5, the risks of exposing patients to an antibiotic with no expected benefit outweigh any potential value.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, supported by preclinical or laboratory data
- Any published case-level or observational data on ceftriaxone in this condition
- Detailed mechanism-of-action data for ceftriaxone
- Package insert warnings and contraindications from Health Canada, for a safety review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for ceftriaxone are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

