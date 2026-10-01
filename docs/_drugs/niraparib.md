---
layout: default
title: Niraparib
parent: Model Prediction Only (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Niraparib is a PARP inhibitor used in oncology; the Evidence Pack identifies ovarian cancer as an already marketed setting. The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but this is a knowledge-graph prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence records (ovarian cancer is referenced as a marketed setting elsewhere in the pack) |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Niraparib inhibits PARP1 and PARP2, enzymes involved in repairing damaged DNA. In tumours that cannot repair DNA through homologous recombination, blocking PARP is "synthetically lethal" and kills the cancer cells. This is the basis for its use in ovarian cancer.

For epiglottis neoplasm, no disease-specific rationale was provided. There is no biomarker data (such as homologous recombination deficiency or BRCA status), no preclinical work and no clinical evidence for this site. The high score comes only from the model's knowledge-graph patterns, so the prediction should be treated as a hypothesis rather than a finding.

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
| 2530031 | ZEJULA |
| 2538555 | AKEEGA |
| 2538563 | AKEEGA |

Dosage forms and approved indication text were not included in the supplied records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | Myelosuppression is a recognised concern for this drug class; please refer to the package insert warnings and precautions for specifics |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count is the usual baseline; please refer to the package insert for the full monitoring schedule |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for niraparib in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials, no literature and no disease-specific mechanistic rationale for epiglottis neoplasm. The Health Canada safety information has also not yet been obtained.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, interactions) to complete safety screening
- Disease-specific evidence for epiglottis neoplasm, such as HRD/BRCA prevalence in head and neck tumours and preclinical data
- Approved indication text and dosage forms for the three Canadian DINs
- For comparison, the rank 2 prediction (cystic neoplasm, a proxy for serous carcinomas) has a Phase 2 trial in endometrial serous carcinoma (NCT04716686, recruiting, 83 participants) and a stronger rationale (evidence level L3). It may be a better candidate for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

