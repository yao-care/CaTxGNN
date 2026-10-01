---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 278
evidence_level: L5
indication_count: 2
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Gastrointestinal Antispasmodic Use to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antimuscarinic smooth-muscle relaxant. The Canadian licence records in this dataset do not list its approved indication text.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided Canadian licence data (general pharmacology: antispasmodic for gastrointestinal smooth-muscle spasm) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, dicyclomine is an antimuscarinic and direct smooth-muscle relaxant. Its main use is relieving smooth-muscle spasm, and mechanistically it may act on downstream symptoms rather than on the underlying disease.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots. Dicyclomine could at most act on secondary bladder or bowel symptoms. It cannot address the compression or the nerve injury itself. The link is therefore indirect and speculative.

There is also a safety concern. Cauda equina syndrome commonly causes urinary retention (an underactive bladder), and an anticholinergic could worsen retention and constipation. The high TxGNN score (99.66%) is a model output with no supporting clinical signal.

A second prediction, "obsolete neurogenic bladder (disease)" (score 99.50%, L5), is mechanistically more coherent because antimuscarinics are an established class for detrusor overactivity. The disease term is obsolete in the ontology and should be remapped to a current term, such as neurogenic detrusor overactivity, before further analysis. No dicyclomine-specific evidence was provided for it either. Dicyclomine is not a bladder-selective agent, and its anticholinergic burden would need to be weighed against approved alternatives.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02366088 | JAMP-DICYCLOMINE HCL | Not listed | Not listed |
| 02391619 | JAMP-DICYCLOMINE HCL | Not listed | Not listed |
| 00557102 | RIVA-DICYCLOMINE | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Anticholinergic considerations (general pharmacology, not from the Evidence Pack)**: In the predicted setting, urinary retention and constipation are the main concerns. Anticholinergic effects on cognition should also be considered.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or literature. The mechanistic link is weak, and the drug's anticholinergic effects could worsen the typical retention symptoms of cauda equina syndrome.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data (MOA), for example from DrugBank
- Approved indication text for the three Canadian DINs
- Remapping of the obsolete neurogenic bladder term to a current disease term, followed by a targeted literature search for dicyclomine in neurogenic bladder and cauda equina syndrome
- Any clinical or observational evidence before revisiting the decision

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

