---
layout: default
title: Dalbavancin
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dalbavancin: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Skin disease caused by infection"
monitor_inn: "DALBAVANCIN"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa", "ophthalmic herpes zoster", "infectious mononucleosis", "orbital cellulitis"]
---

# Dalbavancin
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

## Dalbavancin: From Skin Infection to Postinfectious Vasculitis
{: .text-alpha }

## One-Sentence Summary

Dalbavancin is an antibiotic originally used to treat skin disease caused by infection.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skin disease caused by infection |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, dalbavancin is a lipoglycopeptide antibiotic that inhibits bacterial cell wall synthesis and is active against Gram-positive organisms. Its efficacy in infection-related skin disease is the basis of its original use.

Postinfectious vasculitis is largely immune-mediated rather than an active bacterial infection. Antibacterial activity therefore has no clear direct link to this condition, unless a persistent Gram-positive infection is the trigger. The high TxGNN score most likely comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions reviewed:** The nine other predicted indications were also examined, and all are supported by model scores only (no trials or literature):

| Predicted Indication | Score | Assessment |
|------|------|------|
| Post-bacterial disorder | 0.9976 | Non-specific category; antibacterial action would not address sequelae after the pathogen has cleared |
| Post-infectious syndrome | 0.9976 | Generic category with no defined mechanism |
| Infective urethral stricture | 0.9974 | Fibrotic and anatomical; an antibiotic would not reverse the stricture |
| Chagas cardiomyopathy | 0.9972 | Parasitic cause; no plausible mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| Infection-related hemolytic uremic syndrome | 0.9972 | Mostly Gram-negative STEC; antibiotics generally not recommended |
| Otitis externa | 0.9970 | Often Pseudomonas, which is not covered; topical therapy is standard |
| Ophthalmic herpes zoster | 0.9925 | Viral cause; no antiviral activity |
| Infectious mononucleosis | 0.9916 | Viral (EBV); antibacterial therapy not indicated |
| Orbital cellulitis | 0.9902 | Most plausible: typically S. aureus (including MRSA) and streptococci, which dalbavancin covers, and close to its approved skin and soft-tissue infection use. Orbital tissue penetration and polymicrobial etiology remain uncertain. Flagged as a research question |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02480522 | XYDALBA | Not available | Not available |

## Safety Considerations

**Drug Interactions** (3 moderate-level interactions recorded):
- Picosulfuric acid (Moderate)
- Ethinylestradiol (Moderate)
- Mycophenolic acid (Moderate)

For warnings and contraindications, please refer to the package insert. Label-based safety information was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5) with no trials or literature, and the mechanism is weak because postinfectious vasculitis is largely immune-mediated. Among the ten predictions, orbital cellulitis is the only one with a plausible link, and it merits a research question rather than clinical adoption.

**To proceed, the following is needed:**
- Mechanism of action data
- Warnings and contraindications from the Health Canada package insert, needed before any safety screening
- Approved indication text, dosage form, and manufacturer details for the Canadian licence
- For orbital cellulitis: pharmacokinetic review of orbital tissue penetration and case-level literature review
- Evidence of a persistent Gram-positive trigger if postinfectious vasculitis is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

