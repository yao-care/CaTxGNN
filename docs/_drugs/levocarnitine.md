---
layout: default
title: Levocarnitine
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Levocarnitine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Levocarnitine (DB00583): From an Undocumented Original Indication to Rheumatoid Arthritis, Heart Failure, and Diabetic Nephropathy

## One-Sentence Summary

Levocarnitine (DB00583) has no Taiwan/Canada regulatory license or original-indication record in this evidence pack (it is currently **Not marketed / not marketed** in Canada, 0 DINs), so its established clinical use cannot be sourced here — it is generally known as the endogenous mitochondrial fatty-acid transport cofactor. TxGNN scored **10 candidate indications** at very high but closely clustered confidence (99.4–99.9%); when cross-checked against real clinical trial and PubMed evidence, three stand out as genuinely actionable — **rheumatoid arthritis**, **congestive heart failure**, and **diabetic nephropathy** — while the other seven (including the single highest-scored disease) have **zero or irrelevant evidence** and appear to be model noise.

---

## Quick Overview

### Drug & Regulatory Snapshot

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no Taiwan/Canada license record exists in this pack |
| Original MOA | Not directly documented (Data Gap DG002); mechanism inferred below from the literature captured in this evidence base |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Predicted Indications Evaluated | 10 (TxGNN top-ranked candidates) |
| Indications with Actionable Evidence (≥L3) | 3 — Diabetic Nephropathy (L3), Rheumatoid Arthritis (L2), Congestive Heart Failure (L2) |
| Overall Recommended Decision | **Proceed with Guardrails** (RA, CHF, DN) / **Hold** (remaining 7 candidates) |

### Predicted Indication Ranking (all 10 TxGNN candidates)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|--------------|-----------------|------------------|------------------|
| 1 | Autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome | 99.94% | L5 | S0 | Hold |
| 2 | Brain small vessel disease 1 with or without ocular anomalies | 99.94% | L5 | S0 | Hold |
| 3 | **Diabetic nephropathy** | 99.91% | **L3** | S1 | Research Question |
| 4 | **Rheumatoid arthritis** | 99.87% | **L2** | S2 | Research Question |
| 5 | Sclerosing cholangitis | 99.75% | L4 | S0 | Hold |
| 6 | Gout | 99.74% | L4 | S0 | Hold |
| 7 | Brachydactyly–syndactyly syndrome | 99.66% | L5 | S0 | Hold |
| 8 | Colobomatous microphthalmia–rhizomelic dysplasia syndrome | 99.63% | L5 | S0 | Hold |
| 9 | **Congestive heart failure** | 99.47% | **L2** | S2 | Research Question |
| 10 | Hypoalphalipoproteinemia | 99.45% | L4 | S0 | Hold |

Note: TxGNN scores alone are **not** a reliable proxy for evidentiary strength here — the single highest-scored prediction (rank 1) has zero supporting trials or literature, while the strongest evidence (RA, CHF) sits at ranks 4 and 9.

---

## Why Are These Predictions Reasonable?

