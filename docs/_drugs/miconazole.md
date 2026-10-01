---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 609
evidence_level: L3
indication_count: 1
---

# Miconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

# Miconazole: From Fungal Infections to Acne

## One-Sentence Summary

Miconazole is an imidazole antifungal, marketed in Canada mainly as vaginal and skin products.
The TxGNN model predicts it may be effective for **acne**, but the supporting evidence is weak: **1 clinical trial** (suspended, and testing a combination product) and **4 publications** (one review, one clinical study, one study in a related condition, one in vitro study).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records; the products (vaginal creams, skin cream, powder spray) are topical antifungals |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Miconazole is an azole antifungal, and azoles are known to inhibit fungal CYP51 (lanosterol 14-alpha-demethylase). Its efficacy in fungal skin and mucosal infections is well established.

Published work suggests plausible links to acne:

- **In vitro activity against the acne bacterium:** azole antifungals, including miconazole-class agents, are active against *Propionibacterium (Cutibacterium) acnes*, the bacterium implicated in acne vulgaris. This matters as antibiotic-resistant strains increase.
- **Activity against *Malassezia* (*Pityrosporum*):** these yeasts can cause acne-like folliculitis.
- **Anti-inflammatory effects on skin:** a 2008 review describes miconazole's multiple effects on skin disorders.

Two cautions apply. The very high TxGNN score is a computational prediction, not clinical evidence. Part of the signal may also come from *Malassezia* folliculitis, which is often misdiagnosed as acne, rather than from true acne vulgaris.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Tests a fixed combination of beclomethasone, gentamicin and an azole (likely clotrimazole) cream in contaminated dermatoses. Miconazole is not clearly the tested agent, no results are available, and the population is not specific to acne. Weak indirect support only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small sample) | Skin Res Technol | Split-face clinical and bioinstrumental assessment of mild inflammatory catamenial acne. The available abstract excerpt does not report miconazole-specific results. |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Review of the multiple effects of miconazole nitrate, a long-established imidazole antifungal, on skin disorders. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study | Clin Exp Dermatol | Therapeutic trials in 62 patients with *Pityrosporum* folliculitis, a condition frequently misdiagnosed as acne vulgaris. Indirect relevance to acne. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | Tested azole antifungals against *P. acnes* isolated from acne patients, motivated by rising antibiotic resistance. |

---

## Canada Market Information

Ten authorizations (DINs) are recorded. Five main ones are listed below; the records provide no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2244005 | MONISTAT 3 VAGINAL CREAM |
| 2245546 | MICONAZOLE NITRATE VAGINAL CREAM 2% |
| 2230304 | MICATIN POWDER SPRAY - UNSCENTED 2% |
| 2126567 | MONISTAT DERM CREAM |
| 2126257 | MONISTAT 7 DUAL-PAK |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is a research question rather than a development candidate. The only trial is suspended and tests a combination product, and the literature consists of one small clinical study, one review, one study in a related condition and one in vitro study. The Canadian safety documentation has also not been retrieved, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism-of-action data from DrugBank, to support the mechanistic-link analysis
- Approved indication text and dosage forms for the Canadian licenses
- Clinical evidence in confirmed acne vulgaris (excluding *Malassezia* folliculitis), ideally a controlled trial of miconazole alone
- Confirmation of whether the available topical products are suitable for acne-prone skin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

