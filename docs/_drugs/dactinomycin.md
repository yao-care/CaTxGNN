---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dactinomycin: From Rhabdomyosarcoma/Wilms Tumor to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin (Actinomycin D) is an established cytotoxic antibiotic and cornerstone of the VAC (vincristine–actinomycin D–cyclophosphamide) regimen, used globally for rhabdomyosarcoma, Wilms tumor, and Ewing's sarcoma, though it is not currently marketed in Canada.
The TxGNN model's highest-ranked prediction assigns a **99.58% score** for **relapsing-remitting multiple sclerosis (RRMS)**, but this direction is supported by **no clinical trials and no publications**, and the mechanistic rationale is considered biologically implausible.
Importantly, this Evidence Pack also identifies **parameningeal embryonal rhabdomyosarcoma** (Rank 5) as a higher-priority finding with **L1 evidence** backed by Phase 3 RCTs — representing the most clinically actionable repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rhabdomyosarcoma, Wilms tumor, gestational trophoblastic neoplasia (established global use; not approved in Canada) |
| Predicted New Indication (Top TxGNN) | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** (for RRMS) — see supplementary section for actionable RMS subtype findings |

---

## Why Is This Prediction Reasonable?

Dactinomycin intercalates between guanine–cytosine base pairs in double-stranded DNA and physically blocks RNA polymerase, halting transcription. This makes it highly cytotoxic to rapidly proliferating cells — the basis of its efficacy against rhabdomyosarcoma, Wilms tumor, and other pediatric solid tumors. It is a decades-proven component of combination chemotherapy protocols (VAC for RMS; actinomycin D + vincristine for Wilms), with multiple Phase 3 landmark trials (IRS-III, IRS-IV, NWTS-5) establishing its role.

For relapsing-remitting multiple sclerosis, the mechanistic bridge is extremely tenuous. While cytotoxic immunosuppression can theoretically dampen autoimmune activity, RRMS management demands safe, sustained immunomodulation over years or decades — a profile fundamentally at odds with dactinomycin's high-toxicity, narrow-therapeutic-window character. Known risks including severe myelosuppression, veno-occlusive disease of the liver, and teratogenicity make long-term RRMS use clinically untenable.

The high TxGNN score for RRMS most likely reflects indirect graph connectivity — dactinomycin's associations with neurological tumour contexts and broad immune-cell interactions propagating through the knowledge graph — rather than genuine biological relevance. The repurposing rationale embedded in the Evidence Pack explicitly confirms: *"TxGNN high score may reflect indirect graph pathways between RMS and the nervous system, not a true biological association."*

---

## Clinical Trial Evidence

Currently no clinical trials related to dactinomycin in relapsing-remitting multiple sclerosis are registered.

---

## Literature Evidence

Currently no related literature is available for dactinomycin in relapsing-remitting multiple sclerosis.

---

## Canada Market Information

Dactinomycin is not currently marketed in Canada. No DIN records were found in the regulatory database.

---

## Cytotoxicity

Dactinomycin is a conventional cytotoxic agent (actinomycin class, DNA-intercalating antibiotic) and triggers mandatory assessment under this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA-intercalating antibiotic (Actinomycin class) |
| Myelosuppression Risk | **High** — significant neutropenia, thrombocytopenia, and anemia reported; dose-limiting in pediatric regimens |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential (weekly during treatment), liver function tests (AST/ALT/bilirubin for VOD surveillance), renal function, body weight (fluid retention as VOD signal), mucositis assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system transfer devices, PPE, dedicated disposal pathways required |

---

## Safety Considerations

**Key known safety signals from retrieved literature:**

