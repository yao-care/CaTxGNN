---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: From Hypoparathyroidism to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active hormonal form of vitamin D, clinically established as first-line therapy for hypoparathyroidism, vitamin D-dependent rickets, and chronic kidney disease–associated mineral bone disorders.
The TxGNN model's top-ranked prediction maps to an obsolete ontology term ("obsolete vitamin D deficiency," score 99.96%), which reflects calcitriol's intrinsic pharmacological identity rather than a novel repurposing signal; the most clinically actionable new prediction is **Hereditary Hypophosphatemic Rickets** (rank #7, score 99.28%), supported by **7 clinical trials** and **20 publications** with an overall evidence level of **L2**.
Calcitriol is not currently registered in Canada under this dataset (0 DINs), but products such as Rocaltrol® are known to have regulatory history internationally; Health Canada database verification is recommended.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada — no approved indication on file (data gap; established international use for hypoparathyroidism and CKD mineral bone disorder) |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets (best-evidenced prediction, rank #7) |
| TxGNN Prediction Score | 99.28% (rank #7 among all disease predictions) |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory records on file. Based on established pharmacological knowledge, calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active terminal metabolite of vitamin D, produced in the proximal renal tubule via 1α-hydroxylase (CYP27B1). It binds directly to the Vitamin D Receptor (VDR), a nuclear hormone receptor, triggering transcription of genes that upregulate intestinal calcium and phosphate absorption, suppress parathyroid hormone (PTH) secretion, and promote bone mineralization. Critically, calcitriol requires no further metabolic activation — it works even when hepatic or renal hydroxylation steps are impaired, making it uniquely suited to conditions where endogenous vitamin D activation is blocked.

Hereditary Hypophosphatemic Rickets — most commonly X-linked Hypophosphatemia (XLH, caused by *PHEX* gene loss-of-function mutations) — involves a dual biochemical defect: (1) excess FGF23 production drives renal phosphate wasting, causing chronic hypophosphatemia; and (2) FGF23 simultaneously suppresses renal 1α-hydroxylase activity, causing inappropriately low calcitriol synthesis. This creates a direct and mechanistically compelling rationale for exogenous calcitriol supplementation: it bypasses the FGF23-imposed block on calcitriol production, restoring intestinal calcium and phosphate absorption and supporting bone mineralization without requiring the dysfunctional renal enzymatic step.

Calcitriol combined with oral phosphate supplementation has been the conventional standard of care for XLH for over four decades, documented in landmark studies published in the *New England Journal of Medicine* (PMID 6252463) and the *Journal of Clinical Investigation* (PMID 3839245). A dedicated Phase 4 trial (NCT03820518) is evaluating dose optimisation of calcitriol in paediatric XLH, and a separate Early Phase 1 study (NCT03748966) is specifically investigating calcitriol monotherapy in both children and adults. Although newer anti-FGF23 biologics (burosumab) have emerged as an alternative, calcitriol remains clinically relevant — particularly in cost-sensitive settings or as combination therapy — and the TxGNN model's high score reflects this deep mechanistic alignment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Calcitriol monotherapy in XLH** — the only trial using calcitriol as the sole intervention; dose-escalation design evaluating mineral ions, growth, and skeletal mineralisation in children and adults with XLH over 1 year |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | **High-dose vs. low-dose calcitriol + phosphate in paediatric XLH** — establishes weight-based dosing consistency; Phase 4 status indicates prior efficacy and safety basis in this population |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | **ENERGY 3 study: INZ-701 in ENPP1 Deficiency** — calcitriol likely serves as standard-of-care background therapy, reinforcing its role as established comparator in phosphate-wasting rickets |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | **Observational study of FGF23 hypersecretion in hypophosphataemia** (N=260, completed) — provides large-scale pathophysiological context: FGF23 inhibits calcitriol synthesis, validating the mechanistic basis for calcitriol supplementation |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and Sclerostin in kidney stone formers — background evidence for the phosphate–calcitriol–FGF23 regulatory axis |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | ³¹P-spectroscopy measurement of ATP in phosphate diabetes (XLH) — diagnostic biomarker study; provides insight into metabolic burden of the disease |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Cinacalcet for familial hypophosphatemic rickets — withdrawn before any enrollment; no data available; confirms calcitriol + phosphate as the de facto control arm design |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guideline/Review | *Calcified Tissue International* | Current XLH diagnosis and therapy guidelines — confirms calcitriol + phosphate as long-standing standard of care; discusses positioning relative to burosumab |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Comprehensive Review | *The Lancet* | Authoritative review of X-linked hypophosphataemia — FGF23-driven suppression of calcitriol synthesis established as core pathophysiology; calcitriol supplementation rationale validated |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | *Hormone Research in Paediatrics* | Historical and clinical overview of rickets and vitamin D therapy, including calcitriol's role in hereditary forms of hypophosphataemic rickets |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | *Journal of Clinical Investigation* | **Foundational study**: high-dose calcitriol (68 ng/kg/day) heals both rachitic bone lesions AND coexistent osteomalacia in XLH — demonstrates superiority over conventional vitamin D doses |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | *New England Journal of Medicine* | **Landmark RCT**: calcitriol + phosphate vs. ergocalciferol + phosphate in vitamin D-resistant rickets — calcitriol markedly superior for bone healing and intestinal phosphate absorption |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Multicentre Cohort | *Pediatric Endocrinology Reviews* | Growth outcomes before and after early calcitriol + phosphate therapy in 127 XLH patients across 49 centres — largest real-world dataset for paediatric XLH treatment |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Review | *Journal of Bone and Mineral Research* | Hypophosphataemic rickets and short stature — clinical workup and management algorithm featuring calcitriol as primary active vitamin D supplementation |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort Study | *Journal of Endocrinological Investigation* | Retrospective cohort study of height and body proportions from birth to adulthood in hereditary hypophosphataemic rickets — documents treatment-related growth outcomes |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Observational Study | *Calcified Tissue International* | Bone mineral density measured at baseline and 6-month intervals in 17 children with familial hypophosphataemia receiving calcitriol + phosphate — documents skeletal response to therapy |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | *Nutrients* | Comprehensive review of rickets subtypes and vitamin D analogue treatments — calcitriol and alfacalcidol positioned as key active metabolites for hereditary hypophosphataemic forms |

---

## Canada Market Information

Calcitriol currently has **no registered products (DINs) in Canada** according to this dataset.

> **Important note:** This absence of DINs likely reflects a data gap in the current regulatory dataset rather than true non-availability. Calcitriol-containing products (e.g., Rocaltrol® 0.25 mcg and 0.5 mcg capsules; Roche) have established international regulatory histories. Health Canada's Drug Product Database (DPD) should be queried directly to confirm current Canadian registration status and any associated approved indications before concluding the drug is unavailable in this market.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is available in the current Evidence Pack for Canada-specific labelling.

> Please refer to the package insert for full safety information. Based on well-established pharmacological properties, the following monitoring considerations are clinically critical for calcitriol use in hereditary hypophosphatemic rickets:
>
> - **Hypercalcaemia and hypercalciuria**: Calcitriol's potent stimulation of intestinal calcium absorption is the primary dose-limiting toxicity; urinary calcium-to-creatinine ratio should be monitored regularly
> - **Nephrocalcinosis**: A well-documented complication of calcitriol overtreatment in XLH patients — renal ultrasound surveillance is standard practice in treated children
> - **Special population caution (Dahlberg-Borer-Newcomer syndrome, rank #6)**: In conditions already associated with hypercalciuria and nephrocalcinosis (CLDN16/CLDN19 mutations), calcitriol supplementation carries heightened renal risk and requires a separate S1 safety assessment before proceeding

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol has over four decades of documented clinical use as standard-of-care therapy for X-linked Hypophosphatemia and related hereditary hypophosphataemic rickets, supported by landmark *NEJM* and *JCI* publications, a Lancet comprehensive review, and active Phase 1 and Phase 4 clinical trials that specifically test calcitriol dosing regimens — making this one of the most evidence-supported repurposing predictions in this dataset despite the absence of a Canadian regulatory record.

**To proceed, the following is needed:**

- **Regulatory status verification**: Query Health Canada's Drug Product Database directly to confirm whether calcitriol products hold active DINs and to retrieve Canadian-approved labelling (resolves the Blocking data gap DG001)
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB00136) to complete the mechanistic analysis (resolves High-severity gap DG002)
- **Safety screening (S1)**: Obtain the Canadian package insert to perform formal S1 safety screening — particularly critical given calcitriol's narrow therapeutic window and the hypercalciuria/nephrocalcinosis risk in XLH patients
- **Dose optimisation data**: Await peer-reviewed results from NCT03820518 (Phase 4 high- vs. low-dose comparison) and NCT03748966 (calcitriol monotherapy in XLH, completion estimated May 2026)
- **Competitive positioning analysis**: Clarify the clinical role of calcitriol relative to burosumab (Crysvita®) for XLH in the Canadian health technology assessment context — calcitriol's cost advantage may be a compelling argument for resource-limited settings or combination regimens
- **Paediatric vs. adult dosing plan**: Establish weight-based dosing protocols based on NCT03820518 outcomes, given current lack of regulatory consistency noted in the trial background

---

> **⚠️ Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

