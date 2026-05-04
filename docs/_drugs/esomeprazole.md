---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Esomeprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole (Nexium) is a proton pump inhibitor (PPI) — the S-isomer of omeprazole — widely used for acid-related diseases including gastro-oesophageal reflux disease (GERD), peptic ulcer, and *Helicobacter pylori* eradication therapy.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux** (rank 1, score 99.53%), supported by **no clinical trials** and **1 narrative review** for this specific indication.
Notably, the model also predicts strong activity for **Duodenal Ulcer** (rank 3, score 99.40%), which carries substantially richer evidence — **50+ clinical trials** and **20 publications** at Evidence Level L1 — and may represent the more actionable repurposing signal from this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease, GERD, *H. pylori* eradication (from published literature; no Canadian DINs on record in current dataset) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs — likely a data gap; independent Health Canada verification recommended) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on published literature included in this pack, esomeprazole irreversibly inhibits the H⁺/K⁺-ATPase (proton pump) in gastric parietal cells — the final common pathway of gastric acid secretion. As the S-isomer of omeprazole, it achieves superior and more consistent intragastric pH control compared to its racemate, making it the backbone of triple and quadruple eradication regimens and a first-line agent for all acid-related mucosal disorders.

Duodenogastric reflux (DGR) is defined by the retrograde flow of bile salts and alkaline duodenal contents into the stomach. The pathological injury arises from a combination of bile-acid toxicity and concurrent acid exposure — the so-called "acid-bile synergism." Acid suppression with a PPI does not correct the mechanical reflux itself, but by raising intragastric pH it disrupts this synergism and reduces bile-related mucosal damage. The mechanistic link is therefore **indirect and gastroprotective**, not causal treatment of DGR.

The TxGNN score of 0.9953 most likely reflects the structural proximity of the PPI drug class to the gastroduodenal disease cluster within the knowledge graph, rather than a prediction derived from DGR-specific pharmacology. The prediction is biologically plausible, but should be interpreted cautiously given the absence of dedicated clinical evidence. A more targeted literature search and mechanistic review would be needed before advancing this hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for esomeprazole in duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Narrative Review | *European Journal of Clinical Pharmacology* | Comprehensive update on PPI clinical use and pharmacokinetics; confirms esomeprazole's first-line role in peptic ulcer, *H. pylori*, NSAID-related GI lesions, GERD, and Zollinger-Ellison syndrome. Duodenogastric reflux is not specifically addressed, but the broader acid suppression framework provides indirect mechanistic context. |

---

## Canada Market Information

No Canadian DINs are currently registered for esomeprazole in this dataset (market status recorded as "Not marketed," 0 licences). This is inconsistent with esomeprazole's known international availability as a widely approved PPI. This likely reflects a **data pipeline gap** rather than actual market absence. Independent verification via the Health Canada Drug Product Database is strongly recommended before using this field for regulatory decision-making.

---

## Safety Considerations

Please refer to the product monograph (package insert) for safety information. Formal safety data — including Health Canada-approved warnings, contraindications, and drug interaction profile — were not available in the current evidence pack and represent a blocking data gap for a full S1 safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high score for duodenogastric reflux most likely reflects knowledge-graph structural clustering rather than a specific mechanistic prediction; the evidence base is limited to a single 2008 narrative review (Evidence Level L4), and the mechanistic connection — indirect acid-bile synergism disruption — does not constitute a primary indication for esomeprazole in DGR. Proceeding to clinical translation is premature without stronger dedicated evidence.

**To proceed, the following is needed:**

- **Regulatory data verification**: Confirm Canada market status and retrieve approved product monograph via Health Canada Drug Product Database — required to resolve the blocking DG001 data gap (safety warnings/contraindications)
- **MOA data retrieval**: Query DrugBank API for DB00736 to populate the formal mechanism of action — required for DG002 and mechanistic link analysis
- **Targeted literature search**: Search "esomeprazole AND duodenogastric reflux" and "proton pump inhibitor AND bile reflux" to identify any PPI studies where DGR was a primary or secondary endpoint
- **Parallel evaluation of Duodenal Ulcer prediction**: Rank 3 (Duodenal Ulcer, L1 evidence, 50+ trials, recommendation: *Proceed with Guardrails*) presents a far more actionable repurposing candidate and should be prioritized for a full evaluation report
- **If exploratory study is considered**: A retrospective review of existing PPI cohort data for DGR-related outcomes, or a pilot pH/impedance monitoring study, would be the lowest-cost path to generating direct evidence

---

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application to patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

