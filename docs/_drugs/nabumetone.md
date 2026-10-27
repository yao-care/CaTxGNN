---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nabumetone: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "NABUMETONE"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome", "rheumatoid nodulosis"]
---

# Nabumetone
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

## Nabumetone: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Nabumetone is a nonsteroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nabumetone is a COX-2-preferential NSAID, and its efficacy in arthritis-related pain and inflammation is established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by mutations in the CDMP1/GDF5 gene, which disrupt BMP/GDF5 signalling during cartilage formation. No plausible mechanism links COX inhibition to correcting this defect. The high score most likely reflects the model's network proximity to other skeletal and joint conditions rather than a therapeutic rationale.

The other top-ranked predictions show the same pattern. Most are rare skeletal or developmental syndromes with no mechanistic connection to prostaglandin synthesis inhibition. The exception is **spondyloarthropathy, susceptibility to** (rank 8, score 99.94%). NSAIDs are a first-line therapy for spondyloarthritis, so there is class-level plausibility, but no nabumetone-specific evidence was retrieved. It is the one candidate that merits a follow-up literature search.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238639 | NABUMETONE | Not specified | Not specified |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from graph edges, not label text): hypertension and hypertensive disorder, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, pyoureter, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were found in the DDI query; the 20 retrieved are summarised here.
  - **Moderate**: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, vancomycin, potassium citrate, potassium bicarbonate, picosulfuric acid, sodium sulfate, and polyethylene glycol with electrolytes.
  - **Minor**: ranitidine, cimetidine, linaclotide.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanism. Nabumetone's COX inhibition is unrelated to the GDF5/BMP signalling defect underlying this disease. The high TxGNN score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for nabumetone
- Package insert warnings and contraindications from Health Canada
- Approved indication text and dosage form for the Canadian licence (DIN 02238639)
- A targeted literature search on nabumetone in spondyloarthropathy, the only prediction with class-level plausibility, which could be evaluated as a research question
- Any preclinical evidence that would link NSAID pharmacology to GDF5/BMP pathway biology, if this specific prediction is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

