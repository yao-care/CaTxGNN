---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 574
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
description: "Mebendazole: predicted new indication Acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mebendazole
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

## Mebendazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic originally used for intestinal worm infections (enterobiasis, ascaridiasis and trichuriasis).
The TxGNN model's top-scoring prediction is acne (0.9920), but it has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mebendazole is a benzimidazole anthelmintic that inhibits tubulin polymerization in helminths. This impairs microtubule-dependent glucose uptake in the parasite.

Cestode larvae are susceptible to the same tubulin-targeting mechanism that acts against intestinal worms. Mebendazole and albendazole are the benzimidazoles used as parasitostatic chemotherapy for this disease. The WHO treatment guidelines and several reviews describe this use.

This is therefore better described as an established alternative than as a novel repurposing. Albendazole is generally the preferred agent. Treatment with benzimidazoles is mainly parasitostatic, meaning the parasite can resume growth if treatment stops. Surgery remains the cornerstone of management where feasible.

**Other predictions** (all L5 prediction only, Hold, except echinococcus granulosus):
- **Echinococcus granulosus infection (cystic hydatid disease, 95.6%)** is biologically plausible, using the same mechanism. It has L4 evidence and is a research question. The only supporting clinical report, a 1989 study of 70 patients treated with mebendazole (PMID 2585032), has an unconfirmed design.
- The only paper retrieved for acne is an unrelated case report of sparganosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Study types are inferred from titles and abstracts and should be verified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Open-label observational study and review | J Antimicrob Chemother | 35 patients on mebendazole or albendazole followed for an average of 39 months; compares outcomes of different regimens |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Case report | J Hepatol | A patient with non-resectable hepatic disease treated for 13 years with mebendazole; suggests long-term therapy may be parasitocidal |
| [8789923](https://pubmed.ncbi.nlm.nih.gov/8789923/) | 1996 | Guideline | Bull World Health Organ | WHO guidelines for cystic and alveolar echinococcosis; benzimidazole chemotherapy (albendazole or mebendazole) |
| [15532108](https://pubmed.ncbi.nlm.nih.gov/15532108/) | 2004 | Long-term analysis of a chemotherapy trial | J Hepatol | Immunosurveillance in the Swiss chemotherapy trial (1976-2001); long-term benzimidazole therapy is beneficial in non-resectable disease |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Benzimidazoles are the only recommended compounds, but are parasitostatic and can cause liver dysfunction |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current status of drug therapy for alveolar echinococcosis |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Trop | Albendazole and mebendazole remain the licensed drugs; no non-surgical replacement is available |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Albendazole and mebendazole, and the search for novel options |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Pharmacology study | Eur J Clin Pharmacol | Plasma mebendazole concentrations in infected animals and in humans; high oral doses were only partly effective |
| [1724571](https://pubmed.ncbi.nlm.nih.gov/1724571/) | 1991 | Animal study | Trop Med Parasitol | Mebendazole alone and combined with isoprinosine in infected gerbils; mebendazole reduced parasite glucose levels |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00556734 | VERMOX | Not available | Not available |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease and gallbladder disease.
- **Drug Interactions** (10 found; 1 minor, 9 moderate):
  - Moderate: metronidazole, iodide I-131, iodide I-123, ritonavir
  - Moderate, antiepileptics (possible reduced mebendazole exposure through enzyme induction): phenobarbital, carbamazepine, fosphenytoin, phenytoin, primidone
  - Minor: cimetidine
- The literature notes that benzimidazoles can cause liver dysfunction. This is relevant because long-term, high-dose therapy would be needed.

The Health Canada package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**. Cystic echinococcosis (*E. granulosus*) is a research question.

**Rationale:**
- The model's top predictions have high scores but no clinical or mechanistic support.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications and dosage form), which is currently a blocking gap for safety screening
- Mechanistic (MOA) data from DrugBank
- Verification of study designs and outcomes for the key publications, which were classified from titles and abstracts
- A comparison with albendazole as the preferred agent, plus a plan for liver function monitoring and for managing the interactions with antiepileptics and other drugs
- Confirmation of whether the Canadian label covers echinococcosis, since the current licence data list no indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

