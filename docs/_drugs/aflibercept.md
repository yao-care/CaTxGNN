---
layout: default
title: Aflibercept
parent: Model Prediction Only (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Metastatic Colorectal Cancer and Retinal Disease to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF-blocking "trap" protein, originally used for metastatic colon cancer and retinal diseases such as macular degeneration, retinal artery occlusion and diabetic macular edema.
The TxGNN model predicts it may be effective for **esotropia**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastasis from malignant tumour of colon; macular degeneration; retinal artery occlusion; diabetic macular edema (approved-indication text is not available in the Canadian licence records) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, aflibercept acts as a trap for VEGF-A, VEGF-B and placental growth factor (PlGF), which drives its use in diseases with abnormal blood vessel growth or leakage, such as retinal disease and colorectal cancer.

Esotropia is a form of strabismus (inward eye turning) driven mainly by neuromuscular and sensorimotor factors. No clear mechanistic route from VEGF blockade to esotropia is evident. The high TxGNN score most likely reflects the drug's association with eye-related diseases in the knowledge graph rather than a true biological link, and the prediction should be treated as a hypothesis only.

Other predictions in the list are similarly weak. The most plausible are:
- **Esophageal varices (with or without bleeding):** anti-angiogenic therapy has an indirect rationale, but systemic VEGF blockade carries bleeding risk.
- **Rare tumours** (ectomesenchymoma, malignant cutaneous granular cell tumour, middle ear neuroendocrine tumour): a general anti-angiogenic rationale exists, but there are no data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for esotropia.

One trial was linked to another predicted term (hemorrhagic disease of newborn), but it is an ophthalmic study and appears to be a mismatched term mapping:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02537054](https://clinicaltrials.gov/study/NCT02537054) | Phase 2 | Completed | 15 | Intravitreal aflibercept for choroidal neovascularization and fibrovascular proliferation in pseudoxanthoma elasticum; assesses preservation or improvement of visual acuity. Not relevant to esotropia. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02558238 | YESAFILI | Not available | Not available |
| 02554178 | AFLIVU | Not available | Not available |
| 02415992 | EYLEA | Not available | Not available |
| 02535858 | YESAFILI | Not available | Not available |
| 02505355 | EYLEA | Not available | Not available |

Ten valid single-ingredient licences are listed in total (including PAVBLU, ENZEEVU and EYLEA HD); the five above are shown as the main ones.

---

## Safety Considerations

- **Drug Interactions:** 78 interactions were identified. Major-level examples include deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine and clozapine. Moderate-level examples include roflumilast, chloramphenicol, zidovudine, azathioprine and alemtuzumab.
- **Class-related concern:** Systemic VEGF blockade carries hemorrhage risk, which is particularly relevant to the bleeding-related predictions.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction rests on the model score alone (L5). There are no trials or publications, and no plausible mechanistic link between VEGF blockade and a neuromuscular or sensorimotor strabismus disorder.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale for esotropia
- Preclinical or clinical evidence in strabismus
- Health Canada package insert warnings and contraindications for a safety review
- Dosage form, route and approved-indication details for the Canadian licences
- Assessment of route compatibility and the bleeding-risk profile for any systemic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

