---
layout: default
title: Ipilimumab
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Ipilimumab: predicted new indication Choroideremia (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ipilimumab: From Metastatic Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab is an immune checkpoint antibody (anti-CTLA-4) originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **choroideremia** (a rare inherited retinal degeneration), but **no clinical trials and no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Ipilimumab is known to block CTLA-4, which enhances T-cell priming and activation. This is the basis of its use in melanoma, where it helps the immune system attack tumour cells.

Choroideremia is a different kind of disease. It is an X-linked inherited retinal degeneration caused by loss of function of the *CHM* gene (REP1 protein). It is not driven by tumour immune evasion, so there is no plausible biological reason why CTLA-4 blockade would help. The high score most likely reflects an artefact of the knowledge graph, not a real therapeutic link.

Systemic checkpoint blockade can also cause immune-related eye adverse events such as uveitis. These would be undesirable in an already degenerating retina.

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
| 02379384 | YERVOY |

Dosage form and approved indication text were not available for this licence.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Immune-related adverse events: liver function, thyroid function, and signs of colitis, dermatitis and ocular inflammation. Please also refer to the package insert. |
| Handling Protection | Please refer to the package insert and local institutional handling policies |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The 20 listed in the compiled data include:
  - **Major**: anticoagulants, including apixaban, betrixaban, bivalirudin, dalteparin, desirudin, edoxaban, argatroban and danaparoid.
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), metronidazole, tinidazole, naltrexone, rosuvastatin and simvastatin.
- **Ocular risk**: Immune-related eye inflammation, such as uveitis, is a recognised risk of checkpoint blockade. This is a particular concern in a retinal disease.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or publications for choroideremia. The disease mechanism (inherited loss of *CHM* function) has no plausible link to CTLA-4 blockade. Immune-related eye toxicity adds a safety concern.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking CTLA-4 blockade to retinal degeneration in choroideremia
- Package insert warnings and contraindications, particularly for ocular adverse events
- Detailed mechanism of action data
- Confirmation that the high score is not a knowledge-graph artefact

**Note on another prediction:** The same model also ranks **non-cutaneous melanoma** (score 99.02%) as a candidate for ipilimumab. This is biologically plausible, since it is closely related to the approved indication, and it has more supporting trials, including a Phase 2 trial of nivolumab plus ipilimumab in uveal melanoma. Several listed trials are not melanoma-specific, so the Phase 3 entry should be verified before it is counted as direct evidence. This indication may be a more promising direction to evaluate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

