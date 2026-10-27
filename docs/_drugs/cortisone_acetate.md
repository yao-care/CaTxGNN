---
layout: default
title: Cortisone Acetate
parent: Model Prediction Only (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cortisone Acetate: predicted new indication Alopecia areata (evidence level L5). Approved use: Not stated in the Canadian licence record. Knowledge-graph indication…"
monitor_inn: "CORTISONE ACETATE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions"]
---

# Cortisone Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Cortisone Acetate: From Autoimmune and Inflammatory Conditions to Alopecia Areata
{: .text-alpha }

## One-Sentence Summary

Cortisone acetate is a glucocorticoid prodrug that has been used for adrenal insufficiency, autoimmune and inflammatory diseases (such as Crohn disease), and certain leukaemias.
The TxGNN model predicts it may be effective for **alopecia areata**, but the supporting evidence is thin: **no registered clinical trials** and only **2 publications**, both case-level reports from 1952.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record. Knowledge-graph indications include adrenocortical insufficiency, Addison disease, autoimmune disease and Crohn disease |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 by the strict rules (no Phase 2/3 RCTs, no observational studies or systematic reviews). The two 1952 case reports are the only human evidence; the underlying analysis rated this prediction L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (a research question, not ready for development) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, cortisone acetate is a prodrug that is converted to cortisol by the enzyme 11-beta-HSD1. Cortisol produces the broad anti-inflammatory and immunosuppressive effects typical of glucocorticoids.

Alopecia areata is an autoimmune condition in which T cells attack the hair follicle. This is mechanistically consistent with the drug's known use in autoimmune and inflammatory diseases. Corticosteroids as a class are an established treatment for alopecia areata (intralesional, topical and short-course systemic).

There are important caveats. Oral cortisone acetate is not used for this purpose today. Systemic steroids tend to be followed by relapse after withdrawal, and they carry significant side effects. The class-level rationale is therefore reasonable, but it does not show that this specific drug is a useful or competitive option.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14908175](https://pubmed.ncbi.nlm.nih.gov/14908175/) | 1952 | Case report/case series | J Invest Dermatol | Treatment of alopecia areata totalis and universalis with cortisone acetate (no abstract available) |
| [14952032](https://pubmed.ncbi.nlm.nih.gov/14952032/) | 1952 | Case report | AMA Arch Dermatol Syphilol | One case of alopecia areata universalis treated with ACTH plus intramuscular cortisone acetate, with post-treatment observations (no abstract available) |

Both reports are historical and lack abstracts, so outcomes cannot be summarised here. The second case also involved ACTH, so the effect of cortisone acetate alone cannot be separated.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00280437 | CORTISONE ACETATE | Not specified | Not specified |

---

## Safety Considerations

The data compiled for this report contain no label-based warnings or contraindications, and no drug interactions were found. The knowledge graph links the drug to contraindications in the following conditions (these are database associations, not label text):

- **Cardiovascular and metabolic:** hypertension, hyperglycaemia
- **Organ disease:** kidney disease, liver disease, gallbladder disease, pyoureter, gastric ulcer
- **Neurological:** epilepsy
- **Infections:** measles, herpes simplex keratitis, anogenital human papillomavirus infection, common wart
- **Pituitary and gonadal deficiency states:** hypopituitarism, growth hormone deficiency and related syndromes, hypogonadotropic hypogonadism (including Kallmann syndrome)

Please refer to the package insert for authoritative safety information. Obtaining it is a blocking gap for safety screening.

---

## Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Alopecia mucinosa | 99.95% | L5 | Plausible anti-inflammatory rationale, but no supporting data |
| 3 | Telogen effluvium | 99.94% | L5 | Usually self-limiting and not immune-mediated, so the rationale is weak |
| 4 | Folliculitis decalvans | 99.94% | L5 | Likely bacterial component, and immunosuppression could worsen infection |
| 5 | Alopecia antibody deficiency | 99.93% | L5 | Immunosuppression is potentially harmful in antibody deficiency |
| 6–8 | Hereditary or genetic hair disorders (three entries) | 99.7–99.93% | L5 | No glucocorticoid-responsive mechanism |
| 9 | Idiopathic steroid-sensitive nephrotic syndrome | 99.48% | L5 | Strong class rationale, but prednisolone is the standard agent |
| 10 | Steroid-resistant nephrotic syndrome | 99.47% | L5 | Resistant to glucocorticoids by definition, so unlikely to help |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia areata prediction has a sound class-level rationale, since corticosteroids are an established therapy. However, the drug-specific evidence is limited to two 1952 case-level reports with no abstracts. There are no registered trials, and better-studied steroids and newer therapies are available. The prediction is best treated as a research question for now.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings and contraindications), which is currently a blocking gap
- Mechanism of action data (for example from DrugBank)
- The approved indications and dosage form for the Canadian licence
- A review of the full text of the 1952 reports, and a modern literature search comparing cortisone acetate with current corticosteroids and newer alopecia areata therapies
- A justification for choosing cortisone acetate over agents such as prednisolone, plus a relapse and adverse-effect risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

