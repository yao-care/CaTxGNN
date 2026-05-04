---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Wet Age-Related Macular Degeneration to Esotropia

## One-Sentence Summary

Aflibercept (marketed globally as Eylea and Zaltrap) is a recombinant VEGF-trap fusion protein approved in major markets for neovascular (wet) age-related macular degeneration, diabetic macular edema, and metastatic colorectal cancer — though it carries no active licenses in this jurisdiction.
The TxGNN model predicts it may be effective for **Esotropia** (convergent strabismus), with a prediction score of **99.38%**.
However, **0 clinical trials** and **0 publications** currently support this specific repurposing direction, making this a model-prediction-only finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Wet age-related macular degeneration, diabetic macular edema, metastatic colorectal cancer (global approvals; no local license on file) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Market Status | Not Marketed (0 licenses) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Aflibercept is a recombinant fusion protein constructed from the extracellular ligand-binding domains of VEGF receptor 1 (VEGFR-1) and VEGF receptor 2 (VEGFR-2) fused to the Fc region of human IgG1. It functions as a high-affinity "VEGF trap," sequestering VEGF-A, VEGF-B, and placental growth factor (PlGF) before they can activate their endogenous receptors. This suppresses pathological angiogenesis and reduces vascular hyperpermeability — the mechanisms underlying its approved uses in wet AMD and macular edema.

Esotropia is a form of strabismus in which one or both eyes deviate inward toward the nose. The theoretical bridge between VEGF inhibition and esotropia is indirect at best: clinical observations following intravitreal anti-VEGF treatment for retinopathy of prematurity (ROP) have noted altered rates of subsequent strabismus in treated infants, suggesting that VEGF signaling may play some role in neurovascular development of ocular alignment. However, this represents an epidemiological side-effect observation, not a validated therapeutic rationale.

The most plausible explanation for the high TxGNN score is **knowledge graph topology bias**: Aflibercept is densely connected to ophthalmology-related nodes (AMD, DME, ROP, retinal vein occlusion), and esotropia, being an eye disorder, shares the same graph neighborhood. The model may be picking up on co-occurrence within the ophthalmic disease cluster rather than a genuine mechanistic signal. No direct biological hypothesis currently supports Aflibercept as a primary treatment for esotropia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Aflibercept is **not currently marketed** in this jurisdiction (0 licenses on file). No approved product monograph or local regulatory review was available for this assessment.

For reference, Aflibercept is globally available as:

| Product | Route | Key Approved Indications (Reference Markets) |
|---------|-------|----------------------------------------------|
| Eylea (2 mg/0.05 mL) | Intravitreal injection | Wet AMD, Diabetic Macular Edema, Macular Edema following RVO, Diabetic Retinopathy |
| Eylea HD (8 mg/0.07 mL) | Intravitreal injection | Wet AMD, DME (extended dosing interval formulation) |
| Zaltrap (25 mg/mL) | IV infusion | Metastatic colorectal cancer (combined with FOLFIRI after oxaliplatin failure) |

---

## Safety Considerations

Please refer to the package insert for safety information. No local product monograph, warning text, contraindications, or drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.38%), the esotropia prediction for Aflibercept has no clinical trial evidence, no supporting literature, and no established mechanistic hypothesis linking VEGF-trap activity to the treatment of convergent strabismus. The score almost certainly reflects ophthalmology co-occurrence bias in the knowledge graph rather than genuine drug-disease biological plausibility. Additionally, Aflibercept is not marketed in this jurisdiction, meaning there is no existing regulatory pathway to leverage for a rapid repurposing study.

**To proceed, any of the following would be required:**

- A credible mechanistic hypothesis demonstrating how VEGF-A/B or PlGF inhibition could correct or prevent esotropia (currently absent)
- Preclinical data (animal models of strabismus) showing an anti-VEGF effect on extraocular muscle alignment
- Epidemiological analysis of esotropia rates in ROP patients treated with anti-VEGF agents versus laser photocoagulation, to determine if any protective signal exists
- Graph topology analysis of TxGNN to confirm whether this high score reflects genuine signal or neighborhood bias in the ophthalmology subgraph
- Resolution of local regulatory data gaps (no licensed product, no local safety monograph) before any clinical exploration could be considered

> **Research Note:** Among the 10 predicted indications reviewed in this evidence pack, **esophageal varices without bleeding** (Rank 2) and **middle ear neuroendocrine tumor** (Rank 10) carry stronger mechanistic rationale based on VEGF-driven portal hypertension angiogenesis and NET vascular biology, respectively. If resources are limited, those indications may offer more defensible hypotheses for preclinical investigation than esotropia.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

