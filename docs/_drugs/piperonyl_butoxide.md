---
layout: default
title: Piperonyl Butoxide
parent: Model Prediction Only (L5)
nav_order: 734
evidence_level: L5
indication_count: 10
---

# Piperonyl Butoxide
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

# Piperonyl Butoxide: From Ectoparasiticide Synergist (No Approved Indication on Record) to Trombiculiasis

## One-Sentence Summary

Piperonyl butoxide (PBO) is a pesticide synergist found in ectoparasiticide products, but the record lists no approved indication for it.
The TxGNN model ranks **trombiculiasis (chigger mite infestation)** as its top predicted new indication, with **0 clinical trials** and **0 publications** directly supporting it.
The better-supported prediction is **scabies** (rank 5), which has **11 publications** but still **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Health Canada record |
| Predicted New Indication | Trombiculiasis |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. From general pharmacology, PBO is not an acaricide itself. It inhibits cytochrome P450 and esterase detoxification enzymes in arthropods, which makes pyrethrins and pyrethroids more potent against them.

Trombiculiasis is a mite (chigger) infestation, so arthropod P450 inhibition is plausible in principle. However, no trials or literature were supplied for it. The high prediction score alone is not clinical evidence.

The rest of the top 10 predictions are weak:
- **Bacterial, fungal and viral diseases** (hordeolum, impetigo, staphylococcal scalded skin syndrome, esophageal candidiasis, variola minor): PBO has no known antimicrobial activity. Impetigo may appear only because it often complicates scabies.
- **Veterinary diseases** (Aleutian mink disease, feline panleukopenia): no plausible link, and not relevant to human use. These are likely knowledge-graph artifacts.

**Scabies and Norwegian (crusted) scabies** are the more credible directions. The PBO/pyrethroid synergy rationale applies as a synergist in combination products such as pyrethrins/PBO and deltamethrin/PBO, possibly including permethrin-resistant mites. PBO is already used within these combinations, so this is closer to an existing combination use than true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for trombiculiasis. The table below shows the literature linked to **scabies** (rank 5), the best-supported prediction. Only a few of these papers evaluate PBO-containing products directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12609786](https://pubmed.ncbi.nlm.nih.gov/12609786/) | 2003 | RCT (investigator-blinded) | Eur J Dermatol | Synergised pyrethrins foam vs permethrin 5% cream in 40 scabies patients: equally effective in clinical resolution of lesions |
| [37526055](https://pubmed.ncbi.nlm.nih.gov/37526055/) | 2023 | Case series | J Dermatolog Treat | Pyrethrins/PBO foam used in permethrin-resistant scabies |
| [8272612](https://pubmed.ncbi.nlm.nih.gov/8272612/) | 1993 | Case series | Rev Med Chil | Deltamethrin/PBO in 33 scabies patients: effective and well tolerated in 32; PBO allowed shorter treatment |
| [19125173](https://pubmed.ncbi.nlm.nih.gov/19125173/) | 2009 | Laboratory study | PLoS Negl Trop Dis | Effect of insecticide synergists on scabies mite response to pyrethroids, addressing metabolic resistance |
| [12353201](https://pubmed.ncbi.nlm.nih.gov/12353201/) | 2002 | Review | Clin Infect Dis | Update of scabies and pediculosis pubis treatments; topical agents and ivermectin |
| [7540875](https://pubmed.ncbi.nlm.nih.gov/7540875/) | 1995 | Review | Clin Infect Dis | Review of ectoparasite treatment literature 1982–1992; lindane and permethrin effective |
| [19588676](https://pubmed.ncbi.nlm.nih.gov/19588676/) | 2009 | Review | Pediatr Ann | Overview of pediatric infestations |
| [16180929](https://pubmed.ncbi.nlm.nih.gov/16180929/) | 2005 | Review | Toxicol Rev | Pyrethroid poisoning and toxicity (safety context) |
| [26651923](https://pubmed.ncbi.nlm.nih.gov/26651923/) | 2016 | Cohort | Ann Dermatol Venereol | Observational study of therapeutic failure in scabies (not PBO-specific) |
| [21441056](https://pubmed.ncbi.nlm.nih.gov/21441056/) | 2011 | Case report | Joint Bone Spine | Crusted Norwegian scabies in a rheumatoid arthritis patient on tocilizumab (not PBO-specific) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2125447 | R & C Shampoo with Conditioner | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trombiculiasis, rests on model score alone (L5) with no trials or literature. Most other top-10 predictions have no plausible mechanism. Scabies is the only direction worth pursuing (L3, research question), and it is largely an existing combination use of PBO.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data, for example from the DrugBank API.
- Clinical or comparative data on PBO-containing products in scabies, especially permethrin-resistant cases.
- Any clinical evidence for trombiculiasis, if it is to be pursued.
- Route and formulation compatibility assessment (currently pending).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

