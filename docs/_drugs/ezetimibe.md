---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a selective intestinal cholesterol absorption inhibitor, established globally as a standard treatment for hypercholesterolemia and mixed dyslipidemia, though no Canadian product licenses are currently captured in the regulatory dataset.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**, with evidence from **multiple Phase 3/4 clinical trials** and **19 publications** providing strong mechanistic and clinical support.
This prediction closely aligns with ezetimibe's well-documented pharmacological profile, representing a high-confidence validation of its lipid-lowering role in the Canadian market context.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Dyslipidemia (established global use; Canadian DINs not found in current dataset — likely a data gap) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed (no DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ezetimibe selectively inhibits NPC1L1 (Niemann-Pick C1-Like 1), a sterol transporter protein on the intestinal brush-border membrane. By blocking this transporter, ezetimibe prevents absorption of both dietary and biliary cholesterol from the small intestine, reducing cholesterol delivery to the liver via chylomicrons. This triggers compensatory upregulation of hepatic LDL receptors and lowers plasma LDL-C by approximately 15–20% as monotherapy. When combined with statins — which inhibit endogenous cholesterol synthesis via HMG-CoA reductase — the two complementary mechanisms produce an additive LDL-C reduction of up to 60–70%.

Hyperlipoproteinemia is a spectrum of lipid metabolism disorders characterized by elevated circulating lipoproteins, encompassing elevated LDL (Fredrickson Type IIa), elevated LDL plus VLDL/triglycerides (Type IIb), and conditions involving excess chylomicron remnants. Ezetimibe's mechanism directly addresses the LDL-elevating subtypes, and by reducing intestinal lipid load, it also lowers atherogenic remnant delivery relevant to other hyperlipoproteinemia types. The mechanistic rationale further notes that ezetimibe provides adjunctive lipid-lowering benefit in conditions with excess chylomicrons and VLDL remnants, consistent with the breadth of the hyperlipoproteinemia classification.

