---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 743
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Piroxicam: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis"
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
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

## Piroxicam: From Rheumatoid Arthritis and Osteoarthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Piroxicam is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental disorder.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis (from knowledge-graph indication data; no indication text was available in the Canadian licence records) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Piroxicam is an NSAID, and its efficacy in rheumatoid arthritis and osteoarthritis is established. It is understood to act by inhibiting COX-1 and COX-2, which reduces prostaglandin-driven inflammation and pain.

The predicted condition is a rare developmental syndrome affecting the eye and skeleton. No plausible link to COX inhibition was identified. The high score most likely reflects the model's network proximity to other skeletal and arthropathy terms, not a biological rationale. It should be treated as a computational signal only.

Several other top-ranked predictions are also rare skeletal or genetic disorders (for example brachydactyly-syndactyly syndrome and acromesomelic dysplasia, Hunter-Thompson type). They share the same weakness: high scores with no clinical or mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|------|
| 00642894 | APO PIROXICAM CAP 20MG | Valid (single-ingredient) |
| 00642886 | APO PIROXICAM CAP 10MG | Valid (single-ingredient) |
| 00695718 | TEVA-PIROXICAM | Valid (single-ingredient) |
| 00695696 | TEVA-PIROXICAM | Valid (single-ingredient) |

All four authorizations are valid single-ingredient products, and none are cancelled.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from the product label): hypertension, kidney disease, liver disease (including acute liver failure, hepatitis and drug-induced liver injury), congestive heart failure and other cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, active peptic ulcer disease, blood coagulation disorders, thrombotic disease, anaemia and haemoglobinopathies, gallbladder disease, substance abuse/dependence, and vision disorders.
- **Drug Interactions**: 100 interactions are recorded in total. The main ones listed are mostly of Moderate severity:
  - Other anti-inflammatory and anti-ulcer agents: acetylsalicylic acid, mesalazine, balsalazide.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide.
  - Antidiabetic drugs: metformin, glimepiride, chlorpropamide.
  - Others: aprepitant, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes.
  - Minor interactions: famotidine, ranitidine, cimetidine, linaclotide.

The product label's warnings and contraindications were not available for this report. Please refer to the package insert before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (Evidence Level L5). There is also no credible mechanistic link between COX inhibition and this developmental syndrome. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- A mechanistic hypothesis connecting piroxicam to this syndrome's biology, plus any preclinical data.
- Detailed mechanism of action data (MOA) and the Health Canada package insert warnings and contraindications.
- Consideration of a better-supported alternative. Among the model's lower-ranked predictions, **juvenile idiopathic arthritis** (rank 10, score 99.93%) has an L3 evidence level. It includes a multicentre double-blind crossover trial of piroxicam versus naproxen in 47 children ([PMID 3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/), 1986), a randomized comparison in 26 patients ([PMID 2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/), 1987) and a paediatric pharmacokinetic study ([PMID 1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/), 1991). This evidence is old, symptomatic only and of limited quality, and current juvenile idiopathic arthritis care relies mainly on DMARDs and biologics. It could still be a more realistic research question than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