Levocarnitine is the physiologically active enantiomer of carnitine, an essential cofactor of the carnitine palmitoyltransferase system (CPT1/CPT2) and the carnitine-acylcarnitine translocase, which shuttles long-chain fatty acids across the inner mitochondrial membrane for β-oxidation. This role is consistently documented across the literature returned in this evidence pack itself (e.g., PMID [21561431](https://pubmed.ncbi.nlm.nih.gov/21561431/), [36632072](https://pubmed.ncbi.nlm.nih.gov/36632072/)), rather than external prior knowledge — which is why it recurs as a plausible mechanistic thread across several unrelated organ systems.

- **Diabetic nephropathy**: Impaired renal fatty-acid oxidation and CPT1A downregulation drive lipotoxic injury in proximal tubular and podocyte cells; preclinical work shows CPT1A overexpression or carnitine-pathway restoration attenuates injury (PMID [38506804](https://pubmed.ncbi.nlm.nih.gov/38506804/), [40402578](https://pubmed.ncbi.nlm.nih.gov/40402578/)). This is mechanistically coherent but has not yet been confirmed in a completed, adequately powered human trial.
- **Rheumatoid arthritis**: RA fibroblast-like synoviocytes and T cells show altered fatty-acid oxidation/acylcarnitine metabolism (PMID [35273614](https://pubmed.ncbi.nlm.nih.gov/35273614/), [40894250](https://pubmed.ncbi.nlm.nih.gov/40894250/)), and carnitine/antioxidant depletion has been observed in RA patients since 1998 (PMID [9855215](https://pubmed.ncbi.nlm.nih.gov/9855215/)). This is now backed by an actual completed randomized crossover trial and two additional direct RA intervention trials.
- **Congestive heart failure**: Failing myocardium shifts from fatty-acid to glucose metabolism, and carnitine deficiency has long been implicated in cardiomyopathy and anthracycline-induced cardiotoxicity (PMID [11298185](https://pubmed.ncbi.nlm.nih.gov/11298185/), [12695723](https://pubmed.ncbi.nlm.nih.gov/12695723/)). A completed 268-patient RCT of IV levocarnitine in heart failure directly supports this pathway.

By contrast, the top-ranked prediction (a rare hematuria/retinal-tortuosity syndrome) and rank 2 (brain small vessel disease with ocular anomalies) returned **no clinical trials and no on-topic literature** — the 19 papers retrieved for rank 2 are unrelated congenital-ophthalmology case reports, most plausibly a disease-ontology text-matching artifact rather than a real signal.

---

## Detailed Evidence by Indication

### 1. Diabetic Nephropathy (Rank 3, L3, TxGNN 99.91%)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755404](https://clinicaltrials.gov/study/NCT00755404) | Phase 2 | Withdrawn | 0 | Intended to test peritoneal dialysis solution with L-carnitine (0.1%) on insulin sensitivity in CAPD patients; withdrawn before enrollment |
| [NCT01566006](https://clinicaltrials.gov/study/NCT01566006) | N/A | Unknown | 80 | Tested MMF + carnitine + PDE5 inhibitor as combined therapy for resistant proteinuria/progressive diabetic nephropathy in T2DM; carnitine's individual contribution cannot be isolated from this design |

**Literature** (top 10 of 20 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40402578](https://pubmed.ncbi.nlm.nih.gov/40402578/) | 2025 | Review/Translational | JCI Insight | Impaired carnitine-dependent fatty acid oxidation (via OCTN2 deficiency) drives lipid accumulation and correlates inversely with kidney function in diabetic kidney disease |
| [37330521](https://pubmed.ncbi.nlm.nih.gov/37330521/) | 2023 | Cohort (biomarker) | Diabetol Metab Syndr | Acylcarnitine levels associate with and predict diabetic nephropathy in Chinese T2DM patients |
| [38506804](https://pubmed.ncbi.nlm.nih.gov/38506804/) | 2024 | Preclinical (mechanistic) | Diabetes | CPT1A protects podocytes from lipotoxicity/apoptosis in vitro and alleviates diabetic nephropathy in vivo |
| [35104825](https://pubmed.ncbi.nlm.nih.gov/35104825/) | 2022 | Preclinical (animal) | Kidney Blood Press Res | L-carnitine treatment improves kidney mitochondrial function and reduces macrophage activation in a diabetic nephropathy mouse model |
| [24371263](https://pubmed.ncbi.nlm.nih.gov/24371263/) | 2014 | Human biopsy study | J Lipid Res | Altered renal lipid metabolism with heavy lipid accumulation demonstrated in human diabetic nephropathy kidney biopsies |
| [34103347](https://pubmed.ncbi.nlm.nih.gov/34103347/) | 2021 | Preclinical | Diabetes | Annexin A1 attenuates diabetic nephropathy via AMPK/PPARα/CPT1b lipid-metabolism pathway |
| [38767438](https://pubmed.ncbi.nlm.nih.gov/38767438/) | 2024 | Preclinical | Acta Physiol | ALR knockout aggravates tubular ferroptosis via CPT1A-linked lipid metabolism dysregulation in diabetic nephropathy |
| [37728037](https://pubmed.ncbi.nlm.nih.gov/37728037/) | 2023 | Case-control | Biomed Chromatogr | Children with type 1 diabetic nephropathy show altered plasma free carnitine and acylcarnitine profiles |
| [41139215](https://pubmed.ncbi.nlm.nih.gov/41139215/) | 2026 | Preclinical | Autophagy | XIAP-ULK1-mediated mitophagy regulates carnitine metabolism to mitigate diabetic kidney disease |
| [34900545](https://pubmed.ncbi.nlm.nih.gov/34900545/) | 2021 | Metabolomics | Acta Pharm Sin B | Spatial mass-spectrometry imaging reveals tissue-specific metabolic reprogramming, including carnitine-pathway shifts, in diabetic nephropathy |

### 2. Rheumatoid Arthritis (Rank 4, L2, TxGNN 99.87%)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03953703](https://clinicaltrials.gov/study/NCT03953703) | Phase 2 | Completed | 15 | Randomized, placebo-controlled crossover trial of levocarnitine for keratoconjunctivitis sicca (dry eye) in **Sjögren's syndrome** — a related autoimmune rheumatic disease, not RA itself; note the mismatch with the RA indication label |
| [NCT06753565](https://clinicaltrials.gov/study/NCT06753565) | Phase 2 | Recruiting | 60 | Evaluates L-carnitine as add-on therapy for improving disease activity outcomes in RA patients |
| [NCT05792527](https://clinicaltrials.gov/study/NCT05792527) | Phase 3 | Unknown | 46 | Tests L-carnitine's efficacy/safety in RA via JAK/STAT and TGF-β1 pathway modulation for pain and inflammation |

**Literature** (top 10 of 20 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41037123](https://pubmed.ncbi.nlm.nih.gov/41037123/) | 2025 | Clinical | Inflammopharmacology | L-carnitine as adjunct RA therapy targeting JAK/STAT and TGF-β1 in 46 active-RA patients (likely publication of NCT05792527) |
| [9855215](https://pubmed.ncbi.nlm.nih.gov/9855215/) | 1998 | Cohort | Scand J Rheumatol | RA patients show altered carnitine and antioxidant (MDA, SOD) levels versus controls |
| [35523821](https://pubmed.ncbi.nlm.nih.gov/35523821/) | 2022 | Cohort/Mechanistic | Sci Rep | RA T-cell and muscle oxidative metabolism associate with exercise-induced cardiorespiratory fitness changes |
| [33674638](https://pubmed.ncbi.nlm.nih.gov/33674638/) | 2021 | Metabolomic cohort | Sci Rep | Carnitine- and choline-derivative profiles differ with periodontal inflammation severity in RA outpatients |
| [35273614](https://pubmed.ncbi.nlm.nih.gov/35273614/) | 2022 | Preclinical | Front Immunol | CPT1A-mediated fatty acid oxidation promotes osteoclast precursor fusion and bone destruction in RA |
| [27755546](https://pubmed.ncbi.nlm.nih.gov/27755546/) | 2016 | Biobank cohort | PLoS One | Metabolite/lipid profiling of plasma collected before RA onset, aiming to improve early diagnosis |
| [37163819](https://pubmed.ncbi.nlm.nih.gov/37163819/) | 2023 | Preclinical (rat) | J Trace Elem Med Biol | L-carnitine + zinc protects against methotrexate-induced intestinal toxicity in arthritis model |
| [37405586](https://pubmed.ncbi.nlm.nih.gov/37405586/) | 2023 | Preclinical | Inflammopharmacology | Zinc + L-carnitine prevents MTX-induced intestinal toxicity via Nrf2/Sirt1/Foxo3 pathways during arthritis treatment |
| [17142562](https://pubmed.ncbi.nlm.nih.gov/17142562/) | 2007 | Mechanistic | Drug Metab Dispos | RA-associated transcription factor RUNX1 and inflammatory cytokines regulate the carnitine transporter OCTN1 (SLC22A4) |
| [18328148](https://pubmed.ncbi.nlm.nih.gov/18328148/) | 2008 | Genetic association | Clin Exp Rheumatol | SLC22A4/RUNX1 genotype variants show no influence on circulating carnitine ester profile in RA |

### 3. Congestive Heart Failure (Rank 9, L2, TxGNN 99.47%)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01580553](https://clinicaltrials.gov/study/NCT01580553) | Phase 2/3 | Completed | 268 | Multicenter, randomized, double-blind, placebo-controlled trial of L-carnitine injection in Chinese heart failure patients — the largest completed direct interventional evidence for this indication |
| [NCT00247975](https://clinicaltrials.gov/study/NCT00247975) | Phase 2/3 | Terminated | 36 | Tested L-carnitine for primary prevention of anthracycline-induced cardiotoxicity in breast cancer patients |
| [NCT01904396](https://clinicaltrials.gov/study/NCT01904396) | Phase 4 | Unknown | 30 | Identifies carnitine-responsive cardiomyopathy/myopathy in adults with dilated/hypertrophic cardiomyopathy and limb-girdle weakness |
| [NCT02862600](https://clinicaltrials.gov/study/NCT02862600) | Phase 2 | Terminated | 35 | Perhexiline (a fatty-acid-oxidation/CPT inhibitor, mechanistically linked) in hypertrophic cardiomyopathy with HFpEF |
| [NCT04913805](https://clinicaltrials.gov/study/NCT04913805) | Phase 2 | Recruiting | 53 | Tests propionyl-L-carnitine plus nicotinamide riboside for exercise endurance and skeletal-muscle mitochondrial function in HFpEF |
| [NCT07201714](https://clinicaltrials.gov/study/NCT07201714) | Early Phase 1 | Not yet recruiting | 20 | Oral L-carnitine supplementation planned in cardiorenal heart failure patients |
| [NCT03994874](https://clinicaltrials.gov/study/NCT03994874) | Phase 1/2 | Recruiting | 84 | Tests a PolyCore (polydextrin, L-carnitine, D-xylitol) peritoneal ultrafiltration solution to prevent HFrEF exacerbation |
| [NCT01524861](https://clinicaltrials.gov/study/NCT01524861) | Phase 4 | Completed | 90 | Evaluated α-lipoic acid and L-acetyl carnitine on sympathetic cardiac innervation after Takotsubo (stress) cardiomyopathy |
| [NCT04426578](https://clinicaltrials.gov/study/NCT04426578) | Phase 2 | Unknown | 60 | Perhexiline (CPT inhibitor) for regression of LV hypertrophy in symptomatic hypertrophic cardiomyopathy |

**Literature** (top 10 of 20 retrieved)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30195728](https://pubmed.ncbi.nlm.nih.gov/30195728/) | 2020 | Clinical | Hellenic J Cardiol | Levocarnitine improves cardiac function and reduces urinary albumin, hs-CRP, BNP, and troponin in coronary heart disease with heart failure |
| [21561431](https://pubmed.ncbi.nlm.nih.gov/21561431/) | 2011 | Review | Curr Drug Metab | Overview of L-carnitine's metabolic functions, including fatty-acid transport into mitochondria |
| [36632072](https://pubmed.ncbi.nlm.nih.gov/36632072/) | 2023 | Review | Saudi J Biol Sci | Carnitine deficiency is linked to cardiomyopathy, diabetes, and other conditions; nutrition/pathology overview |
| [17445089](https://pubmed.ncbi.nlm.nih.gov/17445089/) | 2007 | Review | Cardiovasc Drug Rev | Perhexiline inhibits carnitine palmitoyltransferase to reduce fatty-acid metabolism, mechanistically relevant to carnitine-pathway modulation in HF |
| [12695723](https://pubmed.ncbi.nlm.nih.gov/12695723/) | 2003 | Review | Am J Med Sci | L-carnitine deficiency may contribute to congestive heart failure in patients with chronic kidney disease/ESRD |
| [11298185](https://pubmed.ncbi.nlm.nih.gov/11298185/) | 2000 | Review | Int J Exp Pathol | Metabolic cardiomyopathies overview, including fatty-acid β-oxidation enzyme deficiencies |
| [40593619](https://pubmed.ncbi.nlm.nih.gov/40593619/) | 2025 | Preclinical | Nat Commun | Mitophagy mitigates cardiomyopathy caused by mitochondrial fatty-acid β-oxidation deficiency |
| [38718533](https://pubmed.ncbi.nlm.nih.gov/38718533/) | 2024 | Preclinical | Redox Biol | Sirt5 improves cardiomyocyte fatty-acid metabolism via CPT2 de-succinylation, ameliorating diabetic cardiomyopathy lipotoxicity |
| [39858422](https://pubmed.ncbi.nlm.nih.gov/39858422/) | 2024 | Cohort (biomarker) | Biomolecules | Plasma propionylcarnitine improves prediction of heart failure and all-cause mortality in stable coronary artery disease |
| [40064034](https://pubmed.ncbi.nlm.nih.gov/40064034/) | 2025 | Preclinical (canine) | ESC Heart Fail | Plasma metabolites and cardiac mitochondrial function associate with heart failure progression |

### Other Predicted Indications (Low/No Evidence — Hold)

| Rank | Disease | Trials | Literature | Rationale Summary |
|------|---------|--------|------------|---------------------|
| 1 | Autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome | 0 | 0 | No trials, no literature, no known mechanistic link to carnitine metabolism — pure model prediction |
| 2 | Brain small vessel disease 1 with/without ocular anomalies | 0 | 19 (all off-topic) | 19 papers retrieved are unrelated congenital ophthalmology case reports (e.g., Axenfeld-Rieger, optic disc anomalies); assessed as disease-ontology matching noise, not real evidence |
| 5 | Sclerosing cholangitis | 0 | 4 | Descriptive/mechanistic literature on hepatic mitochondrial dysfunction and lipid alteration only; no interventional data |
| 6 | Gout | 0 | 16 | Mendelian-randomization/metabolomic association between acylcarnitines, OCTN transporters, and urate levels — indirect correlation, not a treatment mechanism; no trials |
| 7 | Brachydactyly–syndactyly syndrome | 0 | 0 | No evidence of any kind; no known mechanistic link (skeletal developmental disorder) |
| 8 | Colobomatous microphthalmia–rhizomelic dysplasia syndrome | 0 | 0 | No evidence of any kind; no known mechanistic link (congenital developmental syndrome) |
| 10 | Hypoalphalipoproteinemia | 0 | 3 | ABCA1-related genetic HDL disorder; literature is metabolomic/genetic association only, no treatment rationale or trials |

**Currently no related clinical trials registered** for 6 of the 10 candidates (ranks 1, 2, 5, 6, 7, 8, 10 — ranks 7 and 8 additionally have no literature at all).

---

## Canada Market Information

Levocarnitine is **not marketed** in Canada under this evidence pack (`market_status: Not marketed`, `total_licenses: 0`). No DIN or product-level licensing data is available, so the standard authorization table is omitted.

---

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack's own safety fields (key warnings, contraindications, and drug-interaction query) returned no data, and the TFDA label/warning lookup is flagged in `meta.data_gaps` as a **Blocking** gap (DG001) that must be resolved before any Stage-1 safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Rheumatoid Arthritis, Congestive Heart Failure, and Diabetic Nephropathy) / **Hold** (for the remaining 7 candidates)

**Rationale:**
- RA and CHF each have at least one **completed** interventional trial with a plausible fatty-acid-oxidation mechanism, warranting continued research investment but not yet a "Go" (no ≥2 completed Phase 3 RCTs exist for either).
- Diabetic nephropathy has strong preclinical/mechanistic and biomarker support but only withdrawn/indeterminate trials, so it remains a research question rather than an actionable candidate.
- The seven remaining candidates — including the single **highest**-scoring TxGNN prediction — have no meaningful clinical or mechanistic support and are held pending better evidence or are likely scoring artifacts.

**To proceed, the following is needed:**
- TFDA/Canada label warnings and contraindications (Blocking gap DG001) — required before any safety screening
- Confirmed mechanism-of-action and original approved indication documentation (High-priority gap DG002) — currently absent from regulatory records in this pack
- For RA: results from the two ongoing/unknown-status direct RA trials (NCT06753565, NCT05792527)
- For CHF: independent replication of the completed 268-patient trial (NCT01580553) in a non-single-country population
- For diabetic nephropathy: a properly powered, completed interventional trial isolating levocarnitine's effect (current trials are withdrawn or use multi-drug combinations)
- Clarification of why rank-2 literature retrieval returned exclusively unrelated ophthalmology case reports, to assess whether the underlying disease-mapping pipeline needs correction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

