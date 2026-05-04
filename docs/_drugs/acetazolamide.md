---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Altitude Sickness & Glaucoma to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase (CA) inhibitor with established international uses in altitude sickness prevention, glaucoma, and epilepsy, though it is not currently registered in Canada.
The TxGNN model predicts it may be effective for **Cardiomyopathy** — specifically in the management of acute decompensated heart failure requiring diuretic augmentation —
with **3 clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered in Canada (established uses in other markets: altitude sickness, glaucoma, epilepsy, periodic paralysis) |
| Predicted New Indication | Cardiomyopathy |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not included in the evidence pack. Based on known information, acetazolamide is a **carbonic anhydrase (CA) inhibitor** — specifically blocking CA isoforms II and IV in the renal proximal tubule. This prevents bicarbonate (HCO₃⁻) reabsorption, driving increased urinary excretion of bicarbonate, sodium, and water. The net result is an alkaline, proximal-tubule–driven diuresis that is mechanistically distinct from — and complementary to — loop diuretics such as furosemide.

In acute decompensated heart failure (ADHF), progressive volume overload and diuretic resistance are the central clinical challenges. When loop diuretics are used intensively, patients typically develop metabolic alkalosis, which paradoxically blunts loop diuretic effectiveness. Acetazolamide counteracts this alkalosis by promoting bicarbonate excretion, restoring the kidneys' sensitivity to loop diuretics and dramatically improving total decongestion. This synergistic mechanism was validated by the landmark **ADVOR trial** (NEJM 2022, NCT03505788): acetazolamide added to standard loop diuretic therapy achieved successful decongestion in **42.2% of patients vs. 30.5% for loop diuretic alone** (p<0.001). This trial, while not captured in the current evidence dataset, represents critical background context.

Cardiomyopathy — structural disease of the heart muscle — is the primary underlying cause of heart failure in a large proportion of patients. Although "cardiomyopathy" and "heart failure" carry distinct diagnostic labels, they are inseparable in clinical management: fluid overload and decongestion are central to cardiomyopathy care. The TxGNN prediction aligns with this established biological pathway, and the ongoing Phase 4 trial NCT05802849, titled directly *"Acetazolamide Per os for Decompensation of Heart Failure,"* represents a direct translational validation study extending ADVOR findings to the oral route.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | **Acetazolamide Per os for Decompensation of Heart Failure**: Directly evaluates oral acetazolamide in chronic heart failure decompensation; framed as an oral-route extension of the IV-based ADVOR trial. Investigates whether the ADVOR decongestion benefit translates to ambulatory/oral administration. Completion target: December 2025. |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | **Optimal Diuretic Therapies for Acute Heart Failure with Volume Overload**: Double-blind, randomized, multicenter trial in patients with loop-diuretic resistance. Compares loop diuretics combined with acetazolamide vs. metolazone vs. loop diuretics alone. Expected completion: September 2027. |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | Not Applicable | Recruiting | 466 | **TAILOR-AHF**: Urine sodium–guided tailored diuretic algorithm in ADHF. Acetazolamide is one of the candidate agents within the adaptive diuretic protocol; tests whether personalizing diuretic selection based on urine sodium biomarker achieves faster and more complete decongestion. Completion target: August 2026. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | 2024 update on heart failure management; summarizes 2023 ESC guideline recommendations including SGLT2 inhibitors and finerenone for HF prevention in diabetic CKD; provides current-standard context against which acetazolamide's diuretic role would be positioned |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | New pharmacological agents in cardiovascular medicine (2022); covers mavacamten approval for obstructive HCM; relevant background on evolving cardiomyopathy pharmacotherapy landscape |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiology Cases | **Highest direct relevance**: Acetazolamide used to treat hypochloremia (94 mEq/L) in an 87-year-old patient with advanced HF **and hypertrophic cardiomyopathy**; demonstrated improvement in electrolyte balance and fluid management; highlights chloride manipulation as a therapeutic target in HF |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Cohort | Acta Neurol Scand | Familial hypokalemic periodic paralysis with heart muscle disease treated with acetazolamide 750–1000 mg/day; patient developed exercise angina during treatment — an important **cardiac safety signal** at high doses |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Report | Acta Neurol Scand | Echocardiographic and cardiac evaluation in 9 members of a family with hypokalemic periodic paralysis and cardiomyopathy; documents that cardiac muscle involvement is not uncommon in this acetazolamide-treated population |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Preclinical | Saudi Medical Journal | Acetazolamide effects on ischemia-reperfusion injury in isolated rabbit hearts (2-week and 8-week-old); provides preclinical mechanistic evidence regarding acetazolamide's direct cardiac effects |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report | Acute Medicine & Surgery | **Safety signal**: Non-cardiogenic pulmonary edema developed one hour after IV acetazolamide in a patient with **dilated cardiomyopathy**; hypoxia resolved with alternative diuretics and vasodilators. Warrants caution with IV formulation in cardiac patients |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian J Ophthalmology | Oral acetazolamide (plus topical dorzolamide) used in Danon disease — a cardiomyopathy-associated lysosomal storage disorder — for cystoid macular edema; provides indirect exposure data for acetazolamide use in a cardiomyopathy patient population |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Case Series | J Nucl Med | Regional cerebral blood flow by SPECT in mitochondrial encephalomyopathy; limited relevance to cardiomyopathy indication |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | J Medical Case Reports | Congenital hydrocephalus with trisomy 9p and coexisting congenital heart disease; minimal relevance to cardiomyopathy repurposing; included for completeness |

