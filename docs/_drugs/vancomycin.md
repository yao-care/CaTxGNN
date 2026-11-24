---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 965
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis, staphylococcal infections, endocarditis"
monitor_inn: "VANCOMYCIN"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model (deep learning) predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report** behind this prediction. The score may reflect similarities the model learned between related diseases, not biological evidence, so it is best not read as a real lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridium difficile* colitis, staphylococcal infections, endocarditis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 19; dormant: 1) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for vancomycin: "Vancomycin is an antibacterial drug. […] The bactericidal action of vancomycin results primarily from inhibition of cell-wall biosynthesis. In addition, vancomycin alters bacterial-cell-membrane permeability and RNA synthesis." ([DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560), label version 2026-08-19; accessed 2026-11-19.) Based on general knowledge, vancomycin is a glycopeptide antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in Gram-positive infections is well established.

That mechanism does not connect to diffuse scleroderma, which is an autoimmune fibrotic disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only paper retrieved is a case report on erythroderma with sepsis and eosinophilia, which is not evidence for scleroderma.

### Other Top-Ranked Predictions

The other top predictions fall into three groups:

- **Gram-negative infections (paratyphoid fever, salmonellosis, typhoid fever):** *Salmonella* is intrinsically resistant to vancomycin, which cannot cross the Gram-negative outer membrane. The retrieved papers are surveys, reviews and case reports that do not show efficacy.
- **Unrelated conditions (congenital analbuminemia, polyclonal hyperviscosity syndrome, hyperamylasemia, blood group incompatibility, premalignant hematological system disease):** There is no mechanistic rationale and no meaningful literature.
- **Streptococcal pneumonia (rank 9):** This is the only plausible one. *Streptococcus pneumoniae* is Gram-positive and vancomycin-susceptible, and vancomycin is used for penicillin-resistant pneumococcal infection. It is more an extension of existing anti-Gram-positive use than true repurposing. No trials were found, and the evidence is indirect (reviews, guidelines, resistance reports). It is rated L4 and labelled a "Research Question".

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with diffuse exfoliative rash, sepsis and eosinophilia, evaluated for erythroderma. It does not address scleroderma or vancomycin efficacy. |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02139243 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02139375 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02139383 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02241807 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02342863 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02394626 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02405822 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02405830 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02406543 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02406551 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02407744 | JAMP VANCOMYCIN | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02407752 | JAMP VANCOMYCIN | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02435713 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02435721 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02487071 | VANCOMYCIN INJECTION USP IN 0.9% SODIUM CHLORIDE | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02532999 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02533006 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02543974 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02543982 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Marketed |
| 02502607 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | VANCOMYCIN (VANCOMYCIN HYDROCHLORIDE) | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-vancomycin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "None are cancelled." Removed: this was the remainder of a sentence describing the earlier licence table, which showed only some of the DINs; the table under Canada Market Information now shows the current status of each DIN. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-vancomycin-1 -->

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph (not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder, auditory system disease.
- **Drug Interactions:** 100 interactions were identified, mostly Moderate. The Major ones are:
  - Human immunoglobulin G (intravenous)
  - Human botulinum neurotoxin A/B immune globulin
  - *Vibrio cholerae* CVD 103-HgR live vaccine strain

  Notable Moderate interactions include:
  - Nephrotoxic or ototoxic agents: amikacin, amphotericin B (including lipid complex), bacitracin, capreomycin, carboplatin
  - NSAIDs: ketorolac, ibuprofen, diclofenac, celecoxib
  - Others: metformin, mesalazine, cholestyramine

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The diffuse scleroderma prediction has no trials, no relevant literature and no plausible mechanism. It is a model-only (L5) signal from the TxGNN model (deep learning) that may reflect similarities the model learned between related diseases, not biological evidence. The only item with a credible mechanism is streptococcal pneumonia, which mostly extends existing use.

**To proceed, the following is needed:**
- Mechanism of action data and Health Canada package insert warnings and contraindications
- For diffuse scleroderma: a credible biological rationale (for example, a gut-microbiome or immune-modulation hypothesis) before any further work
- For streptococcal pneumonia, if pursued: a targeted review of vancomycin use in penicillin-resistant pneumococcal infection, treated as an extension of existing use
- A renal and auditory safety monitoring plan for any new indication, given the knowledge-graph contraindication signals

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560) |
| 2026-11-24 | Removed: "None are cancelled." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

