---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Plaque Psoriasis to Ulcerative Colitis

## One-Sentence Summary

Guselkumab (Tremfya®) is a fully human anti-IL-23p19 monoclonal antibody, globally established as a first-line biologic for moderate-to-severe plaque psoriasis, but currently without Health Canada authorization.
The TxGNN model's top-scored predictions — drug-induced osteoporosis (#1, 99.84%) and severe nonproliferative diabetic retinopathy (#2, 99.80%) — lack mechanistic support and clinical data (L5, Hold); however, **psoriasis** (rank #3, 99.74%) and **ulcerative colitis** (rank #6, 99.70%) each reach **L1 evidence level**, backed by completed Phase 3 RCTs and recent FDA approvals.
With **40+ clinical trials** and **20 publications** for psoriasis, and **17 clinical trials** and **20 publications** for UC, both represent high-priority repurposing candidates for the Canadian market.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Canada; globally established for moderate-to-severe plaque psoriasis (FDA approved 2017) |
| Primary Predicted New Indication | Psoriasis — TxGNN rank #3, score 99.74% (L1) |
| Secondary Predicted New Indication | Ulcerative Colitis — TxGNN rank #6, score 99.70% (L1) |
| TxGNN Top Score | 99.84% (drug-induced osteoporosis, rank #1 — L5, Hold) |
| Evidence Level | L1 (psoriasis & ulcerative colitis) / L5 (all other predictions) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Proceed with Guardrails** (psoriasis & UC) · **Hold** (all other predictions) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack (Data Gap: DG002). Based on global clinical and scientific literature, guselkumab is a fully human IgG1λ monoclonal antibody that selectively binds to the **p19 subunit of interleukin-23 (IL-23)**, preventing its binding to the IL-23 receptor. This blocks downstream Th17 cell differentiation and the downstream production of IL-17A, IL-17F, and IL-22 — key effectors of chronic immune-mediated inflammation — while leaving IL-12/Th1 immunity (important for infection defence) largely intact.

**For psoriasis**, the IL-23/Th17 axis is the core pathogenic driver. IL-23 secreted by dermal dendritic cells and macrophages expands Th17 populations that produce IL-17, driving keratinocyte hyperproliferation, epidermal thickening, and plaque formation. Guselkumab's selective p19 blockade directly interrupts this loop without broad immunosuppression. The VOYAGE 1 and VOYAGE 2 pivotal Phase 3 trials (vs adalimumab and placebo) established guselkumab as superior to an anti-TNF biologic for sustained skin clearance, and the ECLIPSE trial further confirmed superiority over secukinumab (IL-17A inhibitor) for durable PASI 90 at week 48.

**For ulcerative colitis**, the intestinal lamina propria in active UC shows marked IL-23-driven Th17 expansion. IL-23 promotes secretion of IL-17A, IL-22, and IFN-γ that compromise mucosal barrier integrity and sustain colonic inflammation. Guselkumab's IL-23p19 blockade interrupts this mucosal inflammatory circuit through the same molecular mechanism validated in psoriasis. The large Phase 2b/3 QUASAR programme (n = 1,064) demonstrated significant clinical remission and endoscopic response versus placebo for both induction and maintenance, leading to FDA approval for moderately-to-severely active UC in late 2024/2025.

Both indications are classic **IL-23-driven immune-mediated inflammatory diseases (IMIDs)** sharing susceptibility loci (*IL23R*, *CARD9*) — the mechanistic bridge from psoriasis to UC is biologically robust and now clinically validated across multiple jurisdictions.

---

## Clinical Trial Evidence — Psoriasis (TxGNN Rank #3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02325219](https://clinicaltrials.gov/study/NCT02325219) | Phase 3 | Completed | 192 | VOYAGE 1: guselkumab vs adalimumab vs placebo; PASI 90 at week 24 significantly superior to adalimumab; foundational for FDA 2017 approval |
| [NCT02207244](https://clinicaltrials.gov/study/NCT02207244) | Phase 3 | Completed | 992 | VOYAGE 2: randomized withdrawal and retreatment; disease control maintained; retreatment successfully re-establishes response |
| [NCT03090100](https://clinicaltrials.gov/study/NCT03090100) | Phase 3 | Completed | 1,048 | ECLIPSE: head-to-head vs secukinumab; guselkumab superior for sustained PASI 90 at week 48 |
| [NCT02207231](https://clinicaltrials.gov/study/NCT02207231) | Phase 3 | Completed | 837 | Confirmatory Phase 3 for moderate-to-severe plaque psoriasis; consistent long-term efficacy through week 100 |
| [NCT05272150](https://clinicaltrials.gov/study/NCT05272150) | Phase 3b | Completed | 213 | Efficacy in skin-of-color participants; supports generalizability across diverse populations |
| [NCT03818035](https://clinicaltrials.gov/study/NCT03818035) | Phase 3b | Completed | 880 | Extended dosing interval (q16w) non-inferior in super-responders (PASI = 0 at weeks 20 & 28) |
| [NCT06039189](https://clinicaltrials.gov/study/NCT06039189) | Phase 3b | Completed | 338 | Low BSA moderate psoriasis with special site involvement (facial, genital, scalp, nail); efficacy vs placebo confirmed |
| [NCT04340076](https://clinicaltrials.gov/study/NCT04340076) | Phase 4 | Completed | 244 | BeNeBio: controlled dose reduction of IL-17/IL-23 inhibitors non-inferior to standard care; informs dosing strategy |
| [NCT04914429](https://clinicaltrials.gov/study/NCT04914429) | Phase 4 | Completed | 327 | Chinese population Phase 4 study confirming efficacy and safety consistency across ethnicities |
| [NCT03451851](https://clinicaltrials.gov/study/NCT03451851) | Phase 3 | Active, not recruiting | 120 | Pediatric (age 6–18) safety and efficacy study; ongoing through December 2026 |

---

## Literature Evidence — Psoriasis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/) | 2017 | RCT (Phase 3) | J Am Acad Dermatol | VOYAGE 1: PASI 90 at week 24: guselkumab 73.3% vs adalimumab 49.7% vs placebo 2.9%; primary endpoint met with high statistical significance |
| [28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/) | 2017 | RCT (Phase 3) | J Am Acad Dermatol | VOYAGE 2: confirmed durable efficacy; patients re-randomized to placebo at week 28 who relapsed were successfully retreated |
| [28635018](https://pubmed.ncbi.nlm.nih.gov/28635018/) | 2018 | RCT (Phase 3) | Br J Dermatol | NAVIGATE: guselkumab superior to continued ustekinumab in inadequate responders; PASI 90 significantly higher at weeks 28 and 52 |
| [31402114](https://pubmed.ncbi.nlm.nih.gov/31402114/) | 2019 | RCT (Phase 3) | Lancet | ECLIPSE: guselkumab vs secukinumab; 84.5% vs 70.0% sustained PASI 90 at week 48 (p < 0.001); first head-to-head IL-23 vs IL-17 superiority |
| [34105767](https://pubmed.ncbi.nlm.nih.gov/34105767/) | 2021 | Long-term Follow-up | Br J Dermatol | VOYAGE 1&2: 5-year sustained PASI 90/100 and HRQoL improvement; no new safety signals at 5 years |
| [31583255](https://pubmed.ncbi.nlm.nih.gov/31583255/) | 2019 | Network Meta-Analysis | J Immunol Res | NMA of IL-17/IL-12/23/IL-23 inhibitors: guselkumab ranks among highest for PASI 90 response with favourable safety |
| [32022825](https://pubmed.ncbi.nlm.nih.gov/32022825/) | 2020 | Meta-Analysis | JAMA Dermatol | Comprehensive meta-analysis of biologics and oral treatments; guselkumab demonstrates top-tier PASI 90/100 rates |
| [37906417](https://pubmed.ncbi.nlm.nih.gov/37906417/) | 2024 | Integrated Safety Analysis | Drug Safety | Pooled safety from 11 Phase 2/3 studies in psoriasis and PsA; guselkumab well-tolerated; no increased malignancy or MACE signal |
| [30772098](https://pubmed.ncbi.nlm.nih.gov/30772098/) | 2019 | Clinical Guidelines | J Am Acad Dermatol | AAD-NPF joint guidelines: guselkumab recommended as a first-line biologic for moderate-to-severe psoriasis |
| [32427307](https://pubmed.ncbi.nlm.nih.gov/32427307/) | 2020 | Review | JAMA | Psoriasis pathophysiology and treatment overview; IL-23p19 inhibitors highlighted as paradigm-shifting therapeutic class |

---

## Clinical Trial Evidence — Ulcerative Colitis (TxGNN Rank #6)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Phase 2b/3 | Active, not recruiting | 1,064 | QUASAR core trial: IV induction (200 mg q8w × 3 doses) followed by SC maintenance; primary basis for FDA approval of UC indication |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Phase 3 | Active, not recruiting | 418 | ASTRO: all-SC induction regimen; aims to simplify treatment without IV administration |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Phase 2b | Active, not recruiting | 577 | Guselkumab + golimumab dual-biologic combination vs monotherapy in bio-experienced moderate-to-severe UC |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Phase 3 | Active, not recruiting | 112 | Pediatric UC Phase 3: induction and maintenance in children with moderately-to-severely active UC |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Phase 2a | Completed | 214 | Proof-of-concept combination (guselkumab + golimumab) in UC; combination arm showed numerical superiority over monotherapy |
| [NCT06408935](https://clinicaltrials.gov/study/NCT06408935) | Phase 3b | Recruiting | 112 | Transmural healing endpoint (MaRIA score) as disease modification marker at week 48 in CD |
| [NCT07102368](https://clinicaltrials.gov/study/NCT07102368) | Observational | Recruiting | 400 | Real-world effectiveness in IBD (UC and CD) post-approval; multiple European centres |
| [NCT07245394](https://clinicaltrials.gov/study/NCT07245394) | Observational | Recruiting | 200 | **SHIFT-IBD (Canada-based)**: switching from ustekinumab to guselkumab in active IBD; provides Canadian real-world data |
| [NCT07302360](https://clinicaltrials.gov/study/NCT07302360) | Observational | Recruiting | 200 | Real-world bio-naïve UC patients in China receiving guselkumab; supplements ethnic diversity data |
| [NCT07242248](https://clinicaltrials.gov/study/NCT07242248) | Observational | Recruiting | 220 | UK real-world effectiveness in UC and CD by lines of therapy and subpopulations |

---

## Literature Evidence — Ulcerative Colitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | RCT (Phase 3) | Lancet | QUASAR induction & maintenance: clinical remission and endoscopic response significantly superior to placebo; FDA approval basis for UC (2024/2025) |
| [41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/) | 2026 | RCT (Phase 3) | Lancet Gastroenterol Hepatol | ASTRO: SC induction achieves clinical remission and endoscopic improvement vs placebo; enables fully SC treatment pathway |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | RCT (Phase 2b) | Gastroenterology | QUASAR Phase 2b: dose-ranging induction (200 mg and 1,200 mg IV) both superior to placebo for clinical remission; dose selection confirmed |
| [40113101](https://pubmed.ncbi.nlm.nih.gov/40113101/) | 2025 | RCT (Phase 3) | Gastroenterology | GRAVITI: SC induction/maintenance in Crohn's disease; confirms IL-23p19 class effect across IBD spectrum |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Clinical Guidelines | Gastroenterology | AGA Living Guideline: guselkumab included as a recommended advanced therapy for moderate-to-severe UC |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Network Meta-Analysis | Gastroenterology | AGA evidence synthesis: guselkumab ranks among top-tier agents for clinical remission and endoscopic improvement in UC |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Review | Nat Rev Gastroenterol Hepatol | Comprehensive mechanistic and clinical review of IL-12/IL-23 pathway inhibition in IBD; guselkumab as selective IL-23 option |
| [41324615](https://pubmed.ncbi.nlm.nih.gov/41324615/) | 2025 | Expert Review | Expert Opin Biol Ther | Expert evaluation of guselkumab for UC: positioning, clinical data review, and place in current treatment algorithm |
| [35553666](https://pubmed.ncbi.nlm.nih.gov/35553666/) | 2022 | Review | J Crohns Colitis | IL-23 blockade pipeline in IBD: selective vs non-selective inhibition; mechanistic rationale for guselkumab in UC and CD |
| [39994836](https://pubmed.ncbi.nlm.nih.gov/39994836/) | 2025 | Review | Chin Med J | IBD epidemiology, pathogenesis, diagnosis, and treatment update; IL-23 inhibitors including guselkumab highlighted as key advance |

---

## Canada Market Information

Guselkumab currently has **no Health Canada authorization** and **no DINs on file**.

| DIN | Product Name | Dosage Form | Approved Indication |
|-----|-------------|-------------|---------------------|
| — | Not applicable | — | No Canadian approval |

> **Note**: Guselkumab (Tremfya®) holds regulatory approvals in the United States (FDA, 2017 — plaque psoriasis; 2022 — psoriatic arthritis; 2024/2025 — ulcerative colitis), the European Union (EMA), Japan, and multiple other jurisdictions. The absence of Canadian authorization represents a **regulatory filing gap**, not a gap in global evidence.

---

## Safety Considerations

Health Canada-specific safety data (product monograph, warnings, contraindications) is not available (Data Gap: DG001). No drug-drug interactions were identified in the DDI database. Based on global regulatory documents and integrated clinical trial safety analyses:

- **Key Warnings**: Risk of serious infections (bacterial, mycobacterial, fungal, viral); tuberculosis screening required before initiation; do not administer during clinically significant active infections; interrupt treatment if serious infection develops
- **Contraindications**: Clinically important active infections; known hypersensitivity to guselkumab or to any excipient
- **Immunization**: Avoid live vaccines during treatment; bring vaccinations up to date before initiating therapy

For complete safety information, refer to the FDA Prescribing Information (Tremfya® US label) or EMA Summary of Product Characteristics, as Health Canada-specific guidance is not yet available.

---

## Conclusion and Next Steps

### TxGNN Prediction Summary

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|------------|----------------|---------|
| 1 | Drug-induced osteoporosis | 99.84% | L5 | Hold |
| 2 | Severe nonproliferative diabetic retinopathy | 99.80% | L5 | Hold |
| **3** | **Psoriasis** | **99.74%** | **L1** | **Proceed with Guardrails** |
| 4 | Diabetic retinopathy | 99.74% | L5 | Hold |
| 5 | Renal osteodystrophy | 99.73% | L5 | Hold |
| **6** | **Ulcerative colitis** | **99.70%** | **L1** | **Proceed with Guardrails** |
| 7–10 | Genetic/hematologic disorders | 99.67–99.55% | L5 | Hold |

---

**Decision: Proceed with Guardrails** (Psoriasis & Ulcerative Colitis)

**Rationale:**
Guselkumab has completed multiple Phase 3 RCTs for both psoriasis and UC with consistent, statistically significant superiority over placebo and active comparators; the IL-23p19 mechanistic basis is directly validated by FDA and EMA approvals. The absence of Health Canada authorization is a **regulatory filing gap** — the Canadian clinical evidence base already exists. TxGNN's top-ranked predictions (ranks #1 and #2) score highly due to shared inflammatory network neighbours in the knowledge graph but lack direct mechanistic rationale or clinical data and should remain on **Hold**.

**To proceed, the following is needed:**

- **Regulatory filing**: Prepare or expedite a Health Canada New Drug Submission (NDS) leveraging existing FDA/EMA dossier; consider Priority Review or Standard Review pathway
- **Safety documentation**: Obtain full Health Canada Product Monograph equivalent; complete Data Gap DG001 (TFDA-equivalent warnings and contraindications)
- **MOA documentation**: Complete DrugBank lookup (DB11834) to fill Data Gap DG002 for formal mechanistic risk assessment
- **Pharmacoeconomic review**: Commission CADTH (Canadian Drug Review) health technology assessment for public payer reimbursement of both psoriasis and UC indications
- **Canadian real-world evidence**: Monitor SHIFT-IBD (NCT07245394, recruiting in Canada) for domestic UC effectiveness data
- **Hold indications**: For drug-induced osteoporosis, diabetic retinopathy, and other L5 predictions — initiate targeted mechanistic and preclinical studies before any clinical investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

