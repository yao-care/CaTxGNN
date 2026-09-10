---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

Using the evidence pack, I noticed this candidate (`TW-DB00883-multi`) has **10 predicted indications** with very different evidence strength — the highest TxGNN score (alopecia) has zero supporting studies, while a lower-ranked signal (vascular disease) has 50 trials + 20 papers. I led the report with the evidence-strongest candidate rather than the raw rank-1 score, and kept the others visible for transparency.

---

# Isosorbide Dinitrate: From Antianginal Vasodilator to Vascular Disease (with Pulmonary Hypertension as a Secondary Signal)

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is an established nitric oxide (NO)-donor vasodilator used internationally for angina pectoris and coronary artery disease, though it is currently **not marketed** in this jurisdiction (0 licenses on file). TxGNN flags 10 candidate indications; the two backed by real-world evidence are **Vascular Disease** (**50 clinical trials**, **20 publications**, evidence level L1) and **Pulmonary Hypertension** (0 trials, 20 publications, evidence level L3) — the remaining 8 candidates (e.g., alopecia, hypotrichosis) have TxGNN scores above 99.9% but **zero** supporting trials or literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file locally (0 licenses); internationally known as a nitrate vasodilator for angina pectoris / coronary artery disease |
| Predicted New Indication | Vascular Disease (primary signal, L1) — Pulmonary Hypertension (secondary signal, L3) |
| TxGNN Prediction Score | 99.97% (Vascular Disease) |
| Evidence Level | L1 (Vascular Disease) / L3 (Pulmonary Hypertension) |
| Canada Market Status | Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails (Vascular Disease) / Research Question (Pulmonary Hypertension) |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug (DrugBank MOA field is a data gap). Based on the pharmacological context embedded in the repurposing rationale, ISDN is a nitric oxide (NO) donor that activates soluble guanylate cyclase (sGC), raising intracellular cGMP and relaxing vascular smooth muscle — the established mechanism of the nitrate class used for angina, coronary artery disease, and peripheral vascular conditions.

**Vascular Disease** is therefore not a mechanistically novel prediction but essentially a restatement of ISDN's known pharmacology (antianginal, coronary, and peripheral vasodilation). The 50 clinical trials and 20 publications reflect decades of real-world use of ISDN and its analogues (isosorbide mononitrate, hydralazine/ISDN combinations) across angina, heart failure, and small-vessel disease. Because the drug is not currently marketed here, this candidate is better framed as a **market-entry / label-extension opportunity** than a true repurposing discovery.

**Pulmonary Hypertension** is mechanistically plausible via the same NO→sGC→cGMP pathway used by approved PAH therapies (inhaled NO, PDE5 inhibitors, riociguat). However, the supporting literature is largely small, older (1970s–1990s) hemodynamic studies rather than modern RCTs, there are zero registered clinical trials for this specific pairing, and chronic nitrate use carries a well-documented tolerance liability — so this remains a research hypothesis rather than a near-term regulatory candidate.

---

## Clinical Trial Evidence

