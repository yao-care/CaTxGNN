---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 5
---

# Golimumab
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

# Golimumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab (Simponi®) is a fully human anti-TNFα monoclonal antibody approved internationally for rheumatoid arthritis (RA), psoriatic arthritis (PsA), and ankylosing spondylitis (AS), but currently not marketed in Canada.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **3 clinical trials** and **6 publications** currently supporting this direction.
The evidence base is predominantly mechanistic and indirect, placing this prediction at Level L4 — sufficient to frame a research question, but not yet ready for clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (international approvals; no Canada DIN on file) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (Mechanistic / indirect evidence) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Golimumab is a fully human IgG1κ monoclonal antibody that selectively neutralizes both soluble and transmembrane TNF-α — a master pro-inflammatory cytokine central to the pathogenesis of many autoimmune and inflammatory diseases. TNF-α activates endothelial cells, upregulates adhesion molecules (ICAM-1, VCAM-1), and drives neutrophil infiltration into vessel walls, all of which are hallmark features of vasculitic pathology. By blocking TNF-α signalling at its source, golimumab theoretically interrupts the inflammatory cascade upstream of vascular injury.

Rheumatoid vasculitis (RV) is a serious extra-articular manifestation of seropositive RA, characterized by immune complex deposition, complement activation, and sustained TNF-α-mediated inflammation of small- and medium-sized vessels. Since golimumab is already a first-line biologic for RA and has documented benefit in reducing extra-articular manifestations (including uveitis) in ankylosing spondylitis, its anti-TNFα mechanism is biologically coherent as an intervention for the vascular inflammatory component of RV. Published case literature (PMID 29075910) explicitly notes that the introduction of anti-TNF biologics as a class has reduced the observed incidence of rheumatoid vasculitis in seropositive patients, lending further biological plausibility to the TxGNN prediction.

However, rheumatoid vasculitis as an independent primary therapeutic endpoint has never been studied in a dedicated golimumab RCT. The available evidence consists of mechanistic inference, observational case reports, and indirect data from broader RA biologic trials. An important safety counterpoint also exists: case reports describe paradoxical new-onset large-vessel vasculitis (Takayasu's arteritis) occurring under anti-TNF therapy (PMID 22999907), underscoring that TNF-α inhibition in vasculitic disease is not uniformly protective and requires careful patient selection.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multi-national observational study of tocilizumab in RA patients with inadequate response to DMARDs or one prior biologic; provides real-world safety and disease control context for biologic therapy in RA, indirectly relevant to the biologic treatment landscape of extra-articular RA |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Evaluates perioperative immunosuppressant holding strategies in rheumatology patients undergoing total shoulder arthroplasty; assesses flare risk and surgical outcomes, not vasculitis directly |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large retrospective observational study evaluating incidence of new-onset immune-mediated inflammatory diseases (IMID) in patients treated with biologics and immunosuppressants; broad scope with limited direct applicability to rheumatoid vasculitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-Analysis | Int J Mol Sci | 36 RCTs compared five TNF inhibitors (including golimumab) vs MTX on radiographic joint destruction in RA; golimumab and biosimilars demonstrated equivalent joint-protective efficacy, supporting class-level anti-TNF efficacy in RA |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Comprehensive review of biologic therapies for autoimmune diseases including anti-TNF agents; discusses mechanism, limitations, and clinical positioning of golimumab in broader inflammatory disease context |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Characterizes end-stage renal disease in RA patients and causes of systemic/extra-articular organ involvement; highlights clinical burden of uncontrolled systemic RA manifestations relevant to vasculitis management |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatology Int | Pyoderma gangrenosum and pyogenic arthritis presenting as severe sepsis in a golimumab-treated RA patient; explicitly notes that anti-TNF biologics have attenuated the incidence of rheumatoid vasculitis in seropositive patients since their introduction |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Series | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel granulomatous vasculitis) arising paradoxically during anti-TNF therapy; important safety signal suggesting anti-TNFα may not uniformly suppress all vasculitic subtypes |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocular Immunol Inflamm | Behçet disease-associated uveitis successfully managed with off-label golimumab after failure of other anti-TNF agents; demonstrates golimumab's anti-TNFα efficacy extends to vascular-adjacent autoimmune manifestations beyond its approved indications |

---

## Canada Market Information

Golimumab has no approved product licenses (DINs) in Canada. No product authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, drug interactions) were not available in this Evidence Pack. Prescribers should consult the current product monograph for golimumab (Simponi® / Simponi Aria®) before any clinical use. Particular attention should be paid to risks of serious infections (including tuberculosis reactivation), malignancies, hepatitis B reactivation, and the paradoxical occurrence of new-onset inflammatory conditions including vasculitis under anti-TNF therapy (see PMID 22999907).

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Rheumatoid vasculitis shares a TNF-α-driven inflammatory pathway with golimumab's core approved indications, and observational data suggest that anti-TNF biologics as a class have reduced RV incidence in clinical practice. However, no dedicated clinical trial exists evaluating golimumab specifically for rheumatoid vasculitis as a primary endpoint, and a paradoxical vasculitis signal under anti-TNF therapy adds complexity. This places the prediction firmly at Level L4 — biologically plausible, but not yet clinically actionable.

**To proceed, the following is needed:**
- **Dedicated clinical evidence**: Design a prospective observational registry or pilot study examining golimumab efficacy in confirmed rheumatoid vasculitis (skin, nerve, or visceral involvement) as the primary endpoint
- **MOA data**: Obtain full DrugBank pharmacology entry for golimumab to formally characterize receptor binding kinetics, half-life, and immunogenicity profile (currently a data gap)
- **Safety profile review**: Download and parse the Health Canada / FDA approved prescribing information to document boxed warnings, contraindications, and clinically significant drug interactions
- **Paradoxical vasculitis assessment**: Systematically review post-marketing pharmacovigilance data for anti-TNF-associated new-onset vasculitis to characterize the benefit-risk profile before proceeding
- **Epidemiologic baseline**: Estimate rheumatoid vasculitis prevalence and current standard-of-care gaps in the target population to determine whether an unmet need justifies a prospective study investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

