---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Hypertriglyceridemia/Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a selective PPARα agonist in the fibrate class, established in clinical practice for the treatment of hypertriglyceridemia and mixed dyslipidemia.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **1 clinical trial** and **11 publications** currently identified in support of this direction — though the available evidence does not directly evaluate fenofibrate as an intervention for HoFH, and mechanistic alignment is limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Canadian regulatory registry |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, fenofibrate is a selective PPARα (peroxisome proliferator-activated receptor alpha) agonist. It acts on the triglyceride/HDL metabolic axis through multiple complementary mechanisms: (1) upregulating lipoprotein lipase (LPL) to accelerate clearance of VLDL, IDL, and chylomicrons; (2) downregulating apoC-III to relieve endogenous LPL inhibition, reducing triglycerides; (3) upregulating apoA-I/apoA-II to increase HDL synthesis via reverse cholesterol transport; and (4) suppressing hepatic VLDL secretion. These effects are well-established across Fredrickson type IIb, III, IV, and V hyperlipoproteinemia.

Homozygous familial hypercholesterolemia (HoFH) is a distinct and severe condition caused by near-complete loss of LDL receptor (LDLR) function (typically <2% of normal activity), resulting in LDL-C levels that routinely exceed 13 mmol/L. The standard of care relies on LDLR-independent clearance pathways (e.g., SR-B1), LDL apheresis, and high-intensity combination pharmacotherapy including statins, ezetimibe, and PCSK9 inhibitors (evolocumab/alirocumab). Fenofibrate's PPARα mechanism does not meaningfully rescue LDLR-mediated LDL clearance, meaning it cannot address the core pathology of HoFH.

The TxGNN model likely captured a pattern from shared lipid metabolism networks between HoFH and fenofibrate's known indications. A narrow mechanistic justification does exist: when HoFH patients present with concurrent severe hypertriglyceridemia (TG >5.6 mmol/L), fenofibrate could serve as an adjunct to reduce pancreatitis risk. One early case report (PMID 6593751, 1984) documented the greatest LDL-C reduction in a single HoFH patient among a type II cohort, suggesting a modest on-target response. However, this constitutes an outlier observation rather than a therapeutic rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab (PCSK9 inhibitor) in children and adolescents aged 8–17 with HoFH on background treatments. Evaluated LDL-C reduction at Weeks 12, 24, and 48. Fenofibrate is not the study intervention; provides context on HoFH trial design and background therapy expectations. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE clinical practice guidelines for dyslipidemia and cardiovascular disease prevention; fenofibrate referenced as a non-statin lipid-lowering option within the broader dyslipidemia treatment framework |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Comprehensive review of traditional and novel non-statin agents; establishes fenofibrate monotherapy's most definitive indication as TG >500 mg/dL to reduce acute pancreatitis risk, with modest cardiovascular benefit |
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | Long-term fenofibrate (300 mg/day, 4–12 months) in 22 type II hyperlipoproteinemia patients; one HoFH patient showed the greatest reduction in total and LDL cholesterol among the cohort (~28–31%), representing the only direct HoFH observation |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Intern Med J | Discusses liver transplantation as treatment for HoFH and the landscape of emerging lipid-lowering therapies; notes that standard drugs including fibrates are insufficient for HoFH core pathology |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic | Pharmacotherapy | Characterizes pharmacokinetic interactions between lomitapide (approved for HoFH) and lipid-lowering therapies including fenofibrate; relevant to combination therapy safety in HoFH management |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann NY Acad Sci | Reviews pharmacologic treatment of dyslipidemic children and adolescents; fenofibrate listed among agents used in pediatric FH with variable success in LDL reduction |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atherosclerosis Rep | Dyslipidemia management in pregnancy; reviews fibrate safety limitations and guideline gaps relevant to special populations |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Discusses LDL-C reduction strategies, residual risk after statin therapy, and the role of PCSK9 inhibitors in severe hypercholesterolemia; positions fibrates as adjuncts rather than primary agents |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Review of ezetimibe as selective cholesterol absorption inhibitor; provides comparative context for combination lipid-lowering strategies used alongside fibrates in complex dyslipidemias |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | Can J Cardiology | Landmark clinical trial evidence for LDL-C lowering in CAD prevention; discusses TG-rich lipoproteins as risk factors and frames the complementary role of fibrate therapy |

---

## Canada Market Information

Fenofibrate has **no active Drug Identification Numbers (DINs)** on record in the Health Canada drug product database for this analysis. No authorization records are available to display.

> **Note:** This may reflect a data gap in the current evidence pack rather than an absence of Canadian marketing history. Fenofibrate products (e.g., TriCor, Lipidil) are known to have been commercially available in Canada under various brand names. Independent verification via the Health Canada Drug Product Database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Canadian product monograph data was not retrieved in this evidence pack. Key safety areas to review include: rhabdomyolysis risk when co-administered with statins, hepatotoxicity monitoring, renal function-based dose adjustments, cholelithiasis risk, and contraindications in pregnancy and severe hepatic/renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN computational score (99.91%), the mechanistic basis for fenofibrate in HoFH is fundamentally weak — the drug's PPARα-mediated TG/HDL effects do not compensate for complete LDLR dysfunction, which is the defining pathology of HoFH. The sole available clinical trial evaluated alirocumab (not fenofibrate), and the 11 literature references consist predominantly of general dyslipidemia reviews and guideline documents with no direct RCT evidence for fenofibrate in HoFH.

**To proceed, the following is needed:**
- Direct clinical evidence of fenofibrate as an intervention in HoFH (a dedicated pilot or observational study in patients with concurrent hypertriglyceridemia)
- Clarification of the intended clinical role: adjunct for TG management in HoFH vs. primary LDL-C lowering
- Health Canada product monograph retrieval for complete safety warnings and contraindications (DG001)
- DrugBank MOA data to formally document mechanistic profile (DG002)
- Evaluation of whether a subpopulation of HoFH patients with TG >5.6 mmol/L may represent a targeted niche where fenofibrate provides incremental benefit alongside standard-of-care LDL-lowering therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

