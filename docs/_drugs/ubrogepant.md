---
layout: default
title: Ubrogepant
parent: Model Prediction Only (L5)
nav_order: 812
evidence_level: L5
indication_count: 3
---

# Ubrogepant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ubrogepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Ubrogepant is a small-molecule CGRP (calcitonin gene-related peptide) receptor antagonist ("gepant") originally developed for the acute treatment of migraine, with or without aura. The TxGNN model predicts it may be particularly effective for **Migraine with Brainstem Aura**, a proposal currently supported by **20 publications** (including multiple completed Phase 3 RCTs of ubrogepant in the general migraine population), but with **no registered clinical trials or literature specific to the brainstem-aura subtype**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine, with or without aura (per literature evidence; no Canadian product monograph on file) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 (RCT evidence exists only for general migraine population; no dedicated trial in the brainstem-aura subtype) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data (DrugBank) is not available for this candidate. Based on the literature collected in the evidence pack, ubrogepant is a small-molecule CGRP receptor antagonist that blocks CGRP-mediated neurogenic inflammation and trigeminovascular nociceptive signaling — the pathway considered central to migraine pathophysiology (PMID [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/), [32011192](https://pubmed.ncbi.nlm.nih.gov/32011192/)). It received its first global approval (US FDA, 2019) for acute treatment of migraine with or without aura in adults (PMID [32020557](https://pubmed.ncbi.nlm.nih.gov/32020557/)).

The predicted new indication, migraine with brainstem aura, is a clinically distinct migraine subtype (formerly "basilar-type migraine") that is typically excluded from triptan use because triptans have vasoconstrictive activity. CGRP receptor antagonists such as ubrogepant do not share this vasoconstrictive mechanism, which provides a plausible pharmacological rationale for use in this subtype where vasoactive migraine drugs are cautioned against. However, none of the trials or literature in the current evidence set specifically enrolled or reported on patients with brainstem aura — the existing RCTs (ACHIEVE I/II, the prodrome trial, the 52-week extension study) were conducted in general episodic migraine populations. The mechanistic plausibility is therefore stronger than the direct clinical evidence at this time.

---

## Clinical Trial Evidence

Currently no clinical trials are registered specifically for migraine with brainstem aura. The literature below includes several completed Phase 3 RCTs, but these studied ubrogepant in the general migraine population, not this specific aura subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31800988](https://pubmed.ncbi.nlm.nih.gov/31800988/) | 2019 | RCT (ACHIEVE I) | N Engl J Med | Pivotal Phase 3 trial establishing efficacy of oral ubrogepant for acute migraine treatment |
| [31742631](https://pubmed.ncbi.nlm.nih.gov/31742631/) | 2019 | RCT (ACHIEVE II) | JAMA | Ubrogepant superior to placebo for pain freedom and most bothersome symptom freedom at 2 hours |
| [37979595](https://pubmed.ncbi.nlm.nih.gov/37979595/) | 2023 | Phase 3 RCT | Lancet | Ubrogepant 100 mg during the migraine prodrome (pre-headache) phase vs placebo, randomized crossover design |
| [31913519](https://pubmed.ncbi.nlm.nih.gov/31913519/) | 2020 | Phase 3 RCT (extension) | Headache | 52-week open-label extension confirming long-term safety and tolerability |
| [33874756](https://pubmed.ncbi.nlm.nih.gov/33874756/) | 2021 | RCT post-hoc analysis | Cephalalgia | Efficacy/safety of ubrogepant maintained across cardiovascular risk categories (ACHIEVE I/II pooled) |
| [33749826](https://pubmed.ncbi.nlm.nih.gov/33749826/) | 2021 | RCT post-hoc analysis | Headache | Efficacy of ubrogepant regardless of prior triptan response |
| [32573795](https://pubmed.ncbi.nlm.nih.gov/32573795/) | 2020 | Phase 1 RCT | Headache | No clinically relevant PK interaction between ubrogepant and sumatriptan; safety supports triptan co-administration |
| [32020557](https://pubmed.ncbi.nlm.nih.gov/32020557/) | 2020 | Review | Drugs | Summary of ubrogepant's development milestones leading to first global (FDA) approval |
| [33948091](https://pubmed.ncbi.nlm.nih.gov/33948091/) | 2021 | Narrative Review | J Pain Res | Overview of ACHIEVE I/II results and 52-week extension safety data |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook Clin Neurol | Review of second-generation gepants (ubrogepant, rimegepant) as CGRP receptor antagonists for acute migraine |

---

## Canada Market Information

Ubrogepant currently has **no Health Canada market authorization** (0 DINs, status: not marketed). No product monograph or licensed indication text is available to cite for this candidate.

---

## Safety Considerations

Please refer to the package insert / US FDA prescribing information for safety details, as no Canadian regulatory safety data (warnings, contraindications, or drug interaction data) are currently on file for this candidate — this is flagged as a **blocking data gap (DG001)** pending TFDA/Health Canada product monograph retrieval.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has a plausible mechanistic rationale and is backed by robust Phase 3 RCT evidence for ubrogepant in general migraine, but no trial or publication directly addresses the brainstem-aura subtype. Combined with the absence of any Canadian market authorization and a blocking gap in safety/contraindication data, the candidate is not ready to advance to safety review (S1).

**To proceed, the following is needed:**
- Resolve DG001: obtain official product monograph / prescribing information (warnings, contraindications, DDI) for ubrogepant
- Resolve DG002: confirm structured MOA data via DrugBank API
- Confirm Health Canada regulatory pathway/status (currently 0 DINs, not marketed)
- Seek dedicated clinical or case-series evidence in patients with migraine with brainstem aura, given this population's typical exclusion from standard migraine RCTs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

