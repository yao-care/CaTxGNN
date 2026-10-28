---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-28
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Relations recorded in the knowledge graph (not label text): dermatiti…"
---

# Lidocaine
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

## Lidocaine: From Local Anaesthesia and Neuralgia to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a sodium channel–blocking local anaesthetic, with relations recorded in the knowledge graph for conditions such as dermatitis, neuralgia, postherpetic neuralgia, haemorrhoids and scabies.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not label text): dermatitis, neuralgia, postherpetic neuralgia, haemorrhoids, scabies and others. Licence records contain no indication text |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lidocaine is generally known as a voltage-gated sodium channel blocker that numbs sensory nerves, and it is used as a local anaesthetic.

The link to punctate epithelial keratoconjunctivitis is weak. Any plausible benefit would be symptomatic pain relief, not treatment of the underlying disease. Topical anaesthetics can also damage the corneal epithelium with prolonged use, which argues against a therapeutic role. The very high TxGNN score is a computational prediction only and is not backed by any trial or publication on this disease.

For reference, the other top-ranked predictions are also ocular or renal conditions (papillary conjunctivitis, rosacea conjunctivitis, exposure keratitis, atopic conjunctivitis, nephrotic syndrome). All of them are likewise at the L5 or low-evidence stage, except where noted below.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## Canada Market Information

At least 20 single-ingredient lidocaine licences are valid in Canada; the list below is partial and shows 5 of them. The licence records contain no dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02485311 | LIDOCAINE | Not listed | Not listed |
| 02372983 | XYLOCAINE 0.5% | Not listed | Not listed |
| 02422018 | LIDOCAINE HYDROCHLORIDE INJECTION USP | Not listed | Not listed |
| 02462443 | LIDOCAINE INJECTION BP | Not listed | Not listed |
| 02003767 | XYLOCAINE SPRAY | Not listed | Not listed |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: the knowledge graph lists contraindication relations with, among others, hypertension, liver failure and liver disease, cirrhosis, epilepsy, kidney disease, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, herpes simplex virus keratitis, varicella zoster infection, atopic eczema, osteoporosis, psychotic and other mental disorders, fungal infections and gastritis. These should be verified against the package insert.
- **Drug Interactions**: 100 interactions were found. The main ones listed here are:
  - Major: bupropion.
  - Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid, sodium sulfate.
  - Minor: dexamethasone, kanamycin, neomycin, omeprazole, streptomycin, troglitazone.
- **Reported adverse events in the literature**: neuropsychiatric and cardiac side effects with intravenous lidocaine (PMID 19250287); methemoglobinemia in a child with nephrotic syndrome using topical lidocaine, benzocaine and co-trimoxazole (PMID 41995267).

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No trial or publication studies lidocaine in punctate epithelial keratoconjunctivitis, so the evidence level is L5. The mechanism offers at most symptomatic relief, and prolonged topical anaesthetic use can harm the corneal epithelium.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for the disease
- Preclinical or clinical studies that directly address punctate epithelial keratoconjunctivitis, including corneal safety
- Health Canada package insert warnings and contraindications, and approved indication text for the licences
- Route and formulation compatibility assessment (ophthalmic use)

**Note on other predictions:** Among the other ranked predictions, only "conjunctival disorder" has substantial material (a completed Phase 4 trial and pterygium surgery studies). These concern procedural anaesthesia, not treatment of conjunctival disease, and the SUNCT/SUNA papers concern a headache syndrome. They may be worth considering as a separate research question, but they do not support the lead prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

