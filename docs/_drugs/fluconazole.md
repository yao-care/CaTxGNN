---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an antifungal originally used to treat candidiasis (oral, esophageal, vulvovaginal, and disseminated forms) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, candidiasis, vulvovaginal candidiasis, esophageal candidiasis, cryptococcal meningitis, candidemia, disseminated candidiasis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, fluconazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), blocking ergosterol synthesis and impairing fungal cell membranes. Its efficacy in candidiasis and cryptococcal infection is well established.

Punctate epithelial keratoconjunctivitis is often not caused by fungi. Common causes include viral infection (such as adenovirus), toxic injury, and immune-mediated processes, so a direct antifungal mechanism is not clearly relevant. Possible links include fungal keratitis, fungal colonization of the ocular surface, or a secondary anti-inflammatory effect, but none of these is supported by the data compiled for this report.

The prediction is most likely driven by network proximity to other ocular or fungal infection indications in the knowledge graph, rather than by a verified mechanism. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Fluconazole has 20 valid single-ingredient authorizations in Canada and no cancelled ones. Dosage form and approved indication text were not available for these products. The main authorizations are:

| DIN | Product Name |
|---------|------|
| 02141442 | DIFLUCAN ONE |
| 02024152 | DIFLUCAN |
| 00891835 | DIFLUCAN |
| 02241895 | APO-FLUCONAZOLE-150 |
| 02245643 | PMS-FLUCONAZOLE |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, and gallbladder disease are flagged as contraindication-related conditions.
- **Drug Interactions**: 100 interactions were identified in total. A selection from the first 20 reviewed:
  - **Major**: Chlorpropamide
  - **Moderate**: Famotidine, rabeprazole, omeprazole, dexlansoprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, loperamide, aprepitant, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - **Minor**: Amphotericin B, amphotericin B (lipid complex), clarithromycin

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high model score (99.24%), with no clinical trials or publications. The antifungal mechanism has no clear connection to a condition that is usually non-fungal, so the evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Literature and trial searches on fluconazole (including topical or ophthalmic use) in keratoconjunctivitis and fungal keratitis
- Clarification of the biological rationale, such as whether any fungal or anti-inflammatory component exists in PEK
- Health Canada package insert warnings and contraindications for safety screening
- Mechanism of action data from DrugBank
- Route and formulation compatibility assessment, since an ocular indication may need a topical or ophthalmic route
- Review of QT-prolongation risk and the interaction profile for any new patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

