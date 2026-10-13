---
layout: default
title: Minocycline
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 2
---

# Minocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Minocycline: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a tetracycline-class antibiotic originally used for infections such as urinary tract infection, bronchitis, gonorrhea and periodontitis, as well as for acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** in the data compiled for this report, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; the knowledge graph lists urinary tract infection, bronchitis, acne, gonorrhea, periodontitis, pharyngitis and others |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, minocycline is a tetracycline-class antibiotic. Its efficacy in bacterial infections and acne is established, and mechanistically it may be applicable to inflammatory conditions of the ocular surface.

The plausible mechanisms below come from general knowledge of the drug, not from the data compiled for this report. They include anti-inflammatory activity (inhibition of matrix metalloproteinase-9 and reduced cytokine production) and antimicrobial activity against bacteria on the ocular surface. Tetracycline-class drugs are already used for ocular surface inflammation, which makes the prediction biologically plausible.

This link cannot be verified from the supplied data. The second-ranked prediction, **exposure keratitis** (score 99.20%), is even more speculative. Its main cause is corneal drying from incomplete eyelid closure, and lubrication and protection are the primary management. Any benefit from minocycline would be secondary, through reduced inflammation or prevention of secondary infection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02084104 | MINOCYCLINE | Not specified | Not specified |
| 02084090 | MINOCYCLINE | Not specified | Not specified |
| 02278219 | ARESTIN MICROSPHERES | Not specified | Not specified |

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not taken from label text): kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, pseudotumor cerebri, intracranial hypertension, and dyskinesia of esophagus.
- **Drug Interactions**: the interaction query was completed, with 100 interactions in total; 20 are listed in the data compiled for this report.
  - **Major**: isotretinoin and acitretin. Minocycline is also associated with intracranial hypertension, as noted above.
  - **Moderate**: ethinylestradiol, amoxicillin, ampicillin, aminolevulinic acid (topical), sodium citrate, calcium acetate, calcium phosphate, balsalazide, bismuth subcitrate potassium, brentuximab vedotin, cannabidiol, and the asparaginase products (*E. coli*, *Erwinia chrysanthemi*, and calaspargase pegol).
  - **Minor**: acetazolamide, hydrochlorothiazide, amiloride and bumetanide.

Package insert warnings and contraindications for the Canadian products have not been retrieved. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (99.63%) but no supporting clinical trials or publications (evidence level L5). Mechanism of action data and Canadian label safety information are also missing, so the prediction cannot yet be assessed beyond the model output.

**To proceed, the following is needed:**
- A systematic literature search on minocycline (oral or topical ocular) for punctate epithelial keratoconjunctivitis and related ocular surface inflammation
- Detailed mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications, to complete safety screening
- Approved indication text and dosage forms for the three DINs
- Assessment of route compatibility, since no ocular formulation is identified in the Canadian licence data
- A review of the knowledge-graph contraindications (for example intracranial hypertension) against the planned patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

