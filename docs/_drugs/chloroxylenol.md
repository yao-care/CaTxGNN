---
layout: default
title: Chloroxylenol
parent: Model Prediction Only (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chloroxylenol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not specified in the licence data (products are topical antiseptic/di…"
---

# Chloroxylenol
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

# Chloroxylenol: From Topical Antisepsis to Osteoarthritis

## One-Sentence Summary

Chloroxylenol is a halogenated phenol antiseptic and disinfectant, used in hand soaps, wound cleansers and liniments.
The TxGNN model predicts it may be effective for **osteoarthritis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The only related publication found (for a lower-ranked prediction, rheumatoid arthritis) is an animal toxicity study that raises a safety signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the licence data (products are topical antiseptic/disinfectant and liniment products) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.27% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chloroxylenol is a topical halogenated phenol antiseptic. It is used to reduce microbes on skin and surfaces, not to treat joint disease.

No mechanistic link to osteoarthritis has been established. Chloroxylenol has no known anti-inflammatory, chondroprotective or analgesic activity in joint tissue. The high score (0.983) most likely reflects connections within the knowledge graph rather than a pharmacological relationship.

Other top-ranked predictions are osteoarthritis susceptibility, rheumatoid arthritis, hepatic porphyria, gout, pseudoachondroplasia and several rare hepatic diseases. None has trial or literature support, and none has a plausible mechanism. Several hepatic diseases share an identical score (0.9727), which points to a generic graph-based association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for osteoarthritis. One paper was retrieved for the lower-ranked rheumatoid arthritis prediction. It is an ecotoxicology study, not evidence of benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39489103](https://pubmed.ncbi.nlm.nih.gov/39489103/) | 2024 | Preclinical (animal, non-mammalian) | Aquatic Toxicology | Chronic chloroxylenol exposure (1.43–143 μg/L) affected endochondral ossification and body condition in *Rana chensinensis* tadpoles, suggesting a possible skeletal/cartilage toxicity signal. |

---

## Canada Market Information

Twelve single-ingredient licences are valid in Canada. Dosage form and approved-indication text are not available for these entries. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02449420 | SOFT CARE DEFEND | Not available | Not available |
| 02448866 | SOFT CARE DEFEND FOAM | Not available | Not available |
| 02480506 | APPLAUD AB ANTISEPTIC LOTIONIZED HAND SOAP | Not available | Not available |
| 01977873 | GERMICIDAL HAND SOAP LIQ 0.6% | Not available | Not available |
| 02242847 | DIGICLEAN E FOAM HAND SOAP | Not available | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information.

The animal study above (PMID 39489103) suggests a possible skeletal/cartilage toxicity signal at environmental concentrations in amphibians. It is not human data, but it argues against assuming benefit in joint disease. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone. There are no clinical trials, no supporting literature, and no plausible mechanism for a topical antiseptic in osteoarthritis. The only related finding is a potential toxicity signal.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- Package insert warnings and contraindications from Health Canada
- Evidence of anti-inflammatory or chondroprotective activity in joint models
- Assessment of whether a topical antiseptic could reach joint tissue at relevant concentrations
- Review of mammalian safety data on cartilage and bone effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

