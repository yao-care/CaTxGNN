---
layout: default
title: Procainamide
parent: Model Prediction Only (L5)
nav_order: 772
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Procainamide"
predicted_indications: ["Tourette syndrome", "hyperthyroidism", "Prinzmetal angina", "methemoglobinemia, alpha type", "methemoglobinemia", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "methemoglobin reductase deficiency", "rheumatoid arthritis"]
description: "Procainamide: predicted new indication Tourette syndrome (evidence level L5). In Canada: 1 DIN (1 marketed)"
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

## Procainamide: Tourette syndrome
{: .text-alpha }

## One-Sentence Summary

Procainamide is an injectable antiarrhythmic (a class Ia sodium channel blocker) marketed in Canada as Procainamide Hydrochloride Injection USP.
The TxGNN model (deep learning) predicts it may be effective for **Tourette syndrome**, but this score may reflect similarities the model learned between related diseases, not biological evidence, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for procainamide: "Procainamide (PA) increases the effective refractory period of the atria, and to a lesser extent the bundle of His-Purkinje system and ventricles of the heart. It reduces impulse conduction velocity in the atria, His-Purkinje fibers, and ventricular muscle, but has variable effects on the atrioventricular (A-V) node, a direct slowing action and a weaker vagolytic effect which may speed A-V conduction slightly." ([DailyMed: procainamide hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ec3b767-66bb-4634-877e-71f70d501da0), label version 2026-08-31; accessed 2026-11-19.) Procainamide is generally known as a class Ia sodium channel blocker used for heart rhythm disorders. It has no known action on the dopaminergic or cortico-striatal circuitry implicated in Tourette syndrome.

No plausible mechanistic bridge between the original use (arrhythmia) and the predicted use (a neurodevelopmental tic disorder) is evident. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; no trials or literature support it. The prediction should be treated as a weak hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02184486 | PROCAINAMIDE HYDROCHLORIDE INJECTION USP | PROCAINAMIDE HYDROCHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

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
The Tourette syndrome prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials, no literature, and no plausible mechanism. The drug also carries significant cardiac, hematological and autoimmune safety concerns.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indication text (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to assess any link to tic-disorder biology
- Preclinical or mechanistic evidence supporting a role in Tourette syndrome
- A benefit-risk assessment addressing QT prolongation, blood dyscrasias, and drug-induced lupus

---

### Other Predicted Indications (Brief Note)

Other predictions in the data compiled for this report also have no clinical trials and no supporting evidence. All are rated Hold:

- **Hyperthyroidism** (0.9944): L5. The retrieved papers address atrial fibrillation rate control and drug-induced vasculitis, not treatment of hyperthyroidism.
- **Prinzmetal angina** (0.9944): L4. The papers cover arrhythmias complicating variant angina, and class Ia agents may provoke torsades de pointes.
- **Rheumatoid arthritis** (0.9912): L4. The literature shows procainamide *inducing* autoimmunity (drug-induced lupus), which is a safety signal rather than support.
- **Methemoglobinemia, alpha type** (0.9940), **methemoglobinemia** (0.9933), **methemoglobin reductase deficiency** (0.9920), **nephrogenic syndrome of inappropriate antidiuresis** (0.9927), **trichotillomania** (0.9926), and **resistance to thyroid hormone (THRB mutation)** (0.9922): L5, with no plausible mechanism or evidence.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: procainamide hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ec3b767-66bb-4634-877e-71f70d501da0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

