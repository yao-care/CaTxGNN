---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 614
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-05
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
description: "Miconazole: predicted new indication 痤瘡 (acne (disease)) (evidence level L4). In Canada: 10 DINs (9 marketed)"
---

# Miconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Miconazole: 痤瘡 (acne (disease))
{: .text-alpha }

## One-Sentence Summary

Miconazole is an imidazole antifungal marketed in Canada in several topical and vaginal products.
The TxGNN model predicts it may be useful for **acne (disease)**, with a prediction score of **0.9954**.
Currently there are **no registered clinical trials** and **4 publications** (one review, one small split-face clinical study, one study of an acne-like condition, one in vitro study). None of them is a clinical study of miconazole in acne itself, so the evidence level is **L4**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | 痤瘡 (acne (disease)) |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (marketed DINs: 9 of 10; cancelled: 1) |
| Number of DINs | 10 (marketed: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for miconazole: "Miconazole is an antifungal drug. […] Miconazole inhibits the enzyme cytochrome P450 14α-demethylase which leads to inhibition of ergosterol synthesis, an essential component of the fungal cell membrane. Miconazole also affects the synthesis of triglycerides and fatty acids and inhibits oxidative and peroxidative enzymes, increasing the amount of reactive oxygen species within the cell." ([DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a), label version 2026-01-08; accessed 2026-11-19.) Based on general knowledge, miconazole is an imidazole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase). It also has some activity against Gram-positive bacteria and reported anti-inflammatory effects on skin. These points come from general pharmacology and the cited literature, not from the supplied mechanism field.

Acne involves *Cutibacterium (Propionibacterium) acnes* and skin inflammation. An in vitro study (PMID 20045949) found that azole antifungals, including miconazole, are active against *P. acnes* isolates from patients with acne vulgaris. A review (PMID 18627330) describes miconazole's antibacterial and anti-inflammatory effects on skin disorders. Malassezia (Pityrosporum) folliculitis, which looks like acne and responds to azoles, gives a further plausible link (PMID 8593718).

The high TxGNN score is a computational prediction only and is not clinical evidence. The supporting data are indirect: in vitro activity, a narrative review, and studies of related conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Reviews miconazole's antifungal, antibacterial and anti-inflammatory effects on skin disorders; no clinical study in acne |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small) | Skin Res Technol | Split-face bioinstrumental assessment in mild inflammatory catamenial acne; the abstract provided does not state the treatment or results, so it cannot be taken as support for miconazole |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study / therapeutic trial | Clin Exp Dermatol | 62 patients with Pityrosporum folliculitis, an acne-mimicking condition that is often misdiagnosed as acne vulgaris; not true acne |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | Azole antifungals were tested for in vitro activity against *P. acnes* isolated from acne vulgaris patients |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244005 | MONISTAT 3 VAGINAL CREAM | Not specified | Not specified |
| 02245546 | MICONAZOLE NITRATE VAGINAL CREAM 2% | Not specified | Not specified |
| 02230304 | MICATIN POWDER SPRAY - UNSCENTED 2% | Not specified | Not specified |
| 02126567 | MONISTAT DERM CREAM | Not specified | Not specified |
| 02126257 | MONISTAT 7 DUAL-PAK | Not specified | Not specified |

Nine of the ten licences are valid and one (MONICURE COMBO) is cancelled. Only five are listed here.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. Most of those listed are Moderate, for example paclitaxel, fentanyl, acalabrutinib, nifedipine, ethinylestradiol, alfentanil, alfuzosin, aliskiren, estradiol, alosetron, alprazolam, amiodarone, amitriptyline, amlodipine and hydrocodone. Minor ones include dolutegravir, loratadine, amphotericin B and ambrisentan.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4. The supporting data are one review of miconazole's skin effects, in vitro activity against *P. acnes*, and studies of related conditions, with no clinical study of miconazole in acne. The high TxGNN score alone does not justify moving forward.

**To proceed, the following is needed:**
- Controlled clinical studies of topical miconazole in acne vulgaris
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications
- Review of the dosage forms and routes available in Canada against those needed for acne

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

