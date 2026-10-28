---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Mexiletine"
predicted_indications: ["hypertrichosis (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "migraine disorder", "isolated genetic hair shaft abnormality", "pulmonary hypertension", "migraine with brainstem aura", "headache disorder"]
description: "Mexiletine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mexiletine
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

## Mexiletine: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Mexiletine is a class IB antiarrhythmic sodium channel blocker marketed in Canada. The TxGNN model's top-ranked predictions (such as hypertrichosis) have no supporting evidence, so this report focuses on the best-supported prediction, **headache disorder** (migraine disorder is closely related), which has **0 clinical trials** and **5 publications**, all small and uncontrolled. The evidence is limited to case series and open-label studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 (headache disorder, migraine disorder); L5 (hypertrichosis) |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Hold (headache: research question only, not ready for development) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, mexiletine is a class IB antiarrhythmic that blocks voltage-gated sodium channels. It is also used in practice for neuropathic pain and myotonia.

The link to headache is plausible because sodium channel blockade may reduce neuronal hyperexcitability and dampen trigeminal-autonomic and central sensitization pathways. Related drugs (lidocaine and mexiletine) have been reported in trigeminal autonomic cephalalgias and refractory chronic daily headache.

The other top-scoring predictions, such as hypertrichosis, nephrogenic syndrome of inappropriate antidiuresis (a vasopressin V2 receptor gain-of-function disorder), and congenital malformation syndromes, have no plausible mechanistic link and no trials or publications. They are computational predictions only. Pulmonary hypertension has only indirect preclinical support from a lidocaine study, and it is not shown that mexiletine shares that activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with single-arm meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT/SUNA, rare headache conditions with scarce evidence-based recommendations |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Clinical report | Curr Pain Headache Rep | IV lidocaine and mexiletine (class 1B sodium channel blockers) in trigeminal autonomic cephalalgias |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series | Headache | Mexiletine in nine patients with refractory chronic daily headache |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Early clinical report | N Z Med J | Mexiletine and vascular headaches |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Review | Cochrane Database Syst Rev | Drug treatment for myotonia (not direct headache evidence) |

Note: These studies are small, uncontrolled and heterogeneous, and SUNCT/SUNA and chronic daily headache are related to, but not identical with, migraine. For pulmonary hypertension, the only items are a 2026 preclinical lidocaine study (PMID 41518899) and a 1991 ventricular arrhythmia study (PMID 1724233), neither of which is direct evidence.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02536846 | MINT-MEXILETINE | Not specified | Not specified |
| 02536854 | MINT-MEXILETINE | Not specified | Not specified |
| 02230359 | TEVA-MEXILETINE | Not specified | Not specified |
| 02230360 | TEVA-MEXILETINE | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): epilepsy, liver disease, gallbladder disease, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome.
- **Drug Interactions**: 100 interactions were identified. Notable ones:
  - **Major**: Bupropion
  - **Moderate**: Alosetron, Morphine, Lorcaserin, Potassium citrate, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Eliglustat, Obeticholic acid, Sodium sulfate, Glycerol phenylbutyrate, Rolapitant
  - **Minor**: Ascorbic acid
- Mexiletine's cardiac proarrhythmic profile requires particular attention in any new use.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-scoring predictions have no trials, no literature and no mechanistic basis. Headache disorder and migraine have only small, uncontrolled studies (L3), with no RCT and no registered trial. This is a research question, not a development candidate.

**To proceed, the following is needed:**
- Mechanism of action data and the Health Canada package insert (warnings, contraindications, approved indications)
- A controlled study, or a systematic review of existing headache reports, defining the target subtype (for example SUNCT/SUNA or refractory chronic daily headache rather than migraine in general)
- A cardiac safety monitoring plan (ECG, conduction disease screening) and a review of the interaction burden, including the major interaction with bupropion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

