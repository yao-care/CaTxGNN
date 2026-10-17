---
layout: default
title: Ephedrine
parent: Moderate Evidence (L3-L4)
nav_order: 335
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Ephedrine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, bronchitis, pharyngitis…"
monitor_inn: "Ephedrine"
predicted_indications: ["trigeminal autonomic cephalalgia"]
---

# Ephedrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Ephedrine: From Allergic Rhinitis to Nasal Cavity Disease

## One-Sentence Summary

Ephedrine is a sympathomimetic originally used for upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, bronchitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the support is thin: **no registered clinical trials** and only **2 older, low-tier publications**. This prediction is largely a restatement of its existing rhinitis-related uses rather than a clearly novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, bronchitis, pharyngitis, common cold and others (from the knowledge graph; no indication text in the Canadian licence record) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ephedrine is a sympathomimetic with alpha-adrenergic agonist activity and indirect norepinephrine release. This causes vasoconstriction of the nasal mucosa and decongestion.

"Nasal cavity disease" is a broad term that overlaps heavily with ephedrine's existing indications (rhinitis, vasomotor rhinitis, nasopharyngitis). The high TxGNN score (0.999) is consistent with this overlap. Because the term is largely redundant with established uses, it should be viewed as a research question rather than a genuinely new indication.

Two other predictions were also generated, both with weaker support:
- **Acute laryngopharyngitis** (score 99.90%, Evidence Level L5): the decongestant effect could in theory reduce upper airway swelling, but no trials or literature were found. The condition is mostly self-limited, and the benefit of a systemic sympathomimetic is unestablished.
- **Trigeminal autonomic cephalalgia** (score 99.34%, Evidence Level L5): the link is indirect and no mechanistic or clinical evidence was found. Ephedrine's cardiovascular stimulation (hypertension, tachycardia) is also a safety concern in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Clinical study | Svenska lakartidningen | Experimental clinical testing of N-hydroxyethylpromethazine chloride (Aprobit) combined with ephedrine hydrochloride in the nasal cavity; no abstract available |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Preliminary clinical observation | Zhongguo Zhong xi yi jie he za zhi | Preliminary observation of a rhinitis spray in chronic rhinitis; the formulation composition is not confirmed from the title |

Both publications are low-tier and not clearly attributable to ephedrine alone.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00876534 | EPHEDRINE SULFATE INJECTION USP | Not specified | Not specified |

---

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (these come from a knowledge graph, not from label text):
  - Cardiovascular: hypertension, hypertensive disorder, congestive heart failure
  - Respiratory: chronic obstructive pulmonary disease (including severe early-onset COPD)
  - Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
  - Hepatic, renal, biliary and pancreatic: liver failure, liver disease, kidney disease, pyoureter, gallbladder disease, pancreatitis
  - Gastrointestinal: gastric ulcer, peptic ulcer disease, inflammatory bowel disease
  - Endocrine and metabolic: hypothyroidism, myxedema, congenital hypothyroidism, porphyria (including inherited porphyria and porphyrin metabolism disease)
  - Other: thrombocytopenia, open-angle glaucoma
- **Drug Interactions**: 100 interactions were identified, of which 20 are listed in the data compiled for this report. Major-level interactions include:
  - Tramadol
  - Amitriptyline
  - Bupropion
  - Methylene blue

  Moderate-level interactions include:
  - Beta-blockers (acebutolol, atenolol)
  - Beta-agonists (formoterol, salbutamol, arformoterol)
  - Stimulants (methylphenidate, amphetamine, atomoxetine)
  - Antidiabetic agents (metformin, acarbose, alogliptin, albiglutide)

  Morphine and ascorbic acid have minor interactions.

Package insert warnings and contraindications for the Canadian product were not available. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and two old, low-tier publications, with no registered trials. "Nasal cavity disease" largely duplicates existing rhinitis-related uses, so it is not a clearly novel repurposing opportunity. The only Canadian product is an injection, which is not an obvious fit for nasal conditions. Many knowledge-graph contraindications (especially cardiovascular) also call for caution.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A more specific disease definition, to separate genuinely new uses from existing rhinitis-related indications
- Route and formulation compatibility assessment (an injectable product versus nasal or oral delivery)
- Higher-quality clinical evidence, such as controlled trials of ephedrine alone in a defined nasal condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

