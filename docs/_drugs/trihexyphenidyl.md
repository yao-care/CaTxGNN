---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 940
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic drug of the antiparkinsonian class, and the Canadian licence records do not state its approved indication.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **0 clinical trials** and only **1 indirect publication** supporting this direction.
The mechanistic reasoning argues against benefit, so the prediction is on **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (drug class: anticholinergic antiparkinsonian agent) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (weak; the only publication does not study the drug) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trihexyphenidyl is a central muscarinic antagonist with preferential M1 activity. Detailed mechanism-of-action data are not available in the current dataset, so this description rests on its known drug class. Its established role is symptomatic relief of parkinsonian tremor and rigidity, and of dystonia.

The only link to ADHD is a speculative balance between the cholinergic and dopaminergic systems. Anticholinergics can impair attention and memory, which argues against benefit in a disorder defined by inattention. The single publication found concerns primary tic disorder with dystonia. In that setting the drug might treat the dystonia, not ADHD symptoms. The prediction for the "inattentive type" subtype (score 99.75%, no trials or literature) is probably a duplicate of the ADHD node and adds no independent support.

The TxGNN score is very high, but it is a model output and is not supported by clinical evidence here.

**Other predictions:** Of the top 10 predictions, only **PLA2G6-associated neurodegeneration** (score 99.58%) is flagged as a research question. This condition can present with dystonia and parkinsonism, so a symptomatic rationale is plausible. The two retrieved items are case-level reports, and drug use or response in them is not confirmed. The remaining predictions have no identifiable mechanistic link and are model output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohort | Movement Disorders | Large clinical series of patients with tics and persistent dystonia. It describes the prevalence and clinical features of this syndrome and does not evaluate trihexyphenidyl for ADHD. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 545074 | TRIHEXYPHENIDYL |
| 545058 | TRIHEXYPHENIDYL |

Dosage form and approved indication text are not listed for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

Pharmacology-based concerns raised in the prediction analysis:
- **Cognitive effects**: Anticholinergics can impair attention and memory, which is directly relevant to ADHD.
- **Ocular effects**: Mydriasis and cycloplegia are possible.
- **Seizure threshold**: Anticholinergics carry seizure-threshold concerns, which matters for epileptic conditions.

No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction has no registered trials and no direct drug evidence, and the known anticholinergic effects on attention and memory argue against benefit. The high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data, for example from the DrugBank API
- Evidence of trihexyphenidyl use or response in ADHD, if any exists
- For PLA2G6-associated neurodegeneration, confirmation of drug use and response in the reported cases, and a focused literature review of symptomatic dystonia or parkinsonism treatment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

