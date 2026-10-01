---
layout: default
title: Ketorolac
parent: Model Prediction Only (L5)
nav_order: 508
evidence_level: L5
indication_count: 3
---

# Ketorolac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ketorolac: From NSAID Analgesic Use to Headache Disorder

## One-Sentence Summary

Ketorolac is a marketed non-steroidal anti-inflammatory drug (NSAID) used as an analgesic.
The TxGNN model predicts it may be effective for **Headache Disorder** (mainly acute migraine), with **many registered clinical trials** and **published RCTs, systematic reviews and guidelines** in this direction.
Note that ketorolac for acute migraine is already an established off-label use, so this is not a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 (pipeline-assigned; see caveat in the conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ketorolac is a non-selective COX-1/COX-2 inhibitor. Blocking prostaglandin synthesis reduces peripheral and central sensitization and neurogenic inflammation, both of which contribute to migraine and other headache pain. Detailed original mechanism-of-action data is not recorded in the Evidence Pack. However, ketorolac's marketed analgesic use is consistent with this mechanism.

Headache pain, especially migraine, is driven in part by inflammatory and prostaglandin-mediated pathways. This is why an NSAID analgesic is a mechanistically sensible fit.

The strongest support is clinical rather than model-based. Ketorolac is already used for acute migraine, particularly in emergency departments. It is an active arm in randomized comparisons against metoclopramide, valproate, meperidine and sumatriptan. The prediction is best read as confirming an existing practice.

---

## Clinical Trial Evidence

Ketorolac-related trials in headache, selected from the retrieved list (only registry summaries are available, and no results are reported here):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | Randomized comparison of IV valproate, IV metoclopramide and IV ketorolac for acute migraine |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Non-inferiority trial of intranasal vs intravenous ketorolac for pediatric migraine |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind, placebo-controlled study of intranasal ketorolac for acute migraine |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac plus metoclopramide combination for pediatric migraine in the emergency department |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Metoclopramide/diphenhydramine vs ketorolac alone for tension-type headache |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute tension-type headache |
| [NCT02664116](https://clinicaltrials.gov/study/NCT02664116) | Phase 4 | Unknown | 40 | IM ketorolac vs oral diclofenac potassium powder (Cambia) for severe migraine |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal vs IV ketorolac, each with oral adjuncts, for pediatric migraine |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Neostigmine plus atropine vs ketorolac for post-dural puncture headache |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | Compared IV metoclopramide alone with metoclopramide plus IV ketorolac for pediatric migraine in the emergency department |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | Double-blind trial of IV dexamethasone, metoclopramide, ketorolac and chlorpromazine for pain relief and recurrence prevention in migraine |
| [41100185](https://pubmed.ncbi.nlm.nih.gov/41100185/) | 2025 | RCT | Cephalalgia | Greater occipital nerve block added to triple therapy vs triple therapy alone in acute migraine in the emergency department |
| [39428459](https://pubmed.ncbi.nlm.nih.gov/39428459/) | 2024 | Semi-experimental | Chin Neurosurg J | IV ketorolac vs IV acetaminophen for headache after head trauma |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | Double-blind trial of IM ketorolac vs meperidine plus hydroxyzine for acute migraine |
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic review/meta-analysis | Acad Emerg Med | Evaluated the efficacy of parenteral ketorolac for acute migraine |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic review/meta-analysis | Adv Clin Exp Med | Updated comparison of IV ketorolac vs metoclopramide in adults with migraine |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic review/guideline | Cephalalgia | Canadian Headache Society recommendations on migraine pain treatment in emergency settings |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/evidence assessment | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Curr Pain Headache Rep | Overview of IV migraine treatments in children; notes a lack of well-designed randomized pediatric studies |

---

## Canada Market Information

Of 14 authorizations, the 5 main ones are listed. Dosage form and approved-indication text are not recorded in the source data.

| DIN | Product Name |
|---------|------|
| 02369362 | ACUVAIL |
| 02245821 | KETOROLAC |
| 02162644 | TORADOL IM |
| 01968300 | ACULAR |
| 02390582 | KETOROLAC TROMETHAMINE INJECTION USP |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the drug-interaction query. However, a published case report (PMID 7928331, 1994) describes **lithium neurotoxicity in a patient with cluster headache after ketorolac was co-administered**. Lithium is used in cluster headache, so this is a relevant safety signal, though it is case-level evidence only.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ketorolac has a plausible COX-inhibition mechanism, multiple randomized trials and meta-analyses in acute migraine, and guideline coverage. Two cautions apply:
- The relevant trials are mostly small and Phase 4. Only one Phase 3 completed trial (NCT02358681, n=59) is clearly ketorolac-specific, so the L1 level is generous under a strict reading of the rules.
- This is an existing off-label use rather than a new discovery.

**Other predicted indications:**
- **Trigeminal autonomic cephalalgia** (score 99.39%, L4, Research Question): evidence is limited to a general review and the lithium case report.
- **Rosacea conjunctivitis** (score 99.40%, L5, Hold): model prediction only, with no trials or publications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Approved-indication text and dosage forms for the Canadian DINs, to confirm the original indication and route compatibility
- Extraction of actual results from the key ketorolac trials and meta-analyses (efficacy vs metoclopramide and other comparators), since only aims and summaries were available here
- A safety plan for common NSAID risks in headache patients, including lithium co-administration, and a pediatric dosing review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

