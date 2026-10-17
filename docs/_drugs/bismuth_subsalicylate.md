---
layout: default
title: Bismuth Subsalicylate
parent: Model Prediction Only (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bismuth Subsalicylate: predicted new indication Paratyphoid fever (evidence level L5). Approved use: Diarrheal disease, dyspepsia"
monitor_inn: "BISMUTH SUBSALICYLATE"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "salmonellosis", "typhoid fever", "conjunctivitis", "relapsing fever", "acute contagious conjunctivitis", "gingivitis", "punctate epithelial keratoconjunctivitis", "otitis externa"]
---

# Bismuth Subsalicylate
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

# Bismuth Subsalicylate: From Diarrheal Disease and Dyspepsia to Paratyphoid Fever

## One-Sentence Summary

Bismuth subsalicylate is a long-marketed over-the-counter agent originally used for diarrheal disease and dyspepsia.
The TxGNN model predicts it may be effective for **paratyphoid fever** (top-ranked prediction), but **no clinical trials and no publications** currently support this specific indication.
The most evidence-supported predictions among the top 10 are salmonellosis and gingivitis, both at preclinical or indirect level only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dyspepsia (from the TxGNN knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bismuth subsalicylate is a poorly soluble, minimally absorbed luminal agent with antimicrobial and anti-secretory activity against enteric pathogens, and it is established in diarrheal disease and dyspepsia. Mechanistically, this may be applicable to enteric Salmonella infections.

Paratyphoid fever is caused by *Salmonella* Paratyphi and is closely related to diarrheal and other Salmonella-associated conditions. The high TxGNN score is likely driven by graph proximity to those indications rather than by direct evidence. In vitro work shows that the drug binds and kills diverse bacteria, which makes the prediction biologically plausible.

There are important limits. Paratyphoid and typhoid fever are systemic infections that require antibiotics, and a luminal, minimally absorbed agent is unlikely to treat systemic disease. The drug is best viewed as a possible symptomatic or adjunctive option, not a curative one.

### Other Top-Ranked Predictions

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 1 | Paratyphoid fever | 99.98% | L5 | No evidence; plausible but unvalidated |
| 2 | Diffuse scleroderma | 99.96% | L5 | No plausible mechanism; likely a knowledge-graph artifact |
| 3 | Salmonellosis | 99.95% | L4 | In vitro antibacterial data and older reviews |
| 4 | Typhoid fever | 99.92% | L5 | Systemic infection; luminal agent unlikely to suffice |
| 5 | Conjunctivitis | 99.92% | L5 | Theoretical only; no ocular data |
| 6 | Relapsing fever | 99.85% | L5 | Loose rationale from historical antispirochetal use of bismuth |
| 7 | Acute contagious conjunctivitis | 99.84% | L5 | Theoretical only |
| 8 | Gingivitis | 99.75% | L4 | Preclinical dental studies and historical reports |
| 9 | Punctate epithelial keratoconjunctivitis | 99.74% | L5 | Often viral or immune-mediated; weak fit |
| 10 | Otitis externa | 99.68% | L5 | No otic formulation or safety data |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for paratyphoid fever, nor for any of the other nine top-ranked predicted indications.

---

## Literature Evidence

Currently no related literature available for paratyphoid fever.

For the closely related **salmonellosis** prediction (rank 3), the following records were compiled:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2694949](https://pubmed.ncbi.nlm.nih.gov/2694949/) | 1989 | In vitro study | Antimicrob Agents Chemother | Bismuth subsalicylate bound diverse bacteria and killed them, with a 4-log10 reduction of *E. coli* within 4 hours |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Describes bismuth subsalicylate as an antisecretory agent that reduces stool number by about 50% in acute diarrhea |
| [2655632](https://pubmed.ncbi.nlm.nih.gov/2655632/) | 1989 | Review | Annu Rev Public Health | General review of diarrheal disease control; indirect support only |
| [1760758](https://pubmed.ncbi.nlm.nih.gov/1760758/) | 1991 | Veterinary review | Vet Clin North Am Food Anim Pract | Diarrhea management in neonatal calves, mentioning bismuth subsalicylate; veterinary and indirect |

For **gingivitis** (rank 8), the following records were compiled:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28837052](https://pubmed.ncbi.nlm.nih.gov/28837052/) | 2017 | Preclinical in vitro | Nanotechnology | Bismuth subsalicylate nanoparticles showed antibacterial activity against oral anaerobic bacteria |
| [34038883](https://pubmed.ncbi.nlm.nih.gov/34038883/) | 2021 | Preclinical materials study | Biomed Mater | Drug incorporated into electrospun membranes to prevent bacterial colonization in periodontal therapy |
| [20994674](https://pubmed.ncbi.nlm.nih.gov/20994674/) | 1946 | Historical clinical report | Eye Ear Nose Throat Mon | Bismuth subsalicylate in oil for Vincent's angina; old and low quality |
| [21012833](https://pubmed.ncbi.nlm.nih.gov/21012833/) | 1946 | Historical clinical report | Ill Med J | Same topic as above |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02313162 | Bismuth Subsalicylate Suspension | Not specified | Not specified |
| 02468646 | Regular Strength Bismuth | Not specified | Not specified |
| 02097079 | Pepto-Bismol | Not specified | Not specified |
| 02534436 | Gastrovol Liquid Gels | Not specified | Not specified |
| 02177994 | Pepto Bismol Caplet, 262 mg/caplet | Caplet | Not specified |

All 14 licences are valid single-ingredient products; none are cancelled. Only the first five are listed above. Other product names include liquid, chewable, caplet and liquicap forms.

---

## Safety Considerations

**Contraindication signals (knowledge graph, not label text):**
The TxGNN knowledge graph links the drug to contraindications in the following conditions: liver failure, liver disease, kidney disease, gallbladder disease, epilepsy, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, gout, peripheral neuropathy, peripheral nervous system disease, brain disease, non-infectious meningitis, blood coagulation disease, substance abuse/dependence, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and pyoureter. These reflect graph edges and should be verified against the product monograph.

**Drug Interactions:** 64 interactions were identified; all 20 reviewed are rated Moderate. The main groups are:
- **Tetracycline antibiotics:** doxycycline, tetracycline, minocycline
- **Antidiabetic agents:** insulins (aspart, degludec, detemir, glargine, glulisine, human), sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide), and meglitinides (repaglinide, nateglinide)
- **Others:** morphine, fenfluramine

**Additional note:** The salicylate component raises concern in some populations, such as those with scleroderma-related or other vulnerable conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, paratyphoid fever, has no clinical trials or literature, and the score likely reflects graph proximity rather than real efficacy. As a luminal agent, the drug is unlikely to address a systemic infection. Among the top 10, only salmonellosis and gingivitis reach L4, and only on preclinical or indirect evidence, so they are better treated as research questions than as candidates for development.

**To proceed, the following is needed:**
- Product monograph warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Approved indication text and dosage form data for the Canadian licences
- Controlled clinical evidence for enteric Salmonella infection (including paratyphoid), or, if prioritizing, a preclinical-to-clinical plan for salmonellosis or periodontal use
- Drug interaction management guidance, particularly for tetracyclines and antidiabetic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

