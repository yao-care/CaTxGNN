---
layout: default
title: Flunarizine
parent: Model Prediction Only (L5)
nav_order: 390
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Flunarizine: From an Unlisted Original Indication to Migraine Disorder

## One-Sentence Summary

Flunarizine is a calcium channel blocker. Its original approved indication is not recorded in the Canadian license data supplied, and a trial summary describes it as traditionally used for vertigo and migraine.
The TxGNN model predicts it may be effective for **migraine disorder** (score 99.12%), with **19 clinical trials** and **20 publications** currently linked to this direction.
Guidelines and meta-analyses already support flunarizine for migraine prevention, but no completed Phase 3 flunarizine trial is itemised in the data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license record |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L3 (systematic reviews and meta-analyses; no completed Phase 2/3 flunarizine RCT in the supplied data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

DrugBank mechanism-of-action data is not available in the supplied data. The following comes from general pharmacology. Flunarizine is a selective calcium entry blocker (L-type and T-type channels) with additional antihistamine (H1) and weak dopamine D2 antagonist activity.

These actions are thought to reduce cortical spreading depression and neuronal hyperexcitability, and to stabilise cerebral vascular tone. This makes flunarizine biologically plausible for migraine prophylaxis. A trial summary in the pack (NCT00740259) also describes it as traditionally used for vertigo and migraine.

The prediction is consistent with existing practice. The Canadian Headache Society guideline and the AAN pediatric migraine prevention update appear in the literature set. So do a European Headache Federation meta-analysis specific to flunarizine and several network meta-analyses. Because these summarise underlying RCTs that are not itemised here, the true evidence base is probably stronger than the L3 level assigned.

---

## Clinical Trial Evidence

Of 19 registered trials, the 10 most relevant are listed. Most are comparator or head-to-head studies in which flunarizine is an active arm. Only NCT00752466 is a Phase 1 pharmacokinetic study, and none is a completed Phase 3 flunarizine RCT.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | Completed | 120 | Greater occipital nerve block vs topiramate vs flunarizine in episodic migraine; compares VAS pain scores and attack frequency |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | Recruiting | 44 | Flunarizine vs propranolol in children aged 8-15, measured by PedMIDAS score |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | Unknown | 84 | Flunarizine vs amitriptyline for migraine prophylaxis; compares attack frequency and pain score |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not yet recruiting | 460 | Pragmatic primary-care trial comparing amitriptyline, flunarizine, topiramate and propranolol |
| [NCT03828539](https://clinicaltrials.gov/study/NCT03828539) | Phase 4 | Completed | 777 | Erenumab vs topiramate; participants had failed or were unsuitable for up to three prophylactics, including flunarizine |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Completed | 60 | Add-on alpha-lipoic acid for adolescent migraine prophylaxis; the linked publication (PMID 37563914) shows a flunarizine background arm |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Pharmacokinetic interaction study of flunarizine with topiramate; no efficacy data |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | NA | Active, not recruiting | 60 | Pulsed radiofrequency vs calcium channel blockers in childhood migraine |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | NA | Unknown | 96 | Acupuncture for migraine without aura; flunarizine is named as the current standard therapy |

---

## Literature Evidence

Of 20 publications, the 10 most relevant are listed, prioritising systematic reviews, guidelines and RCTs.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Systematic review / meta-analysis | J Headache Pain | European Headache Federation appraisal of flunarizine, described as a repurposed first- or second-line migraine prophylactic |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic review / meta-analysis | J Assoc Physicians India | Compares amitriptyline with propranolol and flunarizine for migraine prophylaxis efficacy and safety |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review | Health Technol Assess | Preventive drugs for chronic migraine, with economic modelling |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network meta-analysis | JAMA Netw Open | Efficacy and safety of preventive medications in pediatric migraine |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Guideline | Neurology | AAN/AHS update on pharmacologic prevention of pediatric migraine |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Guideline | Can J Neurol Sci | Canadian Headache Society guideline for migraine prophylaxis in episodic migraine |
| [2404346](https://pubmed.ncbi.nlm.nih.gov/2404346/) | 1990 | Double-blind trial | S Afr Med J | Flunarizine 10 mg nightly vs propranolol 60 mg three times daily over 4 months in 58 patients |
| [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/) | 1997 | Postmarketing study | Pharm World Sci | Open multicentre study of flunarizine vs propranolol in 686 migraine patients, with attention to depression and extrapyramidal events |
| [37563914](https://pubmed.ncbi.nlm.nih.gov/37563914/) | 2023 | RCT | J Clin Pharmacol | 60 adolescents randomised to flunarizine or flunarizine plus add-on alpha-lipoic acid |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | Clinical study | Acta Neurol Scand | Flunarizine plus transcutaneous supraorbital neurostimulation vs either alone for migraine prophylaxis |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2246082 | FLUNARIZINE |

Dosage form, manufacturer and approved indication text are not recorded for this authorization.

---

## Safety Considerations

- **Drug Interactions**: No interactions were found in the queried database. A completed Phase 1 study (NCT00752466) examined the pharmacokinetic interaction between flunarizine and topiramate.

Please refer to the package insert for warnings and contraindications.

Guardrails from general pharmacology, not from the supplied safety data:
- Monitor for depression, extrapyramidal symptoms or parkinsonism (especially in older patients), sedation and weight gain.
- Avoid use in patients with a history of depression or Parkinson's disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score is very high (99.12%), and flunarizine is already an established migraine prophylactic in guidelines and meta-analyses. The supplied data shows no completed Phase 3 flunarizine RCT, and Canadian labelling and safety data are missing. The prediction should therefore go forward with the safety guardrails above, pending label review.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications and approved indication) for DIN 2246082
- Confirmation of whether migraine prophylaxis is within the Canadian labelled indication
- DrugBank mechanism-of-action data
- Extraction of the individual RCTs behind the guidelines and meta-analyses to confirm the evidence level
- A monitoring plan for depression and extrapyramidal symptoms, especially in older patients and children

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

