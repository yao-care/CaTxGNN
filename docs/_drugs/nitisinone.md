---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone (NTBC) is an HPPD inhibitor whose established clinical role is managing hereditary tyrosinemia type 1 (HT-1), preventing accumulation of the toxic tyrosine-pathway metabolites that damage the liver and kidneys. The TxGNN model predicts a strong signal for **Renal Tubular Acidosis**, supported by **2 publications** and **0 registered clinical trials** — evidence that describes a known complication-improvement within HT-1 patients rather than an independent new disease population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT-1) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), blocking the tyrosine catabolic pathway upstream and preventing formation of toxic intermediates such as fumarylacetoacetate and succinylacetone.

In untreated or inadequately treated HT-1 patients, these metabolites accumulate in the proximal renal tubules and cause Fanconi syndrome-type renal tubular acidosis, alongside the well-known hepatic toxicity. Because nitisinone blocks the metabolite generation directly, its renal tubular benefit is a pharmacologically direct and well-understood extension of its existing mechanism in HT-1 — not a mechanistically novel repurposing.

It is worth noting that this is fundamentally an improvement of an HT-1 disease complication in patients already being treated with nitisinone for their primary diagnosis, rather than a new indication in an unrelated disease population. The remaining TxGNN top-10 predictions (galactosemia, serpinopathy, C1 inhibitor deficiency, glycogen storage diseases, Griscelli syndrome, chronic granulomatous disease, ermine phenotype) have no supporting literature or trials and no plausible mechanistic link to HPPD inhibition — these most likely reflect knowledge-graph embedding similarity among rare metabolic/genetic disease nodes rather than genuine pharmacological relationships, and are appropriately scored L5/Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular Genetics and Metabolism | Describes early effect of NTBC on renal tubular dysfunction in HT-1 patients, evaluating whether nitisinone therapy improves proximal tubular function. |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case series | Indian Journal of Gastroenterology | Case series of 4 children with tyrosinemia treated with NTBC; those remaining on therapy showed normal liver function and no renal tubular complications. |

---

## Canada Market Information

Nitisinone is not currently marketed in Canada (0 DINs on record). No product license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: the source safety data pack flags an unresolved **Blocking**-severity gap (Canadian labelled warnings/contraindications not yet obtained), which prevents a full safety pre-screen (S1) at this time.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The HPPD-inhibition mechanism gives a clear, direct pharmacological basis for benefit in HT-1-associated renal tubular acidosis, and two cohort/case-series publications support it — but this describes a complication benefit within the existing HT-1 population, evidence is limited to non-RCT study designs (L3), and the drug is not currently marketed in Canada.

**To proceed, the following is needed:**
- Canadian product monograph / labelled warnings and contraindications (currently a Blocking data gap)
- Formal confirmation of original mechanism of action and approved indication documentation
- Clarification of regulatory pathway given the drug has 0 DINs / no current Canadian market presence
- Additional prospective or controlled evidence beyond the existing cohort and case-series data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

