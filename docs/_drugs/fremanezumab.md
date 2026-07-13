---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Fremanezumab (Ajovy) is a fully humanized anti-CGRP monoclonal antibody internationally approved (FDA/EMA) for preventive treatment of episodic and chronic migraine, though it has not been authorized in Canada.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBA)** — a rare and pharmacologically underserved migraine subtype — with **0 dedicated clinical trials** but **20 publications** providing mechanistic and indirect clinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preventive treatment of episodic and chronic migraine (international approval; not authorized in Canada) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fremanezumab is a fully humanized IgG2Δa monoclonal antibody that selectively targets the CGRP ligand (calcitonin gene-related peptide), blocking its binding to receptors and inhibiting activation of the trigeminovascular system. CGRP is densely distributed in the brainstem trigeminal nucleus caudalis, paratrigeminal nuclei, and dorsal raphe nucleus — precisely the anatomical structures implicated in brainstem aura generation.

Migraine with Brainstem Aura (MBA, formerly "basilar-type migraine") is characterized by aura symptoms originating from the brainstem: dysarthria, vertigo, tinnitus, diplopia, and ataxia. The core pathophysiology involves cortical spreading depression (CSD) propagating posteriorly into the occipital cortex and cerebellum, triggering sensitization of the trigeminal nucleus caudalis through CGRP-mediated neuroinflammation. Two preclinical studies directly testing fremanezumab in CSD models (PMID 31127003; PMID 31895266) demonstrate that fremanezumab slows CSD propagation velocity and shortens cortical recovery period when allowed to cross a compromised blood-brain barrier — providing direct mechanistic plausibility for MBA.

Historically, triptans were contraindicated in MBA due to vasoconstrictive risk in posterior circulation territories. Fremanezumab, as a ligand-targeting antibody that does not directly constrict blood vessels, theoretically removes this pharmacological barrier. However, the pivotal HALO Phase 3 RCTs were not designed with MBA as an independent subgroup, leaving a significant evidence gap between mechanistic rationale and formal clinical validation.

---

## Clinical Trial Evidence

Currently no clinical trials specifically targeting migraine with brainstem aura with fremanezumab are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical Mechanistic | J Neuroscience | Fremanezumab does not affect CSD-induced arterial dilatation or plasma protein extravasation, suggesting CGRP antagonism does not disrupt the CSD vascular response per se — important for understanding MBA safety |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical Mechanistic | Pain | In rats with compromised BBB, fremanezumab slows CSD propagation rate and shortens cortical recovery period — the strongest preclinical mechanistic link to MBA |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical Mechanistic | J Neuroscience | Fremanezumab selectively inhibits trigeminovascular neurons; establishes the neuroanatomical basis relevant to brainstem trigeminal sensitization in MBA |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports + Review | J Clinical Medicine | Anti-CGRP mAbs (including fremanezumab) may reduce migraine aura frequency; limited but relevant case-level evidence for aura subtypes |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Prospective Observational | European J Neurology | Post-hoc FOCUS study analysis: fremanezumab shows efficacy in migraine patients with associated neurological dysfunction, including aura — most clinically proximate published dataset |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Analysis | J Headache and Pain | Anti-CGRP mAbs show effectiveness in hemiplegic migraine (another aura-dominant subtype); individual patient quantitative analysis with fremanezumab included |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report + Review | Frontiers in Neurology | Anti-CGRP mAbs effective in hemiplegic migraine despite RCT exclusion — supports extrapolation to other rare aura subtypes like MBA |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational Case Series | CNS Neuroscience & Therapeutics | Anti-CGRP targeted therapy (including fremanezumab) reduces aura frequency in migraine with aura patients — real-world signal |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handbook of Experimental Pharmacology | Comprehensive review of CGRP's role in migraine pathophysiology including aura and brainstem involvement; foundational mechanistic context |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Real-World Observational | Frontiers in Neurology | 3-month real-world prospective study confirming fremanezumab efficacy and tolerability in chronic migraine; validates post-marketing safety profile |

---

## Canada Market Information

Fremanezumab (Ajovy) has no Drug Identification Numbers (DINs) in Canada and is not currently marketed. No Health Canada licenses on file.

For reference, fremanezumab holds regulatory approval in:
- **United States** (FDA, 2018): Preventive treatment of migraine in adults
- **European Union** (EMA, 2019): Preventive treatment of migraine in adults with ≥4 migraine days/month

---

## Safety Considerations

Safety information (key warnings, contraindications, and drug interactions) was not retrievable from the available data sources for this candidate.

> Please refer to the Ajovy package insert and Health Canada's Drug Product Database for current safety information. Particular attention should be paid to cardiovascular considerations in patients with posterior circulation cerebrovascular risk, given the MBA population profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for fremanezumab in migraine with brainstem aura is scientifically sound — grounded in CGRP neurobiology and two direct preclinical CSD studies — no clinical trials have been conducted in this specific population, and all available clinical data derive from general migraine or aura-in-general cohorts rather than MBA. Evidence level L4 does not meet the threshold for a "Proceed with Guardrails" recommendation without at least prospective observational data in MBA patients.

**To proceed, the following is needed:**

- **Prospective case series or registry study** in MBA patients treated with any anti-CGRP mAb (erenumab, galcanezumab, or fremanezumab), to establish clinical signal before designing a dedicated trial
- **Subgroup analysis** from existing fremanezumab RCTs (HALO CM, HALO EM, FOCUS) specifically identifying patients who meet IHS criteria for MBA — even retrospective reclassification would provide preliminary signal
- **Safety profile clarification** for the MBA population: confirm absence of posterior circulation vasoconstrictive risk distinct from triptans; this should be addressable through review of cardiovascular adverse event data from existing RCTs
- **Formal MOA data** (DrugBank API query): confirm receptor-level pharmacology to strengthen the mechanistic argument for regulatory and clinical audiences
- **Health Canada regulatory pathway scoping**: fremanezumab is not marketed in Canada; any development program for MBA would require either a new drug submission (NDS) or expanded indication filing, which requires the drug to first achieve Canadian market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

