---
layout: default
title: Pimozide
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
---

# Pimozide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pimozide: From Gilles de la Tourette Syndrome to Trichotillomania

## One-Sentence Summary

> Pimozide is a diphenylbutylpiperidine-class antipsychotic, historically approved as a backup treatment for Gilles de la Tourette syndrome and used in some countries for schizophrenia.
> The TxGNN model predicts it may be effective for **Trichotillomania**,
> with **no registered clinical trials** but **10 supporting publications** (case reports, reviews, and a systematic evidence mapping) currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gilles de la Tourette syndrome (per literature evidence; not confirmed via Canadian licensing data — drug is not marketed in Canada) |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.996% (rank 164 among all predictions) |
| Evidence Level | L3 (case reports/series + one systematic evidence mapping; no dedicated RCT or clinical trial) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The drug-level record marks Pimozide's mechanism of action as a data gap, but the supporting literature consistently describes it as a diphenylbutylpiperidine-class antipsychotic acting primarily as a central dopamine D2 receptor antagonist, with additional dopamine reuptake inhibition and L-type calcium channel blocking activity (e.g., PMID 7976448, 6155678). This dopaminergic blockade underlies its historical use in Gilles de la Tourette syndrome and other hyperdopaminergic movement/behavioral conditions.

Trichotillomania (compulsive hair-pulling) sits within the obsessive-compulsive and body-focused repetitive behavior spectrum, which shares clinical and neurobiological overlap with Tourette syndrome — both are tic/impulse-control-related conditions with proposed dopaminergic dysregulation. This overlap is directly reflected in the literature: pimozide has been used as a low-dose augmentation agent added to serotonin reuptake inhibitors in serotonin-reuptake-inhibitor-refractory trichotillomania (PMID 1532960), and its broader off-label use in dermatology/psychodermatology (delusional parasitosis, psychogenic excoriation) further illustrates the same underlying rationale — dopamine antagonism applied to compulsive, tic-like, or delusional behavioral disorders that are otherwise treatment-resistant.

Mechanistically, the prediction is therefore plausible: the same D2-blocking action that controls tics in Tourette syndrome is proposed to dampen the compulsive urge-driven behavior of trichotillomania, particularly as an add-on in SRI-refractory cases. However, this rationale is built on small case series and augmentation reports rather than disease-specific controlled trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36802832](https://pubmed.ncbi.nlm.nih.gov/36802832/) | 2023 | Systematic Review (RCT evidence mapping) | J Cutan Med Surg | Evidence mapping of RCTs for primary psychodermatologic disorders; highlights the lack of clinical guidelines for pharmacological management of compulsive skin/hair-pulling-type conditions |
| [15554735](https://pubmed.ncbi.nlm.nih.gov/15554735/) | 2004 | Review | Am J Clin Dermatol | Comprehensive review noting pimozide is FDA-approved only as backup therapy for Tourette syndrome, but is used off-label in dermatologic practice for monosymptomatic hypochondriacal psychosis |
| [30446201](https://pubmed.ncbi.nlm.nih.gov/30446201/) | 2018 | Review | Clin Dermatol | Reviews antipsychotic drugs (including pimozide) in dermatology via central D2 and peripheral receptor-blocking effects relevant to cutaneous perception |
| [27320510](https://pubmed.ncbi.nlm.nih.gov/27320510/) | 2016 | Review | Tijdschrift voor psychiatrie | Reviews treatment options for paediatric trichotillomania, noting limited pharmacotherapy research investment for this condition |
| [11475941](https://pubmed.ncbi.nlm.nih.gov/11475941/) | 2001 | Review | CNS Drugs | Proposes diagnostic criteria and treatment approaches for psychogenic excoriation, a related compulsive skin-picking disorder |
| [10497682](https://pubmed.ncbi.nlm.nih.gov/10497682/) | 1999 | Review | Ann Acad Med Singapore | Reviews trichotillomania as an under-diagnosed chronic psychiatric condition with hair-pulling behavior |
| [1532960](https://pubmed.ncbi.nlm.nih.gov/1532960/) | 1992 | Case series | J Clin Psychiatry | Low-dose pimozide augmentation of serotonin reuptake blockers described as beneficial in trichotillomania, based on phenomenological overlap with Tourette syndrome/OCD |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case report (3 cases) | J Child Adolesc Psychopharmacol | Open-label low-dose pimozide (typical neuroleptic) addition was beneficial in some SRI-refractory trichotillomania patients, motivating a follow-up risperidone case series |
| [28225970](https://pubmed.ncbi.nlm.nih.gov/28225970/) | 2017 | Case report | An Bras Dermatol | Case report of trichotillomania with dermatoscopic differential diagnosis vs. alopecia areata; notes lack of standardized treatment |
| [10900563](https://pubmed.ncbi.nlm.nih.gov/10900563/) | 2000 | Case series | Int J Psychiatry Med | Clinical profile of delusional parasitosis, a related monosymptomatic hypochondriacal psychosis historically treated with pimozide |

---

## Canada Market Information

Pimozide currently has no Health Canada Drug Identification Number (DIN) authorization — the drug is **not marketed in Canada** (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety data (key warnings, contraindications, drug interactions) are entirely unavailable, which is a **Blocking** data gap that prevents even a preliminary (S1) safety assessment; combined with zero clinical trials and no Canadian market presence, the evidence does not support advancing beyond model prediction.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings, contraindications, and cardiac (QT-prolongation) safety data (DG001, blocking)
- Confirmed mechanism of action from DrugBank or equivalent structured source (DG002)
- Prospective or controlled clinical evidence specifically evaluating pimozide in trichotillomania (current evidence is limited to case reports/series and one indirect systematic review)
- A regulatory pathway assessment, since the drug is not currently marketed in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

