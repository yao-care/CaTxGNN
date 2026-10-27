---
layout: default
title: Methocarbamol
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Methocarbamol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the licence records. Product names (e.g.…"
monitor_inn: "METHOCARBAMOL"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "panuveitis (disease)", "anaphylaxis", "iris disease", "uveitis", "ventricular tachycardia", "food-dependent exercise-induced anaphylaxis", "conjunctivitis", "obsolete bundle branch block"]
---

# Methocarbamol
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

## Methocarbamol: From Muscle Spasm and Back Pain to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Methocarbamol is a centrally acting skeletal muscle relaxant, marketed in Canada alone and in combination with analgesics for muscle and back pain.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a computational prediction only.
**No clinical trials and no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records. Product names (e.g., "Muscle & Back Pain Relief", "Analgesic and Muscle Relaxant") point to muscle spasm and back pain |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methocarbamol is known as a centrally acting muscle relaxant, and it is used for painful muscle spasm and back pain. Beyond that, its precise mechanism cannot be assessed from the data compiled for this report.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots and is usually a surgical emergency. A muscle relaxant might ease spasm and pain linked to back conditions, but it would not treat the compression that causes the syndrome. The mechanistic link is therefore weak, and the high score most likely reflects network associations rather than biological evidence.

Other top-ranked predictions include irritable bowel syndrome, several eye inflammation conditions (panuveitis, iris disease, uveitis, conjunctivitis), anaphylaxis, food-dependent exercise-induced anaphylaxis and cardiac conduction or rhythm disorders. None of these has supporting trials, and the eye-related predictions appear to form a correlated cluster rather than independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For cauda equina syndrome, currently no related literature available.

Two publications were retrieved for the rank-4 prediction (anaphylaxis). Neither shows therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20086833](https://pubmed.ncbi.nlm.nih.gov/20086833/) | 1998 | Review | The Physician and Sportsmedicine | Management of arthropod bites and stings. Methocarbamol is mentioned as one option for systemic reactions to widow spider bites; anaphylaxis itself is treated with epinephrine |
| [42543011](https://pubmed.ncbi.nlm.nih.gov/42543011/) | 2026 | Review | Orvosi Hetilap | Compares side-effect profiles of centrally acting muscle relaxants, including methocarbamol. This is safety information, not efficacy in anaphylaxis |

---

## Canada Market Information

All 16 licences are valid single-ingredient authorizations. Dosage form and approved indication text are not available in the data compiled for this report. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01932187 | ROBAXIN 750 | Not available | Not available |
| 02377462 | ANALGESIC AND MUSCLE RELAXANT | Not available | Not available |
| 02239141 | EXTRA STRENGTH MUSCLE & BACK PAIN RELIEF | Not available | Not available |
| 02230949 | ROBAXISAL EXTRA STRENGTH | Not available | Not available |
| 02357356 | EXTRA STRENGTH TYLENOL BODY PAIN NIGHT | Not available | Not available |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from a computational knowledge graph, not from label text): epilepsy, kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease (including active), gout, substance abuse/dependence, hemophilia, anaemia, thrombocytopenic purpura, gastritis, Reye syndrome, Alzheimer disease, Pick disease, cerebellar degeneration, von Willebrand disease, and others. Many of these likely reflect the aspirin, acetaminophen or ibuprofen partners in combination products rather than methocarbamol itself.
- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: morphine (including liposomal morphine). Additive central nervous system depression is the likely concern.
  - **Moderate**: dronabinol, nabilone, metoclopramide, opium, sibutramine.
  - Many others are of unknown severity (e.g., metformin, omeprazole, prednisone, doxycycline).

Label warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no trials or supporting publications. The mechanistic link is weak, because cauda equina syndrome is a compressive emergency that a muscle relaxant would not treat. The other top predictions are similarly unsupported.

**To proceed, the following is needed:**
- Mechanism of action data for methocarbamol
- Package insert warnings and contraindications from Health Canada, to allow safety screening
- Approved indication text and dosage forms for the Canadian licences
- Any clinical or preclinical evidence for the predicted indication, or a better-supported candidate from the list (for example, irritable bowel syndrome, where a spasm-related rationale is conceivable but still untested)
- Reclassification of the obsolete "bundle branch block" term before any further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

