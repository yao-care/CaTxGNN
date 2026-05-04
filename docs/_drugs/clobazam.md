---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine antiepileptic drug, FDA-approved as adjunctive therapy for seizures associated with Lennox-Gastaut syndrome (LGS), though it is not currently marketed in Canada.
The TxGNN model predicts it may also be effective for **febrile infection-related epilepsy syndrome (FIRES)** — a catastrophic form of new-onset refractory status epilepticus — with **0 registered clinical trials** and **2 publications** currently available to support this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy — adjunctive treatment of LGS-related seizures (FDA-approved 2011; Canada regulatory data not available) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Although detailed MOA data is not available from the Health Canada regulatory file, clobazam is a well-characterized 1,5-benzodiazepine that functions as a positive allosteric modulator of GABA-A receptors. By facilitating chloride ion influx through GABA-A-gated channels, it enhances inhibitory neurotransmission and raises the seizure threshold across the CNS. Unlike classical 1,4-benzodiazepines (e.g., diazepam, clonazepam), the 1,5-structural variant confers a comparatively lower sedation and muscle-relaxant burden at antiepileptic doses — a clinically meaningful property when considering chronic use in refractory epilepsy syndromes.

FIRES is defined as new-onset refractory status epilepticus (NORSE) preceded by a febrile illness in previously healthy individuals, most often school-aged children. The acute phase requires pharmacological coma with intravenous benzodiazepines (typically midazolam) and barbiturates. The TxGNN prediction is mechanistically plausible through a **benzodiazepine class effect**: oral clobazam targets the same GABA-A receptor system as the IV benzodiazepines used acutely, and could theoretically serve as a chronic maintenance or weaning agent following suppression of status epilepticus — a role analogous to the enteral lorazepam strategy described in the supporting literature.

However, this rationale rests entirely on class-level mechanistic extrapolation. There are no direct clinical trials or observational studies of clobazam specifically in FIRES, and both supporting publications address other agents (lorazepam and perampanel). The prediction therefore remains a mechanistic hypothesis (L4), and clinical validation is required before any development pathway can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | Epileptic Disorders | Enteral lorazepam used as an effective weaning substitute from midazolam in FIRES patients; supports feasibility of oral benzodiazepines for chronic phase management, though clobazam was not specifically evaluated |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | Perampanel reduced barbiturate dependency in a 13-year-old boy with FIRES; highlights the clinical need for oral adjunctive antiepileptics in the chronic FIRES phase, providing indirect context for clobazam's potential role |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The two available publications address related benzodiazepines and adjunctive antiepileptics — not clobazam itself — and no clinical trials exist for this specific indication. Combined with clobazam's non-marketed status in Canada (0 DINs) and the complete absence of direct evidence, the current data is insufficient to support advancing this candidate.

> **Note on a stronger signal in this Evidence Pack:** While FIRES (rank 1) is the top TxGNN-ranked prediction, **childhood onset epileptic encephalopathy** (rank 6, which includes LGS as its representative subtype) carries a far stronger evidence profile — **Evidence Level L1**, supported by multiple systematic reviews, consensus guidelines, and reference to clobazam's existing FDA approval for LGS. Stakeholders may wish to prioritize that indication for a Health Canada regulatory pathway assessment instead.

**To proceed with the FIRES indication, the following is needed:**
- Direct observational data or prospective case series documenting clobazam use in FIRES patients (acute weaning or chronic maintenance phase)
- Detailed MOA and pharmacokinetic data from DrugBank to confirm GABA-A receptor engagement profiles in the FIRES neuroinflammatory context
- Health Canada regulatory pathway assessment, including evaluation of Special Access Programme (SAP) eligibility given the drug's non-marketed status in Canada
- Paediatric safety data specific to clobazam in super-refractory status epilepticus populations, including sedation interaction risks when co-administered with barbiturates or ketamine
- Clarity on TFDA package insert warnings and contraindications (currently a blocking data gap) to enable a complete safety evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

