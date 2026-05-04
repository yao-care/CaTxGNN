---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atorvastatin: From Dyslipidemia to Familial Hypercholesterolemia

## One-Sentence Summary

Atorvastatin is a second-generation synthetic statin and HMG-CoA reductase inhibitor, widely established for the treatment of dyslipidemia and prevention of cardiovascular disease.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**, a monogenic disorder of LDL metabolism causing severely elevated LDL-C from birth,
with **35 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrievable from Canada database (0 DINs on record) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the connected database. Based on well-established pharmacological knowledge, atorvastatin is a potent inhibitor of **HMG-CoA reductase** — the rate-limiting enzyme in hepatic cholesterol biosynthesis. By depleting intracellular cholesterol, atorvastatin triggers compensatory upregulation of LDL receptor (LDLR) expression on hepatocyte surfaces, dramatically increasing the clearance of circulating LDL-C particles from the bloodstream. Its long half-life (~20–30 hours) and active metabolites provide sustained HMG-CoA reductase inhibition throughout the day.

Familial hypercholesterolemia is caused by loss-of-function mutations in the *LDLR* gene, apolipoprotein B (*APOB*), or gain-of-function mutations in *PCSK9*, all of which impair LDL-C clearance and result in lifelong LDL-C elevation averaging 2–3 times normal. Although atorvastatin cannot repair the underlying genetic lesion, it addresses the shared downstream consequence: excessive circulating LDL-C. By maximally upregulating residual LDLR activity (particularly relevant in heterozygous FH where one functional *LDLR* allele remains) and suppressing de novo cholesterol synthesis, atorvastatin partially compensates for the receptor deficiency. In homozygous FH, even partial LDLR upregulation provides meaningful, though incomplete, LDL-C reduction.

