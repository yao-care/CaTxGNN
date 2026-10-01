---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 894
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Tetrabenazine is a monoamine-depleting drug marketed in Canada, and it is used to reduce chorea in Huntington's disease. The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease** (score 99.90%). However, there are **0 clinical trials** and **20 publications**, and none of the publications mention tetrabenazine, so this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chorea in Huntington's disease (inferred from the drug's linked trial record; the Canadian license records carry no indication text) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Tetrabenazine is a reversible VMAT2 inhibitor that depletes presynaptic monoamines in the central nervous system, which is why it is used for hyperkinetic movement disorders.

The predicted disease is a genetic disorder of cyst formation. It involves defective polycystin-1 maturation (GANAB-related) and produces kidney and liver cysts. I could not identify a plausible link between VMAT2 inhibition and this process.

All 20 retrieved papers cover the disease itself: guidelines, genetics and reviews. None mention tetrabenazine. The high score (0.999) reflects a graph-based association without supporting biology, so it should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The papers below describe the disease and its management. None study tetrabenazine, and none are RCTs. Study types come from the pack's classification; papers it left unclassified are labelled from their titles and abstracts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG guideline on focal liver lesions, including hepatic cystic lesions and polycystic liver disease |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guidelines on diagnosis and management of cystic liver diseases, including polycystic liver disease |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | ADPKD as a systemic disorder, with liver cysts among its extrarenal complications |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic liver disease as the most common extrarenal manifestation of ADPKD; tolvaptan can slow renal decline |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap between ADPKD and polycystic liver disease, including GANAB |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of polycystic kidney and liver diseases; defective primary cilia function is central |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annu Rev Pathol | Mechanisms of hepatic cystogenesis and advances in treatment |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepat Med | Pathophysiology, diagnosis and treatment of polycystic liver disease |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Basic/genetic study | J Clin Invest | Exome sequencing identifies new isolated polycystic liver disease genes and polycystin-1 effectors |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Retrospective case series | Ann Transplant | Outcomes of organ transplantation in 9 patients with polycystic liver and kidney disease |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2402424 | PMS-TETRABENAZINE |
| 2407590 | APO-TETRABENAZINE |
| 2199270 | NITOMAN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score. There are no clinical trials, no publications mentioning tetrabenazine, and no identified mechanistic link between VMAT2 inhibition and polycystin-related cyst formation. The other nine predicted indications are also model-only (L5) with no mechanistic link; the one trial attached to any of them studies tetrabenazine in Huntington's disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data, for example from DrugBank
- A preclinical or mechanistic rationale connecting monoamine depletion to cyst formation, such as in vitro or animal cyst models
- Safety data for tetrabenazine in patients with renal or hepatic impairment, who would be the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

