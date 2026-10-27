---
layout: default
title: Fidaxomicin
parent: Model Prediction Only (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fidaxomicin: predicted new indication Staphylococcal scalded skin syndrome (evidence level L5). Approved use: Clostridium difficile colitis"
monitor_inn: "Fidaxomicin"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis", "parasitic skin disease"]
---

# Fidaxomicin
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

## Fidaxomicin: From Clostridium difficile Colitis to Staphylococcal Scalded Skin Syndrome
{: .text-alpha }

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrocyclic antibiotic originally used to treat *Clostridium difficile* colitis.
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome**,
but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis (the Health Canada licence record has no indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fidaxomicin is a narrow-spectrum macrocyclic antibiotic that inhibits bacterial RNA polymerase. It has in vitro activity against some Gram-positive organisms, including *Staphylococcus aureus*. Its efficacy in *C. difficile* colitis is established, and this Gram-positive activity is the likely basis of the model's prediction.

The link to the new indication is weak. Staphylococcal scalded skin syndrome is driven by exfoliative toxins from *S. aureus* and is normally managed with systemic anti-staphylococcal agents. Fidaxomicin is barely absorbed into the bloodstream, so it is unlikely to reach effective concentrations in skin tissue. The prediction therefore has some theoretical support (Gram-positive activity) but a major practical barrier (exposure).

Other top-ranked predictions show the same pattern:
- **Skin and eye staphylococcal infections** (bullous impetigo, impetigo, hordeolum): the organism is plausible, but there is no topical or ocular formulation, and effective alternatives already exist.
- **Botulism forms** (inhalational and toxin-mediated infectious): these are neurotoxin-driven diseases. Antibiotics have a limited role, and bacterial lysis may even increase toxin release.
- **Vulvovaginal candidiasis and parasitic skin disease**: the causes are fungi and eukaryotic parasites, against which a bacterial RNA polymerase inhibitor is not expected to work. These predictions lack a plausible mechanism.
- **Punctate epithelial keratoconjunctivitis**: often viral or inflammatory, with no clear role for an antibacterial agent.
- ***S. aureus* pneumonia**: negligible lung exposure is expected with oral fidaxomicin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (staphylococcal scalded skin syndrome).

For reference, the only publication in the top-10 predictions is linked to *S. aureus* pneumonia (rank 8). It is a general hospital medicine literature update that notes vancomycin or fidaxomicin as first-line treatment for *C. difficile* infection. It is not a study of fidaxomicin in *S. aureus* disease and provides no direct evidence for any predicted indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Review | Journal of Hospital Medicine | Summary of high-impact hospital medicine articles; notes vancomycin or fidaxomicin as first-line therapy for *C. difficile* infection (related to the rank 8 prediction, not the lead prediction) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02387174 | DIFICID | Not specified | Not specified in the data compiled |

## Safety Considerations

- **Drug Interactions**: 79 interactions were identified in total. The sample reviewed is mostly Minor, with some Moderate and one Major.
  - **Major**: Vibrio cholerae CVD 103-HgR strain live antigen (live vaccine)
  - **Moderate**: alpelisib, apalutamide, binimetinib, picosulfuric acid
  - **Minor** (examples): nifedipine, amiodarone, diltiazem, verapamil, cyclosporine, clarithromycin, erythromycin, spironolactone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.71%), but it is supported only by the model. There are no clinical trials and no relevant literature. Fidaxomicin's minimal systemic absorption is a major obstacle for a toxin-mediated systemic skin disease, and established treatments already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Evidence of tissue exposure or a new formulation (e.g., topical) that could reach the site of infection
- Preclinical or clinical data on fidaxomicin activity against *S. aureus* in skin infection models
- Route compatibility assessment between the available oral product and the route required for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

