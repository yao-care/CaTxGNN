---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 701
evidence_level: L5
indication_count: 5
---

# Sacubitril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

> **Note on TxGNN ranking:** TxGNN's top-ranked candidate for sacubitril is *"brain small vessel disease 1 with or without ocular anomalies"* (score 99.58%). However, the evidence pack itself flags this — and the next three ranked candidates (autosomal dominant familial hematuria syndrome, rheumatoid arthritis, hemoglobinopathy) — as **false positives**: the 19 associated PubMed articles are about unrelated congenital eye/genetic disorders matched only by keyword overlap, with no mechanistic plausibility. All four were scored **L5 / Hold**. This report therefore focuses on **rank 3 — diabetic nephropathy** — the only candidate with real clinical trial and literature support.

## One-Sentence Summary

Sacubitril, combined with valsartan (ARNI), is used to treat heart failure with reduced ejection fraction (HFrEF).
The TxGNN model's evidentially-supported prediction is **Diabetic Nephropathy**,
backed by **2 clinical trials** (one Phase 4 RCT, one real-world study) and **17 publications**, though no completed RCT has yet reported results.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure with reduced ejection fraction (based on trial evidence; no Canada product license on file) |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocked as a High-severity data gap). Based on known information, sacubitril is the prodrug component of sacubitril/valsartan (ARNI, LCZ696); its active metabolite LBQ657 inhibits neprilysin, raising levels of natriuretic peptides (ANP/BNP/CNP), producing natriuretic, vasodilatory, anti-fibrotic, and antioxidant effects. This combination's efficacy in HFrEF is well established.

Heart failure and diabetic nephropathy share overlapping hemodynamic and neurohormonal pathophysiology — both involve renin-angiotensin system activation, fluid overload, and inflammatory/fibrotic injury. Multiple animal studies (rat and db/db mouse models) in this evidence pack show sacubitril/valsartan reduces proteinuria and suppresses NF-κB-mediated glomerular inflammation, and a secondary analysis of the PARADIGM-HF trial found renoprotective signals in diabetic HF patients — supporting the mechanistic plausibility of this prediction, though direct confirmatory clinical evidence in diabetic nephropathy (without concurrent heart failure) is still pending.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not Yet Recruiting | 297 | Randomized, multicenter trial (Hyper-Save Study) comparing sacubitril/valsartan vs. valsartan in mild-moderate hypertension with type 2 diabetic nephropathy; 12-week treatment, 2:1 randomization |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Retrospective real-world EMR study of sacubitril/valsartan prescribing patterns in HFrEF patients in India (diabetic subgroup overlap possible, not primary endpoint) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT (PARADIGM-HF) | Lancet Diabetes Endocrinol | Neprilysin inhibition associated with favorable effects on renal function decline in type 2 diabetics with chronic HF |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical (randomized comparison, n=112) | Int Immunopharmacol | Sacubitril/valsartan + nifedipine improved renal function vs. valsartan + nifedipine in DN patients with hypertension |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical (imaging biomarker) | Diabetes Metab Syndr Obes | BOLD-MRI used to evaluate renal protective effects of sacubitril/valsartan in type 2 diabetics |
| [40635044](https://pubmed.ncbi.nlm.nih.gov/40635044/) | 2025 | In vitro (human podocytes) | Eur J Med Res | LCZ696 reduces glucose-induced oxidative stress in human podocytes via Nrf2/HO-1 pathway |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preclinical (rat model) | Diabetes Metab Syndr Obes | Sacubitril/valsartan slows early diabetic nephropathy progression via NLRP3 inflammasome inhibition |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | Preclinical (mouse model) | Front Endocrinol | Sacubitril/valsartan improves diabetic kidney disease and modulates gut microbiota in mice |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preclinical (rat model) | PeerJ | LCZ696 mitigates diabetic nephropathy via reduced oxidative stress, NF-κB inflammation, and glomerulosclerosis |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Preclinical (db/db and KKAy mice) | Am J Physiol Renal Physiol | Sacubitril/valsartan shows differential renoprotective effects vs. valsartan alone in diabetic mouse models |
| [30909895](https://pubmed.ncbi.nlm.nih.gov/30909895/) | 2019 | Preclinical (Zucker Obese rat) | Cardiovasc Diabetol | Sacubitril + valsartan attenuates glomerular and tubular injury more effectively than valsartan alone |
| [37202215](https://pubmed.ncbi.nlm.nih.gov/37202215/) | 2023 | Preclinical (mouse model) | Nephrol Dial Transplant | Sacubitril/valsartan improves renal tubulointerstitial injury via increased renal plasma flow in T2D with aldosterone excess |

## Canada Market Information

Sacubitril is not currently marketed in Canada — no Drug Identification Numbers (DINs) are on file (0 licenses registered).

## Safety Considerations

Please refer to the package insert for safety information. (Note: key warnings, contraindications, and drug interaction data are currently unavailable — this is flagged as a **Blocking** data gap that must be resolved before any safety evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only evidence-supported candidate (diabetic nephropathy) has mechanistic plausibility and consistent preclinical signal, but no completed RCT has yet confirmed efficacy — the sole purpose-designed Phase 4 trial (NCT06501651) has not started recruiting. Combined with the drug's unmarketed status in Canada and a Blocking safety data gap, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA/Health Canada-equivalent product monograph (key warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action via DrugBank query
- Results from NCT06501651 once recruitment completes
- Clarification of Canada regulatory/market pathway, given 0 current DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

