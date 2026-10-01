---
layout: default
title: Polyethylene Glycol 400
parent: Model Prediction Only (L5)
nav_order: 742
evidence_level: L5
indication_count: 2
---

# Polyethylene Glycol 400
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Polyethylene Glycol 400: From Ophthalmic Eye Drop Ingredient to Bronchitis

## One-Sentence Summary

Polyethylene Glycol 400 (PEG 400) is a pharmaceutical excipient and solvent, marketed in Canada as an ingredient in eye drop products.
The TxGNN model predicts it may be effective for **bronchitis**, but the evidence is weak: **0 relevant clinical trials** and **0 publications** support this direction.
The five trials retrieved were keyword matches on "polyethylene glycol" and concern an unrelated PEGylated anaemia drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data. The products are eye drops (inferred from product names). |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. PEG 400 is a pharmaceutical excipient, solvent and lubricant or humectant vehicle. It has no established anti-inflammatory, mucolytic or antimicrobial activity in the airway.

The high TxGNN score (99.58%) is most likely a knowledge-graph artifact from polyethylene glycol name and structure associations, not biological evidence. No credible mechanism links PEG 400 to bronchitis.

The second-ranked prediction, **congenital ichthyosiform erythroderma** (score 99.10%), is also speculative. PEG 400 is a humectant used in topical products and could in theory aid skin hydration, but that is not evidence of efficacy in a genetic keratinisation disorder. No trials or literature were found for it.

---

## Clinical Trial Evidence

The retrieved trials were all graded **not relevant**. They study Mircera (methoxy polyethylene glycol-epoetin beta), a PEGylated erythropoiesis-stimulating agent, in renal anaemia. None involves PEG 400 or bronchitis. They are listed for transparency only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00559273](https://clinicaltrials.gov/study/NCT00559273) | Phase 3 | Completed | 307 | Mircera vs darbepoetin in renal anaemia (CKD, not on dialysis). Not relevant. |
| [NCT01519947](https://clinicaltrials.gov/study/NCT01519947) | Phase 4 | Completed | 87 | Effect of altitude on Mircera dosing in renal anaemia. Not relevant. |
| [NCT01422824](https://clinicaltrials.gov/study/NCT01422824) | N/A (observational) | Completed | 185 | Safety and efficacy of Mircera in haemodialysis patients. Not relevant. |
| [NCT01379963](https://clinicaltrials.gov/study/NCT01379963) | N/A (observational) | Completed | 780 | Retrospective haemoglobin levels in Mircera-treated patients. Not relevant. |
| [NCT01309295](https://clinicaltrials.gov/study/NCT01309295) | N/A (observational) | Completed | 250 | Mircera in predialysis and dialysis CKD patients. Not relevant. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2518228 | RED EYE WORKPLACE |
| 2518201 | RED EYE TRIPLE ACTION |
| 2344319 | ADVANCED RELIEF EYE DROPS |

Dosage form, manufacturer and approved indication text are not recorded for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). There is no plausible mechanism, no relevant trial and no literature. PEG 400 is an excipient, so the high score is likely a naming artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank, to check for any airway-relevant pathway
- Original approved indication text for the three DINs
- Relevant clinical or preclinical evidence for PEG 400 in bronchitis, or in congenital ichthyosiform erythroderma
- A route-compatibility assessment, since current products are ophthalmic and a respiratory or systemic route has not been evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

