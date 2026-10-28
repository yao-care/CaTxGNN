---
layout: default
title: Micafungin
parent: Moderate Evidence (L3-L4)
nav_order: 613
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
description: "Micafungin: predicted new indication Urinary tract infection (evidence level L3). Approved use: Esophageal candidiasis, candidemia, disseminated candidiasis"
monitor_inn: "MICAFUNGIN"
predicted_indications: ["urinary tract infection (disease)"]
---

# Micafungin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Micafungin: From Esophageal Candidiasis and Candidemia to Urinary Tract Infection
{: .text-alpha }

## One-Sentence Summary

Micafungin is an echinocandin antifungal originally used to treat esophageal candidiasis, candidemia, and disseminated candidiasis.
The TxGNN model predicts it may be effective for **urinary tract infection** (mainly Candida-related), with **no registered clinical trials** but **12 publications** (cohort studies, case series, and case reports) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia, disseminated candidiasis |
| Predicted New Indication | Urinary tract infection |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L3 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the known class mechanism, micafungin is an echinocandin that inhibits 1,3-beta-D-glucan synthase and disrupts fungal cell wall synthesis in Candida species. This is an inference from the drug class, not from the compiled data.

Its efficacy in invasive Candida infections is established. Candida urinary tract infection (candiduria) is caused by the same genus, so antifungal activity is mechanistically plausible.

The main limitation is pharmacokinetic. Echinocandins have low urinary excretion of active drug. One study (PMID 27424599) reports that urinary micafungin levels were nevertheless sufficient against Candida spp. This suggests a possible role, particularly for fluconazole-resistant species such as *C. glabrata*, *C. krusei*, and *C. auris*, where standard options are limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Cohort | Pediatr Int | Micafungin for hospital-acquired Candida UTI in critically ill children; treatment success rates analysed by species |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Cohort | Int Urol Nephrol | Candiduria elimination rates in hospitalized patients treated with micafungin |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Pharmacokinetic study | Int J Antimicrob Agents | Six UTI cases successfully treated; urinary micafungin levels sufficient against Candida spp., including fluconazole-resistant strains |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case series | Med Mycol Case Rep | Five candiduria cases treated with micafungin; fungal clearance within 30 days of treatment completion |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case report | Transpl Infect Dis | Chronic *C. krusei* UTI eradicated with increased-dose micafungin in a liver and kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case report | Front Pediatr | *C. glabrata* urinary infection in a premature neonate treated with micafungin |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case report | Med Mycol Case Rep | Renal fungus ball from *C. glabrata* (micafungin-sensitive) treated with antifungal therapy plus endoscopic extraction |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Case report | J Pharm Health Care Sci | *C. glabrata* pyelonephritis and bacteraemia in a patient on an SGLT2 inhibitor, successfully treated with micafungin |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case report | Cureus | *C. auris* UTI in a nursing home patient with multiple comorbidities |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Cohort | Antimicrob Agents Chemother | Multi-institutional study showing overtreatment of asymptomatic candiduria, a caution against indiscriminate antifungal use |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02532360 | MICAFUNGIN SODIUM FOR INJECTION | Not specified | Not specified |
| 02294222 | MYCAMINE | Not specified | Not specified |
| 02311054 | MYCAMINE | Not specified | Not specified |
| 02547236 | MICAFUNGIN SODIUM FOR INJECTION | Not specified | Not specified |
| 02524961 | MICAFUNGIN SODIUM FOR INJECTION | Not specified | Not specified |

Eight valid single-ingredient licences are on record in total; the first five are listed here.

---

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): kidney disease and pyoureter are linked to micafungin as contraindication-type associations. This deserves attention given the intended urinary tract use.
- **Drug Interactions** (5 moderate-level interactions identified):
  - Amphotericin B
  - Nitisinone
  - Everolimus
  - Ribociclib
  - Sirolimus

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence consists mostly of small cohort studies, case series, and case reports, with no registered clinical trials. Echinocandins are not routinely recommended for candiduria because of low urinary concentrations, and the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction is biologically plausible but remains a research question rather than a ready-to-act indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Controlled studies, or prospective trials, comparing micafungin with standard therapy in Candida UTI, especially fluconazole-resistant species
- Further urinary pharmacokinetic data to confirm adequate drug levels at the infection site
- Clarification of the kidney disease and pyoureter associations
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

