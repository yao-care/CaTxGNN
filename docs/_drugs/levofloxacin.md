---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal and staphylococcal infections…"
monitor_inn: "LEVOFLOXACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as pneumonia, sinusitis, conjunctivitis and pyelonephritis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but the evidence is very thin: **0 clinical trials** and **1 publication**, which is an outbreak report of a different (microsporidial) eye infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal and staphylococcal infections, bacterial pneumonia, sinusitis, conjunctivitis, pyelonephritis, anthrax) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Levofloxacin belongs to the fluoroquinolone class of antibacterials, and its efficacy against bacterial infections, including bacterial conjunctivitis, is established.

The prediction most likely reflects the similarity between ocular infections: the model links a drug used for bacterial conjunctivitis to another inflammatory or infectious condition of the eye surface. The one paper retrieved describes a **microsporidial** keratoconjunctivitis outbreak. Fluoroquinolones have no established activity against microsporidia, so the mechanistic link is weak. The very high score appears to rest on network similarity, not on clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis linked to swimming-pool water contamination in Taiwan. It does not show levofloxacin benefit. |

---

## Canada Market Information

Levofloxacin has 17 valid single-ingredient authorizations in Canada. Dosage form and approved indication text were not available for these products. Five of the main authorizations:

| DIN | Product Name |
|---------|------|
| 02442302 | QUINSAIR |
| 02537079 | LEVOFLOXACIN IN 5% DEXTROSE INJECTION |
| 02298651 | SANDOZ LEVOFLOXACIN |
| 02315440 | TEVA-LEVOFLOXACIN |
| 02325942 | APO-LEVOFLOXACIN |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (not label text; to be verified against the package insert): long QT syndrome, torsades de pointes, epilepsy, liver disease and drug-induced liver injury, tendinitis, peripheral neuropathy, myasthenia gravis, impaired renal function, diabetes mellitus and diabetic ketoacidosis, *Clostridium difficile* colitis, rhabdomyolysis, thrombocytopenia, leukopenia, pancytopenia, anemia, myocardial ischemia and coronary artery disease, potassium deficiency, and others.
- **Drug Interactions**: 100 interactions were identified. Those shown include two **Major** ones, **tramadol** and **hydrocortisone**. Many are **Moderate**, for example abiraterone, acarbose, famotidine, formoterol, ketorolac, ibuprofen, ethinylestradiol, metformin, pioglitazone, alfuzosin and amifampridine. Minor ones include paclitaxel and aldesleukin.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials. Its only publication concerns a microsporidial outbreak, a pathogen not expected to respond to fluoroquinolones. Evidence is at the model-prediction level (L5).

**To proceed, the following is needed:**
- Clinical or preclinical evidence of levofloxacin activity against punctate epithelial keratoconjunctivitis, and identification of the causative pathogens (for example adenoviral versus bacterial)
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, including ophthalmic formulation and route compatibility
- Consideration of other predictions for this drug that have stronger support. Infection prophylaxis in newly diagnosed myeloma (monoclonal gammopathy) is backed by the phase 3 TEAMM RCT. Plague (septicemic plague) is backed by animal-model data that supported regulatory approval. Both are better candidates for further evaluation, with stewardship-based guardrails.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

