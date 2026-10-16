---
layout: default
title: Cefprozil
parent: Model Prediction Only (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefprozil: predicted new indication Urinary tract infection (evidence level L5). Approved use: Bronchitis, tonsillitis, infectious otitis media…"
---

# Cefprozil
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

# Cefprozil: From Respiratory Tract Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an oral second-generation cephalosporin antibiotic, originally used for respiratory and related bacterial infections such as bronchitis, tonsillitis, and otitis media.
The TxGNN model predicts it may be effective for **urinary tract infection (UTI)**.
Support comes from **0 registered clinical trials** and **9 publications**, including three comparative studies against cefaclor in acute uncomplicated UTI.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, tonsillitis, infectious otitis media, streptococcal infection, respiratory tract infectious disease, common cold, staphylococcal infection (from the knowledge graph; the Canadian licence records have no indication text) |
| Predicted New Indication | Urinary tract infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (provisional: study design inferred from titles only; no registered trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on its drug class, cefprozil is a second-generation oral cephalosporin. Drugs of this class inhibit bacterial cell wall synthesis by binding penicillin-binding proteins.

Its established uses are respiratory and skin infections caused by streptococci, methicillin-susceptible *Staphylococcus aureus*, *H. influenzae*, and *M. catarrhalis*. It also shows in vitro activity against common urinary pathogens such as *E. coli*, *Klebsiella pneumoniae*, and *Proteus mirabilis*. A study of 637 clinical isolates from Taiwan found cefprozil inhibited over 80% of *E. coli* and *K. pneumoniae* isolates at 8 mg/L. Since the mechanism is antibacterial, extending it to bacterial UTI is plausible.

Cefprozil is also excreted in urine, and the 1990s trials gave it once daily for acute uncomplicated UTI. Caution is needed because the evidence is old, and these studies were not designed to support a new regulatory claim.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for urinary tract infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | Comparative multicentre randomized study | Clinical Therapeutics | Once-daily cefprozil vs three-times-daily cefaclor for 10 days in acute uncomplicated UTI (patients ≥2 years) |
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | Comparative clinical trial | Antimicrob Agents Chemother | In 108 women, clinical and bacterial cure were 94% and 93% for cefprozil vs 94% and 94% for cefaclor (not significantly different) |
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | Open, randomized comparative trial | J Antimicrob Chemother | Cefprozil 500 mg once daily vs cefaclor 250 mg three times daily in adults with acute uncomplicated UTI |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Review | Drugs | Reviews antibacterial activity, pharmacokinetics, and therapeutic potential; active against many Enterobacteriaceae |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Review | Pediatric Annals | Cefprozil is active against respiratory, skin, and soft tissue pathogens, with once- or twice-daily dosing |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Review | American Family Physician | Positions new oral cephalosporins as alternatives for skin, respiratory, and urinary tract infections |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In vitro study | Chemotherapy | Good activity against *E. coli* and *K. pneumoniae* in Taiwanese clinical isolates |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Pediatric clinical study | Jpn J Antibiot | 19 of 21 children with acute bacterial infections (including a few UTIs) had good to excellent responses |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Pediatric clinical/laboratory study | Jpn J Antibiot | Pediatric pharmacokinetic and clinical data, including urinary concentrations and recovery |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02293528 | SPC-CEFPROZIL | Not available | Not available |
| 02329204 | SPC-CEFPROZIL | Not available | Not available |
| 02347261 | AURO-CEFPROZIL | Not available | Not available |
| 02347288 | AURO-CEFPROZIL | Not available | Not available |
| 02293579 | SPC-CEFPROZIL | Not available | Not available |

Seven valid single-ingredient licences are on record in total; the first five are shown.

---

## Safety Considerations

- **Contraindication-related disease associations (knowledge graph, not label text)**: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and congenital prothrombin deficiency.
- **Drug Interactions**: 55 interactions were identified. Those rated Moderate include balsalazide, kanamycin, neomycin, streptomycin, and picosulfuric acid. Others have an unrated ("Unknown") severity, including acetylsalicylic acid, amoxicillin, pantoprazole, omeprazole, lansoprazole, cimetidine, metformin, simvastatin, prednisone, and hydrocortisone.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefprozil is already marketed in Canada, has plausible antibacterial activity against urinary pathogens, and three randomized comparative studies against cefaclor showed similar clinical and bacterial cure rates in acute uncomplicated UTI. The evidence is old, there are no registered trials, and the design and phase were inferred from titles, so the evidence level is provisional.

**To proceed, the following is needed:**
- Retrieve the Health Canada package insert and confirm warnings, contraindications, and approved indications (the licence records lack indication text and dosage forms)
- Confirm the study designs and results of the three UTI comparative studies from full texts
- Check current local resistance data for common uropathogens and compare against current first-line UTI guidance
- Obtain detailed mechanism-of-action data
- Review the moderate-severity interactions (especially aminoglycosides) and the history of *C. difficile* colitis before use

**Other predicted indications (for reference):**
- Pneumonia (L3): the only registered trial is a Phase 4 antibiotic-duration study that does not clearly test cefprozil. Respiratory evidence is mostly indirect.
- Laryngitis (L3): only two low-quality Japanese pediatric reports, and the condition is mostly viral. In one report, efficacy in laryngitis was 0%.
- Epiglottitis, gonococcal urethritis, Ureaplasma urethritis, xanthogranulomatous pyelonephritis, uterine inflammatory disease, urogenital tuberculosis, and abdominal tuberculosis (all L5, Hold): model predictions only, with no clinical evidence. Several (Ureaplasma, tuberculosis) conflict with known pharmacology.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

