---
layout: default
title: Dimenhydrinate
parent: Model Prediction Only (L5)
nav_order: 286
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Dimenhydrinate: predicted new indication Allergic urticaria (evidence level L4). Approved use: Motion sickness"
monitor_inn: "DIMENHYDRINATE"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
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

## Dimenhydrinate: From Motion Sickness and Vertigo to Allergic Urticaria
{: .text-alpha }

## One-Sentence Summary

Dimenhydrinate is an antiemetic and anti-vertigo drug, originally used for motion sickness and vertigo of central nervous system origin.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and only **1 publication** (a pharmacokinetic study in dogs) supporting this direction, so the evidence is indirect and the prediction rests mainly on computation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness; central nervous system origin vertigo |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 20 of 20) |
| Number of DINs | 20 (valid: 20) |
| Recommended Decision | Hold |

The Canadian licence records compiled for this report contain no approved-indication text, so the original indications shown above could not be taken from those records. Any TxGNN model (deep learning) scores on this page come from the model itself and may reflect similarities the model learned between related diseases, not biological evidence.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Diphenhydramine is a first-generation H1-antihistamine, and the antihistamine component is responsible for much of the drug's known pharmacology.

Urticaria is driven by mast cell degranulation and histamine release, and H1-antihistamines are standard therapy for it. This shared H1-antagonist pharmacology explains the very high TxGNN score (0.9974). The link between the original indications (motion sickness, vertigo) and urticaria is therefore the same active moiety acting on the H1 receptor, not a shared disease process.

There are practical limits. First-generation antihistamines cause sedation and anticholinergic effects. Guidelines generally prefer second-generation, non-sedating H1-antihistamines for chronic urticaria, which reduces the clinical value of repurposing dimenhydrinate.

A second prediction, **cold urticaria** (score 0.9924), rests on the same class-level logic. No trials or literature were found for it, so its evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic pilot study (healthy dogs) | Veterinary Dermatology | Compared diphenhydramine exposure after oral and IV diphenhydramine and after oral dimenhydrinate, and its effect on histamine-induced wheal formation. It provides bridging data between the two compounds but no efficacy data in human urticaria. |

## Canada Market Information

Dosage form and approved-indication text are not available in the data compiled for this report. The first 5 of the 20 valid single-ingredient licences are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00783595 | KIDS GRAVOL SUPPOSITORIES | Not available | Not available |
| 00392553 | CONFAB DIMENHYDRINATE 50 MG | Not available | Not available |
| 00605786 | TRAVEL TABS 50 MG | Not available | Not available |
| 02490528 | GAVISCON NAUSEA | Not available | Not available |
| 00013803 | GRAVOL TABLETS | Not available | Not available |

The remaining licences include injection, liquid gel, chewable, liquid, suppository and long-acting caplet products (for example Gravol, Kids Gravol, Jamp-Dimenhydrinate and Dimenhydrinate Injection USP). None has been cancelled.

## Safety Considerations

**Knowledge-graph contraindications.** These come from drug-disease contraindication edges in the knowledge graph, not from label text, and should be confirmed against the package insert. Listed conditions include:
- Cardiovascular: hypertension, hypotension, acute coronary syndrome, coronary artery disease, myocardial infarction
- Ocular and urinary: angle-closure glaucoma, ocular hypertension, benign prostatic hyperplasia, bladder neck obstruction
- Gastrointestinal and hepatic: peptic ulcer disease, pyloric stenosis, liver disease, gallbladder disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperthyroidism (including Graves disease and thyrotoxicosis), gout, hypophosphatemia
- Haematological: thrombocytopenia, blood coagulation disease, hemoglobinopathy
- Other: substance abuse/dependence

**Drug interactions.** The interaction query found 67 interacting drugs. Examples from the first 20 returned:
- **Major:** potassium citrate, potassium chloride
- **Moderate:** anticholinergics (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium and others), opioids (morphine, opium), loperamide, metoclopramide, nabilone, eluxadoline, prucalopride

Warnings and contraindications from the Canadian package insert were not available, so please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link through diphenhydramine is plausible, but no clinical trials exist, and the only publication is an animal pharmacokinetic study. Second-generation antihistamines are already preferred for urticaria and are better tolerated, so there is little reason to prioritize dimenhydrinate without direct data.

**To proceed, the following is needed:**
- Human efficacy data for dimenhydrinate or diphenhydramine in allergic urticaria, ideally from controlled trials
- A comparison against second-generation antihistamines, including sedation and anticholinergic burden
- Health Canada package insert warnings and contraindications, which are currently blocking safety screening
- Detailed mechanism of action data (MOA)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

