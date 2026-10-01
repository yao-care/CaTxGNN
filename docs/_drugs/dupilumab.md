---
layout: default
title: Dupilumab
parent: Model Prediction Only (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is an IL-4Rα-blocking antibody, an established treatment for type 2 inflammatory disease such as atopic dermatitis and asthma. The TxGNN model predicts it may be useful for **bronchitis**, but this rests on **1 indirect clinical trial** (chronic rhinosinusitis, not bronchitis) and **6 publications**, none of which studies bronchitis directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (the pack's rationale notes it is a labelled use; the Canadian licence records carry no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (indirect and mechanistic support only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dupilumab blocks IL-4Rα, the shared receptor subunit for IL-4 and IL-13. These are the key signals in type 2 inflammation. This mechanism is well established in atopic dermatitis and in asthma. It also has support in COPD with an eosinophilic phenotype, according to the review cited in the pack. The mechanism-of-action field in the pack is empty, so this description is based on the pack's rationale and the literature.

The link to bronchitis is plausible only for a subset. Eosinophilic or type 2 bronchitis, including pediatric plastic bronchitis, could respond to the same pathway. Bronchitis in general covers many other causes, including viral infection and smoking-related chronic bronchitis, and there is no reason to expect IL-4/IL-13 blockade to help those.

All support is indirect. It comes from asthma and COPD studies, and the one listed trial is an upper-airway study. Nothing provided tests dupilumab in bronchitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps. It is not a bronchitis trial and only supports a "unified airway" type 2 rationale. No results were provided. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Open-label extension of RCT | Lancet Respir Med | TRAVERSE: long-term safety and efficacy of dupilumab beyond 1 year in moderate-to-severe asthma |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic review / meta-analysis | J Asthma | Pooled randomized trials of dupilumab versus placebo in uncontrolled asthma |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberc Respir Dis | Pharmacologic options for preventing COPD exacerbations, including novel agents |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Prospective clinical study | Chest | Anti-T2 biologic effects on lung ventilation (MRI) in prednisone-dependent asthma |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Managing asthma with smoking-induced airway disease, including chronic bronchitis; such patients are excluded from most trials |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review | Pediatr Pulmonol | Novel therapies for eosinophilic pediatric plastic bronchitis. This is the only bronchitis-specific item; no abstract was provided. |

---

## Canada Market Information

| Licence No. | Product Name |
|---------|------|
| 2510049 | DUPIXENT |
| 2524252 | DUPIXENT |
| 2492504 | DUPIXENT |
| 2470365 | DUPIXENT |

Dosage form and approved-indication text are empty in the provided records. The pack lists TFDA among its inputs, and these 7-digit numbers do not look like 8-digit Canadian DINs. Please verify them against the Health Canada Drug Product Database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible for type 2 (eosinophilic) bronchitis. However, no bronchitis-specific trial exists, and the supporting evidence comes from asthma, COPD and one upper-airway study. Because the evidence is only indirect, this stays a research question rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- Define the target phenotype (eosinophilic or type 2 bronchitis, pediatric plastic bronchitis) rather than "bronchitis" in general.
- Find or run a bronchitis-specific study. The evidence so far is limited to case-level or review-level reports.
- Obtain the Health Canada package insert warnings and contraindications. This gap is blocking for safety screening.
- Confirm the original indication and licence data from the Canadian records, and confirm the DINs.
- Obtain the mechanism-of-action record from DrugBank.

Note that the prediction ranked second, atopic dermatitis, is an already labelled use with Phase 3 RCT support (for example NCT02260986, n=740). It confirms a known indication rather than offering new repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

