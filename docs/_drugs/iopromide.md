---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated radiographic contrast agent, used to enhance visibility in imaging procedures rather than to treat disease.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but **0 clinical trials** and **0 publications** support this specific prediction.
The score is a graph-based signal only, and no therapeutic mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Use | Iodinated contrast medium for diagnostic imaging (no approved indication text available in the record) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is a contrast agent for diagnostic imaging, and it has no known disease-modifying pharmacology.

The prediction does not appear to reflect a therapeutic relationship. The related osteoarthritis prediction (rank 2) has two retrieved papers. One describes CT-guided nerve block for hip pain, and the other measures cartilage with MRI after contrast injection. Both use contrast for imaging or procedural guidance and neither tests the drug as a treatment. The high score most likely reflects the drug's co-occurrence with musculoskeletal imaging in the knowledge graph.

The other top predictions include rare skeletal dysplasias (brachyolmia, acromesomelic dysplasia, pseudoachondroplasia), alopecia and hemoglobinopathy. None has a plausible pharmacological link to iopromide. Until a mechanism is shown, these predictions should be treated as computational artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for osteoarthritis susceptibility.

For reference, the closely related **osteoarthritis** prediction (score 99.53%, evidence level L4) has two indirect papers, both imaging-related:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11419151](https://pubmed.ncbi.nlm.nih.gov/11419151/) | 2001 | Case series / procedural technique | European Radiology | CT-guided obturator nerve block for diagnosing and treating painful hip conditions. This is a procedural pilot study, not a test of the drug as a therapy. |
| [9678042](https://pubmed.ncbi.nlm.nih.gov/9678042/) | 1998 | Methodological imaging study | Clinical Orthopaedics and Related Research | Accuracy of MRI cartilage volume and thickness measurements in cadaveric knees, validated against contrast-enhanced CT. It concerns measurement, not treatment. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2078619 | ULTRAVIST 370 |
| 2078600 | ULTRAVIST 300 |

Dosage form and approved indication text are not recorded for these licenses.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.
- **Literature safety signal**: A case report ([PMID 16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/), 2006, American Journal of Hematology) describes a cerebral vaso-occlusive event after low-osmolar intravenous contrast in a patient with sickle cell disease. This was flagged in the hemoglobinopathy prediction and should be addressed before any repurposing hypothesis in that area.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials and no literature testing iopromide for osteoarthritis susceptibility. The nearest evidence (osteoarthritis, hemoglobinopathy) is limited to imaging use, and one report is a safety signal.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to assess any biological link
- Preclinical or mechanistic evidence for a therapeutic effect, since none currently exists
- A review of why the knowledge graph links iopromide to these diseases, to confirm whether the association is only imaging co-occurrence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

