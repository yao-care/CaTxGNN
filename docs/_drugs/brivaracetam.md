---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: From Epilepsy (Focal Onset Seizures) to Visual Epilepsy

## One-Sentence Summary

Brivaracetam (BRV) is a third-generation antiseizure medication developed for adjunctive and monotherapy treatment of focal onset seizures, with international approvals from the US FDA (2016) and EMA (2016).
The TxGNN model predicts it may be effective for **Visual Epilepsy** (a reflex epilepsy triggered by visual stimuli),
with **0 clinical trials** and **19 publications** currently supporting this direction — anchored in BRV's established SV2A mechanism and validated photosensitivity model data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal onset seizures (epilepsy) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although the DrugBank mechanism of action record was not populated in this dataset, published literature robustly describes BRV's pharmacology: it is a selective, high-affinity ligand for synaptic vesicle glycoprotein 2A (SV2A), binding with 15–30 times greater affinity than its structural predecessor levetiracetam. By modulating SV2A — a presynaptic protein involved in synaptic vesicle cycling and neurotransmitter release — BRV attenuates the excessive neuronal firing underlying seizure activity. Its higher lipophilicity also enables rapid blood-brain barrier penetration compared to levetiracetam, giving it a faster onset of anticonvulsant action.

Visual epilepsy (photosensitive epilepsy) is a reflex epilepsy in which seizures are triggered by flickering lights or specific visual patterns. The cortical hyperexcitability driving these seizures is mechanistically identical to the target pathophysiology BRV was designed to suppress. Crucially, the photoparoxysmal response (PPR) to intermittent photic stimulation (IPS) is a validated human proof-of-concept model for antiseizure efficacy — and BRV has been directly evaluated in this model, demonstrating rapid suppression of PPR with faster onset than levetiracetam (PMID 17785672; PMID 32949370). This photosensitivity model data provides direct mechanistic and clinical evidence directly relevant to visual epilepsy, even though these studies appear in adjacent literature searches.

The prediction is further reinforced by the extensive clinical evidence base for BRV across focal and generalized seizure types, including Phase III RCTs and multiple systematic reviews. Visual epilepsy, as a focal-onset or generalised reflex epilepsy, falls squarely within the seizure spectrum where SV2A modulation is effective. BRV's broad-spectrum antiseizure profile, favorable tolerability relative to levetiracetam, and existing photosensitivity model data collectively make this a scientifically well-grounded prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for brivaracetam in visual epilepsy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Review | J Epilepsy Res | Comprehensive review of BRV pharmacology, clinical efficacy, and safety; confirms broad-spectrum seizure control through selective SV2A binding and rapid CNS penetration |
| [39664134](https://pubmed.ncbi.nlm.nih.gov/39664134/) | 2024 | Systematic Review | Cureus | Systematic review of BRV's current role in adults and children with epilepsy; summarizes efficacy, safety, and clinical rationale for switching from prior ASMs |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Review | Advances in Therapy | Narrative review of BRV preclinical profile and clinical benefits; highlights 15–30× superior SV2A affinity and greater brain permeability versus levetiracetam |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | RCT | Epilepsia Open | Phase III double-blind placebo-controlled RCT of adjunctive BRV in adult Asian patients with uncontrolled focal-onset seizures; demonstrated significant seizure frequency reduction and favorable tolerability |
| [38970892](https://pubmed.ncbi.nlm.nih.gov/38970892/) | 2024 | Pooled Analysis | Epilepsy & Behavior | EXPERIENCE pooled analysis: BRV effectiveness and tolerability in older (≥65 y) and younger adults with epilepsy across real-world international datasets |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Meta-Analysis | Front Neurol | Systematic review and meta-analysis of BRV safety and efficacy in childhood epilepsy; supports broad applicability across age groups |
| [38205459](https://pubmed.ncbi.nlm.nih.gov/38205459/) | 2023 | Observational | Cureus | Prospective non-interventional real-world study confirming BRV's strong SV2A selectivity, equivalent efficacy to other ASMs, and superior tolerability |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Analysis | Epilepsy & Behavior | In-depth pooled safety analysis of adjunctive BRV across all Phase II/III trials; characterizes adverse event profile including psychiatric and CNS events |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Comprehensive review of ASM mechanisms of action, including SV2A modulation; provides mechanistic context for BRV's applicability in reflex epilepsies |
| [26165169](https://pubmed.ncbi.nlm.nih.gov/26165169/) | 2015 | Meta-Analysis | Expert Opin Pharmacother | Meta-analysis of BRV at different doses for partial-onset epilepsy; established dose-response relationship and supported 50–200 mg/day dosing range |

---

## Canada Market Information

Brivaracetam is not currently approved in Canada. No Drug Identification Numbers (DINs) are on file for this compound in the Health Canada database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Brivaracetam has a mechanistically validated basis for efficacy in visual epilepsy, supported by direct photosensitivity model clinical data and an extensive evidence base across focal seizure types. However, BRV is not currently registered in Canada, and prospective evidence in confirmed visual epilepsy populations remains limited to early-phase and indirect studies.

**To proceed, the following is needed:**
- **Health Canada regulatory submission and DIN registration** — a prerequisite for any Canadian clinical or commercial use
- **Package insert / product monograph review** — to document key warnings, contraindications, and drug interaction profile (currently unavailable in this dataset)
- **Prospective clinical study or registry** specifically enrolling patients with confirmed visual or photosensitive epilepsy treated with brivaracetam
- **DrugBank MOA data retrieval** — to complete the pharmacological dossier and support regulatory submissions
- **Pediatric dosing assessment** — visual/photosensitive epilepsy frequently manifests in adolescents; specific PK/PD data in this subgroup should be confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

