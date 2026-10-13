---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Psychotic Disorders to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is a dopamine D2 antagonist antipsychotic, originally used for psychotic disorders, schizophrenia and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorders, schizophrenia and related conditions (schizophreniform and schizoaffective disorder), Tourette syndrome |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Haloperidol is a dopamine D2 receptor antagonist. Detailed mechanism of action data was not available in the data compiled for this report, so this description rests on the drug's well-established pharmacology. Its efficacy in psychotic disorders, schizophrenia and Tourette syndrome is long established.

For this prediction, **no mechanistic link could be identified**. Congenital disorders of glycosylation with defective fucosylation involve problems in fucose metabolism or transport (for example, GDP-fucose transport). Dopamine receptor blockade has no known connection to these pathways. The high score (0.999) reflects a pattern found by the model in a knowledge graph, not biological or clinical evidence. The similarity between the original and predicted indications has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Nine valid single-ingredient authorizations exist in Canada. Dosage form and approved indication text were not available for any of them. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 00363669 | TEVA-HALOPERIDOL |
| 00713449 | TEVA-HALOPERIDOL |
| 02366010 | HALOPERIDOL INJECTION |
| 00363677 | TEVA-HALOPERIDOL |
| 00363685 | TEVA-HALOPERIDOL |

The remaining four include other haloperidol injection products and a long-acting formulation (HALOPERIDOL LA).

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindications flagged in the knowledge graph (not label text)**:
  - Cardiac: long QT syndrome (including familial forms) and torsades de pointes.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm and neuroleptic malignant syndrome.
  - Blood: neutropenia (including congenital and idiopathic forms), agranulocytosis and leukopenia.
  - Other: liver disease, gallbladder disease, hypothyroidism and myxedema, potassium deficiency, hypotensive disorder and female breast carcinoma.
- **Drug Interactions**: 100 interactions are recorded. Major-level interactions include bupropion, morphine, clarithromycin and dolasetron. Moderate-level interactions include famotidine, epinephrine, hydrocortisone, amphotericin B, atropine, loperamide and aprepitant, among others.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanistic link between D2 antagonism and fucosylation defects. Haloperidol also carries significant safety considerations, including QT prolongation and neurological and haematological risks. These are hard to justify without any supporting evidence in a rare metabolic disease.

**Other predictions for this drug:**
Of the ten predictions compiled, the strongest evidence is for **manic bipolar affective disorder** (Level L1, recommendation: Proceed with Guardrails). It is supported by a completed Phase 3 haloperidol- and placebo-controlled olanzapine trial ([NCT00129220](https://clinicaltrials.gov/study/NCT00129220), n=224) and by network meta-analyses. Mania is already close to established clinical practice, so this is more of a guideline-supported use than a novel repurposing. Haloperidol's effects on retinal ganglion cells in a retinitis pigmentosa rat model (L4, preclinical only) are the only other signal of note.

**To proceed with the glycosylation indication, the following is needed:**
- Any mechanistic or preclinical evidence linking dopamine signalling to fucosylation pathways
- Detailed mechanism of action data and the full Health Canada package insert warnings and contraindications
- A disease-specific safety assessment, including QTc, neurological and haematological monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

