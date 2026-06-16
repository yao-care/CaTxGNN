---
layout: default
title: Eptinezumab
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 1
---

# Eptinezumab
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

# Eptinezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Eptinezumab (Vyepti®) is an intravenous anti-CGRP monoclonal antibody approved by the FDA for preventive treatment of episodic and chronic migraine in adults, though it has not yet received Health Canada approval.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBA)**, a distinct migraine subtype characterized by brainstem-originating neurological symptoms preceding headache,
with **no registered clinical trials** specifically targeting this subtype but **8 publications** — including 1 post-hoc RCT analysis directly evaluating eptinezumab in aura patients — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Canada; FDA-approved for episodic and chronic migraine prevention |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query in this Evidence Pack. Based on known information from the retrieved literature, eptinezumab is a humanized IgG1 monoclonal antibody that targets calcitonin gene-related peptide (CGRP) — a potent neuropeptide vasodilator released from trigeminal nerve terminals during migraine attacks. By binding free circulating CGRP with high affinity before it can engage its receptor, eptinezumab interrupts the trigeminal neurovascular cascade that drives migraine pain. Its intravenous route achieves immediate therapeutic plasma concentrations, distinguishing it pharmacokinetically from subcutaneous CGRP antibodies and potentially providing more complete CGRP blockade in the early post-infusion window.

Migraine with Brainstem Aura (formerly termed basilar-type migraine) is characterized by aura symptoms originating from the brainstem — including dysarthria, diplopia, tinnitus, vertigo, ataxia, and decreased consciousness — preceding headache. CGRP is well-established as a key mediator in brainstem trigeminal pathways, and cortical spreading depression-like activity in this region triggers CGRP release from trigeminal afferents. Because eptinezumab acts systemically by neutralizing circulating CGRP before it binds receptors, its mechanism is directly applicable to aura subtypes involving trigeminal CGRP release. A post-hoc analysis of the PROMISE-1 and PROMISE-2 phase 3 RCTs (PMID 35302389) showed eptinezumab was efficacious and safe in migraine patients with self-reported aura, providing the most direct human evidence for this prediction.

An important mechanistic caveat, however, is raised by a 2025 RCT (PMID 40229719): PACAP38-induced migraine attacks appear to occur via CGRP-independent pathways. This suggests a subset of MBA attacks — possibly those driven by PACAP38 — may not respond to anti-CGRP therapy. Additionally, the brainstem aura subtype was historically considered a relative contraindication to triptans (due to vasoconstrictive concerns in the basilar territory), a safety context that may warrant careful evaluation before extending eptinezumab use to this population. Overall, the mechanistic rationale is strong but carries unresolved subtype-specific uncertainty that prospective evidence would need to address.

---

## Clinical Trial Evidence

Currently no clinical trials specifically for eptinezumab in migraine with brainstem aura are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | RCT | J Headache Pain | PACAP38-induced migraine attacks occur via CGRP-independent mechanisms; signals that some MBA attacks may fall outside the scope of anti-CGRP therapy |
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Post-hoc RCT Analysis | Cephalalgia | Eptinezumab demonstrated efficacy and safety for migraine prevention in patients with self-reported aura in PROMISE-1 and PROMISE-2; most direct evidence for aura subtype applicability |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Clinical/Genetic Study | Headache | Two cases of genetic migraine disorders with chronic migraine and visual aura responded to CGRP antagonist therapy, supporting broader aura population applicability |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports + Literature Review | J Clin Medicine | Anti-CGRP mAbs including eptinezumab may reduce aura frequency alongside headache; cortical spreading depression inhibition proposed as secondary mechanism |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Case Report | Rev Neurol | Eptinezumab successfully managed wearing-off effect in chronic migraine with aura refractory to two subcutaneous CGRP antibodies, demonstrating utility in aura patients who fail other CGRP agents |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Comprehensive review of CGRP's mechanistic role in migraine including aura subtypes and trigeminal neurovascular activation; foundational rationale for CGRP-targeted therapies |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Positions eptinezumab within the landscape of new migraine preventive therapies, detailing CGRP neurovascular hypothesis and clinical trial data from PROMISE program |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Review | Cureus | CGRP antagonists reviewed for episodic and chronic migraine with aura; eptinezumab highlighted among approved preventive options with favourable rapid-onset profile |

---

## Canada Market Information

Eptinezumab has not received Health Canada approval and currently has no Drug Identification Numbers (DINs) in Canada. There are no licensed products to list. Clinicians seeking prescribing information should refer to the FDA-approved Vyepti® US prescribing information or Health Canada's Special Access Programme for compassionate use.

---

## Safety Considerations

Safety labelling data specific to a Health Canada submission is not available, as the drug is not approved in Canada. No drug-drug interactions were identified in the evidence pack query.

Please refer to the FDA Vyepti® (eptinezumab-jjmr) package insert for current warnings, contraindications, and interaction data. Key areas to review include hypersensitivity reactions (anaphylaxis and angioedema have been reported post-infusion) and the historical caution around brainstem aura subtypes given older vasoconstrictive migraine therapies.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Post-hoc analyses of two Phase 3 RCTs confirm eptinezumab's efficacy and safety in aura-positive migraine patients, and the CGRP mechanistic rationale extends logically to the brainstem aura subtype — however, no prospective trial has specifically enrolled MBA patients, a 2025 RCT reveals CGRP-independent attack pathways that could limit response in a subset of MBA cases, and the drug is not yet approved in Canada, creating regulatory and safety documentation gaps.

**To proceed, the following is needed:**

- **Prospective trial evidence**: Design or identify a registry or clinical trial specifically enrolling migraine with brainstem aura patients receiving eptinezumab, with brainstem aura frequency as a primary endpoint
- **Health Canada regulatory pathway**: Initiate or track the New Drug Submission (NDS) process for eptinezumab in Canada; coordinate with Health Canada for labelling review
- **Complete MOA documentation**: Retrieve full mechanism of action data from DrugBank API to support the mechanistic dossier
- **CGRP vs. PACAP38 subtyping**: Identify biomarkers or clinical features that distinguish CGRP-driven MBA from PACAP38-driven MBA to define the optimal responding patient population
- **Safety dossier for MBA subtype**: Review historical triptan contraindication rationale in brainstem aura to assess whether any analogous caution applies to CGRP pathway inhibition, and document Canadian-specific labelling requirements upon regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

