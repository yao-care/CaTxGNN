---
layout: default
title: Pimecrolimus
parent: High Evidence (L1-L2)
nav_order: 736
evidence_level: L2
indication_count: 4
last_modified_at: 2026-10-13
description: "Pimecrolimus: predicted new indication Seborrheic dermatitis (evidence level L2). Approved use: Atopic dermatitis (atopic eczema)"
monitor_inn: "PIMECROLIMUS"
predicted_indications: ["seborrheic dermatitis", "dermatitis", "exanthem (disease)", "acrodermatitis chronica atrophicans"]
---

# Pimecrolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus is a topical calcineurin inhibitor, originally used to treat atopic dermatitis (atopic eczema).
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
with **1 completed Phase 2 clinical trial** and **18 publications** (including 2 systematic reviews of randomized trials) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (atopic eczema) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known class information, pimecrolimus is a topical calcineurin inhibitor. It blocks T-cell activation and the release of inflammatory cytokines such as IL-2, IL-4, interferon-gamma and TNF-alpha, and it also inhibits mast cell degranulation.

Atopic dermatitis and seborrheic dermatitis are both chronic, relapsing inflammatory skin diseases. Seborrheic dermatitis involves an inflammatory response to *Malassezia* yeast on the skin in sebum-rich areas, so a non-steroidal topical anti-inflammatory agent is biologically plausible. Calcineurin inhibitors may also have some antifungal activity against *Malassezia*. This is attractive because long-term topical corticosteroid use on the face carries well-known adverse effects.

The very high TxGNN score is consistent with the clinical signal, but it remains a model prediction. The strength of this case comes from the published trials and reviews.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomized, double-blind, active-comparator exploratory study of Elidel (pimecrolimus) in seborrheic dermatitis |

This is the only registered trial for this indication. It is a Phase 2 study, and no Phase 3 confirmation is available.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream appears well tolerated and effective for seborrheic dermatitis, with efficacy comparable to comparators such as corticosteroids |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic review of RCTs | Cureus | Critical review of the efficacy and safety of pimecrolimus in facial seborrheic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Review of topical treatments (antifungals, keratolytics, corticosteroids) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors are a safer alternative to corticosteroids, which have limited use because of long-term adverse effects |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Review | J Cutan Med Surg | Review of off-label uses of topical pimecrolimus, focusing on published RCTs |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | Am J Clin Dermatol | Pimecrolimus 1% cream was effective and well tolerated in resistant facial seborrheic dermatitis |
| [17982237](https://pubmed.ncbi.nlm.nih.gov/17982237/) | 2007 | Open-label study | J Korean Med Sci | 20 Korean patients applied pimecrolimus 1% cream for 4 weeks; study assessed efficacy and tolerability in facial seborrheic dermatitis |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | Int J Clin Pract | Pimecrolimus selectively targets T cells and mast cells, inhibiting cytokine release |
| [17020422](https://pubmed.ncbi.nlm.nih.gov/17020422/) | 2006 | Review | Expert Opin Pharmacother | Pimecrolimus has potential in inflammatory skin diseases beyond atopic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of the current status and therapeutic options for facial seborrheic dermatitis |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247238 | ELIDEL | Not specified | Not specified |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The knowledge graph links pimecrolimus with caution in viral and infectious skin conditions, including common wart, epidermodysplasia verruciformis, anogenital human papillomavirus infection, herpes simplex infection, herpes simplex dermatitis, herpes zoster, chickenpox, infectious mononucleosis and chronic Epstein-Barr virus infection. It also lists lymphatic system disease, Netherton syndrome and ichthyosis linearis circumflexa.
- **Drug Interactions**: The interaction screen returned 100 potential interacting drugs, but none had a severity level assigned. Examples include corticosteroids (prednisone, hydrocortisone, triamcinolone, budesonide), proton pump inhibitors (omeprazole, pantoprazole), simvastatin, metformin, and tetracycline-class antibiotics (doxycycline, tetracycline). These need clinical review.
- **Class-level guardrails**: Topical calcineurin inhibitors carry a boxed warning about long-term safety (theoretical malignancy risk). A 2023 meta-analysis ([36370744](https://pubmed.ncbi.nlm.nih.gov/36370744/)) examined cancer risk with topical calcineurin inhibitors. Use is generally second-line, and should be avoided in immunocompromised patients and in children under 2 years.

Label warnings and contraindications for the Canadian product were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 randomized, double-blind trial (n=113) and two systematic reviews of RCTs support pimecrolimus in seborrheic dermatitis, with a plausible anti-inflammatory mechanism shared with its approved indication. The evidence stays at Phase 2 level, and class-level malignancy and infection warnings call for careful use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing and blocking for safety screening)
- Detailed mechanism of action data from DrugBank
- Results and outcome data from NCT00403559, and ideally a Phase 3 confirmatory trial
- Approved indication text, dosage form and manufacturer for the Canadian DIN
- Severity grading of the 100 flagged drug interactions
- A long-term safety monitoring plan, especially for facial and chronic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

