---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 6
---

# Adalimumab
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

---

## One-Sentence Summary

Adalimumab (Humira®) is a fully human anti-TNF-α monoclonal antibody, globally approved for rheumatoid arthritis and multiple other inflammatory diseases, though not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
with **3 indirectly relevant clinical trials** and **20 publications** — including 1 systematic review specifically addressing biological therapy in rheumatoid vasculitis — currently supporting this direction, though no direct head-to-head trials exist.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Taiwan; internationally approved for rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis, Crohn's disease, and others |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known published information, adalimumab is a fully human IgG1 monoclonal antibody that binds with high affinity to both soluble and membrane-bound TNF-α, blocking its interaction with TNFR1 and TNFR2. This suppresses downstream pro-inflammatory cascades including NF-κB activation, matrix metalloproteinase secretion, and RANKL expression — mechanisms well-validated in the treatment of rheumatoid arthritis and related immune-mediated inflammatory diseases.

Rheumatoid vasculitis (RV) is a severe extra-articular complication of long-standing RA, primarily affecting small-to-medium calibre vessels. Its core pathology involves CD4+ T cell and macrophage infiltration of vascular walls, with locally elevated TNF-α driving endothelial damage and vascular necrosis. This immunopathological profile directly mirrors the TNF-α-dominated environment that adalimumab is designed to suppress, providing a strong mechanistic rationale for investigating its use in RV. Published case reports have documented digital vasculitis responding well to adalimumab (PMID 25133007), and the 2021 systematic review by de Cerqueira et al. confirmed that biological agents, including TNF-α inhibitors, are increasingly incorporated into RV management algorithms.

However, a critical complication exists: adalimumab itself has been reported to paradoxically *induce* vasculitis-like events (PMID 28719435), and the BSRBR-RA registry study documented lupus-like and vasculitis-like events among TNFi-treated RA patients (PMID 28123776). One case further showed that severe systemic RV refractory to anti-TNF therapy required switching to tocilizumab (anti-IL-6) for resolution (PMID 21385558), suggesting that a subset of RV may be TNF-independent. A careful patient-level benefit-risk evaluation is therefore essential before any clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large epidemiological study examining the risk of developing new immune-mediated inflammatory diseases (IMID) in patients exposed to biologics and immunosuppressants; can provide indirect estimates of TNF inhibitor exposure and vasculitis incidence rates across IMID populations |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multi-national observational study of RA patients receiving tocilizumab after inadequate response to non-biological DMARDs or a prior biologic; provides indirect safety and clinical background for RA patients on biological therapy |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study describing bDMARD treatment patterns and RA patient demographics in China; characterises the RA biologic-treated population relevant to vasculitis risk profiling |

