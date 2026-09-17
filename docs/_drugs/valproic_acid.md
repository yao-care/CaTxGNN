---
layout: default
title: Valproic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 817
evidence_level: L3
indication_count: 10
---

# Valproic Acid
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Valproic Acid: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Valproic acid (VPA, DrugBank DB00313) is a broad-spectrum antiepileptic/mood-stabilizing drug. TxGNN's knowledge graph flags **10 candidate new indications** for this molecule, the large majority of which are rare reflex/situational epilepsy syndromes (e.g., reading seizures, startle epilepsy, audiogenic seizures). Of these, **Trigeminal Neuralgia** is the most clinically credible candidate, supported by **1 small positive clinical study (n=20)** and **multiple pharmacology reviews**, though modern confirmatory trials are still missing.

> **Note on methodology**: TxGNN's single highest-scoring prediction (*trigeminal nerve neoplasm*, 99.97%) is explicitly flagged within the evidence pack itself as a likely **false positive** — its only supporting literature is an unrelated Sturge-Weber syndrome case series. This report therefore centers on the best-*evidenced* candidate (trigeminal neuralgia) rather than the highest-*scored* one, and summarizes the remaining 9 candidates separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this data pack (`original_indications` empty; VPA is a well-established broad-spectrum antiepileptic/mood stabilizer, but no Health Canada license text was available for confirmation) |
| Predicted New Indication (lead candidate) | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.83% (rank 3917 of graph) |
| Evidence Level | L3 |
| Canada Market Status | Not marketed (Not marketed under this DrugBank entry — 0 DINs found) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** — classified internally as "Research Question" (decision stage S2); further study needed before advancing |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this entry is not available (Data Gap DG002). Based on known pharmacology, valproic acid is a broad-spectrum antiseizure medication acting via voltage-gated sodium channel blockade, GABAergic enhancement, and (at higher exposures) HDAC inhibition. Its efficacy in seizure disorders is well established.

Trigeminal neuralgia is classically treated with carbamazepine, another **voltage-gated sodium channel blocker**, and other anticonvulsants (phenytoin, clonazepam, oxcarbazepine) as first- and second-line agents. Because VPA shares the sodium-channel-blocking mechanism believed to dampen the paroxysmal ectopic discharges arising from the trigeminal root entry zone, it has a plausible mechanistic rationale for use in this indication.

