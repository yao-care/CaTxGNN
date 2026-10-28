---
layout: default
title: Brodalumab
parent: Model Prediction Only (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brodalumab: predicted new indication Strongyloidiasis (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Brodalumab"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "chronic relapsing inflammatory optic neuropathy", "isolated optic neuritis", "recurrent idiopathic neuroretinitis", "optic perineuritis", "episcleritis periodica fugax", "nodular episcleritis"]
---

# Brodalumab
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

## Brodalumab: From an Unspecified Original Indication to Strongyloidiasis
{: .text-alpha }

## One-Sentence Summary

Brodalumab is an IL-17 receptor A antagonist marketed in Canada as SILIQ. The approved indication text is not available in the data compiled for this report.
The TxGNN model's top-ranked prediction is **strongyloidiasis**, with **0 clinical trials** and **0 publications** supporting it. This prediction is model-only and has no supporting biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the license record has no indication text) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, brodalumab is an IL-17 receptor A (IL-17RA) antagonist. It blocks signaling by IL-17 family cytokines.

There is no clear mechanistic link to strongyloidiasis. IL-17 signaling contributes to antiparasitic and mucosal host defense, so blocking it could plausibly **increase** infection risk rather than reduce it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it should not be treated as a therapeutic signal.

The other top-ranked predictions are weak too. Several are ocular or optic inflammatory conditions (eye disease, optic neuritis, neuroretinitis, episcleritis). Their rationale is only speculative Th17 involvement, and none has clinical trials. The one with some literature, "eye disease", is too broad to support a specific indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for strongyloidiasis.

For reference, the second-ranked prediction ("eye disease") has three publications. None shows therapeutic benefit, and two point to possible safety concerns:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Preclinical (animal model) | J Transl Med | IL-17R blockade with brodalumab limited experimental periodontitis; not an eye indication |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Case report | Rheumatol Int | Behçet's disease developed as a paradoxical reaction after brodalumab initiation in a patient with chronic non-bacterial osteitis |
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Pharmacovigilance analysis | Can J Ophthalmol | Real-world analysis of systemic drugs disproportionately associated with reported uveitis events |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02473623 | SILIQ | Not specified | Not specified |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not from label text): Crohn disease, inflammatory bowel disease, Crohn's colitis.
- **Drug Interactions**: 68 interactions were found. The main ones are:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, and live BCG vaccine (Tice substrain).
  - **Moderate**: roflumilast, alefacept, alemtuzumab, anakinra, canakinumab, and several vaccines (tetanus toxoid, anthrax, adenovirus type 4, live cholera, *Candida albicans* antigen). These indicate additive immunosuppression and live-vaccine concerns.
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).
- Mechanistically, IL-17 blockade may weaken host defense against infection. This is directly relevant to a parasitic infection such as strongyloidiasis.

For warnings and contraindications from the label, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongyloidiasis prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. It has no clinical trials or literature, and no plausible mechanism. The biology suggests blocking IL-17 could worsen infection risk. None of the other top-10 predictions has supportive therapeutic evidence either.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Approved indication text and dosage form for SILIQ
- Mechanism of action data confirmed from DrugBank
- Any direct preclinical or clinical evidence of benefit for the predicted indication
- A review of the immune-mediated ocular candidates (e.g., uveitis-type conditions) with narrower disease definitions, taking the paradoxical-reaction and uveitis signals into account
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

