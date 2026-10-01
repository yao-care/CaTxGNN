---
layout: default
title: Clomipramine
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Clomipramine
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

# Clomipramine: From Depression and Obsessive-Compulsive Disorder to Anxiety Disorder

## One-Sentence Summary

Clomipramine is a tricyclic antidepressant, best known for treating obsessive-compulsive disorder (OCD) and depression. The Canadian label text was not available in the Evidence Pack, so these original uses come from the retrieved literature.
The TxGNN model predicts it may be effective for **anxiety disorder**, with **19 registered clinical trials** and **20 publications** retrieved. Most of this evidence concerns OCD and panic disorder rather than anxiety disorder as a whole, so the support is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression and OCD (from literature; Canadian label text not provided) |
| Predicted New Indication | Anxiety disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 (as assigned in the Evidence Pack; evidence is indirect, see below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clomipramine is a potent serotonin reuptake inhibitor. Its metabolite, desmethylclomipramine, adds noradrenaline reuptake inhibition. This dual serotonergic and noradrenergic action supports both anxiolytic and anti-obsessional effects. Detailed mechanism-of-action data were not available from DrugBank in this Evidence Pack, so this description comes from the pack's own rationale.

The prediction is partly a matter of classification. Most retrieved trials and papers concern OCD, panic disorder (with or without agoraphobia) and separation anxiety, not anxiety disorder as a whole. The high score may partly reflect the disease ontology grouping OCD and panic under "anxiety". Clomipramine is already established for OCD in many jurisdictions, so this is not a novel repurposing signal.

The strongest supporting evidence is in panic disorder. Several double-blind studies and a 2023 Cochrane network meta-analysis include clomipramine, and older reviews describe tricyclics such as clomipramine as effective for panic disorder and agoraphobia.

---

## Clinical Trial Evidence

19 trials were retrieved. The 10 most relevant are listed below. Only a few test clomipramine directly, and none is a completed Phase 3 trial of clomipramine in anxiety disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unknown | 76 | Randomized comparison of intravenous vs oral clomipramine in OCD (direct drug evidence, but OCD) |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind augmentation in OCD non-responders: fluoxetine alone vs fluoxetine + quetiapine vs fluoxetine + clomipramine |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Open trial of quetiapine vs clomipramine augmentation of SSRIs in OCD (small sample) |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicting response to clomipramine vs escitalopram in OCD (indirect, small) |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Completed | 44 | Quetiapine vs placebo added to SSRI/clomipramine in OCD (clomipramine as background therapy) |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT added to serotonin reuptake inhibitor treatment in children with OCD |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | N/A | Completed | 144 | Adaptive treatment strategies for children and adolescents with psychiatric disorders, including OCD pharmacotherapy |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Adjunctive troriluzole in OCD with inadequate response to SSRI or clomipramine (clomipramine is only background) |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Pharmacovigilance of psychotropic drugs in elderly psychiatric inpatients (not indication-specific) |
| [NCT05952713](https://clinicaltrials.gov/study/NCT05952713) | N/A | Completed | 73,336 | Real-world comparison of 15 antidepressants in major depressive disorder (relevant to the depression side, not anxiety) |

---

## Literature Evidence

20 publications were retrieved. The 10 most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Pharmacological treatments for panic disorder in adults |
| [41978943](https://pubmed.ncbi.nlm.nih.gov/41978943/) | 2026 | Systematic review/meta-analysis | Acta Neuropsychiatrica | Parenteral vs oral clomipramine for depression or OCD |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Meta-analysis | J Am Acad Child Adolesc Psychiatry | Early treatment responses to SSRIs and clomipramine in pediatric OCD |
| [10066007](https://pubmed.ncbi.nlm.nih.gov/10066007/) | 1999 | RCT | Acta Psychiatr Scand | 180 panic disorder patients: low and high dose clomipramine vs placebo over 8 weeks; both doses more effective than placebo |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine and cognitive therapy in panic disorder |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | Eur Arch Psychiatry Clin Neurosci | Double-blind comparison of moclobemide vs clomipramine 150 mg/day in panic disorder (135 patients randomized) |
| [9585709](https://pubmed.ncbi.nlm.nih.gov/9585709/) | 1998 | RCT | Am J Psychiatry | Aerobic exercise vs clomipramine vs placebo in panic disorder |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | Meta-analysis | J Behav Ther Exp Psychiatry | Clomipramine, fluoxetine and behavior therapy for OCD (25 studies); all three effective |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | Pharmacology of clomipramine and its use in OCD and panic disorder |
| [22204483](https://pubmed.ncbi.nlm.nih.gov/22204483/) | 2012 | Review | Curr Top Med Chem | Treatment strategies for OCD and panic disorder/agoraphobia |

---

## Canada Market Information

Dosage form and approved-indication text were not provided for these licenses.

| DIN | Product Name |
|---------|------|
| 2497514 | TARO-CLOMIPRAMINE |
| 2497506 | TARO-CLOMIPRAMINE |
| 324019 | ANAFRANIL |
| 402591 | ANAFRANIL |
| 330566 | ANAFRANIL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clomipramine has a plausible mechanism and randomized evidence in panic disorder and OCD, and it is marketed in Canada. However, the evidence for anxiety disorder as a whole is indirect. There are no completed Phase 3 trials of clomipramine in anxiety disorder, and the high score partly reflects how OCD and panic are grouped under anxiety.

**To proceed, the following is needed:**
- Health Canada product monograph (approved indications, warnings, contraindications), since safety screening cannot proceed without it.
- DrugBank mechanism-of-action data to confirm the mechanistic link.
- Clarification of which anxiety subtype is targeted (panic disorder, generalized anxiety or OCD), followed by trials specific to that subtype.
- A safety plan for tricyclic-class risks: cardiotoxicity, anticholinergic burden, overdose lethality, and suicidality warnings in young patients.

**Other predictions:** Major depressive disorder also reaches L2 with "Proceed with Guardrails", but it falls within clomipramine's established use. Agoraphobia and endogenous depression are research questions. The remaining predictions (benign paroxysmal torticollis of infancy, the four personality disorders and ADHD) are on Hold, with no supporting evidence or with adverse-effect signals only.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

