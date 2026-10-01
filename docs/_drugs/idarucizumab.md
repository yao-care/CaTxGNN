---
layout: default
title: Idarucizumab
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: From Dabigatran Reversal to Hemoglobinopathy

## One-Sentence Summary

Idarucizumab (PRAXBIND) is an antibody fragment that reverses the anticoagulant effect of dabigatran.
The TxGNN model predicts it may be effective for **hemoglobinopathy**, but **0 clinical trials** and **0 publications** support this prediction.
The high score appears to be a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of dabigatran anticoagulant activity (the license record lists no indication text; this is inferred from the drug's mechanism) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 95.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. What is known is that idarucizumab is a humanized Fab fragment that binds dabigatran with high affinity and neutralizes its anticoagulant activity.

**The prediction is not mechanistically plausible.** The drug does not act on hemoglobin synthesis, red cell biology, or globin gene expression. Its only relevance to a hemoglobin disorder would be reversing dabigatran in a patient who happens to be anticoagulated, and that is not a repurposed indication.

The same is true of the other top-ranked predictions:
- **Red cell disorders:** beta-thalassemia, pyruvate kinase deficiency, glucophosphate isomerase deficiency, and hereditary pyropoikilocytosis. The drug has no action on globin balance, red cell glycolysis, or membrane stability.
- **Inflammatory and respiratory conditions:** rheumatoid arthritis, gout, and bronchitis. The drug has no immunomodulatory, anti-inflammatory, or antimicrobial activity.
- **Genetic syndromes:** a chromosome 16p partial deletion and colobomatous microphthalmia-rhizomelic dysplasia syndrome. A single-target antibody fragment cannot address these underlying genetic defects.

All ten predictions are computational only.

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
| 2454343 | PRAXBIND |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical, or literature support and no plausible mechanism. It is Level 5 (model prediction only). The score is most likely a knowledge-graph artifact, and the drug's action is specific to dabigatran.

**To proceed, the following is needed:**
- A mechanistic hypothesis that links dabigatran-specific antibody binding to a hemoglobin disorder. Without one, further investment is not justified.
- The Health Canada package insert, for warnings and contraindications.
- Detailed mechanism of action data from DrugBank.
- Any preclinical or clinical signal for hemoglobinopathy. Absent that, the candidate should be deprioritized.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