This is not a purely theoretical link: a small clinical study from 1980 (n=20) directly tested sodium valproate in trigeminal neuralgia and reported meaningful pain control in roughly half of patients, and several subsequent pharmacology reviews list valproate among agents with demonstrated efficacy in this condition. However, no modern randomized trial has replicated this finding, so the evidence remains historical and preliminary.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal neuralgia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6776393](https://pubmed.ncbi.nlm.nih.gov/6776393/) | 1980 | Clinical Study | Med J Australia | Sodium valproate trialed in 20 trigeminal neuralgia patients: 6 attack-free 6–18 months, 3 with ≥50% reduction, 4 responded in combination therapy |
| [1774173](https://pubmed.ncbi.nlm.nih.gov/1774173/) | 1991 | Review | Headache | Lists carbamazepine, phenytoin, clonazepam, and valproic acid as anticonvulsants effective in trigeminal neuralgia via depression of trigeminal root entry zone potentials |
| [1408017](https://pubmed.ncbi.nlm.nih.gov/1408017/) | 1992 | Review | Oral Surg Oral Med Oral Pathol | Reviews drug management of trigeminal neuralgia; positions VPA among adjunct/alternative agents |
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Reviews antiepileptic drug use outside epilepsy, including neuropathic/neuralgic pain conditions |
| [22180190](https://pubmed.ncbi.nlm.nih.gov/22180190/) | 2012 | Review | J Investig Clin Dent | 11-year retrospective on single- vs multi-drug regimens for classic trigeminal neuralgia |
| [2931939](https://pubmed.ncbi.nlm.nih.gov/2931939/) | 1985 | Review | Acta Neurol Scand | Comprehensive VPA review covering efficacy in epilepsy and other neurological disorders |
| [7580659](https://pubmed.ncbi.nlm.nih.gov/7580659/) | 1995 | Systematic Review | BMJ | Systematic review of anticonvulsant drugs (incl. VPA) for pain management |
| [11129121](https://pubmed.ncbi.nlm.nih.gov/11129121/) | 2000 | Review | Drugs | Reviews anticonvulsant mechanisms of action for neuropathic pain syndromes |

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are recorded for this valproic acid entry in the current data pack (`total_licenses: 0`, market status "Not marketed"). This likely reflects a search/mapping gap rather than genuine absence from the Canadian market (valproic acid is marketed in Canada under products such as Depakene/Epival) and should be re-verified against Health Canada's Drug Product Database before any regulatory conclusions are drawn.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not available in this data pack (Data Gap DG001, flagged **Blocking** severity — this must be resolved before any S1 safety pre-assessment can proceed).

---

## Other TxGNN-Predicted Indications (Full Candidate Set)

For completeness, all 10 candidates generated for this drug are summarized below. Most cluster around rare **reflex/situational epilepsy syndromes**, consistent with VPA's known broad-spectrum antiseizure mechanism — but nearly all lack disease-specific human efficacy data.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------|------|------|------|------|
| 1 | Trigeminal nerve neoplasm | 99.97% | L5 | S0 | Hold | Likely **false positive** — sole literature (Sturge-Weber case series) unrelated |
| 2 | Visual epilepsy | 99.88% | L3 | S1 | Research Question | Trials found are indirect (TBI neuroprotection, amblyopia, unrelated drug) |
| 3 | **Trigeminal neuralgia** | 99.83% | L3 | S2 | Research Question | **Lead candidate** — see main report above |
| 4 | Startle epilepsy | 99.81% | L3 | S1 | Research Question | 1 direct clinical study on VPA suppression of auditory startle reflex |
| 5 | Thinking seizures | 99.81% | L4 | S0 | Hold | No direct VPA efficacy evidence for this reflex subtype |
| 6 | Orgasm-induced seizures | 99.81% | L5 | S0 | Hold | No supporting literature or trials at all |
| 7 | Eating seizures | 99.81% | L4 | S0 | Hold | Literature describes the disease only, not VPA treatment |
| 8 | Audiogenic seizures | 99.81% | L3 | S1 | Research Question | Preclinical evidence in GASH/Sal hamster model; no human data |
| 9 | Micturition-induced seizures | 99.81% | pending | pending | pending | Evidence not yet classified |
| 10 | Reading seizures | 99.79% | L3 | S2 | Research Question | Case report of VPA achieving complete seizure control in reading-induced absence seizures |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Across all 10 TxGNN-predicted indications, evidence remains at an exploratory stage (L3–L5, decision stages S0–S2). Even the best-supported candidate, trigeminal neuralgia, rests on a single small clinical study from 1980 without modern replication, and essential safety/regulatory inputs (TFDA/Health Canada warnings, MOA, market licensing) are completely missing from this pack.

**To proceed, the following is needed:**
- Retrieve Health Canada product monograph warnings and contraindications (Blocking gap DG001)
- Retrieve DrugBank MOA data to support mechanistic-link analysis (High-priority gap DG002)
- Verify actual Canadian market/licensing status for valproic acid products (this pack shows 0 DINs, which appears to be a data/mapping gap)
- Identify or design a modern controlled trial of VPA in trigeminal neuralgia to confirm the 1980 pilot findings
- For the reflex-epilepsy cluster (ranks 2, 4, 5, 7–10): triage as a group given shared mechanistic rationale, but require disease-specific confirmatory evidence before advancing any single candidate
- Discard rank-1 (trigeminal nerve neoplasm) as a likely knowledge-graph artifact unless independent supporting evidence is found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

