---
layout: default
title: Loteprednol Etabonate
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
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

# Loteprednol Etabonate: From Ocular Inflammation to Non-Viral Serous Conjunctivitis

## One-Sentence Summary

Loteprednol etabonate is a topical corticosteroid, marketed in Canada under four licences as ophthalmic gel, ointment and drop products. The TxGNN model predicts it may be effective for **serous conjunctivitis (non-viral)**, but **no clinical trials and no publications** were retrieved for this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the retrieved licence data (approved indication text is empty); understood as a topical ophthalmic corticosteroid for ocular inflammation |
| Predicted New Indication | Serous conjunctivitis except viral |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, loteprednol etabonate is a topical corticosteroid, its anti-inflammatory use in the eye is established, and mechanistically it may be applicable to non-viral conjunctival inflammation.

The relationship between the original and predicted indications is plausible but unverified. Non-viral serous conjunctivitis is an inflammatory ocular-surface condition, which fits a corticosteroid's expected activity. The very high graph score (99.69%) probably also reflects the drug's association with neighbouring conjunctival terms in the knowledge graph. The original indications and MOA are missing from the input, so this link could not be checked against label data.

**Other predicted indications** (all L4–L5, none supported by trials):

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Conjunctival folliculosis | 99.69% | L5 | Often benign and non-inflammatory, so the steroid rationale is weak |
| Chronic follicular conjunctivitis | 99.69% | L4 | Two case reports retrieved; neither is evidence of loteprednol efficacy |
| Parasitic conjunctivitis | 99.69% | L5 | A steroid may worsen an uncontrolled parasitic infection |
| Pseudomembranous conjunctivitis | 99.66% | L4 | One 2025 viral-load study in adenoviral conjunctivitis; loteprednol involvement unconfirmed |
| Angelucci syndrome | 99.66% | L5 | Vernal-type allergic features make a steroid plausible; no specific evidence |
| Acute hemorrhagic conjunctivitis | 99.62% | L5 | Self-limited viral disease; little proven steroid benefit |
| Rosacea conjunctivitis | 99.34% | L5 | Reasonable mechanistic fit; a research question |
| Acute contagious conjunctivitis | 99.26% | L5 | Mainly infectious, so steroid monotherapy is unfavourable |
| Otitis externa | 99.13% | L5 | No otic formulation; prediction only |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2435853 | LOTEMAX GEL |
| 2320924 | ALREX |
| 2421941 | LOTEMAX OINTMENT |
| 2321114 | LOTEMAX |

Dosage form, manufacturer and approved indication text were not present in the retrieved licence records.

---

## Safety Considerations

Please refer to the package insert for safety information.

For the infectious predicted indications (parasitic, acute contagious, acute hemorrhagic and adenoviral conjunctivitis), a topical steroid may worsen infection or prolong viral shedding. Any exploration should account for this.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) for the top indication, with no registered trials and no literature. The Health Canada label data (indications, warnings, contraindications) and the MOA are also missing, so the prediction cannot yet be checked against the approved use or screened for safety.

**To proceed, the following is needed:**
- Health Canada package insert (approved indications, warnings, contraindications), which is currently a blocking gap
- Mechanism of action data from DrugBank
- A targeted literature search for loteprednol in non-viral conjunctivitis
- Clarification of the aetiology (allergic, toxic, infectious) for each candidate before any steroid rationale is applied
- Follow-up on the 2025 adenoviral conjunctivitis study (PMID 40638366) to confirm whether loteprednol was a study arm and what the viral-load findings were

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

