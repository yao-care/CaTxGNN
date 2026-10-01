---
layout: default
title: Bumetanide
parent: Model Prediction Only (L5)
nav_order: 131
evidence_level: L5
indication_count: 1
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Bumetanide: From Edema Associated with Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a loop diuretic used to treat edema, mainly in congestive heart failure, hepatic disease and renal disease.
The TxGNN model predicts it may be effective for **acute pulmonary heart disease** (acute cor pulmonale), with **3 registered clinical trials** and **5 publications** found. None of these studies directly addresses this condition, so the signal rests on indirect evidence from heart failure.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Edema associated with congestive heart failure (per the literature review; the Canadian license records list no indication text) |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 (indirect evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this record. Pharmacologically, bumetanide is a loop diuretic that inhibits NKCC2 in the thick ascending limb of the loop of Henle. This produces rapid natriuresis and diuresis. In acute cor pulmonale, where the right ventricle is suddenly overloaded with pressure, removing excess fluid can lower right ventricular preload and wall stress. The mechanism is therefore plausible.

The supporting evidence is indirect. It comes from left-sided or general heart failure, where bumetanide is already used for edema. This makes the prediction closer to an extension of the existing use than a truly novel repurposing.

There is also a safety caveat. In acute cor pulmonale, reducing preload too aggressively can lower cardiac output, so the benefit-risk balance depends on the clinical context. The high TxGNN score is a computational prediction and is not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Planned single 4 mg intranasal bumetanide dose to reduce pulmonary artery pressure and blood volume in heart failure patients with implanted monitoring devices (CardioMEMS/Cordella). Withdrawn, so no data. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Open-label study of empagliflozin and sacubitril/valsartan in adults with heart failure with reduced ejection fraction and congenital heart disease. Bumetanide is not clearly the investigational agent. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational study of seismocardiographic remote monitoring in heart failure. No efficacy or safety data for bumetanide. |

All three trials were graded low relevance (C). None targets acute pulmonary heart disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical hemodynamic study (n=24) | Br J Clin Pharmacol | IV bumetanide reduced cardiac index and pulmonary artery occluded pressure in patients with acute exercise-induced or chronic heart failure. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Bumetanide is a potent loop diuretic for edema in congestive heart failure, hepatic and renal disease, and acute pulmonary congestion. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews acute heart failure management, where diuretic agents are the mainstay of therapy. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Compares pharmacokinetics, safety, efficacy and cost of loop diuretics, asking whether furosemide should be first line. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiology / cohort | Am J Emerg Med | Describes heart failure presentations to US emergency departments from 2016 to 2023. Background context only. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 728284 | BURINEX |
| 728276 | BURINEX |

Dosage form and approved indication text are not listed in the license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, but no study directly examines bumetanide in acute pulmonary heart disease. The only interventional trial on bumetanide was withdrawn with no participants, and the rest of the evidence comes from general heart failure. Because there is a risk of excessive preload reduction and reduced cardiac output, the safety profile cannot be assumed transferable.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings and contraindications), which is required for safety screening
- Mechanism-of-action data from DrugBank, to cross-check the mechanistic link
- Clinical evidence directly in acute cor pulmonale or acute right ventricular pressure overload
- A clinical-context assessment of the benefit-risk balance, specifically the risk of reduced cardiac output
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

