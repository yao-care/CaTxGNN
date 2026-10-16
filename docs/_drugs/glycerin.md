---
layout: default
title: Glycerin
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Glycerin: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Constipation disorder"
---

# Glycerin
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

# Glycerin: From Constipation to Cauda Equina Syndrome

## One-Sentence Summary

Glycerin is an osmotic agent originally used to treat constipation, and it is also found in many over-the-counter eye drops in Canada.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this prediction.
The prediction is graph-based only, and the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycerin is an osmotic agent. Its efficacy in constipation is established, and it is also widely used as a lubricant in eye drops.

For cauda equina syndrome, no mechanistic link has been identified. The high score appears to come from the structure of the knowledge graph only. Cauda equina syndrome is a surgical emergency caused by compression of the nerve roots. Glycerin has no established neuroprotective or decompressive role in it, so the prediction is not biologically convincing.

### Other Candidates Considered

The other top-ranked predictions are listed below. None has clinical trial support.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Open-angle glaucoma | 99.59% | L4 | Oral glycerin lowers intraocular pressure through an osmotic effect, but it has historically been used for acute angle-closure episodes. The retrieved literature is indirect. |
| 3 | Primary hereditary glaucoma | 99.56% | L5 | Prediction only. This form is usually managed surgically. |
| 4 | Alopecia | 99.55% | L4 | No credible mechanism. Glycerin appears only as an excipient in the literature. |
| 6 | Irritable bowel syndrome | 99.49% | L4 | Plausible for constipation-predominant IBS, but it is close to the original indication and the literature is weak. |
| 9 | Migraine disorder | 99.27% | L5 | No mechanistic link. The one article retrieved concerns epistaxis. |

Ranks 5, 7, 8 and 10 (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, migraine with brainstem aura) are prediction only, with no supporting data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For open-angle glaucoma, the strongest alternative candidate, the retrieved articles are only indirectly related:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1614157](https://pubmed.ncbi.nlm.nih.gov/1614157/) | 1992 | Review | Klin Monbl Augenheilkd | Pathogenesis and treatment of primary angle-closure glaucoma. This is a different glaucoma type. |
| [32890110](https://pubmed.ncbi.nlm.nih.gov/32890110/) | 2020 | Other | J Glaucoma | Glycerin-preserved donor corneoscleral patch grafts for glaucoma drainage devices. This is tissue preservation, not a drug effect. |
| [20872359](https://pubmed.ncbi.nlm.nih.gov/20872359/) | 2011 | Other | Eur J Ophthalmol | Osmoprotective artificial tears for ocular surface damage caused by glaucoma therapy. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02389886 | DRY EYE TEARS | Not specified | Not specified |
| 02321696 | LUBRICANT EYE DROPS / ARTIFICIAL TEARS | Not specified | Not specified |
| 02354535 | ARTIFICIAL TEARS | Not specified | Not specified |
| 02438585 | VISINE FOR DRY EYE TIRED EYE RELIEF | Not specified | Not specified |
| 02360837 | CLEAR EYES EXTRA STRENGTH REDNESS RELIEF | Not specified | Not specified |

There are 13 valid single-ingredient licences in total. The listed products are mainly ophthalmic lubricants, not constipation products. The approved indication text is not available for any of them.

---

## Safety Considerations

- **Drug Interactions**: 220 interactions were recorded. The listed ones are mostly Moderate, for example abiraterone, tramadol, acetazolamide, hydrocortisone, salbutamol, hydrochlorothiazide, amiodarone and propofol. Doxycycline is the only Minor one on the list.
- **Systemic osmotic risks**: Where glycerin is used systemically as an osmotic agent, hyperglycaemia, dehydration and nausea can limit chronic use.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of cauda equina syndrome rests only on a graph-based score. There are no trials, no publications and no plausible mechanism. It is a surgical emergency for which glycerin has no recognized role. Across all ten predictions, none has direct clinical support. Open-angle glaucoma and irritable bowel syndrome have some biological plausibility but still lack direct evidence.

**To proceed, the following is needed:**
- Mechanism of action data for glycerin
- Package insert warnings and contraindications from Health Canada, which are needed before any safety screening
- Dosage form and approved indication details for the Canadian licences
- Direct clinical or mechanistic evidence for the chosen indication. If the programme is redirected, open-angle glaucoma or constipation-predominant IBS are the more plausible candidates to investigate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

