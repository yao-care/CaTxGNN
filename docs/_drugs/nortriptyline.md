---
layout: default
title: Nortriptyline
parent: High Evidence (L1-L2)
nav_order: 663
evidence_level: L2
indication_count: 2
---

# Nortriptyline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

# Nortriptyline: From Depression to Attention Deficit-Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant (TCA) that the literature describes as widely used for depression. The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**. No clinical trials are registered for this prediction, but **20 publications** support it, including a controlled study in children and adolescents and a Cochrane review of TCAs in ADHD.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (from the literature; the Canadian licence records list no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

A second predicted indication, *ADHD, inattentive type* (score 99.33%), has no trials or subtype-specific literature (Evidence Level L4, Hold). Its score most likely comes from the parent ADHD node in the knowledge graph.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Based on known pharmacology, nortriptyline inhibits norepinephrine reuptake and has weaker effects on serotonin. A PET study in patients with depression (PMID 24345533) describes it as a norepinephrine transporter (NET)-selective TCA. That study also notes that the NET matters in both depression and ADHD.

ADHD treatments with documented activity share a noradrenergic or dopaminergic action. Reviews list the more noradrenergic secondary-amine TCAs, desipramine and nortriptyline, among the established alternative treatments (PMID 15064003). Boosting noradrenaline in prefrontal circuits is also how the approved non-stimulant atomoxetine works, so the link is biologically plausible.

This mechanistic link rests on general pharmacology, not on the supplied record. Safety is the main limiting factor, as described in the safety section below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline's efficacy and tolerability in children and adolescents with ADHD (outcome data not in the supplied abstract) |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT | Pediatr Nephrol | Randomized double-blind trial of nortriptyline for enuresis in children with ADHD, assessing efficacy, tolerability and adverse effects |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Reviews TCAs as second-line treatment for ADHD symptoms in children and adolescents |
| [7807071](https://pubmed.ncbi.nlm.nih.gov/7807071/) | 1995 | Systematic assessment | J Nerv Ment Dis | Systematic assessment of TCAs in adult ADHD (no abstract supplied) |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Guideline | Ann Clin Psychiatry | CANMAT recommendations for managing mood disorders with comorbid ADHD |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Open-label cohort | J Am Acad Child Adolesc Psychiatry | Nortriptyline in children with ADHD and tic disorder or Tourette's syndrome, where stimulants can worsen tics |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | TCAs are established alternative ADHD treatments, but a narrow therapeutic index and cardiovascular toxicity limit their use |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opin Drug Saf | Safety review of non-stimulant ADHD agents; stimulants are first choice and atomoxetine is second-line |
| [8444754](https://pubmed.ncbi.nlm.nih.gov/8444754/) | 1993 | Retrospective study | J Am Acad Child Adolesc Psychiatry | Serum levels and ECG effects of nortriptyline in a large paediatric outpatient population |
| [24345533](https://pubmed.ncbi.nlm.nih.gov/24345533/) | 2014 | PET study | Int J Neuropsychopharmacol | Measured NET occupancy by nortriptyline in patients with depression |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 15237 | AVENTYL |
| 15229 | AVENTYL |

Dosage form and approved indication text are not listed in the supplied licence records.

---

## Safety Considerations

Please refer to the package insert for safety information. The Health Canada warnings, contraindications and drug-interaction data are not available in this record. The empty interaction result most likely reflects a data gap, not evidence of safety.

Class-level concerns for TCAs, based on general pharmacology and the literature above, include:
- Cardiac conduction effects (a retrospective study of ECG effects in young patients is listed above)
- Anticholinergic burden
- Toxicity in overdose, with a narrow therapeutic index
- The antidepressant suicidality warning in children and young adults

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature includes a controlled paediatric study and a Cochrane review, so evidence is at L2, and the noradrenergic mechanism is plausible. However, no clinical trials are registered, and the Health Canada safety information is missing, which blocks safety screening. TCAs also have cardiac and overdose risks, and non-stimulant alternatives such as atomoxetine exist.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, interactions) and the approved indication and dosage forms for the AVENTYL DINs
- Mechanism-of-action data from DrugBank
- Full-text appraisal of the controlled paediatric study (PMID 11052409) and the Cochrane review (PMID 25238582) to confirm effect size and tolerability
- A cardiac (ECG) and suicidality monitoring plan for paediatric and adolescent use
- Subtype-specific evidence before considering the inattentive-type indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

