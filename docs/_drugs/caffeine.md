---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From Its Marketed Uses to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is marketed in Canada in several products, including caffeine citrate oral solution and injection and acetaminophen combination products, but the licence records do not state an approved indication.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials** and only **3 publications** (a formulation study, a review and an animal study) touch this direction, and none show treatment benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Caffeine is generally described as an adenosine receptor antagonist, but the Evidence Pack does not confirm this, and it is not linked to nasal disease in any of the retrieved material.

The review of the retrieved evidence found **no credible mechanistic link** to a nasal disease:

- The only intranasal work is a thermo-sensitive nasal gel that uses the nose as a delivery route for caffeine to improve cognition after sleep deprivation. It is not a nasal disease treatment.
- Bitter taste receptor research describes these receptors in the nasal cavity and airways, but it is background pharmacology, not disease treatment.
- The high TxGNN score is a model prediction without clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation/Preclinical | Current Drug Delivery | Nasal thermo-sensitive in situ caffeine gel developed to enhance cognition after sleep deprivation. The nose is used as a delivery route, not as a disease target. |
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in the nasal cavity and lungs, among other tissues. It reviews receptor pharmacology, not caffeine treatment of nasal disease. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced tobacco-carcinogen-induced lung tumours in rats. Not a nasal disease and not a human study. |

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and approved indication text are not recorded for these entries.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2496771 | PEYONA | Not listed | Not listed |
| 2526751 | CAFFEINE CITRATE ORAL SOLUTION USP | Not listed | Not listed |
| 2526778 | CAFFEINE CITRATE INJECTION USP | Not listed | Not listed |
| 2254468 | TYLENOL ULTRA RELIEF | Not listed | Not listed |
| 2544687 | EXTRA STRENGTH TYLENOL DAYTIME RELIEF | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The nasal cavity disease prediction rests on the model score alone. There are no clinical trials, the literature does not test caffeine as a treatment for any nasal condition, and no mechanistic link was identified.

**To proceed, the following is needed:**
- A defined nasal or upper-airway disease target with a plausible mechanism, since "nasal cavity disease" is too broad to test
- Mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Approved indication text and dosage forms for the Canadian licences

**Other predictions in this pack:** Among the ten predicted indications, only **hypnic headache** reached the S1 stage (Research Question). Reviews report caffeine, such as strong coffee on waking, as a first-line therapy based on case reports and small series, with no controlled trials. It would be a better starting point for further evaluation than nasal cavity disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

