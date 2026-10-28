---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 520
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Lamotrigine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including partial epilepsy and Lennox-Gastaut syndrome)"
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Lamotrigine
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

## Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm (with Trigeminal Neuralgia as the Best-Supported Prediction)
{: .text-alpha }

## One-Sentence Summary

Lamotrigine is an antiseizure medicine, originally used for epilepsy, including partial epilepsy and Lennox-Gastaut syndrome.
The top-ranked TxGNN prediction is **trigeminal nerve neoplasm**, but it has **no clinical trials** and only 2 publications, which concern trigeminal neuralgia rather than tumours, so it is most likely a naming artefact.
The second-ranked prediction, **trigeminal neuralgia**, is much better supported, with **2 completed clinical trials** and **18 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including partial epilepsy and Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1); trigeminal neuralgia (rank 2, best supported) |
| TxGNN Prediction Score | 0.9997 (trigeminal nerve neoplasm); 0.9989 (trigeminal neuralgia) |
| Evidence Level | L5 (trigeminal nerve neoplasm); L2 (trigeminal neuralgia) |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold (trigeminal nerve neoplasm); Proceed with Guardrails (trigeminal neuralgia) |

The Canadian licence records compiled for this report contain no approved-indication text.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Lamotrigine is known to block voltage-gated sodium channels and reduce glutamate release. This dampens abnormal, high-frequency neuronal firing, which is the basis of its antiseizure effect.

**Trigeminal nerve neoplasm.** The high score most likely reflects semantic closeness between trigeminal nerve disease terms and trigeminal neuralgia, not an antitumour effect. The retrieved papers describe trigeminal neuralgia, including one case caused by a cavernous malformation treated with radiosurgery. Lamotrigine may relieve neuralgic pain, but no antitumour activity has been shown.

**Trigeminal neuralgia.** The mechanistic link is much stronger. Trigeminal neuralgia involves ectopic, high-frequency firing of trigeminal afferents after focal demyelination, usually from vascular compression. Lamotrigine acts on the same pathway as carbamazepine, the first-line therapy. Guidelines, including the European Academy of Neurology guideline, position lamotrigine as an add-on or second-line option.

**Other predictions in the list.** Most of the remaining predictions are reflex seizure types, which extend the existing epilepsy use. They are summarised in the table below.

| Predicted Indication | Score | Evidence Level | Evidence Summary | Suggested Decision |
|------|------|------|------|------|

---

## Clinical Trial Evidence

**Trigeminal nerve neoplasm:** Currently no related clinical trials registered.

**Trigeminal neuralgia (best-supported prediction):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head comparison of lamotrigine and carbamazepine for efficacy and safety in trigeminal neuralgia (2007–2008). Highly relevant design, but small. |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Not specified | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine in trigeminal neuralgia, looking at attack reduction and side effects (2003–2006). Small. |

Both trials are underpowered, and there is no confirmatory Phase 3 evidence.

---

## Literature Evidence

**Trigeminal nerve neoplasm:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; not about neoplasm treatment |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a cavernous malformation |

**Trigeminal neuralgia (up to 10 most relevant):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology recommendations for managing trigeminal neuralgia |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic review | Biomedicines | Umbrella review of drugs used for trigeminal neuralgia, covering efficacy and side effects |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Carbamazepine and oxcarbazepine are effective but limited by side effects; newer anticonvulsants and other agents may be useful adjuncts |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | Practical guide to diagnosis and medical and surgical treatment |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Pathophysiology and pharmacological treatments |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clin Evid | Evidence summary on treatments for trigeminal neuralgia |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Current and innovative drug options for typical and atypical trigeminal neuralgia |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka | Lamotrigine is among the off-label alternatives to carbamazepine in Japan, but alternatives are less effective than carbamazepine |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in cluster headache and trigeminal neuralgia |
| [34003166](https://pubmed.ncbi.nlm.nih.gov/34003166/) | 2021 | Review | Neurol India | Medical management of trigeminal neuralgia |

---

## Canada Market Information

Lamotrigine has 20 valid single-ingredient authorisations in Canada and none are cancelled. The compiled records do not include dosage form or approved-indication text. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02381370 | AURO-LAMOTRIGINE |
| 02243803 | LAMICTAL |
| 02302993 | LAMOTRIGINE-150 |
| 02302969 | LAMOTRIGINE-25 |
| 02245210 | APO-LAMOTRIGINE |

---

## Safety Considerations

- **Knowledge-graph contraindication associations:** anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pancytopenia, idiopathic aplastic anaemia, aplastic anaemia and non-infectious meningitis. These come from the knowledge graph, not from label text, and should be checked against the Canadian product monograph.
- **Rash risk:** slow dose titration is needed to limit the risk of rash.
- **Myoclonic generalised syndromes:** lamotrigine may aggravate some of these, which matters when considering reflex or generalised epilepsy types.
- **Drug interactions:** 100 interactions were found. The moderate-level ones include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and orlistat. Metformin is minor, and many others are of unknown severity. The full list should be reviewed before any new use.

Please also refer to the Health Canada package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision:**
- **Trigeminal nerve neoplasm: Hold**
- **Trigeminal neuralgia: Proceed with Guardrails**

**Rationale:**
- The neoplasm prediction has no trials and no tumour-related literature, so the high score likely reflects naming similarity to trigeminal neuralgia.
- Trigeminal neuralgia has two completed small trials, including a head-to-head comparison with carbamazepine, and guideline support as an add-on or second-line option. This reaches L2 only, because the trials are small and there is no confirmatory Phase 3 evidence.

**To proceed, the following is needed:**
- Re-label the top prediction as trigeminal neuralgia, or confirm whether a true neoplasm question is intended.
- A larger, adequately powered randomised trial of lamotrigine in trigeminal neuralgia, since the two completed studies enrolled only 20 and 21 patients.
- The Health Canada package insert warnings and contraindications, with a slow-titration plan for rash risk.
- A review of the drug-interaction burden, especially with opioids and cannabinoids, and of the haematological and liver-related associations.
- Mechanism of action data, to support the mechanistic link analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

