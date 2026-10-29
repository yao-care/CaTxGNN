---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 923
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Topiramate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (generalized tonic-clonic seizures, partial epilepsy…"
monitor_inn: "TOPIRAMATE"
predicted_indications: ["trigeminal nerve neoplasm"]
---

# Topiramate
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

## Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Topiramate is an antiseizure medication originally used for epilepsy, including generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm** (score 0.9970), but **no clinical trials and no publications** support it.
The model's other high-scoring predictions are mostly reflex-seizure subtypes of epilepsy, which are really extensions of the existing indication and not new uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 18) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

The approved-indication text was not available in the Canadian license data compiled for this report.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the pharmacology generally described in the literature, topiramate reduces neuronal excitability by blocking voltage-gated sodium channels, enhancing GABA-A activity, antagonizing AMPA/kainate glutamate receptors, and weakly inhibiting carbonic anhydrase.

**For the top prediction (trigeminal nerve neoplasm):** none of these mechanisms offers a plausible route to controlling a tumor. The high score (0.9970) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, topiramate might relieve symptoms such as trigeminal neuralgia, which is a different condition.


---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

For the top-ranked prediction (trigeminal nerve neoplasm), currently no related literature is available.

For context, the most relevant literature found for the second- and third-ranked predictions is summarized below. It concerns the parent epilepsy indication and is not specific to the predicted subtypes.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24570033](https://pubmed.ncbi.nlm.nih.gov/24570033/) | 2014 | Cochrane systematic review | Cochrane Database Syst Rev | Topiramate as add-on treatment for drug-resistant partial epilepsy |
| [31642054](https://pubmed.ncbi.nlm.nih.gov/31642054/) | 2019 | Cochrane systematic review | Cochrane Database Syst Rev | Topiramate add-on therapy for drug-resistant focal epilepsy |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic review / network meta-analysis | J Neurol | Comparison of antiseizure medications in idiopathic generalized epilepsies |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES practice guideline update on new antiepileptic drugs for new-onset epilepsy |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Review / consensus | Epilepsy Behav | Topiramate is among the FDA-approved antiseizure drugs for Lennox-Gastaut syndrome |
| [35421622](https://pubmed.ncbi.nlm.nih.gov/35421622/) | 2022 | Review | Seizure | Molecular mechanisms of topiramate and its clinical value in epilepsy |
| [30687937](https://pubmed.ncbi.nlm.nih.gov/30687937/) | 2019 | Cochrane review | Cochrane Database Syst Rev | Topiramate for juvenile myoclonic epilepsy |
| [12581224](https://pubmed.ncbi.nlm.nih.gov/12581224/) | 2003 | Preclinical (animal) | Epilepsia | Topiramate reduced seizures in genetic absence (GAERS) and audiogenic rat models |
| [10666508](https://pubmed.ncbi.nlm.nih.gov/10666508/) | 2000 | Preclinical (animal) | Eur J Pharmacol | Topiramate antagonized audiogenic seizures in DBA/2 mice and potentiated other anticonvulsants |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230894 | TOPAMAX 100MG | Not listed | Not listed |
| 02230896 | TOPAMAX 200MG | Not listed | Not listed |
| 02279614 | APO-TOPIRAMATE | Not listed | Not listed |
| 02248862 | TEVA-TOPIRAMATE | Not listed | Not listed |
| 02262991 | PMS-TOPIRAMATE | Not listed | Not listed |

There are 20 valid single-ingredient licences in total, and none are cancelled. Other brands include JAMP, GLN, AURO, PRO, MINT, MYLAN and NRA topiramate products.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease graph links, not from package insert text):
anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, diarrheal disease, ocular hypertension, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, acidosis disorder, metabolic acidosis, amnestic disorder and retrograde amnesia.

**Drug Interactions:** the interaction search returned 100 records. The main ones listed are:
- **Major:** metformin, and anticholinergic agents (hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, trospium)
- **Moderate:** pioglitazone, glyburide, morphine, dronabinol, nabilone, phentermine, metoclopramide, phenylbutyric acid, glycerol phenylbutyrate

Topiramate's known adverse effects reported in the retrieved literature include kidney stones, metabolic acidosis, cognitive impairment, psychiatric effects, and pregnancy-related risks. Please refer to the package insert for the full warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, trigeminal nerve neoplasm, has a very high model score but no trials, no literature, and no plausible mechanistic link. It should be treated as a TxGNN model (deep learning) artifact.
- The other predictions are rare reflex-seizure subtypes. They are either supported only indirectly by evidence from epilepsy generally, or have no evidence at all. Together with the knowledge-graph warnings about kidney, liver and metabolic conditions, this does not justify advancing any of them as a new indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (this is currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Indication-specific evidence for any seizure subtype of interest (for example, case series or trials in reflex epilepsies such as reading or audiogenic seizures)
- Confirmation that the trigeminal nerve neoplasm prediction is not an artifact, such as a manual review of the similarities the TxGNN model (deep learning) learned between related diseases
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

