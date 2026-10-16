---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Colistin: predicted new indication Sinusitis (evidence level L5). Approved use: E. coli infection, otitis externa, external ear disease"
monitor_inn: "COLISTIN"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
---

# Colistin
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

# Colistin: From Gram-Negative Infections (E. coli Infection, Otitis Externa) to Sinusitis

## One-Sentence Summary

Colistin is a polymyxin antibiotic, originally used for *Escherichia coli* infection, otitis externa and external ear disease.
The TxGNN model's top-ranked predictions have no supporting evidence, so this report focuses on the best-supported candidate, **sinusitis** (rank 8). It has **0 clinical trials** and **11 publications**, mostly case reports, pharmacokinetic data, reviews and preclinical work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *E. coli* infection, otitis externa, external ear disease (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Sinusitis (the top-ranked prediction, postinfectious vasculitis, has no evidence and no plausible mechanism) |
| TxGNN Prediction Score | 99.25% for sinusitis (99.91% for postinfectious vasculitis, rank 1) |
| Evidence Level | L4 (sinusitis); L5 for the top 6 predictions |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold (sinusitis is a research question, not ready to advance) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Colistin is a polymyxin that disrupts the outer membrane of Gram-negative bacteria. It is a bactericidal agent with activity against *Pseudomonas aeruginosa* and other Gram-negative pathogens.

**The top-ranked predictions are not credible.** The first six (postinfectious vasculitis, post-bacterial disorder, post-infectious syndrome, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome, infective urethral stricture) score above 99.8%, but none has trials or literature. Most are immune-mediated or structural conditions that an antibacterial would not treat. Chagas disease is caused by a protozoan against which colistin has no recognized activity. In infection-related HUS, antibiotics are generally avoided and colistin's nephrotoxicity is a serious concern. These scores likely reflect graph associations with bacterial infection rather than true therapeutic potential.

**Sinusitis is the most plausible candidate.** Sinus infections, especially in cystic fibrosis (CF) or multidrug-resistant cases, are often caused by *Pseudomonas aeruginosa*. This fits colistin's spectrum and its existing use in ear and ENT-adjacent infections. Topical or nebulized delivery could limit systemic toxicity, but efficacy remains unproven. The related predictions, chronic rhinosinusitis (rank 9) and chronic ethmoidal sinusitis (rank 10), rest on the same antibacterial rationale.

**Paratyphoid fever** (rank 7) is a Gram-negative infection, so colistin may be active in vitro. However, it is not a standard treatment, and tissue penetration is poor for an intracellular systemic pathogen.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sinusitis or any of the other top 10 predicted indications.

---

## Literature Evidence

Evidence for **sinusitis** (up to 10 most relevant, prioritizing clinical and review items):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | Review of therapeutic options for chronic rhinosinusitis in cystic fibrosis, which is common and often refractory to standard therapy |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | Pharmacokinetic study | J Antimicrob Chemother | Systemic absorption of nasally administered tobramycin and colistin (as colistin sulfomethate) in CF patients, used as a surrogate for safety |
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Case report | Int J Hematol | IV colistin successfully treated sinusitis, orbital cellulitis and pneumonia from multidrug-resistant *P. aeruginosa* in a patient with acute myeloid leukemia |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Cohort | Int Forum Allergy Rhinol | Sinus surgery improved quality of life, lung infections and lung function in primary ciliary dyskinesia (not colistin-specific) |
| [33155505](https://pubmed.ncbi.nlm.nih.gov/33155505/) | 2021 | Preclinical | Acta Otolaryngol | Fibrin sealant co-delivered with antibiotics as a topical treatment after sinus surgery in CF |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | In vitro | Int J Antimicrob Agents | Colistin's killing of planktonic *P. aeruginosa* does not depend on hydroxyl radical formation |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | In vitro | Pharmaceutics | Ceragenins plus ivacaftor prevent biofilm formation by rhinosinusitis-causing bacteria (not colistin) |
| [2778857](https://pubmed.ncbi.nlm.nih.gov/2778857/) | 1989 | Microbiological study | Gaoxiong Yi Xue Ke Xue Za Zhi | Bacterial flora and antibiotic sensitivity in 533 maxillary sinuses with chronic sinusitis; mostly Gram-positive organisms |
| [26340063](https://pubmed.ncbi.nlm.nih.gov/26340063/) | 2016 | Preclinical | Biomater Sci | Controlled antibiotic release from porous PMMA space maintainers for craniofacial reconstruction |
| [20132659](https://pubmed.ncbi.nlm.nih.gov/20132659/) | 2010 | Cohort | Hematology | Predictors of severe sepsis in neutropenic febrile episodes (not colistin-specific) |

Other predictions: paratyphoid fever has only one 1964 observational report on typhoid and paratyphoid fever ([14126225](https://pubmed.ncbi.nlm.nih.gov/14126225/)), with no colistin evidence. Chronic rhinosinusitis shares three of the sinusitis publications (34296343, 41599109, 27879058). No literature was found for the other predictions.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244849 | Colistimethate for Injection U.S.P. | Not specified | Not specified |
| 00476420 | Coly-Mycin M | Not specified | Not specified |
| 02403544 | Colistimethate for Injection, USP | Not specified | Not specified |

All three licences are valid single-ingredient products.

---

## Safety Considerations

- **Known class concerns:** Colistin is nephrotoxic and neurotoxic, which weighs heavily in renal-compromised patients.
- **Contraindicated conditions (from the knowledge graph, not label text):** kidney disease, pyoureter, herpes simplex infection, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis (including adult-onset), neuromuscular junction disease, geniculate herpes zoster, myringitis bullosa hemorrhagica.
- **Drug interactions:** No interaction data were found.

Package insert warnings and contraindications for the Canadian products have not been reviewed. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring predictions (99.8%+) have no clinical evidence and, in several cases, no plausible mechanism. Sinusitis and chronic rhinosinusitis are the only reasonable leads, but support is limited to a case report, a pharmacokinetic study, reviews and preclinical work, with no controlled trials. The renal and neurotoxicity profile also requires careful risk management. These are research questions, not candidates ready to advance.

**To proceed, the following is needed:**
- Review of the Health Canada package insert for warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence on topical or nebulized colistin for *Pseudomonas*-associated sinusitis, particularly in CF, including efficacy and local tolerability
- Confirmation of approved indications and dosage forms for the Canadian products, including whether any non-injectable route is available
- A safety plan covering renal function and neurological monitoring, and exclusion of the contraindicated populations listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