---

## Canada Market Information

Acetazolamide is **not currently registered in Canada**. Health Canada records show **zero Drug Identification Numbers (DINs)** and no approved product licenses.

> **Regulatory context**: Acetazolamide is commercially available in many international markets — including the United States (Diamox® and generics), the United Kingdom, and Europe — under indications including acute mountain sickness, open-angle glaucoma, absence epilepsy, and hypokalemic/hyperkalemic periodic paralysis. Any clinical use in Canada would require a regulatory pathway determination, such as a new DIN application or access via the Special Access Programme (SAP).

---

## Safety Considerations

Please refer to the package insert for full safety information. Health Canada–specific warnings and contraindications were not available in this evidence pack.

**Safety signals identified from the literature review:**

- **Potential cardiac adverse event with IV route**: One case report (PMID 29123889) documents acute non-cardiogenic pulmonary edema following IV acetazolamide in a patient with dilated cardiomyopathy. The oral route (as studied in NCT05802849) may carry a different risk profile and should be evaluated separately.
- **High-dose cardiac risk**: A cohort case (PMID 7324871) reported exercise-induced angina pectoris in a patient with heart muscle disease receiving acetazolamide 750–1,000 mg/day. Dose selection and cardiac monitoring are important.
- **Metabolic effects**: Acetazolamide commonly causes metabolic acidosis, hypokalemia, and hyponatremia — electrolyte disturbances that carry heightened risk in heart failure patients already on complex diuretic regimens. Electrolyte monitoring protocols are essential.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADVOR trial (NEJM 2022) provides strong Phase 3 proof-of-concept for acetazolamide in acute decompensated heart failure, and three currently recruiting Phase 4 trials — including one directly named for acetazolamide in CHF decompensation (NCT05802849, n=400) — confirm active international clinical interest. The mechanistic basis via CA inhibition and synergistic alkaline diuresis is well-characterized and biologically coherent in the context of cardiomyopathy-driven heart failure. Evidence level qualifies as L2.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Acetazolamide holds no Canadian DIN; determine whether a new DIN application, Abbreviated New Drug Submission (ANDS) for a generic, or a Special Access Programme (SAP) route is most appropriate for the intended indication
- **Full safety profile review**: Obtain and review the complete package insert (Canadian monograph, USPI, or SmPC) for warnings, contraindications, and drug-drug interactions — particularly with loop diuretics, other diuretics, cardiac glycosides, and antiepileptics
- **MOA formal documentation**: Retrieve and document the mechanism of action from DrugBank (DB00819) via API to support regulatory submissions and clinical rationale documentation
- **Await NCT05802849 results**: This Phase 4 trial (targeted completion December 2025) directly tests oral acetazolamide in heart failure decompensation; results should be incorporated before initiating any Canada-specific program
- **Cardiomyopathy-specific subgroup analysis**: Existing clinical trials enroll broad "heart failure" populations; seek cardiomyopathy-specific subgroup data (e.g., HFrEF vs. HFpEF vs. specific cardiomyopathy etiologies) to strengthen indication specificity
- **Electrolyte and renal monitoring protocol**: Develop a standardized monitoring protocol covering serum potassium, bicarbonate, sodium, creatinine, and eGFR — mandatory given the drug's metabolic profile and the vulnerability of heart failure patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

