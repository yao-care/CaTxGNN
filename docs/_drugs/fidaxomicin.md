---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fidaxomicin: From *C. difficile* Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrocyclic antibiotic approved for *Clostridioides difficile* infection (CDI), notable for its exceptionally low systemic absorption and gut-selective pharmacokinetics.
The TxGNN model predicts it may be effective for **Staphylococcal Scalded Skin Syndrome (SSSS)**, yet **0 clinical trials** and **0 publications** directly support this direction.
Across all 10 top predicted indications, fundamental pharmacokinetic barriers — not lack of *in vitro* activity — represent the central obstacle to repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | *Clostridioides difficile* infection (CDI) |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Fidaxomicin is a macrocyclic antibiotic that selectively inhibits bacterial RNA polymerase (specifically by targeting the sigma subunit initiation complex), with narrow-spectrum activity concentrated against Gram-positive organisms — most notably *Clostridioides difficile* in the gastrointestinal tract. Its defining pharmacokinetic feature is near-zero oral bioavailability (<1%), deliberately engineered so that drug concentrations remain therapeutically high in the gut while systemic exposure stays negligible.

Staphylococcal Scalded Skin Syndrome is caused by *S. aureus* exfoliative toxins (ETs A and B), which disrupt desmoglein-1 in the superficial epidermis and trigger widespread skin blistering. Clinical management requires systemic antibiotics — typically beta-lactamase–resistant penicillins or, for MRSA, vancomycin — capable of reaching therapeutic concentrations in blood and skin tissue. Fidaxomicin does demonstrate *in vitro* inhibitory activity against *S. aureus* including MRSA, which likely explains why TxGNN's graph-based model connects the drug to staphylococcal diseases. However, achieving therapeutic concentrations at the skin is pharmacokinetically impossible via oral dosing given the <1% bioavailability.

This same tension appears across all 10 predicted indications in this Evidence Pack. The TxGNN model correctly identifies biological adjacency between Fidaxomicin's antimicrobial spectrum and various staphylococcal and clostridial disease states, but the drug's pharmacokinetic profile was intentionally designed to prevent systemic distribution. Until a novel delivery route (topical, inhalational, or IV formulation) is developed and validated, the translational gap remains a blocking barrier — not a scientific question about efficacy per se, but a drug delivery constraint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication (Staphylococcal Scalded Skin Syndrome).

---

## Literature Evidence

Currently no related literature available for the predicted indication (Staphylococcal Scalded Skin Syndrome).

> **Note on adjacent indication (S. aureus pneumonia, Rank 8):** One peripheral publication was identified — PMID [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) (2019, *Journal of Hospital Medicine*, Narrative Review) — which mentions Fidaxomicin only in the context of CDI treatment, not S. aureus pneumonia. This reference does not constitute supporting evidence for the repurposing hypothesis.

---

## Taiwan Market Information

Fidaxomicin is currently **not marketed** in Taiwan. No approved licenses are on record as of the data cutoff (2026-04-05).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Package insert warnings and contraindications were not available in this Evidence Pack (Data Gap DG001). The Taiwan FDA (TFDA) product monograph should be retrieved and reviewed before any clinical assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.71%), this score reflects structural proximity in the drug–disease knowledge graph rather than clinical translatability. Fidaxomicin's defining characteristic — near-zero systemic bioavailability — directly contradicts the pharmacokinetic requirement for treating SSSS, a condition that mandates systemic antibiotic exposure to source organs and skin tissue. No clinical trials, observational studies, or directly relevant literature exist to support this repurposing direction. All 10 TxGNN-predicted indications in this pack share the same blocking constraint.

**To proceed, the following is needed:**
- **MOA data** (Data Gap DG002): Confirm RNA polymerase sigma-subunit inhibition mechanism via DrugBank API
- **TFDA package insert** (Data Gap DG001): Retrieve and parse contraindications, boxed warnings, and approved indication text
- **Formulation feasibility assessment**: Evaluate whether a topical or IV formulation of Fidaxomicin is scientifically feasible before any *in vivo* hypothesis can be meaningfully tested
- **PK/PD bridging data**: Document *S. aureus* MIC values against achievable tissue concentrations under any alternative delivery route
- **Regulatory landscape review**: Assess whether Fidaxomicin holds approvals for staphylococcal indications in any jurisdiction (US FDA, EMA, PMDA) that could serve as precedent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