- **Hepatic veno-occlusive disease (VOD)**: Multiple reports of VOD following VAC chemotherapy including dactinomycin in pediatric patients ([PMID 9191535](https://pubmed.ncbi.nlm.nih.gov/9191535/), [PMID 7700188](https://pubmed.ncbi.nlm.nih.gov/7700188/), [PMID 11378345](https://pubmed.ncbi.nlm.nih.gov/11378345/)). VOD has occurred without prior bone marrow transplant conditioning — purely from standard-dose VAC.
- **Age-dependent hepatopathy**: Age is a significant risk factor for dactinomycin-induced liver toxicity; younger children are disproportionately affected ([PMID 15143082](https://pubmed.ncbi.nlm.nih.gov/15143082/)).
- **Myelosuppression and dosing**: Evidence-based dosing guidance remains limited despite 40+ years of use; retrospective COG data highlight toxicity variability ([PMID 21671362](https://pubmed.ncbi.nlm.nih.gov/21671362/)).

> Detailed warning text and formal contraindications are unavailable in this Evidence Pack (Data Gap DG001 — TFDA/Health Canada package insert not yet parsed). Please refer to the product monograph for complete safety information.

---

## Conclusion and Next Steps

**Decision for RRMS (Top TxGNN Prediction): Hold**

**Rationale:**
No clinical or mechanistic evidence supports dactinomycin in relapsing-remitting multiple sclerosis. The severe and cumulative toxicity profile of this conventional cytotoxic drug is incompatible with the long-term, low-toxicity treatment requirements of RRMS. This TxGNN prediction is assessed as a knowledge-graph false positive.

**To revisit this Hold decision, the following would be needed:**
- Mechanistic studies demonstrating selective immunomodulation without systemic cytotoxicity at sub-therapeutic doses
- Preclinical (animal model) evidence in EAE (experimental autoimmune encephalomyelitis) or comparable MS models
- Safety data supporting chronic dosing at immunomodulatory (not cytotoxic) plasma levels

---

## Supplementary: Full Multi-Indication Analysis

### Overview of All Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|------------|----------------|---------|
| 1 | Relapsing-remitting multiple sclerosis | 99.58% | L5 | Hold |
| 2 | Botryoid-type embryonal RMS of the vagina | 99.54% | L4 | Research Question |
| 3 | Extrahepatic bile duct RMS | 99.49% | L4 | Research Question |
| 4 | Embryonal extrahepatic bile duct RMS | 99.48% | L4 | Research Question |
| **5** | **Parameningeal embryonal RMS** | **99.48%** | **L1** | **Proceed with Guardrails** |
| 6 | Prostate embryonal RMS | 99.46% | L2 | Proceed with Guardrails |
| 7 | Liver sarcoma | 99.42% | L3 | Research Question |
| 8 | Upper aerodigestive tract neoplasm | 99.16% | L2 | Proceed with Guardrails |
| 9 | Head and neck cancer | 99.16% | L2 | Proceed with Guardrails |

---

### Priority Finding — Parameningeal Embryonal RMS (Rank 5 | L1 | Proceed with Guardrails)

**TxGNN Score: 99.48%**

Parameningeal embryonal rhabdomyosarcoma is one of the highest-risk RMS subtypes, arising in proximity to the meninges (nasopharynx, paranasal sinuses, middle ear/mastoid, infratemporal and pterygopalatine fossae). It carries high risk of intracranial extension and meningeal seeding. Dactinomycin, as the "A" in the VAC backbone, has been directly evaluated in this anatomical subgroup across multiple landmark Phase 3 RCTs by the Intergroup Rhabdomyosarcoma Study Group (IRSG) and Children's Oncology Group (COG).

**Decision: Proceed with Guardrails**
Phase 3 RCT evidence directly evaluating dactinomycin-containing regimens in parameningeal RMS supports clinical use, subject to specialist centre evaluation and rigorous hepatotoxicity/VOD monitoring protocols.

#### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19770373](https://pubmed.ncbi.nlm.nih.gov/19770373/) | 2009 | Phase 3 RCT | J Clin Oncol | COG D9803: VAC vs VAC/VTC for intermediate-risk RMS (includes parameningeal subgroup); dactinomycin is the standard-arm backbone |
| [10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/) | 2000 | Phase 3 RCT | J Clin Oncol | IRS-IV: Intensified therapy benefit for local/regional embryonal RMS vs IRS-III; parameningeal patients included in both arms |
| [12654440](https://pubmed.ncbi.nlm.nih.gov/12654440/) | 2003 | Retrospective Cohort | Int J Radiat Oncol Biol Phys | Radiation volume impact on pediatric parameningeal RMS outcome; chemotherapy context is VAC |

---

### Prostate Embryonal RMS (Rank 6 | L2 | Proceed with Guardrails)

**TxGNN Score: 99.46%**

Primarily a pediatric malignancy (peak age ~3–6 years), prostatic embryonal RMS is treated within the IRS Group II/III bladder-prostate framework using VAC chemotherapy. Modern case series through 2022 continue using dactinomycin-containing regimens.

#### Literature Evidence (Top 10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/) | 2000 | Phase 3 RCT | J Clin Oncol | IRS-IV: GU tract RMS with VAC backbone including dactinomycin |
| [34900598](https://pubmed.ncbi.nlm.nih.gov/34900598/) | 2022 | Case Report + Review | Urology Case Reports | Adult prostatic embryonal RMS in a 54-year-old: VAC (dactinomycin, vincristine, cyclophosphamide) + surgery + radiation; literature review |
| [11846299](https://pubmed.ncbi.nlm.nih.gov/11846299/) | 2001 | Retrospective Review | J Pediatr Hematol Oncol | IRS I–IV experience review; prognostic factors underpinning IRS-V design; VAC standard treatment context |
| [28427078](https://pubmed.ncbi.nlm.nih.gov/28427078/) | 2019 | Case Report | Urol Int | Adult metastatic prostatic RMS in a 32-year-old; treated with IRS III regimen (VAC induction) + radiation; long-term cure |
| [22104356](https://pubmed.ncbi.nlm.nih.gov/22104356/) | 2012 | Prospective Cohort | Int J Radiat Oncol Biol Phys | COG D9602: Reduced-dose radiotherapy in low-risk RMS; VAC chemotherapy backbone |
| [1127815](https://pubmed.ncbi.nlm.nih.gov/1127815/) | 1975 | Case Series | J Urology | 30 children with bladder/prostate embryonal RMS; 23% overall survival; aggressive combined therapy approach |
| [2488079](https://pubmed.ncbi.nlm.nih.gov/2488079/) | 1989 | Case Series | Cir Pediatr | 12 genitourinary RMS cases; VAC (vincristine, d-actinomycin, cyclophosphamide) as primary chemotherapy |
| [55104](https://pubmed.ncbi.nlm.nih.gov/55104/) | 1975 | Case Report | Arch Chir Neerl | 22-month-old with prostatic embryonal sarcoma; VAC (actinomycin D + vincristine + cyclophosphamide) + surgery; disease-free at 5 years |
| [23320845](https://pubmed.ncbi.nlm.nih.gov/23320845/) | 2013 | Case Report | Int J Urology | Spindle cell RMS of prostate in 23-year-old adult; treated within CWS 2002 P study protocol |
| [941356](https://pubmed.ncbi.nlm.nih.gov/941356/) | 1976 | Review | Urology | Shift from radical surgery to chemotherapy + radiation for childhood GU tract RMS; aggressive combined chemotherapy approach recommended |

---

### Liver Sarcoma (Rank 7 | L3 | Research Question)

**TxGNN Score: 99.42%**

Liver sarcoma in this context primarily refers to undifferentiated embryonal sarcoma of the liver (UESL), a rare, highly malignant pediatric hepatic tumor. The dactinomycin connection arises from IRS-based protocols used empirically for UESL. The only identified clinical trial (NWTS-5) targeted Wilms tumor, not liver sarcoma directly, limiting evidence strength.

#### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT00002611](https://clinicaltrials.gov/study/NCT00002611) | Phase 3 | Completed | 3,031 | NWTS-5: Dactinomycin-containing regimen for childhood kidney cancer (Wilms tumor); pediatric abdominal tumour context; indirect safety/efficacy basis for hepatic tumour settings |

#### Literature Evidence (Top 5)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37814737](https://pubmed.ncbi.nlm.nih.gov/37814737/) | 2023 | Case Series | Cureus | Pediatric UESL (10-year-old boy): Neoadjuvant chemotherapy with alternating ifosfamide/doxorubicin/vincristine/D-actinomycin cycles; PRETEXT II, group III staging |
| [23864278](https://pubmed.ncbi.nlm.nih.gov/23864278/) | 2013 | Case Series/Review | Pediatr Surg Int | UESL accounts for 6% of liver tumours; treatment outcomes review from a referral centre; multimodal approach |
| [21671362](https://pubmed.ncbi.nlm.nih.gov/21671362/) | 2011 | Retrospective Cohort | Pediatr Blood Cancer | Dactinomycin + vincristine toxicity in childhood cancer over 40 years; dosing evidence base |
| [9191535](https://pubmed.ncbi.nlm.nih.gov/9191535/) | 1997 | Case Series | Cancer | Liver VOD complicating VAC chemotherapy for RMS (IRS-IV); critical hepatotoxicity safety signal for dactinomycin near-liver use |
| [15143082](https://pubmed.ncbi.nlm.nih.gov/15143082/) | 2004 | Cohort Study | J Clin Oncol | Age as risk factor for VAC-induced hepatopathy; spectrum of liver toxicity from dactinomycin-containing regimens |

---

### Upper Aerodigestive Tract Neoplasm (Rank 8 | L2) and Head & Neck Cancer (Rank 9 | L2)

**TxGNN Scores: 99.16% each | Decision: Proceed with Guardrails**

For head and neck RMS subtypes (non-orbital, non-parameningeal), dactinomycin has Phase 3 evidence from IRS-III and IRS-IV subgroup analyses. For non-RMS squamous or glandular tumours of the upper aerodigestive tract, a 2022 in vitro study demonstrates that low-dose Actinomycin D activates p53 pathways and induces apoptosis in aerodigestive tract cancer cell lines, suggesting a potential cyclotherapy application — but this remains preclinical only.

#### Clinical Trial Evidence (Head and Neck Cancer)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT03382158](https://clinicaltrials.gov/study/NCT03382158) | Registry (N/A) | Recruiting | 3,400 | International PPB/DICER1 registry; includes DICER1-associated head and neck tumours; no randomized treatment comparison — registry/observational only |

#### Literature Evidence (Head & Neck — Top 5)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11408506](https://pubmed.ncbi.nlm.nih.gov/11408506/) | 2001 | Phase 3 RCT | J Clin Oncol | IRS-IV: Risk-based regimens for non-metastatic RMS; head and neck subgroup with VAC backbone |
| [12586800](https://pubmed.ncbi.nlm.nih.gov/12586800/) | 2003 | Phase 3 Subgroup | J Clin Oncol | IRS III/IV subgroup: Localized non-orbital, non-parameningeal head and neck RMS; outcome analysis; chemotherapy = VAC |
| [35267106](https://pubmed.ncbi.nlm.nih.gov/35267106/) | 2022 | In Vitro Study | Apoptosis | Actinomycin D activates p53 targets and induces apoptosis in aerodigestive tract cancer cells in a context-dependent manner; low-dose cyclotherapy hypothesis |
| [1382002](https://pubmed.ncbi.nlm.nih.gov/1382002/) | 1992 | Retrospective Cohort | Clin Otolaryngol | 22 children with non-orbital head/neck RMS (1970–1988); VAC regimen; 21/22 achieved complete clinical remission with initial chemotherapy |
| [6688242](https://pubmed.ncbi.nlm.nih.gov/6688242/) | 1983 | Retrospective Series | Int J Pediatr Otorhinolaryngol | UCLA head/neck RMS series; cyclic multidrug chemotherapy improved survival ~150% vs historical surgical-only controls |

---

### Rare/Orphan Subtypes (Ranks 2–4 | L4 | Research Question)

These three predictions — **botryoid-type embryonal RMS of the vagina**, **extrahepatic bile duct RMS**, and **embryonal extrahepatic bile duct RMS** — share the same biological foundation: all are RMS subtypes where the VAC regimen is mechanistically applicable by analogy. Clinical evidence is sparse or absent, limited to a single 1971 case report for bile duct RMS ([PMID 5563889](https://pubmed.ncbi.nlm.nih.gov/5563889/)). Expert multidisciplinary tumour board review is essential before any treatment decisions in these extremely rare presentations.

---

## Overall Recommendations

| Indication Group | Decision | Key Action |
|-----------------|----------|-----------|
| RRMS (Rank 1) | **Hold** | No mechanistic or clinical basis; monitor TxGNN model retraining |
| Parameningeal embryonal RMS (Rank 5) | **Proceed with Guardrails** | Phase 3 evidence available; consult pediatric oncology; VOD monitoring mandatory |
| Prostate embryonal RMS (Rank 6) | **Proceed with Guardrails** | Multiple case series + Phase 3 RCT indirect support; IRS protocol framework applicable |
| Upper aerodigestive / Head & neck RMS (Ranks 8–9) | **Proceed with Guardrails** | Phase 3 RCT support for RMS subtype; non-RMS H&N remains preclinical only |
| Liver sarcoma (Rank 7) | **Research Question** | Anecdotal UESL use; initiate retrospective case series review |
| Vaginal / Bile duct RMS (Ranks 2–4) | **Research Question** | Extreme rarity; expert case-by-case evaluation only |

**Prerequisite steps for any Canada-market development:**
- File for Health Canada DIN (dactinomycin currently not marketed in Canada)
- Obtain and parse product monograph / package insert for complete warning and contraindication data (Data Gap DG001)
- Retrieve confirmed mechanism of action data from DrugBank API (Data Gap DG002)
- Establish a paediatric hepatology co-management protocol addressing VOD risk
- Align with COG/EpSSG current trial frameworks to avoid protocol duplication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

