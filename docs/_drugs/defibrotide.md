---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-Von Willebrand Disease

## One-Sentence Summary

Defibrotide is a polydeoxyribonucleotide antithrombotic agent internationally approved for hepatic veno-occlusive disease / sinusoidal obstruction syndrome (VOD/SOS) following hematopoietic stem cell transplantation, but currently without market authorization in Canada.
The TxGNN model's top prediction is **Pseudo-Von Willebrand Disease**, though this is supported by **0 clinical trials** and **0 publications** — making it a pure model-driven hypothesis at this stage.
Across all 10 predicted indications in this multi-indication pack, **Thrombotic Thrombocytopenic Purpura** (Rank 4, L3) represents the strongest evidence signal, backed by 11 publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic veno-occlusive disease / sinusoidal obstruction syndrome (VOD/SOS) post-HSCT — no Canadian DIN data; based on international approval context |
| Predicted New Indication (Top Rank) | Pseudo-Von Willebrand Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Canada Market Status | Not marketed in Canada |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for Defibrotide is not available in this Evidence Pack. Based on information embedded in associated clinical trial records and internal repurposing rationale notes, Defibrotide acts primarily through **endothelial-protective mechanisms** — preventing endothelial cell apoptosis, reducing expression of procoagulant factors, and exerting antithrombotic and profibrinolytic effects. Its established clinical use targets vascular endothelial damage and microvascular thrombosis in the high-risk HSCT setting.

Pseudo-von Willebrand disease (pseudo-vWD, also called platelet-type vWD) is a hereditary platelet disorder caused by gain-of-function mutations in *GP1BA*, leading to increased platelet affinity for large vWF multimers, spontaneous platelet aggregation, and thrombocytopenia. The core pathology sits at the platelet surface receptor (GP1bα) level — a fundamentally different biology from the endothelial injury and intravascular coagulation that Defibrotide targets.

Defibrotide has no known direct regulatory action on the platelet-vWF GP1bα axis. This prediction is supported solely by TxGNN graph-based scoring and carries weak mechanistic plausibility. It should be understood as a hypothesis-generation output, not a clinically actionable lead at this stage.

---

## All Predicted Indications Overview

This Evidence Pack covers 10 predicted indications (multi-indication candidate TW-DB04932-multi):

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|------|---------|-------------|----------------|--------|------------|----------------|
| 1 | Pseudo-Von Willebrand Disease | 99.91% | L5 | 0 | 0 | Hold |
| 2 | Primary Release Disorder of Platelets | 99.91% | L4 | 1 (indirect) | 0 | Hold |
| 3 | Glanzmann Thrombasthenia | 99.88% | L5 | 0 | 0 | Hold |
| **4** | **Thrombotic Thrombocytopenic Purpura** | **99.71%** | **L3** | 0 | **11** | **Research Question** |
| 5 | Scott Syndrome | 99.67% | L5 | 0 | 0 | Hold |
| 6 | Bleeding Diathesis (Collagen Receptor Defect) | 99.43% | L5 | 0 | 0 | Hold |
| 7 | Hemorrhagic Disorder (Constitutional Thrombocytopenia) | 99.39% | L5 | 0 | 0 | Hold |
| 8 | Congenital Factor V Deficiency | 99.30% | L5 | 0 | 0 | Hold |
| 9 | Fetal/Neonatal Alloimmune Thrombocytopenia | 99.23% | L5 | 0 | 0 | Hold |
| **10** | **Thrombocytopenic Purpura** | **99.22%** | **L3** | 0 | **11** | **Research Question** |

---

## Clinical Trial Evidence

No clinical trials were identified for the top prediction (Pseudo-Von Willebrand Disease).

One trial was identified for Rank 2 (Primary Release Disorder of Platelets). Its relevance to platelet release disorders is **indirect** — the trial's primary focus is VOD/SOS:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02851407](https://clinicaltrials.gov/study/NCT02851407) | Phase 3 | Completed | 372 | Defibrotide prophylaxis vs. best supportive care for prevention of hepatic VOD/SOS in high-risk HSCT patients. The primary endpoint is VOD — not platelet release function. Thrombocytopenia observed in VOD is secondary and consumptive in nature. Association with the Rank 2 prediction is considered indirect/incidental. |

---

## Literature Evidence

No literature was identified for the top prediction (Pseudo-Von Willebrand Disease).

