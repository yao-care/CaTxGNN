---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From NSAID Therapy for Rheumatic Pain to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation in rheumatic conditions. The local regulatory record does not list an approved indication.
The TxGNN model ranks **acromesomelic dysplasia, Hunter-Thompson type** as its top prediction, but there are **0 clinical trials** and **0 publications** behind it, and no plausible mechanistic link. This is most likely a knowledge-graph artifact.
The strongest signal among the top 10 predictions is **ankylosing spondylitis** (rank 8), which is close to an established use rather than true repurposing (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local regulatory data (NSAID class; rheumatic pain and inflammation) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% (model rank 518) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Flurbiprofen is known to be a non-selective COX-1/COX-2 inhibitor, so it reduces prostaglandin synthesis and relieves pain and inflammation.

Acromesomelic dysplasia, Hunter-Thompson type is a rare genetic skeletal dysplasia caused by variants in the CDMP1/GDF5 pathway. No plausible connection to COX inhibition was identified. At best, an NSAID could give symptomatic pain relief, and it would not change the underlying disease.

The high score most likely reflects skeletal-phenotype proximity in the knowledge graph rather than pharmacological rationale. The prediction should not be treated as a credible repurposing lead without independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 1912038 | FLURBIPROFEN |
| 1912046 | FLURBIPROFEN |

Dosage form, manufacturer and approved indication text are empty for both entries. The identifiers are 7 digits, while Canadian DINs are 8 digits, and the evidence pack lists TFDA as its regulatory input. The source of these licences should be verified before they are reported as Canadian DINs.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature and no plausible mechanism, so it should not be pursued.
Ankylosing spondylitis (rank 8, score 99.97%) is the exception. It has 8 randomized double-blind trials from 1974–1986 comparing flurbiprofen with indomethacin, phenylbutazone or naproxen, for example [PMID 71969](https://pubmed.ncbi.nlm.nih.gov/71969/), [PMID 3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) and [PMID 4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/). The pack rates it L2 with a recommendation of Proceed with Guardrails, but this is essentially an established NSAID use.

**To proceed, the following is needed:**
- Confirm the local label indications and the source of the two licence numbers, since the original indication is empty in the record
- Obtain the package insert warnings and contraindications, which are missing and block safety screening
- Obtain mechanism of action data from DrugBank (DB00712)
- If the ankylosing spondylitis direction is pursued, evaluate it as a separate candidate, checking whether it is already on the label and reviewing the older trial data against current standards
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

