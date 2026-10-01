---
layout: default
title: Trimebutine
parent: Model Prediction Only (L5)
nav_order: 941
evidence_level: L5
indication_count: 2
---

# Trimebutine
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

# Trimebutine: From a Gastrointestinal Motility Agent to Migraine Disorder

## One-Sentence Summary

Trimebutine is a gut-acting agent with opioid-receptor activity, marketed in Canada under four DINs. The supplied record does not state its approved indication.
The TxGNN model predicts it may help in **Migraine Disorder**, but there are **0 registered clinical trials** and only **4 publications**, one of them a randomized crossover trial of trimebutine added to rizatriptan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record (the Canadian licence entries carry no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L2 (a single randomized, placebo-controlled crossover trial; no registered trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. The reasoning below comes from general pharmacology and the cited literature, not from the supplied data.

The most plausible link is pharmacokinetic rather than disease-modifying. During migraine attacks the stomach often empties slowly (gastric stasis), which delays absorption of oral triptans. Triptans also tend to work better when taken early in an attack. A motility-modulating agent such as trimebutine may therefore make triptan absorption faster or more consistent. Trimebutine is also known as a peripheral opioid-receptor agonist (mu, delta and kappa) with visceral-analgesic and ion-channel effects. These could add to symptom relief, but this is speculative.

The TxGNN score of 99.64% is a model prediction and does not replace clinical evidence.

A second predicted indication, **migraine with brainstem aura** (score 99.54%), has no supporting evidence at all (L5, Hold). Its high score probably just reflects proximity to the parent migraine node in the knowledge graph. Triptans are traditionally used with caution in brainstem aura, and the absorption rationale does not carry over cleanly. Evidence from general migraine should not be extrapolated to this subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16776704](https://pubmed.ncbi.nlm.nih.gov/16776704/) | 2006 | RCT | Cephalalgia | Double-blind, randomized, placebo-controlled crossover study of rizatriptan alone vs. rizatriptan plus trimebutine for acute migraine. The idea is that a gastrokinetic add-on improves triptan efficacy and response consistency. The supplied abstract excerpt does not include the results. |
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review | J Gastroenterol Hepatol | Reviews prokinetic agents and reports effectiveness in diseases outside the GI tract, including central nervous system conditions. |
| [17046449](https://pubmed.ncbi.nlm.nih.gov/17046449/) | 2006 | Review | Lancet | Commentary on ways to increase the effect of triptans in migraine (no abstract available). |
| [16245431](https://pubmed.ncbi.nlm.nih.gov/16245431/) | 2005 | Case report | Pol Merkur Lekarski | A 9-year-old girl with abdominal migraine did not improve on drotaverine, mebeverine or trimebutine. This is a negative signal for trimebutine as a stand-alone treatment. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02245664 | APO-TRIMEBUTINE |
| 02245663 | APO-TRIMEBUTINE |
| 02538202 | MINT-TRIMEBUTINE |
| 02538210 | MINT-TRIMEBUTINE |

Dosage form, manufacturer and approved-indication text are not available for these entries.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is one small randomized crossover trial of trimebutine as an add-on to rizatriptan. There are no registered trials, and the supplied excerpt does not show the trial's results. The mechanism is plausible but unconfirmed, and the one case report is negative. Because Canadian safety information is also missing, this is best treated as a research question for now.

**To proceed, the following is needed:**
- The full text and results of the rizatriptan + trimebutine RCT (PMID 16776704), including effect size and any replication
- The Health Canada package insert warnings and contraindications for the marketed products (APO-TRIMEBUTINE, MINT-TRIMEBUTINE)
- The Canadian approved indication, dosage forms and routes, to check compatibility with an add-on migraine use
- Mechanism of action data from DrugBank to support the mechanistic-link analysis
- A registered Phase 2/3 trial of trimebutine as a triptan adjunct before any move toward a Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

