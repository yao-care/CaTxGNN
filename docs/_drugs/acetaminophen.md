---
layout: default
title: Acetaminophen
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Acetaminophen: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder, headache disorder, common cold, nasopharyngitis…"
monitor_inn: "ACETAMINOPHEN"
predicted_indications: ["migraine with brainstem aura"]
---

# Acetaminophen
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

# Acetaminophen: From Migraine and Headache Disorders to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen is a widely used analgesic and antipyretic, originally used for migraine, headache disorders, the common cold and allergic or vasomotor rhinitis.
The TxGNN model predicts it may be useful for **migraine with brainstem aura**, a subtype of migraine with aura.
Currently there are **0 registered clinical trials** and **20 publications** (mostly general migraine reviews), so the evidence is at the model-prediction level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder, headache disorder, common cold, nasopharyngitis, allergic rhinitis, vasomotor rhinitis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (no registered trials; only general migraine literature and a plausible mechanism) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on general pharmacology, acetaminophen acts as an analgesic and antipyretic. It is thought to involve central COX inhibition and modulation of descending serotonergic pain pathways. This may be relevant to the headache phase of a migraine attack.

Migraine with brainstem aura is a clinical subtype of migraine, and acetaminophen is already used for migraine and headache disorders. The high TxGNN score likely reflects this close disease proximity rather than a subtype-specific finding.

Nothing in the data compiled for this report addresses brainstem aura directly. It is unknown whether acetaminophen affects aura physiology (such as cortical spreading depression), or whether the aura subtype changes treatment response. The prediction should therefore be treated as a research question, not as a confirmed new indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications retrieved concern migraine in general. None studies migraine with brainstem aura specifically. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies in adults |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus: a persistent migraine attack lasting more than 72 hours, with its burden and case series |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Randomized trials (pooled retrospective analysis) | Clinical Therapeutics | Acetaminophen, aspirin and caffeine combination for menstruation-associated migraine, from three placebo-controlled studies |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative study | Headache | Isometheptene, dichloralphenazone and acetaminophen combination compared with sumatriptan in mild-to-moderate migraine |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurologic Clinics | Headache in pregnancy and the puerperium; acetaminophen noted as first-line symptomatic treatment |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and prophylactic migraine therapies in pregnancy |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine treatment approach in pregnancy and breastfeeding |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Review | Pediatric Annals | Management of pediatric migraine |
| [23203776](https://pubmed.ncbi.nlm.nih.gov/23203776/) | 2013 | Review | Current Treatment Options in Neurology | Diagnosis and treatment of familial and sporadic hemiplegic migraine, a rare subtype of migraine with aura |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Ubrogepant for acute migraine; notes acetaminophen among options for mild to moderate migraine |

---

## Canada Market Information

Acetaminophen has 20 valid single-ingredient licences in Canada. Dosage form and approved indication text are not available for these products. The five listed below are examples.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230435 | ACET 160 | Not available | Not available |
| 02255251 | ACETAMINOPHEN 500 MG TABLETS EXTRA STRENGTH EASY TO SWALLOW | Not available | Not available |
| 02238885 | TYLENOL ARTHRITIS PAIN 8H | Not available | Not available |
| 02389908 | INFANTS' TYLENOL FEVER & SORE THROAT PAIN | Not available | Not available |
| 00544981 | APO-ACETAMINOPHEN | Not available | Not available |

---

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: liver failure, liver disease, cirrhosis of the liver, hepatic encephalopathy, hepatic coma and gallbladder disease.
- **Drug Interactions**: 100 interactions were found in total. The 20 shown in the data are mostly Minor.
  - **Moderate**: activated charcoal, glycerol phenylbutyrate, naltrexone.
  - **Minor**: mainly anticholinergic or antispasmodic agents (such as atropine, hyoscyamine, scopolamine, dicyclomine and glycopyrronium), H2 blockers (cimetidine, ranitidine), metoclopramide and liraglutide.
  - **Unknown level**: vitamin A and calcitriol.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score mainly reflects the close relationship between migraine with brainstem aura and migraine, for which acetaminophen is already used. There are no registered trials and no literature specific to brainstem aura, and the mechanism data are incomplete. Acetaminophen is a well-established, widely marketed drug, so this is a research question, not a safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before safety screening can proceed
- Detailed mechanism of action data, including any effect on aura-related mechanisms such as cortical spreading depression
- Evidence specific to brainstem aura, such as subtype analyses of existing migraine trials or a new pilot study
- A hepatic safety plan, given the liver-related cautions in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

