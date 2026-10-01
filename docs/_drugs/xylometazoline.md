---
layout: default
title: Xylometazoline
parent: High Evidence (L1-L2)
nav_order: 979
evidence_level: L2
indication_count: 2
---

# Xylometazoline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

# Xylometazoline: From Nasal Congestion to Nasal Cavity Disease

## One-Sentence Summary

Xylometazoline is a topical nasal decongestant, and it is marketed in Canada in several nasal products.
The TxGNN model predicts it may be effective for **nasal cavity disease**, with **2 clinical trials** and **7 publications** currently supporting this direction.
This is largely an on-label or near-label use rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nasal congestion (inferred from product names; no indication text on record) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Xylometazoline is a topical alpha-adrenergic agonist of the imidazoline class. It constricts the blood vessels of the nasal mucosa, which reduces mucosal swelling and nasal airway resistance and widens the nasal cavity.

This mechanism fits a broad "nasal cavity disease" label well, and it is consistent with the very high TxGNN score. The available studies show xylometazoline widening the nasal airway, reducing nasal resistance and preparing the nose for procedures. These are mostly physiological and procedural settings rather than trials treating a defined nasal disease.

A second prediction, **acute laryngopharyngitis** (score 99.89%), rests on model output alone. Xylometazoline is applied to the nasal mucosa, and no evidence shows that it reaches or benefits the laryngopharynx. No trials or publications were found for it.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple crossover of cocaine, lidocaine/xylometazoline and saline for intranasal analgesia before nasotracheal intubation. Xylometazoline is part of a combination arm, so its effect cannot be isolated. |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | Not applicable | Unknown | 80 | Foley catheter-assisted nasal intubation and nasal bleeding in adults. This is a procedural technique study, and xylometazoline's role is indirect. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT | JAMA Otolaryngol Head Neck Surg | Double-blind, placebo-controlled trial of intranasal local anesthetic and decongestant spray before flexible nasendoscopy in children |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Randomized blinded study | Eur Arch Otorhinolaryngol | Cotton pledget packing versus topical spray for nasal preparation before endoscopy in 100 patients |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Clinical study | Korean J Anesthesiol | Prophylactic xylometazoline spray compared with epinephrine gauze packing for expanding the nasal cavity before nasotracheal intubation |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | Double-blind study | Arzneimittel-Forschung | Rhinomanometry in 18 healthy subjects comparing a tuaminoheptane/N-acetylcysteine spray with xylometazoline and placebo for nasal resistance |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological study | Rhinology | Nasal airflow asymmetry in healthy subjects and in acute rhinitis from the common cold, and how xylometazoline changed it |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestn Otorinolaringol | Nasal mucosa changes in the elderly and treatment approaches for inflammatory nasal and sinus disease, including combined decongestant sprays |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal study | Pneumologie | Xylometazoline reduced raised nasal airway resistance in brachycephalic dogs by about 50% (indirect evidence) |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02208903 | OTRIVIN MEDICATED COLD & ALLERGY RELIEF WITH MOISTURIZERS |
| 02452863 | NASAL DECONGESTANT SPRAY WITH MOISTURIZERS |
| 00653330 | OTRIVIN MEDICATED COLD & ALLERGY RELIEF |
| 02452812 | DECONGESTANT NASAL SPRAY |
| 02331403 | OTRIVIN MEDICATED COMPLETE NASAL CARE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is biologically consistent with the prediction, and the drug is already marketed in Canada as a nasal decongestant. Direct evidence is limited, however: one small Phase 3 trial with a combination arm, procedural endpoints, and mostly physiological studies.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing. This is a blocking gap for safety screening.
- Approved indication text and dosage forms for the five DINs.
- Mechanism of action and original indication data from DrugBank.
- Guardrails: short-term topical use only, monitoring for rebound congestion (rhinitis medicamentosa) with prolonged use, and caution in hypertension and cardiovascular disease.
- For acute laryngopharyngitis (**Hold**): a feasibility and safety assessment before any further consideration.

*These results are for research reference only and do not constitute medical advice. Predicted candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

