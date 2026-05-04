---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase: From Acute Ischemic Stroke to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Alteplase is an internationally established recombinant tissue plasminogen activator (rt-PA) used as a thrombolytic agent for acute ischemic stroke, ST-elevation myocardial infarction (STEMI), and massive pulmonary embolism; however, no Canadian Drug Identification Numbers (DINs) are currently on record.
The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction** — an anatomical subtype of inferior STEMI involving simultaneous posterior wall involvement —
with **0 dedicated clinical trials** and **1 publication** currently supporting this specific indication direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute ischemic stroke, STEMI, and pulmonary embolism (internationally established; no Canadian DIN on record) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, alteplase is a recombinant tissue-type plasminogen activator that selectively binds to fibrin within a thrombus and converts plasminogen to plasmin, initiating localized fibrinolysis with limited systemic fibrinogen depletion. This mechanism directly targets fibrin-rich coronary thrombi responsible for acute coronary artery occlusion — the central event in any STEMI subtype. Its use in standard inferior and anterior STEMI is well-documented in landmark trials such as GUSTO and TAMI.

Posteroinferior myocardial infarction is a specific anatomical STEMI subtype typically caused by acute occlusion of the right coronary artery (RCA) or, less commonly, the left circumflex artery (LCx), with concurrent ischaemia of both the inferior and posterior walls. Because the fibrin-rich coronary thrombus is the common pathophysiological driver, alteplase's thrombolytic mechanism is directly applicable to this subtype. The TxGNN model's high prediction score (99.79%) most likely reflects a strong knowledge graph topology linking STEMI subtypes → coronary thrombolysis → alteplase.

However, posteroinferior MI carries unique clinical complexity. Posterior wall involvement requires additional posterior ECG leads (V7–V9) for diagnosis, and reperfusion assessment criteria differ from anterior STEMI. These diagnostic challenges mean that clinical outcomes following thrombolysis in this specific subtype may diverge from the broader STEMI population, necessitating independent subtype-level evidence before definitive clinical conclusions can be drawn.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for alteplase in posteroinferior myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16294818](https://pubmed.ncbi.nlm.nih.gov/16294818/) | 2005 | Retrospective Observational | Archivos de cardiologia de Mexico | Evaluated short-term clinical and angiographic outcomes of rescue percutaneous transluminal coronary angioplasty (RPTCA) in patients with acute MI following failed thrombolysis; provides indirect context for thrombolysis failure management in the acute MI setting including inferior/posterior subtypes |

---

## Canada Market Information

Alteplase does not currently hold any Drug Identification Numbers (DINs) in the Canadian regulatory database. The product is not marketed in Canada per available evidence pack data. International formulations (e.g., Activase®, Cathflo Activase®) are approved by the U.S. FDA and other regulatory agencies, but Canadian market authorization requires a separate Health Canada submission.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The biological basis for using alteplase in posteroinferior MI is mechanistically sound — this subtype shares the same fibrin-rich coronary thrombus pathophysiology as all other STEMI types — but only a single retrospective observational study with indirect relevance was identified, and no dedicated clinical trials exist for this specific anatomical subtype. The evidence base is insufficient to support a clinical application decision at this time.

**To proceed, the following is needed:**
- Targeted subgroup analysis of existing large STEMI thrombolysis RCTs (e.g., GUSTO, TAMI-1 through TAMI-5) specifically isolating posteroinferior MI patients to assess differential thrombolysis efficacy and safety
- Prospective registry or feasibility study comparing thrombolysis vs. primary PCI outcomes in posteroinferior MI, with standardized posterior lead ECG criteria (V7–V9) for patient identification
- Resolution of MOA data gap (DG002): retrieval of full alteplase pharmacology from DrugBank API to support mechanistic analysis
- Resolution of safety data gap (DG001): download and parse Health Canada–approved package insert to complete contraindication and warning profile
- Health Canada regulatory filing (New Drug Submission or Supplemental NDS) to establish a Canadian DIN before any domestic clinical application

> **Note:** This report presents the top-ranked TxGNN prediction (Rank 1 — Posteroinferior Myocardial Infarction). Eight additional predicted indications were evaluated in this analysis, ranging from **Proceed with Guardrails** (Septal Myocardial Infarction, L2; Coronary Stenosis, L2) to **Research Question** (Posterolateral MI, Congenital Coronary Artery Anomaly, Thrombophilia) to **Hold** (Heparin Cofactor 2 Deficiency, Factor 5 Excess with Spontaneous Thrombosis, Antithrombin Deficiency Type 2). The highest-priority actionable indication based on available evidence is **Septal Myocardial Infarction** (Rank 3, L2, Proceed with Guardrails), supported by TAMI-1 RCT subgroup data and direct alteplase late-thrombolysis studies.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

