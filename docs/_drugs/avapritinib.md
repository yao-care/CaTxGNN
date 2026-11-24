---
layout: default
title: Avapritinib
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 9
monitor_inn: "Avapritinib"
predicted_indications: ["axial spondylometaphyseal dysplasia", "bilateral parasagittal parieto-occipital polymicrogyria", "amyotrophic lateral sclerosis", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "amyotrohpic lateral sclerosis type 22", "lower motor neuron syndrome with late-adult onset", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome"]
last_modified_at: 2026-11-24
description: "Avapritinib: predicted new indication axial spondylometaphyseal dysplasia (evidence level L5). In Canada: 4 DINs (4 marketed)"
---

# Avapritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Avapritinib: KIT/PDGFRA kinase inhibitor → axial spondylometaphyseal dysplasia
{: .text-alpha }

## One-Sentence Summary

Avapritinib is a KIT/PDGFRA kinase inhibitor marketed in Canada under the brand AYVAKYT.
The TxGNN model predicts it may be relevant to **axial spondylometaphyseal dysplasia**, a rare skeletal disorder,
but **no clinical trials and no publications** were found to support this prediction, so it remains a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | axial spondylometaphyseal dysplasia |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for avapritinib: "Avapritinib is a tyrosine kinase inhibitor that targets KIT D816V, PDGFRA and PDGFRA D842 mutants as well as multiple KIT exon 11, 11/17 and 17 mutants with half maximal inhibitory concentrations (IC 50s ) less than 25 nM in biochemical assays. Certain mutations in PDGFRA and KIT can result in the autophosphorylation and constitutive activation of these receptors which can contribute to tumor and mast cell proliferation." ([DailyMed: Ayvakit (avapritinib) prescribing information, Blueprint Medicines Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=645c887c-8cd4-4623-8da9-ac223d71a8b9), label version 2026-10-20; accessed 2026-11-19.) Avapritinib is generally known as an inhibitor of the KIT and PDGFRA kinases.

Axial spondylometaphyseal dysplasia is a rare skeletal disorder reported to be linked to CFAP410 (C21orf2). No involvement of KIT or PDGFRA is known, so no mechanistic link can be established from the available data. The TxGNN score reflects a computational prediction only and should not be read as evidence of efficacy. A kinase inhibitor given after birth is also unlikely to correct a structural developmental skeletal condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02551764 | AYVAKYT | AVAPRITINIB | Marketed |
| 02551772 | AYVAKYT | AVAPRITINIB | Marketed |
| 02551780 | AYVAKYT | AVAPRITINIB | Marketed |
| 02551799 | AYVAKYT | AVAPRITINIB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All four single-ingredient licences are currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; typically includes blood counts and liver function |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the interaction database; 20 are listed in the data compiled for this report.
  - Major: aprepitant, acetylsalicylic acid, clarithromycin, dexamethasone, cobicistat, deferasirox, deferiprone, ibritumomab tiuxetan, tositumomab (I-131), samarium (153Sm) lexidronam
  - Moderate: cimetidine, clotrimazole, dexfenfluramine, fenfluramine, glycerol phenylbutyrate, metreleptin, miconazole, sibutramine, troglitazone, strontium chloride Sr-89

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (Evidence Level L5), and no plausible mechanistic link between KIT/PDGFRA inhibition and this disorder could be established. The very high score is a model output only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism of action data
- Preclinical or genetic evidence linking KIT/PDGFRA signalling to the disease
- A safety and risk-benefit assessment for the target population, including the major drug interactions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ayvakit (avapritinib) prescribing information, Blueprint Medicines Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=645c887c-8cd4-4623-8da9-ac223d71a8b9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

