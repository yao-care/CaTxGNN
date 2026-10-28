---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 933
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Trastuzumab Deruxtecan: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Trastuzumab deruxtecan"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Trastuzumab Deruxtecan: From HER2-Directed Cancer Therapy to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-directed antibody-drug conjugate marketed in Canada as ENHERTU. The approved indication text was not available in the data compiled for this report.
The TxGNN model (deep learning) predicts it may be effective for **drug-induced osteoporosis**, but **no clinical trials and no publications** currently support this prediction. The score comes from the model and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian license record has no indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, trastuzumab deruxtecan is a HER2-directed antibody-drug conjugate that delivers a topoisomerase I inhibitor payload to HER2-expressing cells. Its use is in HER2-expressing cancers, notably breast cancer.

The prediction is difficult to justify mechanistically. No plausible link between a HER2-targeted cytotoxic conjugate and bone metabolism or drug-induced bone loss is evident. The high score (rank 11,995 in the model's ordering) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of benefit.


---

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.


---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02514400 | ENHERTU | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload (targeted therapy delivering a cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; haematological parameters and respiratory status are generally relevant |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: The interaction query found 42 interacting drugs in total. Examples flagged as **Major** include deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, leflunomide, and natalizumab. Examples flagged as **Moderate** include palifermin, strontium chloride Sr-89, roflumilast, chloramphenicol, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, dimethyl fumarate, and niraparib. Many involve immunosuppressive or myelosuppressive agents.
- **Respiratory risk**: The retrieved literature includes case reports of interstitial lung disease and pneumonitis associated with this drug, which is relevant to any airway-related use.
- **Other reported adverse events**: Case reports describe reversible Fanconi syndrome and dermatomyositis with interstitial pneumonia.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis has no clinical, literature, or mechanistic support (Evidence Level L5). A systemic cytotoxic ADC with known serious toxicities, including lung toxicity, offers an unfavourable risk-benefit profile for a non-oncologic bone condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and the approved indication text for the Canadian license
- Preclinical or mechanistic evidence linking the drug to bone metabolism
- A risk-benefit assessment justifying systemic cytotoxic exposure in a non-oncology population
- Any registered trials or published studies for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

