---
layout: default
title: Trihexyphenidyl
parent: Moderate Evidence (L3-L4)
nav_order: 947
evidence_level: L4
indication_count: 10
---

# Trihexyphenidyl
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Trihexyphenidyl: From Parkinson Disease to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic drug originally used to treat Parkinson disease and related movement disorders such as dystonia.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**,
but there are **no registered clinical trials** and only **1 publication** (a case series that does not test the drug in ADHD), so the prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related movement disorders (parkinsonism, dystonia, blepharospasm). No approved indication text is available for the Canadian licences. |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, trihexyphenidyl is a central muscarinic antagonist with a preference for the M1 receptor. It modulates the balance between cholinergic and dopaminergic signalling in the striatum, which is why it relieves tremor, rigidity and dystonia.

ADHD involves dopaminergic and noradrenergic dysregulation in frontostriatal circuits, so a theoretical link to a drug that acts on striatal neurotransmitter balance exists. This is the likely basis of the model's prediction.

However, this link is weak. Anticholinergic drugs can impair attention, memory and cognition, which argues against benefit and raises the possibility of harm in ADHD. The only linked publication describes tic disorder with dystonia, a related movement phenotype, and is not evidence of ADHD treatment. The very high score is a computational output and is not supported by clinical data.

Other predictions in the same list include the inattentive subtype of ADHD (99.75%), PLA2G6-associated neurodegeneration (99.58%), Rasmussen encephalitis, myelitis and several rare genetic syndromes. Among these, only PLA2G6-associated neurodegeneration has a plausible symptomatic rationale, because it includes dystonia-parkinsonism phenotypes. It is still supported only by a single case report that does not examine trihexyphenidyl.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series | Movement Disorders | Clinical series describing patients with tic disorder and persistent dystonia. It characterises the syndrome and does not evaluate trihexyphenidyl or ADHD treatment. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00545074 | TRIHEXYPHENIDYL | Not specified | Not specified |
| 00545058 | TRIHEXYPHENIDYL | Not specified | Not specified |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not from label text)**: The knowledge graph links trihexyphenidyl to contraindication or caution in the following conditions:
  - Eye: angle-closure (closed-angle) glaucoma and open-angle glaucoma
  - Urinary and prostate: benign prostatic hyperplasia
  - Gastrointestinal: paralytic ileus, achalasia and megaesophagus, hiatus hernia, ulcerative colitis and inflammatory bowel disease, gastric ulcer, *Clostridium difficile* colitis, necrotizing enterocolitis
  - Cardiovascular: hypertension, hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Respiratory, liver and kidney: COPD, liver disease, gallbladder disease, kidney disease
- **Drug Interactions**: 100 interactions were identified in total. The main ones are:
  - **Major**: potassium chloride and potassium citrate
  - **Moderate**: other anticholinergic or antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate), opioids and related drugs (morphine, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), drugs affecting gut motility (metoclopramide, prucalopride, pramlintide), and magnesium hydroxide

Because the compiled data contains no label warnings, please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for ADHD has no clinical trial support and only one tangentially related case series. The pharmacology also argues against benefit, because anticholinergics can worsen attention and cognition. The high TxGNN score alone is not sufficient to justify progression.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Targeted literature review of anticholinergic effects on attention and cognition in ADHD and in children
- If any repurposing direction is pursued, consider the PLA2G6-associated dystonia-parkinsonism indication as a better-justified research question, since it overlaps with the drug's existing symptomatic uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

