---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Latanoprostene Bunod: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "LATANOPROSTENE BUNOD"
predicted_indications: ["visceral calciphylaxis", "primary hereditary glaucoma", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "idiopathic spontaneous coronary artery dissection", "angiodysplasia of stomach", "lymphangiectasis", "hemangioendothelioma"]
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Latanoprostene bunod is an eye drop originally used to lower eye pressure in **open-angle glaucoma** and **ocular hypertension**.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** directly supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, latanoprostene bunod releases two active components: latanoprost acid, a prostaglandin F receptor (FP) agonist, and nitric oxide (NO), a vasodilator. Its efficacy in lowering eye pressure is established. The FP receptor (PTGFR) is its recorded pharmacological target.

The link to visceral calciphylaxis is speculative. NO/cGMP signalling may in theory counter vascular calcification. However, the drug is given as an eye drop, which produces very low exposure in the rest of the body. A systemic effect on a disease such as calciphylaxis is therefore implausible. The high score reflects model output, not clinical or mechanistic support.

Other top-ranked predictions in the data compiled for this report show the same pattern:
- **Primary hereditary glaucoma** (score 99.71%): the most biologically plausible one, since it is close to the approved use. No specific trials or literature exist, and congenital or paediatric glaucoma often responds poorly to medical therapy, so extrapolation needs caution.
- **Thoracic outlet syndromes (venous, arterial, neurogenic)**, **spontaneous coronary artery dissection**, **gastric angiodysplasia** and **lymphangiectasis**: no credible mechanistic link and no clinical evidence.
- **Vascular disease** and **hemangioendothelioma**: only indirect evidence, described below.

---

## Clinical Trial Evidence

No clinical trials are registered for visceral calciphylaxis.

The only trial found for the broader predicted category "vascular disease" (rank 6) is shown below. It is about eye blood vessels, not systemic vascular disease, and offers only indirect information.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03931317](https://clinicaltrials.gov/study/NCT03931317) | N/A | Completed | 70 | Randomized crossover study comparing latanoprostene bunod with timolol on retinal blood vessel density and visual acuity in ocular hypertension or primary open-angle glaucoma |

---

## Literature Evidence

No publications are available for visceral calciphylaxis.

Related publications found for other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30028313](https://pubmed.ncbi.nlm.nih.gov/30028313/) | 2018 | Review | Neural Regeneration Research | Overview of treatment options for glaucomatous optic neuropathy (for "vascular disease"; indirect) |
| [38113361](https://pubmed.ncbi.nlm.nih.gov/38113361/) | 2023 | Case report | Ophthalmic Surgery, Lasers & Imaging Retina | An 11-year-old with a port-wine birthmark, choroidal haemangioma and glaucoma developed serous retinal detachment on prostaglandin analogues, including latanoprostene bunod. This is a possible adverse event, not a treatment benefit (for "hemangioendothelioma") |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02484218 | VYZULTA | Not specified | Not specified |

---

## Safety Considerations

- **Drug target:** The drug acts on the prostanoid FP receptor (PTGFR). No other interacting drugs were identified.
- **Safety signal from the literature:** A 2023 case report described serous retinal detachment in a child with a port-wine birthmark and choroidal haemangioma after prostaglandin analogue therapy, including latanoprostene bunod.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for visceral calciphylaxis rests only on a model score. No trials or publications support it, and the mechanism is speculative. Eye-drop dosing gives minimal systemic exposure, so a systemic effect is unlikely.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- Evidence that a relevant drug level can be reached in the target tissue by an ocular or other route
- Preclinical data on NO/cGMP and FP receptor effects on vascular calcification
- If a nearer indication is of interest, specific evidence for primary hereditary glaucoma, including paediatric and congenital subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

