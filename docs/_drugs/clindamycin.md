---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Streptococcal and staphylococcal infections…"
monitor_inn: "CLINDAMYCIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis"]
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic originally used for bacterial infections (streptococcal, staphylococcal, anaerobic), bacterial vaginosis, and acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this direction. It is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis, acne (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Clindamycin is a lincosamide antibiotic. It blocks bacterial protein synthesis by binding the 50S ribosomal subunit. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects general pharmacological knowledge.

Its established uses are bacterial infections caused by gram-positive and anaerobic organisms, plus bacterial vaginosis and acne. Punctate epithelial keratoconjunctivitis is often viral or non-infectious (for example adenoviral, toxic, or dry-eye related). An antibacterial therefore has no clear rationale unless a bacterial component is present, such as staphylococcal blepharokeratoconjunctivitis.

The very high score therefore appears to be a graph-level association rather than a demonstrated biological link. The link should be treated as unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Clindamycin is marketed in Canada with 20 valid single-ingredient licences. Dosage form, manufacturer, and approved indication text were not available for these entries. Five main authorisations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02408511 | Clindamycin IV Infusion | Not available | Not available |
| 02400529 | Clindamycin | Not available | Not available |
| 02230535 | Clindamycin Injection USP | Not available | Not available |
| 00260436 | Dalacin C Phosphate | Not available | Not available |
| 02060604 | Dalacin Vaginal Cream | Not available | Not available |

The product names indicate injectable, vaginal cream, and oral granule presentations. No ophthalmic formulation appears among the licences listed.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug–disease relationships, not label text): liver failure, sunburn, Crohn disease, inflammatory bowel disease, Crohn's colitis, ulcerative colitis, atopic eczema/dermatitis, exfoliative dermatitis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, and vulvovaginal candidiasis.
- **Drug interactions**: 100 interactions were identified. Those rated Moderate include balsalazide, clarithromycin, picosulfuric acid, attapulgite, and kaolin. Other listed interactions, such as amphotericin B, aspirin, amoxicillin, bupropion, pantoprazole, glimepiride, doxycycline, morphine, metformin, omeprazole, sucralfate, vancomycin, and others, have an unclassified severity level.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications, the likely causes of the condition (viral or non-infectious) are not addressed by an antibacterial, and no ophthalmic clindamycin product is licensed in Canada.

**To proceed, the following is needed:**
- Evidence that a bacterial component (such as staphylococcal disease) is relevant in this condition, and any clinical or preclinical data on clindamycin in it
- A feasible ocular route and formulation
- Mechanism of action data and Health Canada package insert warnings and contraindications for formal safety screening

---

### Other Predictions Reviewed (for context)

The other top predictions are also weakly supported, and all are rated Hold:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Exposure keratitis | 99.80% | L4 | Only bacterial keratitis case reports and cohorts; none tests clindamycin |
| 3 | Non-human animal disease | 99.69% | L5 | Non-specific category; papers concern *C. difficile* epidemiology in animals |
| 4 | Neurotrophic keratopathy | 99.49% | L5 | No mechanistic link to nerve or epithelial repair |
| 5 | Epidemic keratoconjunctivitis | 99.49% | L5 | Adenoviral disease; literature is veterinary (bovine) |
| 6 | Postmenopausal atrophic vaginitis | 99.03% | L5 | Hormonal cause; likely score inflation from existing vaginitis indications |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

