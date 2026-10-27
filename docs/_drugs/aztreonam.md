---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Aztreonam: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, Pseudomonas aeruginosa infection…"
monitor_inn: "AZTREONAM"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Aztreonam: From Urinary Tract Infection to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used to treat Gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, and endometritis.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting it, so this prediction is regarded as a model artifact.
A more plausible direction is **gonococcal urethritis** (rank 5), which has **6 publications**, including one 2020 single-arm open-label trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, rhinoscleroma, Escherichia coli infection, endometritis (the Canadian licence record has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, aztreonam is a monobactam that inhibits penicillin-binding protein 3 in aerobic Gram-negative bacteria. It has proven efficacy in Gram-negative infections such as urinary tract infection.

For the top prediction, **polyclonal hyperviscosity syndrome**, there is no plausible mechanistic link. It is a protein/immunoglobulin disorder rather than an infection, and the high score (99.73%) appears to be a graph-based artifact. The same applies to the other non-infectious predictions: hyperamylasemia, congenital analbuminemia, and premalignant hematological system disease.

Some lower-ranked predictions are biologically more reasonable because they involve Gram-negative bacterial infections:
- **Gonococcal urethritis** (rank 5): *Neisseria gonorrhoeae* is a Gram-negative diplococcus, so the mechanism is plausible. Early studies and a 2020 trial reported single-dose efficacy. However, aztreonam-resistant strains have emerged, and no randomized evidence exists.
- **Epiglottitis** (rank 8): often caused by *Haemophilus influenzae* type b, which is susceptible. The evidence is indirect, and established first-line agents make it a low priority.
- **Xanthogranulomatous pyelonephritis** (rank 10): an extension of the existing urinary tract infection indication, with no direct studies.
- **Ureaplasma urethritis** (rank 4) is mechanistically contradicted, because Ureaplasma has no cell wall and beta-lactams are expected to be ineffective.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (polyclonal hyperviscosity syndrome), and none for any of the other top 10 predictions.

## Literature Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), currently no related literature is available.

For reference, the most relevant publications among lower-ranked predictions are listed below. They concern **gonococcal urethritis** unless stated otherwise.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single-dose intramuscular aztreonam 2 g tested as a new gonorrhoea regimen amid concern over ceftriaxone resistance |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM: no failures with either drug in uncomplicated gonorrhoea |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical study | Genitourin Med | Single 1 g IM dose cleared infection in 61 men and 26 women, apart from one pharyngeal infection; effective against penicillin-sensitive and resistant strains |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic and therapeutic study | Hinyokika Kiyo | Clinical study of single-dose aztreonam for gonorrhoeal infections, with epidemiologic data |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro/clinical study | J Infect Dis | Aztreonam was effective against penicillin-resistant gonococci |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance surveillance | J Infect Chemother | Emergence of cephem- and aztreonam-highly-resistant, non-β-lactamase-producing *N. gonorrhoeae* |
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Open pediatric study | Am J Dis Child | Aztreonam in 59 children with serious Gram-negative infections (including one epiglottitis case); indirect evidence for epiglottitis |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Clinical study | Jpn J Antibiot | In 90 evaluable patients with hematologic disorders, the efficacy rate was 51.1%; supports treating infections in this population, not monoclonal gammopathy itself |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02329840 | CAYSTON | Not specified | Not specified |

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, bronchial disease.

**Drug Interactions:** 27 interactions were identified in total. Those rated **Moderate** are:
- Picosulfuric acid
- Dicoumarol
- Warfarin

Others, such as pantoprazole, omeprazole, lansoprazole, morphine, vancomycin, hydrocortisone, ondansetron, metronidazole, dexamethasone, amphotericin B, acetylsalicylic acid, heparin, salbutamol, fluconazole, tacrolimus, amikacin, and acyclovir, have an unclassified severity level.

Please refer to the package insert for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, polyclonal hyperviscosity syndrome, has no clinical, literature, or mechanistic support (evidence level L5), and the high TxGNN score appears to be a graph-based artifact. The more credible candidate, gonococcal urethritis (L3, research question), has only small, mostly older, non-randomized studies, and resistance and current guideline regimens limit its practical value.

**To proceed, the following is needed:**
- Mechanism of action data, and the package insert warnings and contraindications from Health Canada
- For gonococcal urethritis, randomized controlled evidence and current resistance surveillance data
- Clarification of the dosage form and approved indication for the Canadian licence (CAYSTON)
- Review of the knowledge-graph contraindications (kidney, liver, and gastrointestinal disease) against the label
- Review of the Moderate-level interactions, especially with warfarin and dicoumarol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

