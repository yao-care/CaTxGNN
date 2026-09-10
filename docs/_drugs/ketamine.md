---
layout: default
title: Ketamine
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ketamine: From General Anesthesia to Headache Disorder

## One-Sentence Summary

Ketamine is a dissociative anesthetic historically used for the induction and maintenance of general anesthesia. The TxGNN model predicts it may be effective for **headache disorder** (including migraine and cluster headache), with **39 clinical trials** and **19 publications** identified in the evidence pool — though only a subset directly test ketamine in headache populations, with the strongest support coming from a completed Phase 3 randomized trial (THINK Trial) and several completed cluster-headache/ED studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug is not currently marketed in Taiwan); internationally known as a dissociative general anesthetic |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for ketamine was not available in this evidence pack. Based on known pharmacology, ketamine is a **non-competitive NMDA receptor antagonist**. NMDA receptor activation is closely tied to central sensitization, cortical spreading depression (a core pathological mechanism in migraine), and trigeminovascular nociceptive signaling. Blocking NMDA signaling can reduce pain sensitization and nociceptive transmission underlying refractory headache and migraine.

This mechanistic pathway is not a repurposing from an unrelated indication — ketamine has long been used off-label in pain medicine (sub-dissociative dosing) for refractory chronic pain conditions, and its analgesic properties in emergency and palliative settings are well documented. The predicted extension into headache disorder is therefore a natural mechanistic and clinical-practice extension rather than a novel hypothesis, and this is reflected in the existing trial base (ED headache trials, chronic cluster headache trials).

The main caveats are ketamine's well-known dissociative/psychotomimetic effects and hemodynamic effects (transient blood pressure and heart rate increases), which mean any headache indication would need to be pursued at sub-dissociative doses with clinical monitoring, not as an unsupervised outpatient therapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial — RCT of intranasal sub-dissociative ketamine vs. standard therapy for acute primary headache in the ED; the most direct L1-grade evidence |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | CHECK Trial — multicenter RCT comparing low-dose ketamine vs. Compazine (prochlorperazine) for ED headache control |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine spray for refractory chronic cluster headache |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead Study — multicenter placebo-controlled RCT of high-dose IV ketamine infusion for chronic daily headache |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | Single ketamine + magnesium sulfate infusion for refractory chronic cluster headache |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A (RCT) | Completed | 34 | Placebo-controlled RCT of sub-dissociative IV ketamine for acute migraine-type headache in the ED |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Open-label RCT of oral ketamine + aspirin vs. rimegepant (Nurtec) for acute ED headache |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs. ketorolac for acute tension-type headache in the ED |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Placebo-controlled RCT of ketamine and/or stellate ganglion block for TBI-associated headache and PTSD |
| [NCT01686009](https://clinicaltrials.gov/study/NCT01686009) | Phase 4 | Completed | 40 | Intranasal ketamine for general ED analgesia — supportive mechanistic evidence, not headache-specific |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Cohort | Frontiers in Neurology | Retrospective cohort study finding IV lidocaine + ketamine infusions effective and reasonably safe for inpatient headache disorders |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Review of cluster headache pharmacotherapy, noting ketamine as an option for refractory pain syndromes |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on trigeminal neuralgia pharmacotherapy listing ketamine as a promising adjuvant option |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Current Pain and Headache Reports | Evidence-based review of complex regional pain syndrome treatment, including ketamine's role in refractory chronic pain |
| [35416105](https://pubmed.ncbi.nlm.nih.gov/35416105/) | 2022 | Review | Expert Opinion on Drug Safety | Review of long-term safety of ketamine/esketamine across psychiatric and pain-related uses |

*Note: the remaining literature identified by the search (mostly esketamine trials in treatment-resistant depression) relate to ketamine's psychiatric use rather than headache disorder and were excluded as low relevance.*

## Canada/Taiwan Market Information

Ketamine currently holds **no marketing licenses on file** and is listed as **not marketed** in this jurisdiction (0 licenses, no dosage-form records available). No product-level table can be generated from the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack (labeled as a **Blocking** data gap — TFDA label/warning data must be obtained before this candidate can enter safety pre-screening). Given ketamine's known profile (dissociative/psychotomimetic effects, transient hypertension/tachycardia, abuse/dependence potential as a controlled substance), a full label review is required regardless of repurposing evidence strength.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is strong (NMDA antagonism → reduced central sensitization) and is backed by one completed Phase 3 RCT (THINK Trial) plus multiple completed Phase 1/2–4 studies specifically in cluster headache, migraine, and ED headache populations. However, the drug is not currently marketed locally, and a **Blocking**-severity data gap on label warnings/contraindications means safety pre-screening (S1) cannot yet be completed.

**To proceed, the following is needed:**
- TFDA label / prescribing information (warnings, contraindications) — required before S1 safety assessment
- Confirmed drug-drug interaction data (current query returned no results)
- Full mechanism-of-action documentation (original_moa is currently a data gap)
- A regulatory pathway assessment given the drug's current "not marketed" status and controlled-substance handling requirements
- Completion of the ongoing Phase 3 KetHead trial (NCT05306899) to strengthen the evidence base before any Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

