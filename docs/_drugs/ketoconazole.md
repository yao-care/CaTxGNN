---
layout: default
title: Ketoconazole
parent: Moderate Evidence (L3-L4)
nav_order: 506
evidence_level: L4
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Ketoconazole: From Fungal Infections to Acne

## One-Sentence Summary

Ketoconazole is an azole antifungal, and Canada currently has 4 authorizations for it, including a 2% cream and oral-brand products.
The TxGNN model predicts it may be effective for **acne**, with **1 clinical trial** (small, no phase designation, no results posted) and **14 publications** (mostly reviews, case reports and in vitro studies) currently touching on this direction.
The evidence is early-stage, and the high model score is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antifungal use (the Canadian licence records provided do not list indication text) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoconazole is an azole antifungal, its antifungal activity is established, and mechanistically it may be applicable to acne. The mechanistic link below is inferred from the literature, not from curated DrugBank MOA data.

**Two plausible routes.**
- **Topical, anti-yeast and anti-inflammatory action.** Ketoconazole inhibits Malassezia (Pityrosporum) yeast, which may contribute to follicular inflammation and pustular eruptions. It also has reported anti-inflammatory activity. In vitro work (PMIDs 28111792 and 20045949) suggests it inhibits *Propionibacterium acnes* growth and lipase activity. This may matter as antibiotic-resistant strains become more common.
- **Systemic, androgen lowering.** Systemic ketoconazole inhibits CYP17A1 and steroidogenesis, lowering androgens. This is the rationale cited in the PCOS and hyperandrogenism literature. However, systemic use is limited by hepatotoxicity and adrenal suppression, so topical use is the only realistic repurposing route.

**Important caveats.**
- The single trial found is small, has no phase designation and no posted results, and compares ketoconazole with adapalene.
- The retrieved literature is mostly reviews, case reports and studies of related conditions (Malassezia-related disease, PCOS, Cushing's syndrome), not acne vulgaris efficacy trials.
- The TxGNN score of 0.998 is not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Not applicable | Active, not recruiting | 52 | Randomized comparison of topical ketoconazole 2% cream vs topical adapalene 2% cream in mild comedonal and papulopustular acne, over 12 weeks. It tests whether ketoconazole could be an alternative to a topical retinoid with fewer side effects and better compliance. No results posted. |

---

## Literature Evidence

No randomized controlled trials were retrieved. The table lists the most relevant items, prioritizing direct acne or ketoconazole-related studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | In vitro study | Microbiol Immunol | Ketoconazole inhibits *P. acnes* lipase activity and growth, suggesting it may be an alternative acne treatment given rising antibiotic resistance. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | Tested azole antifungals against *P. acnes* isolates from acne patients, motivated by increasing antibiotic resistance. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study | Clin Exp Dermatol | Pityrosporum folliculitis in 62 patients is often misdiagnosed as acne vulgaris. The report covers diagnosis and therapeutic trials. |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology | Overview of systemic acne treatment (antibiotics and other agents). The retrieved excerpt does not address ketoconazole efficacy. |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | Keio J Med | *P. ovale* is associated with folliculitis, seborrhoeic dermatitis and some atopic dermatitis, which supports a yeast-related mechanism. |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | Pharmaceuticals (Basel) | Reviews adapalene, the active comparator in the ongoing trial, as a first-line acne therapy. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Arch Dermatol | Neonatal papulopustular facial eruptions, often called neonatal acne, may be associated with *Malassezia furfur* infection. |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | FP Essentials | Common infant skin rashes, including neonatal and infantile acne. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clin Evid | PCOS is associated with hirsutism, infertility and acne. |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Review | Pol Tyg Lek | Hormonal treatment of hyperandrogenic manifestations in PCOS reduces acne and seborrhea within about 3 months. The retrieved excerpt does not mention ketoconazole. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2245662 | KETODERM CREAM 2% |
| 2231061 | TEVA-KETOCONAZOLE |
| 2237235 | APO-KETOCONAZOLE |
| 2182920 | NIZORAL |

---

## Safety Considerations

- **Systemic use:** Hepatotoxicity and adrenal suppression limit systemic ketoconazole for acne, so any repurposing would focus on topical use.
- No drug interaction records were found in the query.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the supporting evidence is limited to a small, unphased trial without results and to indirect literature (in vitro work, reviews and related-condition reports). The topical 2% cream is already marketed in Canada, so the idea is feasible to study. It currently remains a research question rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- Trial results from NCT07237763, and confirmation of its exact condition (acne vs another dermatosis)
- A larger randomized Phase 2/3 trial of topical ketoconazole in acne vulgaris with clinical endpoints
- Curated mechanism of action data (DrugBank)
- Health Canada package insert warnings, contraindications and approved indication text
- A route-compatibility assessment confirming that the topical route is the intended one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

