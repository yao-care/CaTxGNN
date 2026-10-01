---
layout: default
title: Ubrogepant
parent: Model Prediction Only (L5)
nav_order: 950
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

# Ubrogepant: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Ubrogepant (Canadian brand name UBRELVY) is an oral CGRP receptor antagonist, originally used for the acute treatment of migraine with or without aura in adults.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are **0 registered clinical trials** and **no publication testing this subtype**. The 19 supplied publications cover migraine in general.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (per published literature; the Canadian label text was not supplied) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (no subtype-specific studies; only mechanism-level support from the parent condition) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. The published literature describes ubrogepant as a small-molecule CGRP receptor antagonist. CGRP signalling is central to migraine pathophysiology, and ubrogepant is approved for acute migraine with or without aura.

Brainstem aura is a subtype of migraine with aura, so a CGRP-targeted drug is mechanistically plausible. The very high TxGNN score most likely reflects the drug's strong link to the parent condition (migraine) rather than a distinct repurposing signal. Gepants are not vasoconstrictors, so they may have a vascular-safety advantage over triptans in this subtype. This is a theoretical argument. It must be checked against the Canadian label and the exclusion criteria of the pivotal trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below tests the brainstem aura subtype. They support ubrogepant in migraine generally.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37979595](https://pubmed.ncbi.nlm.nih.gov/37979595/) | 2023 | RCT (Phase 3) | Lancet | Ubrogepant 100 mg vs placebo for treating migraine attacks during the prodrome (crossover design) |
| [31742631](https://pubmed.ncbi.nlm.nih.gov/31742631/) | 2019 | RCT (Phase 3) | JAMA | ACHIEVE II: ubrogepant vs placebo on pain and the most bothersome associated symptom in acute migraine |
| [31800988](https://pubmed.ncbi.nlm.nih.gov/31800988/) | 2019 | Clinical trial | N Engl J Med | Oral CGRP receptor antagonist evaluated for acute migraine treatment |
| [31913519](https://pubmed.ncbi.nlm.nih.gov/31913519/) | 2020 | Phase 3 extension trial | Headache | 52-week randomized extension evaluating long-term safety and tolerability |
| [33874756](https://pubmed.ncbi.nlm.nih.gov/33874756/) | 2021 | Post hoc analysis of RCTs | Cephalalgia | Safety and efficacy across cardiovascular risk categories in ACHIEVE I and II |
| [39569702](https://pubmed.ncbi.nlm.nih.gov/39569702/) | 2025 | Clinical trial | Headache | TANDEM: safety and tolerability of ubrogepant in people taking atogepant for prevention |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | J Headache Pain | Indirect comparison of lasmiditan vs rimegepant and ubrogepant as acute migraine treatments |
| [32020557](https://pubmed.ncbi.nlm.nih.gov/32020557/) | 2020 | Review | Drugs | First-approval summary: approved in the USA in Dec 2019 for acute migraine (± aura) in adults |
| [33948091](https://pubmed.ncbi.nlm.nih.gov/33948091/) | 2021 | Narrative review | J Pain Res | ACHIEVE I and II showed superiority over placebo for pain freedom and most bothersome symptom freedom at 2 hours |
| [39262541](https://pubmed.ncbi.nlm.nih.gov/39262541/) | 2024 | Case report | Cureus | Treatment-resistant migraine without aura with substantial improvement on ubrogepant |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2532581 | UBRELVY |
| 2532530 | UBRELVY |

Dosage form, manufacturer and approved indication text were not provided for these two authorizations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but rests on the drug's link to the parent condition. No trial or publication tests brainstem aura, and the Canadian safety documents have not been reviewed, which blocks safety screening. The other two predictions (atrophoderma vermiculata and ulerythema ophryogenesis) have no mechanistic link and no supporting evidence, and are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication), to confirm whether brainstem aura is already label-adjacent or excluded
- Mechanism of action data from DrugBank
- The exclusion criteria of the pivotal trials, especially for brainstem aura or hemiplegic subtypes
- Literature or case series specific to brainstem aura, and a check of ICTRP and ClinicalTrials.gov for registered studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

