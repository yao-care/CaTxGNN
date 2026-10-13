---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 965
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report** behind this prediction, so it is best read as a graph-based artifact rather than a real lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridium difficile* colitis, staphylococcal infections, endocarditis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, vancomycin is a glycopeptide antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in Gram-positive infections is well established.

That mechanism does not connect to diffuse scleroderma, which is an autoimmune fibrotic disease. The high TxGNN score appears to be an artifact of the knowledge graph. The only paper retrieved is a case report on erythroderma with sepsis and eosinophilia, which is not evidence for scleroderma.

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

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02407752 | JAMP VANCOMYCIN | Not specified | Not specified |
| 02394626 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | Not specified | Not specified |
| 02406543 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | Not specified | Not specified |
| 02139243 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | Not specified | Not specified |
| 02533006 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP | Not specified | Not specified |

These are 5 of the 20 valid single-ingredient licences. None are cancelled.

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
The diffuse scleroderma prediction has no trials, no relevant literature and no plausible mechanism. It is a model-only (L5) signal that is likely a graph artifact. The only item with a credible mechanism is streptococcal pneumonia, which mostly extends existing use.

**To proceed, the following is needed:**
- Mechanism of action data and Health Canada package insert warnings and contraindications
- For diffuse scleroderma: a credible biological rationale (for example, a gut-microbiome or immune-modulation hypothesis) before any further work
- For streptococcal pneumonia, if pursued: a targeted review of vancomycin use in penicillin-resistant pneumococcal infection, treated as an extension of existing use
- A renal and auditory safety monitoring plan for any new indication, given the knowledge-graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

