---
layout: default
title: Mepyramine
parent: Moderate Evidence (L3-L4)
nav_order: 591
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-13
description: "Mepyramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis"
monitor_inn: "Mepyramine"
predicted_indications: ["allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "cold urticaria"]
---

# Mepyramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Mepyramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Mepyramine is a first-generation antihistamine, originally used for allergic conditions such as allergic rhinitis, conjunctivitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **no registered clinical trials**. The **4 publications** found are indirect (preclinical studies and one veterinary study), so the evidence is weak. Urticaria is also already a labeled use, so this is largely an on-label indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (the Canadian license records contain no indication text; the original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, mepyramine is a first-generation histamine H1 receptor antagonist. Histamine is the central mediator of allergic urticaria, so blocking H1 receptors gives a strong mechanistic rationale.

The knowledge graph already lists urticaria and angioedema among mepyramine's original indications. The prediction is therefore close to its existing uses and does not represent a distinct new therapeutic area.

The other predicted indications are less well supported:
- **Cold urticaria** (score 99.70%): a histamine-mediated physical urticaria, so H1 antagonism is plausible. Standard therapy typically uses second-generation antihistamines, and no mepyramine-specific evidence exists. Any benefit is presumed to be a class effect.
- **Nasal cavity disease** (score 99.74%): a broad category. H1 blockade is relevant to allergic and vasomotor rhinitis, but non-allergic subtypes lack a clear histamine-driven mechanism.
- **Acute laryngopharyngitis** (score 99.72%): a model prediction only. The condition is mostly infectious or irritant-driven, so any benefit is likely limited to symptom relief.

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

