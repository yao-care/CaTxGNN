---
layout: default
title: Diatrizoate
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diatrizoate: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not specified in the Canadian license data (diagnostic contrast agent)"
monitor_inn: "Diatrizoate"
predicted_indications: ["osteoarthritis susceptibility", "rheumatoid arthritis", "osteoarthritis", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachydactyly-syndactyly syndrome"]
---

# Diatrizoate
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

# Diatrizoate: From Radiographic Contrast Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Diatrizoate is an iodinated, water-soluble radiographic contrast agent, and its original therapeutic indication is not specified in the data compiled for this report.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (top-ranked prediction), but there are **0 clinical trials** and **0 publications** for this prediction.
The prediction is best regarded as a knowledge-graph artifact rather than a pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data (diagnostic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diatrizoate is an iodinated, water-soluble radiographic contrast agent used for diagnostic imaging, and it has no known disease-modifying pharmacology.

No mechanistic link was identified between diatrizoate and osteoarthritis susceptibility. The high TxGNN score appears to reflect proximity within the knowledge graph rather than biological rationale. "Susceptibility" is also a genetic-risk concept, not a treatable clinical condition.

The same pattern holds for the other top-ranked predictions:

| Rank | Predicted Disease | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Rheumatoid arthritis | 99.02% | L5 | The only paper is a 1984 laboratory cell-separation method in which diatrizoate is a component of the medium, not a treatment |
| 3 | Osteoarthritis | 98.95% | L4 | The only paper uses contrast-enhanced micro-CT as a diagnostic imaging tool, not as a therapy |
| 4 | Hemoglobinopathy | 98.46% | L4 | The literature signals possible haematological harm, not benefit |
| 5–10 | Rare skeletal/congenital syndromes (e.g., brachyolmia, myosclerosis) | 98.07–98.35% | L5 | No mechanistic link or clinical evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (osteoarthritis susceptibility), currently no related literature is available.

Literature found for other predicted indications (none is therapeutic evidence):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6491310](https://pubmed.ncbi.nlm.nih.gov/6491310/) | 1984 | Laboratory methodology | J Immunol Methods | Ficoll-Hypaque density-gradient separation of blood cells in rheumatoid arthritis patients; diatrizoate is a medium component only (rheumatoid arthritis) |
| [25602512](https://pubmed.ncbi.nlm.nih.gov/25602512/) | 2015 | Imaging/observational | Connect Tissue Res | EPIC micro-CT used to measure sGAG content in elderly hip cartilage; diagnostic use of contrast (osteoarthritis) |
| [18080596](https://pubmed.ncbi.nlm.nih.gov/18080596/) | 2007 | Experimental (in vivo) | Niger J Med | Effects of intravenous sodium meglumine diatrizoate on haematological parameters (hemoglobinopathy) |
| [13936563](https://pubmed.ncbi.nlm.nih.gov/13936563/) | 1963 | Review/toxicology | J Med Assoc Ga | Serious toxic reactions to commonly used drugs; full text review needed (hemoglobinopathy) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02228564 | GASTROGRAFIN | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 records; the main ones listed here are Major-level.
- Metformin
- Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
- Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
- Aminoglycosides and related antibiotics: kanamycin, neomycin, streptomycin, polymyxin B, vancomycin
- Ketorolac
- Acyclovir

Moderate-level interactions include mannitol, acebutolol, acetazolamide and nifedipine.

Warnings and contraindications from the package insert are not available in the data compiled for this report. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by model scores, with no clinical trials and no therapeutic literature. Diatrizoate is a diagnostic contrast agent with no plausible disease-modifying mechanism, and the high scores appear to be knowledge-graph artifacts. The hemoglobinopathy literature points toward potential harm rather than benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- The approved indication text for the Canadian license
- A credible biological rationale and therapeutic-use evidence for any predicted indication, since none has been identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

