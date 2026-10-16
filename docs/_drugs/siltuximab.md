---
layout: default
title: Siltuximab
parent: Model Prediction Only (L5)
nav_order: 849
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Siltuximab: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Castleman disease"
monitor_inn: "Siltuximab"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever", "syndrome with combined immunodeficiency", "TAFRO syndrome"]
---

# Siltuximab
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

# Siltuximab: From Castleman Disease to Extracutaneous Mastocytoma

## One-Sentence Summary

Siltuximab is an anti-interleukin-6 (IL-6) antibody, originally used to treat Castleman disease.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Castleman disease (Kimura disease is also listed in the knowledge graph) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Siltuximab is described in the supplied literature as a chimeric monoclonal antibody that binds IL-6. Its efficacy in multicentric Castleman disease, a disorder driven by dysregulated IL-6 production, has been established.

The link to extracutaneous mastocytoma is weak. IL-6 signaling has been implicated in mast cell biology, and IL-6 is elevated in mast cell disorders such as mastocytosis. However, the data compiled for this report show no direct evidence connecting siltuximab to this disease. The TxGNN score is high, but it is a model-based association only and has not been tested clinically or in the literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02435128 | SYLVANT |
| 02435136 | SYLVANT |

Both are valid single-ingredient authorizations. Dosage form and approved indication text were not available.

---

## Safety Considerations

**Drug Interactions:** The interaction screen found 100 potential interactions. Examples from the 20 reviewed entries:
- **Major:** Deferiprone
- **Moderate:**
  - Anticoagulants: warfarin, apixaban, rivaroxaban, dicoumarol
  - Statin: simvastatin
  - Respiratory drugs: theophylline, aminophylline, oxtriphylline, roflumilast
  - Other medicines: tacrolimus, lidocaine, nifedipine
  - Opioids: fentanyl, hydrocodone
  - Vaccine: tetanus toxoid
- **Minor:** Zinc salts (sulfate, acetate, gluconate, chloride)

Many of these involve drugs with narrow therapeutic windows, so close monitoring would be needed if co-administered.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, and the mechanistic link is only indirect. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Mechanistic and preclinical data on IL-6 involvement in extracutaneous mastocytoma
- A literature search for any case-level use of IL-6 blockade in mast cell neoplasms
- Package insert warnings and contraindications from Health Canada, and detailed mechanism of action data
- Review of the other predicted indications. Notably, **TAFRO syndrome** (rank 10, score 98.8%) has considerably more supporting evidence, at L4: case reports, consensus guidance, and an indirect Phase 2 RCT in idiopathic multicentric Castleman disease. It is a more promising candidate to prioritize.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

