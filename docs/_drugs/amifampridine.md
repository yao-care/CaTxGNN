---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine (3,4-diaminopyridine) is a voltage-gated potassium channel blocker with established efficacy in Lambert-Eaton Myasthenic Syndrome (LEMS), a rare autoimmune neuromuscular junction disorder.
The TxGNN model ranks **Glaucoma** as the top predicted new indication (score 99.71%), with 9 additional candidate indications identified in this multi-indication evaluation—none of which are currently supported by direct clinical trials or literature for amifampridine.
The only literature evidence in this pack (**2 publications**) relates to the rank-10 prediction, paraneoplastic cerebellar degeneration, providing indirect mechanistic support through amifampridine's validated role in LEMS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lambert-Eaton Myasthenic Syndrome (LEMS) |
| Top Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (glaucoma); L4 (paraneoplastic cerebellar degeneration) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacology, amifampridine works by **blocking presynaptic voltage-gated potassium (Kv) channels**, thereby prolonging the action potential duration. This extends the window for calcium influx through voltage-gated calcium channels (VGCC) and enhances acetylcholine release at the neuromuscular junction. In LEMS—where P/Q-type VGCC are targeted and inactivated by autoantibodies—amifampridine effectively compensates by amplifying the depolarization signal that drives calcium entry. This mechanism is well-validated by multiple RCTs in LEMS.

For **glaucoma** (the top-ranked prediction), the proposed rationale rests on the presence of Kv channels in the ciliary body epithelium and trabecular meshwork, where they may theoretically modulate aqueous humor secretion and intraocular pressure. However, this is an **extremely indirect and unverified mechanistic link**, driven primarily by topological proximity within the TxGNN knowledge graph rather than any direct pharmacological evidence. No preclinical or clinical studies have ever investigated amifampridine in glaucoma.

In contrast, the **paraneoplastic indications** ranked 7, 8, and 10 (limbic encephalitis, polyneuropathy, and cerebellar degeneration) carry meaningfully stronger biological plausibility. These syndromes frequently co-occur with LEMS in the context of small cell lung cancer, share the same autoimmune target (anti-P/Q-type VGCC antibodies), and are pathophysiologically adjacent to the disease where amifampridine's mechanism has already been proven. Among all 10 predictions, these three constitute the most scientifically defensible targets for future research investment.

---

## All Predicted Indications — Summary (Top 10)

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Glaucoma | 99.71% | L5 | Hold |
| 2 | Acute Intermittent Porphyria | 99.32% | L5 | Hold |
| 3 | Esophageal Varices with Bleeding | 98.77% | L5 | Hold |
| 4 | Esophageal Varices without Bleeding | 98.77% | L5 | Hold |
| 5 | Porphyria | 98.51% | L5 | Hold |
| 6 | Primary Immunodeficiency (p14 Deficiency) | 98.39% | L5 | Hold |
| 7 | Paraneoplastic Limbic Encephalitis | 98.31% | L5 | Research Question |
| 8 | Paraneoplastic Polyneuropathy | 98.26% | L5 | Research Question |
| 9 | Varicose Disease | 98.08% | L5 | Hold |
| 10 | Paraneoplastic Cerebellar Degeneration | 97.99% | L4 | Research Question |

**Interpretation note:** Ranks 3 and 4 share an identical score (0.9877), indicating TxGNN treats the bleeding and non-bleeding variants of esophageal varices as the same disease node — which reduces the specificity of both predictions. Similarly, ranks 2 and 5 (acute intermittent porphyria and porphyria) represent a parent–child node overlap, not independent evidence.

---

## Clinical Trial Evidence

No clinical trials were identified for amifampridine across any of the 10 predicted indications in this evidence pack. All 30 ClinicalTrials.gov and ICTRP queries returned zero results.

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for the rank-1 prediction (glaucoma). The only publications retrieved in this evidence pack are for **paraneoplastic cerebellar degeneration** (rank 10), and both report amifampridine efficacy in LEMS — providing indirect but mechanistically relevant evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15034474](https://pubmed.ncbi.nlm.nih.gov/15034474/) | 2004 | Review | Revue neurologique | Comprehensive review of LEMS: proximal muscle weakness, autonomic features, ~60% paraneoplastic (small cell lung cancer); confirms role of anti-VGCC antibodies and the rationale for Kv-channel blockade |
| [29386498](https://pubmed.ncbi.nlm.nih.gov/29386498/) | 2018 | Retrospective Cohort | Rinsho shinkeigaku (Clinical Neurology) | 9 LEMS patients treated with 3,4-DAP; 8/9 showed improved ADL (primarily limb weakness); 7/9 anti-VGCC antibody positive; 5/9 had small cell lung carcinoma — directly overlapping the paraneoplastic disease context |

*Both publications address LEMS rather than paraneoplastic cerebellar degeneration directly. Their relevance derives from the well-established clinical and mechanistic overlap between LEMS and paraneoplastic cerebellar degeneration in the small cell lung cancer setting.*

---

## Canada Market Information

Amifampridine has **no approved products in Canada** and is not currently marketed. There are zero Drug Identification Numbers (DINs) on file.

> **For reference:** Amifampridine phosphate (Firdapse®) is FDA-approved in the United States for LEMS in adults (2018), and amifampridine base (Ruzurgi®) for patients aged 6 and older (2019). A Health Canada submission has not been reported as of the data cutoff.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack. The FDA-approved product labels (Firdapse® and Ruzurgi®) are the most accessible reference sources for safety assessment pending a formal Health Canada review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (glaucoma) lacks any direct mechanistic, preclinical, or clinical evidence for amifampridine, and the biological plausibility of the Kv-channel–aqueous humor link is highly speculative. Across all 10 predicted indications, no clinical trials were found, and no literature directly supports any of the novel proposed uses. The evidence base is insufficient to justify clinical development at this stage.

**The paraneoplastic conditions (ranks 7, 8, 10) are the only predictions meriting continued scientific attention**, classified as "Research Question" due to mechanistic overlap with the validated LEMS indication.

**To proceed, the following is needed:**

- Retrieve full safety data (warnings, contraindications, drug interactions) from the FDA product monograph (Firdapse®/Ruzurgi®) or Health Canada drug database
- Confirm complete mechanism of action details via DrugBank API query (DG002 remediation)
- Conduct a systematic PubMed review specifically targeting amifampridine or 3,4-DAP in paraneoplastic limbic encephalitis, paraneoplastic polyneuropathy, and paraneoplastic cerebellar degeneration
- For the glaucoma prediction: require at least one published in vitro or animal model study demonstrating Kv-channel modulation of intraocular pressure before this indication can advance beyond L5
- Explore orphan drug designation pathways (FDA/EMA/Health Canada) for any paraneoplastic indication pursued, given the ultra-rare disease population
- Assess blood-brain barrier penetration data for amifampridine if central nervous system paraneoplastic indications are to be pursued clinically

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

