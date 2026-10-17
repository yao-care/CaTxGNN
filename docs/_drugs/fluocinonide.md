---
layout: default
title: Fluocinonide
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Fluocinonide: predicted new indication Alopecia mucinosa (evidence level L5). Approved use: Inflammatory skin conditions (atopic dermatitis, contact dermatitis…"
monitor_inn: "FLUOCINONIDE"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "alopecia areata", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome"]
---

# Fluocinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fluocinonide: From Dermatitis and Other Inflammatory Skin Conditions to Alopecia Mucinosa

## One-Sentence Summary

Fluocinonide is a high-potency topical corticosteroid, originally used for inflammatory skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **alopecia mucinosa**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin conditions (atopic dermatitis, contact dermatitis, seborrheic dermatitis, discoid lupus erythematosus, among others) |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

*Note: The Canadian licence records compiled for this report contain no approved-indication text. The original indications above come from the TxGNN knowledge graph.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluocinonide is a high-potency topical corticosteroid with anti-inflammatory, immunosuppressive and antiproliferative effects. Its efficacy in inflammatory skin disease is established, and mechanistically it may be applicable to alopecia mucinosa.

Alopecia mucinosa (follicular mucinosis) is an inflammatory disorder of the hair follicle. Topical corticosteroids are used empirically in clinical practice, so the link is biologically plausible. However, the only support in the data compiled for this report is the high TxGNN score (0.996). No trials or publications were provided, so the prediction remains a hypothesis.

**Other predicted indications (all with no or minimal evidence):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Telogen effluvium | 99.61% | L5 | Usually non-inflammatory, so limited mechanistic relevance |
| 3 | Alopecia areata | 99.59% | L4 | Biologically coherent (autoimmune, T-cell-mediated), but not directly tested with fluocinonide |
| 4 | Quinquaud's folliculitis decalvans | 99.58% | L5 | Possible adjunct role for inflammation; no direct evidence |
| 5 | Hereditary hypotrichosis with recurrent skin vesicles | 99.56% | L5 | No clear inflammatory driver; likely reflects network proximity |
| 6 | Alopecia antibody deficiency | 99.51% | L5 | Primary problem is immune deficiency; immunosuppression could be counterproductive |
| 7 | Alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 99.49% | L5 | No plausible mechanistic effect on the underlying cause |

Of the alternatives, alopecia areata has the strongest biological rationale and the most related material, so it may be the more productive research question.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for alopecia mucinosa.

For the alternative prediction alopecia areata, one loosely related trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicentre prospective study comparing before-and-after photos across treatment groups in central centrifugal cicatricial alopecia (a scarring alopecia distinct from alopecia areata). Fluocinonide is not confirmed as the studied intervention. |

---

## Literature Evidence

Currently no related literature is available for alopecia mucinosa.

For the alternative prediction alopecia areata:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | Journal of the American Academy of Dermatology | Four cases of congenital alopecia areata followed for 3 to 5 years, with prolonged quiescent periods; treatments included minoxidil 2% and a range of topical agents. It does not directly test fluocinonide. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00716863 | LYDERM | Not listed | Not listed |
| 02236997 | LYDERM | Not listed | Not listed |
| 02236996 | LYDERM | Not listed | Not listed |
| 00598933 | TIAMOL CREAM 0.05% | Cream | Not listed |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease links, not from label text):
- Metabolic and endocrine conditions: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis
- Adrenal conditions: adrenal gland hyperfunction, Cushing syndrome
- Pituitary and gonadal conditions: hypopituitarism and other pituitary hormone deficiencies, Sheehan syndrome, growth hormone deficiency forms, hypogonadotropic hypogonadism and Kallmann syndrome
- Thymus gland disease

These are consistent with the systemic effects of corticosteroids, which can occur with extensive or prolonged topical use.

**Drug Interactions:** 64 potential interactions were identified, but none have a severity level assigned. Examples include other corticosteroids (triamcinolone, prednisone, budesonide, dexamethasone, fluticasone), cyclosporine, clopidogrel, acetylsalicylic acid, ibuprofen, omeprazole, lansoprazole, famotidine, cetirizine, fexofenadine, clotrimazole, bupropion and salbutamol.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for alopecia mucinosa is supported only by a model score (L5), with no trials or publications. The mechanism is plausible but untested. Of the predicted indications, alopecia areata is the most promising research question (L4), though the available evidence does not test fluocinonide directly.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A systematic literature search on topical corticosteroids in follicular mucinosis and alopecia areata
- Confirmation of whether fluocinonide was the intervention in NCT04207931
- Dosage form and approved indication details for the Canadian licences
- Assessment of route compatibility and of systemic absorption risk for scalp use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

