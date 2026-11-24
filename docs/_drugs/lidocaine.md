---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-11-24
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
| Canada Market Status | Marketed (marketed DINs on record: at least 19; cancelled: 1) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lidocaine: "Lidocaine hydrochloride exerts an antiarrhythmic effect by increasing the electrical stimulation threshold of the ventricle during diastole. In usual therapeutic doses, lidocaine hydrochloride produces no change in myocardial contractility, in systemic arterial pressure, or in absolute refractory period." ([DailyMed: Lidocaine Hydrochloride And Dextrose (lidocaine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f21512ea-c7c3-4766-b976-b2c0b5616bf0), label version 2026-02-20; accessed 2026-11-19.) Lidocaine is generally known as a voltage-gated sodium channel blocker that numbs sensory nerves, and it is used as a local anaesthetic.

The link to punctate epithelial keratoconjunctivitis is weak. Any plausible benefit would be symptomatic pain relief, not treatment of the underlying disease. Topical anaesthetics can also damage the corneal epithelium with prolonged use, which argues against a therapeutic role. The very high TxGNN score is a computational prediction only and is not backed by any trial or publication on this disease.

For reference, the other top-ranked predictions are also ocular or renal conditions (papillary conjunctivitis, rosacea conjunctivitis, exposure keratitis, atopic conjunctivitis, nephrotic syndrome). All of them are likewise at the L5 or low-evidence stage, except where noted below.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## Canada Market Information

At least 20 single-ingredient lidocaine licences are valid in Canada. The licence records contain no dosage form or approved indication text.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00001732 | XYLOCAINE 1% | LIDOCAINE HYDROCHLORIDE | Marketed |
| 00001937 | XYLOCARD | LIDOCAINE HYDROCHLORIDE | Marketed |
| 00436208 | LIDOCAINE HYDROCHLORIDE INJECTION USP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 01901982 | LIDOCAINE HYDROCHLORIDE INJECTION USP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02003767 | XYLOCAINE SPRAY | LIDOCAINE | Marketed |
| 02231147 | LIDODAN ENDOTRACHEAL NON-AEROSOL SPRAY | LIDOCAINE (LIDOCAINE HYDROCHLORIDE) | Marketed |
| 02245939 | MAXILENE 5 | LIDOCAINE | Marketed |
| 02372983 | XYLOCAINE 0.5% | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02419505 | LIDODAN 4% TOPICAL SOLUTION | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02422018 | LIDOCAINE HYDROCHLORIDE INJECTION USP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02422026 | LIDOCAINE HYDROCHLORIDE INJECTION USP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02462443 | LIDOCAINE INJECTION BP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02469146 | JELIDO | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02485311 | LIDOCAINE | LIDOCAINE | Marketed |
| 02522268 | LIDOCAINE HYDROCHLORIDE INJECTION | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02530449 | LIDOCAINE INJECTION BP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02542218 | LIDOCAINE HYDROCHLORIDE INJECTION | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02542838 | SOLARCAINE BURN PAIN RELIEF | LIDOCAINE HYDROCHLORIDE | Marketed |
| 02547856 | LIDOCAINE HYDROCHLORIDE INJECTION USP | LIDOCAINE HYDROCHLORIDE | Marketed |
| 01923986 | SOLARCAINE FIRST AID LIDOCAINE SPRAY | LIDOCAINE | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lidocaine Hydrochloride And Dextrose (lidocaine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f21512ea-c7c3-4766-b976-b2c0b5616bf0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

