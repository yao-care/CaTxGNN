---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Abatacept is a selective T-cell co-stimulation modulator (CTLA-4-Ig fusion protein) established globally for the treatment of moderate-to-severe rheumatoid arthritis (RA), though it has not received regulatory approval in Canada.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis (RV)**, with **1 clinical trial** and **20 publications** currently supporting this direction.
However, the evidence base consists primarily of case reports and mechanistic reviews, placing this prediction at exploratory level — a research question rather than an actionable clinical recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (approved globally; no Canada DIN on record) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Abatacept (brand name: Orencia) is a recombinant fusion protein composed of the extracellular domain of CTLA-4 linked to the Fc region of human IgG1. It acts by competitively binding CD80 and CD86 on antigen-presenting cells, thereby blocking the CD28 co-stimulatory signal that naïve T cells require for full activation. Without this second signal, autoreactive T cells fail to expand efficiently — directly suppressing the adaptive immune cascade that drives chronic inflammatory joint disease. Detailed pharmacological MOA data from DrugBank was not available for this report; the above summary draws from published literature characterising the drug class.

Rheumatoid vasculitis is a severe extra-articular complication of longstanding, poorly controlled RA, estimated to affect 1–5% of RA patients. Its pathogenesis is driven by T-cell-mediated vascular wall inflammation, immune complex deposition in vessel walls, and endothelial injury — all processes dependent on sustained T-cell activation. Because these mechanisms share the same upstream CD28 co-stimulatory dependency as RA joint inflammation, abatacept's mode of action is theoretically well-positioned to intercept RV. Several published case reports (PMID 22124545, PMID 29930884) document rapid clinical resolution of RV after abatacept initiation, supporting this mechanistic hypothesis.

A critical caveat must be flagged: one case report (PMID 27052429) describes new-onset RV developing *during* abatacept therapy, with subsequent improvement only after switching to rituximab. This paradoxical finding — whether reflecting true drug-induced vasculitis, inadequate disease control, or disease progression independent of abatacept — significantly tempers enthusiasm. Until prospective data clarify this signal, RV remains a biologically plausible but clinically unconfirmed candidate for abatacept repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management (including abatacept) in rheumatology patients undergoing elective shoulder replacement; evaluates flare rates and wound complications — not a direct RV efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | Case Series/Review | Cureus | Abatacept used therapeutically for RV in a patient with RA and common variable immunodeficiency where rituximab was contraindicated; cutaneous purpura resolved — supports abatacept as an alternative when standard therapy is not feasible |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | Case Report | Modern Rheumatology | A 38-year-old woman with RV refractory to MTX, TNF inhibitors, steroids, plasmapheresis, and IL-6 inhibitor achieved rapid clinical improvement and near-normalization of inflammatory markers after abatacept — strongest positive case evidence |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | Case Report | Joint Bone Spine | New-onset RV developed during abatacept therapy; lesions improved only after switching to rituximab — key cautionary evidence suggesting possible paradoxical effect or mechanism-drug mismatch in some patients |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | Case Report/Review | Ophthalmic Plastic & Reconstructive Surgery | RA patient on abatacept developed bilateral orbital vasculitis with eosinophilic infiltrate on biopsy; progressed despite cyclophosphamide — highlights orbital RV as a distinct and treatment-refractory phenotype |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated pauci-immune nephritis emerged during abatacept + adalimumab therapy for RA, controlled with tocilizumab — illustrates vasculitic complications occurring in the context of abatacept use |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | Comprehensive review of RA-associated episcleritis and scleritis management, including biologics; contextually relevant to ocular manifestations of RV |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort Study | Annals of the Rheumatic Diseases | Serial ANA testing utility in predicting bDMARD-associated lupus and vasculitis in RA patients; provides epidemiological context for vasculitic risk under biologic therapy |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | Review | Best Practice & Research. Clinical Rheumatology | CNS involvement in RA including cerebral vasculitis; discusses biologics including abatacept in this context — relevant to neurological RV manifestations |
| [24493331](https://pubmed.ncbi.nlm.nih.gov/24493331/) | 2015 | Case Series | Clinical Rheumatology | Off-label use of abatacept in myositis reviewed alongside other biologics; illustrates the breadth of T-cell-mediated inflammatory conditions where abatacept has been explored |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Update on biologic therapies across autoimmune diseases; provides background on abatacept's role relative to other bDMARDs in managing RA and systemic autoimmune conditions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for abatacept in rheumatoid vasculitis is coherent — RV is a T-cell-driven extra-articular RA complication, and CD28 co-stimulation blockade directly targets this pathway. However, the evidence base consists entirely of individual case reports (L4), and a documented case of paradoxical RV onset during abatacept therapy creates unresolved safety ambiguity. Without at least a prospective observational study with defined RV entry criteria and standardised outcome measures, regulatory or institutional endorsement of this use cannot be justified.

**To proceed, the following is needed:**

- **Prospective observational registry:** Systematically enrol RA patients with confirmed RV receiving abatacept and document clinical outcomes using validated tools such as the Birmingham Vasculitis Activity Score (BVAS)
- **Mechanistic clarification:** Resolve the paradoxical RV-during-abatacept signal — determine whether it reflects an inadequate CD4+ Th17/Treg imbalance that CTLA-4-Ig cannot correct, or a subset-specific immune escape
- **MOA data supplement:** Retrieve complete DrugBank pharmacological profile (currently unavailable) to finalize mechanistic link analysis
- **Safety profiling:** Obtain Canadian (Health Canada) package insert warnings and contraindications to complete the S1 safety pre-screening currently blocked by missing regulatory data
- **Patient selection criteria:** Identify candidate biomarkers (e.g., ACPA positivity, CD4+ T-cell subset ratios) that predict which RV patients are most likely to respond to T-cell co-stimulation blockade versus B-cell depletion (rituximab)
- **Comparator strategy:** Design a comparative cohort study contrasting abatacept versus rituximab (current standard of care for RV) to generate the first head-to-head evidence

> **Research Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

