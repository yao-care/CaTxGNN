---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 9
---

# Acetic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Acetic Acid: From Marketed Product Use to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is marketed in Canada under 20 licences, but the licence data records no approved indication. The product names listed suggest hemodialysis acid concentrates. The TxGNN model predicts it may be effective for **post-bacterial disorder**, but the 18 matched clinical trials are keyword hits on unrelated conditions and there are **0 publications** for this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data (listed product names suggest hemodialysis acid concentrates) |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Acetic acid is known to have topical antibacterial and antifungal activity through acidification, and this is the only biological rationale that can be drawn on.

"Post-bacterial disorder" is a vague umbrella term, and no mechanism links acetic acid to a defined post-bacterial pathology. The very high score (rank 685 in the model) is therefore best read as a statistical association in the knowledge graph, not a mechanistic finding.

Among the other predictions, **tinea corporis** (a fungal skin infection) has the most biologically plausible link. It is discussed in the conclusion.

---

## Clinical Trial Evidence

The 18 matched trials are keyword matches. All are Phase NA, Phase 1 or Phase 2 (none Phase 3), and none tests acetic acid as a treatment for a post-bacterial disorder. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04824261](https://clinicaltrials.gov/study/NCT04824261) | NA | Unknown | 100 | 4% boric acid vs clotrimazole in otomycosis. Topical ear antimicrobial setting; the condition is fungal, not post-bacterial. |
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | NA | Completed | 10 | Photodynamic therapy as an adjunct to endodontic treatment. Acetic acid is not clearly the intervention. |
| [NCT04036318](https://clinicaltrials.gov/study/NCT04036318) | N/A | Completed | 3022 | Presumptive periodic STI treatment strategy in high-risk populations. Does not test acetic acid. |
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | NA | Completed | 126 | Apple cider vinegar plus metformin in type 2 diabetes. Vinegar contains acetic acid, but the condition is metabolic. |
| [NCT07048028](https://clinicaltrials.gov/study/NCT07048028) | NA | Recruiting | 90 | Chitosan vs sodium hypochlorite combinations as root-canal irrigants. Antibacterial irrigation only. |
| [NCT03619161](https://clinicaltrials.gov/study/NCT03619161) | NA | Completed | 58 | Bathroom cleaning vs bleach baths in eczema. Not a post-bacterial disorder. |
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | Completed | 28 | Safety of topical SoftOx Biofilm Eradicator in chronic leg wounds. |
| [NCT04657757](https://clinicaltrials.gov/study/NCT04657757) | NA | Completed | 16 | Bacterial adhesion and bactericidal effect on implant restoration materials (ex vivo). |
| [NCT02872675](https://clinicaltrials.gov/study/NCT02872675) | NA | Completed | 17 | Prebiotic supplementation and gut bacterial metabolites (short-chain fatty acids) in adults with and without exercise-induced bronchoconstriction. Indirect. |
| [NCT06612164](https://clinicaltrials.gov/study/NCT06612164) | NA | Completed | 65 | Kefir consumption and health outcomes in healthy adults. Acetic acid is at most a fermentation by-product. |

---

## Literature Evidence

Currently no related literature available for post-bacterial disorder.

---

## Canada Market Information

Five of the 20 licences are shown. The licence records provide no dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2254085 | ACID CONCENTRATE A1230 | Not listed | Not listed |
| 2415496 | SELECTBAG ONE (AX 2525 G) | Not listed | Not listed |
| 2414902 | SELECTBAG ONE (AX 325 G) | Not listed | Not listed |
| 2415461 | SELECTBAG ONE (AX 250 G) | Not listed | Not listed |
| 2414821 | SELECTBAG ONE (AX 150 G) | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found. Separately, the evidence retrieved for tinea corporis includes a case series of burns caused by folk vinegar remedies (Korea, 2023). This points to skin irritation and chemical burn risk when concentration is not controlled.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for post-bacterial disorder is supported only by the model score. The indication is too vague to map to a mechanism, there are no relevant trials, and there is no literature. The safety review also cannot proceed until the package insert is obtained.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Mechanism of action data from DrugBank
- The approved indication and dosage form for each Canadian licence, to establish the original use
- A more specific disease definition in place of "post-bacterial disorder"
- Consideration of **tinea corporis** as a better-founded research question. The evidence is indirect: historical 1940s tinea capitis reports using dilute acetic acid with iodine, vinegar-based regimens, and in vitro onychomycosis models. There are no registered trials. A small controlled study with a defined acetic acid concentration would be a feasible next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

