---
layout: default
title: Ibutilide
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 2
---

# Ibutilide
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

# Ibutilide: From Arrhythmia Treatment to Rheumatoid Arthritis

## One-Sentence Summary

Ibutilide is marketed in Canada as CORVERT. The data compiled for this report do not list an approved indication text for it.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibutilide is generally described as a class III antiarrhythmic. It prolongs cardiac repolarization by blocking the delayed rectifier potassium current (IKr/hERG) and promoting a slow inward sodium current. The licence data do not state an original indication.

No known pathway links IKr blockade to the inflammatory, autoimmune, or synovial processes of rheumatoid arthritis. The high TxGNN score reflects a model-based prediction that may capture network-level associations rather than biological causality. Any link, such as ion-channel modulation in immune cells or synoviocytes, would be speculative and is not supported by the available evidence.

A second prediction, nephrogenic syndrome of inappropriate antidiuresis (score 99.30%), has the same weaknesses. It is a very rare vasopressin V2 receptor disorder, and ibutilide has no recognized activity on that receptor or on renal water handling. It also has no supporting trials or literature, and its recommendation is also Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242470 | CORVERT | Not stated | Not stated |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph):** The TxGNN knowledge graph links ibutilide to the following conditions as contraindications. These come from graph edges, not from label text:
  - long QT syndrome
  - familial long QT syndrome
  - torsades de pointes
  - potassium deficiency disease
  - atrioventricular dissociation
  - atrioventricular block
  - heart block
- **Drug Interactions:** The data compiled for this report list 100 interactions, 20 of which are shown here. Several are rated Major, and most of those involve QT prolongation or electrolyte disturbance:
  - Clarithromycin
  - Levofloxacin
  - Cisapride
  - Ondansetron
  - Granisetron
  - Dolasetron
  - Palonosetron
  - Eliglustat
  - Picosulfuric acid
  - Sodium sulfate
  - Polyethylene glycol (3350 with electrolytes)

  Moderate interactions include famotidine, loperamide, bisacodyl, lactitol, lactulose, polyethylene glycol (3350), castor oil and glycerin. Metronidazole is rated Minor.
- **Serious proarrhythmic risk:** Ibutilide can cause torsades de pointes and generally requires in-hospital monitoring. This would be a major barrier to any chronic use, such as in rheumatoid arthritis.

Please refer to the package insert for the full warnings and contraindications, because that information is not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanistic link to rheumatoid arthritis. Ibutilide also has a serious proarrhythmic risk, and the licence data lack indication and safety information.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication), which is needed before any safety screening
- Detailed mechanism of action data, for example from DrugBank
- Preclinical or mechanistic evidence for ion-channel involvement in rheumatoid arthritis
- A risk-benefit assessment of the torsades de pointes risk and the QT-prolonging drug interactions for any non-acute use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

