---
layout: default
title: Sulfamethoxazole
parent: Model Prediction Only (L5)
nav_order: 871
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Sulfamethoxazole: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Infectious otitis media, nocardiosis, toxoplasmosis, pneumocystosis…"
---

# Sulfamethoxazole
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

# Sulfamethoxazole: From Bacterial Infections to Acute Contagious Conjunctivitis

## One-Sentence Summary

Sulfamethoxazole is a sulfonamide antibacterial originally used for infections such as otitis media, nocardiosis, toxoplasmosis, pneumocystosis and shigellosis.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but conjunctivitis is already among its listed original indications, so this is not a true repurposing candidate.
Evidence is limited to **0 clinical trials** and **1 publication** (a susceptibility survey, not an efficacy study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Infectious otitis media, nocardiosis, toxoplasmosis, pneumocystosis, shigellosis, conjunctivitis and others (the Health Canada licence records contain no indication text) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (the data compiled for this report rated it L4, but no efficacy or mechanism studies were found, so L5 is the better fit) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge, sulfamethoxazole inhibits bacterial dihydropteroate synthase, which blocks folate synthesis. This is a plausible antibacterial mechanism against the pathogens that cause bacterial conjunctivitis.

Conjunctivitis already appears among the drug's original indications, so the high TxGNN score (0.996) most likely reflects this existing association and the drug's antibacterial class. It should not be read as new, independent evidence.

Viral causes of acute contagious conjunctivitis would not be expected to respond to an antibacterial. Any benefit would be limited to bacterial cases.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cross-sectional microbiology/susceptibility study | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Retrospective analysis of the bacteria and antibiotic susceptibility patterns in childhood acute bacterial conjunctivitis in Western Greece. It is not a clinical efficacy study of sulfamethoxazole. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02525917 | Sulfamethoxazole and Trimethoprim for Injection, USP | Not specified | Not specified |
| 00445266 | Sulfatrim Pediatric | Not specified | Not specified |
| 00550086 | Septra Injection | Not specified | Not specified |
| 00445274 | Sulfatrim | Not specified | Not specified |
| 00445282 | Sulfatrim DS | Not specified | Not specified |

## Safety Considerations

**Disease-related cautions (from knowledge graph contraindication links, not label text):**
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, folic acid deficiency anaemia, G6PD deficiency
- Kidney: kidney disease, kidney failure, uraemia, glomerulonephritis, pyoureter
- Liver and gallbladder: liver disease, gallbladder disease
- Metabolic: porphyria (including inherited porphyria and porphyrin metabolism disease), glycogen storage disease, cystinuria, galactosemia
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis

**Drug Interactions:** The interaction screen returned 100 interacting drugs. The main ones in the data compiled for this report are:
- **Moderate:** the sulfonylurea antidiabetics (chlorpropamide, glimepiride, acetohexamide, glipizide, glyburide), several insulins (human, aspart, degludec, detemir, glargine, glulisine), balsalazide and picosulfuric acid. The antidiabetic interactions suggest monitoring for low blood sugar.
- **Minor:** famotidine, clarithromycin, dolasetron, palonosetron, cisapride and granisetron.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Conjunctivitis is already an original indication, so this is not a true repurposing finding. The only supporting publication is a susceptibility survey, and there are no clinical trials. The high model score does not add independent evidence, and viral conjunctivitis would not be expected to respond.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (the safety screen cannot proceed without them)
- Mechanism of action data confirmed from DrugBank
- Clinical efficacy evidence, ideally comparative trials, in bacterial conjunctivitis
- Confirmation of whether an ophthalmic or topical route is relevant, since the licensed products are listed without dosage form details
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

