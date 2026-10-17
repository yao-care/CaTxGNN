---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Iodixanol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not available in the data compiled for this report (iodixanol is an i…"
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "hemoglobinopathy", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "pseudoachondroplasia"]
---

# Iodixanol
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

# Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is an iodinated radiographic contrast agent, marketed in Canada as VISIPAQUE and as generic iodixanol injections.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (top-ranked prediction), but there are **0 clinical trials** and **0 publications** for this specific indication.
The prediction is computational only, and the literature found for related osteoarthritis predictions concerns diagnostic imaging use, not treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (iodixanol is an iodinated contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iodinated, iso-osmolar radiocontrast agent. It works by absorbing X-rays, which improves image contrast, and it has no known therapeutic pharmacological action.

The analysis found no plausible mechanistic link between iodixanol and genetic susceptibility to osteoarthritis. The high score (0.992) most likely reflects co-occurrence or network proximity in the knowledge graph rather than a real therapeutic effect.

Literature on the closely related prediction of **osteoarthritis** shows iodixanol used as an imaging tool. Examples are CT-based cartilage imaging, solute transport studies across the cartilage-bone interface, and compatibility with platelet-rich plasma. This is diagnostic use and does not support a disease-modifying or symptom-relieving effect.

The other top-10 predictions are rheumatoid arthritis, hemoglobinopathy, and several rare skeletal or genetic dysplasias (brachyolmia, Hunter-Thompson acromesomelic dysplasia, pseudoachondroplasia, and others). None has a supporting mechanism or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

There is no literature for the top-ranked prediction (osteoarthritis susceptibility). The table below shows publications retrieved for the closely related prediction, **osteoarthritis**. All are non-therapeutic studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging/diagnostic study | Annals of Biomedical Engineering | Nanoparticle diffusion CT imaging combined with finite element modelling to reveal cartilage function |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging/diagnostic study | Annals of Biomedical Engineering | Dual-contrast agent in photon-counting CT to assess articular cartilage health |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Experimental transport study | Journal of Biomechanics | Iodixanol (~1550 Da) used as a CT tracer to study permeability of the cartilage-bone interface in equine and human samples |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational model | Journal of Biomechanics | Finite element model of neutral solute transport across the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | Journal of Experimental Orthopaedics | Iodine contrast agents did not affect platelet-rich plasma function at an early time point |

For rheumatoid arthritis, the only paper found (PMID 36628042, a 2022 case report in Cureus) describes desensitization to a different contrast agent (iohexol). It does not address iodixanol efficacy.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02145766 | VISIPAQUE 270 | Not specified | Not specified |
| 02145774 | VISIPAQUE 320 | Not specified | Not specified |
| 02553953 | IODIXANOL INJECTION 270 | Not specified | Not specified |
| 02553961 | IODIXANOL INJECTION 320 | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. The main ones listed below are mostly rated Major and relate to additive kidney risk or related effects:
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin, polymyxin B
  - **Moderate**: mannitol
  - **Unknown severity**: famotidine, acetylsalicylic acid, morphine, omeprazole, prednisone
- For key warnings and contraindications, please refer to the package insert. Use in sickle cell disease and other hemoglobinopathies is a safety consideration for contrast agents rather than a therapeutic opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials, no therapeutic literature, and no plausible mechanism. The only related publications describe iodixanol as an imaging tool, not as a treatment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, to allow safety screening
- Mechanism of action data
- Approved indication text and dosage forms for the Canadian licences
- Any preclinical or clinical evidence of a therapeutic effect in osteoarthritis. Without it, the drug is better regarded as a diagnostic agent in this setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

