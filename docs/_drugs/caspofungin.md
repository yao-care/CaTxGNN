---
layout: default
title: Caspofungin
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Esophageal Candidiasis and Candidemia to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin antifungal originally used to treat esophageal candidiasis and candidemia.
The TxGNN model predicts it may be effective for **gastrin secretion abnormality**, but **0 clinical trials** and **0 publications** support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Caspofungin is known to inhibit beta-(1,3)-D-glucan synthase, an enzyme that fungi need to build their cell walls. This explains its efficacy against Candida infections.

The relationship between the original and new indications is weak. Gastrin is a hormone regulating gastric acid secretion, and humans have no beta-(1,3)-D-glucan synthase pathway. The review of the data found no known mechanism linking caspofungin to gastrin regulation.

The high TxGNN score (99.44%) therefore reflects network-based pattern matching in the knowledge graph rather than biological or clinical support. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Six valid single-ingredient authorizations are listed in Canada. The five main ones are shown below.

| DIN | Product Name |
|---------|------|
| 02244265 | CANCIDAS |
| 02244266 | CANCIDAS |
| 02460947 | CASPOFUNGIN FOR INJECTION |
| 02460955 | CASPOFUNGIN FOR INJECTION |
| 02486997 | CASPOFUNGIN FOR INJECTION |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from label text): liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions**: 81 interactions were identified.
  - Major: dexamethasone
  - Moderate: naltrexone
  - Unclassified severity: many others, including amphotericin B, vancomycin, simvastatin, the proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), and several corticosteroids (prednisone, prednisolone, hydrocortisone)

Please refer to the package insert for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism, so it is a model output alone (L5). The product is well established in Canada for its antifungal uses, but that does not support this new indication.

Among the other predictions from the same analysis, **neonatal candidiasis** is much better supported. It has two Phase 2 neonatal trials (NCT00330395 and NCT01945281), a pediatric echinocandin meta-analysis, and a strong mechanistic fit. It would be a more productive candidate to pursue, although it sits close to the existing antifungal indication.

**To proceed with gastrin secretion abnormality, the following is needed:**
- A plausible biological hypothesis linking caspofungin to gastrin regulation
- Preclinical or mechanistic studies, as no human data exist
- Complete safety data from the Canadian package insert, including warnings and contraindications
- Mechanism of action data entered into the dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

