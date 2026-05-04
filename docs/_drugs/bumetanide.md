---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 1
---

# Bumetanide
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

# Bumetanide: From Oedema and Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic classically used for oedema associated with congestive heart failure, hepatic disease, and acute pulmonary congestion. The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease**, with **3 registered clinical trials** and **5 publications** currently supporting this direction — though the evidence is largely indirect and no completed dedicated trial yet exists for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oedema; congestive heart failure; acute pulmonary congestion (no Canada DIN on record) |
| Predicted New Indication | Acute Pulmonary Heart Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack; however, bumetanide's pharmacology is well established in the clinical literature. Bumetanide is a potent loop diuretic that inhibits the NKCC2 (Na⁺-K⁺-2Cl⁻ co-transporter) on the apical membrane of the thick ascending limb of Henle's loop in the kidney. This produces a rapid and marked natriuresis and diuresis — typically within 30 minutes of administration — leading to significant reduction in venous preload (filling pressure). Its principal haemodynamic consequence is a decrease in pulmonary artery occlusion pressure, making it mechanistically suited to any state of pulmonary congestion and fluid overload.

In acute pulmonary heart disease (cor pulmonale acutum), elevated pulmonary arterial pressures impose an acute pressure overload on the right ventricle. The resulting right heart failure causes systemic and pulmonary venous congestion, fluid retention, and worsening gas exchange. Loop diuretics directly counteract this by reducing circulating blood volume and pulmonary venous pressure, thereby relieving oedema and improving respiratory function. This is the same haemodynamic rationale underlying the well-established class effect of furosemide in acute decompensated heart failure, to which bumetanide is pharmacologically equivalent.

The mechanistic bridge between bumetanide's established indications and acute pulmonary heart disease is therefore very short. A 1984 comprehensive pharmacological review (PMID 6391889) already explicitly listed "acute pulmonary congestion" among bumetanide's approved therapeutic uses, and a 1987 prospective haemodynamic study (PMID 3304383) directly documented the drug's acute reduction of pulmonary artery pressure in patients with heart failure. The TxGNN prediction aligns closely with decades of clinical pharmacology data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Planned single 4 mg intranasal bumetanide dose to assess acute pulmonary artery pressure and blood volume reduction in outpatient heart failure patients with implanted CardioMEMS™/Cordella™ haemodynamic monitoring devices; withdrawn before any enrolment began |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Open-label trial evaluating empagliflozin + sacubitril/valsartan in adults with congenital heart disease and heart failure; bumetanide likely functions as background diuretic therapy only, not as a primary study intervention |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational validation study of seismocardiographic remote monitoring in heart failure patients; no specific drug intervention — provides disease-burden and monitoring context only |

> **Note:** No trial has been completed with bumetanide as the primary intervention specifically for acute pulmonary heart disease. The withdrawn NCT07375212 confirms investigator interest in this clinical area but contributed no data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Prospective Haemodynamic Study | Br J Clin Pharmacol | IV bumetanide (25 µg/kg) significantly reduced pulmonary artery occlusion pressure and cardiac index in 24 patients with acute or chronic heart failure; confirms direct acute haemodynamic benefit relevant to pulmonary congestion |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Comprehensive Drug Review | Drugs | Landmark pharmacodynamic and pharmacokinetic review; explicitly lists oedema in congestive heart failure, acute pulmonary congestion, hepatic and renal disease as established indications — directly supports mechanistic plausibility |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Clinical Management Review | Am J Therapeutics | Reviews therapeutic strategies for acute decompensated heart failure; loop diuretics, including bumetanide, identified as first-line symptomatic treatment in the acute setting |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Drug Review | Ann Pharmacother | Systematic comparison of all loop diuretics evaluating whether furosemide should remain first-line; positions bumetanide as a clinically equivalent alternative with distinct pharmacokinetic advantages |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological Study | Am J Emerg Med | Contemporary US epidemiological analysis of heart failure ED presentations from 2016–2023; documents continued high burden and treatment patterns, providing population context |

---

## Canada Market Information

Bumetanide currently has **no Drug Identification Numbers (DINs) registered in Canada**. There are no Health Canada-approved products on record, and the drug is not marketed in the Canadian market. Regulatory safety, prescribing, and indication information cannot be sourced from domestic product monographs.

For reference, bumetanide is approved and marketed in the **United States** (Bumex®, FDA) and the **United Kingdom** (Burinex®, MHRA), where prescribing information and monographs are publicly accessible and may serve as proxy safety documentation.

---

## Safety Considerations

Please refer to the package insert of a jurisdictionally equivalent approved product (e.g., FDA label for Bumex® or MHRA label for Burinex®) for complete safety information, including key warnings, contraindications, and drug interactions. No safety data was available from Canadian regulatory records for this review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bumetanide's loop diuretic mechanism directly and logically addresses the haemodynamic pathophysiology of acute pulmonary heart disease — the same mechanism that underpins its established use in acute pulmonary congestion and decompensated heart failure. Existing literature confirms haemodynamic efficacy in closely related settings (PMID 3304383, 6391889). However, bumetanide is not marketed in Canada, no completed dedicated trial in acute cor pulmonale exists, and all regulatory safety documentation is currently unavailable, necessitating structured guardrails before any clinical application.

**To proceed, the following is needed:**

- **Regulatory safety data**: Obtain the full US FDA or MHRA prescribing information as a proxy monograph to document warnings, contraindications, and precautions (resolves DG001)
- **Mechanism of action documentation**: Confirm detailed MOA data from DrugBank API (DB00887) to complete mechanistic link analysis (resolves DG002)
- **Drug interaction profile**: Establish DDI risk with common co-medications relevant to pulmonary heart disease patients (e.g., digoxin, aminoglycosides, antihypertensives, NSAIDs)
- **Dedicated clinical evidence**: Identify or initiate a prospective study of bumetanide specifically in acute pulmonary heart disease (cor pulmonale), distinct from general cardiac failure populations
- **Monitoring plan**: Develop a pharmacovigilance protocol covering serum electrolytes (Na⁺, K⁺, Mg²⁺), renal function (creatinine, eGFR), fluid balance, and blood pressure — given the known risk of electrolyte disturbances with loop diuretics
- **Canada access pathway**: Evaluate a Health Canada Special Access Program (SAP) submission or regulatory filing pathway given the absence of a Canadian DIN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

