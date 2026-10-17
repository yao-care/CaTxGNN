---
layout: default
title: Apremilast
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Apremilast: predicted new indication Migraine disorder (evidence level L5). Approved use: Psoriatic arthritis"
monitor_inn: "Apremilast"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis to Migraine Disorder

## One-Sentence Summary

Apremilast is an oral PDE4 inhibitor, originally used to treat psoriatic arthritis.
The TxGNN model predicts it may be effective for **migraine disorder**,
but **no clinical trials and no publications** currently support this prediction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriatic arthritis |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for apremilast is not available in the data compiled for this report. Based on published literature, apremilast is an oral small-molecule inhibitor of type-4 cyclic nucleotide phosphodiesterase (PDE4). Blocking PDE4 raises intracellular cAMP and dampens the production of pro-inflammatory cytokines. This is consistent with its approved use in psoriatic arthritis.

PDE4 inhibition may plausibly modulate neuroinflammation and cAMP signalling, and PDE4 is highly expressed in the brain. A review of PDE4 as a target in neurological disorders (PMID 32673703) discusses this general area. However, the data compiled here do not support a direct link between PDE4 inhibition and migraine pathophysiology. The high score is a statistical output of the knowledge-graph model, not independent evidence.

Several other top-ranked predictions also lack support. The second prediction, migraine with brainstem aura, appears to inherit its score from the broader migraine node. The fifth prediction, migraine susceptibility, retrieved only papers on apremilast safety and psoriatic arthritis treatment satisfaction. The safety paper may even be relevant to headache as an adverse event, which argues against a benefit.

**Context from other predictions:** Rheumatoid arthritis (rank 3, score 98.09%) is the only predicted indication with clinical trials and a randomised trial publication (see below). It is mechanistically the best supported, though it is not the primary prediction in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For reference, the following trials relate to the third-ranked prediction, rheumatoid arthritis. They are not evidence for migraine.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Randomised, double-blind, placebo-controlled study of two apremilast doses in RA patients with inadequate response to methotrexate. Termination reason not provided |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Placebo-controlled trial of apremilast in active RA. Results not provided |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Add-on apremilast in RA despite TNF inhibitor and methotrexate. No participants enrolled |

---

## Literature Evidence

Currently no related literature available for migraine disorder.

For reference, selected publications on the rheumatoid arthritis prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | RCT | Arthritis & Rheumatology | Phase 2 placebo-controlled study of apremilast in active RA with inadequate response to methotrexate |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Preclinical | Arthritis Research & Therapy | Apremilast inhibited spontaneous TNF-α production from human RA synovial cells and ameliorated experimental arthritis |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Preclinical | Frontiers in Immunology | Apremilast ameliorated mouse arthritis by suppressing Th1/Th17 cells and enhancing regulatory T cells |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Review | Drugs | First global approval of apremilast (PDE4 inhibitor) for active psoriatic arthritis |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | Pharmacokinetic study | Clin Pharmacol Drug Dev | Pharmacokinetic effect of coadministering apremilast and methotrexate in RA and PsA patients |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02434334 | OTEZLA | Not specified | Not specified |
| 02434318 | OTEZLA | Not specified | Not specified |
| 02521733 | PMS-APREMILAST | Not specified | Not specified |
| 02528959 | JAMP APREMILAST | Not specified | Not specified |
| 02529092 | SANDOZ APREMILAST | Not specified | Not specified |

Eleven valid single-ingredient DINs are listed in total, including generics from Apotex, Auro, GLN, JAMP, PMS and Sandoz.

---

## Safety Considerations

**Drug Interactions:** The interaction screen identified 75 potential interactions. The first 20 listed include:
- **Major:** lumacaftor, fosphenytoin, apalutamide
- **Moderate:** dexamethasone, troglitazone, deferasirox, fostamatinib, betrixaban, lusutrombopag, griseofulvin, elagolix, somatrem, somatotropin, abametapir (topical), amobarbital, aminoglutethimide, bexarotene, binimetinib, bosentan
- **Minor:** armodafinil

Several of the major and moderate interactions involve enzyme inducers. The full list of 75 should be reviewed in the package insert.

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a model score alone (L5), with no trials, no relevant literature and no demonstrated mechanistic link. Safety label data is also missing. Evidence is currently insufficient to justify development.

**To proceed, the following is needed:**
- Mechanism-of-action data for apremilast, and evidence linking PDE4 inhibition to migraine pathophysiology
- Preclinical or exploratory clinical data in migraine
- Health Canada package insert warnings and contraindications, which are needed before safety screening
- Approved indication text and dosage forms for the Canadian licences
- A decision on whether to prioritise the rheumatoid arthritis prediction instead. It has a completed Phase 2 RCT, but the drug has not progressed to Phase 3 for RA and the efficacy results were not available for this assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

