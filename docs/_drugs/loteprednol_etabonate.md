---
layout: default
title: Loteprednol Etabonate
parent: Model Prediction Only (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Loteprednol Etabonate: predicted new indication Serous conjunctivitis except viral (evidence level L5). Approved use: Uveitis and related ocular inflammatory conditions, including atopic…"
monitor_inn: "LOTEPREDNOL ETABONATE"
predicted_indications: ["serous conjunctivitis except viral", "conjunctival folliculosis", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "pseudomembranous conjunctivitis", "Angelucci syndrome", "acute hemorrhagic conjunctivitis", "rosacea conjunctivitis", "acute contagious conjunctivitis", "otitis externa"]
---

# Loteprednol Etabonate
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

# Loteprednol Etabonate: From Ocular Inflammatory Conditions to Serous Conjunctivitis (Non-Viral)

## One-Sentence Summary

Loteprednol etabonate is a topical corticosteroid originally used for inflammatory and allergic eye conditions such as uveitis and atopic, vernal and papillary conjunctivitis.
The TxGNN model predicts it may be effective for **serous conjunctivitis except viral**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uveitis and related ocular inflammatory conditions, including atopic, vernal and papillary conjunctivitis (the Canadian licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Serous conjunctivitis except viral |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, loteprednol etabonate is a topical corticosteroid. Its anti-inflammatory efficacy in allergic and inflammatory eye diseases is established, and mechanistically it may be applicable to non-viral serous conjunctivitis.

The original indications are immune-mediated or allergic inflammation of the conjunctiva and uveal tract. Non-viral serous conjunctivitis shares conjunctival surface inflammation, so an anti-inflammatory drug could plausibly help. The model's high score likely reflects this similarity to approved conjunctival indications within the knowledge graph.

However, no trial or publication in the data compiled for this report confirms the benefit. The prediction should be treated as a hypothesis.

### Other Predicted Indications (for context)

All other predictions also sit at evidence level L5.

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Conjunctival folliculosis | 99.69% | Usually benign and asymptomatic, so clinical need is questionable |
| 3 | Chronic follicular conjunctivitis | 99.69% | Plausible fit, but long-term steroid use raises intraocular pressure and cataract concerns |
| 4 | Parasitic conjunctivitis | 99.69% | Needs antiparasitic therapy; steroids alone may worsen infection |
| 5 | Pseudomembranous conjunctivitis | 99.66% | One indirect paper on adenoviral conjunctivitis (see below) |
| 6 | Angelucci syndrome | 99.66% | Rare; plausible anti-allergic effect, no clinical evidence |
| 7 | Acute hemorrhagic conjunctivitis | 99.62% | Self-limited viral disease; steroids are not standard care |
| 8 | Rosacea conjunctivitis | 99.34% | Strongest mechanistic plausibility, since rosacea is already an original indication; better framed as a research question |
| 9 | Acute contagious conjunctivitis | 99.26% | Mostly infectious; steroid use without anti-infective therapy is risky |
| 10 | Otitis externa | 99.13% | Only ophthalmic formulations are authorised; speculative |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the lead prediction (serous conjunctivitis except viral). One indirect paper was found for a lower-ranked prediction, pseudomembranous conjunctivitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40638366](https://pubmed.ncbi.nlm.nih.gov/40638366/) | 2025 | Comparative study (design unconfirmed) | Ocular Immunology and Inflammation | Evaluated topical ganciclovir, povidone-iodine, and their combination with loteprednol etabonate for viral load reduction and clinical outcomes in adenoviral conjunctivitis. Indirect context only. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02435853 | LOTEMAX GEL | Not specified | Not specified |
| 02320924 | ALREX | Not specified | Not specified |
| 02421941 | LOTEMAX OINTMENT | Not specified | Not specified |
| 02321114 | LOTEMAX | Not specified | Not specified |

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Ocular hypertension, glaucoma, herpes simplex virus keratitis, fungal eye infection, viral eye infection, ocular tuberculosis, and ophthalmic herpes zoster are flagged as contraindicated conditions. This matters because several predicted indications are infectious.
- **Drug Interactions**: 30 potential interactions were recorded, all with an unknown severity level. Examples include other corticosteroids (triamcinolone, prednisone), warfarin, clopidogrel, acetylsalicylic acid, ibuprofen, simvastatin, rosuvastatin, and several proton pump inhibitors (omeprazole, pantoprazole, lansoprazole). Topical ocular dosing has low systemic exposure, so the clinical relevance is unclear.
- **Longer-term concerns noted in the evidence**: Prolonged steroid use may raise intraocular pressure and promote cataract formation.

Please refer to the package insert for key warnings and formal contraindications, as label-level data were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.69%), but the evidence level is L5. No trials or publications support it. Many of the predicted conjunctival conditions are infectious, where steroids carry real risk. Safety information from the label is missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, dosage forms and approved indications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature and trial search for non-viral serous conjunctivitis
- A clinical review of whether the condition has a real unmet need and how it is defined
- Consider prioritising **rosacea conjunctivitis** as a research question, given its link to an existing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

