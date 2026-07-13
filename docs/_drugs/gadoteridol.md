---
layout: default
title: Gadoteridol
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Gadoteridol
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

# Gadoteridol: From MRI Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Gadoteridol (brand name ProHance) is a macrocyclic, non-ionic gadolinium-based contrast agent (GBCA) used clinically to enhance MRI images of the central nervous system and body structures — it is a diagnostic imaging agent, not a therapeutic drug.
The TxGNN model predicts it may have relevance for **Osteoarthritis Susceptibility**, with **0 clinical trials** and **0 publications** directly supporting this repurposing direction.
This report concludes that all 10 predicted indications in this pack represent model false positives, most likely driven by the systematic co-occurrence of gadoteridol in musculoskeletal and cardiac imaging research literature rather than any therapeutic mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MRI contrast enhancement (CNS, spine, body imaging) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Gadoteridol is a small-molecule gadolinium(III) chelate (Gd-HP-DO3A) belonging to the macrocyclic, non-ionic GBCA class. Its mechanism of action as a contrast agent is purely physical: the paramagnetic gadolinium ion shortens T1 relaxation time of surrounding protons, producing signal enhancement on MRI. It has no receptor binding, no enzymatic activity, and no cellular signaling pathway relevant to any disease treatment. After intravenous injection, it distributes extracellularly and is eliminated unchanged by renal filtration within hours.

Osteoarthritis susceptibility refers to genetic and environmental risk factors predisposing individuals to develop osteoarthritis — a condition requiring disease-modifying agents, analgesics, or biologics for management. Gadoteridol has no cartilage-protective, anti-inflammatory, or disease-modifying mechanism of any kind. There is no pharmacological basis connecting a passive imaging contrast agent to the prevention or treatment of joint degeneration.

The high TxGNN score almost certainly reflects a knowledge graph artefact: gadoteridol appears extensively in musculoskeletal imaging literature (contrast-enhanced CT/MRI of cartilage, synovitis, joint biomechanics), causing the model to create a spurious drug–disease association through co-occurrence rather than mechanistic inference. This is a known limitation of graph-based repurposing models when applied to diagnostic agents — the tool cannot distinguish between "drug used to image disease" and "drug used to treat disease." **This is not a repurposing candidate.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the osteoarthritis susceptibility indication.

> **Analyst Note:** For the closely ranked prediction of osteoarthritis (rank 2, score 98.75%), 12 publications were retrieved — however, all are imaging technology studies where gadoteridol serves as the CT/MRI contrast agent used to *visualize* cartilage composition and biomechanics (e.g., dual-contrast CT, synchrotron microCT, photon-counting CT). None represent therapeutic interventions. Selected examples:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Imaging Technology | J Orthop Res | Dual-contrast CT (CA4+ + gadoteridol) for characterizing articular cartilage degeneration |
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Imaging Technology | J Orthop Res | Triple contrast CT (BiNPs + CA4+ + gadoteridol) for segmenting cadaveric knee cartilage |
| [30816584](https://pubmed.ncbi.nlm.nih.gov/30816584/) | 2019 | CT Imaging | J Orthop Res | Full-body CT dual-contrast imaging of proteoglycan and water content in human articular cartilage |
| [31068614](https://pubmed.ncbi.nlm.nih.gov/31068614/) | 2019 | Synchrotron Imaging | Sci Rep | Simultaneous quantitation of cationic and non-ionic (gadoteridol) contrast agents in cartilage via synchrotron microCT |
| [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/) | 2009 | Safety Study | Metallomics | Gadolinium accumulation in femoral head bone of patients exposed to chelated GBCA — a safety signal |

These publications confirm gadoteridol's role as an **imaging probe**, not a treatment, and some raise additional safety concerns about gadolinium tissue deposition.

---

## Canada Market Information

Gadoteridol is not currently approved or marketed in Canada. No Drug Identification Numbers (DINs) are on record.

> Gadoteridol (ProHance) is approved by the US FDA, EMA, and several other regulators for CNS and body MRI enhancement, but holds no Canadian market authorization at the time of this report (data cutoff: 2026-06-21).

---

## Safety Considerations

The package insert safety data (key warnings, contraindications) was not available at the time of this evidence collection. Please refer to the official product monograph for complete safety information.

Based on drug class knowledge, the following class-level concerns are relevant for completeness:

- **NSF Risk**: Gadolinium-based contrast agents are associated with Nephrogenic Systemic Fibrosis (NSF) in patients with severe renal impairment (eGFR < 30 mL/min/1.73 m²). Macrocyclic agents like gadoteridol carry lower but non-zero risk compared to linear GBCAs.
- **Gadolinium Retention**: Evidence of gadolinium deposition in brain and bone tissue has been documented (PMID [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/)); clinical significance of long-term retention remains under study.
- **Relevant to ranked predictions**: Conditions such as congestive heart failure (rank 8) and hemoglobinopathy (rank 5) commonly present with co-existing renal insufficiency, making GBCA administration in these populations a formal contraindication or high-risk scenario — further undermining repurposing viability.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for gadoteridol are assessed as non-viable repurposing candidates. Gadoteridol is a diagnostic imaging agent with no therapeutic mechanism of action; its presence in musculoskeletal and cardiac disease literature reflects its use as an imaging probe in those disease contexts, not as a treatment. The TxGNN model cannot reliably distinguish diagnostic co-occurrence from therapeutic evidence, generating systematic false positives for contrast agents. This is an important quality signal about the input data pipeline — diagnostic agents should ideally be filtered from therapeutic repurposing models upstream.

**To proceed, the following is needed:**

- **Model pipeline correction**: Flag gadolinium-based contrast agents (and all diagnostic agents) in the DrugBank input to exclude them from therapeutic repurposing scoring, or apply a post-hoc diagnostic-agent filter to TxGNN outputs.
- **Root cause audit**: Investigate how gadoteridol achieved rank scores above 98% across structurally unrelated diseases (bone dysplasias, hemoglobinopathies, heart failure, musculoskeletal conditions) — this pattern suggests a systematic KG node-embedding bias toward diagnostic agents with broad imaging co-occurrence.
- **No clinical follow-up warranted**: Given the complete absence of therapeutic MOA and the zero-evidence profile for all predicted indications, no further evidence collection or clinical evaluation is recommended for gadoteridol as a repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

