---
layout: default
title: Paliperidone
parent: Moderate Evidence (L3-L4)
nav_order: 592
evidence_level: L3
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

Paliperidone (9-hydroxyrisperidone) is an atypical antipsychotic already used for schizophrenia and schizoaffective disorder, though it is not currently marketed in Canada (0 DIN records). Among the ten TxGNN-predicted indications in this evidence pack, only **treatment-refractory schizophrenia** is supported by real clinical and literature evidence (**4 clinical trials, 2 publications**); the other nine top-scoring predictions (rare congenital/genetic disorders) have no supporting trials or relevant literature and are flagged in the model's own rationale as likely graph-embedding artifacts rather than genuine signals.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / schizoaffective disorder (established use; not derivable from Canadian licensing data since the drug is unmarketed) |
| Predicted New Indication | Treatment-refractory schizophrenia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Paliperidone is the active metabolite of risperidone and acts primarily as a D2 dopamine receptor and 5-HT2A serotonin receptor antagonist — a mechanism firmly established within the core pharmacology of schizophrenia treatment. Treatment-refractory schizophrenia is not a novel disease target in the way TxGNN repurposing candidates usually are; it is a difficult-to-treat subtype of the drug's own approved disease class. This explains why this candidate reaches evidence level L3 (backed by an actual completed Phase 4 case series and ongoing trials) while the model's numerically higher-scoring predictions do not.

The other nine predictions in this evidence pack — retinal dystrophy, X-linked myopia, syndromic myopia, hydranencephaly, a congenital glycosylation disorder, X-linked female-limited myopia, a perisylvian polymicrogyria syndrome, Charcot-Marie-Tooth disease type 1G, and atypical glycine encephalopathy — all scored higher by raw TxGNN probability (99.85–99.92%) but returned **zero clinical trials** and either zero or only tangentially related literature (mostly general ophthalmology/neurology reviews with no mention of paliperidone). Each entry's own repurposing rationale explicitly states there is no known mechanistic link and attributes the high score to knowledge-graph embedding similarity rather than causal evidence. These are correctly scored L5/Hold and are not pursued further in this report; they are noted here only for transparency since they numerically outrank the schizophrenia signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating effectiveness of paliperidone palmitate across schizophrenia patient subgroups |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Pharmacotherapy combined with recovery-oriented programs (RECOVERYTRSGR) for treatment-resistant schizophrenia; paliperidone's specific role within the combination regimen is not fully specified |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label RCT comparing aripiprazole vs. paliperidone/risperidone using multi-omics data in first-episode psychosis; paliperidone is one of two comparator arms |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated (n=5) | 5 | Clozapine vs. non-clozapine antipsychotics — immune/inflammatory marker comparison in treatment-resistant schizophrenia; terminated early, low relevance to paliperidone specifically |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews psychopharmacologic evidence for schizoaffective disorder; notes absence of disorder-specific treatment guidelines, with antipsychotics (including paliperidone-class agents) as mainstay |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Reviews psychopharmacologic management of early-onset schizophrenia spectrum disorders in adolescents, including dosing and switching strategies |

## Canada Market Information

Paliperidone currently has no Health Canada marketing authorization on record (0 DIN, market status: not marketed). No license entries are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available for this compound in the evidence pack — this is flagged as a **blocking data gap (DG001)**, since Health Canada label warnings/contraindications have not yet been retrieved.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The treatment-refractory schizophrenia signal is mechanistically sound (extension within paliperidone's own established receptor pharmacology) and is supported by one completed Phase 4 real-world case series plus several ongoing/ambiguous-role trials — enough to justify continued evaluation, but not yet strong enough (no completed RCT specific to this subtype) for an unconditional Go. The nine other top-ranked TxGNN predictions in this pack should be held (Hold) — they lack any supporting trial or literature evidence and are explicitly flagged by the model's own rationale as likely artifacts of graph-embedding similarity.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain Health Canada product label warnings/contraindications before any safety review can proceed
- Resolve DG002: confirm formal DrugBank MOA record for paliperidone
- Since the drug holds no Canadian DIN, a market-entry/regulatory pathway assessment is required if this indication is to be pursued locally
- Seek RCT-level evidence specific to treatment-refractory schizophrenia (current evidence is largely observational, small-sample, or still recruiting)
- No further action recommended on the retinal/ophthalmic and rare congenital-disorder predictions unless independent mechanistic or experimental evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

