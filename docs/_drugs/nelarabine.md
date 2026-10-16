---
layout: default
title: Nelarabine
parent: Model Prediction Only (L5)
nav_order: 646
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Nelarabine: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). Approved use: Acute lymphoblastic leukemia…"
---

# Nelarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Nelarabine: From T-Cell Acute Lymphoblastic Leukemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine was originally used to treat T-cell acute lymphoblastic leukemia and T-lymphoblastic lymphoma.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia, precursor T-cell acute lymphoblastic leukemia, T-cell leukemia, T-lymphoblastic lymphoma (from the knowledge graph; Canadian licence text is not available) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nelarabine is a prodrug of ara-G, a deoxyguanosine analogue. Ara-G is converted intracellularly to ara-GTP, which is incorporated into DNA and causes selective cytotoxicity in lymphocytes, especially T cells. This mechanism has not been independently verified here.

Relapsing-remitting multiple sclerosis is driven largely by autoreactive T cells (and B cells). A drug that depletes lymphocytes is therefore conceptually relevant. Cladribine, another purine analogue, is already approved for MS, which gives this idea some precedent.

However, the link is hypothetical. Nelarabine carries a well-known boxed warning for severe neurotoxicity, including somnolence, confusion, seizures, peripheral neuropathy, and demyelination or Guillain-Barré-like syndromes. In a demyelinating disease of the central nervous system, this is a serious conflict that may outweigh any theoretical benefit. The very high TxGNN score (0.994) is a model output only and has not been validated.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02299925 | ATRIANCE | Not available | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue) |
| Myelosuppression Risk | Medium to high (neutropenia, thrombocytopenia and anaemia are listed among the knowledge-graph contraindication associations) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, bilirubin, and regular neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, epilepsy, thrombocytopenia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anaemia, macrocytic anaemia, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, impaired renal function, learning disability, intellectual disability, demyelinating disease, and inflammatory demyelinating polyradiculoneuropathy. The demyelinating disease association is especially relevant to multiple sclerosis.
- **Drug Interactions**: 100 interactions were found in total. Examples of **Major** interactions are:
  - Bupropion
  - Deferiprone
  - Iopamidol
  - Iohexol
  - Samarium (153Sm) lexidronam

  Examples of **Moderate** interactions are:
  - Metronidazole
  - Tinidazole
  - Rosuvastatin
  - Simvastatin
  - Chloroquine
  - Hydroxychloroquine
  - Disulfiram
  - Palifermin

Label warnings and contraindications from the Health Canada package insert were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or publications. In addition, nelarabine's neurotoxicity and demyelination warnings directly conflict with a demyelinating disease such as multiple sclerosis. Under the evidence level rules this is L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Verified mechanism of action data from DrugBank
- Preclinical or mechanistic evidence in MS models, such as experimental autoimmune encephalomyelitis
- A neurotoxicity risk-benefit assessment specific to demyelinating disease
- Approved indication text and dosage form details for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

