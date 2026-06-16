---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
---

# Erenumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab (Aimovig) is a fully human monoclonal antibody targeting the CGRP receptor, globally approved for the prevention of episodic and chronic migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic and chronic) — globally approved; not currently licensed in Canada |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Erenumab selectively blocks the calcitonin gene-related peptide (CGRP) receptor. CGRP is a potent vasodilatory and pro-inflammatory neuropeptide released during migraine attacks from trigeminal nerve terminals. By antagonizing its receptor, erenumab dampens trigeminal neuroinflammation and vasodilation — the two key drivers of migraine pain — without affecting CGRP synthesis itself. This mechanism is directly evidenced by the drug's established Phase 3 efficacy in episodic and chronic migraine (PMID 30360965), including in patients who had failed multiple prior preventive therapies.

Migraine with brainstem aura (MBA, formerly basilar-type migraine) is characterized by aura symptoms attributable to the brainstem or both hemispheres simultaneously — vertigo, dysarthria, diplopia, tinnitus — followed by typical migraine headache. Its pathophysiology specifically involves activation of brainstem nuclei (nucleus trigeminalis caudalis, periaqueductal gray, locus coeruleus) and local CGRP release; all three nuclei express CGRP receptors. This mechanistic overlap directly supports the TxGNN prediction: the same receptor-blocking action that suppresses trigeminal activation in common migraine is theoretically applicable to the brainstem-originating cascade in MBA.

A key historical safety concern was that CGRP blockade might impair compensatory vasodilation in the basilar and posterior cerebral circulation — precisely the territory involved in MBA aura. However, clinical evidence has not borne this out: erenumab did not alter cerebral vasomotor reactivity or flow-mediated dilation (PMID 32867533), and pooled long-term data showed no increase in cardiovascular or cerebrovascular events across vascular risk strata (PMID 36942409). Critically, no dedicated trial has enrolled MBA patients specifically; all available evidence is indirect extrapolation from migraine-with-aura subgroup analyses and real-world cohorts, placing this prediction at evidence level L3 pending prospective validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Erenumab specifically in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3 RCT | Lancet | Erenumab significantly reduced monthly migraine days vs. placebo in patients who failed 2–4 prior preventives; establishes efficacy in treatment-resistant episodic migraine |
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT Secondary Analysis | JAMA Neurology | Erenumab was safe and effective in both migraine with and without aura; aura status did not meaningfully modify treatment response, directly relevant to MBA subtype |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacol | Confirmed erenumab's preventive efficacy across episodic and chronic migraine in multiple RCTs; key basis for the L3 evidence rating applied here |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Prospective Cohort | Headache | Post-hoc pooled analysis: no increase in cardiovascular events with erenumab across all CV risk strata; critical vascular safety reassurance for a subtype with posterior circulation involvement |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Prospective Cohort | J Headache Pain | REFORM study: elevated plasma suPAR (systemic inflammation marker, raised in migraine with aura) linked to CGRP-pathway activity and erenumab response; supports inflammatory–CGRP mechanistic bridge |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Mechanistic Observational | Cephalalgia | Erenumab did not alter cerebral vasomotor reactivity or endothelial function in migraine without aura; addresses the key safety concern for a brainstem-aura subtype |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-World Cohort | Clin Neurol Neurosurg | 6-month Croatian real-world data: erenumab effective and well-tolerated in treatment-resistant chronic migraine; supports generalizability beyond controlled trial populations |
| [38850034](https://pubmed.ncbi.nlm.nih.gov/38850034/) | 2024 | Mechanistic RCT | Cephalalgia | Sildenafil (cGMP pathway) induced migraine attacks independently of CGRP receptor activation; clarifies that erenumab does not block all migraine triggers — relevant to understanding incomplete responders in MBA |
| [33125303](https://pubmed.ncbi.nlm.nih.gov/33125303/) | 2021 | Retrospective Case Series | J Pain Palliat Care Pharmacother | Erenumab + onabotulinumtoxinA combination reduced migraine frequency in intractable chronic migraine; suggests combination approaches may be warranted in refractory MBA |
| [40596876](https://pubmed.ncbi.nlm.nih.gov/40596876/) | 2025 | Single-arm Prospective | J Headache Pain | Switch from erenumab to fremanezumab was tolerable in patients with erenumab adverse events; informs treatment sequencing options when erenumab fails or is not tolerated in MBA |

---

## Canada Market Information

Erenumab is not currently licensed in Canada. No DINs are registered in the Health Canada Drug Product Database.

> **Note:** Erenumab (Aimovig) holds FDA approval (2018) and EMA authorization for migraine prevention in adults. Health Canada authorization status should be verified directly at the [Health Canada Drug Product Database](https://health-canada.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) prior to any regulatory planning.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal warnings, contraindications, and drug interaction data were not available in this evidence pack. Safety review against the Health Canada–approved product monograph (if/when licensed) or the FDA label is required before clinical use planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Erenumab's established CGRP receptor blockade mechanism aligns directly with the known brainstem-trigeminovascular pathophysiology of migraine with brainstem aura, and available evidence from migraine-with-aura subgroup analyses consistently shows no cerebrovascular harm. However, the complete absence of dedicated MBA clinical trials and the drug's unlicensed status in Canada require structured, monitored evaluation before broader application.

**To proceed, the following is needed:**
- Prospective clinical trial or registry study specifically enrolling patients with confirmed migraine with brainstem aura (ICHD-3 criteria) treated with erenumab
- Health Canada regulatory submission and DIN registration (or Named Patient Programme pathway if urgent)
- Formal MOA documentation from DrugBank or product monograph to fill the current data gap
- Safety monitoring protocol specifically addressing posterior circulation hemodynamics and aura duration/frequency in MBA patients
- Complete review of Health Canada or FDA product monograph for boxed warnings, contraindications, and drug interactions before institutional formulary consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

