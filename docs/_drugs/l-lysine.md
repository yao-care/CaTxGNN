---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 435
evidence_level: L5
indication_count: 3
---

# L-Lysine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# L-Lysine: From No Recorded Original Indication to Gastroparesis (Prediction Not Supported by Evidence)

## One-Sentence Summary

L-Lysine (DB00123) is an essential amino acid with no approved therapeutic indication and no mechanism-of-action data recorded in this Evidence Pack.
The TxGNN model's top prediction is **Gastroparesis**, but on inspection the single supporting publication does not actually support this link —
it concerns lysine as a chemical residue in a hydrogel drug-delivery material, not L-lysine as a pharmacological agent, so evidence remains at **L5 (no real evidence)**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indications recorded, drug not marketed in Canada |
| Predicted New Indication | Gastroparesis (highest-ranked of 3 candidates; likely false positive) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned no MOA). L-lysine is an essential amino acid normally used as a nutritional supplement or feed additive; this Evidence Pack contains no record of an approved therapeutic indication to compare against, so no original-indication-to-new-indication rationale can be constructed.

More importantly, the underlying evidence for the top-ranked prediction does not hold up. The only literature match for gastroparesis (PMID 29414870) describes a gelatin-alginate hydrogel used as a physical carrier to deliver mesenchymal stem cells to the stomach — gelatin contains lysine residues as a structural/chemical component of the material, not as a pharmacologically active ingredient being tested for gastroparesis. This is very likely a string/NER co-occurrence artifact rather than genuine pharmacological evidence. The same pattern holds for the other two candidates: the congenital prothrombin/Factor X deficiency literature match (PMID 1973167) actually describes a disease-causing mutation (Gla→Lys substitution), the opposite of a therapeutic signal, and the vitamin D deficiency candidate has zero supporting trials or literature and targets an obsolete disease term. Across all three, the high TxGNN embedding scores (99.0–99.8%) should be read as model noise rather than validated biological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical/Other | Bioengineering (Basel, Switzerland) | Describes a gelatin-alginate hydrogel used to deliver mesenchymal stem cells to the stomach for gastroparesis; lysine appears only as a structural amino acid residue in the gelatin carrier, not as a tested drug — does not constitute pharmacological evidence for L-lysine itself. |

## Canada Market Information

L-Lysine is currently not marketed in Canada under this evaluation (0 licenses/DINs on record).

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/Health Canada label warnings and contraindications are flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet proceed to a formal S1 safety review.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the three TxGNN-predicted indications are supported by credible clinical or mechanistic evidence — the top candidate's only literature match is a materials-science artifact, not pharmacology, and the drug itself has no recorded original indication, MOA, or Canadian market presence to anchor a repurposing rationale.

**To proceed, the following is needed:**
- MOA data for L-lysine from DrugBank or primary literature
- TFDA/Health Canada label (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Re-run literature/trial search with pharmacological filtering to exclude string-matching false positives (e.g., "lysine" as a chemical residue rather than the active substance)
- Confirmation of any approved original indication, if one exists, to establish a genuine repurposing hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

