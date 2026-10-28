---
layout: default
title: Pyridostigmine
parent: Model Prediction Only (L5)
nav_order: 785
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
monitor_inn: "Pyridostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly"]
description: "Pyridostigmine: predicted new indication Autoimmune disease of peripheral nervous system (evidence level L5). Approved use: Not recorded in the local data"
---

# Pyridostigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Pyridostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## One-Sentence Summary

Pyridostigmine is an acetylcholinesterase inhibitor originally used to treat myasthenia gravis and related neuromuscular junction disease.
The TxGNN model predicts it may be effective for **autoimmune disease of peripheral nervous system**.
Currently there are **no registered clinical trials** and **3 publications** (one review, one case report and one cohort study) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune disease of peripheral nervous system |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pyridostigmine is a reversible acetylcholinesterase inhibitor. By slowing the breakdown of acetylcholine, it raises acetylcholine levels at the neuromuscular junction. This is the established symptomatic mechanism in myasthenia gravis.

Thymic hyperplasia is a common feature of myasthenia gravis with acetylcholine receptor (AChR) antibodies. The predicted indication is therefore a subtype of the approved indication, so this is not true repurposing. The supporting literature is observational: a case of MuSK-positive MG with thymic hyperplasia and a cohort on thymectomy outcomes. None tests pyridostigmine specifically in this subgroup.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | Two-year outcomes of thymectomy in 39 patients with non-thymomatous, AChR-antibody-positive late-onset MG |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Genomic, phenotypic and epigenetic insights into MG pathology and autoimmunity |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | MuSK-positive MG with thymus hyperplasia presenting with dropped head syndrome |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00869953 | MESTINON-SR | Not listed | Not listed |
| 00869961 | MESTINON | Not listed | Not listed |
| 02495643 | RIVA-PYRIDOSTIGMINE | Not listed | Not listed |
| 02508362 | JAMP PYRIDOSTIGMINE BROMIDE | Not listed | Not listed |

All four are valid single-ingredient products.

---

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text)**: kidney disease, pyoureter, asthma (including intrinsic and allergic asthma) and urinary tract obstruction.
- **Drug Interactions**: 78 interactions were identified. The 20 listed in the data compiled for this report are all rated Moderate. They include:
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Anticholinergics and antispasmodics: atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, propantheline, trospium, methscopolamine, clidinium, mepenzolate
  - Aminoglycosides: neomycin, kanamycin, paromomycin

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pyridostigmine is already marketed in Canada and is a standard symptomatic treatment for myasthenia gravis. The predicted indication is a subtype of that use, and the pyridostigmine-specific evidence for this subgroup is observational only. No trials are registered.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing
- Mechanism of action data from DrugBank
- Dosage form and approved indication details for the four Canadian licences
- Review of the knowledge-graph contraindications (asthma, urinary tract obstruction, kidney disease) in the target patient group
- Attention to MuSK-positive MG, where cholinesterase inhibitors may respond poorly or worsen symptoms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

