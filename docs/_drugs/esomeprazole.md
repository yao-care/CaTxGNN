---
layout: default
title: Esomeprazole
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "ESOMEPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Esomeprazole: predicted new indication Duodenal obstruction (evidence level L5). In Canada: at least 20 DINs"
---

# Esomeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Esomeprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) originally used for acid-related conditions such as peptic ulcer disease and gastroesophageal reflux disease.
The TxGNN model predicts it may be useful for **duodenal obstruction**, but the evidence is thin: **0 clinical trials** and **1 publication**, a general review of PPIs that does not study this condition directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 19; dormant: 1) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for esomeprazole: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), label version 2025-12-19; accessed 2026-11-19.) Based on the known class mechanism, esomeprazole is a PPI. It blocks the H+/K+ ATPase (proton pump) in gastric parietal cells and so suppresses stomach acid. Its efficacy in acid-related disease is well established.

The high model score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | Update on PPI clinical use and pharmacokinetics. PPIs are first-choice drugs for peptic ulcer, H. pylori infection, GERD, NSAID-related GI lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux specifically. |

---

## Canada Market Information

Esomeprazole has 20 valid single-ingredient authorizations in Canada and none are cancelled. Dosage form and approved indication text were not available for these entries. Five main products:

| DIN | Product Name | Status |
|---------|------|------|
| 02244521 | NEXIUM - 20MG | Valid |
| 02244522 | NEXIUM - 40MG | Valid |
| 02300524 | NEXIUM | Valid |
| 02444712 | NEXIUM 24HR | Valid |
| 02339099 | APO-ESOMEPRAZOLE | Valid |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. Major-level ones include **acalabrutinib** and **atazanavir**. Moderate-level ones include hydrochlorothiazide, atorvastatin, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, bendamustine, bosutinib and bumetanide. Minor-level ones include acetylsalicylic acid, axitinib, bortezomib, brivaracetam and cyanocobalamin.
- **Knowledge-graph contraindication signals** (from a drug-disease network, not product label text): liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture and chronic atrophic gastritis. These need verification against the official labelling.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and only one general review, which does not study this condition. The mechanism is indirect: acid suppression does not treat bile reflux. The evidence is model prediction plus a general mechanistic argument, so I do not recommend advancing it now.

Another predicted indication in the same data, duodenal ulcer, has much stronger support: Phase 3 trials and RCTs. It is essentially already within esomeprazole's established use, so it is not a true repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism-of-action data
- Health Canada package insert warnings and contraindications
- Clinical studies of esomeprazole in duodenogastric (bile) reflux, ideally with symptom and mucosal-injury endpoints
- A comparison against therapies that target bile reflux itself

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

