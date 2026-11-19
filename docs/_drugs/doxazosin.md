---
layout: default
title: Doxazosin
parent: Moderate Evidence (L3-L4)
nav_order: 303
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "DOXAZOSIN"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
description: "Doxazosin: predicted new indication Migraine disorder (evidence level L4). In Canada: 9 DINs (9 marketed)"
---

# Doxazosin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Doxazosin: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Doxazosin is an alpha-1 adrenergic blocker originally used to treat hypertension and benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **migraine disorder**,
but currently only **0 registered clinical trials** and **1 publication** (a small 1997 review of 10 patients) support this direction, so it remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (marketed DINs: 9 of 9) |
| Number of DINs | 9 (marketed: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxazosin: "Benign Prostatic Hyperplasia (BPH) The symptoms associated with benign prostatic hyperplasia (BPH), such as urinary frequency, nocturia, weak stream, hesitancy, and incomplete emptying are related to two components, anatomical (static) and functional (dynamic). The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Studies in normal human subjects have shown that doxazosin competitively antagonized the pressor effects of phenylephrine (an alpha 1 agonist) and the systolic pressor effect of norepinephrine." ([DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82), label version 2023-10-15; accessed 2026-11-19.) Based on general pharmacology, doxazosin is a selective alpha-1 adrenergic receptor antagonist. Its efficacy in hypertension and BPH is well established, and it works by relaxing vascular and prostatic smooth muscle.

Adrenergic signalling influences cerebrovascular tone and sympathetic activity, both of which are hypothesised to play a role in migraine. This offers a plausible but indirect rationale for migraine prophylaxis.

The only supporting publication is a 1997 report in which 10 patients in a neurology practice received terazosin or doxazosin. Migraine frequency or severity decreased in all but one patient, but five stopped treatment because of side effects. This is conceptual support only. The very high TxGNN score is a computational signal, not clinical evidence.

A second predicted indication, migraine with brainstem aura, has no trials or literature. It likely reflects closeness to the parent migraine term in the ontology rather than independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review | Headache | Ten migraine patients were given terazosin or doxazosin. Nine had fewer or milder migraines, but five discontinued because of side effects. No serious adverse reactions were reported. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240588 | APO-DOXAZOSIN | Not available | Not available |
| 02240589 | APO-DOXAZOSIN | Not available | Not available |
| 02240590 | APO-DOXAZOSIN | Not available | Not available |
| 02242728 | TEVA-DOXAZOSIN | Not available | Not available |
| 02242729 | TEVA-DOXAZOSIN | Not available | Not available |

Nine single-ingredient licences are valid in total (APO, TEVA and JAMP brands); the five above are shown as the main ones.

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, liver failure, liver disease, gallbladder disease, pyloric stenosis, intestinal obstruction, priapism, and intraoperative floppy iris syndrome.
- **Drug Interactions**: The interaction screening returned 100 interactions in total. The listed ones are mostly of Moderate severity, including:
  - Corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Opioids (morphine, opium)
  - Cannabinoids (dronabinol, nabilone)
  - Bupropion and clarithromycin
- Interactions with calcitriol, clotrimazole and cimetidine are of unknown severity.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence consists of one small, 1997 uncontrolled report and a model prediction, with no registered trials. The mechanism is plausible but indirect, and the patient-reported side-effect burden (5 of 10 discontinued) is a concern. This is a research question rather than a candidate ready for development.

**To proceed, the following is needed:**
- Controlled clinical data (at least a well-designed Phase 2 trial) of doxazosin for migraine prophylaxis
- A systematic literature search beyond the single identified publication
- Official mechanism of action data
- Health Canada package insert warnings and contraindications, as well as approved indication text and dosage forms for each DIN
- A tolerability and orthostatic hypotension risk assessment for migraine populations, who are often younger and normotensive

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

