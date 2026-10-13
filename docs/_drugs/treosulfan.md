---
layout: default
title: Treosulfan
parent: Model Prediction Only (L5)
nav_order: 938
evidence_level: L5
indication_count: 10
---

# Treosulfan
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

# Treosulfan: From Conditioning Before Stem Cell Transplantation to Diabetic Cataract

## One-Sentence Summary

Treosulfan is an alkylating agent used as a conditioning treatment before hematopoietic stem cell transplantation.
The TxGNN model predicts it may be effective for **diabetic cataract** (and several other cataract subtypes), but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model output only, and the available data do not support a plausible mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Canadian license data (the approved indication text is empty). Based on general knowledge, conditioning before hematopoietic stem cell transplantation |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Treosulfan is generally understood to be a bifunctional alkylating agent. It is a prodrug that converts into epoxide species, which damage DNA and cause cytotoxicity, and it is used for conditioning before stem cell transplantation.

Based on the data provided, **no mechanistic link supports this prediction**. Diabetic cataract mainly involves polyol pathway activation and oxidative stress in the lens. DNA alkylation and cytotoxicity have no recognized benefit for lens opacity, and alkylating agents may themselves carry ocular toxicity or cataract risk. The high score (0.990) most likely reflects graph-level similarity across cataract subtypes rather than biology.

The other predicted indications show the same pattern. These are nuclear senile cataract, cortical cataract, mature cataract, tetanic cataract, craniostenosis cataract, immature cataract, type 2 diabetes–associated cataract, senile cataract, and diabetic retinopathy. All have scores of about 0.989–0.990, all are L5 with no trials or publications, and none has a plausible mechanism. For example:
- Tetanic cataract is driven by low calcium, which treosulfan does not address.
- Diabetic retinopathy is treated through VEGF, inflammation, and glycemic control, and treosulfan's myelosuppression would be a major concern.
- Craniostenosis cataract is a congenital or syndromic condition in which cytotoxic exposure would be especially worrying.

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
| 02517388 | TRECONDYV | Not listed | Not listed |
| 02560585 | TREOSULFAN FOR INJECTION | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (myeloablative conditioning use) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the data compiled for this report. This is not evidence of absence of interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, literature, or supported mechanism. The drug's cytotoxic and myelosuppressive profile argues against use in chronic, non-lethal eye conditions such as cataract.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any biological link to lens disease exists
- Package insert warnings and contraindications from Health Canada, including ocular toxicity
- Preclinical or observational evidence of any effect on lens opacity
- Review of the Canadian license data (dosage forms and approved indications are missing)
- A route and formulation assessment for any ocular use, which has not yet been done
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

