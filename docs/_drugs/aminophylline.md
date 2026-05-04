---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: From Bronchospasm to Migraine Disorder

## One-Sentence Summary

Aminophylline is a methylxanthine compound with established clinical use as a bronchodilator for asthma and obstructive airway disease, and for apnea of prematurity.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **0 clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm / asthma, apnea of prematurity (standard clinical use; no Canadian DIN on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Aminophylline is the ethylenediamine salt of theophylline, a methylxanthine compound long used as a bronchodilator in asthma and COPD, and as first-line therapy for apnea of prematurity. Detailed mechanism-of-action data is not available in the current Evidence Pack. Based on published literature, Aminophylline is understood to act primarily as an **adenosine receptor antagonist** (blocking A1, A2A, and A2B receptors), with secondary activity as a **phosphodiesterase (PDE) inhibitor** that raises intracellular cAMP. This dual mechanism is pharmacologically analogous to caffeine, which has a well-established association with migraine relief.

The connection to migraine is mechanistically coherent. Accumulating evidence (PMID 38059379) suggests that migraine may be driven, at least in part, by elevated adenosine levels and impaired brain energy metabolism. Activation of adenosine A2A receptors causes vasodilation of intracranial arteries, which can trigger migraine attacks. By blocking these receptors, Aminophylline could theoretically counteract this vasodilatory cascade. Critically, PMID 34308528 provides direct clinical corroboration: regadenoson, a selective A2A agonist used in cardiac stress testing, triggered a hemiplegic migraine episode that was subsequently reversed by aminophylline administration — precisely the expected pharmacodynamic outcome if adenosine receptor antagonism underlies migraine relief. PMID 7728647 further supports the adenosine hypothesis by describing adenosine-excess-driven "myocardial migraine," and in vitro data (PMID 219563) confirm that adenosine potently dilates human intracranial arteries.

Despite this biologically plausible framework, no prospective clinical trials have been conducted. The current evidence base is limited to a narrative review, one case report with direct mechanistic relevance, and supporting mechanistic/observational data. Aminophylline's narrow therapeutic index and known adverse effect profile (arrhythmia, seizure at toxic levels) also demand careful evaluation before clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Aminophylline in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | *Pain Management* | Narrative review proposing aminophylline (adenosine receptor antagonist) as a treatment for migraine driven by high adenosine and impaired brain energy metabolism; cites observational case series showing strong therapeutic response in migraine and post-dural puncture headache |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | *Journal of Nuclear Cardiology* | Regadenoson (A2A agonist) triggered a hemiplegic migraine episode during cardiac stress imaging; aminophylline reversed the episode, directly demonstrating adenosine antagonism as a mechanism for migraine reversal |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | *Canadian Journal of Cardiology* | 53-year-old female with syndrome X: dipyridamole-induced adenosine excess provoked disabling pain consistent with "myocardial migraine," supporting the role of pathological adenosine signalling in migraine-like episodes |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro Study | *Stroke* | Adenosine and adenine compounds markedly dilated feline and human pial (intracranial) arteries in vitro; dilation increased with vessel tone, while extracranial arteries were unaffected — consistent with adenosine's selective role in intracranial vascular dysregulation |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Historical Reference | *The Practitioner* | Historical clinical reference on suppository formulations; limited direct relevance to migraine mechanism |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Historical Reference | *Aggiornamenti Clinicoterapeutici* | Historical Italian-language report on medication-treated headaches; no extractable data available |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No Canadian product monograph (DIN) is on file for Aminophylline, and TFDA package insert warnings and contraindications were not available at the time of this report. This is classified as a **Blocking** data gap that must be resolved before any safety evaluation can proceed. Aminophylline is a narrow-therapeutic-index drug; theophylline toxicity (arrhythmia, seizure) is a known clinical risk that warrants careful dose management in any new indication study.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The adenosine receptor antagonism mechanism provides a biologically coherent rationale for Aminophylline in migraine, and the clinical reversal of an A2A-agonist-triggered migraine episode (PMID 34308528) offers compelling proof-of-concept evidence. However, the evidence base remains limited to a narrative review and case-level observations — no prospective clinical trials exist for this indication. Combined with the drug's absence from the Canadian market and a blocking safety data gap, this candidate is not yet ready for formal development but merits structured investigation.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain and review the full product monograph / package insert warnings and contraindications before advancing to any safety stage gate
- **Mechanistic data:** Retrieve complete MOA profile from DrugBank (DB01223), including receptor binding affinities, PDE isoform selectivity, and known CNS effects
- **Full-text review:** Access full text of PMID 38059379 to evaluate the quality and size of the referenced observational case series in migraine/post-dural headache
- **Dose selection rationale:** Identify the dose range used in migraine-relevant case observations vs. established therapeutic ranges for asthma/apnea (to assess safety margin)
- **Prospective pilot study:** Design a small proof-of-concept study (e.g., single-arm open-label, acute migraine treatment) before committing to a full RCT
- **Regulatory pathway:** Assess Health Canada requirements for clinical investigation of a non-marketed drug in a new neurological indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

