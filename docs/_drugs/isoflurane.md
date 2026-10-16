---
layout: default
title: Isoflurane
parent: Model Prediction Only (L5)
nav_order: 498
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Isoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Canadian license data (isoflurane is generally used…"
monitor_inn: "ISOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
---

# Isoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Isoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is an inhaled general anesthetic that is marketed in Canada. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a **model prediction only**, with **0 clinical trials** and **0 publications** supporting it. Among the other predicted indications, migraine disorder has the most supporting material (12 publications, mostly preclinical).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (isoflurane is generally used for inhaled general anesthesia) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, isoflurane is a volatile anesthetic that enhances GABA-A receptor activity and inhibits NMDA and nicotinic receptors. It also relaxes vascular smooth muscle.

For Prinzmetal angina (coronary vasospasm), the vasodilatory effect and modulation of calcium channels in vascular smooth muscle could theoretically be relevant. However, isoflurane can also cause "coronary steal" in some settings, which could be harmful. No clinical or literature evidence was found to support this link, so the prediction remains speculative.

The other predicted indications are ranked below. Only migraine and manic bipolar disorder have any supporting literature.

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 1 | Prinzmetal angina | 99.67% | L5 | Prediction only |
| 2 | Tourette syndrome | 99.61% | L5 | Prediction only |
| 3 | Manic bipolar affective disorder | 99.57% | L4 | Indirect evidence only |
| 4 | Trichotillomania | 99.54% | L5 | Prediction only |
| 5 | Dysthymic disorder | 99.27% | L5 | Prediction only |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 99.09% | L5 | Prediction only |
| 7 | Migraine disorder | 99.06% | L4 | Preclinical mechanism plus a case report; flagged as a research question |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked indication (Prinzmetal angina). The most relevant literature is for **migraine disorder** (rank 7), the best-supported alternative. Most of it is preclinical, and several animal studies likely used isoflurane only as background anesthesia rather than as the treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Animal mechanistic study | Cephalalgia | Inhalational anesthetics inhibit cortical spreading depression, the correlate of migraine aura |
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case report | Braz J Anesthesiol | General anesthesia (propofol and isoflurane) used to treat status migrainosus |
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | Case report | Rev Bras Anestesiol | Portuguese-language entry of the same status migrainosus report |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Animal study | J Neurosci | Susceptibility of sensory cortex to spreading depolarizations |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Animal study | J Pharmacol Exp Ther | NMDA receptor antagonists affect cortical spreading depression, with potential for migraine |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | Animal study | J Headache Pain | Atogepant does not affect cortical spreading depression susceptibility in rats |

For **manic bipolar affective disorder** (rank 3), the evidence is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | Open-label comparison (12 patients) | Eur J Anaesthesiol | Burst-suppression isoflurane anesthesia and ECT both markedly improved severe treatment-refractory depression |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | Animal imaging study | Psychiatry Res | FDG-PET in a rat model of mania; isoflurane was used for anesthesia, not treatment |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | Case report | AANA J | Differential diagnosis of malignant hyperthermia; not evidence of efficacy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02231929 | ISOFLURANE USP | Not stated | Not stated |
| 02188856 | FORANE | Not stated | Not stated |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links to liver disease, gallbladder disease, hypotensive disorder, malignant hyperthermia of anesthesia, exercise-induced malignant hyperthermia, Duchenne muscular dystrophy, muscular dystrophy and Becker muscular dystrophy. These should be verified against the official product monograph.
- **Drug Interactions**: 38 interactions were identified. The only one rated Major is **epinephrine**. **Morphine** and **opium** are rated Moderate. The remaining interactions are of unknown severity, including atropine, hydrocortisone, mannitol, pantoprazole, omeprazole, vancomycin, simvastatin, ondansetron, metronidazole, metoclopramide, famotidine, acetylsalicylic acid and dexamethasone.

Official label warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, Prinzmetal angina, is supported only by the model score, with no trials or literature, and isoflurane's potential for coronary steal raises a possible safety concern. Isoflurane is also a hospital-administered inhaled anesthetic, which makes it a poor fit for chronic conditions such as Tourette syndrome, trichotillomania and dysthymic disorder. Migraine is the most credible lead, with preclinical support and case reports, but it remains a research question rather than a candidate for clinical development.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for the two Canadian licenses
- For Prinzmetal angina, any mechanistic or clinical evidence, including an assessment of coronary steal risk
- For migraine, a review of whether isoflurane or the other agents drove the effects seen in the animal studies, and a feasibility assessment for refractory, hospital-based use only
- Route and setting compatibility assessment, since it is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

