---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Asfotase alfa (Strensiq) is a recombinant human tissue-nonspecific alkaline phosphatase (TNSALP) enzyme replacement therapy approved for the treatment of Hypophosphatasia (HPP), a rare inherited disorder of defective bone and tooth mineralization caused by loss-of-function mutations in the *ALPL* gene.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies** (score: 99.95%), placing it as the top-ranked repurposing candidate.
However, **0 clinical trials** and **0 publications** currently support this direction, and the mechanistic rationale is indirect at best.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypophosphatasia (HPP) — defective bone and tooth mineralization due to TNSALP deficiency |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Asfotase alfa is a bone-targeted, recombinant form of human TNSALP fused to a deca-aspartate (D10) hydroxyapatite-binding domain and the Fc region of human IgG1. Its mechanism of action is to enzymatically cleave inorganic pyrophosphate (PPi) — a potent inhibitor of hydroxyapatite crystal deposition — thereby allowing normal bone mineralization to proceed. In HPP patients, loss-of-function mutations in *ALPL* cause PPi to accumulate, resulting in rickets, fractures, muscle weakness, and in severe perinatal forms, respiratory failure and death.

The biological rationale linking Asfotase alfa to mitochondrial oxidative phosphorylation disorder is tenuous. TNSALP is known to be expressed on the plasma membrane of diverse cell types including hepatocytes, osteoblasts, and kidney proximal tubule cells, and some studies have noted alkaline phosphatase activity in the vicinity of mitochondrial membranes. Furthermore, phosphate and ATP metabolism are intertwined: PPi is a byproduct of many ATP-consuming biosynthetic reactions, and TNSALP activity influences cellular phosphate availability. These shared metabolic nodes — ATP metabolism, inorganic phosphate homeostasis — are likely the topological features in the TxGNN knowledge graph that drive the high prediction score.

However, the primary pathology in nuclear-encoded mitochondrial oxidative phosphorylation disorders is dysfunction of electron transport chain complexes (I–V) or associated assembly factors due to mutations in nuclear DNA. This is mechanistically entirely distinct from PPi-mediated inhibition of bone mineralization. There is no published preclinical study, animal model, or patient case suggesting that TNSALP enzyme replacement modifies mitochondrial respiratory chain function or disease progression in this condition. The TxGNN score almost certainly reflects a false-positive arising from shared metabolic pathway nodes in the knowledge graph rather than a true biological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Asfotase alfa is not currently approved or marketed in Canada. No Drug Identification Numbers (DINs) have been issued.

> **Note:** Strensiq (asfotase alfa) holds FDA approval (USA, 2015) and EMA approval (Europe, 2015) for the treatment of perinatal/infantile/juvenile-onset HPP. Health Canada approval has not been granted as of the data cutoff date (2026-04-05).

---

## Safety Considerations

Please refer to the package insert for safety information. No Canadian-specific warning, contraindication, or drug interaction data was available in this Evidence Pack.

> Based on the known pharmacological profile of Asfotase alfa, clinicians should be aware of injection-site reactions (lipodystrophy, erythema, bruising), ectopic calcification (particularly optic nerve and renal), and the need for ophthalmological and renal monitoring during therapy. These are drawn from published product monographs and are not confirmed from a Health Canada-approved label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.95% is driven by shared metabolic graph topology (ATP/phosphate metabolism nodes) rather than a mechanistically coherent biological hypothesis. No clinical trials, observational studies, preclinical publications, or case reports support the use of Asfotase alfa in mitochondrial oxidative phosphorylation disorders, and the underlying disease mechanism (nuclear-encoded electron transport chain defects) is fundamentally orthogonal to TNSALP's substrate (PPi) and tissue target (bone/skeleton). This is a classic L5 model artefact: high score, no real-world evidence, low biological plausibility for direct application.

**To proceed, the following would be needed:**

- **Preclinical feasibility study**: Demonstrate that TNSALP enzyme replacement, or PPi reduction, alters mitochondrial respiratory chain activity or ATP production in a relevant cell model (e.g., patient-derived fibroblasts, cybrid cells) — this is the minimum gate to justify further investment.
- **Mechanistic clarification**: Establish whether secondary PPi accumulation occurs in nuclear mitochondrial disease models and whether it impairs any downstream process addressable by Asfotase alfa.
- **Biomarker identification**: Identify a measurable surrogate endpoint (e.g., PPi plasma levels, phosphoethanolamine) in patients with mitochondrial disease to assess whether TNSALP substrate accumulation is present.
- **MOA data gap resolution**: Obtain full DrugBank MOA profile for Asfotase alfa to confirm or refute any mitochondria-adjacent mechanism.
- **Regulatory data**: Obtain Health Canada product monograph or FDA label (Strensiq) to complete the safety profile before any human hypothesis-testing study.

> **YMYL Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates identified by computational models require rigorous clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

