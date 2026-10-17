---
layout: default
title: Tafamidis
parent: Model Prediction Only (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tafamidis: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Amyloidosis, including AH, AL and ATTRV122I amyloidosis"
monitor_inn: "Tafamidis"
predicted_indications: ["primary release disorder of platelets", "thrombocytopenic purpura", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "primary hyperoxaluria", "dermis disease", "biotin metabolic disease", "mixed-type autoimmune hemolytic anemia"]
---

# Tafamidis
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tafamidis: From Transthyretin Amyloidosis to Primary Amyloidosis

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabiliser originally used to treat amyloidosis, including transthyretin-type forms.
The TxGNN model's top-ranked prediction is **primary release disorder of platelets**, but the data compiled for this report show no supporting evidence for it. The best-supported prediction is **primary amyloidosis** (rank 5), with **0 clinical trials** and **20 publications**, most of which concern transthyretin amyloidosis, a disease the drug already treats.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyloidosis, including AH, AL and ATTRV122I amyloidosis (from the knowledge graph; no approved indication text in the Canadian licence record) |
| Predicted New Indication | Primary release disorder of platelets (rank 1, top TxGNN prediction); best-supported alternative: primary amyloidosis (rank 5) |
| TxGNN Prediction Score | 89.27% (rank 1); 85.00% (primary amyloidosis, rank 5) |
| Evidence Level | L5 (rank 1); L4 (primary amyloidosis) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (rank 1); Hold overall, with primary amyloidosis and acquired amyloid peripheral neuropathy as research questions |

---

## Why is This Prediction Reasonable?

**Mechanism.** Tafamidis binds the thyroxine-binding sites of the TTR tetramer and stabilises it. It acts on both wild-type and mutated TTR. By strengthening the weak dimer-dimer interface, it slows the tetramer dissociation that is the first step of amyloid formation. It is approved for TTR-mediated amyloidosis, and its use can reduce cardiovascular mortality and cardiovascular-related hospitalisations in patients with TTR cardiomyopathy.

**Top-ranked prediction (primary release disorder of platelets).** Nothing in the data compiled for this report links TTR stabilisation to platelet granule release defects. The score of 89.27% is a graph-based inference only, with no trials or literature. The same applies to the other high-scoring predictions: thrombocytopenic purpura, pseudo-von Willebrand disease, Glanzmann thrombasthenia, primary hyperoxaluria, dermis disease, biotin metabolic disease and mixed-type autoimmune hemolytic anaemia. None has a plausible mechanistic link or any supporting studies.

**Amyloid-related predictions.** Two predictions have a plausible mechanistic basis, but both need caution:

- **Primary amyloidosis (rank 5):** this label usually refers to AL amyloidosis, where the precursor is immunoglobulin light chain rather than TTR, so TTR stabilisation does not directly apply. The strong evidence retrieved (including the pivotal ATTR-ACT Phase 3 trial) concerns ATTR cardiomyopathy, which overlaps with the drug's existing indications and is not true repurposing. No direct evidence for AL amyloidosis was found.
- **Acquired amyloid peripheral neuropathy (rank 6):** tafamidis slows neuropathy progression in early hereditary ATTR polyneuropathy. The "acquired" label is ambiguous (wild-type ATTR or AL-related), and no primary efficacy data exist for the acquired form. The evidence is indirect and review-based.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for the amyloid-related predictions in the data compiled for this report.

---

## Literature Evidence

No literature is available for the top-ranked prediction (primary release disorder of platelets). The table below shows the most relevant publications for the best-supported prediction, primary amyloidosis (rank 5). Most concern ATTR rather than AL amyloidosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30145929](https://pubmed.ncbi.nlm.nih.gov/30145929/) | 2018 | RCT (Phase 3, ATTR-ACT) | N Engl J Med | Tafamidis in transthyretin amyloid cardiomyopathy; binds TTR and prevents tetramer dissociation and amyloidogenesis |
| [41282536](https://pubmed.ncbi.nlm.nih.gov/41282536/) | 2025 | Network meta-analysis | Eur Heart J Open | Compares tafamidis, acoramidis, patisiran and vutrisiran in transthyretin cardiac amyloidosis |
| [40889572](https://pubmed.ncbi.nlm.nih.gov/40889572/) | 2025 | Systematic review and meta-analysis | J Card Fail | Harmonises Phase 3 placebo-controlled trials of amyloid-specific drugs in ATTR-CM |
| [41334760](https://pubmed.ncbi.nlm.nih.gov/41334760/) | 2025 | Cohort study | J Am Heart Assoc | Tafamidis reduces death and acute heart failure hospitalisation in octogenarians with transthyretin cardiac amyloidosis |
| [41317156](https://pubmed.ncbi.nlm.nih.gov/41317156/) | 2025 | Real-world cohort | Eur J Heart Fail | Clinical phenotype and survival of wild-type ATTR-CM patients treated with tafamidis |
| [38441582](https://pubmed.ncbi.nlm.nih.gov/38441582/) | 2024 | Review | JAMA | Review of transthyretin cardiac amyloidosis |
| [39819772](https://pubmed.ncbi.nlm.nih.gov/39819772/) | 2025 | Review | Curr Opin Cardiol | New therapies for ATTR-CM and AL cardiac amyloidosis |
| [35414852](https://pubmed.ncbi.nlm.nih.gov/35414852/) | 2022 | Review | Methodist DeBakey Cardiovasc J | Current and experimental treatments for cardiac amyloidosis |
| [32796279](https://pubmed.ncbi.nlm.nih.gov/32796279/) | 2020 | Review | Curr Opin Neurol | Current treatment of hereditary ATTR amyloidosis |
| [39213194](https://pubmed.ncbi.nlm.nih.gov/39213194/) | 2025 | RCT (different drug) | N Engl J Med | Vutrisiran in ATTR-CM (not tafamidis) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02517841 | VYNDAMAX | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions** (13 records; one is the target-binding entry for TTR rather than an interacting drug):

- **Major:** Ozanimod
- **Moderate:** Rosuvastatin, Deferasirox, Eltrombopag, Lusutrombopag, Artesunate, Axitinib, Methotrexate, Irinotecan (including liposomal), Belinostat, Imatinib

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (primary release disorder of platelets) has no mechanistic link, trials or literature, so it rests on a graph-based score alone (Evidence Level L5).
- The amyloid-related predictions (primary amyloidosis, acquired amyloid peripheral neuropathy) are plausible research questions at L4. Their strong evidence mostly overlaps with already-approved ATTR indications rather than representing new repurposing.

**To proceed, the following is needed:**
- Clarify what "primary amyloidosis" and "acquired amyloid neuropathy" mean in the model, and whether AL amyloidosis is the intended target
- Direct evidence of tafamidis in AL amyloidosis or acquired ATTR neuropathy, if these are pursued
- Detailed mechanism of action data
- Health Canada package insert warnings, contraindications and approved indication text, which are needed for safety screening
- Dosage form and manufacturer details for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

