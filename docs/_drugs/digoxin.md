---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Digoxin: From Atrial Fibrillation to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used to treat atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **1 publication** (an unrelated review) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the Health Canada licence records compiled for this report contain no approved indication text; this indication comes from the TxGNN knowledge graph) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, digoxin inhibits the Na+/K+-ATPase pump, which raises intracellular calcium and increases cardiac contractility. It also has vagotonic effects that slow conduction through the atrioventricular node, which is why it is used for rate control in atrial fibrillation.

The link to Prinzmetal angina is weak. Prinzmetal angina is caused by coronary vasospasm and is treated mainly with calcium channel blockers and nitrates. Digoxin has no recognized antispasmodic action, and the rise in intracellular calcium could in theory worsen vasospasm. The high TxGNN score (0.998) should therefore be read as a statistical association from the knowledge graph, not as evidence of mechanistic plausibility.

Other predicted indications are also unsupported. Duodenal obstruction, duodenal ulcer, duodenogastric reflux and hypoalphalipoproteinemia have no plausible mechanistic basis. One further prediction, "obsolete susceptibility to ischemic stroke", is an outdated ontology term rather than an actionable indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology review of antihypertensive treatment; it does not address digoxin in vasospastic angina, so it provides no direct support |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02498510 | JAMP DIGOXIN | Not listed | Not listed |
| 02335719 | PMS-DIGOXIN | Not listed | Not listed |
| 02498502 | JAMP DIGOXIN | Not listed | Not listed |
| 02335700 | PMS-DIGOXIN | Not listed | Not listed |
| 02554402 | AURO-DIGOXIN | Not listed | Not listed |

Eight valid single-ingredient licences are held in total; the five above are shown. Another product is a digoxin injection (DIN 02048264).

---

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text)**: Associated conditions include:
  - Cardiac conduction and rhythm: Wolff-Parkinson-White syndrome, sick sinus syndrome (including the familial form), atrioventricular block, ventricular fibrillation.
  - Structural and inflammatory heart disease: hypertrophic cardiomyopathy (including the familial form), restrictive cardiomyopathy, constrictive pericarditis, myocarditis, cor pulmonale, myocardial infarction, coronary thrombosis.
  - Electrolyte and metabolic disorders: potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease.
  - Other: kidney disease, pyoureter, hemoglobinopathy, myxedema, hypothyroidism (including congenital).
- **Drug Interactions**: 100 interactions were identified in total (DDInter). Examples among those listed:
  - Moderate: acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcium phosphate, metformin, amphotericin B (including the lipid complex), bupropion, acetylsalicylic acid.
  - Minor: albiglutide, hyoscyamine, atropine, glycopyrronium.
- Digoxin has a narrow therapeutic index. Please refer to the package insert for label warnings and contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, the single publication is unrelated, and there is no plausible mechanism for Prinzmetal angina. Digoxin's calcium-raising effect could in theory aggravate vasospasm, and the knowledge graph lists several cardiac conditions as contraindications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing and blocking safety screening)
- Mechanism of action data, e.g. from DrugBank
- Targeted literature search for digoxin in vasospastic angina, including any preclinical evidence
- Safety assessment of the theoretical vasospasm risk before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

