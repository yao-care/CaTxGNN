---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From FGFR-Driven Cancers to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib (marketed in Canada as PEMAZYRE) is a selective FGFR1-3 inhibitor, an oncology drug. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **0 clinical trials** and **0 publications** support this prediction. It rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (Canadian license records contain no indication text). Pemigatinib is generally known as an FGFR inhibitor for FGFR-altered cancers. |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pemigatinib is a selective inhibitor of FGFR1, FGFR2 and FGFR3. Detailed original mechanism-of-action data is not available in the Evidence Pack, so the analysis relies on its known target class.

The link to multiple endocrine neoplasia (MEN) is **speculative**. MEN syndromes are mainly driven by MEN1 or RET alterations, and FGFR signaling is not a known primary driver. The very high score (0.997) is a graph-based prediction, not a finding supported by trials or publications.

Among the other top-ranked predictions, only **HER2-positive breast carcinoma** has a plausible biological rationale. FGFR pathway activation is reported as one mechanism of resistance to HER2-targeted therapy, so FGFR inhibition could make sense in combination settings. Its only retrieved publication is a general review of kinase inhibitors, with no pemigatinib-specific clinical data.

The remaining top-10 predictions are weak or likely artifacts of the knowledge graph:
- **Veterinary diseases:** infectious bovine rhinotracheitis and malignant catarrh, which have no human relevance.
- **ALS entries:** three overlapping amyotrophic lateral sclerosis terms with unclear direction of effect.
- **Other predictions:** amenorrhea, cytomegalovirus infection, and axial spondylometaphyseal dysplasia, which have no supported mechanistic link or raise safety concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports the top prediction (multiple endocrine neoplasia). The only publication retrieved across the top 10 predictions relates to HER2-positive breast carcinoma:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | General review of FDA-approved small-molecule protein kinase inhibitors. It provides no indication-specific clinical evidence for pemigatinib. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2519941 | PEMAZYRE | — | — |
| 2519933 | PEMAZYRE | — | — |
| 2519968 | PEMAZYRE | — | — |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Serum phosphate (hyperphosphatemia is a known adverse effect); other items per package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

Hyperphosphatemia and endocrine effects are known pemigatinib adverse effects, and these matter for any endocrine-related indication. In addition, no drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. It has no trials and no indication-specific literature, and the mechanistic link to multiple endocrine neoplasia is speculative. Evidence level is L5, at the earliest screening stage (S0).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank, to support a mechanistic-link analysis
- Original approved indication text, dosage forms and manufacturer for the three DINs
- Preclinical evidence linking FGFR inhibition to MEN biology
- If prioritizing, reviewing HER2-positive breast carcinoma (FGFR-mediated resistance) as a more plausible candidate than the top-ranked prediction

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

