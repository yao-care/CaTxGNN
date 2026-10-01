---
layout: default
title: Apixaban
parent: Moderate Evidence (L3-L4)
nav_order: 65
evidence_level: L4
indication_count: 10
---

# Apixaban
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Apixaban: From Thromboembolism Prevention to Migraine Disorder

## One-Sentence Summary

Apixaban is an oral anticoagulant used to prevent stroke and blood clots (per the registered trial titles in the evidence pack, its approved uses include non-valvular atrial fibrillation and post-surgical venous thromboembolism prevention).
The TxGNN model predicts it may be effective for **migraine disorder**, but the evidence is thin and points the wrong way: **1 indirect clinical trial** and **4 publications**, of which the two apixaban-specific case reports describe worsening or no benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thromboembolism prevention (stroke prevention in atrial fibrillation, VTE prevention). Not stated in the Health Canada license records provided; inferred from registered trial titles |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Apixaban is a selective factor Xa inhibitor, and its efficacy in preventing thromboembolism is established. Mechanistically, it could be relevant to migraine only through an indirect thrombotic route.

The proposed link is speculative. Some migraine with aura may involve paradoxical embolism (for example via a patent foramen ovale) or antiphospholipid antibody-related clotting. If so, anticoagulation might help. Some older case reports describe migraine improving on warfarin or heparin.

The apixaban-specific literature does not support this. One case report describes aura worsening after apixaban was started. Another describes a patient whose aura had been in remission on warfarin, returned within 3 weeks of switching to apixaban, and resolved again after warfarin was resumed. The high TxGNN score is therefore not backed by clinical data.

Two other migraine-related nodes in the prediction list (migraine with brainstem aura, and migraine susceptibility) reuse the same case reports and add no independent support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSE trial: PFO closure or anticoagulants versus antiplatelet therapy to prevent stroke recurrence. Migraine is not a primary endpoint and apixaban is not the specific comparator, so it gives indirect PFO/stroke context only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients; agent and design need verification) | Lupus | Response to antithrombotic therapy in refractory migraine with antiphospholipid antibodies; the abstract reports no specific results |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report | The Neurologist | Migraine with aura worsened after starting apixaban; the evidence for direct oral anticoagulants in migraine is described as scarce and controversial |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura in remission on warfarin returned on apixaban and resolved again on warfarin |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case report | Headache | Vestibular migraine resolving on warfarin and topiramate; does not involve apixaban |

---

## Canada Market Information

Apixaban has 20 licenses in Canada; 5 are listed below. Dosage form and approved-indication text are not populated in the license records provided.

| DIN | Product Name |
|---------|------|
| 2527987 | BIO-APIXABAN |
| 2486806 | AURO-APIXABAN |
| 2510464 | TARO-APIXABAN |
| 2546884 | NRA-APIXABAN TABLETS |
| 2530724 | PRO-APIXABAN |

---

## Safety Considerations

- **Reported signal from the literature**: Two case reports describe migraine with aura worsening or returning after apixaban was started or substituted for warfarin (PMIDs 37582651, 28960288).

Please refer to the package insert for other safety information. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only clinical trial is indirect, the apixaban case reports describe worsening or no benefit, and the anticoagulant-responsive cases involved warfarin, not apixaban. The evidence does not justify further investment in migraine at this time.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Verification of the design, agent and results of the antiphospholipid-antibody study (PMID 33402037)
- Prospective controlled data in a defined subgroup (for example migraine with aura and PFO, or antiphospholipid antibody positive) before any re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

