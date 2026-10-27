---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 733
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
monitor_inn: "PHENYTOIN"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is an established antiseizure medication, originally used for epilepsy, including generalized tonic-clonic seizures, partial seizures, status epilepticus and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** (top-ranked prediction), but there are **0 clinical trials** and only **2 publications**, neither of which addresses a tumour.
The more clinically credible direction among the predictions is **trigeminal neuralgia**, which has literature support (L3) but is not a tumour indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the product-level approved indication text was not available in the data compiled for this report; the original indication comes from knowledge-graph indication edges) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, phenytoin is a voltage-gated sodium channel blocker that stabilizes hyperexcitable neuronal membranes and limits seizure spread. Its efficacy in epilepsy is well established.

For the top-ranked prediction, **trigeminal nerve neoplasm**, there is no plausible mechanistic link between sodium channel blockade and tumour control. The two retrieved publications concern trigeminal neuralgia treatment and Sturge-Weber syndrome, not neoplasm. The high score most likely reflects graph proximity to trigeminal nerve disorders and neuralgia rather than an antineoplastic effect. This prediction should be treated as a probable model artifact.

Other high-scoring predictions fall into three groups:
- **Reflex or special seizure types** (startle epilepsy, micturition-induced, audiogenic, thinking, orgasm-induced, eating and reading seizures): sodium channel blockade is plausible, but these overlap with existing epilepsy indications, so they are not true repurposing candidates. Direct evidence is sparse (a single case report for micturition/defecation seizures; animal studies for audiogenic seizures).
- **Trigeminal neuralgia** (score 99.97%): this is the most credible new direction. Phenytoin shares the sodium-channel mechanism underlying carbamazepine's efficacy, and it appears as a second-line or acute option in the literature. Carbamazepine and oxcarbazepine remain first-line.
- **Beta-ketothiolase deficiency**: no mechanistic link, no trials, no literature; likely a graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; concerns neuralgia, not neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | Experience with 14 Sturge-Weber syndrome cases; no tumour-treatment evidence for phenytoin |

For context, the trigeminal neuralgia prediction (not the headline prediction) is supported by items such as a 2022 retrospective analysis of 144 cases of intravenous lacosamide and phenytoin for acute exacerbations ([35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/)), a 2020 retrospective cohort of IV phenytoin as rescue treatment ([32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/)), and a 2017 appraisal of phenytoin and carbamazepine ([28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/)). No randomized trials were identified in the data.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02250896 | TARO-PHENYTOIN | Not available | Not available |
| 00023698 | DILANTIN INFATABS | Not available | Not available |
| 00022772 | DILANTIN | Not available | Not available |
| 00498335 | PHENYTOIN SODIUM INJECTION USP | Not available | Not available |
| 00022780 | DILANTIN | Not available | Not available |

Eight valid single-ingredient authorizations are listed in total; only the first five are shown. No cancelled licences were recorded.

---

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text)**: long QT syndrome and torsades de pointes, liver failure and liver disease, porphyria, kidney disease, thrombocytopenia, neutropenia and agranulocytosis, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus, hypotensive disorder, hepatic coma and hepatic encephalopathy, anxiety and related disorders, substance abuse/dependence, and sleep apnea syndromes.
- **Drug interactions**: 100 interactions were identified in total. Examples at Moderate level include acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, metformin, pioglitazone, bupropion, aprepitant, morphine, omeprazole, metronidazole, cholecalciferol and calcifediol. Acetylsalicylic acid is Minor.
- **Literature-reported adverse effects**: thrombocytopenia, hyperglycemia/diabetic ketoacidosis, EMPACT syndrome (erythema multiforme with cranial radiation), peripheral neuropathy, ophthalmoplegia, gingival hyperplasia, and bone health effects.
- Phenytoin has a narrow therapeutic index, so drug-level monitoring is important. Please refer to the package insert for official warnings and contraindications, as label text was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, rests on a very high model score but has no trials, no tumour-specific literature, and no plausible mechanistic link, so it appears to be a graph artifact. The seizure-type predictions overlap with existing epilepsy indications, and trigeminal neuralgia (L3) is the only direction with meaningful literature, though it remains a second-line option behind carbamazepine and oxcarbazepine.

**To proceed, the following is needed:**
- Re-focus the evaluation on trigeminal neuralgia as a research question, with a structured review of the evidence for phenytoin versus first-line agents
- Mechanism of action data and Health Canada package insert warnings and contraindications (not currently available)
- Product-level approved indication text and dosage forms for the Canadian DINs
- A drug interaction and therapeutic drug monitoring plan, given the 100 identified interactions and narrow therapeutic index
- Prospective or randomized evidence if any acute or rescue use in trigeminal neuralgia is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

