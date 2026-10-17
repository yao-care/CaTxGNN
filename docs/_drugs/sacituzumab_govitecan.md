---
layout: default
title: Sacituzumab Govitecan
parent: Model Prediction Only (L5)
nav_order: 830
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sacituzumab Govitecan: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "mature cataract", "immature cataract", "tetanic cataract"]
---

# Sacituzumab Govitecan
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

# Sacituzumab govitecan: From an Unspecified Original Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab govitecan (marketed in Canada as TRODELVY) is a Trop-2-directed antibody-drug conjugate that carries the topoisomerase I inhibitor SN-38. The TxGNN model predicts it may be effective for **drug-induced osteoporosis**. **No clinical trials and no publications** currently support this prediction, so it is a computational output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general knowledge of the drug, sacituzumab govitecan is a Trop-2-directed antibody-drug conjugate. It delivers SN-38, the active metabolite of irinotecan and a topoisomerase I inhibitor, to Trop-2-expressing cells. Its use is in oncology.

**No credible mechanistic link to the predicted indication could be established.** Drug-induced osteoporosis is a bone-loss condition, typically caused by agents such as glucocorticoids. Nothing in the drug's mechanism suggests bone-protective or bone-forming effects. A cytotoxic ADC would be expected to carry bone-marrow and general toxicity risk rather than bone benefit. The high TxGNN score (0.998; model rank 4900) most likely reflects proximity in the knowledge graph rather than biological relevance, and without supporting evidence the prediction is biologically implausible.

The other nine predictions in the ranked list (diabetic retinopathy and severe nonproliferative diabetic retinopathy, plus diabetic, cortical, nuclear senile, senile, mature, immature and tetanic cataract) have the same weakness. They also have no trials or publications and no plausible mechanism. Several cataract subtypes share identical scores, which suggests ontology-driven clustering rather than independent signals.

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
| 02520788 | TRODELVY | Not available | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (SN-38) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (bone-marrow toxicity is expected for this class) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; blood counts and liver and renal function are generally monitored with cytotoxic agents |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

A drug-interaction query returned **40 interactions**; the 20 below were available for review. Several are rated Major.

- **Drug Interactions (Major):** Deferiprone, fostamatinib, adalimumab, apalutamide, certolizumab pegol, cladribine, dacomitinib, irinotecan, leflunomide, natalizumab, nilotinib, ozanimod
- **Drug Interactions (Moderate):** Alefacept, alemtuzumab, anakinra, canakinumab, dimethyl fumarate, lorlatinib, ocrelizumab, omacetaxine mepesuccinate

Many of these interacting drugs are immunosuppressive or myelosuppressive, so overlapping toxicity is a particular concern. Irinotecan shares the same active metabolite (SN-38) and is therefore a notable combination.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score, with no clinical trials, no literature, and no plausible mechanistic link. Using a systemic cytotoxic ADC for a non-malignant bone condition would raise substantial safety concerns, and no safety benefit-risk case can be made on current data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Original approved indication and mechanism of action data from Health Canada and DrugBank
- Any preclinical or mechanistic evidence linking Trop-2 or topoisomerase I inhibition to bone metabolism
- A review of whether the other predicted indications offer a more plausible lead; none currently shows supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

