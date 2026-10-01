---
layout: default
title: Cobimetinib
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Cobimetinib
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

# Cobimetinib: From MEK-Inhibitor Oncology Use to Amyotrophic Lateral Sclerosis

## One-Sentence Summary

Cobimetinib is a marketed cancer drug in Canada, but the Evidence Pack contains no approved-indication text for it.
The TxGNN model predicts it may be effective for **amyotrophic lateral sclerosis (ALS)**, with a score of 99.7%.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Health Canada record provided. Cobimetinib is generally known as a MEK inhibitor used in oncology. |
| Predicted New Indication | Amyotrophic lateral sclerosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Cobimetinib is generally described as a MEK1/2 inhibitor, but this is an assumption that needs to be verified against DrugBank.

If that assumption holds, the link to ALS is plausible but speculative. MAPK/ERK signaling has been discussed in ALS neuroinflammation and motor neuron stress. Nothing in the pack shows that blocking this pathway slows motor neuron loss.

A major concern is central nervous system exposure. Cobimetinib is likely a P-glycoprotein efflux substrate, so it may not reach the brain and spinal cord at useful levels. The 0.997 score reflects network proximity in the knowledge graph, not evidence that the drug works.

### Other Predicted Indications

The other nine predictions (scores 99.5–99.7%) also have no trials or literature, and all are L5 with a Hold recommendation.

- **Redundant with the ALS entry:** ALS susceptibility and ALS type 22 (the source spelling "amyotrohpic" is a typo). These should be de-duplicated against the ALS entry.
- **Motor neuron disorders near ALS in the graph:** Mills syndrome, late-adult-onset lower motor neuron syndrome, lethal arthrogryposis-anterior horn cell disease syndrome, and monomelic amyotrophy. These lack independent support. Monomelic amyotrophy is benign and self-limiting, so a MEK inhibitor's toxicity profile makes the risk-benefit balance unfavorable.
- **No plausible mechanistic link:** bilateral parasagittal parieto-occipital polymicrogyria, axial spondylometaphyseal dysplasia, and trichomegaly-retina pigmentary degeneration-dwarfism syndrome. These are likely graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2452340 | COTELLIC | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor, assumed; not confirmed by pack data) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | The pack's rationale notes dermatologic, ocular, hepatic and cardiac toxicities; specific monitoring should follow the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack contains no warnings or contraindications, and the drug-interaction query returned no results. This is a data gap and does not mean the drug is safe. Toxicities noted in the prediction rationale (dermatologic, ocular, hepatic, cardiac) would need to be weighed against any benefit in a progressive neurodegenerative disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ALS prediction has no supporting trials or literature (L5) and no confirmed mechanism. Doubtful CNS penetration and notable MEK-inhibitor toxicities further weaken the case. Safety screening also cannot proceed, because the Health Canada package insert data is missing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication), which is currently blocking safety screening
- Confirmed mechanism-of-action data from DrugBank
- Preclinical evidence that MEK/ERK inhibition is relevant in ALS models, and data on brain penetration
- A search of clinical trial registries and PubMed for cobimetinib or MEK inhibitors in ALS and motor neuron disease
- De-duplication of the ALS-related predictions (ALS, ALS susceptibility, ALS type 22)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

