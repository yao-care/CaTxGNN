---
layout: default
title: Mepyramine
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Mepyramine"
predicted_indications: ["nasal cavity disease"]
description: "Mepyramine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Mepyramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Mepyramine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Mepyramine is a first-generation antihistamine, originally used for allergic conditions such as allergic rhinitis, conjunctivitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **no registered clinical trials**. The **4 publications** found are indirect (preclinical studies and one veterinary study), so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, mepyramine is a first-generation histamine H1 receptor antagonist. Histamine is the central mediator of allergic urticaria, so blocking H1 receptors gives a strong mechanistic rationale.


The other predicted indications are less well supported:
- **Nasal cavity disease** (score 0.9974): a broad category. H1 blockade is relevant to allergic and vasomotor rhinitis, but non-allergic subtypes lack a clear histamine-driven mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21033572](https://pubmed.ncbi.nlm.nih.gov/21033572/) | 2010 | Veterinary clinical study | Polish Journal of Veterinary Sciences | In 27 dogs with angioedema (15 treated, 12 placebo controls), mepyramine maleate showed potential benefit |
| [34758144](https://pubmed.ncbi.nlm.nih.gov/34758144/) | 2021 | Preclinical (mechanistic) | FASEB Journal | Mepyramine directly blocks nociceptor voltage-gated sodium channels, suggesting a topical pain-relief effect |
| [18222495](https://pubmed.ncbi.nlm.nih.gov/18222495/) | 2008 | Preclinical (rat neurons) | Neuropharmacology | Mepyramine inhibits the KCNQ/M potassium channel and depolarizes neurons, which may explain the neurotoxicity seen in overdose |
| [29371669](https://pubmed.ncbi.nlm.nih.gov/29371669/) | 2018 | Preclinical (tool compound) | Scientific Reports | Fluorescent H1-receptor probes were developed to study ligand-binding kinetics in living cells |

None of these studies tested mepyramine as a treatment for allergic urticaria in humans.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02275201 | MIDOL COMPLETE | Not specified | Not specified |
| 02275228 | MIDOL PMS | Not specified | Not specified |

Both licenses are valid single-ingredient authorizations.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from graph relationships, not from package insert text):
- Cardiovascular: hypertension and hypotensive disorders, coronary artery disease, myocardial infarction, coronary thrombosis
- Liver, pancreas and gallbladder: liver failure, liver disease, pancreatitis, gallbladder disease
- Kidney and urinary: kidney disease, pyoureter, benign prostatic hyperplasia
- Respiratory: chronic obstructive pulmonary disease (including severe early onset)
- Neurological and substance use: epilepsy, substance abuse/dependence
- Endocrine and metabolic: hypothyroidism, myxedema, congenital hypothyroidism, diabetes mellitus, diabetic ketoacidosis
- Gastrointestinal: peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- Other: rhabdomyolysis, nodular fasciitis, hemoglobinopathy

**Drug interactions:** The interaction query returned 100 records. The main ones are:
- **Major:** potassium citrate and potassium chloride
- **Moderate:**
  - Anticholinergics: atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, clidinium, mepenzolate, methscopolamine, propantheline, trospium
  - Opioids and antidiarrheals: morphine, opium, loperamide, eluxadoline
  - Others: metoclopramide, dronabinol

**Preclinical neurotoxicity signal:** Overdose of first-generation antihistamines has been linked to seizures and convulsions, and mepyramine inhibits the neuronal KCNQ/M channel.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale is strong, but the evidence is weak. There are no registered clinical trials, and the literature is indirect: preclinical studies and a veterinary study.
- Urticaria is already a labeled indication, so this is not truly a new use.
- Package insert warnings and contraindications are not yet available, and this gap blocks progression to safety screening.

**To proceed, the following is needed:**
- The Health Canada package insert for warnings and contraindications
- Mechanism of action data, for example from DrugBank
- Dosage form, manufacturer and indication details for the two Canadian products, which are combination-type brands (MIDOL)
- Human clinical evidence for mepyramine in urticaria, or a clear decision that on-label use needs no repurposing study
- A review of whether the knowledge-graph contraindications apply to the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

