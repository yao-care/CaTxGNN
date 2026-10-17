---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 902
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Tetracaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "TETRACAINE"
predicted_indications: ["neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Tetracaine: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is an ester local anaesthetic, originally associated with dermatitis in the knowledge graph used for this analysis and marketed in Canada mainly as a topical anaesthetic.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but **no clinical trials and no publications** currently support this prediction.
The prediction rests on model output alone and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tetracaine is an ester local anaesthetic that blocks voltage-gated sodium channels, which reduces nerve conduction and produces local numbness.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of *Borrelia* infection (Lyme disease). Sodium channel blockade does not act on this infection or on its skin atrophy. No credible mechanistic link could be established. The high score (rank 1,884 in the model's overall ranking) is best read as a knowledge-graph association, probably driven by the shared "skin disease" context with dermatitis, and not as evidence of therapeutic benefit.

Other top-ranked predictions show the same pattern. These include neonatal dermatomyositis, amyopathic dermatomyositis, hydroa vacciniforme, bronchitis, childhood connective-tissue-disease-associated interstitial lung disease, and irritable bowel syndrome. At best, tetracaine could give symptomatic topical anaesthesia, which does not modify the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acrodermatitis chronica atrophicans.

---

## Literature Evidence

Currently no related literature available for acrodermatitis chronica atrophicans.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02148544 | MINIMS TETRACAINE HYDROCHLORIDE | Not specified | Not specified |
| 02230575 | AMETOP GEL 4% | Not specified | Not specified |
| 02148528 | MINIMS TETRACAINE HYDROCHLORIDE | Not specified | Not specified |
| 02398028 | PLIAGLIS | Not specified | Not specified |
| 01930699 | ZAP TOPICAL ANESTHETIC GEL | Not specified | Not specified |

Seven valid single-ingredient licences are on record in total; the five main ones are shown above.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** epilepsy, kidney disease, liver disease, gallbladder disease, heart disease (including cardiovascular disease, sudden cardiac arrest and heart conduction disease), respiratory failure, myasthenia gravis and other neuromuscular junction diseases, butyrylcholinesterase deficiency, hyperthyroidism (Graves disease, thyrotoxicosis), and several eye conditions (uveitis, iris and ciliary body disease, panuveitis, eye infections, conjunctivitis).
- **Drug interactions:** 32 interactions were identified. Two are rated **Major**: nitrous acid and liposomal bupivacaine. Most of the others are Moderate, including other local anaesthetics (lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine), benzodiazepines (alprazolam, chlordiazepoxide, clobazam, clonazepam, diazepam, estazolam), sulfonamides (sulfasalazine, sulfamethoxazole). Hyaluronidase is Minor.
- **Neurotoxicity signal:** For the lower-ranked prediction of cauda equina syndrome, the literature (case reports, reviews and animal studies) describes tetracaine as a *cause* of the syndrome after spinal administration. This is an adverse-effect signal, not a therapeutic one, and this prediction should be excluded as a repurposing candidate.

Package-insert warnings and contraindications for the Canadian products were not available in the data compiled for this report. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications, and there is no plausible mechanistic link between sodium channel blockade and a *Borrelia*-related skin infection. The only trial found for any predicted indication (acne keloidalis nuchae) tested tetracaine cream for procedural pain relief, not disease treatment.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications for the Canadian products (currently a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) and a credible biological rationale for the predicted indication
- Any preclinical or clinical evidence in the predicted disease
- Assessment of route compatibility, since the marketed products are topical or ophthalmic and the indication may need a different route
- Consideration of whether a symptom-control use (topical anaesthesia of skin lesions) is a more realistic goal than disease modification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

