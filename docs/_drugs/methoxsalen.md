---
layout: default
title: Methoxsalen
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "METHOXSALEN"
predicted_indications: ["localized pagetoid reticulosis", "neoplasm of mature B-cells", "small intestinal Burkitt lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "vulvar inverted follicular keratosis"]
description: "Methoxsalen: predicted new indication Localized pagetoid reticulosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Methoxsalen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Methoxsalen: Localized pagetoid reticulosis
{: .text-alpha }

## One-Sentence Summary

Methoxsalen is a photosensitizing drug originally used for primary cutaneous T-cell lymphoma and vitiligo.
The TxGNN model predicts it may be effective for **localized pagetoid reticulosis** (Woringer-Kolopp disease), a variant of mycosis fungoides.
There are currently **0 clinical trials** and **0 publications** directly supporting this specific prediction, so it rests on model prediction and disease-class similarity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (L5 would apply strictly, as no direct studies were supplied; L4 reflects the mechanistic rationale) |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, methoxsalen is a psoralen photosensitizer. When activated by UVA light (PUVA), or in extracorporeal photopheresis, it is understood to form DNA crosslinks and induce apoptosis in malignant T-cells.

Localized pagetoid reticulosis is a variant of mycosis fungoides, which is itself a primary cutaneous T-cell lymphoma. The predicted indication is therefore biologically very close to the drug's existing use, and this is largely an extension of the existing label rather than a truly new repurposing.

It should be noted that the link is inferred from disease-class similarity and the high TxGNN score. No trials or literature specific to this variant were included in the data compiled for this report.

## Other Predicted Indications

The model also ranked nine further candidates. Evidence is limited for all of them.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 3 | Neoplasm of mature B-cells | 0.9984 | L5 | Speculative; methoxsalen's activity is established in T-cell disease |
| 4 | Small intestinal Burkitt lymphoma | 0.9980 | L5 | UVA cannot reach the site; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 5 | Thyroid gland MALT lymphoma | 0.9978 | L5 | Internal site; no clear rationale |
| 6 | Small intestinal MALT lymphoma | 0.9978 | L5 | Internal site; no clear rationale |
| 8 | Breast MALT lymphoma | 0.9977 | L5 | Deep tissue site; no supporting mechanism |
| 9 | Tonsillar lymphoma | 0.9977 | L5 | Mostly B-cell; photochemotherapy not established |
| 10 | Vulvar inverted follicular keratosis | 0.9965 | L5 | Benign lesion; PUVA carcinogenic risk argues against use |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for localized pagetoid reticulosis. For the second-ranked indication (indolent primary cutaneous T-cell lymphoma), one indirect item was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) | 2006 | Review (health technology assessment) | Ontario Health Technology Assessment Series | Evidence-based analysis of extracorporeal photopheresis for refractory erythrodermic cutaneous T-cell lymphoma and chronic graft-versus-host disease; not specific to indolent disease or to methoxsalen alone |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02406233 | UVADEX | Not specified | Not specified in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Photoactivated DNA-crosslinking agent (photochemotherapy); not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the knowledge graph, not from label text):
  - Photosensitivity conditions: photosensitivity disease, photoparoxysmal response
  - Porphyrias: porphyria, variegate porphyria, porphyria cutanea tarda, erythropoietic protoporphyria, and related disorders of porphyrin metabolism
  - Skin and other cancers: melanoma, basal cell carcinoma, squamous cell carcinoma, skin carcinoma, sweat gland cancer, sebaceous adenocarcinoma
  - DNA-repair and pigmentation disorders: xeroderma pigmentosum, albinism, Waardenburg syndrome, piebaldism, Griscelli syndrome
  - Other: systemic lupus erythematosus (including pediatric), liver disease, gallbladder disease, peroxisome biogenesis disorder
- **Drug Interactions**: 100 interactions were found. The 20 listed are all Moderate severity: doxycycline, tetracycline, minocycline (including topical forms), levofloxacin, sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide, tolazamide, tolbutamide), sulfasalazine, sulfamethizole, promethazine, alosetron, ibuprofen and flurbiprofen. Many of these are likely additive photosensitivity effects, but this is not stated in the data.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is mechanistically close to the approved use, but no trials or literature specific to localized pagetoid reticulosis were provided. The model score alone is not sufficient evidence. The label-level safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data (for example from DrugBank)
- A targeted literature search for PUVA in localized pagetoid reticulosis and mycosis fungoides variants
- Approved indication text and dosage form for UVADEX, to confirm whether the existing label already covers this use
- Route and device compatibility assessment (PUVA versus extracorporeal photopheresis)
- A review of carcinogenic risk (skin cancer) and the photosensitizing drug interactions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