For **Thrombotic Thrombocytopenic Purpura** (Rank 4) and **Thrombocytopenic Purpura** (Rank 10), 11 publications were identified (substantially overlapping). Sorted by study quality and recency:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | Mechanistic / In vitro | Thrombosis Research | Defibrotide attenuates endothelial injury caused by COVID-19 patient plasma; demonstrates mechanistic overlap with TTP, aHUS, and VOD via endothelial protection pathways |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | Comprehensive review of TA-TMA in HSCT (incidence 0.5–76%, mortality 60–90%); Defibrotide cited as a potential therapeutic option among limited available treatments |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplantation | TA-TMA diagnosis and management review; underscores lack of consensus therapy and high unmet need; Defibrotide mentioned as investigated agent |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Japanese J Clin Hematol | TA-TMA management overview highlighting complement activation as central pathogenic driver; contextualizes Defibrotide's endothelial protective role |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Case Series | Bone Marrow Transplantation | Describes Defibrotide as a "promising treatment" for TTP in BMT patients — small case series, no control group |
| [11100281](https://pubmed.ncbi.nlm.nih.gov/11100281/) | 2000 | Retrospective Cohort | Bone Marrow Transplantation | TTP incidence and risk factors in 131 leukemic children post-BMT across 4 Italian centers; Defibrotide use discussed in management |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case Series | Clin Appl Thromb Hemost | Defibrotide in recurrent TTP; reports medium-to-long-term remission in refractory cases refractory to plasma exchange — no randomized comparison |
| [8317470](https://pubmed.ncbi.nlm.nih.gov/8317470/) | 1993 | Case Series | Am J Hematol | Early case series reporting treatment of TTP with Defibrotide |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | ⚠️ Case Report (Adverse Event) | Haematologica | **Safety signal: TTP reported as an adverse event occurring *after* Defibrotide therapy** — this counter-signal must be factored into any repurposing evaluation |
| [6547211](https://pubmed.ncbi.nlm.nih.gov/6547211/) | 1984 | Case Report | Nephron | Defibrotide as antithrombotic agent in HUS/TTP-related acute renal failure; earliest reported clinical use in this indication |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | Case Series / Observational | Haemostasis | Effects of Defibrotide on acute renal failure due to thrombotic microangiopathy; supports antithrombotic role in microvascular disease |

---

## Canada Market Information

Defibrotide is currently **not marketed in Canada** and has no Drug Identification Numbers (DINs) on file.

For reference: Defibrotide (brand name **Defitelio®**) has received regulatory approvals from the U.S. FDA (March 2016) and European Medicines Agency (EMA) for treatment of severe hepatic VOD/SOS with multi-organ dysfunction in adult and pediatric HSCT patients. A Canadian New Drug Submission has not been confirmed in available data, representing a significant regulatory gap for any Canada-based repurposing initiative.

---

## Safety Considerations

Please refer to the package insert for safety information.

No package insert warnings, contraindications, or drug interaction data were available for Canada in this Evidence Pack. As a proxy, clinicians should consult the U.S. FDA label or EMA Summary of Product Characteristics for Defitelio®. One notable safety signal from the literature: PMID 7896218 reports TTP occurring as an adverse event following Defibrotide administration — this warrants careful consideration if evaluating repurposing for any thrombotic microangiopathy indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Pseudo-Von Willebrand Disease, Rank 1) carries no mechanistic plausibility and zero clinical evidence — Defibrotide does not act on the GP1bα-vWF axis central to pseudo-vWD pathology. The most evidence-supported predicted indication across the full pack is Thrombotic Thrombocytopenic Purpura (Rank 4, L3), but available literature consists entirely of small case reports and retrospective series from the 1980s–2000s, along with an unresolved adverse event signal (TTP possibly induced by Defibrotide, PMID 7896218). Defibrotide is also not marketed in Canada, creating a regulatory barrier to any domestic repurposing pathway.

**To proceed, the following is needed:**

- Retrieve Defibrotide's full mechanism of action from DrugBank (currently a blocking data gap per DG002)
- Obtain package insert safety data — warnings and contraindications — from FDA/EMA labeling as a proxy for Canadian use (blocking per DG001)
- Formally resolve the adverse event signal (PMID 7896218): determine whether TTP was drug-induced or a manifestation of underlying disease progression in that patient
- For the TTP / TA-TMA indication (Ranks 4 and 10): conduct a systematic literature review to properly quantify effect size, patient populations, and safety across all available case series
- Assess whether a registry-based prospective observational study in HSCT centers using Defibrotide for VOD/SOS could capture TTP/TA-TMA outcomes as secondary endpoints — this is the lowest-cost path to generating new evidence
- Initiate a regulatory landscape review for a potential Health Canada New Drug Submission, as Defibrotide's absence from the Canadian market is a prerequisite barrier to any clinical development program

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

