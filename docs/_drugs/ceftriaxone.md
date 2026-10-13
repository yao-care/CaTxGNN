---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ceftriaxone: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftriaxone is a third-generation injectable cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, meningitis, gonorrhea and salmonellosis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction.
The more credible signals among the other predictions are for otitis media, which largely overlaps with ceftriaxone's existing antibacterial use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, bacterial meningitis, gonorrhea, salmonellosis (the Canadian licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ceftriaxone is a bactericidal beta-lactam antibiotic with proven efficacy in a broad range of bacterial infections.

For the top-ranked prediction, polyclonal hyperviscosity syndrome, no plausible mechanistic link could be identified. This condition is a protein- or immunoglobulin-driven rheologic disorder, not an infection. The high TxGNN score reflects a network-based association only and is not backed by clinical or literature evidence.

The other predictions differ in plausibility:
- **Infectious otitis media (rank 4):** Strong fit. Ceftriaxone is active against the main causative pathogens (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*). However, this is largely an existing, guideline-recognized use (typically a single intramuscular dose) rather than a novel repurposing.
- **Suppurative otitis media (rank 6):** Plausible antibacterial rationale, supported by one old clinical comparison in the acute setting.
- **Chronic otitis media (rank 7):** Indirect evidence only. Biofilms and *Pseudomonas* limit the usefulness of systemic ceftriaxone, and topical therapy is first-line.
- **Hyperamylasemia, congenital analbuminemia, blood group incompatibility (ranks 2, 3, 5):** No therapeutic link. Some of these point to safety concerns instead, such as biliary sludge and pancreatitis, altered albumin binding, and fetal or neonatal gallstones.

## Clinical Trial Evidence

Currently no clinical trials are registered for the top-ranked prediction (polyclonal hyperviscosity syndrome).

For reference, the only registered trial found among the other predictions (infectious otitis media) does not test ceftriaxone:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | Not applicable | Completed | 250 | Tympanostomy tubes vs non-surgical management in children with recurrent acute otitis media; a device/surgical trial, so it gives no direct evidence on ceftriaxone |

## Literature Evidence

Currently no related literature is available for polyclonal hyperviscosity syndrome.

The most relevant publications for the closest-fitting prediction (infectious otitis media) are listed below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | Pediatrics | Single intramuscular ceftriaxone dose compared with 10 days of oral trimethoprim-sulfamethoxazole in acute otitis media |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus recommendations | Clinical Pediatrics | Consensus recommendations for managing acute otitis media |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clinical Therapeutics | Review of antimicrobial treatment recommendations for acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical study | Pediatric Infectious Disease Journal | One-day vs three-day intramuscular ceftriaxone for nonresponsive acute otitis media in children |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical study | Pediatric Infectious Disease Journal | Bacteriologic efficacy of a three-day intramuscular ceftriaxone regimen in nonresponsive acute otitis media |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | Int J Pediatr Otorhinolaryngol | Use patterns of ceftriaxone for acute otitis media in US primary care; raises stewardship and resistance concerns |
| [2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) | 1989 | Clinical study | Japanese Journal of Antibiotics | Ceftriaxone 1 g once daily vs cefotiam in acute suppurative otitis media; efficacy 71% vs 86% |
| [6301365](https://pubmed.ncbi.nlm.nih.gov/6301365/) | 1983 | Clinical study | Antimicrob Agents Chemother | Ceftriaxone in 50 adults with serious bacterial infections; favourable responses in 34 of 37 infections |

## Canada Market Information

Thirteen valid single-ingredient licences are on record. The compiled data contain no dosage form or approved indication text for them. Five are listed below:

| DIN | Product Name |
|---------|------|
| 02325632 | Ceftriaxone Sodium for Injection BP |
| 02409968 | Ceftriaxone for Injection |
| 02325616 | Ceftriaxone Sodium for Injection BP |
| 02292270 | Ceftriaxone Sodium for Injection BP |
| 02499738 | Ceftriaxone Injection, USP |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver disease, gallbladder disease, neonatal jaundice, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and hemolytic anemia.
- **Drug Interactions:** 100 interactions were identified in total.
  - **Major:** calcium chloride, calcium glucoheptonate, calcium gluconate.
  - **Moderate:** kanamycin, neomycin, streptomycin, picosulfuric acid.
  - Many other listed interactions have an unclassified severity level.
- **Context-specific concerns:** ceftriaxone is highly albumin-bound, so low albumin states could change its pharmacokinetics. It is also associated with biliary sludge, gallstones and pancreatitis. For otitis media, stewardship concerns about overuse apply.

Please refer to the package insert for the full set of warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, polyclonal hyperviscosity syndrome, has no mechanistic link, no trials and no literature (evidence level L5). Of the other predictions, infectious otitis media (L3) is the only one that could proceed with guardrails, but it is an existing guideline-recognized use rather than a new repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data to support or refute any biological link to the predicted condition
- Health Canada package insert warnings, contraindications and approved indication text for the 13 licences
- For polyclonal hyperviscosity syndrome, mechanistic or preclinical evidence before any clinical consideration
- If pursuing otitis media, a decision on whether it counts as new repurposing, and a review of the evidence against current antimicrobial stewardship guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

