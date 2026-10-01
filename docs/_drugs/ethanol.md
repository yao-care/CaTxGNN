---
layout: default
title: Ethanol
parent: Model Prediction Only (L5)
nav_order: 361
evidence_level: L5
indication_count: 2
---

# Ethanol
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

# Ethanol: From an Unrecorded Original Indication to Migraine Disorder

## One-Sentence Summary

Ethanol is marketed in Canada through 2 registered products, but no approved indication is recorded in the available data.
The TxGNN model predicts it may be relevant to **migraine disorder**, with a score of 99.29%. However, **none of the 35 retrieved clinical trials tests ethanol as a migraine treatment**.
The 20 retrieved publications mostly describe ethanol as a migraine **trigger**, so the evidence argues against this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 (preclinical and mechanism studies only, and they point toward harm) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ethanol, so the link between its original use and migraine cannot be analysed directly.

The TxGNN score is a graph-association signal, not evidence of therapeutic benefit. The published literature points the other way. Reviews report that about one-third of migraine patients name alcohol as an occasional trigger, and only about 10% name it as a consistent one. A 2023 systematic review and meta-analysis found the relationship between alcohol and primary headaches inconclusive.

A 2023 preclinical mouse study (PMID 37101198) offers a possible mechanism, and it is pro-nociceptive. Ethanol is metabolised to acetaldehyde, which acts through the CGRP receptor and TRPA1 in Schwann cells to cause periorbital mechanical allodynia. This suggests ethanol may promote migraine-like pain rather than relieve it.

The second-ranked prediction, migraine with brainstem aura (score 99.14%), has no clinical trials. Its literature is mainly genetic association studies and studies of palmitoylethanolamide (PEA). PEA is a different compound from ethanol and probably appeared through keyword matching. It provides no support for ethanol.

---

## Clinical Trial Evidence

The search returned 35 trials. Most were matched on the condition (migraine or headache) and do not involve ethanol. Only the first trial below involves an alcohol intervention, and it uses isopropyl alcohol, not ethanol. The other trials listed are shown to illustrate the mismatch.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05175521](https://clinicaltrials.gov/study/NCT05175521) | N/A | Completed | 21 | Double-blind RCT of inhaled isopropyl alcohol vapour vs eucalyptus scent for nausea in acute migraine. The intervention is isopropyl alcohol, not ethanol, and the study is small. It is the only alcohol-vapour migraine trial in the set. |
| [NCT00109083](https://clinicaltrials.gov/study/NCT00109083) | Phase 2 | Completed | 300 | Dose-ranging placebo-controlled trial of RWJ-333369 for migraine prophylaxis. Ethanol is not the intervention. |
| [NCT07301008](https://clinicaltrials.gov/study/NCT07301008) | Phase 4 | Recruiting | 60 | Rimegepant as preemptive treatment for trigger-induced migraine. Alcohol appears only as an allowed trigger. |
| [NCT02810015](https://clinicaltrials.gov/study/NCT02810015) | Phase 2 | Unknown | 40 | Botulinum toxin for temporo-myofascial disorder. Not an ethanol or migraine indication. |
| [NCT07297901](https://clinicaltrials.gov/study/NCT07297901) | N/A | Enrolling by invitation | 30 | App-based breathing program for migraine. Non-drug intervention. |
| [NCT03404336](https://clinicaltrials.gov/study/NCT03404336) | N/A | Recruiting | 30 | Well-being therapy pilot RCT in chronic migraine. Psychological intervention. |
| [NCT07762690](https://clinicaltrials.gov/study/NCT07762690) | N/A | Not yet recruiting | 80 | Cervical sensorimotor rehabilitation in chronic migraine. Non-drug. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37612595](https://pubmed.ncbi.nlm.nih.gov/37612595/) | 2023 | Systematic review and meta-analysis | J Headache Pain | Assesses alcohol intake in people with primary headaches. The existing literature is inconclusive, although migraine patients tend to avoid alcohol. |
| [18231712](https://pubmed.ncbi.nlm.nih.gov/18231712/) | 2008 | Review | J Headache Pain | About one-third of migraine patients report alcohol as an occasional trigger, and only about 10% as a consistent one. |
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Reviews the complex relationship between alcohol and migraine. |
| [41305669](https://pubmed.ncbi.nlm.nih.gov/41305669/) | 2025 | Review | Nutrients | Reviews alcohol as a trigger for migraine, tension-type headache and other primary headaches. The pathophysiological mechanism remains unknown. |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preclinical (mouse) | J Biomed Sci | Acetaldehyde, acting via CGRP receptor and TRPA1 in Schwann cells, mediates ethanol-evoked periorbital allodynia. This is a pro-migraine pathway. |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetic association | Headache | Tests the association of an ADH2 alcohol-metabolism variant with migraine risk. It does not show therapeutic benefit. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2246888 | AVAGARD CHG |
| 2230769 | DALMACOL |

Dosage form and approved indication text are not available for either product.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is only a computational association. Not one of the 35 retrieved trials tests ethanol for migraine. The mechanistic and clinical literature identifies ethanol as a migraine trigger, so the available evidence argues against repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- The original approved indication and dosage form for each Canadian product
- Mechanism of action data from DrugBank
- Any direct human evidence that ethanol relieves migraine. None currently exists, and the preclinical data suggest the opposite.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

