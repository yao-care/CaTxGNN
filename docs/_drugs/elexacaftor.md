---
layout: default
title: Elexacaftor
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Elexacaftor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Elexacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Elexacaftor is a CFTR protein corrector, used as part of the Trikafta triple combination (Elexacaftor/Tezacaftor/Ivacaftor) for the treatment of cystic fibrosis (CF) in patients carrying at least one F508del mutation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **1 clinical trial** (Grade C — not directly targeting RA) and **0 publications** directly supporting this indication.
Overall evidence remains at model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cystic fibrosis (CFTR F508del mutation, part of ETI triple therapy) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.11% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on clinical context embedded in the prediction rationales, Elexacaftor is a CFTR-specific corrector: it binds to the NBD1 domain of the CFTR protein, stabilising its three-dimensional folding and restoring chloride channel function at the cell surface. In CF patients, the ETI triple combination has demonstrated FEV₁ improvements of 10–14% and broad reductions in systemic inflammatory markers including IL-6 and TNF-α.

The proposed mechanistic bridge to rheumatoid arthritis relies on the fact that CFTR is expressed at low levels in immune cells such as neutrophils. ETI-mediated reduction of IL-6 and TNF-α in CF patients theoretically overlaps with the same cytokines that drive synovial inflammation in RA. However, this connection is extremely indirect: the core pathological axes of RA — JAK-STAT signalling, TNF-driven synoviocyte activation, B-cell/CD20 dysregulation, and IL-17 recruitment of neutrophils — have no established point of intervention by a CFTR corrector.

The most plausible explanation for this high-scoring TxGNN prediction is knowledge-graph co-localisation: Elexacaftor's CF indication places it adjacent to immune and inflammatory disease nodes, which propagates into RA through shared vocabulary (cytokines, neutrophils) rather than through a validated pharmacological pathway. This prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Completed | 47 | Prospective analysis of blood neutrophil function and phenotype in CF patients, assessing the impact of Pseudomonas aeruginosa chronic infection, CFTR modulator treatment, and acute exacerbations. No RA patients enrolled; this is a basic immunology study in CF — Grade C relevance only, cannot support an RA indication. |

---

## Literature Evidence

Currently no related literature available directly linking Elexacaftor to rheumatoid arthritis.

---

## Canada Market Information

Elexacaftor is not currently marketed in Canada as a standalone product. No Drug Identification Numbers (DINs) are registered. In markets where it is available (e.g., the United States as Trikafta), it is approved exclusively for cystic fibrosis in patients with at least one F508del mutation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The Taiwan TFDA product monograph (warnings, contraindications) was identified as a blocking data gap (DG001) in this Evidence Pack and could not be reviewed. Full safety assessment cannot be completed until these data are retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (98.11%) to the Elexacaftor → Rheumatoid Arthritis prediction, but this score reflects knowledge-graph proximity rather than clinical or mechanistic evidence. The evidence level is L5 (model prediction only): the sole retrieved clinical trial does not study RA patients, and no literature directly supports this indication. The mechanistic gap between CFTR correction and RA pathophysiology is substantial, with no established point of pharmacological intersection.

**To proceed, the following is needed:**
- Preclinical data (cell-line or animal model) demonstrating that CFTR modulation directly alters RA-relevant immune pathways (JAK-STAT, TNF, IL-17, or B-cell activation)
- MOA documentation from DrugBank (DG002) confirming whether Elexacaftor has any off-target immunomodulatory effects beyond CFTR
- Safety and contraindication data from the TFDA product monograph (DG001) before any patient-level evaluation
- A disease-directed clinical signal — at minimum, a mechanistic pilot study or case series in RA patients or RA-relevant models
- Clarification of whether ETI's systemic anti-inflammatory effect in CF patients is CFTR-dependent or a secondary consequence of improved pulmonary health

> **Reviewer Note:** Among all 10 TxGNN predictions in this pack, **Pulmonary Hypertension (rank 10)** carries the highest real-world evidence level (L4, "Research Question") with 1 clinical trial and 7 publications, including an imaging study showing ETI-related lung perfusion improvements (PMID 38573129). If repurposing exploration is to be prioritised, CF-associated pulmonary hypertension represents a more scientifically grounded starting point than rheumatoid arthritis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

