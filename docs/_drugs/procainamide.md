---
layout: default
title: Procainamide
parent: Model Prediction Only (L5)
nav_order: 772
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Procainamide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the Canadian license data (the drug is known as an anti…"
monitor_inn: "Procainamide"
predicted_indications: ["Tourette syndrome", "hyperthyroidism", "Prinzmetal angina", "methemoglobinemia, alpha type", "methemoglobinemia", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "methemoglobin reductase deficiency", "rheumatoid arthritis"]
---

# Procainamide
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

# Procainamide: From Arrhythmia Treatment to Tourette Syndrome

## One-Sentence Summary

Procainamide is an injectable antiarrhythmic (a class Ia sodium channel blocker) marketed in Canada as Procainamide Hydrochloride Injection USP.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (the drug is known as an antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Procainamide is generally known as a class Ia sodium channel blocker used for heart rhythm disorders. It has no known action on the dopaminergic or cortico-striatal circuitry implicated in Tourette syndrome.

No plausible mechanistic bridge between the original use (arrhythmia) and the predicted use (a neurodevelopmental tic disorder) is evident. The high TxGNN score reflects a pattern in the knowledge graph, not supporting trials or literature. The prediction should be treated as a weak hypothesis only.

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
| 02184486 | PROCAINAMIDE HYDROCHLORIDE INJECTION USP | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease links in the TxGNN knowledge graph, not from label text):
  - Cardiac: long QT syndrome (including familial), torsades de pointes, atrioventricular block, digitalis poisoning
  - Blood: agranulocytosis, neutropenia (including several congenital forms), thrombocytopenia
  - Immune: systemic lupus erythematosus (including pediatric)
  - Neuromuscular: myasthenia gravis, neuromuscular junction disease
  - Organ and metabolic: kidney disease, liver disease, gallbladder disease, potassium deficiency, hypotensive disorder
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Examples of **Major** interactions include clarithromycin, levofloxacin, dolasetron, palonosetron, eliglustat, picosulfuric acid, sodium sulfate, and polyethylene glycol with electrolytes. Several **Moderate** interactions were also noted, such as famotidine, ranitidine, cimetidine, metformin, loperamide, metoclopramide, and bisacodyl.
- **Procainamide's autoimmune signal**: Literature retrieved for other predicted indications consistently describes procainamide-induced lupus, antinuclear and anti-histone antibodies, and inhibition of T-cell DNA methylation.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests only on a graph score. There are no trials, no literature, and no plausible mechanism. The drug also carries significant cardiac, haematological and autoimmune safety concerns.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indication text (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to assess any link to tic-disorder biology
- Preclinical or mechanistic evidence supporting a role in Tourette syndrome
- A benefit-risk assessment addressing QT prolongation, blood dyscrasias, and drug-induced lupus

---

### Other Predicted Indications (Brief Note)

Other predictions in the data compiled for this report also have no clinical trials and no supporting evidence. All are rated Hold:

- **Hyperthyroidism** (99.44%): L5. The retrieved papers address atrial fibrillation rate control and drug-induced vasculitis, not treatment of hyperthyroidism.
- **Prinzmetal angina** (99.43%): L4. The papers cover arrhythmias complicating variant angina, and class Ia agents may provoke torsades de pointes.
- **Rheumatoid arthritis** (99.12%): L4. The literature shows procainamide *inducing* autoimmunity (drug-induced lupus), which is a safety signal rather than support.
- **Methemoglobinemia, alpha type** (99.40%), **methemoglobinemia** (99.33%), **methemoglobin reductase deficiency** (99.20%), **nephrogenic syndrome of inappropriate antidiuresis** (99.27%), **trichotillomania** (99.26%), and **resistance to thyroid hormone (THRB mutation)** (99.22%): L5, with no plausible mechanism or evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

