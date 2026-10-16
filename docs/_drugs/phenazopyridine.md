---
layout: default
title: Phenazopyridine
parent: Model Prediction Only (L5)
nav_order: 726
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Phenazopyridine: predicted new indication Bronchitis (evidence level L5). Approved use: Not specified in the Canadian license data (the drug is known as a ur…"
monitor_inn: "Phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Phenazopyridine: From Urinary Tract Symptom Relief to Bronchitis

## One-Sentence Summary

Phenazopyridine is a urinary tract analgesic marketed in Canada under the brand name PYRIDIUM. The TxGNN model predicts it may be effective for **bronchitis**, but the prediction is supported by **0 clinical trials** and **0 publications**. It is a knowledge-graph prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data (the drug is known as a urinary tract analgesic) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenazopyridine is generally understood to act locally on the urinary mucosa to relieve pain, burning and urgency, but its exact mechanism is not well characterized.

There is no established pharmacological link between this local urinary analgesic effect and bronchial inflammation or respiratory infection. The high TxGNN score (0.992) comes from patterns in the knowledge graph, not from clinical or mechanistic evidence. The data compiled for this report contain no trials or publications on respiratory use. The prediction should therefore be treated as a hypothesis only, and its plausibility is weak.

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
| 00476714 | PYRIDIUM | Not listed | Not listed |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are drug–disease links from PrimeKG, not package insert text; they should be confirmed against the label):
- Liver and biliary: liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease
- Kidney and urinary: kidney disease, pyoureter, benign prostatic hyperplasia
- Blood: anemia (including macrocytic anemia), thrombocytopenia, neutropenia, agranulocytosis, other haematologic disease
- Porphyria: inherited porphyria, porphyrin metabolism disease, porphyria
- Cardiovascular: hypertension, hypertensive disorder, coronary artery disease
- Respiratory and sleep: chronic obstructive pulmonary disease (including severe early-onset COPD), obstructive sleep apnea, sleep apnea syndrome, congenital central hypoventilation syndrome, Haddad syndrome
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence

Several of these, particularly COPD and other respiratory conditions, are relevant to the proposed bronchitis use.

**Drug Interactions:** 24 interactions are recorded, 20 of them listed in detail. Two are rated Major:
- Nitrous acid
- Leflunomide

Moderate interactions include:
- Topical, ophthalmic and nasal local anaesthetics (lidocaine, benzocaine, cocaine, tetracaine, oxybuprocaine, cinchocaine)
- Naltrexone
- Methotrexate
- Interferon beta-1a and beta-1b
- Oncology agents (asparaginase, pegaspargase, brentuximab vedotin, clofarabine, idelalisib)

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests solely on a knowledge-graph score. There are no clinical trials or publications, and no mechanistic basis for a respiratory effect.
- Many knowledge-graph contraindication signals, including respiratory disease, and the number of recorded interactions further argue against prioritization.

**To proceed, the following is needed:**
- Mechanism of action data and a testable mechanistic hypothesis linking the drug to bronchial inflammation or infection
- The Health Canada package insert (warnings, contraindications, approved indication and dosage form)
- Preclinical or observational evidence of any benefit in respiratory conditions
- A review of the knowledge-graph contraindications, particularly COPD and other respiratory disorders, against the label
- A confirmed route and formulation suitable for a respiratory indication, since none has been established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

