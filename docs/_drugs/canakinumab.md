---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Cryopyrin-Associated Periodic Syndrome to Familial Mediterranean Fever (Autosomal Dominant)

## One-Sentence Summary

Canakinumab (Ilaris) is a fully human anti-IL-1β monoclonal antibody originally approved for Cryopyrin-Associated Periodic Syndromes (CAPS), encompassing familial cold autoinflammatory syndrome, Muckle-Wells syndrome, and neonatal-onset multisystem inflammatory disease.
The TxGNN model predicts it may be effective for **Familial Mediterranean Fever (Autosomal Dominant)**, supported by **7 clinical trials** and **20 publications** — a prediction further validated by existing FDA and EMA approval for colchicine-resistant FMF.
This is the highest-evidence actionable candidate in this analysis (L1), with all other top-ranked predictions (hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis, monosomy X, liver angiosarcoma) assessed as mechanistically unsupported and recommended for Hold pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cryopyrin-Associated Periodic Syndrome (CAPS) — FCAS, Muckle-Wells Syndrome, NOMID |
| Predicted New Indication | Familial Mediterranean Fever, Autosomal Dominant |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Canakinumab is a fully human IgG1/κ monoclonal antibody that selectively neutralizes IL-1β, preventing it from binding to its receptor and blocking the downstream NF-κB–driven inflammatory cascade. The drug was first clinically validated in CAPS, where gain-of-function mutations in the *NLRP3* gene cause constitutive inflammasome assembly, excess caspase-1 activation, and IL-1β hypersecretion — resulting in systemic fever, urticarial rash, sensorineural hearing loss, and amyloidosis.

Familial Mediterranean Fever (FMF) converges on the same terminal effector through a distinct genetic route. FMF is caused by mutations in the *MEFV* gene encoding pyrin, a natural repressor of the pyrin inflammasome. Loss-of-function or hypomorphic pyrin leads to unrestrained IL-1β release, driving recurrent self-limited attacks of high fever, peritonitis, pleuritis, and arthritis. If inadequately treated, chronic IL-1β–driven inflammation leads to secondary AA amyloidosis with end-stage renal disease — the most feared long-term complication. The autosomal dominant form (AD-FMF), arising from heterozygous *MEFV* variants with variable penetrance, follows the same IL-1β–centered pathogenic axis.