Globally, ezetimibe is approved as monotherapy and in fixed-dose combinations with statins (Vytorin®/Inegy® as ezetimibe/simvastatin) across the United States, European Union, Japan, and numerous other jurisdictions. Multiple completed Phase 3/4 trials — including large-scale real-world studies enrolling thousands of patients and head-to-head comparisons against PCSK9 inhibitors — consistently confirm its efficacy and safety across the hyperlipoproteinemia spectrum. The TxGNN model's top-ranked prediction for this indication therefore reflects both strong mechanistic plausibility and extensive clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Randomized open-label parallel comparison of ezetimibe monotherapy versus statin therapy for hypercholesterolemia; directly evaluated lipid-lowering efficacy and safety profile of ezetimibe |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A (observational) | Completed | 2,089 | VYTORIN (ezetimibe/simvastatin) large-scale post-approval re-examination in Japan; confirmed real-world safety and efficacy of ezetimibe combination therapy over 52 weeks |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab vs. ezetimibe in statin-intolerant hypercholesterolemic patients (GAUSS-2); ezetimibe as active comparator confirming its standard-of-care benchmark role for LDL-C reduction |
| [NCT01763905](https://clinicaltrials.gov/study/NCT01763905) | Phase 3 | Completed | 307 | AMG 145 (evolocumab) vs. ezetimibe in statin-intolerant patients; 12-week LDL-C reduction data with ezetimibe as active control, reflecting its established efficacy threshold |
| [NCT04895098](https://clinicaltrials.gov/study/NCT04895098) | N/A (observational) | Completed | 1,000 | Retrospective comparative study of statin monotherapy vs. statin+ezetimibe for CVD primary and secondary prevention; real-world evidence for combination benefit |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment-use study of ezetimibe 10 mg in homozygous familial hypercholesterolemia and homozygous sitosterolemia; safety data in severe hyperlipoproteinemia phenotypes |
| [NCT00189085](https://clinicaltrials.gov/study/NCT00189085) | Phase 4 | Completed | 20 | Ezetimibe effects on postprandial hyperlipidemia and endothelial dysfunction in metabolic syndrome; mechanistic proof-of-concept for NPC1L1 inhibition on postprandial lipaemia |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib + ezetimibe fixed-dose combination (TANDEM) in HeFH/ASCVD on maximally tolerated lipid-modifying therapy; demonstrated additive LDL-C lowering with ezetimibe as combination backbone |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1,220 | Ezetimibe/simvastatin co-administered with extended-release niacin in Type IIa/IIb hyperlipidemia; large-scale efficacy and safety data across hyperlipoproteinemia subtypes |
| [NCT04433533](https://clinicaltrials.gov/study/NCT04433533) | Phase 4 | Unknown | 200 | Rosuvastatin/ezetimibe combination vs. rosuvastatin monotherapy in patients with LV diastolic dysfunction and hyperlipidemia; explored broader cardiovascular benefits of ezetimibe-containing regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | Lancet | TANDEM trial: obicetrapib + ezetimibe fixed-dose combination vs. placebo showed significant additive LDL-C reduction on top of maximally tolerated therapy; validates ezetimibe as a foundational component in combination lipid-lowering for hyperlipoproteinemia |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide vs. placebo in HeFH patients; ezetimibe contextualised as existing standard that remains insufficient for many patients to achieve LDL-C targets |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Systematic Review | J Cardiovasc Pharmacol Ther | Comprehensive PCSK9 inhibitor review; ezetimibe identified as key second-line agent for LDL-C reduction in statin-intolerant patients and refractory hyperlipoproteinemia |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Clinical Guideline | European Heart Journal | EAS consensus statement on familial hypercholesterolaemia; ezetimibe recommended as standard adjunct in lipid-lowering therapy, establishing its guideline-supported role in hyperlipoproteinemia management |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Narrative Review | Mol Med Reports | Current landscape of hyperlipidemia drug targets; ezetimibe reviewed as established NPC1L1 inhibitor and indispensable adjunct across the hyperlipoproteinemia treatment algorithm |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Postprandial hyperlipidemia: pathophysiology and atherogenesis; ezetimibe's mechanism for reducing postprandial TG-rich lipoprotein accumulation and its potential in mixed hyperlipoproteinemia discussed |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | FH treatment overview; ezetimibe listed alongside statins and bile acid sequestrants as a proven LDL-lowering therapy, with early treatment linked to substantial reduction in cardiovascular events |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Curr Cardiol Reports | Global burden of familial hypercholesterolemia; ezetimibe + statin combination highlighted as primary evidence-based strategy for achieving LDL-C targets in genetically driven hyperlipoproteinemia |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review/Primer | Nat Rev Dis Primers | Comprehensive FH primer covering genetics, diagnosis, and treatment; ezetimibe discussed as important adjunct to statin therapy for patients with hereditary forms of hyperlipoproteinemia |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | Updated FH review emphasizing underdiagnosis and cascade screening; ezetimibe positioned as essential second-line agent when statin monotherapy is insufficient in hyperlipoproteinemia management |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3/4 clinical trials — including studies with over 2,000 patients — and extensive real-world surveillance data consistently confirm ezetimibe's efficacy and safety in hyperlipoproteinemia; the TxGNN L1 evidence score reflects this strong clinical foundation, and the drug's NPC1L1 inhibition mechanism provides clear biological plausibility for its role across the full hyperlipoproteinemia spectrum.

**To proceed, the following is needed:**
- **Regulatory status verification**: Confirm whether Health Canada DINs exist for ezetimibe products (Zetia®, Vytorin®/Inegy®) — the current dataset records zero DINs, which is very likely a data gap given ezetimibe's global regulatory status
- **MOA data retrieval**: Query DrugBank API (DB00973) to obtain complete mechanism of action documentation to supplement the mechanistic analysis
- **Safety documentation**: Obtain the Canadian product monograph to extract key warnings, contraindications, and clinically significant drug interactions (particularly with cyclosporine, fibrates, and bile acid sequestrants)
- **Cardiovascular outcomes review**: Assess landmark outcomes trials (e.g., IMPROVE-IT) for cardiovascular event reduction data to support any formal indication filing
- **Market entry pathway**: If ezetimibe is confirmed to lack Canadian approval, determine whether a New Drug Submission (NDS) or Abbreviated New Drug Submission (ANDS) to Health Canada is appropriate, or whether this constitutes a data capture error requiring database correction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

