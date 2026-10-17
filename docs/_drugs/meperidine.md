---
layout: default
title: Meperidine
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Meperidine: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not specified in the available data"
monitor_inn: "Meperidine"
predicted_indications: ["Tourette syndrome", "trichotillomania"]
---

# Meperidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Meperidine: From an Unspecified Original Indication to Tourette Syndrome

## One-Sentence Summary

Meperidine is an opioid medicine marketed in Canada as an injectable hydrochloride product, but the data compiled for this report do not specify its approved indication.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests only on a model score and should not be treated as clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available data |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, meperidine is a mu-opioid receptor agonist with weak serotonin reuptake inhibition and anticholinergic/local anaesthetic-like properties.

A plausible but unverified link is that the opioid system modulates the dopaminergic and cortico-striatal-thalamo-cortical circuits implicated in tics. This reasoning rests on general knowledge, not on the supplied dataset.

There are significant concerns. Mu-opioid agonism carries risks of dependence and respiratory depression. Meperidine's active metabolite, normeperidine, is neurotoxic and can cause seizures. The model's high score reflects network proximity in a knowledge graph and cannot be regarded as evidence of therapeutic benefit.

A second predicted indication, **trichotillomania** (score 99.39%, also L5, Hold), has no supporting trials or literature either. It is mechanistically questionable, because opioid antagonists such as naltrexone, not agonists, have been studied for this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00725765 | Meperidine Hydrochloride Injection USP | Not specified | Not specified |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links meperidine to contraindications in many conditions. Main groups include:
  - Respiratory: COPD, respiratory failure, sleep apnoea syndromes, congenital central hypoventilation syndrome
  - Liver and biliary: liver failure, liver disease, gallbladder disease, hyperbilirubinaemia, Gilbert syndrome
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
  - Endocrine: hypothyroidism, myxedema, Addison disease
  - Other: peptic ulcer disease, benign prostatic hyperplasia, hypotensive disorder, substance abuse/dependence, sickle cell anaemia, thrombophlebitis, angle-closure glaucoma
- **Drug Interactions**: 100 interactions are recorded, of which 20 were reviewed here.
  - **Major**: alvimopan, bupropion, morphine, lorcaserin, dolasetron, palonosetron
  - **Moderate**: hyoscyamine, loperamide, atropine, glycopyrronium, cimetidine, dicyclomine, dronabinol, eluxadoline, naloxone, phentermine, trospium, picosulfuric acid, sodium sulfate, polyethylene glycol (3350 with electrolytes)
- **Relevance to Tourette syndrome**: Patients commonly take SSRIs, alpha-2 agonists and antipsychotics. Meperidine also carries serotonin syndrome and MAOI interaction risks (from general pharmacology, not the supplied data).

Please refer to the package insert for the official warnings and contraindications, as these were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. There are no clinical trials or publications, and the mechanism is uncertain and possibly opposed in direction. Meperidine's safety profile (dependence, neurotoxic metabolite, serotonin syndrome, many interactions) is unfavourable for a chronic neuropsychiatric condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication and dosage form for the Canadian product
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence linking meperidine to tic disorders
- A comparison with established Tourette therapies, and an assessment of whether safer opioid-system or alternative candidates exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

