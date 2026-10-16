---
layout: default
title: Prilocaine
parent: Model Prediction Only (L5)
nav_order: 769
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Prilocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Premature ejaculation"
monitor_inn: "PRILOCAINE"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
---

# Prilocaine
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

# Prilocaine: From Premature Ejaculation to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide-type local anesthetic. The knowledge graph lists premature ejaculation and psychologic dyspareunia as its original indications, and it is marketed in Canada in dental, injectable and topical products.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Premature ejaculation; psychologic dyspareunia (from the knowledge graph, as the Canadian licence records contain no indication text) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Prilocaine belongs to the sodium channel-blocking local anesthetics, and its numbing effect on peripheral nerves is well established. A link to allergic or inflammatory ocular surface disease is speculative.

The original indications relate to genital sensitivity and pain, where a topical anesthetic effect is plausible. Papillary conjunctivitis is an inflammatory, often allergic, eye condition, and the data show no clear mechanistic bridge between the two. The high TxGNN score reflects a graph-based pattern and is not supported by trials, literature or demonstrated biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage form and approved-indication text are not recorded for these licences.

| DIN | Product Name |
|---------|------|
| 02435276 | 4% Citanest Plain Dental |
| 02325993 | Oraqix |
| 02347695 | 4% Citanest Forte Dental with Epinephrine 1:200,000 |
| 00886858 | EMLA Cream |
| 00393746 | Prilocaine HCl 4% Epinephrine 1:200000 Injection |
| 02057794 | EMLA Patch |

All six are single-ingredient authorizations with valid status. None has been cancelled.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (graph-derived associations, not package-insert text): hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, coronary artery disease, myocardial infarction, sudden cardiac arrest, heart conduction disease and atrioventricular block, cardiovascular and heart disease, respiratory failure, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, hemoglobinopathy, and hyperthyroidism (including Graves disease and thyrotoxicosis).
- **Drug Interactions**: 22 interactions were identified. Of the 20 detailed in the data compiled, 18 are rated Major, 1 Moderate (liposomal morphine) and 1 Minor (hyaluronidase). The main Major interactions are:
  - Other local anesthetics: lidocaine (systemic and topical), benzocaine (topical), cinchocaine (topical)
  - Antimalarials: chloroquine, primaquine, quinine, tafenoquine
  - Dapsone (systemic and topical)
  - Nitrite and nitric oxide agents: amyl nitrite, nitrous acid, nitric oxide
  - Others: metoclopramide, sulfasalazine, rasburicase, silver nitrate (topical), silver sulfadiazine (topical)

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The papillary conjunctivitis prediction has a very high model score but no trials, no publications and no plausible mechanism in the data. It remains at evidence level L5, so it cannot support a repurposing decision.

Among the other predictions for prilocaine, **neuralgia** (including postherpetic neuralgia) has the strongest support. It reaches L2, with a small Phase 2 open-label study of lidocaine/prilocaine cream (NCT00916942, n=20) and older EMLA studies. That evidence is small and dated, and the combination product makes it hard to attribute any effect to prilocaine alone, so it is better treated as a research question than a ready candidate.

**To proceed, the following is needed:**
- Mechanism of action data, to assess any biological link to ocular surface disease
- Package insert warnings and contraindications from Health Canada, which are required before any safety screening
- Any preclinical or clinical evidence in conjunctivitis, which does not currently exist
- Review of ocular exposure safety, because the Canadian products are dental, injectable and skin-applied and none is an ophthalmic route
- Consideration of whether to prioritize the neuralgia prediction instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

