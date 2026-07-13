---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 1
---

# Glucagon
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a pancreatic polypeptide hormone classically used to treat severe hypoglycemia and to temporarily relax gastrointestinal smooth muscle during diagnostic procedures. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)** with a score of **99.24%**; however, the **11 clinical trials** and **20 publications** retrieved pertain almost entirely to GLP-1 receptor agonists—a related but pharmacologically distinct class—rather than glucagon itself, raising significant questions about the validity of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe hypoglycemia; GI diagnostic aid (transient smooth muscle relaxation) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glucagon and GLP-1 (Glucagon-Like Peptide-1) are both encoded by the same proglucagon gene but are produced through differential post-translational processing in different tissues: pancreatic α-cells cleave proglucagon into glucagon (which acts on GCGR), while intestinal L-cells produce GLP-1 (which acts on GLP1R). This shared genetic origin is the most likely explanation for TxGNN's high prediction score—the model's graph-based feature representation may have captured proglucagon-family characteristics and attributed GLP-1-related therapeutic signals to glucagon, producing an overly optimistic prediction.

GLP-1 has well-documented roles in gastrointestinal physiology that are genuinely relevant to IBS. It inhibits intestinal smooth muscle contraction, slows gut motility, reduces visceral hypersensitivity, and modulates the gut-brain axis. GLP-1 receptor agonists such as ROSE-010 and exendin-4 have demonstrated measurable symptom relief in IBS patients and animal models, and IBS-C patients have been found to carry significantly lower circulating GLP-1 levels—suggesting a pathophysiological role for the incretin pathway in this condition.

Crucially, however, glucagon acts on GCGR, not GLP1R—a pharmacologically and functionally distinct receptor. While glucagon does relax gastrointestinal smooth muscle (the basis of its diagnostic use in colonoscopy and barium enema preparation), this is a transient, pharmacological effect and is mechanistically unrelated to the sustained anti-nociceptive, motility-regulating, and neurohormonal actions that GLP-1 RAs exert in IBS. Without dedicated preclinical data showing that GCGR activation replicates GLP1R-mediated IBS benefits, the TxGNN score should be interpreted as a model artefact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (synthetic GLP-1 RA) delayed gastric emptying and enhanced gastric accommodation without retarding colonic transit in female IBS-C patients — the most directly relevant GLP-1-class intervention in IBS within this dataset |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 (not glucagon) inhibited prandial antro-duodeno-jejunal motility in humans, confirmed by in vitro smooth muscle strip experiments; establishes the mechanistic basis for GLP-1-class motility effects |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide vs. placebo in IPAA patients with chronic high bowel frequency; terminated early due to very low enrolment — limited evidence value |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Moderate vs. high-intensity exercise in pre-diabetic obese IBS patients; measured GLP-1 (not glucagon) as a secondary biomarker — indirect evidence only |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Butyrate mode of action in human colon including IBS patients; mechanistically connected to L-cell GLP-1 secretion but no direct glucagon component |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Idiopathic reactive hypoglycemia and fructo-oligosaccharide supplementation; glucagon appears as a counter-regulatory hormone rather than as a therapeutic agent for IBS |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Fibre-rich rye bread, gut microbiota, and gut peptide release in healthy subjects; measures intestinal hormone response including GLP-1, no direct glucagon or IBS connection |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, Not Recruiting | 375 | Small intestinal human organoids to evaluate therapeutic agents; an exploratory in vitro platform with no direct glucagon-IBS evidence reported yet |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-energy diet vs. intragastric balloon for obesity; measures metabolic hormones but has no direct relevance to glucagon as an IBS therapy |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Eating rate of ultra-processed foods on energy intake and metabolic responses over two weeks; no connection to glucagon or IBS treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Frontiers in Endocrinology | Meta-analysis confirms GLP-1 RAs improve IBS symptoms (pain, bloating, motility); ROSE-010 inhibits migrating motor complex and decreases GI motility in IBS — strongest pooled evidence for the GLP-1 pathway |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache and Pain | Systematic review of GLP-1 RAs in headache and pain disorders; documents GLP-1's neuronal pathway activity relevant to IBS visceral hypersensitivity |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Real-world/Observational | Annals of Gastroenterology | Real-world GLP-1 RA prescription and discontinuation patterns in IBS patients; GI adverse effects are prominent, highlighting tolerability challenges in functional GI disorders |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Secondary Clinical Analysis | Scand J Gastroenterology | Cross-analysis of ROSE-010 trials in IBS identifies patient subgroups with greatest pain relief; supports GLP-1R pathway but not GCGR activation |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Proposes intestinal L-cells and GLP-1 secretion as central to IBS pathophysiology, responding to stress, bile acid profiles, microbial shifts, and gut permeability changes |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational | Clin Res Hepatol Gastroenterol | IBS-C patients had significantly lower serum GLP-1 levels inversely correlated with abdominal pain severity; reduced GLP-1R expression found in colonic biopsies — key biomarker evidence |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical | Neurogastroenterol Motility | GLP-1 RA exendin-4 ameliorated GI dysfunction in Wistar Kyoto rat IBS model by modulating myenteric neuronal activity — validated preclinical model for the GLP-1 pathway |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Review | J Clinical Investigation | Positions GLP-1 RAs and enteroendocrine cell-neural circuits as key to understanding gut-brain axis dysfunction in functional GI disorders including IBS |
| [3617051](https://pubmed.ncbi.nlm.nih.gov/3617051/) | 1987 | Observational | Tohoku J Exp Medicine | Psychological stress altered colonic motility, autonomic tone, and gastrointestinal hormone levels in IBS patients — one of the few studies to directly measure glucagon (among other hormones) in an IBS clinical context |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Experimental | Adv Exp Med Biol | Explores aerosolized GLP-1 administration as a dual-indication agent for diabetes and IBS; frames GLP-1 (not glucagon) as the active molecule — indirect framing of the IBS opportunity |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.24% is almost certainly a model artefact: glucagon and GLP-1 share a proglucagon gene origin, and the model has likely misattributed GLP-1 receptor agonist evidence—which is substantial and growing—to glucagon itself. Glucagon acts on GCGR, a pharmacologically distinct receptor from GLP1R, and its documented gastrointestinal effect (transient smooth muscle relaxation for diagnostic use) does not translate into the sustained, receptor-mediated therapeutic mechanism that GLP-1 RAs deploy against IBS symptoms.

**To proceed, the following is needed:**
- Dedicated preclinical studies testing glucagon directly at GCGR in validated IBS models (e.g., Wistar Kyoto rat or intestinal organoid systems)
- Receptor-level comparison of GCGR vs. GLP1R downstream signalling in enteric neurons and intestinal smooth muscle, specifically for motility and visceral pain endpoints
- TxGNN model feature attribution analysis to determine whether the prediction derives from glucagon-specific molecular features or from shared proglucagon-family features (i.e., model interpretability audit)
- Canada regulatory status clarification and full package insert review for up-to-date warnings, contraindications, and approved indications
- If GCGR mechanistic studies show IBS-relevant activity, a Phase 1/2 dose-finding and tolerability study in a defined IBS subtype (preferably IBS-C, given GLP-1 pathway evidence) would be the logical next clinical step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

