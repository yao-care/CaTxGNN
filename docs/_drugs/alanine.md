---
layout: default
title: Alanine
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 1
---

# Alanine
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

# ALANINE: From Amino Acid Supplementation to Gastroparesis

## One-Sentence Summary

ALANINE (L-Alanine) is a non-essential glucogenic amino acid with no currently registered drug indication in Canada; it is used primarily as a nutritional and metabolic substrate.
The TxGNN model predicts it may be effective for **Gastroparesis**, with **9 clinical trials** and **3 publications** identified in the current evidence search — though none directly investigate Alanine as the active intervention for this condition.
Given the absence of direct pharmacological evidence, this candidate remains at a very early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established drug indication on record |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known biochemistry, Alanine is a glucogenic amino acid that participates in the **glucose-alanine cycle** — a shuttle between muscle and liver that regulates blood glucose homeostasis. In theory, amino acids including Alanine can stimulate the release of gut hormones such as cholecystokinin (CCK) and GLP-1, both of which influence gastric motility and emptying rate. This provides a plausible, if indirect, biological rationale for the TxGNN model's prediction.

Gastroparesis is a disorder of delayed gastric emptying, often secondary to diabetes mellitus. The connection to Alanine may be partly explained through its role in glucose regulation: because diabetic gastroparesis is closely tied to glycaemic dysregulation, agents that modulate glucose metabolism or gut hormone signalling are theoretically relevant. Alanine's gluconeogenic properties and its potential to modulate GLP-1 secretion place it mechanistically adjacent — though not directly central — to this disease pathway.

However, it is critical to note that this mechanistic link is entirely inferential. There is no direct pharmacological experiment, preclinical animal model, or clinical study demonstrating that Alanine, as a standalone intervention, accelerates gastric emptying or reduces gastroparesis symptoms. The TxGNN prediction appears driven by network topology in the knowledge graph rather than established pharmacology.

---

## Clinical Trial Evidence

The trials retrieved in this search predominantly investigate **other drugs** (GSK962040, Aprepitant, Buspirone, Cannabidiol) in the gastroparesis disease space. None directly evaluate Alanine as the therapeutic agent. They are listed as contextual background evidence only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | Completed | 79 | GSK962040 (motilin receptor agonist) evaluated over 28 days in diabetic gastroparesis; no Alanine involvement |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | Terminated | 91 | GSK962040 + enteral nutrition in critically ill ICU patients; Alanine may have been a nutrition component but was not the primary intervention; study terminated early |
| [NCT07270939](https://clinicaltrials.gov/study/NCT07270939) | N/A | Not Yet Recruiting | 150 | Comparing 18-hour, 20-hour, and 24-hour enteral feeding cycles in ICU patients; Alanine may be present in feed formulations but is not the study intervention |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | Completed | 126 | Aprepitant (NK1 receptor antagonist) for chronic nausea/vomiting of gastric origin; no Alanine involvement |
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | Completed | 96 | Buspirone (5-HT1A agonist) for gastroparesis symptoms including early satiety; no Alanine involvement |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | Completed | 92 | Cannabidiol (CBD) for gastroparesis and functional dyspepsia; no Alanine involvement |
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | Completed | 58 | GSK962040 dose-ranging study in Parkinson's disease patients with delayed gastric emptying; no Alanine involvement |
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | Recruiting | 350 | Traditional Chinese medicine interventions for organ failure in critically ill ICU patients; no direct Alanine connection |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | Terminated | 4 | Albiglutide vs exenatide on gastric myoelectrical activity in T2DM; terminated due to poor enrolment (n=4); no Alanine involvement |

> ⚠️ **Important caveat**: None of these trials test Alanine as the active treatment for gastroparesis. They represent the broader gastroparesis clinical trial landscape retrieved by the evidence engine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | Reviews GI and hepatic complications in end-stage renal disease; notes increased prevalence of gastroparesis in chronic renal failure; no direct Alanine data |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Case Series / Review | Diabetic Medicine | Describes diabetic hepatosclerosis as a microvascular complication of diabetes; contextually links diabetes to GI/hepatic pathology including gastroparesis; no Alanine data |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Case Report | Cureus | Case of glycogen hepatopathy in a Type 1 diabetic patient with co-existing gastroparesis; highlights metabolic complications of poorly controlled T1DM; no Alanine intervention data |

> ⚠️ All three publications are observational or descriptive in nature (Tier 3) and none directly investigate Alanine as a therapeutic agent for gastroparesis.

---

## Canada Market Information

ALANINE (DB00160) currently has **no registered drug products** in Canada and is not marketed as a licensed pharmaceutical.

No DIN records are available for this substance.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data, contraindications, or specific warnings were identified in the current evidence search for Alanine in the context of gastroparesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns Alanine a high prediction score for gastroparesis (99.37%), but all retrieved clinical and literature evidence relates to other drugs operating in the same disease space — not to Alanine itself. The mechanistic link is inferential (via glucose-alanine cycle and indirect gut hormone signalling) and has not been validated in any preclinical or clinical experiment. With zero Canadian approvals, no direct supporting trials, and no mechanistic data on file, this candidate does not yet meet the minimum threshold to advance.

**To proceed, the following is needed:**

- **Mechanism of action validation**: Preclinical studies demonstrating that Alanine directly or indirectly influences gastric motility, CCK/GLP-1 secretion, or gastric emptying rate in relevant animal or in vitro models
- **Direct clinical evidence**: Identification of any human studies (even small pilot studies or case series) in which Alanine was administered as an isolated agent and gastric emptying outcomes were measured
- **Safety profile**: Full safety assessment including contraindications, drug-drug interactions, and warnings, particularly for diabetic and renally impaired populations where gastroparesis is prevalent
- **Dose-route feasibility**: Determination of what route of administration and dosing regimen would be clinically relevant (oral, IV in parenteral nutrition, etc.)
- **Regulatory pathway assessment**: If evidence strengthens, a regulatory feasibility review for a new therapeutic indication in Canada would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

