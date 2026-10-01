---
layout: default
title: Desloratadine
parent: Model Prediction Only (L5)
nav_order: 260
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Desloratadine: From H1-Antihistamine Use to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation antihistamine marketed in Canada. The TxGNN model predicts it may be effective for **cold urticaria**, and **3 completed Phase 4 trials** and **3 randomized controlled trial (RCT) publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (Phase 4 randomized trials and RCT publications; no Phase 3 trial in the data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known pharmacology, desloratadine is a selective peripheral H1-receptor inverse agonist. Cold urticaria is a histamine-mediated physical urticaria in which mast cells degranulate after cold exposure. Blocking H1 receptors is therefore mechanistically consistent with the disease. This link comes from general pharmacology, not from the supplied record.

Antihistamines are the standard first-line symptomatic treatment for urticaria, so the prediction is not a stretch. The clinical question is mainly whether desloratadine, and higher-than-label doses in particular, controls cold-triggered symptoms. The trials and RCTs below test exactly that question. The high TxGNN score agrees with the clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg and 20 mg desloratadine on experimentally induced cold urticaria lesions (thermography, volumetry, photography). No results in the record. |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind, dose-escalating study of 5, 10 and 20 mg desloratadine in acquired cold urticaria, aiming to find the dose that inhibits symptoms. No results in the record. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Compares the inhibitory effect of 5 antihistamines in urticaria. The subtype is not specified, so it supports the class effect only. |

Efficacy results were not included in the data. The grading above rests on trial design, and outcomes should be confirmed in the trial records.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study in acquired cold urticaria. High-dose desloratadine decreased wheal volume and improved cold provocation thresholds compared with standard dose. |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | RCT of H1-antihistamine dose escalation using critical temperature threshold measurement in cold urticaria. |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | Desloratadine 5 mg for 4 days was tested with ice-cube provocation before and after treatment in 12 cold urticaria patients. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of chronic urticaria causes, management and treatment options. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case report | J Allergy Clin Immunol Pract | Describes food-dependent cold urticaria as a new variant of physical urticaria. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | First reported case of cold-induced urticaria after black ant bite anaphylaxis. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02546019 | DESLORATADINE |
| 02243919 | AERIUS |
| 02298155 | DESLORATADINE ALLERGY CONTROL |
| 02247193 | AERIUS KIDS |
| 02309300 | AERIUS SINUS + ALLERGY |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized Phase 4 trials and RCT publications test desloratadine, including up-dosing, directly in cold urticaria. The mechanism is consistent with the disease, and the drug is already marketed in Canada. Efficacy outcomes and safety data are still missing from the record.

**To proceed, the following is needed:**
- Confirm outcomes and conditions in NCT00600847, NCT01444196 and NCT01940393, since only titles and designs were available
- Obtain Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Obtain mechanism of action data from DrugBank
- Use the labeled dose first. Treat up-dosing beyond the label as guideline-based off-label use under clinician oversight.
- Rule out atypical or systemic cold-triggered reactions

**Other predicted indications:** nasal cavity disease (Hold at research-question stage; too broad, and the one early-phase trial cannot be confirmed as desloratadine), acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness and rosacea conjunctivitis. The last four are supported by the prediction score only, with no trials or publications, so all are on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