### Primary signal: Vascular Disease

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00143195](https://clinicaltrials.gov/study/NCT00143195) | Phase 4 | Completed | 200 | Long-acting nitrate (isosorbide-5-mononitrate) vs. amlodipine for anti-ischemic efficacy/safety in stable angina |
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | Completed | 68 | ISDN spray + chitosan gel for diabetic foot ulcers |
| [NCT03451591 (LACI-2)](https://clinicaltrials.gov/study/NCT03451591) | Phase 2/3 | Completed | 363 | Cilostazol + isosorbide mononitrate to prevent recurrent lacunar stroke / cerebral small vessel disease progression |
| [NCT02305095](https://clinicaltrials.gov/study/NCT02305095) | N/A | Completed | 225 | Genomic sub-study on enhanced response to fixed-dose ISDN/hydralazine in African Americans with HFrEF |
| [NCT01769079](https://clinicaltrials.gov/study/NCT01769079) | Phase 4 | Completed | 95 | Multicenter trial on withdrawal of chronic oral nitrate therapy in stable angina |
| [NCT02228408](https://clinicaltrials.gov/study/NCT02228408) | Phase 4 | Completed | 17 | Hydralazine/ISDN vs. placebo on cardiac structure/function in hemodialysis-dependent ESRD |
| [NCT03255512 (VISOR)](https://clinicaltrials.gov/study/NCT03255512) | Phase 1 | Completed | 41 | Pharmacodynamic drug-drug interaction, safety and tolerability of isosorbide mononitrate + vericiguat in stable CAD |
| [NCT02522208](https://clinicaltrials.gov/study/NCT02522208) | Phase 1 | Completed | 12 | Crossover PK/PD study of BiDil (fixed-dose ISDN/hydralazine) vs. extended-release formulation in heart failure |
| [NCT00337116](https://clinicaltrials.gov/study/NCT00337116) | Phase 4 | Withdrawn | 80 | RCT comparing IV vs. sublingual ISDN for relief of acute anginal episodes in ACS |
| [NCT03072121](https://clinicaltrials.gov/study/NCT03072121) | Phase 4 | Unknown | 440 | Adjunct Chinese herbal therapy (Shexiang Baoxin Pill) in CAD not amenable to revascularization — same disease population, not direct ISDN arm |

### Secondary signal: Pulmonary Hypertension

Currently no related clinical trials registered for this specific drug–disease pairing.

---

## Literature Evidence

### Primary signal: Vascular Disease

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1094819](https://pubmed.ncbi.nlm.nih.gov/1094819/) | 1975 | RCT | American Heart Journal | Double-blind comparison of placebo vs. oral ISDN hemodynamics in significant coronary artery disease |
| [36219567](https://pubmed.ncbi.nlm.nih.gov/36219567/) | 2023 | RCT | Stroke and Vascular Neurology | LACI-2 trial protocol/statistical plan: cilostazol + isosorbide mononitrate for cerebral small vessel disease |
| [3325229](https://pubmed.ncbi.nlm.nih.gov/3325229/) | 1987 | Clinical Study | Current Medical Research and Opinion | Multi-centre comparison of ISDN retard vs. isosorbide-5-mononitrate in 200 coronary patients |
| [805037](https://pubmed.ncbi.nlm.nih.gov/805037/) | 1975 | Comparative Clinical Study | Chest | ISDN vs. nitroglycerin for relieving angina during uninterrupted exercise |
| [29682995](https://pubmed.ncbi.nlm.nih.gov/29682995/) | 2018 | RCT | Diabetes & Vascular Disease Research | Double-blind RCT: ISDN spray + chitosan gel for diabetic foot ulcers |
| [813510](https://pubmed.ncbi.nlm.nih.gov/813510/) | 1976 | Comparative Study | American Journal of Cardiology | Nitroglycerin vs. ISDN effects on coronary collateral vessels and ischemic myocardium (canine model) |
| [1576038](https://pubmed.ncbi.nlm.nih.gov/1576038/) | 1992 | Review | AACN Clinical Issues | Overview of nitrate use in angina, heart failure, cardiogenic shock, and portal hypertension |
| [9951954](https://pubmed.ncbi.nlm.nih.gov/9951954/) | 1999 | Review | Drugs | Review of long-acting isosorbide mononitrate formulations and antianginal efficacy |
| [3925742](https://pubmed.ncbi.nlm.nih.gov/3925742/) | 1985 | Review | American Heart Journal | Review of nitrate tolerance mechanisms and clinical implications |
| [30687454](https://pubmed.ncbi.nlm.nih.gov/30687454/) | 2018 | Mechanistic/Preclinical | Oxidative Medicine and Cellular Longevity | Endothelin receptor antagonist macitentan mitigates ISMN/ISDN-induced endothelial dysfunction and oxidative stress |

### Secondary signal: Pulmonary Hypertension

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Clinical Study | Heart and Vessels | Bolus ISDN reduces mean pulmonary arterial pressure in PH with cardiopulmonary comorbidities |
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | Randomized, Double-blind Study | Clinical Pharmacology and Therapeutics | Oral ISDN vs. placebo hemodynamic response in COPD-associated pulmonary hypertension |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Comparative Clinical Study | Bulletin Européen de Physiopathologie Respiratoire | Sublingual ISDN vs. nitroglycerin in COPD-associated pulmonary hypertension |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | Clinical Hemodynamic Study | Acta Anaesthesiologica Scandinavica | Pulmonary vascular effects of nitroglycerin vs. ISDN in end-stage cardiomyopathy (transplant screening) |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | Clinical Study | European Heart Journal | Two-year ISDN therapy sustained reduction of pulmonary hypertension in interstitial lung fibrosis (n=18) |
| [19620510](https://pubmed.ncbi.nlm.nih.gov/19620510/) | 2009 | Cohort Study | Hypertension | Fixed-dose ISDN/hydralazine effects on diastolic function and exercise capacity in hypertension-induced diastolic heart failure |

---

## Canada Market Information

This drug currently has no marketing authorization records in this jurisdiction — **0 DINs on file, status: Not Marketed**. No license-level product, dosage form, or indication text is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Vascular Disease) / **Research Question** (Pulmonary Hypertension) / **Hold** (all other 8 candidates — alopecia, hypotrichosis-related conditions, hypertrichosis, kyphoscoliotic heart disease, visceral calciphylaxis, arterial thoracic outlet syndrome)

**Rationale:**
- Vascular Disease is supported by an L1 evidence base (50 trials incl. completed Phase 3/4 studies, 20 publications incl. RCTs) and is mechanistically identical to ISDN's established pharmacology — this is a market-entry decision more than a novel-mechanism discovery.
- Pulmonary Hypertension has a plausible NO/cGMP mechanistic rationale and 20 supporting publications, but no registered trials and mostly outdated (pre-1990s) hemodynamic studies — warrants further research scoping, not immediate action.
- The remaining 8 TxGNN-flagged indications (all L5, score >99.9%) have **no** clinical trial or literature support and should remain on Hold pending independent validation.

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety assessment)
- Structured mechanism-of-action data from DrugBank (currently a **High**-severity data gap affecting mechanistic-link analysis)
- Local regulatory pathway assessment given 0 current licenses (market-entry filing requirements)
- For Pulmonary Hypertension: a targeted evidence review to determine whether modern RCT-level data exists beyond the historical hemodynamic studies identified here, plus assessment of nitrate tolerance management in a chronic PH regimen
- Drug interaction data (DDI query returned no results) — needs direct source verification given known nitrate contraindications (e.g., PDE5 inhibitors)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