Because both CAPS and FMF culminate in inflammasome-driven IL-1β excess, Canakinumab's mechanism transfers directly. This is not merely a model-predicted extrapolation — the FDA approved Canakinumab for colchicine-resistant FMF, HIDS/MKD, and TRAPS in 2016 (following the landmark CLUSTER Phase 3 programme), and EMA approval followed. The TxGNN score of 99.41% is consistent with this established mechanistic and clinical evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Completed | 35 | Pivotal three-part RCT (open-label run-in → randomized double-blind placebo-controlled withdrawal → open-label extension) in Muckle-Wells Syndrome. Demonstrated that Canakinumab significantly maintained disease remission vs. placebo; core regulatory submission study. |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Largest long-term open-label safety and efficacy study (≥6 months, some patients >12 months) across FCAS, MWS, and NOMID. Provided the primary long-term safety dataset supporting initial CAPS approval. |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Completed | 17 | One-year multicenter study in CAPS patients aged ≤4 years; assessed safety, efficacy, tolerability, and critically, the interaction with childhood immunization schedules. |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Open-label extension for patients completing NCT01302860; evaluated long-term safety, sustained efficacy, and normalization of acute-phase reactants (CRP, SAA) over time. |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | Japanese-population CAPS study (FCAS, MWS, NOMID) with 24-week treatment and extension until Japanese market approval; established efficacy data for East Asian patients. |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Completed | 20 | Open-label 4-month treatment + 6-month follow-up in active TRAPS patients; safety and proof-of-concept for IL-1β inhibition in additional periodic fever syndromes, forming the basis for Phase 3 CLUSTER design. |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Recruiting | 25 | REASSURE: Post-marketing non-interventional real-world study evaluating safety and effectiveness of Ilaris in CAPS, colchicine-resistant FMF (crFMF), TRAPS, HIDS/MKD, and sJIA in clinical practice settings (2025–2028). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Phase 3 Trial Summary | N Engl J Med | CLUSTER programme results: Canakinumab significantly reduced attack frequency vs. placebo in FMF, HIDS/MKD, and TRAPS; remission rates were substantially higher with Canakinumab across all three syndromes. Primary evidence for FDA 2016 indication expansion. |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Front Immunol | Comprehensive systematic review of all approved IL-1 blockers (anakinra, canakinumab, rilonacept) across autoinflammatory and immune-mediated disorders; confirms canakinumab's superior half-life advantage and consistent efficacy across CAPS, FMF, TRAPS, HIDS, and sJIA. |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic Review + Meta-analysis | Rheumatology (Oxford) | Meta-analysis of anti-IL-1 treatment (including canakinumab) efficacy and safety in FMF; provides quantitative pooled estimates for attack reduction and acute-phase reactant normalization in colchicine-resistant or colchicine-intolerant patients. |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Comparative Cohort | Int J Rheumatic Dis | Head-to-head comparison of canakinumab with vs. without concomitant colchicine in FMF patients; evaluated attack characteristics, CRP/SAA levels, and renal outcomes — informing combination therapy strategy. |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Clinical Outcomes Review | Clin Exp Rheumatol | Detailed review of IL-1 inhibition in FMF: indications for switching from colchicine, clinical response benchmarks, dosing considerations, and long-term outcomes including amyloidosis prevention. |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Comprehensive Review | Turk J Med Sci | Contemporary FMF review from pathogenesis to treatment; covers pyrin inflammasome mechanisms, MEFV mutation classification, diagnostic updates, and the evolving role of anti-IL-1 biologics. |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohort Study | Rheumatology (Oxford) | First dedicated study of canakinumab withdrawal feasibility in pediatric colchicine-resistant FMF; established a structured tapering and discontinuation protocol — important for real-world treatment management. |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Expert Review | Expert Rev Clin Immunol | Focused expert review of canakinumab in FMF; covers pharmacology, colchicine-resistant patient profiles, clinical trial outcomes, and position in the treatment algorithm. |
| [31365342](https://pubmed.ncbi.nlm.nih.gov/31365342/) | 2019 | Clinical Cohort | Eur J Rheumatol | Real-world data on canakinumab in colchicine-unresponsive FMF patients; reported clinical response rates and normalization of inflammatory markers in a Turkish cohort. |
| [34684086](https://pubmed.ncbi.nlm.nih.gov/34684086/) | 2021 | Review | Medicina (Kaunas) | Amyloidosis and glomerular disease in FMF; underscores the critical importance of sustained IL-1β suppression (including with canakinumab) in preventing secondary AA amyloidosis and end-stage renal failure. |

---

## Canada Market Information

Canakinumab currently has **no approved Drug Identification Numbers (DINs) in Canada** and is not marketed for any indication.

> **Context:** While Health Canada approval is absent, the US FDA approved Canakinumab (Ilaris, Novartis) in June 2009 for CAPS and expanded the label in 2016 to include colchicine-resistant FMF, HIDS/MKD, and TRAPS. EMA approval for the same spectrum of autoinflammatory diseases is also in place. Canadian patients with confirmed CAPS or colchicine-resistant FMF who require Canakinumab currently depend on Health Canada's Special Access Program (SAP).

---

## Safety Considerations

Full prescribing information from a Canadian product monograph is unavailable for this analysis. Based on published Phase 3 clinical trial data and the FDA prescribing information, the following safety signals are relevant:

- **Serious and Opportunistic Infections**: IL-1β inhibition impairs host defense against bacterial infections, particularly encapsulated organisms. Active tuberculosis, untreated latent TB, serious active infections, and immunocompromised states are contraindications or require mandatory screening before initiation.
- **Neutropenia**: Transient neutropenia has been reported; complete blood count (CBC with differential) monitoring is recommended before and periodically during treatment.
- **Live Vaccines**: Contraindicated during canakinumab treatment. Inactivated vaccines may be given but immunological response may be reduced. The NCT01302860 trial specifically studied childhood vaccination interactions in young CAPS patients.
- **Hypersensitivity**: Anaphylaxis and serious hypersensitivity reactions have been reported; appropriate medical support must be available at time of injection.
- **Lipid and Liver Parameters**: Transient elevations in lipids and liver enzymes have been observed; monitoring is warranted.
- **Macrophage Activation Syndrome (MAS)**: In patients with sJIA, MAS has occurred; clinicians should be vigilant for features of MAS/HLH.

Please refer to the full product monograph / package insert for comprehensive prescribing information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Canakinumab has a fully characterized IL-1β–targeting mechanism that directly addresses the core pathogenic driver of FMF, and has been validated through multiple completed Phase 3 RCTs (CLUSTER programme, published in the *New England Journal of Medicine*) with subsequent FDA and EMA approval for colchicine-resistant FMF. The TxGNN score of 99.41% is consistent with this level of established evidence. The primary gap is the absence of a Canadian market authorization, not a lack of clinical proof.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Determine whether Novartis Canada has submitted or plans to submit a New Drug Submission (NDS) to Health Canada for CAPS and FMF indications; if not, evaluate a third-party or compassionate access pathway.
- **SAP access mapping**: Confirm current Health Canada Special Access Program (SAP) utilization in Canada to understand the actual patient population already receiving canakinumab and any real-world Canadian safety signal.
- **Safety data gap closure (DG001)**: Obtain the Canadian labelling equivalent (US FDA prescribing information / EMA SmPC) to complete the formal safety assessment required for S1 evaluation.
- **MOA documentation (DG002)**: Retrieve the DrugBank MOA entry for DB06168 to formally document the IL-1β neutralization mechanism in the Evidence Pack.
- **Patient population definition**: Specify whether the target indication is pediatric vs. adult FMF, colchicine-resistant FMF specifically, or the broader autoinflammatory syndrome spectrum — as this determines the applicable Phase 3 dataset and labelling strategy.
- **Health economics assessment**: Given the high cost of biologic therapy and the rarity of colchicine-resistant FMF in Canada, a budget impact and cost-effectiveness analysis relative to anakinra (an alternative IL-1 blocker) would support payer engagement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

