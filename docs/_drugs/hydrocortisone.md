---
layout: default
title: Hydrocortisone
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Adrenal Insufficiency and Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid originally used for adrenal insufficiency (including Addison disease), autoimmune and inflammatory conditions such as Crohn disease, and certain leukaemias.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **1 clinical trial** (in which hydrocortisone was only the low-potency comparator) and **20 publications** (mostly case reports, older cohorts and unrelated articles) currently linked to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenal insufficiency / Addison disease, Crohn disease and inflammatory bowel disease, autoimmune disease, acute lymphoblastic leukaemia (the data compiled for this report does not include approved indication text for the Canadian products) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (as scored in the compiled data; see the note below, as the evidence is weaker than this label suggests) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, hydrocortisone is a glucocorticoid with anti-inflammatory and immunosuppressive effects, and its efficacy in adrenal insufficiency and inflammatory or autoimmune disease is well established.

Alopecia areata is a T-cell-mediated autoimmune disorder in which the immune system attacks hair follicles. Suppressing local immune activity is therefore mechanistically plausible. Topical and intralesional corticosteroids are already used in practice for this condition, and historical reports from the 1950s to 1970s describe intralesional hydrocortisone injections.

An important caveat: the only Phase 3 trial used hydrocortisone 1% cream as the low-potency comparator against clobetasol propionate 0.05%. It therefore mainly supports clobetasol's performance and does not demonstrate that hydrocortisone itself is effective. The "L1" label should be read with this in mind. In practice, the evidence for hydrocortisone specifically is closer to historical or indirect support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomised trial in children with alopecia areata comparing clobetasol propionate 0.05% cream with hydrocortisone 1% cream (2002–2003). Hydrocortisone served as the low-potency active comparator, so the trial mainly addresses clobetasol's superiority. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Clobetasol 0.05% vs hydrocortisone 1% for alopecia areata in children (publication of the Phase 3 trial above) |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Cohort | Medical Times | Treatment of alopecia areata with cortisone, hydrocortisone and analogues |
| [14158890](https://pubmed.ncbi.nlm.nih.gov/14158890/) | 1963 | Cohort | Actas Dermo-Sifiliograficas | Comparison of intralesional injection of different corticoids in alopecia areata |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Cohort | Vestnik Dermatologii i Venerologii | Intracutaneous hydrocortisone injections in alopecia areata and total alopecia |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review | J Med Soc New Jersey | Overview of alopecia areata and other common scalp problems |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | J Am Acad Dermatol | Four cases of congenital alopecia areata, treated with minoxidil and a range of topical agents |
| [28094416](https://pubmed.ncbi.nlm.nih.gov/28094416/) | 2017 | Case report | Tierarztl Prax Ausg K | Canine alopecia areata in which topical tacrolimus and hydrocortisone aceponate were ineffective |
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Clinical report | Przeglad Dermatologiczny | Intralesional hydrocortisone acetate suspension injections in severe alopecia areata |
| [14376206](https://pubmed.ncbi.nlm.nih.gov/14376206/) | 1955 | Clinical report | Actas Dermo-Sifiliograficas | First clinical tests of local hydrocortisone therapy for alopecia areata |
| [24326563](https://pubmed.ncbi.nlm.nih.gov/24326563/) | 2013 | Preclinical | J Investig Dermatol Symp Proc | Parathyroid hormone agonists in a mouse model of alopecia areata (not hydrocortisone-specific) |

Several other retrieved articles are tangential (for example, an anaphylaxis case with triamcinolone, a self-medication survey, and unrelated case reports) and are not listed here.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00030619 | SOLU-CORTEF | Not specified | Not specified |
| 02469421 | SANDOZ HYDROCORTISONE | Not specified | Not specified |
| 00030929 | CORTEF | Not specified | Not specified |
| 02524465 | AURO-HYDROCORTISONE | Not specified | Not specified |
| 01954210 | PRAMOX HC LOTION | Lotion (per product name) | Not specified |

In total, 16 single-ingredient authorisations are valid, covering systemic brands (Solu-Cortef, Cortef), generics and several topical or rectal products (for example Pramox HC, Proctol, Teva-Proctosone, Vioform Hydrocortisone).

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: hypertension, epilepsy, gastric ulcer, kidney disease, liver disease, gallbladder disease, hyperglycaemia, measles, herpes simplex keratitis, anogenital HPV infection, common warts, and several pituitary or growth hormone deficiency disorders.
- **Drug Interactions**: 100 interactions were identified. Examples include **Adalimumab (major)**, and moderate interactions with zidovudine, isotretinoin, acarbose, acebutolol, acetazolamide, ketorolac, ibuprofen, nifedipine, ethinylestradiol, aldesleukin, alemtuzumab, and certain live or inactivated vaccine antigens. Formoterol and salbutamol show minor interactions.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high and the mechanism is plausible, but the only controlled trial used hydrocortisone as a weak comparator, so it does not demonstrate hydrocortisone's own efficacy in alopecia areata. Other supporting literature is mostly historical case series. Higher-potency corticosteroids such as clobetasol are already the more reasonable option in this setting. The other predicted indications (for example alopecia mucinosa, telogen effluvium, folliculitis decalvans) have little or no supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A critical review of the 2014 RCT's data on the hydrocortisone arm, or a head-to-head or placebo-controlled trial of hydrocortisone in alopecia areata
- Comparison with established corticosteroid options to define whether hydrocortisone offers any advantage (for example, in a specific population such as children or facial involvement)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