The mechanistic connection is therefore direct, and the clinical evidence is exceptionally well-developed: statins, particularly high-intensity agents such as atorvastatin, are the first-line pharmacological therapy in every major international FH guideline, including those from the European Atherosclerosis Society (EAS), the American College of Cardiology/American Heart Association (ACC/AHA), and the American Association of Clinical Endocrinologists (AACE). The high TxGNN prediction score (99.42%) faithfully reflects this established mechanistic and clinical reality.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2,341 | Large-scale RCT assessing long-term safety and tolerability of alirocumab added to atorvastatin-based background therapy in high-CV-risk FH patients; the largest trial in this dataset and highest evidence weight |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Double-blind, placebo-controlled RCT evaluating alirocumab vs. placebo on LDL-C reduction after 24 weeks in heterozygous FH patients on stable atorvastatin background therapy |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Head-to-head RCT comparing alirocumab add-on vs. atorvastatin dose increase vs. rosuvastatin switch in patients with heFH or high CV risk; directly establishes atorvastatin as the clinical benchmark comparator |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Double-blind, placebo-controlled, parallel-group study of alirocumab in heterozygous FH patients not adequately controlled on lipid-modifying therapy (primarily atorvastatin-based) |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Efficacy and safety of ezetimibe 10 mg added to atorvastatin in heFH or CHD patients with primary hypercholesterolemia not controlled on atorvastatin 10 mg monotherapy |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | Three-year prospective study characterizing growth, development, and cholesterol-lowering efficacy of atorvastatin in pediatric patients (age 6–17) with heterozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label extension study of ezetimibe co-administered with atorvastatin or simvastatin in homozygous FH; provides long-term tolerability data |
| [NCT01107743](https://clinicaltrials.gov/study/NCT01107743) | N/A | Completed | 1,291 | Post-marketing drug use investigation of amlodipine/atorvastatin (Caduet) in daily medical practice; provides real-world safety and efficacy data |
| [NCT00145431](https://clinicaltrials.gov/study/NCT00145431) | Phase 3 | Terminated | 41 | Crossover study of torcetrapib/atorvastatin combination in familial dysbetalipoproteinemia; terminated early due to torcetrapib cardiovascular safety signals; atorvastatin arm data partially informative |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | Pharmacokinetics, pharmacodynamics, safety, and tolerability of atorvastatin in children and adolescents with heterozygous FH; supports dosing decisions in pediatric populations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | RCT | Ann Pharmacother | Foundational review of atorvastatin efficacy and safety in primary hypercholesterolemia and mixed dyslipidemias; establishes clinical profile |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Meta-analysis/Cohort | J Am Coll Cardiol | Statin therapy significantly reduces coronary artery disease events and all-cause mortality in heterozygous FH; provides direct outcome evidence |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atherosclerosis Rep | Comprehensive review of novel pharmacological therapies (including statins as backbone) for homozygous FH; contextualizes atorvastatin within the evolving treatment landscape |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocr Pract | AACE/ACE clinical practice guidelines for dyslipidemia management and cardiovascular disease prevention; statins designated first-line agents for FH |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Practice Guidelines | J Am Coll Cardiol | Guidance on improving monitoring and care of FH patients; high-intensity statins including atorvastatin recommended as cornerstone therapy |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic Epidemiology | Pharmacogenomics J | NGS strategy combining FH genetic diagnosis with statin pharmacogenomics; supports individualized atorvastatin dosing in FH based on genotype |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical Study | Echocardiography | Atorvastatin treatment improves myocardial and peripheral blood flow in FH patients without overt coronary atherosclerosis; demonstrates pleiotropic vascular benefits |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Clinical Study | Nutr Metab Cardiovasc Dis | Head-to-head comparison of atorvastatin vs. simvastatin in achieving NCEP LDL-C targets in heterozygous FH; atorvastatin demonstrated superior goal attainment |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical Study | J Clin Lipidol | Three-year assessment of atorvastatin in children/adolescents (age 6–17) with heFH, including growth and safety monitoring; supports long-term pediatric use |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Review | Rev Med Bruxelles | Detailed review of atorvastatin mechanism of action: HMG-CoA reductase inhibition, prolonged half-life of active metabolites, and upregulation of hepatic LDL receptors |

---

## Canada Market Information

No drug identification numbers (DINs) for atorvastatin were returned by the Canada regulatory database at the time of this analysis (data cutoff: 2026-04-05). A table cannot be generated from empty records.

> **Data Note:** This finding likely reflects an incomplete data ingestion rather than true absence from the Canadian market. Health Canada's Drug Product Database should be queried directly to confirm current approval status, active DINs, and approved indications before any regulatory conclusion is drawn.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gaps Requiring Remediation:**
> - **DG001 (Blocking):** Health Canada product monograph warnings and contraindications have not been retrieved. Download and parse the PDF monograph from Health Canada's website before safety screening proceeds.
> - **DG002 (High):** DrugBank MOA and toxicity data have not been retrieved. Query the DrugBank API using `DB01076` to obtain pharmacological action, contraindications, and adverse effect profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for atorvastatin in familial hypercholesterolemia is among the strongest in this drug repurposing analysis, with multiple completed Phase 3 RCTs (including a landmark trial of n=2,341), consistent support across international clinical guidelines, and a directly applicable, well-characterized mechanism of action. An L1 evidence level and 99.42% TxGNN prediction score jointly support advancement.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm current Canada DIN status through Health Canada's Drug Product Database; retrieve all active approvals and their associated indications
- **Safety data remediation (Blocking — DG001):** Download and parse the Health Canada product monograph PDF to extract warnings, contraindications, and precautions before S1 safety screening
- **MOA data remediation (High — DG002):** Query DrugBank API (`DB01076`) to populate mechanism of action, pharmacological class, and toxicity fields
- **Drug-drug interaction review:** Assess interactions with commonly co-prescribed medications in FH patients (fibrates, cyclosporine, macrolide antibiotics, azole antifungals, PCSK9 inhibitors) given atorvastatin's CYP3A4 metabolism
- **Safety monitoring plan:** Define monitoring parameters including ALT/AST (hepatotoxicity), creatine kinase (CK) for myopathy/rhabdomyolysis risk, renal function, and blood glucose (risk of new-onset diabetes)
- **Pediatric dosing guidance:** Incorporate data from NCT00827606 and NCT00739999 for patients under 18 years with heFH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

