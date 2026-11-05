---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-05
monitor_inn: "CHLORAMPHENICOL"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
description: "Chloramphenicol: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Chloramphenicol: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is an antibiotic with one valid single-ingredient licence in Canada.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but the data compiled for this report contain **no clinical trials** and only **4 basic-research publications** on the disease biology, none of which tests chloramphenicol as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Chloramphenicol is a broad-spectrum antibacterial that acts on bacterial protein synthesis, so its known role is in treating infections.

Diffuse scleroderma (diffuse systemic sclerosis) is an autoimmune, fibrotic disease, not an infection. The four publications linked to this prediction study how skin fibroblasts from patients overproduce collagen (alpha1(I) procollagen gene activation, Smad3/Sp1/p300 and TGF-beta signaling). None of them shows an effect of chloramphenicol on the disease. Chloramphenicol is most likely mentioned in them as a laboratory reagent used in reporter assays, not as a therapy.

There is therefore no plausible therapeutic mechanism supported by the available data. The high TxGNN score most likely reflects an association in the literature rather than a real treatment signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Basic research (in vitro) | Arthritis and Rheumatism | Transcriptional activation of the alpha1(I) procollagen gene in dermal fibroblasts from patients with diffuse systemic sclerosis; role of intronic sequences |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Basic research (in vitro) | Arthritis and Rheumatism | Promoter elements and transcription factors behind up-regulated alpha1(I) procollagen expression in systemic sclerosis |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Basic research (in vitro) | Arthritis and Rheumatism | Blocking TGF-beta signaling prevents up-regulated collagen synthesis in scleroderma fibroblasts |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Basic research (in vitro) | Rheumatology (Oxford) | Constitutively phosphorylated Smad3 interacts with Sp1 and p300 in scleroderma fibroblasts |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00312363 | CHLOROMYCETIN SUCCINATE INJECTION | Not specified | Not specified |

## Cytotoxicity

Chloramphenicol is an antibacterial, not an antineoplastic drug, so cytotoxic-drug classification does not apply.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening; the main ones listed here are examples.
  - Major: cisapride, naloxegol
  - Moderate: sulfonylurea antidiabetics (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), repaglinide, saxagliptin, rosuvastatin, simvastatin, aprepitant, metronidazole, budesonide, iron, eliglustat, naldemedine, nitisinone, balsalazide
- **Conditions of concern**: Chloramphenicol is recorded as a concern in people with blood disorders (anemia, aplastic anemia, neutropenia, agranulocytosis, thrombocytopenia, paroxysmal nocturnal hemoglobinuria), kidney disease, liver disease, gallbladder disease, peripheral neuropathy, optic neuritis and acute intermittent porphyria. These come from drug-disease relation data, not from the label text.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by in vitro studies of scleroderma fibroblast biology, which do not test chloramphenicol. There are no clinical trials, no plausible therapeutic mechanism, and the drug's known bone marrow toxicity is a serious concern for a long-term disease. The evidence level is L5.

**To proceed, the following is needed:**
- Evidence that chloramphenicol has an actual effect on the fibrotic or immune pathways of diffuse scleroderma (for example, dedicated preclinical studies)
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A risk-benefit assessment of hematologic toxicity for a chronic, non-infectious condition

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

