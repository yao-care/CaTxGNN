---
layout: default
title: Carbamazepine
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
monitor_inn: "CARBAMAZEPINE"
predicted_indications: ["trigeminal nerve neoplasm", "beta-ketothiolase deficiency", "Rett syndrome, congenital variant"]
last_modified_at: 2026-10-28
description: "Carbamazepine: predicted new indication trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Carbamazepine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Carbamazepine: Voltage-gated sodium channel blocker → trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Carbamazepine is a sodium channel–blocking anticonvulsant used for seizure and nerve-pain conditions.
The TxGNN model predicts it may be relevant to **trigeminal nerve neoplasm**, but **no clinical trials** and only **indirect publications** (mostly case reports of tumour-associated trigeminal neuralgia) are available, so the evidence is model-driven and weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | trigeminal nerve neoplasm |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 11 of 11) |
| Number of DINs | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Carbamazepine is generally understood to block voltage-gated sodium channels, which reduces abnormal, repetitive neuronal firing. This is the basis for its well-established use in trigeminal neuralgia pain.

The retrieved literature describes patients whose trigeminal neuralgia was caused by a tumour or mass near the trigeminal nerve (venous angioma, lipoma, dermoid cyst, meningioma, schwannoma, lymphoma, melanoma, pituitary adenoma). In these reports carbamazepine was typically used for pain, and in several cases it eventually failed or lost effect as the underlying lesion progressed. This supports symptom control only, not any effect on the tumour itself. The high prediction score most likely reflects the closeness of this disease node to trigeminal neuralgia rather than antineoplastic activity. No evidence suggests the drug treats the neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications directly studies carbamazepine as a treatment for trigeminal nerve neoplasm. Reviews and case reports are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Treatment options for trigeminal neuralgia, which may be caused by vascular compression or a tumour process |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Overview of medical and surgical treatments for trigeminal neuralgia |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case report | British Journal of Neurosurgery | Primary lymphoma of the trigeminal nerve; carbamazepine did not improve symptoms |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case report | Rinsho Shinkeigaku | Lymphoma spreading along the trigeminal nerve; pain initially improved with carbamazepine, then became ineffective |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case report | Arquivos de Neuro-Psiquiatria | Primary melanoma of Meckel's cave; pain not relieved by carbamazepine |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case report | No Shinkei Geka | Cerebellopontine angle lipoma; pain poorly controlled with carbamazepine because of side effects |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case report | World Neurosurgery | Trigeminal neuralgia caused by venous angioma |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case report | World Neurosurgery | Petroclival meningioma causing trigeminal neuralgia, treated surgically |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclinical | Experimental Neurology | Carbamazepine inhibited spontaneous activity in experimental rat neuromas |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey | Br J Oral Maxillofac Surg | Survey of how specialists investigate and medically manage trigeminal neuralgia |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02261847 | SANDOZ-CARBAMAZEPINE CR |
| 00773611 | TEGRETOL CR |
| 02194333 | TEGRETOL SUSPENSION |
| 00755583 | TEGRETOL CR |
| 02244403 | TARO-CARBAMAZEPINE CHEWABLE TABLETS |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug interactions:** 100 interactions were found in the interaction database. Examples:
- **Major:** clarithromycin, eliglustat
- **Moderate:** doxycycline, hydrocortisone, dexamethasone, bupropion, aprepitant, morphine, metronidazole, cimetidine, pioglitazone, canagliflozin, activated charcoal

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no study evaluates carbamazepine against trigeminal nerve neoplasm itself. The literature only shows carbamazepine used for pain in tumour-related neuralgia, which is symptom control and not tumour treatment. Evidence is at the model-prediction level only.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence of antitumour activity in trigeminal nerve tumours
- Mechanism of action data and a clear rationale for tumour-specific effect
- Package insert safety information (warnings, contraindications) from Health Canada
- Evaluation of whether the benefit is limited to symptomatic pain relief, which would not constitute a new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

