---
layout: default
title: Riluzole
parent: Model Prediction Only (L5)
nav_order: 809
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Riluzole: predicted new indication Bilateral parasagittal parieto-occipital polymicrogyria (evidence level L5). Approved use: Amyotrophic lateral sclerosis"
monitor_inn: "RILUZOLE"
predicted_indications: ["bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome", "autosomal dominant mitochondrial myopathy with exercise intolerance"]
---

# Riluzole
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

## Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-occipital Polymicrogyria
{: .text-alpha }

## One-Sentence Summary

Riluzole is a drug originally used to treat amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **bilateral parasagittal parieto-occipital polymicrogyria** (a rare cortical malformation), but **no clinical trials and no publications** currently support this specific prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic lateral sclerosis |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for riluzole: "The mechanism by which riluzole exerts its therapeutic effects in patients with ALS is unknown." ([DailyMed: Tiglutik (riluzole) prescribing information, EDW PHARMA, INC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=75d68f19-4208-109e-e053-2991aa0ac857), label version 2026-07-27; accessed 2026-11-19.) Based on general knowledge, riluzole modulates glutamate signaling and voltage-gated sodium channels. This is the basis of its use in ALS, where excitotoxicity in motor neurons is thought to play a role.

The link to polymicrogyria is speculative. Cortical malformations are often associated with epilepsy and abnormal neuronal excitability, so a modulator of glutamate and sodium channels could theoretically be relevant. No data supplied here support this link, and the very high score (0.9999) should be read as a model output only, not as evidence of efficacy.

Other top-ranked predictions were also reviewed. Several are motor neuron conditions that overlap biologically with ALS (lower motor neuron syndrome, monomelic amyotrophy, Mills syndrome, ALS type 22). These are mechanistically more plausible than the top-ranked prediction, but they also have no disease-specific trial data. Others, such as axial spondylometaphyseal dysplasia, have no evident mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02242763 | RILUTEK | RILUZOLE | Marketed |
| 02352583 | APO-RILUZOLE | RILUZOLE | Marketed |
| 02390299 | MYLAN-RILUZOLE | RILUZOLE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All three authorizations are valid single-ingredient products.

---

## Safety Considerations

**Knowledge-graph contraindication associations** (these come from a knowledge graph, not from package insert text):
- Neutropenia and agranulocytosis
- Substance abuse/dependence
- Hyperbilirubinemia, hereditary hyperbilirubinemia, and Gilbert syndrome
- Interstitial lung disease
- Drug-induced liver injury

**Drug Interactions**: 44 interactions were identified. Examples from the first 20 listed:
- **Moderate**: obeticholic acid, naltrexone, deferasirox, osilodrostat, anagrelide, asparaginase *Escherichia coli*, brentuximab vedotin, clofarabine, methotrexate, epirubicin
- **Minor**: omeprazole, caffeine, theophylline, aminophylline
- **Severity unknown**: metformin, simvastatin, ranitidine, cyanocobalamin, salbutamol, ibuprofen

Please refer to the package insert for warnings and contraindications from the approved label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score only, with no clinical trials or literature for polymicrogyria. The mechanistic link is speculative. The Canada label information (warnings, contraindications, approved indication text) is also incomplete.

**To proceed, the following is needed:**
- Mechanism of action data for riluzole
- Health Canada package insert warnings, contraindications, and approved indication text
- Preclinical or clinical evidence in cortical malformation or malformation-associated epilepsy
- Given the knowledge-graph liver and haematological contraindication associations, a monitoring plan for liver function and blood counts
- Consideration of the motor neuron predictions (e.g., lower motor neuron syndrome, ALS type 22) as more plausible alternatives, each needing disease-specific evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tiglutik (riluzole) prescribing information, EDW PHARMA, INC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=75d68f19-4208-109e-e053-2991aa0ac857) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

