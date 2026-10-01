---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 672
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial. The Canadian licence record lists the product OCUFLOX but gives no approved indication text.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome** with a very high score (99.91%), but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (antibacterial class use; indication text not listed in the Canadian licence record) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Ofloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy is established for bacterial infections.

Nothing in the available data links this antibacterial mechanism to serum viscosity or to excess immunoglobulin, which are the features of polyclonal hyperviscosity syndrome. The high score is therefore a model output without biological or clinical support. It should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2143291 | OCUFLOX | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Predicted Candidates for Ofloxacin

The top-ranked prediction has no support, but two lower-ranked predictions have some evidence. Both come from the same model output.

| Predicted Indication | Score | Evidence Level | Evidence Summary |
|------|------|------|------|
| Monoclonal gammopathy | 99.82% | L4 | The evidence is indirect. The TEAMM Phase 3 RCT ([PMID 31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/), *Lancet Oncol*, 2019) tested **levofloxacin**, not ofloxacin, for infection prophylaxis in newly diagnosed myeloma. This is supportive care, not treatment of the gammopathy, and the population is myeloma rather than MGUS. |
| Septicemic plague | 99.79% | L4 | Experimental ofloxacin work is limited to animal studies, such as [PMID 16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) (2002, mouse plague model). Regulatory-grade primate data exist for ciprofloxacin and levofloxacin, not ofloxacin. There are no human trials, and this falls within the class's established antibacterial spectrum. |

The remaining candidates (hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, hematological disease associated with an acquired peripheral neuropathy, congenital hematological disorder, punctate epithelial keratoconjunctivitis) have no clinical trials and only incidental or no literature. Fluoroquinolones are themselves associated with peripheral neuropathy, which argues against the neuropathy-related prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score. There is no trial, no publication, and no plausible mechanistic link between a bacterial topoisomerase inhibitor and serum hyperviscosity. The two better-supported candidates, monoclonal gammopathy and septicemic plague, rest on evidence about other fluoroquinolones or on animal studies. They are research questions, not repurposing leads for ofloxacin.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Approved indication text and dosage form for the Canadian licence, to confirm the original indication and route compatibility
- Evidence that ofloxacin itself (rather than levofloxacin or ciprofloxacin) is relevant to the monoclonal gammopathy or plague candidates, if either is to be pursued

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

