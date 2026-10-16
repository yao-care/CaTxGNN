---
layout: default
title: Clidinium
parent: Model Prediction Only (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clidinium: predicted new indication Peptic ulcer disease (evidence level L5). Approved use: Irritable bowel syndrome, Clostridium difficile colitis…"
---

# Clidinium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Clidinium: From Irritable Bowel Syndrome to Peptic Ulcer Disease

## One-Sentence Summary

Clidinium is an antimuscarinic (anticholinergic) drug originally used for gastrointestinal conditions such as irritable bowel syndrome and gastroenteritis.
The TxGNN model predicts it may be effective for **Peptic Ulcer Disease** (the highest-evidence candidate among the top 10 predictions), with **0 registered clinical trials** and **6 publications**, mostly old clinical reports of the clidinium–chlordiazepoxide combination.
Evidence is limited, and the top-ranked prediction (cauda equina syndrome) carries potential safety concerns.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome, Clostridium difficile colitis, enterocolitis, gastroenteritis (from the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Peptic ulcer disease (the top-ranked prediction by score is cauda equina syndrome, but it has no evidence and a safety concern; peptic ulcer disease is the best-supported prediction) |
| TxGNN Prediction Score | 99.83% (peptic ulcer disease); 99.93% (cauda equina syndrome, rank 1) |
| Evidence Level | L3 (peptic ulcer disease); L5 for the top-ranked prediction |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (research question for peptic ulcer disease) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on known pharmacology, clidinium is a quaternary antimuscarinic. It blocks muscarinic receptors in the gut, which reduces gastric acid secretion and smooth-muscle motility. Its efficacy in functional bowel disorders is the basis of its original use.

For **peptic ulcer disease**, this mechanism is plausible. Reduced acid secretion and gastric motility are classic targets of anticholinergic therapy. Clidinium is usually paired with the anxiolytic chlordiazepoxide (as in Librax), which may help with stress-related ulcer pathways. A 2016 study tested clidinium-C added to proton-pump-inhibitor triple therapy for *H. pylori* eradication. A 1978 mouse study found additive or supra-additive protection against stress-induced gastric erosion when benzodiazepines were combined with anticholinergics, including clidinium. However, PPIs and *H. pylori* eradication have largely replaced anticholinergics in ulcer care, so the added value is unclear.

Other predictions are weaker:
- **Cauda equina syndrome and neurogenic bladder:** Antimuscarinic blockade could reduce detrusor overactivity, but clidinium has no clinical data here. Anticholinergics may worsen urinary retention, and its quaternary structure limits systemic absorption.
- **Gastroduodenitis:** Plausible mechanism, but supported only by two 1960s combination reports.
- **Myasthenia gravis-related entries, autoimmune peripheral nervous system disease, and "disease of receptor activity":** No credible mechanism. These are likely graph-proximity artifacts, and anticholinergics may worsen myasthenia.
- **Large intestine disease:** Overlaps with the existing IBS indication and adds no new repurposing value.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Literature for the best-supported prediction (peptic ulcer disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27386057](https://pubmed.ncbi.nlm.nih.gov/27386057/) | 2016 | Clinical study (design to be verified) | Caspian J Intern Med | Clidinium-C added to a 14-day PPI-based triple therapy for *H. pylori* eradication; assessed eradication and side-effect prevention |
| [4892352](https://pubmed.ncbi.nlm.nih.gov/4892352/) | 1969 | Clinical evaluation | Br J Clin Pract | Clidinium with chlordiazepoxide ("Libraxin") in duodenal ulcer management |
| [14142206](https://pubmed.ncbi.nlm.nih.gov/14142206/) | 1964 | Clinical report | Rev Clin Esp | Chlordiazepoxide plus clidinium bromide in gastroduodenal ulcer |
| [14477958](https://pubmed.ncbi.nlm.nih.gov/14477958/) | 1962 | Clinical report | Hospital (Rio de Janeiro) | Preliminary note on clidinium bromide with chlordiazepoxide in gastroduodenal peptic ulcer |
| [14497768](https://pubmed.ncbi.nlm.nih.gov/14497768/) | 1962 | Clinical trial report | Minerva Med | Librax trials in several digestive tract diseases |
| [28539](https://pubmed.ncbi.nlm.nih.gov/28539/) | 1978 | Preclinical (mouse) | Pharmacology | Benzodiazepine plus anticholinergic (including clidinium) gave additive or supra-additive protection against stress-induced gastric erosion |

Additional literature for other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [345122](https://pubmed.ncbi.nlm.nih.gov/345122/) | 1978 | Physiological study (large intestine disease / IBS) | N Engl J Med | In 10 IBS patients, a single dose of clidinium bromide was studied against the exaggerated post-meal colonic myoelectrical and motor response; it did not affect colonic slow-wave frequency |

Most of this literature is old, non-randomized, and covers a fixed-dose combination, so the effect of clidinium alone cannot be isolated.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00115630 | LIBRAX | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): hypertension, gastric ulcer, anxiety and other psychiatric disorders (neurotic, dysthymic, psychotic, schizoaffective), porphyria, kidney disease, liver disease, gallbladder disease, benign prostatic hyperplasia, coronary artery disease, sleep apnea syndromes, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction diseases, and lung disease.
  - Myasthenia gravis and related conditions are flagged as contraindications, yet they appear among the predicted indications. These predictions should be treated as unsafe.
  - Gastric ulcer also appears in the contraindication list, which conflicts with the peptic ulcer prediction and needs clarification.
- **Drug Interactions** (100 interactions recorded; examples shown, mostly Moderate):
  - Other anticholinergics and antimuscarinics: hyoscyamine, aclidinium, amitriptyline
  - Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, hydrocodone, tramadol, loperamide, ethanol
  - Antihistamines and others: acrivastine, phenyltoloxamine, amantadine, phenylephrine, acebutolol, botulinum toxin type A, acetylcholine
  - Minor: acetaminophen, hydrochlorothiazide

Package insert warnings and contraindications from Health Canada have not yet been obtained. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The highest-scoring predictions (cauda equina syndrome, neurogenic bladder, myasthenia-related conditions) have no clinical evidence, and several raise safety concerns because anticholinergics can worsen urinary retention and neuromuscular weakness. The best-supported candidate, peptic ulcer disease (L3), rests mainly on 1960s combination reports and one 2016 study of uncertain design. PPIs and *H. pylori* eradication have largely superseded this approach. It is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Verification of the design and results of the 2016 *H. pylori* study (PMID 27386057)
- Resolution of the knowledge-graph conflict listing gastric ulcer as a contraindication
- Approved indication text, dosage form, and manufacturer for DIN 00115630
- Comparative evidence against current standard of care (PPIs) to establish incremental value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

