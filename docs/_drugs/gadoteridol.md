---
layout: default
title: Gadoteridol
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gadoteridol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Gadoteridol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "congestive heart failure", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "myosclerosis"]
---

# Gadoteridol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Gadoteridol: From MRI Contrast Imaging to Osteoarthritis Susceptibility
{: .text-alpha }

## One-Sentence Summary

Gadoteridol (marketed in Canada as PROHANCE) is a gadolinium-based contrast agent used in magnetic resonance imaging (MRI). The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** behind it. The related disease **osteoarthritis** has 10 publications, and these describe diagnostic imaging use, not treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian license lists no indication text; the drug is known as an MRI contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gadoteridol is a non-ionic, gadolinium-based contrast agent. It improves the visibility of tissues on MRI and has no known therapeutic mechanism against disease.

The high score appears to be a computational artefact rather than a biological signal. Osteoarthritis susceptibility is a genetic-risk concept, and no plausible link to a contrast agent has been identified. Other top-ranked predictions (skeletal dysplasias such as brachyolmia, hemoglobinopathy, myosclerosis) show the same pattern: high scores without supporting evidence. The score may reflect similarity to neighbouring nodes in the knowledge graph.

The literature on the closely related **osteoarthritis** and **rheumatoid arthritis** predictions is real but diagnostic. Gadoteridol serves as an imaging probe, for example to quantify cartilage proteoglycan content in CT studies or to enhance inflamed synovium on MRI. These studies suggest a possible **diagnostic imaging research question**, not a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for the top prediction (osteoarthritis susceptibility). The table below shows the most relevant publications for the related predictions, **osteoarthritis** (rank 2) and **rheumatoid arthritis** (rank 3). All are diagnostic imaging studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Ex vivo imaging | J Orthop Res | Triple-contrast CT (bismuth nanoparticles, CA4+, gadoteridol) segments cartilage and shows site-specific biomechanical differences in cadaveric knees |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | Proof-of-concept imaging | Sci Rep | Photon-counting CT with dual contrast tracked gadoteridol diffusion in bovine cartilage and correlated it with biomechanical properties |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | Ex vivo imaging | Sci Rep | Dual-contrast photon-counting CT for quantitative assessment of articular cartilage health |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | Ex vivo imaging | J Orthop Res | Examined how cartilage constituents affect simultaneous diffusion of cationic and non-ionic contrast agents |
| [31576504](https://pubmed.ncbi.nlm.nih.gov/31576504/) | 2020 | Ex vivo imaging | Ann Biomed Eng | Triple-contrast CT evaluates cartilage composition and segmentation at the same time |
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Ex vivo imaging | J Orthop Res | Dual contrast (iodine-based cationic plus gadoteridol) characterizes cartilage earlier than single contrast |
| [31535728](https://pubmed.ncbi.nlm.nih.gov/31535728/) | 2020 | Ex vivo imaging | J Orthop Res | Synchrotron microCT with dual contrast for quantitative assessment of human cartilage composition |
| [8689824](https://pubmed.ncbi.nlm.nih.gov/8689824/) | 1996 | Diagnostic imaging dose study | Clin Radiol | In 19 rheumatoid arthritis patients, 0.3 mmol/kg gadoteridol enhanced inflamed synovium more than 0.1 mmol/kg |
| [9010087](https://pubmed.ncbi.nlm.nih.gov/9010087/) | 1996 | Diagnostic imaging dose study | Br J Rheumatol | Significant dose-dependent difference in synovial enhancement (0.1 vs 0.3 mmol/kg) |
| [8867431](https://pubmed.ncbi.nlm.nih.gov/8867431/) | 1996 | Diagnostic imaging study | Der Radiologe | Compared gadoteridol with Gd-DTPA for MR diagnosis of rheumatoid joint changes |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229056 | PROHANCE | Not listed | Not listed |

---

## Safety Considerations

- **Drug Interactions**: 19 interactions were identified, all rated **Moderate**. All involve beta-blockers: acebutolol, atenolol, betaxolol (systemic and ophthalmic), bisoprolol, carvedilol, esmolol, labetalol, metoprolol, nadolol, nebivolol, pindolol, propranolol, sotalol, timolol (systemic and ophthalmic), carteolol (ophthalmic), levobunolol (ophthalmic) and metipranolol (ophthalmic).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature (L5). The supporting publications for related conditions concern diagnostic imaging, not therapeutic effect. No therapeutic mechanism has been identified, so repurposing gadoteridol as a treatment is not supported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- If the aim is diagnostic imaging, a separate research question focused on cartilage or synovial imaging, rather than therapeutic repurposing
- Original indication text and dosage form details for the Canadian license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