> **Note:** No clinical trials directly evaluating adalimumab as a treatment for rheumatoid vasculitis were identified. The trials listed above provide indirect contextual evidence only. Two additional retrieved trials (NCT05111743 on wet AMD and NCT07138898 on shoulder arthroplasty) were confirmed retrieval mismatches and excluded from evidence assessment.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-based systematic review of all biological drugs used in RV treatment; confirms biological agents including TNF-α inhibitors are now part of the therapeutic armamentarium for this high-morbidity RA complication |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort Study | RMD Open | BSRBR-RA registry; compared risk of lupus-like and vasculitis-like events in TNFi-treated RA patients versus non-biological DMARD users — critical safety context for adalimumab in a population at risk for RV |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 42-year-old female RA patient with necrotising digital ulcers responded well to adalimumab; direct case-level evidence of adalimumab efficacy in digital vasculitis as an RV manifestation |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis emerged 8 months after adalimumab dose reduction in a patient with established RV; highlights adalimumab's potential role in maintaining RV remission and risks of discontinuation |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | Comprehensive overview of RA-associated episcleritis and scleritis (a vascular manifestation of RA); RA accounts for 8–15% of scleritis cases; discusses biologic treatment options including anti-TNF agents |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | Am J Dermatopathology | First documented case of leukocytoclastic vasculitis with cutaneous perivascular hemophagocytosis paradoxically *induced* by adalimumab in RA; underscores the bidirectional risk — adalimumab can both treat and trigger vasculitis |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | MPO-ANCA-associated nephritis (pauci-immune pattern) occurring during concurrent abatacept and adalimumab therapy for RA; subsequently controlled with tocilizumab — illustrates renal vasculitic complications on anti-TNF therapy |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clinical & Experimental Rheumatology | Multi-drug-refractory systemic RV unresponsive to conventional immunosuppressants and anti-TNF agents; successfully treated with tocilizumab (anti-IL-6), suggesting that a subset of RV is TNF-independent and requires alternative biological targeting |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort Study | Annals of the Rheumatic Diseases | Investigated serial ANA testing as a predictor of bDMARD-induced ANA/dsDNA production in RA; relevant to pre-treatment screening and monitoring when adalimumab is considered in RV-risk patients |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-analysis | Int J Molecular Sciences | Network meta-analysis of 36 RCTs comparing five approved TNF inhibitors (including adalimumab) on joint destruction in RA; establishes class-level efficacy equivalence and supports adalimumab's position within the TNFi class |

---

## Taiwan Market Information

Adalimumab is not currently approved or marketed in Taiwan. No product licenses are on record in the Taiwan regulatory database.

> For global regulatory reference: Adalimumab (Humira®) holds marketing authorisations in the United States (FDA), European Union (EMA), Japan (PMDA), and numerous other jurisdictions for rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, non-radiographic axial spondyloarthritis, Crohn's disease, ulcerative colitis, plaque psoriasis, polyarticular juvenile idiopathic arthritis, and hidradenitis suppurativa, among others. Multiple biosimilars are now also approved globally.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Based on published literature, the following safety signals are relevant to rheumatoid vasculitis candidacy assessment:
> - **Serious infections:** Risk of tuberculosis reactivation and opportunistic infections with TNF-α blockade; TB screening mandatory before initiation
> - **Paradoxical vasculitis induction:** Documented cases of adalimumab-induced leukocytoclastic vasculitis and ANCA-associated nephritis (see PMID 28719435, 36418100); patients with pre-existing RV require heightened monitoring
> - **Drug-induced lupus and autoantibody formation:** ANA, anti-dsDNA, and antiphospholipid antibodies may emerge during therapy (PMID 23559388, 24854356)
> - **Immunogenicity:** Anti-drug antibody (ADA) formation can reduce drug levels and efficacy, particularly in monotherapy settings; relevant to dose optimisation in RV

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Although TNF-α pathway inhibition by adalimumab is biologically plausible for rheumatoid vasculitis given the TNF-α-driven vascular inflammation in RV, direct clinical trial evidence is entirely absent. Critically, adalimumab has a documented bidirectional relationship with vasculitis — capable of both treating and paradoxically inducing the condition — making the risk-benefit profile complex and unsuitable for clinical deployment without prospective validation.

**To proceed, the following is needed:**
- Obtain full TFDA package insert (仿單) to document approved warnings, contraindications, and drug interaction data (currently a blocking data gap)
- Retrieve detailed mechanism of action data from DrugBank API to support mechanistic linkage analysis
- Identify or initiate a prospective observational study or case series specifically in confirmed rheumatoid vasculitis patients receiving adalimumab with pre-specified vasculitis outcome measures
- Develop a patient stratification framework to distinguish RV patients with TNF-α-dominant pathology (likely to benefit) from those with TNF-independent or paradoxical vasculitis risk (likely to be harmed)
- Assess the role of combination therapy (adalimumab + immunosuppressant) versus monotherapy, informed by the immunogenicity data from COMARIS-type studies
- Engage with rheumatology KOLs in Taiwan for clinical expert validation of the mechanistic hypothesis before any regulatory or clinical development steps are initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

