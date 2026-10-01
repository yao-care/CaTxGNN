---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 928
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma / Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical ophthalmic prostaglandin analog, used in Canada for glaucoma and ocular hypertension. The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal with no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / ocular hypertension (inferred from the trial and literature context; the license records contain no indication text) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Travoprost is known as a topical FP-receptor (prostaglandin F2α) agonist. Its efficacy in lowering intraocular pressure is established through the many trials in glaucoma and ocular hypertension.

The link to visceral calciphylaxis is weak. Calciphylaxis involves calcification and occlusion of small vessels. Travoprost's only vascular effect seen in the evidence is vasodilation, which appears as conjunctival hyperemia, a side effect rather than a therapeutic effect. Topical ocular dosing also gives minimal systemic exposure, so no plausible pathway to a visceral vascular disease has been identified. The high score is therefore best read as a graph-based association, not a mechanistic finding.

The same pattern holds for the other top-ranked predictions. All of them lack therapeutic evidence:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Evidence Found |
|------|------|------|------|------|
| 1 | Visceral calciphylaxis | 99.9998% | L5 | None |
| 2 | Arterial thoracic outlet syndrome | 99.9998% | L5 | None |
| 3 | Venous thoracic outlet syndrome | 99.9998% | L5 | None |
| 4 | Neurogenic thoracic outlet syndrome | 99.9997% | L5 | None |
| 5 | Vascular disease | 99.9997% | L5 | 15 trials and 20 publications, all on glaucoma or hyperemia side effects |
| 6 | Angiodysplasia of stomach | 99.9997% | L5 | None |
| 7 | Blue toe syndrome | 99.9997% | L5 | None |
| 8 | Idiopathic spontaneous coronary artery dissection | 99.9997% | L5 | None |
| 9 | Lymphangiectasis | 99.9997% | L5 | None |
| 10 | Hemangioendothelioma | 99.9997% | L4 | 2 publications: an adverse-event case report and a context review |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

---

## Canada Market Information

Six licenses are on record; the five main ones are listed. Dosage form and approved-indication text are not available in the input.

| DIN | Product Name |
|---------|------|
| 2457997 | IZBA |
| 2318008 | TRAVATAN Z |
| 2548089 | JAMP TRAVOPROST Z |
| 2413167 | SANDOZ TRAVOPROST |
| 2415305 | APO-TRAVOPROST-TIMOP PQ |

---

## Safety Considerations

Please refer to the package insert for safety information.

One signal from the wider evidence is worth noting. A case report (PMID 19107053) describes uveal effusion with exudative retinal detachment induced by topical travoprost in a patient with Sturge-Weber syndrome, a condition involving vascular malformations. Caution is therefore warranted in patients with vascular malformations or tumours.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no literature, and no plausible mechanism linking a topical ophthalmic FP-receptor agonist to visceral calciphylaxis. The other top-ranked vascular predictions show the same pattern, and the one signal in the evidence is a safety concern, not a benefit.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a pathophysiological rationale connecting FP-receptor signalling to calcific vasculopathy
- Preclinical evidence in calciphylaxis or vascular calcification models
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Confirmation of the approved indication text and dosage forms for the Canadian licenses
- Assessment of whether any route of administration beyond topical ophthalmic dosing could achieve relevant systemic exposure

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

