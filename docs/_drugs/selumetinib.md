---
layout: default
title: Selumetinib
parent: Model Prediction Only (L5)
nav_order: 836
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: From NF1 Plexiform Neurofibromas to Familial Generalized Lentiginosis

## One-Sentence Summary

Selumetinib is a MEK1/2 inhibitor, marketed in Canada as KOSELUGO and approved for NF1-related plexiform neurofibromas. The TxGNN model predicts it may be effective for **familial generalized lentiginosis** with a very high score (99.96%), but there are currently **0 clinical trials** and **0 publications** for this specific disease, so the prediction rests on the model alone. Among the other predicted indications, **peripheral nerve schwannoma** has the strongest support (1 Phase 2 trial and 7 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NF1-related plexiform neurofibromas (taken from the evidence pack's rationale text; the Canadian licence records contain no indication text) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Selumetinib inhibits MEK1/2, key kinases in the RAS/MAPK signalling pathway. Mechanism-of-action data were not supplied in structured form. This description comes from the pack's rationale text.

Some lentiginosis syndromes involve RAS/MAPK dysregulation, as in the RASopathies. Selumetinib's established use in NF1, itself a RASopathy, makes a link plausible.

This link is only a hypothesis. No gene-, pathway- or disease-specific evidence is supplied for familial generalized lentiginosis. The high score reflects graph-based similarity in the knowledge graph, not clinical support. The other pigmentary and skin syndromes in the top 10 (rank 2 and ranks 4–8) have the same limitation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for familial generalized lentiginosis.

---

## Literature Evidence

Currently no related literature available for familial generalized lentiginosis.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2530147 | KOSELUGO |
| 2530139 | KOSELUGO |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature, and only a speculative mechanistic link, so it stays at L5. It is not actionable beyond generating a research hypothesis.

**Better-supported candidates in the same pack:**
- **Peripheral nerve schwannoma (rank 9, L3):**
  - Phase 2 trial [NCT03095248](https://clinicaltrials.gov/study/NCT03095248) of selumetinib in NF2-related tumours was terminated with only 10 patients enrolled, so it cannot support an efficacy conclusion.
  - Supporting literature includes a selumetinib case report in NF2 ([PMID 38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/)) and preclinical MEK inhibitor work in schwannoma cells ([PMID 19804833](https://pubmed.ncbi.nlm.nih.gov/19804833/)).
  - It is the most credible lead and is labelled "Research Question".
- **Rhabdoid tumour (rank 3, L4):**
  - The only trial is the molecular-matched pediatric umbrella protocol [NCT03155620](https://clinicaltrials.gov/study/NCT03155620), which is not rhabdoid-specific.
  - Preclinical support is limited to ATRT work on the MAPK pathway ([PMID 25638158](https://pubmed.ncbi.nlm.nih.gov/25638158/)).

**To proceed, the following is needed:**
- Gene, pathway or phenotype evidence tying familial generalized lentiginosis to MAPK signalling
- Health Canada package insert warnings and contraindications for a safety screen
- Structured mechanism-of-action data from DrugBank
- Indication text, dosage form and manufacturer for the two KOSELUGO DINs
- Route-compatibility and similarity-to-original assessments (currently pending)
- A focused review of schwannoma as the priority repurposing question, including any results from NCT03095248

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

