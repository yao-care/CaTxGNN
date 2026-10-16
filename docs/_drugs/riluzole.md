---
layout: default
title: Riluzole
parent: Model Prediction Only (L5)
nav_order: 809
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Riluzole: predicted new indication Bilateral parasagittal parieto-occipital polymicrogyria (evidence level L5). Approved use: Amyotrophic lateral sclerosis"
monitor_inn: "RILUZOLE"
predicted_indications: ["bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome", "amyotrophic lateral sclerosis, susceptibility to", "autosomal dominant mitochondrial myopathy with exercise intolerance", "amyotrohpic lateral sclerosis type 22"]
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a drug originally used to treat amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **bilateral parasagittal parieto-occipital polymicrogyria** (a rare cortical malformation), but **no clinical trials and no publications** currently support this specific prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic lateral sclerosis |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, riluzole modulates glutamate signaling and voltage-gated sodium channels. This is the basis of its use in ALS, where excitotoxicity in motor neurons is thought to play a role.

The link to polymicrogyria is speculative. Cortical malformations are often associated with epilepsy and abnormal neuronal excitability, so a modulator of glutamate and sodium channels could theoretically be relevant. No data supplied here support this link, and the very high score (0.9999) should be read as a model output only, not as evidence of efficacy.

Other top-ranked predictions were also reviewed. Several are motor neuron conditions that overlap biologically with ALS (lower motor neuron syndrome, monomelic amyotrophy, Mills syndrome, ALS type 22). These are mechanistically more plausible than the top-ranked prediction, but they also have no disease-specific trial data. Others, such as axial spondylometaphyseal dysplasia, appear to be graph-based artifacts with no evident mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02352583 | APO-RILUZOLE | Not specified | Not specified |
| 02390299 | MYLAN-RILUZOLE | Not specified | Not specified |
| 02242763 | RILUTEK | Not specified | Not specified |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

