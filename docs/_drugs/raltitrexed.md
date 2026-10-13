---
layout: default
title: Raltitrexed
parent: Model Prediction Only (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed: From Colorectal Cancer to Sclerosing Cholangitis

## One-Sentence Summary

Raltitrexed is a thymidylate synthase inhibitor (an antimetabolite chemotherapy) used to treat colorectal cancer and malignant mesothelioma.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer and malignant mesothelioma (from the pharmacology reference data; the Canadian licence record contains no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, raltitrexed is an antifolate that targets thymidylate synthase (TYMS), an enzyme required for DNA synthesis. Its efficacy in colorectal cancer and malignant mesothelioma is established, and it works by suppressing rapidly dividing cells.

The link to sclerosing cholangitis is weak. Sclerosing cholangitis is an immune-mediated, fibroinflammatory disease of the bile ducts, and there is no established rationale for cytotoxic antifolate therapy in it. The very high TxGNN score (99.97%) is a model output based on knowledge-graph patterns, not an indication of demonstrated benefit.

Other predictions for this drug include myelodysplastic syndrome and several sickle cell disease variants. The identical scores across the sickle cell variants suggest a shared graph-based signal rather than disease-specific evidence. For myelodysplastic syndrome, a plausible but unvalidated idea is that thymidylate synthase inhibition could suppress abnormal blood-forming cells. However, myelosuppression is a major antifolate toxicity and could worsen existing low blood counts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229566 | TOMUDEX | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate / thymidylate synthase inhibitor) |
| Myelosuppression Risk | Medium to high (myelosuppression is a recognised major toxicity of antifolates) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacological one, with the drug's own target, thymidylate synthase (TYMS). No drug-drug interactions with severity levels were identified.
- **Haematological concern**: Antifolate myelosuppression is a particular concern for the predicted blood-related indications (myelodysplastic syndrome, refractory cytopenia of childhood, sickle cell disease variants).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials or publications (Evidence Level L5). There is no plausible mechanistic rationale for a cytotoxic antifolate in sclerosing cholangitis, and the safety profile is unfavourable.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Preclinical or mechanistic studies linking thymidylate synthase inhibition to biliary inflammation or fibrosis
- Approved indication text for the Canadian licence (DIN 02229566)
- A risk-benefit assessment for a non-malignant condition, given the myelosuppression risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

