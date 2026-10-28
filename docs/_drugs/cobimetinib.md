---
layout: default
title: Cobimetinib
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Cobimetinib: predicted new indication Amyotrophic lateral sclerosis (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "COBIMETINIB"
predicted_indications: ["amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "Mills syndrome", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "amyotrohpic lateral sclerosis type 22", "monomelic amyotrophy"]
---

# Cobimetinib
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

## Cobimetinib: From Metastatic Melanoma to Amyotrophic Lateral Sclerosis
{: .text-alpha }

## One-Sentence Summary

Cobimetinib was originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **amyotrophic lateral sclerosis (ALS)**, but **no clinical trials and no publications** currently support this direction. The prediction is based on the computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Amyotrophic lateral sclerosis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cobimetinib is a MEK1/2 inhibitor. Its efficacy in metastatic melanoma is established, and it acts on the MAPK/ERK signalling pathway.

MAPK/ERK signalling has been implicated in neuroinflammation and motor neuron stress responses in ALS models, so a plausible but unvalidated link exists. The very high TxGNN score (0.9973) is a computational prediction only and does not replace experimental or clinical evidence.

There are important weaknesses in this rationale. Cobimetinib has limited central nervous system penetration (it is a P-gp substrate), which undermines the case for treating a brain and spinal cord disease. Most of the other top-ranked predictions are motor neuron conditions or very rare genetic syndromes. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a specific MEK-dependent mechanism. These include Mills syndrome, ALS type 22, lower motor neuron syndrome, monomelic amyotrophy, and lethal arthrogryposis-anterior horn cell disease syndrome. Several of them overlap with the ALS signal and are not independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02452340 | COTELLIC | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The 20 listed in the compiled data include these:
  - **Major**: aprepitant, dexamethasone, clarithromycin, cobicistat, samarium (153Sm) lexidronam
  - **Moderate**: cimetidine, clotrimazole, eliglustat, metreleptin, miconazole, naltrexone, rolapitant, troglitazone, deferasirox, palifermin, strontium chloride Sr-89, fostamatinib, ticagrelor, quinine, ivacaftor
- **Retinal toxicity**: MEK inhibitors, including cobimetinib, are associated with retinal toxicity (serous retinopathy). This matters especially for predicted indications with retinal involvement, such as trichomegaly-retina pigmentary degeneration-dwarfism syndrome.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score, with no clinical trials or publications (Evidence Level L5). The mechanistic link to ALS is plausible but unvalidated, and limited CNS penetration weakens it further. The safety information from the package insert is also incomplete.

**To proceed, the following is needed:**
- Preclinical evidence of MEK inhibition benefit in ALS models, including evidence of adequate CNS exposure
- Health Canada package insert warnings and contraindications, so that safety screening can proceed
- Detailed mechanism of action data
- A risk-benefit assessment for a chronic neurological indication, given the known toxicities of MEK inhibitors, including retinal toxicity
- Review of the interaction profile, especially the Major interactions, for patients with ALS who take multiple medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

