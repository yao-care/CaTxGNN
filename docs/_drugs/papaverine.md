---
layout: default
title: Papaverine
parent: Moderate Evidence (L3-L4)
nav_order: 706
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Papaverine: predicted new indication Ischemic disease (evidence level L4). Approved use: Peripheral vascular disease, intermittent claudication…"
monitor_inn: "Papaverine"
predicted_indications: ["intracranial arteriosclerosis", "non-inflammatory vasculopathy", "vascular ectasia", "fibrocartilaginous embolism", "venous thromboembolism", "vascular insufficiency disorder", "angiodysplasia", "Monckeberg arteriosclerosis"]
---

# Papaverine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Papaverine: From Peripheral Vascular Disease to Ischemic Disease

## One-Sentence Summary

Papaverine is a smooth muscle vasodilator, originally used for peripheral vascular disease, intermittent claudication, peripheral arterial disease, brain ischemia and transient ischemic attack.
The TxGNN model predicts it may be effective for **ischemic disease**,
but the support is thin: **1 clinical trial** (an observational registry, not a treatment trial) and **20 publications** (mostly reviews, procedural reports and older small studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral vascular disease, intermittent claudication, peripheral arterial disease, brain ischemia, transient ischemic attack |
| Predicted New Indication | Ischemic disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Papaverine is a non-selective smooth muscle vasodilator. It is thought to act by inhibiting phosphodiesterase, which raises cAMP and cGMP in vascular smooth muscle. Detailed mechanism of action data are not available in the data compiled for this report, so this description relies on general pharmacological knowledge.

The original indications (peripheral and cerebral ischemia) and the predicted "ischemic disease" are closely related. Both involve reduced blood flow, and vasodilation to relieve spasm and improve perfusion is a sensible approach. The literature describes papaverine used as an intra-arterial infusion for non-occlusive mesenteric ischemia, as a vasodilator in neurointerventional procedures for vasospasm, and as a pharmacologic stress agent for measuring coronary flow reserve.

These uses are largely procedural or diagnostic, and the evidence is case-level or review-level. The prediction is plausible, but it is not backed by controlled efficacy data. "Ischemic disease" is also a broad category, which partly explains the high score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06125392](https://clinicaltrials.gov/study/NCT06125392) | N/A | Recruiting | 1000 | Multicenter registry of patients with chronic angina and no obstructive coronary stenosis, collecting data on microvascular dysfunction and coronary spasm. Observational, so it offers only indirect context. |

---

## Literature Evidence

The list below covers the most relevant publications. Most are reviews, case-level reports or older studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3661361](https://pubmed.ncbi.nlm.nih.gov/3661361/) | 1987 | Clinical study (diagnostic) | Am Heart J | Intracoronary papaverine was superior to radiographic contrast for measuring coronary flow reserve in ischemic heart disease |
| [16368347](https://pubmed.ncbi.nlm.nih.gov/16368347/) | 2006 | Comparative study | Ann Thorac Surg | Compared papaverine with glyceryl trinitrate-verapamil solution for internal thoracic artery spasm |
| [28455799](https://pubmed.ncbi.nlm.nih.gov/28455799/) | 2018 | Case report | J Robot Surg | Periarterial papaverine treated renal artery vasospasm during partial nephrectomy |
| [32713799](https://pubmed.ncbi.nlm.nih.gov/32713799/) | 2020 | Preclinical (mouse) | J Pharmacol Sci | Papaverine reduced infarct volume in focal cerebral ischemia and showed anti-inflammatory effects |
| [28832798](https://pubmed.ncbi.nlm.nih.gov/28832798/) | 2017 | Preclinical (rat) | Braz J Cardiovasc Surg | Papaverine and vitamin C were studied against liver ischemia-reperfusion injury after aortic cross-clamping |
| [21761272](https://pubmed.ncbi.nlm.nih.gov/21761272/) | 2011 | Guideline/Review | Neurocrit Care | Critical care guidelines on endovascular management of cerebral vasospasm |
| [7590571](https://pubmed.ncbi.nlm.nih.gov/7590571/) | 1995 | Review | Hepatogastroenterology | Non-occlusive mesenteric ischemia and its management |
| [11341865](https://pubmed.ncbi.nlm.nih.gov/11341865/) | 2001 | Review | Curr Treat Options Cardiovasc Med | Mesenteric vascular disease; medical and endovascular options in early stages |
| [8293164](https://pubmed.ncbi.nlm.nih.gov/8293164/) | 1993 | Review | Curr Opin Neurol | Interventional neuroradiology, including superselective papaverine infusion for post-rupture vasospasm |
| [266914](https://pubmed.ncbi.nlm.nih.gov/266914/) | 1977 | Review | Aust N Z J Surg | Acute mesenteric ischaemia; mortality remained very high |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00009881 | PAPAVERINE HYDROCHLORIDE INJECTION USP | Not stated | Not stated |

---

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text)**: The TxGNN knowledge graph links papaverine to contraindications in liver disease, gallbladder disease, hypotensive disorder, coronary artery disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, sudden cardiac arrest, heart conduction disease, atrioventricular block and glaucoma.
- **Drug Interactions**: 100 interactions were found. Among the 20 reviewed, most are Major, including abiraterone, tramadol, adenosine, salbutamol, alfuzosin, amiodarone, amisulpride, amitriptyline, anagrelide, propofol, loperamide, apalutamide, apomorphine, arsenic trioxide, lumefantrine, asenapine and atomoxetine. Moderate ones include amifostine, apraclonidine and aripiprazole. Many of these involve QT prolongation or additive cardiovascular effects.

Please refer to the package insert for labelled warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.91%), but the supporting evidence is weak. The only registered trial is an observational registry, and the literature consists mostly of reviews, case reports, procedural or diagnostic uses, and animal studies. The overlap with the existing peripheral and cerebral ischemia indications also means this is not a clearly new indication. The knowledge graph flags several cardiovascular contraindications, and the label safety information has not been reviewed.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- A narrower, clinically defined indication (for example, non-occlusive mesenteric ischemia or cerebral vasospasm) in place of the broad "ischemic disease" label
- Controlled clinical data for that specific indication
- Review of the cardiovascular drug interactions and the knowledge graph contraindications
- Confirmation of dosage form, route and approved indication for the Canadian product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

