---
layout: default
title: Tremelimumab
parent: Model Prediction Only (L5)
nav_order: 937
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tremelimumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not specified in the Canadian license data compiled for this report"
monitor_inn: "Tremelimumab"
predicted_indications: ["diabetic cataract", "tetanic cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "craniostenosis cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic retinopathy"]
---

# Tremelimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tremelimumab: From Oncology Use to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Tremelimumab is an anti-CTLA-4 monoclonal antibody (marketed in Canada as IMJUDO) that is used in cancer immunotherapy.
The TxGNN model predicts it may be effective for **diabetic cataract**,
but currently **no clinical trials and no publications** support this direction; the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data compiled for this report (clinical use per pharmacology data: malignant mesothelioma, melanoma, unresectable hepatocellular carcinoma) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known pharmacology, tremelimumab is a monoclonal antibody that binds CTLA-4 (CD152) and blocks its interaction with CD80/CD86, thereby enhancing T-cell activation. Its established use is in oncology, including a combination with durvalumab approved for unresectable hepatocellular carcinoma.

The link to diabetic cataract is weak. Diabetic cataract is driven by metabolic mechanisms such as the polyol pathway, oxidative stress and glycation, and none of these is addressed by CTLA-4 blockade. The very high scores for many cataract subtypes (tetanic, immature, mature, senile, cortical, nuclear and others) suggest the model is reflecting closeness among cataract-related nodes in its knowledge graph rather than a disease-specific therapeutic signal. Immune checkpoint blockade also carries risks of ocular immune-related adverse events (e.g., uveitis) and immune-related endocrinopathies, including diabetes, which argue against benefit.

Other top-ranked predictions (all L5, all Hold) include tetanic cataract, immature cataract, type 2 diabetes-associated cataract, mature cataract, craniostenosis cataract, nuclear senile cataract, cortical cataract, senile cataract and diabetic retinopathy. Diabetic retinopathy has a loose conceptual connection through inflammation and microvascular damage, but it remains speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02541009 | IMJUDO | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 immune checkpoint inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; immune-related adverse events (including ocular, endocrine and hepatic events) are a recognized concern for this class |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query was completed and returned one entry, which is the pharmacological target of tremelimumab (CTLA-4/CD152) rather than a co-administered drug. No drug–drug interactions with a defined severity level were identified.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. There are no clinical trials or publications, no plausible mechanistic path to lens opacity, and the drug's class effects (ocular and endocrine immune-related toxicity) suggest potential harm rather than benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication and dosage form details for the Canadian license
- Preclinical evidence (e.g., lens or retinal models) showing a plausible benefit of CTLA-4 blockade
- Assessment of route compatibility, since the drug is a systemic antibody and the target tissue is the eye
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

