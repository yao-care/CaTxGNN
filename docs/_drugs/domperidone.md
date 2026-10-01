---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Domperidone: To Nephrogenic Syndrome of Inappropriate Antidiuresis (Original Indication Not Recorded)

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist marketed in Canada, but the Evidence Pack records no original indication for it.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on a knowledge-graph score alone and is likely a graph-proximity artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (no approved indication text in any listed license) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for domperidone is not available in the Evidence Pack. Based on the rationale provided, domperidone is a peripheral dopamine D2/D3 receptor antagonist. No original indication is recorded, so no link between an original and a new indication can be drawn from the data.

NSIAD is caused by gain-of-function variants in *AVPR2* (the vasopressin V2 receptor), and less often in *GNAS*. These variants make the receptor constitutively active, causing water retention and hyponatremia even when arginine vasopressin (AVP) levels are low or undetectable.

The mechanistic link is weak. Dopamine signaling can modulate AVP release, but that acts upstream of the V2 receptor. It would not be expected to correct a receptor that is active regardless of AVP. No direct connection between domperidone and V2 receptor signaling has been established. The high score (0.991) is most likely a knowledge-graph proximity effect rather than a biologically grounded signal, and the mechanistic assessment is low-confidence.

---

## Canada Market Information

Five of the 10 authorizations are listed below. The Evidence Pack does not provide dosage form, manufacturer, or approved indication text for them.

| DIN | Product Name |
|---------|------|
| 02350440 | DOMPERIDONE |
| 02236857 | PRO-DOMPERIDONE |
| 02369206 | JAMP-DOMPERIDONE |
| 02445034 | BIO-DOMPERIDONE |
| 02238341 | DOMPERIDONE |

---

## Safety Considerations

- **Cardiac risk**: Domperidone carries a known risk of QT prolongation and arrhythmia. This would need careful review in a hyponatremic, electrolyte-disturbed population such as NSIAD patients.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and the mechanism is implausible because NSIAD involves a constitutively active V2 receptor that dopamine antagonism would not be expected to correct. The QT and arrhythmia risk adds a safety concern in an electrolyte-disturbed population.

**To proceed, the following is needed:**
- Preclinical evidence, such as V2 receptor signaling assays, showing any domperidone effect on AVPR2 or GNAS-mediated activity
- Detailed mechanism-of-action data and the recorded original indications
- Health Canada package insert warnings and contraindications, for safety screening
- A cardiac safety assessment (QT and electrolyte considerations) for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

